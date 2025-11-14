#@+leo-ver=4-thin
#@+node:AGP.20250415230112.329:@thin leoCommands.py
#@@language python
#@@tabwidth -4
#@@pagewidth 80

from __future__ import generators # To make the code work in Python 2.2.


#@<< imports >>
#@+node:AGP.20250415230112.330:<< imports  >> (leoCommands)
import leoGlobals as g

import leoAtFile
import leoConfig
import leoEditCommands
import leoFileCommands
import leoKeys
import leoImport
import leoNodes
import leoTangle
import leoUndo

import compiler # for Check Python command
import keyword
import os
import parser # needed only for weird Python 2.2 parser errors.
import string

subprocess = g.importExtension('subprocess',None,verbose=False)

import sys
import tempfile
import time

import tabnanny # for Check Python command
import tokenize # for Check Python command
import Tkinter as Tk

# The following import _is_ used.
import token    # for Check Python command
#@-node:AGP.20250415230112.330:<< imports  >> (leoCommands)
#@nl

#@+others
#@+node:AGP.20250415230112.331:class commands
class baseCommands:
    """The base class for Leo's main commander."""
    #@    @+others
    #@+node:AGP.20250415230112.332: c.Birth & death
    #@+node:AGP.20250415230112.333:c.__init__
    def __init__(self,frame,fileName):
    
        g.c = c = self
        
        # g.trace('Commands')
        
        c.exists = True # Indicate that this class exists and has not been destroyed.
            # Do this early in the startup process so we can call hooks.
        
        self.frame = frame
        self.mFileName = fileName
            # Do _not_ use os_path_norm: it converts an empty path to '.' (!!)
    
        # g.trace(c) # Do this after setting c.mFileName.
        c.initIvars()
    
        self.useTextMinibuffer = c.config.getBool('useTextMinibuffer')
        self.showMinibuffer = c.config.getBool('useMinibuffer')
        self.stayInTree = c.config.getBool('stayInTreeAfterSelect')
    
        # initialize the sub-commanders.
        # c.finishCreate creates the sub-commanders for edit commands.
        self.fileCommands   = leoFileCommands.fileCommands(c)
        self.atFileCommands = leoAtFile.atFile(c)
        self.importCommands = leoImport.leoImportCommands(c)
        self.tangleCommands = leoTangle.tangleCommands(c)
        leoEditCommands.createEditCommanders(c)
    
        if 0 and g.debugGC:
            print ; print "*** using Null undoer ***" ; print
            self.undoer = leoUndo.nullUndoer(self)
        else:
            self.undoer = leoUndo.undoer(self)
    #@-node:AGP.20250415230112.333:c.__init__
    #@+node:AGP.20250415230112.334:c.initIvars
    def initIvars(self):
    
        c = self
        #@    << initialize ivars >>
        #@+node:AGP.20250415230112.335:<< initialize ivars >> (commands)
        self._currentPosition = self.nullPosition()
        self._rootPosition    = self.nullPosition()
        self._topPosition     = self.nullPosition()
        
        # Delayed focus.
        self.doubleClickFlag = False
        self.hasFocusWidget = None
        self.requestedFocusWidget = None
        
        # Official ivars.
        self.gui = g.app.gui
        
        # Interlocks to prevent premature closing of a window.
        self.inCommand = False
        self.requestCloseWindow = False
        
        # For emacs/vim key handling.
        self.commandsDict = None
        self.keyHandler = self.k = None
        self.miniBufferWidget = None
        
        # per-document info...
        self.disableCommandsMessage = ''
            # The presence of this message disables all commands.
        self.hookFunction = None
        self.openDirectory = None
        
        self.expansionLevel = 0  # The expansion level of this outline.
        self.expansionNode = None # The last node we expanded or contracted.
        self.changed = False # True if any data has been changed since the last save.
        self.loading = False # True if we are loading a file: disables c.setChanged()
        self.outlineToNowebDefaultFileName = "noweb.nw" # For Outline To Noweb dialog.
        self.promptingForClose = False # To lock out additional closing dialogs.
        
        # For tangle/untangle
        self.tangle_errors = 0
        
        # Global options
        self.page_width = 132
        self.tab_width = -4
        self.tangle_batch_flag = False
        self.untangle_batch_flag = False
        
        # Default Tangle options
        self.tangle_directory = ""
        self.use_header_flag = False
        self.output_doc_flag = False
        
        # Default Target Language
        self.target_language = "python" # Required if leoConfig.txt does not exist.
        
        # These are defined here, and updated by the tree.select()
        self.beadList = [] # list of vnodes for the Back and Forward commands.
        self.beadPointer = -1 # present item in the list.
        self.visitedList = [] # list of positions for the Nodes dialog.
        
        # For hoist/dehoist commands.
        self.hoistStack = []
            # Stack of nodes to be root of drawn tree.
            # Affects drawing routines and find commands.
        self.recentFiles = [] # List of recent files
        
        # For outline navigation.
        self.navPrefix = '' # Must always be a string.
        self.navTime = None
        #@-node:AGP.20250415230112.335:<< initialize ivars >> (commands)
        #@nl
        self.config = configSettings(c)
        g.app.config.setIvarsFromSettings(c)
    #@-node:AGP.20250415230112.334:c.initIvars
    #@+node:AGP.20250415230112.336:c.__repr__ & __str__
    def __repr__ (self):
        
        return "Commander %d: %s" % (id(self),repr(self.mFileName))
            
    __str__ = __repr__
    #@-node:AGP.20250415230112.336:c.__repr__ & __str__
    #@+node:AGP.20250415230112.337:c.hash
    def hash (self):
    
        c = self
        if c.mFileName:
            return g.os_path_abspath(c.mFileName).lower()
        else:
            return 0
    #@-node:AGP.20250415230112.337:c.hash
    #@+node:AGP.20250415230112.338:c.finishCreate & helper
    def finishCreate (self):  # New in 4.4.
        
        '''Finish creating the commander after frame.finishCreate.
        
        Important: this is the last step in the startup process.'''
        
        c = self ; p = c.currentPosition()
        c.miniBufferWidget = c.frame.miniBufferWidget
        # g.trace('Commands',c.fileName()) # g.callers())
        
        # Create a keyHandler even if there is no miniBuffer.
        c.keyHandler = c.k = k = leoKeys.keyHandlerClass(c,
            useGlobalKillbuffer=True,
            useGlobalRegisters=True)
    
        if g.app.config and g.app.config.inited:
            # A 'real' .leo file.
            c.commandsDict = leoEditCommands.finishCreateEditCommanders(c)
            k.finishCreate()
        else:
            # A leoSettings.leo file.
            c.commandsDict = {}
    
        # Create the menu last so that we can use the key handler for shortcuts.
        if not g.doHook("menu1",c=c,p=p,v=p):
            c.frame.menu.createMenuBar(c.frame)
            
        c.bodyWantsFocusNow()
    #@+node:AGP.20250415230112.339:printCommandsDict
    def printCommandsDict (self):
        
        c = self
        
        print 'Commands...'
        keys = c.commandsDict.keys()
        keys.sort()
        for key in keys:
            command = c.commandsDict.get(key)
            print '%30s = %s' % (key,g.choose(command,command.__name__,'<None>'))
        print
    #@-node:AGP.20250415230112.339:printCommandsDict
    #@-node:AGP.20250415230112.338:c.finishCreate & helper
    #@-node:AGP.20250415230112.332: c.Birth & death
    #@+node:AGP.20250415230112.340: doCommand
    command_count = 0
    
    def doCommand (self,command,label,event=None):
    
        """Execute the given command, invoking hooks and catching exceptions.
        
        The code assumes that the "command1" hook has completely handled the command if
        g.doHook("command1") returns False.
        This provides a simple mechanism for overriding commands."""
        
        c = self ; p = c.currentPosition()
        commandName = command and command.__name__
        c.setLog()
    
        self.command_count += 1
        if not g.app.unitTesting and c.config.getBool('trace_doCommand'):
            g.trace(commandName)
    
        # The presence of this message disables all commands.
        if c.disableCommandsMessage:
            g.es(c.disableCommandsMessage,color='blue')
            return 'break' # Inhibit all other handlers.
    
        if label and event is None: # Do this only for legacy commands.
            if label == "cantredo": label = "redo"
            if label == "cantundo": label = "undo"
            g.app.commandName = label
    
        if not g.doHook("command1",c=c,p=p,v=p,label=label):
            try:
                c.inCommand = True
                val = command(event)
                c.inCommand = False
                if c and c.exists: # Be careful: the command could destroy c.
                    c.k.funcReturn = val
            except:
                c.inCommand = False
                if g.app.unitTesting:
                    raise
                else:
                    g.es("exception executing command")
                    print "exception executing command"
                    g.es_exception(c=c)
                    if c and c.exists and hasattr(c,'frame'):
                        c.redraw_now()
                        
            if c and c.exists and c.requestCloseWindow:
                g.trace('Closing window after command')
                c.requestCloseWindow = False
                g.app.closeLeoWindow(c.frame)
    
        # Be careful: the command could destroy c.
        if c and c.exists:
            p = c.currentPosition()
            g.doHook("command2",c=c,p=p,v=p,label=label)
                
        return "break" # Inhibit all other handlers.
    #@-node:AGP.20250415230112.340: doCommand
    #@+node:AGP.20250415230112.341: version & signon stuff
    #@+node:AGP.20250415230112.342:getBuildNumber
    def getBuildNumber(self):
        c = self
        return c.ver[10:-1] # Strip off "(dollar)Revision" and the trailing "$"
    #@-node:AGP.20250415230112.342:getBuildNumber
    #@+node:AGP.20250415230112.343:getSignOnLine (Contains hard-coded version info)
    def getSignOnLine (self):
        c = self
        return "LeoX 2020"
    #@-node:AGP.20250415230112.343:getSignOnLine (Contains hard-coded version info)
    #@+node:AGP.20250415230112.344:initVersion
    def initVersion (self):
        c = self
        c.ver = "$Revision: 1.83 $" # CVS updates this.
    #@-node:AGP.20250415230112.344:initVersion
    #@+node:AGP.20250415230112.345:c.signOnWithVersion
    def signOnWithVersion (self):
    
        c = self
        color = g.theme['error']#c.config.getColor("log_error_color")
        signon = c.getSignOnLine()
        n1,n2,n3,junk,junk=sys.version_info
        tkLevel = c.frame.top.getvar("tk_patchLevel")
        
        if sys.platform.startswith('win'):
            version = 'Windows '
            try:
                v = os.sys.getwindowsversion()
                version += ', '.join([str(z) for z in v])
            except Exception:
                pass
                
        else: version = sys.platform
        
        g.es("Leo Log Window...",color=color)
        g.es(signon)
        g.es("Python %d.%d.%d, Tk %s\n%s" % (n1,n2,n3,tkLevel,version))
        g.enl()
    #@-node:AGP.20250415230112.345:c.signOnWithVersion
    #@-node:AGP.20250415230112.341: version & signon stuff
    #@+node:AGP.20250415230112.346:c.iterators
    #@+node:AGP.20250415230112.347:c.all_positions_iter == allNodes_iter
    # New in Leo 4.4.2 (It used to be defined in terms of p.allNodes_iter.)
    
    class allNodes_iter_class:
    
        """Returns a list of positions in the entire outline."""
    
        #@    @+others
        #@+node:AGP.20250415230112.348:__init__ & __iter__ (p.allNodesIter)
        def __init__(self,c,copy):
            
            # g.trace('c.allNodes_iter.__init','p',p,'c',c)
        
            self.c = c
            self.first = c.rootPosition()
            self.p = None
            self.copy = copy
            
        def __iter__(self):
        
            return self
        #@-node:AGP.20250415230112.348:__init__ & __iter__ (p.allNodesIter)
        #@+node:AGP.20250415230112.349:next
        def next(self):
            
            if self.first:
                self.p = self.first
                self.first = None
        
            elif self.p:
                self.p.moveToThreadNext()
        
            if self.p:
                if self.copy: return self.p.copy()
                else:         return self.p
            else: raise StopIteration
        #@-node:AGP.20250415230112.349:next
        #@-others
    
    def allNodes_iter (self,copy=False):
        
        c = self
        return self.allNodes_iter_class(c,copy)
    
    all_positions_iter = allNodes_iter
    #@nonl
    #@-node:AGP.20250415230112.347:c.all_positions_iter == allNodes_iter
    #@+node:AGP.20250415230112.350:c.all_tnodes_iter
    def all_tnodes_iter(self):
        
        c = self
        for p in c.all_positions_iter():
            yield p.v.t
    
        # return c.rootPosition().all_tnodes_iter(all=True)
    #@-node:AGP.20250415230112.350:c.all_tnodes_iter
    #@+node:AGP.20250415230112.351:c.all_unique_tnodes_iter
    def all_unique_tnodes_iter(self):
        
        c = self ; marks = {}
        
        for p in c.all_positions_iter():
            if not p.v.t in marks:
                marks[p.v.t] = p.v.t
                yield p.v.t
    #@-node:AGP.20250415230112.351:c.all_unique_tnodes_iter
    #@+node:AGP.20250415230112.352:c.all_vnodes_iter
    def all_vnodes_iter(self):
        
        c = self
        for p in c.all_positions_iter():
            yield p.v
    #@-node:AGP.20250415230112.352:c.all_vnodes_iter
    #@+node:AGP.20250415230112.353:c.all_unique_vnodes_iter
    def all_unique_vnodes_iter(self):
        
        c = self ; marks = {}
        for p in c.all_positions_iter():
            if not p.v in marks:
                marks[p.v] = p.v
                yield p.v
    #@-node:AGP.20250415230112.353:c.all_unique_vnodes_iter
    #@-node:AGP.20250415230112.346:c.iterators
    #@+node:AGP.20250415230112.354:c.executeMinibufferCommand
    def executeMinibufferCommand (self,commandName):
        
        c = self ; k = c.k
        
        func = c.commandsDict.get(commandName)
        
        if func:
            event = g.Bunch(char='',keysym=None,widget=c.frame.body.bodyCtrl)
            stroke = None
            k.masterCommand(event,func,stroke)
            return k.funcReturn
        else:
            g.trace('no such command: %s' % (commandName),color='red')
            return None
    #@-node:AGP.20250415230112.354:c.executeMinibufferCommand
    #@+node:AGP.20250415230112.355:Command handlers...
    #@+node:AGP.20250415230112.356:File Menu
    #@+node:AGP.20250415230112.357:top level (file menu)
    #@+node:AGP.20250415230112.358:new
    def new (self,event=None):
        
        '''Create a new Leo window.'''
    
        c,frame = g.app.newLeoCommanderAndFrame(fileName=None)
        
        # Needed for plugins.
        g.doHook("new",old_c=self,c=c,new_c=c)
        # Use the config params to set the size and location of the window.
        c.beginUpdate()
        try:
            #frame.setInitialWindowGeometry()
            #frame.deiconify()
            #frame.lift()
            
            #print "new"
            #frame.resizePanesToRatio(frame.ratio,frame.secondary_ratio) # Resize the _new_ frame.
            
            
            
            t = leoNodes.tnode()
            v = leoNodes.vnode(t)
            p = leoNodes.position(v,[])
            v.initHeadString("NewHeadline")
            v.moveToRoot(oldRoot=None)
            c.setRootVnode(v) # New in Leo 4.4.2.
            c.editPosition(p)
        finally:
            c.endUpdate()
            if c.config.getBool('outline_pane_has_initial_focus'):
                c.treeWantsFocusNow()
            else:
                c.bodyWantsFocusNow()
                
        frame.show()
        
        return c # For unit test.
    #@-node:AGP.20250415230112.358:new
    #@+node:AGP.20250415230112.359:open
    def open (self,event=None):
        
        '''Open a Leo window containing the contents of a .leo file.'''
    
        c = self
        #@    << Set closeFlag if the only open window is empty >>
        #@+node:AGP.20250415230112.360:<< Set closeFlag if the only open window is empty >>
        #@+at 
        #@nonl
        # If this is the only open window was opened when the app started, and 
        # the window has never been written to or saved, then we will 
        # automatically close that window if this open command completes 
        # successfully.
        #@-at
        #@@c
            
        closeFlag = (
            c.frame.startupWindow and # The window was open on startup
            not c.changed and not c.frame.saved and # The window has never been changed
            g.app.numberOfWindows == 1) # Only one untitled window has ever been opened
        #@-node:AGP.20250415230112.360:<< Set closeFlag if the only open window is empty >>
        #@nl
    
        fileName = g.app.gui.runOpenFileDialog(
            title = "Open",
            filetypes = [("Leox files","*.leox"),("Leo files","*.leo"), ("All files","*")],
            defaultextension = ".leox")
        c.bringToFront()
    
        ok = False
        if fileName and len(fileName) > 0:
            ok, frame = g.openWithFileName(fileName,c)
            if ok:
                g.setGlobalOpenDir(fileName)
            if ok and closeFlag:
                g.app.destroyWindow(c.frame)
                
        
                
        # openWithFileName sets focus if ok.
        if not ok:
            if c.config.getBool('outline_pane_has_initial_focus'):
                c.treeWantsFocusNow()
            else:
                c.bodyWantsFocusNow()
        
    #@nonl
    #@-node:AGP.20250415230112.359:open
    #@+node:AGP.20250415230112.361:openWith and allies
    def openWith(self,event=None,data=None):
    
        """This routine handles the items in the Open With... menu.
    
        These items can only be created by createOpenWithMenuFromTable().
        Typically this would be done from the "open2" hook.
        
        New in 4.3: The "os.spawnv" now works. You may specify arguments to spawnv
        using a list, e.g.:
            
        openWith("os.spawnv", ["c:/prog.exe","--parm1","frog","--switch2"], None)
        """
        
        c = self ; p = c.currentPosition()
        n = data and len(data) or 0
        if n != 3:
            g.trace('bad data, length must be 3, got %d' % n)
            return
        try:
            openType,arg,ext=data
            if not g.doHook("openwith1",c=c,p=p,v=p.v,openType=openType,arg=arg,ext=ext):
                g.enableIdleTimeHook(idleTimeDelay=100)
                #@            << set ext based on the present language >>
                #@+node:AGP.20250415230112.362:<< set ext based on the present language >>
                if not ext:
                    theDict = g.scanDirectives(c)
                    language = theDict.get("language")
                    ext = g.app.language_extension_dict.get(language)
                    # print language,ext
                    if ext == None:
                        ext = "txt"
                    
                if ext[0] != ".":
                    ext = "."+ext
                    
                # print "ext",ext
                #@-node:AGP.20250415230112.362:<< set ext based on the present language >>
                #@nl
                #@            << create or reopen temp file, testing for conflicting changes >>
                #@+node:AGP.20250415230112.363:<< create or reopen temp file, testing for conflicting changes >>
                theDict = None ; path = None
                #@<< set dict and path if a temp file already refers to p.v.t >>
                #@+node:AGP.20250415230112.364:<<set dict and path if a temp file already refers to p.v.t >>
                searchPath = c.openWithTempFilePath(p,ext)
                
                if g.os_path_exists(searchPath):
                    for theDict in g.app.openWithFiles:
                        if p.v == theDict.get('v') and searchPath == theDict.get("path"):
                            path = searchPath
                            break
                #@-node:AGP.20250415230112.364:<<set dict and path if a temp file already refers to p.v.t >>
                #@nl
                if path:
                    #@    << create or recreate temp file as needed >>
                    #@+node:AGP.20250415230112.365:<< create or recreate temp file as needed >>
                    #@+at 
                    #@nonl
                    # We test for changes in both p and the temp file:
                    # 
                    # - If only p's body text has changed, we recreate the 
                    # temp file.
                    # - If only the temp file has changed, do nothing here.
                    # - If both have changed we must prompt the user to see 
                    # which code to use.
                    #@-at
                    #@@c
                    
                    encoding = theDict.get("encoding")
                    old_body = theDict.get("body")
                    new_body = p.bodyString()
                    new_body = g.toEncodedString(new_body,encoding,reportErrors=True)
                    
                    old_time = theDict.get("time")
                    try:
                        new_time = g.os_path_getmtime(path)
                    except:
                        new_time = None
                        
                    body_changed = old_body != new_body
                    temp_changed = old_time != new_time
                    
                    if body_changed and temp_changed:
                        #@    << Raise dialog about conflict and set result >>
                        #@+node:AGP.20250415230112.366:<< Raise dialog about conflict and set result >>
                        message = (
                            "Conflicting changes in outline and temp file\n\n" +
                            "Do you want to use the code in the outline or the temp file?\n\n")
                        
                        result = g.app.gui.runAskYesNoCancelDialog(c,
                            "Conflict!", message,
                            yesMessage = "Outline",
                            noMessage = "File",
                            defaultButton = "Cancel")
                        #@-node:AGP.20250415230112.366:<< Raise dialog about conflict and set result >>
                        #@nl
                        if result == "cancel": return
                        rewrite = result == "outline"
                    else:
                        rewrite = body_changed
                            
                    if rewrite:
                        path = c.createOpenWithTempFile(p,ext)
                    else:
                        g.es("reopening: " + g.shortFileName(path),color="blue")
                    #@-node:AGP.20250415230112.365:<< create or recreate temp file as needed >>
                    #@nl
                else:
                    path = c.createOpenWithTempFile(p,ext)
                
                if not path:
                    return # An error has occured.
                #@-node:AGP.20250415230112.363:<< create or reopen temp file, testing for conflicting changes >>
                #@nl
                #@            << execute a command to open path in external editor >>
                #@+node:AGP.20250415230112.367:<< execute a command to open path in external editor >>
                try:
                    if arg == None: arg = ""
                    shortPath = path # g.shortFileName(path)
                    if openType == "os.system":
                        if 1:
                            # This works, _provided_ that arg does not contain blanks.  Sheesh.
                            command = 'os.system(%s)' % (arg+shortPath)
                            os.system(arg+shortPath)
                        else:
                            # XP does not like this format!
                            command = 'os.system("%s" "%s")' % (arg,shortPath)
                            os.system('"%s" "%s"' % (arg,shortPath))
                    elif openType == "os.startfile":
                        command = "os.startfile(%s)" % (arg+shortPath)
                        os.startfile(arg+path)
                    elif openType == "exec":
                        command = "exec(%s)" % (arg+shortPath)
                        exec arg+path in {}
                    elif openType == "os.spawnl":
                        filename = g.os_path_basename(arg)
                        command = "os.spawnl(%s,%s,%s)" % (arg,filename,path)
                        apply(os.spawnl,(os.P_NOWAIT,arg,filename,path))
                    elif openType == "os.spawnv":
                        filename = os.path.basename(arg[0]) 
                        vtuple = arg[1:]
                        vtuple.insert(0, filename)
                            # add the name of the program as the first argument.
                            # Change suggested by Jim Sizelove.
                        vtuple.append(path)
                        command = "os.spawnv(%s,%s)" % (arg[0],repr(vtuple))
                        apply(os.spawnv,(os.P_NOWAIT,arg[0],vtuple))
                    # This clause by Jim Sizelove.
                    elif openType == "subprocess.Popen":
                        if isinstance(arg, basestring):
                            vtuple = arg + " " + path
                        elif isinstance(arg, (list, tuple)):
                            vtuple = arg[:]
                            vtuple.append(path)
                        command = "subprocess.Popen(%s)" % repr(vtuple)
                        if subprocess:
                            subprocess.Popen(vtuple)
                        else:
                            g.grace('Can not import subprocess.  Skipping: "%s"' % command)
                    else:
                        command="bad command:"+str(openType)
                        g.trace(command)
                except Exception:
                    g.es("exception executing: "+command)
                    g.es_exception()
                #@-node:AGP.20250415230112.367:<< execute a command to open path in external editor >>
                #@nl
            g.doHook("openwith2",c=c,p=p,v=p.v,openType=openType,arg=arg,ext=ext)
        except Exception:
            g.es("unexpected exception in c.openWith")
            g.es_exception()
    
        return "break"
    #@+node:AGP.20250415230112.368:createOpenWithTempFile
    def createOpenWithTempFile (self,p,ext):
        
        c = self
        path = c.openWithTempFilePath(p,ext)
        try:
            if g.os_path_exists(path):
                g.es("recreating:  " + g.shortFileName(path),color="red")
            else:
                g.es("creating:  " + g.shortFileName(path),color="blue")
            theFile = open(path,"w")
            # Convert s to whatever encoding is in effect.
            s = p.bodyString()
            theDict = g.scanDirectives(c,p=p)
            encoding = theDict.get("encoding",None)
            if encoding == None:
                encoding = c.config.default_derived_file_encoding
            s = g.toEncodedString(s,encoding,reportErrors=True) 
            theFile.write(s)
            theFile.flush()
            theFile.close()
            try:    time = g.os_path_getmtime(path)
            except: time = None
            # g.es("time: " + str(time))
            # New in 4.3: theDict now contains both 'p' and 'v' entries, of the expected type.
            theDict = {
                "body":s, "c":c, "encoding":encoding,
                "f":theFile, "path":path, "time":time,
                "p":p, "v":p.v }
            #@        << remove previous entry from app.openWithFiles if it exists >>
            #@+node:AGP.20250415230112.369:<< remove previous entry from app.openWithFiles if it exists >>
            for d in g.app.openWithFiles[:]:
                p2 = d.get("p")
                if p.v.t == p2.v.t:
                    # print "removing previous entry in g.app.openWithFiles for",p.headString()
                    g.app.openWithFiles.remove(d)
            #@-node:AGP.20250415230112.369:<< remove previous entry from app.openWithFiles if it exists >>
            #@nl
            g.app.openWithFiles.append(theDict)
            return path
        except:
            if theFile:
                theFile.close()
            theFile = None
            g.es("exception creating temp file",color="red")
            g.es_exception()
            return None
    #@-node:AGP.20250415230112.368:createOpenWithTempFile
    #@+node:AGP.20250415230112.370:c.openWithTempFilePath
    def openWithTempFilePath (self,p,ext):
        
        """Return the path to the temp file corresponding to p and ext."""
        
        if 0: # new code: similar to code in mod_tempfname.py plugin.
            try:
                # At least in Windows, user name may contain special characters
                # which would require escaping quotes.
                leoTempDir = g.sanitize_filename(getpass.getuser()) + "_" + "Leo"
            except:
                leoTempDir = "LeoTemp"
                g.es("Could not retrieve your user name.")
                g.es("Temporary files will be stored in: %s" % leoTempDir)
            
            td = os.path.join(g.os_path_abspath(tempfile.gettempdir()),leoTempDir)
            if not os.path.exists(td):
                os.mkdir(td)
            
            name = g.sanitize_filename(v.headString()) + '_' + str(id(v.t))  + ext
            path = os.path.join(td,name)
            return path
        else: # Original code.
            name = "LeoTemp_%s_%s%s" % (
                str(id(p.v.t)),
                g.sanitize_filename(p.headString()),
                ext)
        
            name = g.toUnicode(name,g.app.tkEncoding)
        
            if 1:
                td = g.os_path_abspath(tempfile.gettempdir())
            else:
                td = g.os_path_abspath(g.os_path_join(g.app.loadDir,'..','temp'))
        
            path = g.os_path_join(td,name)
        
            return path
    #@-node:AGP.20250415230112.370:c.openWithTempFilePath
    #@-node:AGP.20250415230112.361:openWith and allies
    #@+node:AGP.20250415230112.371:close
    def close (self,event=None):
        
        '''Close the Leo window, prompting to save it if it has been changed.'''
    
        g.app.closeLeoWindow(self.frame)
    #@-node:AGP.20250415230112.371:close
    #@+node:AGP.20250415230112.372:save
    def save (self,event=None):
        
        '''Save a Leo outline to a file.'''
    
        c = self
        
        if g.app.disableSave:
            g.es("Save commands disabled",color="purple")
            return
        
        # Make sure we never pass None to the ctor.
        if not c.mFileName:
            c.frame.title = ""
            c.mFileName = ""
    
        if c.mFileName != "":
            # Calls c.setChanged(False) if no error.
            c.fileCommands.save(c.mFileName)
        else:
            fileName = g.app.gui.runSaveFileDialog(
                initialfile = c.mFileName,
                title="Save",
                filetypes=[("Leox files","*.leox"),("Leo files", "*.leo")],
                defaultextension=".leox")
            c.bringToFront()
    
            if fileName:
                # Don't change mFileName until the dialog has suceeded.
                c.mFileName = g.ensure_extension(fileName, ".leo")
                c.frame.title = c.mFileName
                c.frame.setTitle(g.computeWindowTitle(c.mFileName))
                c.frame.openDirectory = g.os_path_dirname(c.mFileName) # Bug fix in 4.4b2.
                c.fileCommands.save(c.mFileName)
                c.updateRecentFiles(c.mFileName)
    #@-node:AGP.20250415230112.372:save
    #@+node:AGP.20250415230112.373:saveAs
    def saveAs (self,event=None):
        
        '''Save a Leo outline to a file with a new filename.'''
        
        c = self
        
        if g.app.disableSave:
            g.es("Save commands disabled",color="purple")
            return
    
        # Make sure we never pass None to the ctor.
        if not c.mFileName:
            c.frame.title = ""
    
        fileName = g.app.gui.runSaveFileDialog(
            initialfile = c.mFileName,
            title="Save As",
            filetypes=[("Leox files","*.leox"),("Leo files", "*.leo")],
            defaultextension=".leox")
        c.bringToFront()
    
        if fileName:
            # 7/2/02: don't change mFileName until the dialog has suceeded.
            c.mFileName = g.ensure_extension(fileName, ".leo")
            c.frame.title = c.mFileName
            c.frame.setTitle(g.computeWindowTitle(c.mFileName))
            c.frame.openDirectory = g.os_path_dirname(c.mFileName) # Bug fix in 4.4b2.
            # Calls c.setChanged(False) if no error.
            c.fileCommands.saveAs(c.mFileName)
            c.updateRecentFiles(c.mFileName)
    #@-node:AGP.20250415230112.373:saveAs
    #@+node:AGP.20250415230112.374:saveTo
    def saveTo (self,event=None):
        
        '''Save a Leo outline to a file, leaving the file associated with the Leo outline unchanged.'''
        
        c = self
        
        if g.app.disableSave:
            g.es("Save commands disabled",color="purple")
            return
    
        # Make sure we never pass None to the ctor.
        if not c.mFileName:
            c.frame.title = ""
    
        # set local fileName, _not_ c.mFileName
        fileName = g.app.gui.runSaveFileDialog(
            initialfile = c.mFileName,
            title="Save To",
            filetypes=[("Leox files","*.leox"),("Leo files", "*.leo")],
            defaultextension=".leox")
        c.bringToFront()
    
        if fileName:
            fileName = g.ensure_extension(fileName, ".leo")
            c.fileCommands.saveTo(fileName)
            c.updateRecentFiles(fileName)
    #@-node:AGP.20250415230112.374:saveTo
    #@+node:AGP.20250415230112.375:revert
    def revert (self,event=None):
        
        '''Revert the contents of a Leo outline to last saved contents.'''
        
        c = self
    
        # Make sure the user wants to Revert.
        if not c.mFileName:
            return
            
        reply = g.app.gui.runAskYesNoDialog(c,"Revert",
            "Revert to previous version of " + c.mFileName + "?")
        c.bringToFront()
    
        if reply=="no":
            return
    
        # Kludge: rename this frame so openWithFileName won't think it is open.
        fileName = c.mFileName ; c.mFileName = ""
    
        # Create a new frame before deleting this frame.
        ok, frame = g.openWithFileName(fileName,c)
        if ok:
            frame.deiconify()
            g.app.destroyWindow(c.frame)
        else:
            c.mFileName = fileName
        
        
    #@nonl
    #@-node:AGP.20250415230112.375:revert
    #@-node:AGP.20250415230112.357:top level (file menu)
    #@+node:AGP.20250415230112.376:Recent Files submenu & allies
    #@+node:AGP.20250415230112.377:clearRecentFiles
    def clearRecentFiles (self,event=None):
        
        """Clear the recent files list, then add the present file."""
    
        c = self ; f = c.frame ; u = c.undoer
        
        bunch = u.beforeClearRecentFiles()
        
        recentFilesMenu = f.menu.getMenu("Open Recent File...")
        f.menu.delete_range(recentFilesMenu,0,len(c.recentFiles))
        
        c.recentFiles = []
        g.app.config.recentFiles = [] # New in Leo 4.3.
        f.menu.createRecentFilesMenuItems()
        c.updateRecentFiles(c.fileName())
        
        g.app.config.appendToRecentFiles(c.recentFiles)
        
        u.afterClearRecentFiles(bunch)
    #@-node:AGP.20250415230112.377:clearRecentFiles
    #@+node:AGP.20250415230112.378:openRecentFile
    def openRecentFile(self,name=None):
        
        if not name: return
    
        c = self ; v = c.currentVnode()
        #@    << Set closeFlag if the only open window is empty >>
        #@+node:AGP.20250415230112.379:<< Set closeFlag if the only open window is empty >>
        #@+at 
        #@nonl
        # If this is the only open window was opened when the app started, and 
        # the window has never been written to or saved, then we will 
        # automatically close that window if this open command completes 
        # successfully.
        #@-at
        #@@c
            
        closeFlag = (
            c.frame.startupWindow and # The window was open on startup
            not c.changed and not c.frame.saved and # The window has never been changed
            g.app.numberOfWindows == 1) # Only one untitled window has ever been opened
        #@-node:AGP.20250415230112.379:<< Set closeFlag if the only open window is empty >>
        #@nl
        
        fileName = name
        if not g.doHook("recentfiles1",c=c,p=v,v=v,fileName=fileName,closeFlag=closeFlag):
            ok, frame = g.openWithFileName(fileName,c)
            if ok and closeFlag:
                g.app.destroyWindow(c.frame) # 12/12/03
                c = frame.c # Switch to the new commander so the "recentfiles2" hook doesn't crash.
                c.setLog() # Sets the log stream for g.es()
    
        g.doHook("recentfiles2",c=c,p=v,v=v,fileName=fileName,closeFlag=closeFlag)
    #@-node:AGP.20250415230112.378:openRecentFile
    #@+node:AGP.20250415230112.380:c.updateRecentFiles
    def updateRecentFiles (self,fileName):
        
        """Create the RecentFiles menu.  May be called with Null fileName."""
        
        if g.app.unitTesting: return
        
        def munge(name):
            name = name or ''
            return g.os_path_normpath(name).lower()
    
        # Update the recent files list in all windows.
        if fileName:
            compareFileName = munge(fileName)
            # g.trace(fileName)
            for frame in g.app.windowList:
                c = frame.c
                # Remove all versions of the file name.
                for name in c.recentFiles:
                    if compareFileName == munge(name):
                        c.recentFiles.remove(name)
                c.recentFiles.insert(0,fileName)
                # g.trace(fileName)
                # Recreate the Recent Files menu.
                frame.menu.createRecentFilesMenuItems()
        else:
            for frame in g.app.windowList:
                frame.menu.createRecentFilesMenuItems()
    #@-node:AGP.20250415230112.380:c.updateRecentFiles
    #@-node:AGP.20250415230112.376:Recent Files submenu & allies
    #@+node:AGP.20250415230112.381:Read/Write submenu
    #@+node:AGP.20250415230112.382:readOutlineOnly
    def readOutlineOnly (self,event=None):
        
        '''Open a Leo outline from a .leo file, but do not read any derived files.'''
    
        fileName = g.app.gui.runOpenFileDialog(
            title="Read Outline Only",
            filetypes=[("Leo files", "*.leo"), ("All files", "*")],
            defaultextension=".leo")
    
        if not fileName:
            return
    
        try:
            theFile = open(fileName,'r')
            c,frame = g.app.newLeoCommanderAndFrame(fileName)
            frame.deiconify()
            frame.lift()
            g.app.root.update() # Force a screen redraw immediately.
            c.fileCommands.readOutlineOnly(theFile,fileName) # closes file.
        except:
            g.es("can not open:" + fileName)
    #@-node:AGP.20250415230112.382:readOutlineOnly
    #@+node:AGP.20250415230112.383:readAtFileNodes (commands)
    def readAtFileNodes (self,event=None):
        
        '''Read all @file nodes in the presently selected outline.'''
    
        c = self ; u = c.undoer ; p = c.currentPosition()
    
        c.beginUpdate()
        try:
            undoData = u.beforeChangeTree(p)
            c.fileCommands.readAtFileNodes()
            u.afterChangeTree(p,'Read @file Nodes',undoData)
        finally:
            c.endUpdate()
    #@-node:AGP.20250415230112.383:readAtFileNodes (commands)
    #@+node:AGP.20250415230112.384:importDerivedFile
    def importDerivedFile (self,event=None):
        
        """Create a new outline from a 4.0 derived file."""
        
        c = self ; p = c.currentPosition()
        
        types = [
            ("All files","*"),
            ("C/C++ files","*.c"),
            ("C/C++ files","*.cpp"),
            ("C/C++ files","*.h"),
            ("C/C++ files","*.hpp"),
            ("Java files","*.java"),
            ("Lua files", "*.lua"),
            ("Pascal files","*.pas"),
            ("Python files","*.py") ]
        
        names = g.app.gui.runOpenFileDialog(
            title="Import Derived File",
            filetypes=types,
            defaultextension=".py",
            multiple=True)
    
        if names:
            c.importCommands.importDerivedFiles(parent=p,paths=names)
    #@-node:AGP.20250415230112.384:importDerivedFile
    #@-node:AGP.20250415230112.381:Read/Write submenu
    #@+node:AGP.20250415230112.385:Tangle submenu
    #@+node:AGP.20250415230112.386:tangleAll
    def tangleAll (self,event=None):
        
        '''Tangle all @root nodes in the entire outline.'''
        
        c = self
        c.tangleCommands.tangleAll()
    #@-node:AGP.20250415230112.386:tangleAll
    #@+node:AGP.20250415230112.387:tangleMarked
    def tangleMarked (self,event=None):
        
        '''Tangle all marked @root nodes in the entire outline.'''
    
        c = self
        c.tangleCommands.tangleMarked()
    #@-node:AGP.20250415230112.387:tangleMarked
    #@+node:AGP.20250415230112.388:tangle
    def tangle (self,event=None):
        
        '''Tangle all @root nodes in the selected outline.'''
    
        c = self
        c.tangleCommands.tangle()
    #@-node:AGP.20250415230112.388:tangle
    #@-node:AGP.20250415230112.385:Tangle submenu
    #@+node:AGP.20250415230112.389:Untangle submenu
    #@+node:AGP.20250415230112.390:untangleAll
    def untangleAll (self,event=None):
        
        '''Untangle all @root nodes in the entire outline.'''
    
        c = self
        c.tangleCommands.untangleAll()
        c.undoer.clearUndoState()
    #@-node:AGP.20250415230112.390:untangleAll
    #@+node:AGP.20250415230112.391:untangleMarked
    def untangleMarked (self,event=None):
        
        '''Untangle all marked @root nodes in the entire outline.'''
    
        c = self
        c.tangleCommands.untangleMarked()
        c.undoer.clearUndoState()
    #@-node:AGP.20250415230112.391:untangleMarked
    #@+node:AGP.20250415230112.392:untangle
    def untangle (self,event=None):
        
        '''Untangle all @root nodes in the selected outline.'''
    
        c = self
        c.tangleCommands.untangle()
        c.undoer.clearUndoState()
    #@-node:AGP.20250415230112.392:untangle
    #@-node:AGP.20250415230112.389:Untangle submenu
    #@+node:AGP.20250415230112.393:Import&Export submenu
    #@+node:AGP.20250415230112.394:exportHeadlines
    def exportHeadlines (self,event=None):
        
        '''Export all headlines to an external file.'''
        
        c = self
    
        filetypes = [("Text files", "*.txt"),("All files", "*")]
    
        fileName = g.app.gui.runSaveFileDialog(
            initialfile="headlines.txt",
            title="Export Headlines",
            filetypes=filetypes,
            defaultextension=".txt")
        c.bringToFront()
    
        if fileName and len(fileName) > 0:
            g.setGlobalOpenDir(fileName)
            c.importCommands.exportHeadlines(fileName)
    #@-node:AGP.20250415230112.394:exportHeadlines
    #@+node:AGP.20250415230112.395:flattenOutline
    def flattenOutline (self,event=None):
        
        '''Export the selected outline to an external file.
        The outline is represented in MORE format.'''
        
        c = self
    
        filetypes = [("Text files", "*.txt"),("All files", "*")]
    
        fileName = g.app.gui.runSaveFileDialog(
            initialfile="flat.txt",
            title="Flatten Outline",
            filetypes=filetypes,
            defaultextension=".txt")
        c.bringToFront()
    
        if fileName and len(fileName) > 0:
            g.setGlobalOpenDir(fileName)
            c.importCommands.flattenOutline(fileName)
    #@-node:AGP.20250415230112.395:flattenOutline
    #@+node:AGP.20250415230112.396:importAtRoot
    def importAtRoot (self,event=None):
        
        '''Import one or more external files, creating @root trees.'''
        
        c = self
        
        types = [
            ("All files","*"),
            ("C/C++ files","*.c"),
            ("C/C++ files","*.cpp"),
            ("C/C++ files","*.h"),
            ("C/C++ files","*.hpp"),
            ("Java files","*.java"),
            ("Lua files", "*.lua"),
            ("Pascal files","*.pas"),
            ("Python files","*.py") ]
    
        names = g.app.gui.runOpenFileDialog(
            title="Import To @root",
            filetypes=types,
            defaultextension=".py",
            multiple=True)
        c.bringToFront()
    
        if names:
            c.importCommands.importFilesCommand (names,"@root")
    #@-node:AGP.20250415230112.396:importAtRoot
    #@+node:AGP.20250415230112.397:importAtFile
    def importAtFile (self,event=None):
        
        '''Import one or more external files, creating @file trees.'''
        
        c = self
    
        types = [
            ("All files","*"),
            ("C/C++ files","*.c"),
            ("C/C++ files","*.cpp"),
            ("C/C++ files","*.h"),
            ("C/C++ files","*.hpp"),
            ("Java files","*.java"),
            ("Lua files", "*.lua"),
            ("Pascal files","*.pas"),
            ("Python files","*.py") ]
    
        names = g.app.gui.runOpenFileDialog(
            title="Import To @file",
            filetypes=types,
            defaultextension=".py",
            multiple=True)
        c.bringToFront()
    
        if names:
            c.importCommands.importFilesCommand(names,"@file")
    #@-node:AGP.20250415230112.397:importAtFile
    #@+node:AGP.20250415230112.398:importCWEBFiles
    def importCWEBFiles (self,event=None):
        
        '''Import one or more external CWEB files, creating @file trees.'''
        
        c = self
        
        filetypes = [
            ("CWEB files", "*.w"),
            ("Text files", "*.txt"),
            ("All files", "*")]
    
        names = g.app.gui.runOpenFileDialog(
            title="Import CWEB Files",
            filetypes=filetypes,
            defaultextension=".w",
            multiple=True)
        c.bringToFront()
    
        if names:
            c.importCommands.importWebCommand(names,"cweb")
    #@-node:AGP.20250415230112.398:importCWEBFiles
    #@+node:AGP.20250415230112.399:importFlattenedOutline
    def importFlattenedOutline (self,event=None):
        
        '''Import an external created by the flatten-outline command.'''
        
        c = self
        
        types = [("Text files","*.txt"), ("All files","*")]
    
        names = g.app.gui.runOpenFileDialog(
            title="Import MORE Text",
            filetypes=types,
            defaultextension=".py",
            multiple=True)
        c.bringToFront()
    
        if names:
            c.importCommands.importFlattenedOutline(names)
    #@-node:AGP.20250415230112.399:importFlattenedOutline
    #@+node:AGP.20250415230112.400:importNowebFiles
    def importNowebFiles (self,event=None):
        
        '''Import one or more external noweb files, creating @file trees.'''
        
        c = self
    
        filetypes = [
            ("Noweb files", "*.nw"),
            ("Text files", "*.txt"),
            ("All files", "*")]
    
        names = g.app.gui.runOpenFileDialog(
            title="Import Noweb Files",
            filetypes=filetypes,
            defaultextension=".nw",
            multiple=True)
        c.bringToFront()
    
        if names:
            c.importCommands.importWebCommand(names,"noweb")
    #@-node:AGP.20250415230112.400:importNowebFiles
    #@+node:AGP.20250415230112.401:outlineToCWEB
    def outlineToCWEB (self,event=None):
        
        '''Export the selected outline to an external file.
        The outline is represented in CWEB format.'''
        
        c = self
    
        filetypes=[
            ("CWEB files", "*.w"),
            ("Text files", "*.txt"),
            ("All files", "*")]
    
        fileName = g.app.gui.runSaveFileDialog(
            initialfile="cweb.w",
            title="Outline To CWEB",
            filetypes=filetypes,
            defaultextension=".w")
        c.bringToFront()
    
        if fileName and len(fileName) > 0:
            g.setGlobalOpenDir(fileName)
            c.importCommands.outlineToWeb(fileName,"cweb")
    #@-node:AGP.20250415230112.401:outlineToCWEB
    #@+node:AGP.20250415230112.402:outlineToNoweb
    def outlineToNoweb (self,event=None):
        
        '''Export the selected outline to an external file.
        The outline is represented in noweb format.'''
        
        c = self
        
        filetypes=[
            ("Noweb files", "*.nw"),
            ("Text files", "*.txt"),
            ("All files", "*")]
    
        fileName = g.app.gui.runSaveFileDialog(
            initialfile=self.outlineToNowebDefaultFileName,
            title="Outline To Noweb",
            filetypes=filetypes,
            defaultextension=".nw")
        c.bringToFront()
    
        if fileName and len(fileName) > 0:
            g.setGlobalOpenDir(fileName)
            c.importCommands.outlineToWeb(fileName,"noweb")
            c.outlineToNowebDefaultFileName = fileName
    #@-node:AGP.20250415230112.402:outlineToNoweb
    #@+node:AGP.20250415230112.403:removeSentinels
    def removeSentinels (self,event=None):
        
        '''Import one or more files, removing any sentinels.'''
        
        c = self
        
        types = [
            ("All files","*"),
            ("C/C++ files","*.c"),
            ("C/C++ files","*.cpp"),
            ("C/C++ files","*.h"),
            ("C/C++ files","*.hpp"),
            ("Java files","*.java"),
            ("Lua files", "*.lua"),
            ("Pascal files","*.pas"),
            ("Python files","*.py") ]
    
        names = g.app.gui.runOpenFileDialog(
            title="Remove Sentinels",
            filetypes=types,
            defaultextension=".py",
            multiple=True)
        c.bringToFront()
    
        if names:
            c.importCommands.removeSentinelsCommand (names)
    #@-node:AGP.20250415230112.403:removeSentinels
    #@+node:AGP.20250415230112.404:weave
    def weave (self,event=None):
        
        '''Simulate a literate-programming weave operation by writing the outline to a text file.'''
        
        c = self
    
        filetypes = [("Text files", "*.txt"),("All files", "*")]
    
        fileName = g.app.gui.runSaveFileDialog(
            initialfile="weave.txt",
            title="Weave",
            filetypes=filetypes,
            defaultextension=".txt")
        c.bringToFront()
    
        if fileName and len(fileName) > 0:
            g.setGlobalOpenDir(fileName)
            c.importCommands.weave(fileName)
    #@-node:AGP.20250415230112.404:weave
    #@-node:AGP.20250415230112.393:Import&Export submenu
    #@-node:AGP.20250415230112.356:File Menu
    #@+node:AGP.20250415230112.405:Edit Menu...
    #@+node:AGP.20250415230112.406:Edit top level
    #@+node:AGP.20250415230112.407:c.executeScript
    def executeScript(self,event=None,p=None,script=None,
        useSelectedText=True,define_g=True,define_name='__main__',silent=False):
    
        """This executes body text as a Python script.
        
        We execute the selected text, or the entire body text if no text is selected."""
        
        c = self ; script1 = script
        if not script:
            script = g.getScript(c,p,useSelectedText=useSelectedText)
        #@    << redirect output >>
        #@+node:AGP.20250415230112.408:<< redirect output >>
        if c.config.redirect_execute_script_output_to_log_pane:
        
            g.redirectStdout() # Redirect stdout
            g.redirectStderr() # Redirect stderr
        #@-node:AGP.20250415230112.408:<< redirect output >>
        #@nl
        try:
            log = c.frame.log
            if script.strip():
                sys.path.insert(0,c.frame.openDirectory)
                script += '\n' # Make sure we end the script properly.
                try:
                    p = c.currentPosition()
                    d = g.choose(define_g,{'c':c,'g':g,'p':p},{})
                    if define_name: d['__name__'] = define_name
                    # g.trace(script)
                    exec script in d
                    if not script1 and not silent:
                        # Careful: the script may have changed the log tab.
                        tabName = log and hasattr(log,'tabName') and log.tabName or 'Log'
                        g.es("end of script",color="purple",tabName=tabName)
                except Exception:
                    g.handleScriptException(c,p,script,script1)
                del sys.path[0]
            else:
                tabName = log and hasattr(log,'tabName') and log.tabName or 'Log'
                g.es("no script selected",color="blue",tabName=tabName)
        finally: # New in 4.3 beta 2: unredirect output last.
            #@        << unredirect output >>
            #@+node:AGP.20250415230112.409:<< unredirect output >>
            if c.exists and c.config.redirect_execute_script_output_to_log_pane:
            
                g.restoreStderr()
                g.restoreStdout()
            #@-node:AGP.20250415230112.409:<< unredirect output >>
            #@nl
    #@-node:AGP.20250415230112.407:c.executeScript
    #@+node:AGP.20250415230112.410:goToLineNumber & allies
    def goToLineNumber (self,event=None,root=None,lines=None,n=None,scriptFind=False):
        
        '''Place the cursor on the n'th line of a derived file or script.'''
        #print "gtln",n
        
        
        
        c = self ; p = c.currentPosition()
        root1 = root
        if root is None:
            #@        << set root >>
            #@+node:AGP.20250415230112.411:<< set root >>
            # First look for ancestor @file node.
            fileName = None
            for p in p.self_and_parents_iter():
                fileName = p.anyAtFileNodeName()
                if fileName: break
            
            # New in 4.2: Search the entire tree for joined nodes.
            if not fileName:
                p1 = c.currentPosition()
                for p in c.all_positions_iter():
                    if p.v.t == p1.v.t and p != p1:
                        # Found a joined position.
                        for p in p.self_and_parents_iter():
                            fileName = p.anyAtFileNodeName()
                            # New in 4.2 b3: ignore @all nodes.
                            if fileName and not p.isAtAllNode(): break
                    if fileName: break
            
            if fileName:
                root = p.copy()
            else:
                # New in 4.2.1: assume the c.currentPosition is the root of a script.
                root = c.currentPosition()
                g.es("No ancestor @file node: using script line numbers", color="blue")
                scriptFind = True
                lines = g.getScript (c,root,useSelectedText=False)
                lines = g.splitLines(lines)
                if 0:
                    for line in lines:
                        print line,
            #@-node:AGP.20250415230112.411:<< set root >>
            #@nl
        if lines is None:
            #@        << read the file into lines >>
            #@+node:AGP.20250415230112.412:<< read the file into lines >>
            # 1/26/03: calculate the full path.
            d = g.scanDirectives(c)
            path = d.get("path")
            
            fileName = g.os_path_join(path,fileName)
            
            try:
                lines=self.gotoLineNumberOpen(fileName) # bwm
            except:
                g.es("not found: " + fileName)
                return
            #@-node:AGP.20250415230112.412:<< read the file into lines >>
            #@nl
        if n is None:
            #@        << get n, the line number, from a dialog >>
            #@+node:AGP.20250415230112.413:<< get n, the line number, from a dialog >>
            n = g.app.gui.runAskOkCancelNumberDialog(c,"Enter Line Number","Line number:")
            if n == -1:
                return
            #@-node:AGP.20250415230112.413:<< get n, the line number, from a dialog >>
            #@nl
        n = self.applyLineNumberMappingIfAny(n) #bwm
        if n==1:
            p = root ; n2 = 1 ; found = True
        elif n >= len(lines):
            p = root ; found = False
            n2 = p.bodyString().count('\n')
        elif root.isAtAsisFileNode():
            #@        << count outline lines, setting p,n2,found >>
            #@+node:AGP.20250415230112.414:<< count outline lines, setting p,n2,found >> (@file-nosent only)
            p = lastv = root
            prev = 0 ; found = False
            
            for p in p.self_and_subtree_iter():
                lastv = p.copy()
                s = p.bodyString()
                lines = s.count('\n')
                if len(s) > 0 and s[-1] != '\n':
                    lines += 1
                # print lines,prev,p
                if prev + lines >= n:
                    found = True ; break
                prev += lines
            
            p = lastv
            n2 = max(1,n-prev)
            #@-node:AGP.20250415230112.414:<< count outline lines, setting p,n2,found >> (@file-nosent only)
            #@nl
        else:
            vnodeName,childIndex,gnx,n2,delim = self.convertLineToVnodeNameIndexLine(lines,n,root,scriptFind)
            found = True
            if not vnodeName:
                g.es("error handling: " + root.headString())
                return
            #@        << set p to the node given by vnodeName, etc. >>
            #@+node:AGP.20250415230112.415:<< set p to the node given by vnodeName, etc. >>
            if scriptFind:
                #@    << just scan for the node name >>
                #@+node:AGP.20250415230112.416:<< just scan for the node name >>
                # This is safe enough because clones are not much of an issue.
                found = False
                for p in root.self_and_subtree_iter():
                    if p.matchHeadline(vnodeName):
                        found = True ; break
                #@-node:AGP.20250415230112.416:<< just scan for the node name >>
                #@nl
            elif gnx:
                #@    << 4.2: get node from gnx >>
                #@+node:AGP.20250415230112.417:<< 4.2: get node from gnx >>
                found = False
                gnx = g.app.nodeIndices.scanGnx(gnx,0)
                
                # g.trace(vnodeName)
                # g.trace(gnx)
                
                for p in root.self_and_subtree_iter():
                    if p.matchHeadline(vnodeName):
                        # g.trace(p.v.t.fileIndex)
                        if p.v.t.fileIndex == gnx:
                            found = True ; break
                
                if not found:
                    g.es("not found: " + vnodeName, color="red")
                    return
                #@-node:AGP.20250415230112.417:<< 4.2: get node from gnx >>
                #@nl
            elif childIndex == -1:
                #@    << 4.x: scan for the node using tnodeList and n >>
                #@+node:AGP.20250415230112.418:<< 4.x: scan for the node using tnodeList and n >>
                # This is about the best that can be done without replicating the entire atFile write logic.
                
                ok = True
                
                if not hasattr(root.v.t,"tnodeList"):
                    s = "no child index for " + root.headString()
                    g.es_print(s, color="red")
                    ok = False
                
                if ok:
                    tnodeList = root.v.t.tnodeList
                    #@    << set tnodeIndex to the number of +node sentinels before line n >>
                    #@+node:AGP.20250415230112.419:<< set tnodeIndex to the number of +node sentinels before line n >>
                    tnodeIndex = -1 # Don't count the @file node.
                    scanned = 0 # count of lines scanned.
                    
                    for s in lines:
                        if scanned >= n:
                            break
                        i = g.skip_ws(s,0)
                        if g.match(s,i,delim):
                            i += len(delim)
                            if g.match(s,i,"+node"):
                                # g.trace(tnodeIndex,s.rstrip())
                                tnodeIndex += 1
                        scanned += 1
                    #@-node:AGP.20250415230112.419:<< set tnodeIndex to the number of +node sentinels before line n >>
                    #@nl
                    tnodeIndex = max(0,tnodeIndex)
                    #@    << set p to the first vnode whose tnode is tnodeList[tnodeIndex] or set ok = False >>
                    #@+node:AGP.20250415230112.420:<< set p to the first vnode whose tnode is tnodeList[tnodeIndex] or set ok = false >>
                    #@+at 
                    #@nonl
                    # We use the tnodeList to find a _tnode_ corresponding to 
                    # the proper node, so the user will for sure be editing 
                    # the proper text, even if several nodes happen to have 
                    # the same headline.  This is really all that we need.
                    # 
                    # However, this code has no good way of distinguishing 
                    # between different cloned vnodes in the file: they all 
                    # have the same tnode.  So this code just picks p = 
                    # t.vnodeList[0] and leaves it at that.
                    # 
                    # The only way to do better is to scan the outline, 
                    # replicating the write logic to determine which vnode 
                    # created the given line.  That's way too difficult, and 
                    # it would create an unwanted dependency in this code.
                    #@-at
                    #@@c
                    
                    # g.trace("tnodeIndex",tnodeIndex)
                    if tnodeIndex < len(tnodeList):
                        t = tnodeList[tnodeIndex]
                        # Find the first vnode whose tnode is t.
                        found = False
                        for p in root.self_and_subtree_iter():
                            if p.v.t == t:
                                found = True ; break
                        if not found:
                            s = "tnode not found for " + vnodeName
                            g.es_print(s, color="red") ; ok = False
                        elif p.headString().strip() != vnodeName:
                            if 0: # Apparently this error doesn't prevent a later scan for working properly.
                                s = "Mismatched vnodeName\nExpecting: %s\n got: %s" % (p.headString(),vnodeName)
                                g.es_print(s, color="red")
                            ok = False
                    else:
                        if root1 is None: # Kludge: disable this message when called by goToScriptLineNumber.
                            s = "Invalid computed tnodeIndex: %d" % tnodeIndex
                            g.es_print(s, color = "red")
                        ok = False
                    #@-node:AGP.20250415230112.420:<< set p to the first vnode whose tnode is tnodeList[tnodeIndex] or set ok = false >>
                    #@nl
                            
                if not ok:
                    # Fall back to the old logic.
                    #@    << set p to the first node whose headline matches vnodeName >>
                    #@+node:AGP.20250415230112.421:<< set p to the first node whose headline matches vnodeName >>
                    found = False
                    for p in root.self_and_subtree_iter():
                        if p.matchHeadline(vnodeName):
                            found = True ; break
                    
                    if not found:
                        s = "not found: " + vnodeName
                        g.es_print(s, color="red")
                        return
                    #@-node:AGP.20250415230112.421:<< set p to the first node whose headline matches vnodeName >>
                    #@nl
                #@-node:AGP.20250415230112.418:<< 4.x: scan for the node using tnodeList and n >>
                #@nl
            else:
                #@    << 3.x: scan for the node with the given childIndex >>
                #@+node:AGP.20250415230112.422:<< 3.x: scan for the node with the given childIndex >>
                found = False
                for p in root.self_and_subtree_iter():
                    if p.matchHeadline(vnodeName):
                        if childIndex <= 0 or p.childIndex() + 1 == childIndex:
                            found = True ; break
                
                if not found:
                    g.es("not found: " + vnodeName, color="red")
                    return
                #@-node:AGP.20250415230112.422:<< 3.x: scan for the node with the given childIndex >>
                #@nl
            #@-node:AGP.20250415230112.415:<< set p to the node given by vnodeName, etc. >>
            #@nl
        #@    << select p and make it visible >>
        #@+node:AGP.20250415230112.423:<< select p and make it visible >>
        c.beginUpdate()
        try:
            c.frame.tree.expandAllAncestors(p)
            c.selectVnode(p)
        finally:
            c.endUpdate()
        #@-node:AGP.20250415230112.423:<< select p and make it visible >>
        #@nl
        #@    << put the cursor on line n2 of the body text >>
        #@+node:AGP.20250415230112.424:<< put the cursor on line n2 of the body text >>
        if found:
            c.frame.body.setInsertPointToStartOfLine(n2-1)
        else:
            c.frame.body.setInsertionPointToEnd()
            g.es("%d lines" % len(lines), color="blue")
        
        c.bodyWantsFocusNow()
        c.frame.body.makeInsertPointVisible()
        #@-node:AGP.20250415230112.424:<< put the cursor on line n2 of the body text >>
        #@nl
    #@+node:AGP.20250415230112.425:convertLineToVnodeNameIndexLine
    #@+at 
    #@nonl
    # We count "real" lines in the derived files, ignoring all sentinels that 
    # do not arise from source lines.  When the indicated line is found, we 
    # scan backwards for an @+body line, get the vnode's name from that line 
    # and set p to the indicated vnode.  This will fail if vnode names have 
    # been changed, and that can't be helped.
    # 
    # Returns (vnodeName,offset)
    # 
    # vnodeName: the name found in the previous @+body sentinel.
    # offset: the offset within p of the desired line.
    #@-at
    #@@c
    
    def convertLineToVnodeNameIndexLine (self,lines,n,root,scriptFind):
        
        """Convert a line number n to a vnode name, (child index or gnx) and line number."""
        
        c = self ; at = c.atFileCommands
        childIndex = 0 ; gnx = None ; newDerivedFile = False
        thinFile = root.isAtThinFileNode()
        #@    << set delim, leoLine from the @+leo line >>
        #@+node:AGP.20250415230112.426:<< set delim, leoLine from the @+leo line >>
        # Find the @+leo line.
        tag = "@+leo"
        i = 0 
        while i < len(lines) and lines[i].find(tag)==-1:
            i += 1
        leoLine = i # Index of the line containing the leo sentinel
        
        if leoLine < len(lines):
            s = lines[leoLine]
            valid,newDerivedFile,start,end,derivedFileIsThin = at.parseLeoSentinel(s)
            if valid: delim = start + '@'
            else:     delim = None
        else:
            delim = None
        #@-node:AGP.20250415230112.426:<< set delim, leoLine from the @+leo line >>
        #@nl
        if not delim:
            g.es("bad @+leo sentinel")
            return None,None,None,None,None
        #@    << scan back to @+node, setting offset,nodeSentinelLine >>
        #@+node:AGP.20250415230112.427:<< scan back to  @+node, setting offset,nodeSentinelLine >>
        offset = 0 # This is essentially the Tk line number.
        nodeSentinelLine = -1
        line = n - 1
        while line >= 0:
            s = lines[line]
            # g.trace(s)
            i = g.skip_ws(s,0)
            if g.match(s,i,delim):
                #@        << handle delim while scanning backward >>
                #@+node:AGP.20250415230112.428:<< handle delim while scanning backward >>
                if line == n:
                    g.es("line "+str(n)+" is a sentinel line")
                i += len(delim)
                
                if g.match(s,i,"-node"):
                    # The end of a nested section.
                    line = self.skipToMatchingNodeSentinel(lines,line,delim)
                elif g.match(s,i,"+node"):
                    nodeSentinelLine = line
                    break
                elif g.match(s,i,"<<") or g.match(s,i,"@first"):
                    offset += 1 # Count these as a "real" lines.
                #@-node:AGP.20250415230112.428:<< handle delim while scanning backward >>
                #@nl
            else:
                offset += 1 # Assume the line is real.  A dubious assumption.
            line -= 1
        #@-node:AGP.20250415230112.427:<< scan back to  @+node, setting offset,nodeSentinelLine >>
        #@nl
        if nodeSentinelLine == -1:
            # The line precedes the first @+node sentinel
            # g.trace("before first line")
            return root.headString(),0,gnx,1,delim # 10/13/03
        s = lines[nodeSentinelLine]
        # g.trace(s)
        #@    << set vnodeName and (childIndex or gnx) from s >>
        #@+node:AGP.20250415230112.429:<< set vnodeName and (childIndex or gnx) from s >>
        if scriptFind:
            # The vnode name follows the first ':'
            i = s.find(':',i)
            if i > -1:
                vnodeName = s[i+1:].strip()
            childIndex = -1
        elif newDerivedFile:
            i = 0
            if thinFile:
                # gnx is lies between the first and second ':':
                i = s.find(':',i)
                if i > 0:
                    i += 1
                    j = s.find(':',i)
                    if j > 0:
                        gnx = s[i:j]
                    else: i = len(s)
                else: i = len(s)
            # vnode name is everything following the first or second':'
            # childIndex is -1 as a flag for later code.
            i = s.find(':',i)
            if i > -1: vnodeName = s[i+1:].strip()
            else: vnodeName = None
            childIndex = -1
        else:
            # vnode name is everything following the third ':'
            i = 0 ; colons = 0
            while i < len(s) and colons < 3:
                if s[i] == ':':
                    colons += 1
                    if colons == 1 and i+1 < len(s) and s[i+1].isdigit():
                        junk,childIndex = g.skip_long(s,i+1)
                i += 1
            vnodeName = s[i:].strip()
            
        # g.trace("gnx",gnx,"vnodeName:",vnodeName)
        if not vnodeName:
            vnodeName = None
            g.es("bad @+node sentinel")
        #@-node:AGP.20250415230112.429:<< set vnodeName and (childIndex or gnx) from s >>
        #@nl
        # g.trace("childIndex,offset",childIndex,offset,vnodeName)
        return vnodeName,childIndex,gnx,offset,delim
    #@-node:AGP.20250415230112.425:convertLineToVnodeNameIndexLine
    #@+node:AGP.20250415230112.430:skipToMatchingNodeSentinel
    def skipToMatchingNodeSentinel (self,lines,n,delim):
        
        s = lines[n]
        i = g.skip_ws(s,0)
        assert(g.match(s,i,delim))
        i += len(delim)
        if g.match(s,i,"+node"):
            start="+node" ; end="-node" ; delta=1
        else:
            assert(g.match(s,i,"-node"))
            start="-node" ; end="+node" ; delta=-1
        # Scan to matching @+-node delim.
        n += delta ; level = 0
        while 0 <= n < len(lines):
            s = lines[n] ; i = g.skip_ws(s,0)
            if g.match(s,i,delim):
                i += len(delim)
                if g.match(s,i,start):
                    level += 1
                elif g.match(s,i,end):
                    if level == 0: break
                    else: level -= 1
            n += delta
            
        # g.trace(n)
        return n
    #@-node:AGP.20250415230112.430:skipToMatchingNodeSentinel
    #@-node:AGP.20250415230112.410:goToLineNumber & allies
    #@+node:AGP.20250415230112.431:gotoLineNumberOpen
    def gotoLineNumberOpen(self, *args, **kw):
        """
        Hook for mod_shadow plugin.
        """
        theFile = open(*args, **kw)
        lines = theFile.readlines()
        theFile.close()
        return lines
    #@-node:AGP.20250415230112.431:gotoLineNumberOpen
    #@+node:AGP.20250415230112.432:applyLineNumberMappingIfAny
    def applyLineNumberMappingIfAny(self, n):
        """
        Hook for mod_shadow plugin.
        """
        return n
    #@-node:AGP.20250415230112.432:applyLineNumberMappingIfAny
    #@+node:AGP.20250415230112.433:goToScriptLineNumber
    def goToScriptLineNumber (self,root,script,n):
    
        """Go to line n of a script."""
    
        c = self
        
        # g.trace(n,root)
        
        lines = g.splitLines(script)
        c.goToLineNumber(root=root,lines=lines,n=n,scriptFind=True)
    #@-node:AGP.20250415230112.433:goToScriptLineNumber
    #@+node:AGP.20250415230112.434:fontPanel
    def fontPanel (self,event=None):
        
        '''Open the font dialog.'''
        
        c = self ; frame = c.frame
    
        if not frame.fontPanel:
            frame.fontPanel = g.app.gui.createFontPanel(c)
            
        frame.fontPanel.bringToFront()
    #@-node:AGP.20250415230112.434:fontPanel
    #@+node:AGP.20250415230112.435:colorPanel
    def colorPanel (self,event=None):
        
        '''Open the color dialog.'''
        
        c = self ; frame = c.frame
    
        if not frame.colorPanel:
            frame.colorPanel = g.app.gui.createColorPanel(c)
            
        frame.colorPanel.bringToFront()
    #@-node:AGP.20250415230112.435:colorPanel
    #@+node:AGP.20250415230112.436:show/hide/toggleInvisibles
    def hideInvisibles (self,event=None):
        c = self ; c.showInvisiblesHelper(False)
    
    def showInvisibles (self,event=None):
        c = self ; c.showInvisiblesHelper(True)
    
    def toggleShowInvisibles (self,event=None):
        c = self ; colorizer = c.frame.body.getColorizer()
        val = g.choose(colorizer.showInvisibles,0,1)
        c.showInvisiblesHelper(val)
        
    def showInvisiblesHelper (self,val):
        c = self ; frame = c.frame ; p = c.currentPosition()
        colorizer = frame.body.getColorizer()
        colorizer.showInvisibles = val
       
         # It is much easier to change the menu name here than in the menu updater.
        menu = frame.menu.getMenu("Edit")
        index = frame.menu.getMenuLabel(menu,g.choose(val,'Hide Invisibles','Show Invisibles'))
        if index is None:
            if val: frame.menu.setMenuLabel(menu,"Show Invisibles","Hide Invisibles")
            else:   frame.menu.setMenuLabel(menu,"Hide Invisibles","Show Invisibles")
    
        c.frame.body.recolor_now(p)
    #@-node:AGP.20250415230112.436:show/hide/toggleInvisibles
    #@+node:AGP.20250415230112.437:preferences
    def preferences (self,event=None):
        
        '''Handle the preferences command.'''
        
        c = self
        c.openLeoSettings()
    #@-node:AGP.20250415230112.437:preferences
    #@-node:AGP.20250415230112.406:Edit top level
    #@+node:AGP.20250415230112.438:Edit Body submenu
    #@+node:AGP.20250415230112.439:convertAllBlanks
    def convertAllBlanks (self,event=None):
        
        '''Convert all blanks to tabs in the selected outline.'''
        
        c = self ; u = c.undoer ; undoType = 'Convert All Blanks'
        current = c.currentPosition()
    
        if g.app.batchMode:
            c.notValidInBatchMode(undoType)
            return
        
        d = g.scanDirectives(c)
        tabWidth  = d.get("tabwidth")
        c.beginUpdate()
        try: # In update...
            count = 0 ; dirtyVnodeList = []
            u.beforeChangeGroup(current,undoType)
            for p in current.self_and_subtree_iter():
                # g.trace(p.headString(),tabWidth)
                innerUndoData = u.beforeChangeNodeContents(p)
                if p == current:
                    changed,dirtyVnodeList2 = c.convertBlanks(event)
                    if changed:
                        count += 1
                        dirtyVnodeList.extend(dirtyVnodeList2)
                else:
                    changed = False ; result = []
                    text = p.t.bodyString
                    assert(g.isUnicode(text))
                    lines = string.split(text, '\n')
                    for line in lines:
                        i,w = g.skip_leading_ws_with_indent(line,0,tabWidth)
                        s = g.computeLeadingWhitespace(w,abs(tabWidth)) + line[i:] # use positive width.
                        if s != line: changed = True
                        result.append(s)
                    if changed:
                        count += 1
                        dirtyVnodeList2 = p.setDirty()
                        dirtyVnodeList.extend(dirtyVnodeList2)
                        result = string.join(result,'\n')
                        p.setTnodeText(result)
                        u.afterChangeNodeContents(p,undoType,innerUndoData)
            u.afterChangeGroup(current,undoType,dirtyVnodeList=dirtyVnodeList)
            g.es("blanks converted to tabs in %d nodes" % count) # Must come before c.endUpdate().
        finally:
            c.endUpdate(count > 0)
    #@-node:AGP.20250415230112.439:convertAllBlanks
    #@+node:AGP.20250415230112.440:convertAllTabs
    def convertAllTabs (self,event=None):
        
        '''Convert all tabs to blanks in the selected outline.'''
    
        c = self ; u = c.undoer ; undoType = 'Convert All Tabs'
        current = c.currentPosition()
    
        if g.app.batchMode:
            c.notValidInBatchMode(undoType)
            return
        theDict = g.scanDirectives(c)
        tabWidth  = theDict.get("tabwidth")
        c.beginUpdate()
        try: # In update:
            count = 0 ; dirtyVnodeList = []
            u.beforeChangeGroup(current,undoType)
            for p in current.self_and_subtree_iter():
                undoData = u.beforeChangeNodeContents(p)
                if p == current:
                    changed,dirtyVnodeList2 = self.convertTabs(event)
                    if changed:
                        count += 1
                        dirtyVnodeList.extend(dirtyVnodeList2)
                else:
                    result = [] ; changed = False
                    text = p.t.bodyString
                    assert(g.isUnicode(text))
                    lines = string.split(text, '\n')
                    for line in lines:
                        i,w = g.skip_leading_ws_with_indent(line,0,tabWidth)
                        s = g.computeLeadingWhitespace(w,-abs(tabWidth)) + line[i:] # use negative width.
                        if s != line: changed = True
                        result.append(s)
                    if changed:
                        count += 1
                        dirtyVnodeList2 = p.setDirty()
                        dirtyVnodeList.extend(dirtyVnodeList2)
                        result = string.join(result,'\n')
                        p.setTnodeText(result)
                        u.afterChangeNodeContents(p,undoType,undoData)
            u.afterChangeGroup(current,undoType,dirtyVnodeList=dirtyVnodeList)
            g.es("tabs converted to blanks in %d nodes" % count)
        finally:
            c.endUpdate(count > 0)
    #@-node:AGP.20250415230112.440:convertAllTabs
    #@+node:AGP.20250415230112.441:convertBlanks
    def convertBlanks (self,event=None):
        
        '''Convert all blanks to tabs in the selected node.'''
    
        c = self ; undoType = 'Convert Blanks'
        
        if g.app.batchMode:
            c.notValidInBatchMode(undoType)
            return False
    
        head,lines,tail,oldSel,oldYview = c.getBodyLines(expandSelection=True)
        result = [] ; changed = False
    
        # Use the relative @tabwidth, not the global one.
        theDict = g.scanDirectives(c)
        tabWidth  = theDict.get("tabwidth")
        if not tabWidth: return False
    
        for line in lines:
            s = g.optimizeLeadingWhitespace(line,abs(tabWidth)) # Use positive width.
            if s != line: changed = True
            result.append(s)
    
        if changed:
            result = string.join(result,'\n')
            dirtyVnodeList = c.updateBodyPane(head,result,tail,undoType,oldSel,oldYview) # Handles undo
        else:
            dirtyVnodeList = []
    
        return changed,dirtyVnodeList
    #@-node:AGP.20250415230112.441:convertBlanks
    #@+node:AGP.20250415230112.442:convertTabs
    def convertTabs (self,event=None):
        
        '''Convert all tabs to blanks in the selected node.'''
    
        c = self ; undoType = 'Convert Tabs'
        
        if g.app.batchMode:
            c.notValidInBatchMode(undoType)
            return False
    
        head,lines,tail,oldSel,oldYview = self.getBodyLines(expandSelection=True)
        result = [] ; changed = False
        
        # Use the relative @tabwidth, not the global one.
        theDict = g.scanDirectives(c)
        tabWidth  = theDict.get("tabwidth")
        if not tabWidth: return False,None
    
        for line in lines:
            i,w = g.skip_leading_ws_with_indent(line,0,tabWidth)
            s = g.computeLeadingWhitespace(w,-abs(tabWidth)) + line[i:] # use negative width.
            if s != line: changed = True
            result.append(s)
    
        if changed:
            result = string.join(result,'\n')
            dirtyVnodeList = c.updateBodyPane(head,result,tail,undoType,oldSel,oldYview) # Handles undo
        else:
            dirtyVnodeList = []
            
        return changed,dirtyVnodeList
    #@-node:AGP.20250415230112.442:convertTabs
    #@+node:AGP.20250415230112.443:createLastChildNode
    def createLastChildNode (self,parent,headline,body):
        
        '''A helper function for the three extract commands.'''
        
        c = self
        
        if body and len(body) > 0:
            body = string.rstrip(body)
        if not body or len(body) == 0:
            body = ""
    
        p = parent.insertAsLastChild()
        p.initHeadString(headline)
        p.setTnodeText(body)
        p.setDirty()
        c.validateOutline()
        return p
    #@-node:AGP.20250415230112.443:createLastChildNode
    #@+node:AGP.20250415230112.444:dedentBody
    def dedentBody (self,event=None):
        
        '''Remove one tab's worth of indentation from all presently selected lines.'''
        
        c = self ; undoType = 'Unindent' ; current = c.currentPosition()
        
        if g.app.batchMode:
            c.notValidInBatchMode(undoType)
            return
    
        d = g.scanDirectives(c,current) # Support @tab_width directive properly.
        tab_width = d.get("tabwidth",c.tab_width)
        head,lines,tail,oldSel,oldYview = self.getBodyLines()
        
        result = [] ; changed = False
        for line in lines:
            i, width = g.skip_leading_ws_with_indent(line,0,tab_width)
            s = g.computeLeadingWhitespace(width-abs(tab_width),tab_width) + line[i:]
            if s != line: changed = True
            result.append(s)
    
        if changed:
            result = string.join(result,'\n')
            c.updateBodyPane(head,result,tail,undoType,oldSel,oldYview)
    #@-node:AGP.20250415230112.444:dedentBody
    #@+node:AGP.20250415230112.445:extract
    def extract (self,event=None):
        
        '''Create child node from the elected body text, deleting all selected text.
        The text must start with a section reference.  This becomes the new child's headline.
        The body text of the new child node contains all selected lines that follow the section reference line.'''
    
        c = self ; u = c.undoer ; undoType = 'Extract'
        current = c.currentPosition()
        
        if g.app.batchMode:
            c.notValidInBatchMode(undoType)
            return
        
        head,lines,tail,oldSel,oldYview = self.getBodyLines()
        if not lines: return
        headline = lines[0].strip() ; del lines[0]
        
        if not lines:
            g.es("Nothing follows section name",color="blue")
            return
    
        # Remove leading whitespace from all body lines.
        junk, ws = g.skip_leading_ws_with_indent(lines[0],0,c.tab_width)
        strippedLines = [g.removeLeadingWhitespace(line,ws,c.tab_width)
            for line in lines]
        newBody = string.join(strippedLines,'\n')
        if head: head = head.rstrip()
    
        c.beginUpdate()
        try: # In update...
            u.beforeChangeGroup(current,undoType)
            if 1: # In group...
                undoData = u.beforeInsertNode(current)
                p = c.createLastChildNode(current,headline,newBody)
                u.afterInsertNode(p,undoType,undoData)
                c.updateBodyPane(head,None,tail,undoType,oldSel,oldYview,setSel=False)
            u.afterChangeGroup(current,undoType)
        finally:
            c.endUpdate()
    #@-node:AGP.20250415230112.445:extract
    #@+node:AGP.20250415230112.446:extractSection
    def extractSection (self,event=None):
        
        '''Create a section definition node from the selected body text.
        The text must start with a section reference.  This becomes the new child's headline.
        The body text of the new child node contains all selected lines that follow the section reference line.'''
    
        c = self ; u = c.undoer ; undoType = 'Extract Section'
        current = c.currentPosition()
    
        if g.app.batchMode:
            c.notValidInBatchMode(undoType)
            return
        head,lines,tail,oldSel,oldYview = self.getBodyLines()
        if not lines: return
    
        line1 = '\n' + lines[0]
        headline = lines[0].strip() ; del lines[0]
        #@    << Set headline for extractSection >>
        #@+node:AGP.20250415230112.447:<< Set headline for extractSection >>
        if len(headline) < 5:
            oops = True
        else:
            head1 = headline[0:2] == '<<'
            head2 = headline[0:2] == '@<'
            tail1 = headline[-2:] == '>>'
            tail2 = headline[-2:] == '@>'
            oops = not (head1 and tail1) and not (head2 and tail2)
        
        if oops:
            g.es("Selected text should start with a section name",color="blue")
            return
        #@-node:AGP.20250415230112.447:<< Set headline for extractSection >>
        #@nl
        
        if not lines:
            g.es("Nothing follows section name",color="blue")
            return
        
        # Remove leading whitespace from all body lines.
        junk, ws = g.skip_leading_ws_with_indent(lines[0],0,c.tab_width)
        strippedLines = [g.removeLeadingWhitespace(line,ws,c.tab_width)
            for line in lines]
        newBody = string.join(strippedLines,'\n')
        if head: head = head.rstrip()
    
        c.beginUpdate()
        try: # In update...
            u.beforeChangeGroup(current,undoType)
            if 1: # In group...
                undoData = u.beforeInsertNode(current)
                p = c.createLastChildNode(current,headline,newBody)
                u.afterInsertNode(p,undoType,undoData)
                c.updateBodyPane(head+line1,None,tail,undoType,oldSel,oldYview,setSel=False)
            u.afterChangeGroup(current,undoType)
        finally:
            c.endUpdate()
    #@-node:AGP.20250415230112.446:extractSection
    #@+node:AGP.20250415230112.448:extractSectionNames
    def extractSectionNames(self,event=None):
        
        '''Create child nodes for every section reference in the selected text.
        The headline of each new child node is the section reference.
        The body of each child node is empty.'''
    
        c = self ; u = c.undoer ; undoType = 'Extract Section Names'
        body = c.frame.body ; current = c.currentPosition()
        
        if g.app.batchMode:
            c.notValidInBatchMode(undoType)
            return
        head,lines,tail,oldSel,oldYview = self.getBodyLines()
        if not lines: return
    
        c.beginUpdate()
        try: # In update...
            u.beforeChangeGroup(current,undoType)
            if 1: # In group...
                found = False
                for s in lines:
                    #@                << Find the next section name >>
                    #@+node:AGP.20250415230112.449:<< Find the next section name >>
                    head1 = string.find(s,"<<")
                    if head1 > -1:
                        head2 = string.find(s,">>",head1)
                    else:
                        head1 = string.find(s,"@<")
                        if head1 > -1:
                            head2 = string.find(s,"@>",head1)
                            
                    if head1 == -1 or head2 == -1 or head1 > head2:
                        name = None
                    else:
                        name = s[head1:head2+2]
                    #@-node:AGP.20250415230112.449:<< Find the next section name >>
                    #@nl
                    if name:
                        undoData = u.beforeInsertNode(current)
                        p = self.createLastChildNode(current,name,None)
                        u.afterInsertNode(p,undoType,undoData)
                        found = True
                c.selectPosition(current)
                c.validateOutline()
                if not found:
                    g.es("Selected text should contain one or more section names",color="blue")
            u.afterChangeGroup(current,undoType)
        finally:
            c.endUpdate()
    
        # Restore the selection.
        body.setTextSelection(oldSel)
        body.setFocus()
    #@-node:AGP.20250415230112.448:extractSectionNames
    #@+node:AGP.20250415230112.450:findBoundParagraph
    def findBoundParagraph (self,event=None):
        
        c = self
        head,ins,tail = c.frame.body.getInsertLines()
    
        if not ins or ins.isspace() or ins[0] == '@':
            return None,None,None,None # DTHEIN 18-JAN-2004
            
        head_lines = g.splitLines(head)
        tail_lines = g.splitLines(tail)
    
        if 0:
            #@        << trace head_lines, ins, tail_lines >>
            #@+node:AGP.20250415230112.451:<< trace head_lines, ins, tail_lines >>
            if 0:
                print ; print "head_lines"
                for line in head_lines: print line
                print ; print "ins", ins
                print ; print "tail_lines"
                for line in tail_lines: print line
            else:
                g.es("head_lines: ",head_lines)
                g.es("ins: ",ins)
                g.es("tail_lines: ",tail_lines)
            #@-node:AGP.20250415230112.451:<< trace head_lines, ins, tail_lines >>
            #@nl
    
        # Scan backwards.
        i = len(head_lines)
        while i > 0:
            i -= 1
            line = head_lines[i]
            if len(line) == 0 or line.isspace() or line[0] == '@':
                i += 1 ; break
    
        pre_para_lines = head_lines[:i]
        para_head_lines = head_lines[i:]
    
        # Scan forwards.
        i = 0
        trailingNL = False # DTHEIN 18-JAN-2004: properly capture terminating NL
        while i < len(tail_lines):
            line = tail_lines[i]
            if len(line) == 0 or line.isspace() or line[0] == '@':
                trailingNL = line.endswith(u'\n') or line.startswith(u'@') # DTHEIN 21-JAN-2004
                break
            i += 1
            
    #   para_tail_lines = tail_lines[:i]
        para_tail_lines = tail_lines[:i]
        post_para_lines = tail_lines[i:]
        
        head = g.joinLines(pre_para_lines)
        result = para_head_lines 
        result.extend([ins])
        result.extend(para_tail_lines)
        tail = g.joinLines(post_para_lines)
    
        # DTHEIN 18-JAN-2004: added trailingNL to return value list
        return head,result,tail,trailingNL # string, list, string, bool
    #@-node:AGP.20250415230112.450:findBoundParagraph
    #@+node:AGP.20250415230112.452:findMatchingBracket
    def findMatchingBracket (self,event=None):
        
        '''Selecte the text between matching brackets.'''
        
        c = self ; body = c.frame.body
        
        if g.app.batchMode:
            c.notValidInBatchMode("Match Brackets")
            return
    
        brackets = "()[]{}<>"
        ch1 = body.getCharBeforeInsertPoint()
        ch2 = body.getCharAtInsertPoint()
    
        # Prefer to match the character to the left of the cursor.
        if ch1 in brackets:
            ch = ch1 ; index = body.getBeforeInsertionPoint()
        elif ch2 in brackets:
            ch = ch2 ; index = body.getInsertionPoint()
        else:
            return
        
        index2 = self.findSingleMatchingBracket(ch,index)
        if index2:
            if body.compareIndices(index,"<=",index2):
                adj_index = body.adjustIndex(index2,1)
                body.setTextSelection(index,adj_index)
            else:
                adj_index = body.adjustIndex(index,1)
                body.setTextSelection(index2,adj_index)
            adj_index = body.adjustIndex(index2,1)
            body.setInsertionPoint(adj_index)
            body.makeIndexVisible(adj_index)
        else:
            g.es("unmatched '%s'",ch)
    #@+node:AGP.20250415230112.453:findMatchingBracket
    # To do: replace comments with blanks before scanning.
    # Test  unmatched())
    def findSingleMatchingBracket(self,ch,index):
        
        c = self ; body = c.frame.body
        open_brackets  = "([{<" ; close_brackets = ")]}>"
        brackets = open_brackets + close_brackets
        matching_brackets = close_brackets + open_brackets
        forward = ch in open_brackets
        # Find the character matching the initial bracket.
        for n in xrange(len(brackets)):
            if ch == brackets[n]:
                match_ch = matching_brackets[n]
                break
        level = 0
        while 1:
            if forward and body.compareIndices(index,">=","end"):
                # g.trace("not found")
                return None
            ch2 = body.getCharAtIndex(index)
            if ch2 == ch:
                level += 1 #; g.trace(level,index)
            if ch2 == match_ch:
                level -= 1 #; g.trace(level,index)
                if level <= 0:
                    return index
            if not forward and body.compareIndices(index,"<=","1.0"):
                # g.trace("not found")
                return None
            adj = g.choose(forward,1,-1)
            index = body.adjustIndex(index,adj)
        return 0
    #@-node:AGP.20250415230112.453:findMatchingBracket
    #@-node:AGP.20250415230112.452:findMatchingBracket
    #@+node:AGP.20250415230112.454:getBodyLines
    def getBodyLines (self,expandSelection=False):
        
        """Return head,lines,tail where:
            
        before is string containg all the lines before the selected text
        (or the text before the insert point if no selection)
        lines is a list of lines containing the selected text (or the line containing the insert point if no selection)
        after is a string all lines after the selected text
        (or the text after the insert point if no selection)"""
    
        c = self ; body = c.frame.body
        oldVview = body.getYScrollPosition()
        oldSel   = body.getTextSelection()
    
        if expandSelection: # 12/3/03
            lines = body.getAllText()
            head = tail = None
        else:
            # Note: lines is the entire line containing the insert point if no selection.
            head,lines,tail = body.getSelectionLines()
    
        lines = string.split(lines,'\n') # It would be better to use g.splitLines.
    
        return head,lines,tail,oldSel,oldVview
    #@-node:AGP.20250415230112.454:getBodyLines
    #@+node:AGP.20250415230112.455:indentBody
    def indentBody (self,event=None):
        
        '''The indent-region command indents each line of the selected body text,
        or each line of a node if there is no selected text. The @tabwidth directive
        in effect determines amount of indentation. (not yet) A numeric argument
        specifies the column to indent to.'''
    
        c = self ; undoType = 'Indent Region' ; current = c.currentPosition()
        
        if g.app.batchMode:
            c.notValidInBatchMode(undoType)
            return
    
        d = g.scanDirectives(c,current) # Support @tab_width directive properly.
        tab_width = d.get("tabwidth",c.tab_width)
        head,lines,tail,oldSel,oldYview = self.getBodyLines()
    
        result = [] ; changed = False
        for line in lines:
            i, width = g.skip_leading_ws_with_indent(line,0,tab_width)
            s = g.computeLeadingWhitespace(width+abs(tab_width),tab_width) + line[i:]
            if s != line: changed = True
            result.append(s)
    
        if changed:
            result = string.join(result,'\n')
            c.updateBodyPane(head,result,tail,undoType,oldSel,oldYview)
    #@-node:AGP.20250415230112.455:indentBody
    #@+node:AGP.20250415230112.456:insertBodyTime & allies
    def insertBodyTime (self,event=None):
        
        '''Insert a time/date stamp at the cursor.'''
        
        c = self ; undoType = 'Insert Body Time'
        
        if g.app.batchMode:
            c.notValidInBatchMode(undoType)
            return
        
        oldSel = c.frame.body.getTextSelection()
        c.frame.body.deleteTextSelection() # Works if nothing is selected.
        s = self.getTime(body=True)
    
        c.frame.body.insertAtInsertPoint(s)
        c.frame.body.onBodyChanged(undoType,oldSel=oldSel)
    #@+node:AGP.20250415230112.457:getTime & test
    def getTime (self,body=True):
    
        c = self
        default_format =  "%m/%d/%Y %H:%M:%S" # E.g., 1/30/2003 8:31:55
        
        # Try to get the format string from leoConfig.txt.
        if body:
            format = c.config.getString("body_time_format_string")
            gmt    = c.config.getBool("body_gmt_time")
        else:
            format = c.config.getString("headline_time_format_string")
            gmt    = c.config.getBool("headline_gmt_time")
    
        if format == None:
            format = default_format
    
        try:
            import time
            if gmt:
                s = time.strftime(format,time.gmtime())
            else:
                s = time.strftime(format,time.localtime())
        except (ImportError, NameError):
            g.es("time.strftime not available on this platform",color="blue")
            return ""
        except:
            g.es_exception() # Probably a bad format string in leoSettings.leo.
            s = time.strftime(default_format,time.gmtime())
        return s
    #@-node:AGP.20250415230112.457:getTime & test
    #@-node:AGP.20250415230112.456:insertBodyTime & allies
    #@+node:AGP.20250415230112.458:insert/removeComments
    #@+node:AGP.20250415230112.459:addComments
    def addComments (self,event=None):
        
        '''Convert all selected lines in the body text to comment lines.'''
    
        c = self ; undoType = 'Add Comments' ; p = c.currentPosition()
        
        d = g.scanDirectives(c,p)
        # d1 is the line delim.
        d1,d2,d3 = d.get('delims')
    
        head,lines,tail,oldSel,oldYview = self.getBodyLines()
        result = []
        if not lines:
            g.es('No text selected',color='blue')
            return
        
        if d1:
            # Append the single-line comment delim in front of each line
            for line in lines:
                i = g.skip_ws(line,0)
                result.append('%s%s %s' % (line[0:i],d1,line[i:]))
        else:
            n = len(lines)
            for i in xrange(n):
                line = lines[i]
                if i not in (0,n-1):
                    result.append(line)
                if i == 0:
                    j = g.skip_ws(line,0)
                    result.append('%s%s %s' % (line[0:j],d2,line[j:]))
                if i == n-1:
                    j = len(line.rstrip())
                    result.append('%s %s' % (line[0:j],d3))
    
        result = string.join(result,'\n')
        c.updateBodyPane(head,result,tail,undoType,oldSel,oldYview)
    #@-node:AGP.20250415230112.459:addComments
    #@+node:AGP.20250415230112.460:deleteComments
    def deleteComments (self,event=None):
        
        '''Remove one level of comment delimiters from all selected lines in the body text.'''
    
        c = self ; undoType = 'Delete Comments' ; p = c.currentPosition()
        
        d = g.scanDirectives(c,p)
        # d1 is the line delim.
        d1,d2,d3 = d.get('delims')
    
        head,lines,tail,oldSel,oldYview = self.getBodyLines()
        result = []
        if not lines:
            g.es('No text selected',color='blue')
            return
        
        if d1:
            # Append the single-line comment delim in front of each line
            for line in lines:
                i = g.skip_ws(line,0)
                if g.match(line,i,d1):
                    j = g.skip_ws(line,i + len(d1))
                    result.append(line[0:i] + line[j:])
                else:
                    result.append(line)
        else:
            n = len(lines)
            for i in xrange(n):
                line = lines[i]
                if i not in (0,n-1):
                    result.append(line)
                if i == 0:
                    j = g.skip_ws(line,0)
                    if g.match(line,j,d2):
                        k = g.skip_ws(line,j + len(d2))
                        result.append(line[0:j] + line[k:])
                    else:
                        g.es("'%s' not found" % (d2),color='blue')
                        return
                if i == n-1:
                    if i == 0:
                        line = result[0] ; result = []
                    s = line.rstrip()
                    if s.endswith(d3):
                        result.append(s[:-len(d3)].rstrip())
                    else:
                        g.es("'%s' not found" % (d3),color='blue')
                        return
    
        result = string.join(result,'\n')
        c.updateBodyPane(head,result,tail,undoType,oldSel,oldYview)
    #@-node:AGP.20250415230112.460:deleteComments
    #@-node:AGP.20250415230112.458:insert/removeComments
    #@+node:AGP.20250415230112.461:reformatParagraph
    def reformatParagraph (self,event=None):
    
        """Reformat a text paragraph in a Tk.Text widget
    
    Wraps the concatenated text to present page width setting. Leading tabs are
    sized to present tab width setting. First and second line of original text is
    used to determine leading whitespace in reformatted text. Hanging indentation
    is honored.
    
    Paragraph is bound by start of body, end of body, blank lines, and lines
    starting with "@". Paragraph is selected by position of current insertion
    cursor."""
    
        c = self ; body = c.frame.body
        
        if g.app.batchMode:
            c.notValidInBatchMode("xxx")
            return
    
        if body.hasTextSelection():
            g.es("Text selection inhibits Reformat Paragraph",color="blue")
            return
    
        #@    << compute vars for reformatParagraph >>
        #@+node:AGP.20250415230112.462:<< compute vars for reformatParagraph >>
        theDict = g.scanDirectives(c)
        pageWidth = theDict.get("pagewidth")
        tabWidth  = theDict.get("tabwidth")
        
        original = body.getAllText()
        oldSel   = body.getTextSelection()
        oldYview = body.getYScrollPosition()
        head,lines,tail,trailingNL = c.findBoundParagraph() # DTHEIN 18-JAN-2004: add trailingNL
        #@-node:AGP.20250415230112.462:<< compute vars for reformatParagraph >>
        #@nl
        if lines:
            #@        << compute the leading whitespace >>
            #@+node:AGP.20250415230112.463:<< compute the leading whitespace >>
            indents = [0,0] ; leading_ws = ["",""]
            
            for i in (0,1):
                if i < len(lines):
                    # Use the original, non-optimized leading whitespace.
                    leading_ws[i] = ws = g.get_leading_ws(lines[i])
                    indents[i] = g.computeWidth(ws,tabWidth)
                    
            indents[1] = max(indents)
            if len(lines) == 1:
                leading_ws[1] = leading_ws[0]
            #@-node:AGP.20250415230112.463:<< compute the leading whitespace >>
            #@nl
            #@        << compute the result of wrapping all lines >>
            #@+node:AGP.20250415230112.464:<< compute the result of wrapping all lines >>
            # Remember whether the last line ended with a newline.
            lastLine = lines[-1]
            if 0: # DTHEIN 18-JAN-2004: removed because findBoundParagraph now gives trailingNL
                trailingNL = lastLine and lastLine[-1] == '\n'
            
            # Remove any trailing newlines for wraplines.
            lines = [line[:-1] for line in lines[:-1]]
            if lastLine and not trailingNL:
                lastLine = lastLine[:-1]
            lines.extend([lastLine])
            
            # Wrap the lines, decreasing the page width by indent.
            result = g.wrap_lines(lines,
                pageWidth-indents[1],
                pageWidth-indents[0])
            
            # DTHEIN 18-JAN-2004
            # prefix with the leading whitespace, if any
            paddedResult = []
            paddedResult.append(leading_ws[0] + result[0])
            for line in result[1:]:
                paddedResult.append(leading_ws[1] + line)
            
            # Convert the result to a string.
            result = '\n'.join(paddedResult) # DTHEIN 18-JAN-2004: use paddedResult
            if 0: # DTHEIN 18-JAN-2004:  No need to do this.
                if trailingNL:
                    result += '\n'
            #@-node:AGP.20250415230112.464:<< compute the result of wrapping all lines >>
            #@nl
            #@        << update the body, selection & undo state >>
            #@+node:AGP.20250415230112.465:<< update the body, selection & undo state >>
            sel_start, sel_end = body.setSelectionAreas(head,result,tail)
            
            changed = original != head + result + tail
            undoType = g.choose(changed,"Reformat Paragraph",None)
            body.onBodyChanged(undoType,oldSel=oldSel,oldYview=oldYview)
            
            # Advance the selection to the next paragraph.
            newSel = sel_end, sel_end
            body.setTextSelection(newSel)
            body.makeIndexVisible(sel_end)
            
            c.recolor()
            #@-node:AGP.20250415230112.465:<< update the body, selection & undo state >>
            #@nl
    #@-node:AGP.20250415230112.461:reformatParagraph
    #@+node:AGP.20250415230112.466:updateBodyPane (handles changeNodeContents)
    def updateBodyPane (self,head,middle,tail,undoType,oldSel,oldYview,setSel=True):
        
        c = self ; body = c.frame.body ; p = c.currentPosition()
        
        # g.trace(undoType)
    
        # Update the text and notify the event handler.
        body.setSelectionAreas(head,middle,tail)
    
        if setSel and oldSel:
            body.setTextSelection(oldSel)
    
        # This handles the undo.
        body.onBodyChanged(undoType,oldSel=oldSel,oldYview=oldYview)
    
        # Update the changed mark and icon.
        c.beginUpdate()
        try: # In update...
            c.setChanged(True)
            if p.isDirty():
                dirtyVnodeList = []
            else:
                dirtyVnodeList = p.setDirty()
        finally:
            c.endUpdate()
    
        # Scroll as necessary.
        if oldYview:
            body.setYScrollPosition(oldYview)
        else:
            body.makeInsertPointVisible()
    
        body.setFocus()
        c.recolor()
        return dirtyVnodeList
    #@-node:AGP.20250415230112.466:updateBodyPane (handles changeNodeContents)
    #@-node:AGP.20250415230112.438:Edit Body submenu
    #@+node:AGP.20250415230112.467:Edit Headline submenu
    #@+node:AGP.20250415230112.468:editHeadline
    def editHeadline (self,event=None):
        
        '''Begin editing the headline of the selected node.'''
        
        c = self ; k = c.k ; tree = c.frame.tree
        
        if g.app.batchMode:
            c.notValidInBatchMode("Edit Headline")
            return
            
        if k:
            k.setDefaultUnboundKeyAction()
            k.showStateAndMode()
    
        tree.editLabel(c.currentPosition())
    #@-node:AGP.20250415230112.468:editHeadline
    #@+node:AGP.20250415230112.469:toggleAngleBrackets
    def toggleAngleBrackets (self,event=None):
        
        '''Add or remove double angle brackets from the headline of the selected node.'''
        
        c = self ; v = c.currentVnode()
        
        if g.app.batchMode:
            c.notValidInBatchMode("Toggle Angle Brackets")
            return
            
        c.endEditing()
    
        s = v.headString().strip()
        if (s[0:2] == "<<"
            or s[-2:] == ">>"): # Must be on separate line.
            if s[0:2] == "<<": s = s[2:]
            if s[-2:] == ">>": s = s[:-2]
            s = s.strip()
        else:
            s = g.angleBrackets(' ' + s + ' ')
        
        c.frame.tree.editLabel(v)
        w = c.edit_widget(v)
        if w:
            w.delete("1.0","end")
            w.insert("1.0",s)
            c.frame.tree.onHeadChanged(v,'Toggle Angle Brackets')
    #@-node:AGP.20250415230112.469:toggleAngleBrackets
    #@-node:AGP.20250415230112.467:Edit Headline submenu
    #@+node:AGP.20250415230112.470:Find submenu (frame methods)
    #@+node:AGP.20250415230112.471:dismissFindPanel
    def dismissFindPanel (self,event=None):
        
        c = self
        
        if c.frame.findPanel:
            c.frame.findPanel.dismiss()
    #@-node:AGP.20250415230112.471:dismissFindPanel
    #@+node:AGP.20250415230112.472:showFindPanel
    def showFindPanel (self,event=None):
    
        '''Open Leo's legacy Find dialog.'''
        
        c = self
        
        if not c.frame.findPanel:
            c.frame.findPanel = g.app.gui.createFindPanel(c)
    
        c.frame.findPanel.bringToFront()
    #@-node:AGP.20250415230112.472:showFindPanel
    #@+node:AGP.20250415230112.473:findNext
    def findNext (self,event=None):
    
        c = self
        
        if not c.frame.findPanel:
            c.frame.findPanel = g.app.gui.createFindPanel(c)
    
        c.frame.findPanel.findNextCommand(c)
    #@-node:AGP.20250415230112.473:findNext
    #@+node:AGP.20250415230112.474:findPrevious
    def findPrevious (self,event=None):
    
        c = self
        
        if not c.frame.findPanel:
            c.frame.findPanel = g.app.gui.createFindPanel(c)
    
        c.frame.findPanel.findPreviousCommand(c)
    #@-node:AGP.20250415230112.474:findPrevious
    #@+node:AGP.20250415230112.475:replace
    def replace (self,event=None):
    
        c = self
        
        if not c.frame.findPanel:
            c.frame.findPanel = g.app.gui.createFindPanel(c)
    
        c.frame.findPanel.changeCommand(c)
    #@-node:AGP.20250415230112.475:replace
    #@+node:AGP.20250415230112.476:replaceThenFind
    def replaceThenFind (self,event=None):
    
        c = self
        
        if not c.frame.findPanel:
            c.frame.findPanel = g.app.gui.createFindPanel(c)
    
        c.frame.findPanel.changeThenFindCommand(c)
    #@-node:AGP.20250415230112.476:replaceThenFind
    #@+node:AGP.20250415230112.477:replaceAll
    def replaceAll (self,event=None):
    
        c = self
        
        if not c.frame.findPanel:
            c.frame.findPanel = g.app.gui.createFindPanel(c)
    
        c.frame.findPanel.changeAllCommand(c)
    #@-node:AGP.20250415230112.477:replaceAll
    #@-node:AGP.20250415230112.470:Find submenu (frame methods)
    #@+node:AGP.20250415230112.478:notValidInBatchMode
    def notValidInBatchMode(self, commandName):
        
        g.es("%s command is not valid in batch mode" % commandName)
    #@-node:AGP.20250415230112.478:notValidInBatchMode
    #@-node:AGP.20250415230112.405:Edit Menu...
    #@+node:AGP.20250415230112.479:Outline menu...
    #@+node:AGP.20250415230112.480: Top Level... (Commands)
    #@+node:AGP.20250415230112.481:Cut & Paste Outlines
    #@+node:AGP.20250415230112.482:cutOutline
    def cutOutline (self,event=None):
        
        '''Delete the selected outline and send it to the clipboard.'''
    
        c = self
        if c.canDeleteHeadline():
            c.copyOutline()
            c.deleteOutline("Cut Node")
            c.recolor()
    #@-node:AGP.20250415230112.482:cutOutline
    #@+node:AGP.20250415230112.483:copyOutline
    def copyOutline (self,event=None):
        
        '''Copy the selected outline to the clipboard.'''
    
        # Copying an outline has no undo consequences.
        c = self
        c.endEditing()
        c.fileCommands.assignFileIndices()
        s = c.fileCommands.putLeoOutline()
        g.app.gui.replaceClipboardWith(s)
    #@-node:AGP.20250415230112.483:copyOutline
    #@+node:AGP.20250415230112.484:pasteOutline
    # To cut and paste between apps, just copy into an empty body first, then copy to Leo's clipboard.
    
    def pasteOutline(self,event=None,reassignIndices=True):
        
        '''Paste an outline into the present outline from the clipboard.
        Nodes do *not* retain their original identify.'''
    
        c = self ; u = c.undoer ; current = c.currentPosition()
        s = g.app.gui.getTextFromClipboard()
        pasteAsClone = not reassignIndices
        undoType = g.choose(reassignIndices,'Paste Node','Paste As Clone')
        
        c.endEditing()
    
        if not s or not c.canPasteOutline(s):
            return # This should never happen.
    
        isLeo = g.match(s,0,g.app.prolog_prefix_string)
        tnodeInfoDict = {}
        if pasteAsClone:
            #@        << remember all data for undo/redo Paste As Clone >>
            #@+node:AGP.20250415230112.485:<< remember all data for undo/redo Paste As Clone >>
            #@+at
            # 
            # We don't know yet which nodes will be affected by the paste, so 
            # we remember
            # everything. This is expensive, but foolproof.
            # 
            # The alternative is to try to remember the 'before' values of 
            # tnodes in the
            # fileCommands read logic. Several experiments failed, and the 
            # code is very ugly.
            # In short, it seems wise to do things the foolproof way.
            # 
            #@-at
            #@@c
            
            for p in c.allNodes_iter():
                t = p.v.t
                if t not in tnodeInfoDict.keys():
                    tnodeInfoDict[t] = g.Bunch(
                        t=t,head=p.headString(),body=p.bodyString())
            #@-node:AGP.20250415230112.485:<< remember all data for undo/redo Paste As Clone >>
            #@nl
    
        if isLeo:
            pasted = c.fileCommands.getLeoOutline(s,reassignIndices)
        else:
            pasted = c.importCommands.convertMoreStringToOutlineAfter(s,current)
        if not pasted: return
    
        c.beginUpdate()
        try:
            copiedBunchList = []
            if pasteAsClone:
                #@            << put only needed info in copiedBunchList >>
                #@+node:AGP.20250415230112.486:<< put only needed info in copiedBunchList >>
                # Create a dict containing only copied tnodes.
                copiedTnodeDict = {}
                for p in pasted.self_and_subtree_iter():
                    if p.v.t not in copiedTnodeDict:
                        copiedTnodeDict[p.v.t] = p.v.t
                        
                # g.trace(copiedTnodeDict.keys())
                
                for t in tnodeInfoDict.keys():
                    bunch = tnodeInfoDict.get(t)
                    if copiedTnodeDict.get(t):
                        copiedBunchList.append(bunch)
                
                # g.trace('copiedBunchList',copiedBunchList)
                #@-node:AGP.20250415230112.486:<< put only needed info in copiedBunchList >>
                #@nl
            undoData = u.beforeInsertNode(current,
                pasteAsClone=pasteAsClone,copiedBunchList=copiedBunchList)
            c.endEditing()
            c.validateOutline()
            c.selectPosition(pasted)
            pasted.setDirty()
            c.setChanged(True)
            # paste as first child if back is expanded.
            back = pasted.back()
            if back and back.isExpanded():
                pasted.moveToNthChildOf(back,0)
            c.setRootPosition(c.findRootPosition(pasted)) # New in 4.4.2.
            u.afterInsertNode(pasted,undoType,undoData)
        finally:
            c.endUpdate()
            c.recolor()
    #@-node:AGP.20250415230112.484:pasteOutline
    #@+node:AGP.20250415230112.487:pasteOutlineRetainingClones
    def pasteOutlineRetainingClones (self,event=None):
        
        '''Paste an outline into the present outline from the clipboard.
        Nodes *retain* their original identify.'''
        
        c = self
    
        return c.pasteOutline(reassignIndices=False)
    #@-node:AGP.20250415230112.487:pasteOutlineRetainingClones
    #@-node:AGP.20250415230112.481:Cut & Paste Outlines
    #@+node:AGP.20250415230112.488:Hoist & dehoist
    def dehoist (self,event=None):
        
        '''Undo a previous hoist of an outline.'''
    
        c = self ; p = c.currentPosition()
        if p and c.canDehoist():
            bunch = c.hoistStack.pop()
            c.beginUpdate()
            try:
                if bunch.expanded: p.expand()
                else:              p.contract()
            finally:
                c.endUpdate()
            c.frame.clearStatusLine()
            if c.hoistStack:
                bunch = c.hoistStack[-1]
                c.frame.putStatusLine("Hoist: " + bunch.p.headString())
            else:
                c.frame.putStatusLine("No hoist")
            c.undoer.afterDehoist(p,'DeHoist')
    
    def hoist (self,event=None):
        
        '''Make only the selected outline visible.'''
    
        c = self ; p = c.currentPosition()
        if p and c.canHoist():
            # Remember the expansion state.
            bunch = g.Bunch(p=p.copy(),expanded=p.isExpanded())
            c.hoistStack.append(bunch)
            c.beginUpdate()
            try:
                p.expand()
            finally:
                c.endUpdate()
            c.frame.clearStatusLine()
            c.frame.putStatusLine("Hoist: " + p.headString())
            c.undoer.afterHoist(p,'Hoist')
    #@-node:AGP.20250415230112.488:Hoist & dehoist
    #@+node:AGP.20250415230112.489:Insert, Delete & Clone (Commands)
    #@+node:AGP.20250415230112.490:c.checkMoveWithParentWithWarning
    def checkMoveWithParentWithWarning (self,root,parent,warningFlag):
        
        """Return False if root or any of root's descedents is a clone of
        parent or any of parents ancestors."""
    
        message = "Illegal move or drag: no clone may contain a clone of itself"
    
        # g.trace("root",root,"parent",parent)
        clonedTnodes = {}
        for ancestor in parent.self_and_parents_iter():
            if ancestor.isCloned():
                t = ancestor.v.t
                clonedTnodes[t] = t
    
        if not clonedTnodes:
            return True
    
        for p in root.self_and_subtree_iter():
            if p.isCloned() and clonedTnodes.get(p.v.t):
                if warningFlag:
                    g.alert(message)
                return False
        return True
    #@-node:AGP.20250415230112.490:c.checkMoveWithParentWithWarning
    #@+node:AGP.20250415230112.491:c.deleteOutline
    def deleteOutline (self,event=None,op_name="Delete Node"):
        
        """Deletes the selected outline."""
    
        c = self ; u = c.undoer ; p = c.currentPosition()
        if not p: return
    
        if p.hasVisBack(): newNode = p.visBack()
        else: newNode = p.next() # _not_ p.visNext(): we are at the top level.
        if not newNode: return
    
        c.beginUpdate()
        try:
           c.endEditing() # Make sure we capture the headline for Undo.
           undoData = u.beforeDeleteNode(p)
           dirtyVnodeList = p.setAllAncestorAtFileNodesDirty()
           p.doDelete()
           c.selectPosition(newNode)
           c.setChanged(True)
           u.afterDeleteNode(newNode,op_name,undoData,dirtyVnodeList=dirtyVnodeList)
        finally:
            c.endUpdate()
    
        c.validateOutline()
    #@-node:AGP.20250415230112.491:c.deleteOutline
    #@+node:AGP.20250415230112.492:c.insertHeadline
    def insertHeadline (self,event=None,op_name="Insert Node"):
        
        '''Insert a node after the presently selected node.'''
    
        c = self ; u = c.undoer
        current = c.currentPosition()
        
        if not current: return
    
        c.beginUpdate()
        try:
            undoData = c.undoer.beforeInsertNode(current)
            # Make sure the new node is visible when hoisting.
            if (
                (current.hasChildren() and current.isExpanded()) or
                (c.hoistStack and current == c.hoistStack[-1].p)
            ):
                if c.config.getBool('insert_new_nodes_at_end'):
                    p = current.insertAsLastChild()
                else:
                    p = current.insertAsNthChild(0)
            else:
                p = current.insertAfter()
            dirtyVnodeList = p.setAllAncestorAtFileNodesDirty()
            c.setChanged(True)
            u.afterInsertNode(p,op_name,undoData,dirtyVnodeList=dirtyVnodeList)
        finally:
            c.endUpdate()
        c.beginUpdate()
        try:
            c.editPosition(p,selectAll=True)
        finally:
            c.endUpdate(False)
    
        return p # for mod_labels plugin.
    #@-node:AGP.20250415230112.492:c.insertHeadline
    #@+node:AGP.20250415230112.493:c.clone
    def clone (self,event=None):
        
        '''Create a clone of the selected outline.'''
    
        c = self ; u = c.undoer ; p = c.currentPosition()
        if not p: return
        
        c.beginUpdate()
        try: # In update...
            undoData = c.undoer.beforeCloneNode(p)
            clone = p.clone()
            dirtyVnodeList = clone.setAllAncestorAtFileNodesDirty()
            c.setChanged(True)
            if c.validateOutline():
                u.afterCloneNode(clone,'Clone Node',undoData,dirtyVnodeList=dirtyVnodeList)
                c.selectPosition(clone)
        finally:
            c.endUpdate()
    
        return clone # For mod_labels and chapters plugins.
    #@-node:AGP.20250415230112.493:c.clone
    #@+node:AGP.20250415230112.494:c.validateOutline
    # Makes sure all nodes are valid.
    
    def validateOutline (self,event=None):
    
        c = self
        
        if not g.app.debug:
            return True
    
        root = c.rootPosition()
        parent = c.nullPosition()
    
        if root:
            return root.validateOutlineWithParent(parent)
        else:
            return True
    #@-node:AGP.20250415230112.494:c.validateOutline
    #@-node:AGP.20250415230112.489:Insert, Delete & Clone (Commands)
    #@+node:AGP.20250415230112.495:c.sortChildren
    def sortChildren (self,event=None):
        
        '''Sort the children of a node.'''
    
        c = self ; u = c.undoer ; undoType = 'Sort Children'
        p = c.currentPosition()
        if not p or not p.hasChildren(): return
    
        c.beginUpdate()
        try: # In update
            c.endEditing()
            u.beforeChangeGroup(p,undoType)
            c.sortChildrenHelper(p)
            dirtyVnodeList = p.setAllAncestorAtFileNodesDirty()
            c.setChanged(True)
            u.afterChangeGroup(p,undoType,dirtyVnodeList=dirtyVnodeList)
        finally:
            c.endUpdate()
    #@-node:AGP.20250415230112.495:c.sortChildren
    #@+node:AGP.20250415230112.496:c.sortChildrenHelper
    def sortChildrenHelper (self,p):
        
        c = self ; u = c.undoer
    
        # Create a list of tuples sorted on headlines.
        pairs = [(child.headString().lower(),child.copy()) for child in p.children_iter()]
        pairs.sort()
    
        # Move the children.
        index = 0
        for headline,child in pairs:
            undoData = u.beforeMoveNode(child)
            child.moveToNthChildOf(p,index)
            u.afterMoveNode(child,'Sort',undoData)
            index += 1
    #@nonl
    #@-node:AGP.20250415230112.496:c.sortChildrenHelper
    #@+node:AGP.20250415230112.497:c.sortSiblings
    def sortSiblings (self,event=None):
        
        '''Sort the siblings of a node.'''
        
        c = self ; u = c.undoer ; undoType = 'Sort Siblings'
        p = c.currentPosition()
        if not p: return
    
        parent = p.parent()
        if not parent:
            c.sortTopLevel()
        else:
            c.beginUpdate()
            try: # In update...
                c.endEditing()
                u.beforeChangeGroup(p,undoType)
                c.sortChildrenHelper(parent)
                dirtyVnodeList = parent.setAllAncestorAtFileNodesDirty()
                c.setChanged(True)
                u.afterChangeGroup(p,'Sort Siblings',dirtyVnodeList=dirtyVnodeList)
            finally:
                c.endUpdate()
    #@-node:AGP.20250415230112.497:c.sortSiblings
    #@+node:AGP.20250415230112.498:c.sortTopLevel
    def sortTopLevel (self,event=None):
        
        '''Sort the top-level nodes of an outline.'''
    
        c = self ; u = c.undoer ; undoType = 'Sort Siblings'
        root = c.rootPosition()
        if not root: return
    
        # Create a list of tuples sorted by headlines.
        pairs = [(p.headString().lower(),p.copy())
            for p in root.self_and_siblings_iter()]
        pairs.sort()
     
        c.beginUpdate()
        try: # In update...
            dirtyVnodeList = []
            u.beforeChangeGroup(root,undoType)
            if 1: # In group...
                h,p = pairs[0]
                if p != root:
                    undoData = u.beforeMoveNode(p)
                    dirtyVnodeList2 = p.setAllAncestorAtFileNodesDirty()
                    dirtyVnodeList.extend(dirtyVnodeList2)
                    p.moveToRoot(oldRoot=root)
                    dirtyVnodeList2 = p.setAllAncestorAtFileNodesDirty()
                    dirtyVnodeList.extend(dirtyVnodeList2)
                    u.afterMoveNode(p,'Sort',undoData)
                for h,next in pairs[1:]:
                    undoData = u.beforeMoveNode(next)
                    next.moveAfter(p)
                    u.afterMoveNode(next,'Sort',undoData)
                    p = next
                c.setRootPosition(c.findRootPosition(root)) # New in 4.4.2.
            u.afterChangeGroup(root,undoType,dirtyVnodeList=dirtyVnodeList)
        finally:
            c.endUpdate()
    #@-node:AGP.20250415230112.498:c.sortTopLevel
    #@-node:AGP.20250415230112.480: Top Level... (Commands)
    #@+node:AGP.20250415230112.499:Check Outline submenu...
    #@+node:AGP.20250415230112.500:c.checkOutline
    def checkOutline (self,event=None,verbose=True,unittest=False,full=True):
        
        """Report any possible clone errors in the outline.
        
        Remove any unused tnodeLists."""
        
        c = self ; count = 1 ; errors = 0
        isTkinter = g.app.gui and g.app.gui.guiName() == "tkinter"
    
        if full and not unittest:
            g.es("all tests enabled: this may take awhile",color="blue")
    
        p = c.rootPosition()
        for p in c.allNodes_iter():
            try:
                count += 1
                #@            << remove unused tnodeList >>
                #@+node:AGP.20250415230112.501:<< remove unused tnodeList >>
                # Empty tnodeLists are not errors.
                v = p.v
                
                # New in 4.2: tnode list is in tnode.
                if hasattr(v.t,"tnodeList") and len(v.t.tnodeList) > 0 and not v.isAnyAtFileNode():
                    if 0:
                        s = "deleting tnodeList for " + repr(v)
                        print ; g.es_print(s,color="blue")
                    delattr(v.t,"tnodeList")
                    v.t._p_changed = True
                #@-node:AGP.20250415230112.501:<< remove unused tnodeList >>
                #@nl
                if full: # Unit tests usually set this false.
                    #@                << do full tests >>
                    #@+node:AGP.20250415230112.502:<< do full tests >>
                    if not unittest:
                        if count % 100 == 0:
                            g.es('.',newline=False)
                        if count % 2000 == 0:
                            g.enl()
                    
                    #@+others
                    #@+node:AGP.20250415230112.503:assert consistency of threadNext & threadBack links
                    threadBack = p.threadBack()
                    threadNext = p.threadNext()
                    
                    if threadBack:
                        assert p == threadBack.threadNext(), "p==threadBack.threadNext"
                    
                    if threadNext:
                        assert p == threadNext.threadBack(), "p==threadNext.threadBack"
                    #@-node:AGP.20250415230112.503:assert consistency of threadNext & threadBack links
                    #@+node:AGP.20250415230112.504:assert consistency of next and back links
                    back = p.back()
                    next = p.next()
                    
                    if back:
                        assert p == back.next(), "p==back.next"
                            
                    if next:
                        assert p == next.back(), "p==next.back"
                    #@-node:AGP.20250415230112.504:assert consistency of next and back links
                    #@+node:AGP.20250415230112.505:assert consistency of parent and child links
                    if p.hasParent():
                        n = p.childIndex()
                        assert p == p.parent().moveToNthChild(n), "p==parent.moveToNthChild"
                        
                    for child in p.children_iter():
                        assert p == child.parent(), "p==child.parent"
                    
                    if p.hasNext():
                        assert p.next().parent() == p.parent(), "next.parent==parent"
                        
                    if p.hasBack():
                        assert p.back().parent() == p.parent(), "back.parent==parent"
                    #@-node:AGP.20250415230112.505:assert consistency of parent and child links
                    #@+node:AGP.20250415230112.506:assert consistency of directParents and parent
                    if p.hasParent():
                        t = p.parent().v.t
                        for v in p.directParents():
                            try:
                                assert v.t == t
                            except:
                                print "p",p
                                print "p.directParents",p.directParents()
                                print "v",v
                                print "v.t",v.t
                                print "t = p.parent().v.t",t
                                raise AssertionError,"v.t == t"
                    #@-node:AGP.20250415230112.506:assert consistency of directParents and parent
                    #@+node:AGP.20250415230112.507:assert consistency of p.v.t.vnodeList, & v.parents for cloned nodes
                    if p.isCloned():
                        parents = p.v.t.vnodeList
                        for child in p.children_iter():
                            vparents = child.directParents()
                            assert len(parents) == len(vparents), "len(parents) == len(vparents)"
                            for parent in parents:
                                assert parent in vparents, "parent in vparents"
                            for parent in vparents:
                                assert parent in parents, "parent in parents"
                    #@-node:AGP.20250415230112.507:assert consistency of p.v.t.vnodeList, & v.parents for cloned nodes
                    #@+node:AGP.20250415230112.508:assert that clones actually share subtrees
                    if p.isCloned() and p.hasChildren():
                        childv = p.firstChild().v
                        assert childv == p.v.t._firstChild, "childv == p.v.t._firstChild"
                        assert id(childv) == id(p.v.t._firstChild), "id(childv) == id(p.v.t._firstChild)"
                        for v in p.v.t.vnodeList:
                            assert v.t._firstChild == childv, "v.t._firstChild == childv"
                            assert id(v.t._firstChild) == id(childv), "id(v.t._firstChild) == id(childv)"
                    #@-node:AGP.20250415230112.508:assert that clones actually share subtrees
                    #@+node:AGP.20250415230112.509:assert consistency of vnodeList
                    vnodeList = p.v.t.vnodeList
                        
                    for v in vnodeList:
                        
                        try:
                            assert v.t == p.v.t
                        except AssertionError:
                            print "p",p
                            print "v",v
                            print "p.v",p.v
                            print "v.t",v.t
                            print "p.v.t",p.v.t
                            raise AssertionError, "v.t == p.v.t"
                    
                        if p.v.isCloned():
                            assert v.isCloned(), "v.isCloned"
                            assert len(vnodeList) > 1, "len(vnodeList) > 1"
                        else:
                            assert not v.isCloned(), "not v.isCloned"
                            assert len(vnodeList) == 1, "len(vnodeList) == 1"
                    #@-node:AGP.20250415230112.509:assert consistency of vnodeList
                    #@+node:AGP.20250415230112.510:assert that p.headString() matches p.edit_text.get
                    # Not a great test: it only tests visible nodes.
                    # This test may fail if a joined node is being editred.
                    
                    if isTkinter:
                        t = c.edit_widget(p)
                        if t:
                            s = t.get("1.0","end")
                            assert p.headString().strip() == s.strip(), "May fail if joined node is being edited"
                    #@-node:AGP.20250415230112.510:assert that p.headString() matches p.edit_text.get
                    #@-others
                    #@-node:AGP.20250415230112.502:<< do full tests >>
                    #@nl
            except AssertionError,message:
                errors += 1
                #@            << give test failed message >>
                #@+node:AGP.20250415230112.511:<< give test failed message >>
                s = "test failed: %s %s" % (message,repr(p))
                print s ; g.es_print(s,color="red")
                #@-node:AGP.20250415230112.511:<< give test failed message >>
                #@nl
        if verbose or not unittest:
            #@        << print summary message >>
            #@+node:AGP.20250415230112.512:<<print summary message >>
            if full:
                print
                g.enl()
            
            s = "%d nodes checked, %d errors" % (count,errors)
            if errors or verbose:
                g.es_print(s,color="red")
            elif verbose:
                g.es(s,color="green")
            #@-node:AGP.20250415230112.512:<<print summary message >>
            #@nl
        return errors
    #@-node:AGP.20250415230112.500:c.checkOutline
    #@+node:AGP.20250415230112.513:Check Outline commands & allies
    #@+node:AGP.20250415230112.514:checkAllPythonCode
    def checkAllPythonCode(self,event=None,unittest=False,ignoreAtIgnore=True):
        
        '''Check all nodes in the selected tree for syntax and tab errors.'''
        
        c = self ; count = 0 ; result = "ok"
    
        for p in c.all_positions_iter():
            
            count += 1
            if not unittest:
                #@            << print dots >>
                #@+node:AGP.20250415230112.515:<< print dots >>
                if count % 100 == 0:
                    g.es('.',newline=False)
                
                if count % 2000 == 0:
                    g.enl()
                #@-node:AGP.20250415230112.515:<< print dots >>
                #@nl
    
            if g.scanForAtLanguage(c,p) == "python":
                if not g.scanForAtSettings(p) and (not ignoreAtIgnore or not g.scanForAtIgnore(c,p)):
                    try:
                        c.checkPythonNode(p,unittest)
                    except (SyntaxError,tokenize.TokenError,tabnanny.NannyNag):
                        result = "error" # Continue to check.
                    except:
                        import traceback ; traceback.print_exc()
                        return "surprise" # abort
                    if unittest and result != "ok":
                        print "Syntax error in %s" % p.cleanHeadString()
                        return result # End the unit test: it has failed.
                
        if not unittest:
            g.es("Check complete",color="blue")
            
        return result
    #@-node:AGP.20250415230112.514:checkAllPythonCode
    #@+node:AGP.20250415230112.516:checkPythonCode
    def checkPythonCode (self,event=None,unittest=False,ignoreAtIgnore=True,suppressErrors=False):
        
        '''Check the selected tree for syntax and tab errors.'''
        
        c = self ; count = 0 ; result = "ok"
        
        if not unittest:
            g.es("checking Python code   ")
        
        for p in c.currentPosition().self_and_subtree_iter():
            
            count += 1
            if not unittest:
                #@            << print dots >>
                #@+node:AGP.20250415230112.517:<< print dots >>
                if count % 100 == 0:
                    g.es('.',newline=False)
                
                if count % 2000 == 0:
                    g.enl()
                #@-node:AGP.20250415230112.517:<< print dots >>
                #@nl
    
            if g.scanForAtLanguage(c,p) == "python":
                if not ignoreAtIgnore or not g.scanForAtIgnore(c,p):
                    try:
                        c.checkPythonNode(p,unittest,suppressErrors)
                    except (parser.ParserError,SyntaxError,tokenize.TokenError,tabnanny.NannyNag):
                        result = "error" # Continue to check.
                    except:
                        g.es("surprise in checkPythonNode")
                        g.es_exception()
                        return "surprise" # abort
    
        if not unittest:
            g.es("Check complete",color="blue")
            
        # We _can_ return a result for unit tests because we aren't using doCommand.
        return result
    #@-node:AGP.20250415230112.516:checkPythonCode
    #@+node:AGP.20250415230112.518:checkPythonNode
    def checkPythonNode (self,p,unittest=False,suppressErrors=False):
    
        c = self
        
        h = p.headString()
        # We must call getScript so that we can ignore directives and section references.
        body = g.getScript(c,p.copy())
        if not body: return
    
        try:
            compiler.parse(body + '\n')
        except (parser.ParserError,SyntaxError):
            if not suppressErrors:
                s = "Syntax error in: %s" % h
                g.es_print(s,color="blue")
            if unittest: raise
            else:
                g.es_exception(full=False,color="black")
                c.setMarked(p)
    
        c.tabNannyNode(p,h,body,unittest,suppressErrors)
    #@-node:AGP.20250415230112.518:checkPythonNode
    #@+node:AGP.20250415230112.519:tabNannyNode
    # This code is based on tabnanny.check.
    
    def tabNannyNode (self,p,headline,body,unittest=False,suppressErrors=False):
    
        """Check indentation using tabnanny."""
        
        c = self
    
        try:
            # readline = g.readLinesGenerator(body).next
            readline = g.readLinesClass(body).next
            tabnanny.process_tokens(tokenize.generate_tokens(readline))
            return
            
        except parser.ParserError, msg:
            if not suppressErrors:
                g.es("ParserError in %s" % headline,color="blue")
                g.es(str(msg))
            
        except tokenize.TokenError, msg:
            if not suppressErrors:
                g.es("TokenError in %s" % headline,color="blue")
                g.es(str(msg))
    
        except tabnanny.NannyNag, nag:
            if not suppressErrors:
                badline = nag.get_lineno()
                line    = nag.get_line()
                message = nag.get_msg()
                g.es("Indentation error in %s, line %d" % (headline, badline),color="blue")
                g.es(message)
                g.es("offending line:\n%s" % repr(str(line))[1:-1])
            
        except:
            g.trace("unexpected exception")
            g.es_exception()
    
        if unittest: raise
        else: c.setMarked(p)
    #@-node:AGP.20250415230112.519:tabNannyNode
    #@-node:AGP.20250415230112.513:Check Outline commands & allies
    #@+node:AGP.20250415230112.520:c.dumpOutline
    def dumpOutline (self,event=None):
        
        """ Dump all nodes in the outline."""
        
        c = self
    
        for p in c.allNodes_iter():
            p.dump()
    #@-node:AGP.20250415230112.520:c.dumpOutline
    #@+node:AGP.20250415230112.521:Pretty Print commands
    #@+node:AGP.20250415230112.522:prettyPrintAllPythonCode
    def prettyPrintAllPythonCode (self,event=None,dump=False):
        
        '''Reformat all Python code in the outline to make it look more beautiful.'''
    
        c = self ; pp = c.prettyPrinter(c)
    
        for p in c.all_positions_iter():
            
            # Unlike scanDirectives, scanForAtLanguage ignores @comment.
            if g.scanForAtLanguage(c,p) == "python":
    
                pp.prettyPrintNode(p,dump=dump)
                
        pp.endUndo()
    
    # For unit test of inverse commands dict.
    def beautifyAllPythonCode (self,event=None,dump=False):
        return self.prettyPrintAllPythonCode (event,dump)
    #@nonl
    #@-node:AGP.20250415230112.522:prettyPrintAllPythonCode
    #@+node:AGP.20250415230112.523:prettyPrintPythonCode
    def prettyPrintPythonCode (self,event=None,p=None,dump=False):
        
        '''Reformat all Python code in the selected tree to make it look more beautiful.'''
    
        c = self
        
        if p: root = p.copy()
        else: root = c.currentPosition();
        
        pp = c.prettyPrinter(c)
        
        for p in root.self_and_subtree_iter():
            
            # Unlike scanDirectives, scanForAtLanguage ignores @comment.
            if g.scanForAtLanguage(c,p) == "python":
        
                pp.prettyPrintNode(p,dump=dump)
              
        pp.endUndo()
    
    # For unit test of inverse commands dict.
    def beautifyPythonCode (self,event=None,dump=False):
        return self.prettyPrintPythonCode (event,dump)
    
    #@-node:AGP.20250415230112.523:prettyPrintPythonCode
    #@+node:AGP.20250415230112.524:prettyPrintPythonNode
    def prettyPrintPythonNode (self,p=None,dump=False):
    
        c = self
        
        if not p:
            p = c.currentPosition()
        
        pp = c.prettyPrinter(c)
    
        # Unlike scanDirectives, scanForAtLanguage ignores @comment.
        if g.scanForAtLanguage(c,p) == "python":
            pp.prettyPrintNode(p,dump=dump)
              
        pp.endUndo()
    #@-node:AGP.20250415230112.524:prettyPrintPythonNode
    #@+node:AGP.20250415230112.525:class prettyPrinter
    class prettyPrinter:
        
        #@    @+others
        #@+node:AGP.20250415230112.526:__init__
        def __init__ (self,c):
            
            self.array = []
                # List of strings comprising the line being accumulated.
                # Important: this list never crosses a line.
            self.bracketLevel = 0
            self.c = c
            self.changed = False
            self.dumping = False
            self.erow = self.ecol = 0 # The ending row/col of the token.
            self.lastName = None # The name of the previous token type.
            self.line = 0 # Same as self.srow
            self.lineParenLevel = 0
            self.lines = [] # List of lines.
            self.name = None
            self.p = c.currentPosition()
            self.parenLevel = 0
            self.prevName = None
            self.s = None # The string containing the line.
            self.squareBracketLevel = 0
            self.srow = self.scol = 0 # The starting row/col of the token.
            self.startline = True # True: the token starts a line.
            self.tracing = False
            #@    << define dispatch dict >>
            #@+node:AGP.20250415230112.527:<< define dispatch dict >>
            self.dispatchDict = {
                
                "comment":    self.doMultiLine,
                "dedent":     self.doDedent,
                "endmarker":  self.doEndMarker,
                "errortoken": self.doErrorToken,
                "indent":     self.doIndent,
                "name":       self.doName,
                "newline":    self.doNewline,
                "nl" :        self.doNewline,
                "number":     self.doNumber,
                "op":         self.doOp,
                "string":     self.doMultiLine,
            }
            #@-node:AGP.20250415230112.527:<< define dispatch dict >>
            #@nl
        #@-node:AGP.20250415230112.526:__init__
        #@+node:AGP.20250415230112.528:clear
        def clear (self):
            self.lines = []
        #@-node:AGP.20250415230112.528:clear
        #@+node:AGP.20250415230112.529:dumpLines
        def dumpLines (self,p,lines):
        
            encoding = g.app.tkEncoding
            
            print ; print '-'*10, p.cleanHeadString()
        
            if 0:
                for line in lines:
                    line2 = g.toEncodedString(line,encoding,reportErrors=True)
                    print line2, # Don't add a trailing newline!
            else:
                for i in xrange(len(lines)):
                    line = lines[i]
                    line = g.toEncodedString(line,encoding,reportErrors=True)
                    print "%3d" % i, repr(lines[i])
        #@-node:AGP.20250415230112.529:dumpLines
        #@+node:AGP.20250415230112.530:dumpToken
        def dumpToken (self,token5tuple):
        
            t1,t2,t3,t4,t5 = token5tuple
            srow,scol = t3 ; erow,ecol = t4
            line = str(t5) # can fail
            name = token.tok_name[t1].lower()
            val = str(t2) # can fail
        
            startLine = self.line != srow
            if startLine:
                print "----- line",srow,repr(line)
            self.line = srow
        
            print "%10s (%2d,%2d) %-8s" % (name,scol,ecol,repr(val))
        #@-node:AGP.20250415230112.530:dumpToken
        #@+node:AGP.20250415230112.531:endUndo
        def endUndo (self):
            
            c = self.c ; u = c.undoer ; undoType = 'Pretty Print'
            current = c.currentPosition()
            
            if self.changed:
                # Tag the end of the command.
                u.afterChangeGroup(current,undoType,dirtyVnodeList=self.dirtyVnodeList)
        #@-node:AGP.20250415230112.531:endUndo
        #@+node:AGP.20250415230112.532:get
        def get (self):
            
            if self.lastName != 'newline' and self.lines:
                # Strip the trailing whitespace from the last line.
                self.lines[-1] = self.lines[-1].rstrip()
            
            return self.lines
        #@-node:AGP.20250415230112.532:get
        #@+node:AGP.20250415230112.533:prettyPrintNode
        def prettyPrintNode(self,p,dump):
        
            c = self.c
            h = p.headString()
            s = p.bodyString()
            if not s: return
            
            readlines = g.readLinesGenerator(s).next
        
            try:
                self.clear()
                for token5tuple in tokenize.generate_tokens(readlines):
                    self.putToken(token5tuple)
                lines = self.get()
        
            except tokenize.TokenError:
                g.es("Error pretty-printing %s.  Not changed." % h, color="blue")
                return
        
            if dump:
                self.dumpLines(p,lines)
            else:
                self.replaceBody(p,lines)
        #@-node:AGP.20250415230112.533:prettyPrintNode
        #@+node:AGP.20250415230112.534:put
        def put (self,s,strip=True):
            
            """Put s to self.array, and strip trailing whitespace if strip is True."""
            
            if self.array and strip:
                prev = self.array[-1]
                if len(self.array) == 1:
                    if prev.rstrip():
                        # Stripping trailing whitespace doesn't strip leading whitespace.
                        self.array[-1] = prev.rstrip()
                else:
                    # The previous entry isn't leading whitespace, so we can strip whitespace.
                    self.array[-1] = prev.rstrip()
        
            self.array.append(s)
        #@-node:AGP.20250415230112.534:put
        #@+node:AGP.20250415230112.535:putArray
        def putArray (self):
            
            """Add the next text by joining all the strings is self.array"""
            
            self.lines.append(''.join(self.array))
            self.array = []
            self.lineParenLevel = 0
        #@-node:AGP.20250415230112.535:putArray
        #@+node:AGP.20250415230112.536:putNormalToken & allies
        def putNormalToken (self,token5tuple):
        
            t1,t2,t3,t4,t5 = token5tuple
            self.name = token.tok_name[t1].lower() # The token type
            self.val = t2  # the token string
            self.srow,self.scol = t3 # row & col where the token begins in the source.
            self.erow,self.ecol = t4 # row & col where the token ends in the source.
            self.s = t5 # The line containing the token.
            self.startLine = self.line != self.srow
            self.line = self.srow
        
            if self.startLine:
                self.doStartLine()
        
            f = self.dispatchDict.get(self.name,self.oops)
            self.trace()
            f()
            self.lastName = self.name
        #@+node:AGP.20250415230112.537:doEndMarker
        def doEndMarker (self):
            
            self.putArray()
        #@-node:AGP.20250415230112.537:doEndMarker
        #@+node:AGP.20250415230112.538:doErrorToken
        def doErrorToken (self):
            
            self.array.append(self.val)
        
            # This code is executed for versions of Python earlier than 2.4
            if self.val == '@':
                # Preserve whitespace after @.
                i = g.skip_ws(self.s,self.scol+1)
                ws = self.s[self.scol+1:i]
                if ws:
                    self.array.append(ws)
        #@-node:AGP.20250415230112.538:doErrorToken
        #@+node:AGP.20250415230112.539:doIndent & doDedent
        def doDedent (self):
            
            pass
            
        def doIndent (self):
            
            self.array.append(self.val)
        #@-node:AGP.20250415230112.539:doIndent & doDedent
        #@+node:AGP.20250415230112.540:doMultiLine (strings, etc).
        def doMultiLine (self):
        
            # Ensure a blank before comments not preceded entirely by whitespace.
            
            if self.val.startswith('#') and self.array:
                prev = self.array[-1]
                if prev and prev[-1] != ' ':
                    self.put(' ') 
        
            # These may span lines, so duplicate the end-of-line logic.
            lines = g.splitLines(self.val)
            for line in lines:
                self.array.append(line)
                if line and line[-1] == '\n':
                    self.putArray()
            
            # Add a blank after the string if there is something in the last line.
            if self.array:
                line = self.array[-1]
                if line.strip():
                    self.put(' ')
                    
            # Suppress start-of-line logic.
            self.line = self.erow
        #@-node:AGP.20250415230112.540:doMultiLine (strings, etc).
        #@+node:AGP.20250415230112.541:doName
        def doName(self):
            
            # Ensure whitespace or start-of-line precedes the name.
            if self.array:
                last = self.array[-1]
                ch = last[-1]
                outer = self.parenLevel == 0 and self.squareBracketLevel == 0
                chars = '@ \t{([.'
                if not outer: chars += ',=<>*-+&|/'
                if ch not in chars:
                    self.array.append(' ')
        
            self.array.append("%s " % self.val)
        
            if self.prevName == "def": # A personal idiosyncracy.
                self.array.append(' ') # Retain the blank before '('.
        
            self.prevName = self.val
        #@-node:AGP.20250415230112.541:doName
        #@+node:AGP.20250415230112.542:doNewline
        def doNewline (self):
        
            # Remove trailing whitespace.
            # This never removes trailing whitespace from multi-line tokens.
            if self.array:
                self.array[-1] = self.array[-1].rstrip()
        
            self.array.append('\n')
            self.putArray()
        #@-node:AGP.20250415230112.542:doNewline
        #@+node:AGP.20250415230112.543:doNumber
        def doNumber (self):
        
            self.array.append(self.val)
        #@-node:AGP.20250415230112.543:doNumber
        #@+node:AGP.20250415230112.544:doOp
        def doOp (self):
            
            val = self.val
            outer = self.lineParenLevel <= 0 or (self.parenLevel == 0 and self.squareBracketLevel == 0)
            # New in Python 2.4: '@' is an operator, not an error token.
            if self.val == '@':
                self.array.append(self.val)
                # Preserve whitespace after @.
                i = g.skip_ws(self.s,self.scol+1)
                ws = self.s[self.scol+1:i]
                if ws: self.array.append(ws)
            elif val == '(':
                # Nothing added; strip leading blank before function calls but not before Python keywords.
                strip = self.lastName=='name' and not keyword.iskeyword(self.prevName)
                self.put('(',strip=strip)
                self.parenLevel += 1 ; self.lineParenLevel += 1
            elif val in ('=','==','+=','-=','!=','<=','>=','<','>','<>','*','**','+','&','|','/','//'):
                # Add leading and trailing blank in outer mode.
                s = g.choose(outer,' %s ','%s')
                self.put(s % val)
            elif val in ('^','~','{','['):
                # Add leading blank in outer mode.
                s = g.choose(outer,' %s','%s')
                self.put(s % val)
                if val == '[': self.squareBracketLevel += 1
            elif val in (',',':','}',']',')'):
                # Add trailing blank in outer mode.
                s = g.choose(outer,'%s ','%s')
                self.put(s % val)
                if val == ']': self.squareBracketLevel -= 1
                if val == ')':
                    self.parenLevel -= 1 ; self.lineParenLevel -= 1
            # ----- no difference between outer and inner modes ---
            elif val in (';','%'):
                # Add leading and trailing blank.
                self.put(' %s ' % val)
            elif val == '>>':
                # Add leading blank.
                self.put(' %s' % val)
            elif val == '<<':
                # Add trailing blank.
                self.put('%s ' % val)
            elif val in ('-'):
                # Could be binary or unary.  Or could be a hyphen in a section name.
                # Add preceding blank only for non-id's.
                if outer:
                    if self.array:
                        prev = self.array[-1].rstrip()
                        if prev and not g.isWordChar(prev[-1]):
                            self.put(' %s' % val)
                        else: self.put(val)
                    else: self.put(val) # Try to leave whitespace unchanged.
                else:
                    self.put(val)
            else:
                self.put(val)
        #@-node:AGP.20250415230112.544:doOp
        #@+node:AGP.20250415230112.545:doStartLine
        def doStartLine (self):
            
            before = self.s[0:self.scol]
            i = g.skip_ws(before,0)
            self.ws = self.s[0:i]
             
            if self.ws:
                self.array.append(self.ws)
        #@-node:AGP.20250415230112.545:doStartLine
        #@+node:AGP.20250415230112.546:oops
        def oops(self):
            
            print "unknown PrettyPrinting code: %s" % (self.name)
        #@-node:AGP.20250415230112.546:oops
        #@+node:AGP.20250415230112.547:trace
        def trace(self):
            
            if self.tracing:
        
                g.trace("%10s: %s" % (
                    self.name,
                    repr(g.toEncodedString(self.val,"utf-8"))
                ))
        #@-node:AGP.20250415230112.547:trace
        #@-node:AGP.20250415230112.536:putNormalToken & allies
        #@+node:AGP.20250415230112.548:putToken
        def putToken (self,token5tuple):
            
            if self.dumping:
                self.dumpToken(token5tuple)
            else:
                self.putNormalToken(token5tuple)
        #@-node:AGP.20250415230112.548:putToken
        #@+node:AGP.20250415230112.549:replaceBody
        def replaceBody (self,p,lines):
            
            c = self.c ; u = c.undoer ; undoType = 'Pretty Print'
            
            sel = c.frame.body.getInsertionPoint()
            oldBody = p.bodyString()
            body = string.join(lines,'')
            
            if oldBody != body:
                if not self.changed:
                    # Start the group.
                    u.beforeChangeGroup(p,undoType)
                    self.changed = True
                    self.dirtyVnodeList = []
                undoData = u.beforeChangeNodeContents(p)
                c.setBodyString(p,body)
                dirtyVnodeList2 = p.setDirty()
                self.dirtyVnodeList.extend(dirtyVnodeList2)
                u.afterChangeNodeContents(p,undoType,undoData,dirtyVnodeList=self.dirtyVnodeList)
        #@-node:AGP.20250415230112.549:replaceBody
        #@-others
    #@-node:AGP.20250415230112.525:class prettyPrinter
    #@-node:AGP.20250415230112.521:Pretty Print commands
    #@-node:AGP.20250415230112.499:Check Outline submenu...
    #@+node:AGP.20250415230112.550:Expand & Contract...
    #@+node:AGP.20250415230112.551:Commands
    #@+node:AGP.20250415230112.552:contractAllHeadlines
    def contractAllHeadlines (self,event=None):
        
        '''Contract all nodes in the outline.'''
    
        c = self
        
        c.beginUpdate()
        try: # update...
            for p in c.allNodes_iter():
                p.contract()
            # Select the topmost ancestor of the presently selected node.
            p = c.currentPosition()
            while p and p.hasParent():
                p.moveToParent()
            c.selectVnode(p)
        finally:
            c.endUpdate()
            c.treeWantsFocusNow()
    
        c.expansionLevel = 1 # Reset expansion level.
    #@-node:AGP.20250415230112.552:contractAllHeadlines
    #@+node:AGP.20250415230112.553:contractNode
    def contractNode (self,event=None):
        
        '''Contract the presently selected node.'''
        
        c = self ; v = c.currentVnode()
        
        c.beginUpdate()
        try:
            v.contract()
        finally:
            c.endUpdate()
            c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.553:contractNode
    #@+node:AGP.20250415230112.554:contractNodeOrGoToParent
    def contractNodeOrGoToParent (self,event=None):
        
        """Simulate the left Arrow Key in folder of Windows Explorer."""
    
        c = self ; p = c.currentPosition()
     
        if p.hasChildren() and p.isExpanded():
            c.contractNode()
        elif p.hasParent():
            c.goToParent()
    #@-node:AGP.20250415230112.554:contractNodeOrGoToParent
    #@+node:AGP.20250415230112.555:contractParent
    def contractParent (self,event=None):
        
        '''Contract the parent of the presently selected node.'''
        
        c = self ; v = c.currentVnode()
        parent = v.parent()
        if not parent: return
        
        c.beginUpdate()
        try:
            c.selectVnode(parent)
            parent.contract()
        finally:
            c.endUpdate()
            c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.555:contractParent
    #@+node:AGP.20250415230112.556:expandAllHeadlines
    def expandAllHeadlines (self,event=None):
        
        '''Expand all headlines.
        Warning: this can take a long time for large outlines.'''
    
        c = self ; v = root = c.rootVnode()
        c.beginUpdate()
        try:
            while v:
                c.expandSubtree(v)
                v = v.next()
            c.selectVnode(root)
        finally:
            c.endUpdate()
            c.treeWantsFocusNow()
        c.expansionLevel = 0 # Reset expansion level.
    #@-node:AGP.20250415230112.556:expandAllHeadlines
    #@+node:AGP.20250415230112.557:expandAllSubheads
    def expandAllSubheads (self,event=None):
        
        '''Expand all children of the presently selected node.'''
    
        c = self ; v = c.currentVnode()
        if not v: return
    
        child = v.firstChild()
        c.beginUpdate()
        try:
            c.expandSubtree(v)
            while child:
                c.expandSubtree(child)
                child = child.next()
            c.selectVnode(v)
        finally:
            c.endUpdate()
            c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.557:expandAllSubheads
    #@+node:AGP.20250415230112.558:expandLevel1..9
    def expandLevel1 (self,event=None):
        '''Expand the outline to level 1'''
        self.expandToLevel(1)
    
    def expandLevel2 (self,event=None):
        '''Expand the outline to level 2'''
        self.expandToLevel(2)
    
    def expandLevel3 (self,event=None):
        '''Expand the outline to level 3'''
        self.expandToLevel(3)
    
    def expandLevel4 (self,event=None):
        '''Expand the outline to level 4'''
        self.expandToLevel(4)
    
    def expandLevel5 (self,event=None):
        '''Expand the outline to level 5'''
        self.expandToLevel(5)
    
    def expandLevel6 (self,event=None):
        '''Expand the outline to level 6'''
        self.expandToLevel(6)
    
    def expandLevel7 (self,event=None):
        '''Expand the outline to level 7'''
        self.expandToLevel(7)
    
    def expandLevel8 (self,event=None):
        '''Expand the outline to level 8'''
        self.expandToLevel(8)
    
    def expandLevel9 (self,event=None):
        '''Expand the outline to level 9'''
        self.expandToLevel(9)
    #@-node:AGP.20250415230112.558:expandLevel1..9
    #@+node:AGP.20250415230112.559:expandNextLevel
    def expandNextLevel (self,event=None):
        
        '''Increase the expansion level of the outline and
        Expand all nodes at that level or lower.'''
    
        c = self ; v = c.currentVnode()
        
        # 1/31/02: Expansion levels are now local to a particular tree.
        if c.expansionNode != v:
            c.expansionLevel = 1
            c.expansionNode = v
            
        self.expandToLevel(c.expansionLevel + 1)
    #@-node:AGP.20250415230112.559:expandNextLevel
    #@+node:AGP.20250415230112.560:expandNode
    def expandNode (self,event=None):
        
        '''Expand the presently selected node.'''
        
        c = self ; v = c.currentVnode()
        
        c.beginUpdate()
        try:
            v.expand()
        finally:
            c.endUpdate()
            c.treeWantsFocusNow()
    #@nonl
    #@-node:AGP.20250415230112.560:expandNode
    #@+node:AGP.20250415230112.561:expandNodeAnd/OrGoToFirstChild
    def expandNodeAndGoToFirstChild (self,event=None):
        
        """If a node has children, expand it if needed and go to the first child."""
    
        c = self ; p = c.currentPosition()
        if not p.hasChildren():
            c.treeWantsFocusNow()
            return
    
        if not p.isExpanded():
            c.expandNode()
            
        c.beginUpdate()
        try:
            c.selectVnode(p.firstChild())
        finally:
            c.endUpdate()
            c.treeWantsFocusNow()
            
    def expandNodeOrGoToFirstChild (self,event=None):
        
        """Simulate the Right Arrow Key in folder of Windows Explorer."""
    
        c = self ; p = c.currentPosition()
        if not p.hasChildren():
            c.treeWantsFocusNow()
            return
    
        if not p.isExpanded():
            c.expandNode()
        else:
            c.beginUpdate()
            try:
                c.selectVnode(p.firstChild())
            finally:
                c.endUpdate()
        c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.561:expandNodeAnd/OrGoToFirstChild
    #@+node:AGP.20250415230112.562:expandOnlyAncestorsOfNode
    def expandOnlyAncestorsOfNode (self,event=None):
        
        '''Contract all nodes in the outline.'''
    
        c = self ; level = 1
        
        c.beginUpdate()
        try:
            for p in c.allNodes_iter():
                p.contract()
            for p in c.currentPosition().parents_iter():
                p.expand()
                level += 1
        finally:
            c.endUpdate()
            c.treeWantsFocusNow()
    
        c.expansionLevel = level # Reset expansion level.
    #@-node:AGP.20250415230112.562:expandOnlyAncestorsOfNode
    #@+node:AGP.20250415230112.563:expandPrevLevel
    def expandPrevLevel (self,event=None):
        
        '''Decrease the expansion level of the outline and
        Expand all nodes at that level or lower.'''
    
        c = self ; v = c.currentVnode()
        
        # 1/31/02: Expansion levels are now local to a particular tree.
        if c.expansionNode != v:
            c.expansionLevel = 1
            c.expansionNode = v
            
        self.expandToLevel(max(1,c.expansionLevel - 1))
    #@-node:AGP.20250415230112.563:expandPrevLevel
    #@-node:AGP.20250415230112.551:Commands
    #@+node:AGP.20250415230112.564:Utilities
    #@+node:AGP.20250415230112.565:contractSubtree
    def contractSubtree (self,p):
    
        for p in p.subtree_iter():
            p.contract()
    #@-node:AGP.20250415230112.565:contractSubtree
    #@+node:AGP.20250415230112.566:expandSubtree
    def expandSubtree (self,v):
    
        c = self
        last = v.lastNode()
    
        c.beginUpdate()
        try:
            while v and v != last:
                v.expand()
                v = v.threadNext()
        finally:
            c.endUpdate()
    #@-node:AGP.20250415230112.566:expandSubtree
    #@+node:AGP.20250415230112.567:expandToLevel (rewritten in 4.4)
    def expandToLevel (self,level):
    
        c = self
        c.beginUpdate()
        try:
            current = c.currentPosition()
            n = current.level()
            for p in current.self_and_subtree_iter():
                if p.level() - n + 1 < level:
                    p.expand()
                else:
                    p.contract()
            c.expansionLevel = level
            c.expansionNode = c.currentPosition()
        finally:
            c.endUpdate()
    #@-node:AGP.20250415230112.567:expandToLevel (rewritten in 4.4)
    #@-node:AGP.20250415230112.564:Utilities
    #@-node:AGP.20250415230112.550:Expand & Contract...
    #@+node:AGP.20250415230112.568:Goto
    #@+node:AGP.20250415230112.569:goNextVisitedNode
    def goNextVisitedNode (self,event=None):
        
        '''Select the next visited node.'''
        
        c = self
    
        while c.beadPointer + 1 < len(c.beadList):
            c.beadPointer += 1
            v = c.beadList[c.beadPointer]
            if c.positionExists(v):
                c.beginUpdate()
                try:
                    c.frame.tree.expandAllAncestors(v)
                    c.selectVnode(v,updateBeadList=False)
                finally:
                    c.endUpdate()
                c.treeWantsFocusNow()
                return
    #@-node:AGP.20250415230112.569:goNextVisitedNode
    #@+node:AGP.20250415230112.570:goPrevVisitedNode
    def goPrevVisitedNode (self,event=None):
        
        '''Select the previously visited node.'''
        
        c = self
    
        while c.beadPointer > 0:
            c.beadPointer -= 1
            v = c.beadList[c.beadPointer]
            if c.positionExists(v):
                c.beginUpdate()
                try:
                    c.frame.tree.expandAllAncestors(v)
                    c.selectVnode(v,updateBeadList=False)
                finally:
                    c.endUpdate()
                c.treeWantsFocusNow()
                return
    #@-node:AGP.20250415230112.570:goPrevVisitedNode
    #@+node:AGP.20250415230112.571:goToFirstNode
    def goToFirstNode (self,event=None):
        
        '''Select the first node of the entire outline.'''
        
        c = self
        p = c.rootPosition()
        if p:
            c.beginUpdate()
            try:
                c.selectVnode(p)
            finally:
                c.endUpdate()
        c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.571:goToFirstNode
    #@+node:AGP.20250415230112.572:goToFirstSibling (New in 4.4)
    def goToFirstSibling (self,event=None):
        
        '''Select the first sibling of the selected node.'''
        
        c = self ; p = c.currentPosition()
        
        if p.hasBack():
            while p.hasBack():
                p.moveToBack()
    
            c.beginUpdate()
            try:
                c.selectVnode(p)
            finally:
                c.endUpdate()
        c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.572:goToFirstSibling (New in 4.4)
    #@+node:AGP.20250415230112.573:goToLastNode (Bug fix in 4.4)
    def goToLastNode (self,event=None):
        
        '''Select the last node in the selected tree.'''
        
        c = self ; p = c.rootPosition()
        while p and p.hasThreadNext(): # Bug fix: 10/12/05: was p.hasNext.
            p.moveToThreadNext()
    
        if p:
            c.beginUpdate()
            try:
                c.frame.tree.expandAllAncestors(p)
                c.selectVnode(p)
            finally:
                c.endUpdate()
        c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.573:goToLastNode (Bug fix in 4.4)
    #@+node:AGP.20250415230112.574:goToLastSibling (New in 4.4)
    def goToLastSibling (self,event=None):
        
        '''Select the last sibling of the selected node.'''
        
        c = self ; p = c.currentPosition()
        
        if p.hasNext():
            while p.hasNext():
                p.moveToNext()
    
            c.beginUpdate()
            try:
                c.selectVnode(p)
            finally:
                c.endUpdate()
        c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.574:goToLastSibling (New in 4.4)
    #@+node:AGP.20250415230112.575:goToLastVisibleNode
    def goToLastVisibleNode (self,event=None):
        
        '''Select the last visible node of the entire outline.'''
        
        c = self ; p = c.rootPosition()
        
        while p.hasNext():
            p.moveToNext()
            
        while p and p.isExpanded():
            p.moveToLastChild()
    
        if p:
            c.beginUpdate()
            try:
                c.frame.tree.expandAllAncestors(p)
                c.selectVnode(p)
            finally:
                c.endUpdate()
        c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.575:goToLastVisibleNode
    #@+node:AGP.20250415230112.576:goToNextClone
    def goToNextClone (self,event=None):
        
        '''Select the next node that is a clone of the selected node.'''
    
        c = self ; current = c.currentVnode()
        if not current: return
        if not current.isCloned(): return
    
        v = current.threadNext()
        while v and v.t != current.t:
            v = v.threadNext()
            
        if not v:
            # Wrap around.
            v = c.rootVnode()
            while v and v != current and v.t != current.t:
                v = v.threadNext()
    
        if v:
            c.beginUpdate()
            try:
                c.endEditing()
                c.selectVnode(v)
            finally:
                c.endUpdate()
        c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.576:goToNextClone
    #@+node:AGP.20250415230112.577:goToNextDirtyHeadline
    def goToNextDirtyHeadline (self,event=None):
        
        '''Select the node that is marked as changed.'''
    
        c = self ; p = c.currentPosition()
        if not p: return
    
        p.moveToThreadNext()
        while p and not p.isDirty():
            p.moveToThreadNext()
    
        if not p:
            # Wrap around.
            p = c.rootPosition()
            while p and not p.isDirty():
                p.moveToThreadNext()
    
        if p:
            c.beginUpdate()
            try:
                c.endEditing()
                c.selectPosition(p)
            finally:
                c.endUpdate()
        else:
            g.es("done",color="blue")
        c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.577:goToNextDirtyHeadline
    #@+node:AGP.20250415230112.578:goToNextMarkedHeadline
    def goToNextMarkedHeadline (self,event=None):
        
        '''Select the next marked node.'''
    
        c = self ; p = c.currentPosition()
        if not p: return
    
        p.moveToThreadNext()
        while p and not p.isMarked():
            p.moveToThreadNext()
    
        if p:
            c.beginUpdate()
            try:
                c.endEditing()
                c.selectPosition(p)
            finally:
                c.endUpdate()
        else:
            g.es("done",color="blue")
        c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.578:goToNextMarkedHeadline
    #@+node:AGP.20250415230112.579:goToNextSibling
    def goToNextSibling (self,event=None):
        
        '''Select the next sibling of the selected node.'''
        
        c = self
        v = c.currentVnode()
        if not v: return
        next = v.next()
        if next:
            c.beginUpdate()
            try:
                c.selectVnode(next)
            finally:
                c.endUpdate()
        c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.579:goToNextSibling
    #@+node:AGP.20250415230112.580:goToParent
    def goToParent (self,event=None):
        
        '''Select the parent of the selected node.'''
        
        c = self
        v = c.currentVnode()
        if not v: return
        p = v.parent()
        if p:
            c.beginUpdate()
            try:
                c.selectVnode(p)
            finally:
                c.endUpdate()
        c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.580:goToParent
    #@+node:AGP.20250415230112.581:goToPrevSibling
    def goToPrevSibling (self,event=None):
        
        '''Select the previous sibling of the selected node.'''
        
        c = self
        v = c.currentVnode()
        if not v: return
        back = v.back()
        if back:
            c.beginUpdate()
            try:
                c.selectVnode(back)
            finally:
                c.endUpdate()
        c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.581:goToPrevSibling
    #@+node:AGP.20250415230112.582:selectThreadNext
    def selectThreadNext (self,event=None):
        
        '''Select the node following the selected node in outline order.'''
    
        c = self ; current = c.currentPosition()
        if not current: return
    
        p = current.threadNext()
        if p:
            c.beginUpdate()
            try:
                c.selectPosition(p)
            finally:
                c.endUpdate()
        c.treeWantsFocusNow()
    #@nonl
    #@-node:AGP.20250415230112.582:selectThreadNext
    #@+node:AGP.20250415230112.583:selectThreadBack
    def selectThreadBack (self,event=None):
        
        '''Select the node preceding the selected node in outline order.'''
    
        c = self ; current = c.currentVnode()
        if not current: return
        
        v = current.threadBack()
        if v:
            c.beginUpdate()
            try:
                c.selectVnode(v)
            finally:
                c.endUpdate()
        c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.583:selectThreadBack
    #@+node:AGP.20250415230112.584:selectVisBack
    # This has an up arrow for a control key.
    
    def selectVisBack (self,event=None):
        
        '''Select the visible node preceding the presently selected node.'''
    
        c = self ; current = c.currentPosition()
        if not current: return
    
        p = current.visBack()
        if p:
            redraw = not p.isVisible()
            if not redraw: c.frame.tree.setSelectedLabelState(current)
            c.beginUpdate()
            try:
                c.selectVnode(p)
            finally:
                c.endUpdate(redraw)
        c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.584:selectVisBack
    #@+node:AGP.20250415230112.585:selectVisNext
    def selectVisNext (self,event=None):
        
        '''Select the visible node following the presently selected node.'''
    
        c = self ; current = c.currentPosition()
        if not current: return
        
        p = current.visNext()
        if p:
            redraw = not p.isVisible()
            if not redraw: c.frame.tree.setSelectedLabelState(current)
            c.beginUpdate()
            try:
                c.selectVnode(p)
            finally:
                c.endUpdate(redraw)
    
        c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.585:selectVisNext
    #@-node:AGP.20250415230112.568:Goto
    #@+node:AGP.20250415230112.586:Mark...
    #@+node:AGP.20250415230112.587:markChangedHeadlines
    def markChangedHeadlines (self,event=None):
        
        '''Mark all nodes that have been changed.'''
    
        c = self ; u = c.undoer ; undoType = 'Mark Changed'
        current = c.currentPosition()
        
        c.beginUpdate()
        try:
            u.beforeChangeGroup(current,undoType)
            for p in c.allNodes_iter():
                if p.isDirty()and not p.isMarked():
                    bunch = u.beforeMark(p,undoType)
                    c.setMarked(p)
                    c.setChanged(True)
                    u.afterMark(p,undoType,bunch)
            u.afterChangeGroup(current,undoType)
            g.es("done",color="blue")
        finally:
            c.endUpdate()
    #@-node:AGP.20250415230112.587:markChangedHeadlines
    #@+node:AGP.20250415230112.588:markChangedRoots
    def markChangedRoots (self,event=None):
        
        '''Mark all changed @root nodes.'''
    
        c = self ; u = c.undoer ; undoType = 'Mark Changed'
        current = c.currentPosition()
    
        c.beginUpdate()
        try:
            u.beforeChangeGroup(current,undoType)
            for p in c.allNodes_iter():
                if p.isDirty()and not p.isMarked():
                    s = p.bodyString()
                    flag, i = g.is_special(s,0,"@root")
                    if flag:
                        bunch = u.beforeMark(p,undoType)
                        c.setMarked(p)
                        c.setChanged(True)
                        u.afterMark(p,undoType,bunch)
            u.afterChangeGroup(current,undoType)
            g.es("done",color="blue")
        finally:
            c.endUpdate()
    #@-node:AGP.20250415230112.588:markChangedRoots
    #@+node:AGP.20250415230112.589:markAllAtFileNodesDirty (not used)
    def markAllAtFileNodesDirty (self,event=None):
        
        '''Mark all @file nodes as changed.'''
    
        c = self ; p = c.rootPosition()
    
        c.beginUpdate()
        try: # In update...
            while p:
                if p.isAtFileNode() and not p.isDirty():
                    p.setDirty()
                    c.setChanged(True)
                    p.moveToNodeAfterTree()
                else:
                    p.moveToThreadNext()
        finally:
            c.endUpdate()
    #@-node:AGP.20250415230112.589:markAllAtFileNodesDirty (not used)
    #@+node:AGP.20250415230112.590:markAtFileNodesDirty (not used)
    def markAtFileNodesDirty (self,event=None):
        
        '''Mark all @file nodes in the selected tree as changed.'''
    
        c = self
        p = c.currentPosition()
        if not p: return
    
        after = p.nodeAfterTree()
        c.beginUpdate()
        try: # In update...
            while p and p != after:
                if p.isAtFileNode() and not p.isDirty():
                    p.setDirty()
                    c.setChanged(True)
                    p.moveToNodeAfterTree()
                else:
                    p.moveToThreadNext()
        finally:
            c.endUpdate()
    #@-node:AGP.20250415230112.590:markAtFileNodesDirty (not used)
    #@+node:AGP.20250415230112.591:markClones
    def markClones (self,event=None):
        
        '''Mark all clones of the selected node.'''
    
        c = self ; u = c.undoer ; undoType = 'Mark Clones'
        current = c.currentPosition()
        if not current or not current.isCloned():
            g.es('The current node is not a clone',color='blue')
            return
    
        c.beginUpdate()
        u.beforeChangeGroup(current,undoType)
        try: # In update...
            dirtyVnodeList = []
            for p in c.allNodes_iter():
                if p.v.t == current.v.t:
                    bunch = u.beforeMark(p,undoType)
                    c.setMarked(p)
                    c.setChanged(True)
                    dirtyVnodeList2 = p.setDirty()
                    dirtyVnodeList.extend(dirtyVnodeList2)
                    u.afterMark(p,undoType,bunch)
        finally:
            u.afterChangeGroup(current,undoType,dirtyVnodeList=dirtyVnodeList)
            c.endUpdate()
    #@-node:AGP.20250415230112.591:markClones
    #@+node:AGP.20250415230112.592:markHeadline
    def markHeadline (self,event=None):
        
        '''Toggle the mark of the selected node.'''
    
        c = self ; u = c.undoer ; p = c.currentPosition()
        if not p: return
    
        c.beginUpdate()
        try: # In update...
            undoType = g.choose(p.isMarked(),'Unmark','Mark')
            bunch = u.beforeMark(p,undoType)
            if p.isMarked():
                c.clearMarked(p)
            else:
                c.setMarked(p)
            dirtyVnodeList = p.setDirty()
            c.setChanged(True)
            u.afterMark(p,undoType,bunch,dirtyVnodeList=dirtyVnodeList)
        finally:
            c.endUpdate()
    #@-node:AGP.20250415230112.592:markHeadline
    #@+node:AGP.20250415230112.593:markSubheads
    def markSubheads (self,event=None):
        
        '''Mark all children of the selected node as changed.'''
    
        c = self ; u = c.undoer ; undoType = 'Mark Subheads'
        current = c.currentPosition()
        if not current: return
    
        c.beginUpdate()
        u.beforeChangeGroup(current,undoType)
        try: # In update...
            dirtyVnodeList = []
            for p in current.children_iter():
                if not p.isMarked():
                    bunch = u.beforeMark(p,undoType)
                    c.setMarked(p)
                    dirtyVnodeList2 = p.setDirty()
                    dirtyVnodeList.extend(dirtyVnodeList2)
                    c.setChanged(True)
                    u.afterMark(p,undoType,bunch)
        finally:
            u.afterChangeGroup(current,undoType,dirtyVnodeList=dirtyVnodeList)
            c.endUpdate()
    #@-node:AGP.20250415230112.593:markSubheads
    #@+node:AGP.20250415230112.594:unmarkAll
    def unmarkAll (self,event=None):
        
        '''Unmark all nodes in the entire outline.'''
    
        c = self ; u = c.undoer ; undoType = 'Unmark All'
        current = c.currentPosition()
        if not current: return
        
        c.beginUpdate()
        u.beforeChangeGroup(current,undoType)
        try: # In update...
            changed = False
            for p in c.allNodes_iter():
                if p.isMarked():
                    bunch = u.beforeMark(p,undoType)
                    c.clearMarked(p)
                    p.v.t.setDirty()
                    u.afterMark(p,undoType,bunch)
            dirtyVnodeList = [p.v for p in c.allNodes_iter() if p.v.isDirty()]
            if changed: c.setChanged(True)
        finally:
            u.afterChangeGroup(current,undoType,dirtyVnodeList=dirtyVnodeList)
            c.endUpdate()
    #@nonl
    #@-node:AGP.20250415230112.594:unmarkAll
    #@-node:AGP.20250415230112.586:Mark...
    #@+node:AGP.20250415230112.595:Move... (Commands)
    #@+node:AGP.20250415230112.596:demote
    def demote (self,event=None):
        
        '''Make all following siblings children of the selected node.'''
    
        c = self ; u = c.undoer
        current = c.currentPosition()
        command = 'Demote'
        if not current or not current.hasNext():
            c.treeWantsFocusNow()
            return
    
        # Make sure all the moves will be valid.
        for child in current.children_iter():
            if not c.checkMoveWithParentWithWarning(child,current,True):
                c.treeWantsFocusNow()
                return
        c.beginUpdate()
        try: # update...
            c.endEditing()
            u.beforeChangeGroup(current,command)
            p = current.copy()
            while p.hasNext(): # Do not use iterator here.
                child = p.next()
                undoData = u.beforeMoveNode(child)
                child.moveToNthChildOf(p,p.numberOfChildren())
                u.afterMoveNode(child,command,undoData)
            p.expand()
            # Even if p is an @ignore node there is no need to mark the demoted children dirty.
            dirtyVnodeList = current.setAllAncestorAtFileNodesDirty()
            c.setChanged(True)
            u.afterChangeGroup(current,command,dirtyVnodeList=dirtyVnodeList)
        finally:
            c.selectPosition(current)  # Also sets rootPosition.
            c.endUpdate()
            c.treeWantsFocusNow()
        c.updateSyntaxColorer(current) # Moving can change syntax coloring.
    #@-node:AGP.20250415230112.596:demote
    #@+node:AGP.20250415230112.597:moveOutlineDown
    #@+at 
    #@nonl
    # Moving down is more tricky than moving up; we can't move p to be a child 
    # of itself.  An important optimization:  we don't have to call 
    # checkMoveWithParentWithWarning() if the parent of the moved node remains 
    # the same.
    #@-at
    #@@c
    
    def moveOutlineDown (self,event=None):
        
        '''Move the selected node down.'''
    
        c = self ; u = c.undoer ; p = c.currentPosition()
        if not p: return
    
        if not c.canMoveOutlineDown():
            if c.hoistStack: g.es("Can't move node out of hoisted outline",color="blue")
            c.treeWantsFocusNow()
            return
            
        inAtIgnoreRange = p.inAtIgnoreRange()
        # Set next to the node after which p will be moved.
        next = p.visNext()
        while next and p.isAncestorOf(next):
            next = next.visNext()
        if not next:
            c.treeWantsFocusNow()
            return
    
        sparseMove = c.config.getBool('sparse_move_outline_left')
        c.beginUpdate()
        try: # update...
            c.endEditing()
            undoData = u.beforeMoveNode(p)
            #@        << Move p down & set moved if successful >>
            #@+node:AGP.20250415230112.598:<< Move p down & set moved if successful >>
            parent = p.parent()
            
            if next.hasChildren() and next.isExpanded():
                # Attempt to move p to the first child of next.
                moved = c.checkMoveWithParentWithWarning(p,next,True)
                if moved:
                    dirtyVnodeList = p.setAllAncestorAtFileNodesDirty()
                    p.moveToNthChildOf(next,0)
                    
            else:
                # Attempt to move p after next.
                moved = c.checkMoveWithParentWithWarning(p,next.parent(),True)
                if moved:
                    dirtyVnodeList = p.setAllAncestorAtFileNodesDirty()
                    p.moveAfter(next)
                    
            if moved and sparseMove and parent and not parent.isAncestorOf(p):
                # New in Leo 4.4.2: contract the old parent if it is no longer the parent of p.
                parent.contract()
            #@-node:AGP.20250415230112.598:<< Move p down & set moved if successful >>
            #@nl
            if moved:
                if inAtIgnoreRange and not p.inAtIgnoreRange():
                    # The moved nodes have just become newly unignored.
                    p.setDirty() # Mark descendent @thin nodes dirty.
                else: # No need to mark descendents dirty.
                    dirtyVnodeList2 = p.setAllAncestorAtFileNodesDirty()
                    dirtyVnodeList.extend(dirtyVnodeList2)
                c.setChanged(True)
                u.afterMoveNode(p,'Move Down',undoData,dirtyVnodeList)
        finally:
            c.selectPosition(p) # Also sets rootPosition.
            c.endUpdate()
            c.treeWantsFocusNow()
        c.updateSyntaxColorer(p) # Moving can change syntax coloring.
    #@-node:AGP.20250415230112.597:moveOutlineDown
    #@+node:AGP.20250415230112.599:moveOutlineLeft
    def moveOutlineLeft (self,event=None):
        
        '''Move the selected node left if possible.'''
        
        c = self ; u = c.undoer ; p = c.currentPosition()
        if not p: return
        if not c.canMoveOutlineLeft(): # 11/4/03: Support for hoist.
            if c.hoistStack: g.es("Can't move node out of hoisted outline",color="blue")
            c.treeWantsFocusNow()
            return
        if not p.hasParent():
            c.treeWantsFocusNow()
            return
    
        inAtIgnoreRange = p.inAtIgnoreRange()
        parent = p.parent()
        sparseMove = c.config.getBool('sparse_move_outline_left')
        c.beginUpdate()
        try: # In update...
            c.endEditing()
            undoData = u.beforeMoveNode(p)
            dirtyVnodeList = p.setAllAncestorAtFileNodesDirty()
            p.moveAfter(parent)
            if inAtIgnoreRange and not p.inAtIgnoreRange():
                # The moved nodes have just become newly unignored.
                p.setDirty() # Mark descendent @thin nodes dirty.
            else: # No need to mark descendents dirty.
                dirtyVnodeList2 = p.setAllAncestorAtFileNodesDirty()
                dirtyVnodeList.extend(dirtyVnodeList2)
            c.setChanged(True)
            u.afterMoveNode(p,'Move Left',undoData,dirtyVnodeList)
            if sparseMove: # New in Leo 4.4.2
                parent.contract()
        finally:
            c.selectPosition(p) # Also sets rootPosition.
            c.endUpdate()
            c.treeWantsFocusNow()
        c.updateSyntaxColorer(p) # Moving can change syntax coloring.
    #@nonl
    #@-node:AGP.20250415230112.599:moveOutlineLeft
    #@+node:AGP.20250415230112.600:moveOutlineRight
    def moveOutlineRight (self,event=None):
        
        '''Move the selected node right if possible.'''
        
        c = self ; u = c.undoer ; p = c.currentPosition()
        if not p: return
        if not c.canMoveOutlineRight(): # 11/4/03: Support for hoist.
            if c.hoistStack: g.es("Can't move node out of hoisted outline",color="blue")
            c.treeWantsFocusNow()
            return
        if not p.hasBack:
            c.treeWantsFocusNow()
            return
        back = p.back()
        if not c.checkMoveWithParentWithWarning(p,back,True):
            c.treeWantsFocusNow()
            return
    
        c.beginUpdate()
        try: # update...
            c.endEditing()
            undoData = u.beforeMoveNode(p)
            dirtyVnodeList = p.setAllAncestorAtFileNodesDirty()
            n = back.numberOfChildren()
            p.moveToNthChildOf(back,n)
            # g.trace(p,p.parent())
            # Moving an outline right can never bring it outside the range of @ignore.
            dirtyVnodeList2 = p.setAllAncestorAtFileNodesDirty()
            dirtyVnodeList.extend(dirtyVnodeList2)
            c.setChanged(True)
            u.afterMoveNode(p,'Move Right',undoData,dirtyVnodeList)
        finally:
            c.selectPosition(p) # Also sets root position.
            c.endUpdate()
            c.treeWantsFocusNow()
        c.updateSyntaxColorer(p) # Moving can change syntax coloring.
    #@-node:AGP.20250415230112.600:moveOutlineRight
    #@+node:AGP.20250415230112.601:moveOutlineUp
    def moveOutlineUp (self,event=None):
        
        '''Move the selected node up if possible.'''
    
        c = self ; u = c.undoer ; p = c.currentPosition()
        if not p: return
        if not c.canMoveOutlineUp(): # Support for hoist.
            if c.hoistStack: g.es("Can't move node out of hoisted outline",color="blue")
            c.treeWantsFocusNow()
            return
        back = p.visBack()
        if not back: return
        inAtIgnoreRange = p.inAtIgnoreRange()
        back2 = back.visBack()
        if back2 and p.v in back2.v.t.vnodeList:
            # A weird special case: just select back2.
            c.selectPosition(back2)
            c.treeWantsFocusNow()
            return
    
        sparseMove = c.config.getBool('sparse_move_outline_left')
        c.beginUpdate()
        try: # update...
            c.endEditing()
            undoData = u.beforeMoveNode(p)
            dirtyVnodeList = p.setAllAncestorAtFileNodesDirty()
            #@        << Move p up >>
            #@+node:AGP.20250415230112.602:<< Move p up >>
            if 0:
                g.trace("visBack",back)
                g.trace("visBack2",back2)
                g.trace("oldParent",oldParent)
                g.trace("back2.hasChildren",back2.hasChildren())
                g.trace("back2.isExpanded",back2.isExpanded())
                
            parent = p.parent()
            
            if not back2:
                # p will be the new root node
                moved = True
                p.moveToRoot(oldRoot=c.rootPosition())
            
            elif back2.hasChildren() and back2.isExpanded():
                if c.checkMoveWithParentWithWarning(p,back2,True):
                    moved = True
                    p.moveToNthChildOf(back2,0)
            
            else:
                if c.checkMoveWithParentWithWarning(p,back2.parent(),True):
                    moved = True
                    p.moveAfter(back2)
            
            if moved and sparseMove and parent and not parent.isAncestorOf(p):
                # New in Leo 4.4.2: contract the old parent if it is no longer the parent of p.
                parent.contract()
            #@-node:AGP.20250415230112.602:<< Move p up >>
            #@nl
            if moved:
                if inAtIgnoreRange and not p.inAtIgnoreRange():
                    # The moved nodes have just become newly unignored.
                    dirtyVnodeList2 = p.setDirty() # Mark descendent @thin nodes dirty.
                else: # No need to mark descendents dirty.
                    dirtyVnodeList2 = p.setAllAncestorAtFileNodesDirty()
                dirtyVnodeList.extend(dirtyVnodeList2)
                c.setChanged(True)
                u.afterMoveNode(p,'Move Right',undoData,dirtyVnodeList)
                
        finally:
            c.selectPosition(p) # Also sets root position.
            c.endUpdate()
            c.treeWantsFocusNow()
        c.updateSyntaxColorer(p) # Moving can change syntax coloring.
    #@-node:AGP.20250415230112.601:moveOutlineUp
    #@+node:AGP.20250415230112.603:promote
    def promote (self,event=None):
        
        '''Make all children of the selected nodes siblings of the selected node.'''
    
        c = self ; u = c.undoer ; p = c.currentPosition()
        command = 'Promote'
        if not p or not p.hasChildren():
            c.treeWantsFocusNow()
            return
    
        isAtIgnoreNode = p.isAtIgnoreNode()
        inAtIgnoreRange = p.inAtIgnoreRange()
        c.beginUpdate()
        try: # In update...
            c.endEditing()
            u.beforeChangeGroup(p,command)
            after = p
            while p.hasChildren(): # Don't use an iterator.
                child = p.firstChild()
                undoData = u.beforeMoveNode(child)
                child.moveAfter(after)
                after = child
                u.afterMoveNode(child,command,undoData)
            c.setChanged(True)
            if not inAtIgnoreRange and isAtIgnoreNode:
                # The promoted nodes have just become newly unignored.
                dirtyVnodeList = p.setDirty() # Mark descendent @thin nodes dirty.
            else: # No need to mark descendents dirty.
                dirtyVnodeList = p.setAllAncestorAtFileNodesDirty()
            u.afterChangeGroup(p,command,dirtyVnodeList=dirtyVnodeList)
            c.selectPosition(p)
        finally:
            c.endUpdate()
            c.treeWantsFocusNow()
        c.updateSyntaxColorer(p) # Moving can change syntax coloring.
    #@-node:AGP.20250415230112.603:promote
    #@-node:AGP.20250415230112.595:Move... (Commands)
    #@-node:AGP.20250415230112.479:Outline menu...
    #@+node:AGP.20250415230112.604:Window Menu
    #@+node:AGP.20250415230112.605:openCompareWindow
    def openCompareWindow (self,event=None):
        
        '''Open a dialog for comparing files and directories.'''
        
        c = self ; frame = c.frame
        
        if not frame.comparePanel:
            frame.comparePanel = g.app.gui.createComparePanel(c)
    
        frame.comparePanel.bringToFront()
    #@-node:AGP.20250415230112.605:openCompareWindow
    #@+node:AGP.20250415230112.606:openPythonWindow
    def openPythonWindow (self,event=None):
        
        '''Open Python's Idle debugger in a separate process.'''
        
        pythonDir = g.os_path_dirname(sys.executable)
        idle = g.os_path_join(pythonDir,'Lib','idlelib','idle.py')
        args = [sys.executable, idle ]
        
        if 1: # Use present environment.
            os.spawnv(os.P_NOWAIT, sys.executable, args)
        else: # Use a pristine environment.
            os.spawnve(os.P_NOWAIT, sys.executable, args, os.environ)
    #@-node:AGP.20250415230112.606:openPythonWindow
    #@-node:AGP.20250415230112.604:Window Menu
    #@+node:AGP.20250415230112.607:Help Menu
    #@+node:AGP.20250415230112.608:about (version number & date)
    def about (self,event=None):
        
        '''Bring up an About Leo Dialog.'''
        
        c = self
        
        # Don't use triple-quoted strings or continued strings here.
        # Doing so would add unwanted leading tabs.
        version = "Leox 2024\n\n"
        theCopyright = ("Based on Leo 4.4.2.1 final by Edward K. Ream\n\n")
        url = "https://github.com/izaquar/Leox\n\n"
        email = ""
    
        g.app.gui.runAboutLeoDialog(c,version,theCopyright,url,email)
    #@-node:AGP.20250415230112.608:about (version number & date)
    #@+node:AGP.20250415230112.609:openLeoSettings and openMyLeoSettings
    def openLeoSettings (self,event=None):
        '''Open leoSettings.leo in a new Leo window.'''
        self.openSettingsHelper('leoSettings.leo')
        
    def openMyLeoSettings (self,event=None):
        '''Open myLeoSettings.leo in a new Leo window.'''
        self.openSettingsHelper('myLeoSettings.leo')
        
    def openSettingsHelper(self,name):
        c = self
        homeDir = g.app.homeDir
        loadDir = g.app.loadDir
        configDir = g.app.globalConfigDir
    
        # Look in configDir first.
        fileName = g.os_path_join(configDir,name)
    
        # Look in homeDir second.
        ok, frame = g.openWithFileName(fileName,c)
        if not ok:
            if configDir == loadDir:
                g.es("%s not found in %s" % (name,configDir))
            else:
                fileName = g.os_path_join(homeDir,name)
                ok, frame = g.openWithFileName(fileName,c)
                if not ok:
                    g.es("%s not found in %s or %s" % (name,configDir,homeDir))
    #@-node:AGP.20250415230112.609:openLeoSettings and openMyLeoSettings
    #@+node:AGP.20250415230112.610:openLeoScripts
    def openLeoScripts (self,event=None):
        
        c = self
        fileName = g.os_path_join(g.app.loadDir,'..','scripts','scripts.leo')
    
        ok, frame = g.openWithFileName(fileName,c)
        if not ok:
            g.es('not found: %s' % fileName)
    #@-node:AGP.20250415230112.610:openLeoScripts
    #@+node:AGP.20250415230112.611:leoDocumentation
    def leoDocumentation (self,event=None):
        
        '''Open LeoDocs.leo in a new Leo window.'''
        
        c = self ; name = "LeoDocs.leo"
    
        fileName = g.os_path_join(g.app.loadDir,"..","doc",name)
        ok,frame = g.openWithFileName(fileName,c)
        if not ok:
            g.es("not found: %s" % name)
    
        
    #@nonl
    #@-node:AGP.20250415230112.611:leoDocumentation
    #@+node:AGP.20250415230112.612:leoHome
    def leoHome (self,event=None):
        
        '''Open Leo's Home page in a web browser.'''
        
        import webbrowser
    
        url = "http://webpages.charter.net/edreamleo/front.html"
        try:
            webbrowser.open_new(url)
        except:
            g.es("not found: " + url)
    #@-node:AGP.20250415230112.612:leoHome
    #@+node:AGP.20250415230112.613:leoPlugins
    def openLeoPlugins (self,event=None):
        
        '''Open leoPlugins.leo in a new Leo window.'''
        
        c = self ; name = "leoPlugins.leo"
        fileName = g.os_path_join(g.app.loadDir,"..","plugins",name)
        ok,frame = g.openWithFileName(fileName,c)
        if not ok:
            g.es("not found: %s" % name)
    #@-node:AGP.20250415230112.613:leoPlugins
    #@+node:AGP.20250415230112.614:leoTutorial (version number)
    def leoTutorial (self,event=None):
        
        '''Open Leo's online tutorial in a web browser.'''
        
        import webbrowser
    
        if 1: # new url
            url = "http://www.3dtree.com/ev/e/sbooks/leo/sbframetoc_ie.htm"
        else:
            url = "http://www.evisa.com/e/sbooks/leo/sbframetoc_ie.htm"
        try:
            webbrowser.open_new(url)
        except:
            g.es("not found: " + url)
    #@-node:AGP.20250415230112.614:leoTutorial (version number)
    #@+node:AGP.20250415230112.615:leoUsersGuide
    def leoUsersGuide (self,event=None):
        
        '''Open Leo's users guide in a web browser.'''
        
        import webbrowser
        
        theFile = g.os_path_abspath(
            g.os_path_join(
                g.app.loadDir,'..','doc','html','leo_TOC.html'))
    
        url = 'file:%s' % theFile
        
        try:
            webbrowser.open_new(url)
        except:
            g.es("not found: " + url)
    #@-node:AGP.20250415230112.615:leoUsersGuide
    #@-node:AGP.20250415230112.607:Help Menu
    #@-node:AGP.20250415230112.355:Command handlers...
    #@+node:AGP.20250415230112.616:Dragging (commands)
    #@+node:AGP.20250415230112.617:c.dragAfter
    def dragAfter(self,p,after):
    
        c = self ; u = self.undoer ; undoType = 'Drag'
        current = c.currentPosition()
        inAtIgnoreRange = p.inAtIgnoreRange()
        if not c.checkMoveWithParentWithWarning(p,after.parent(),True): return
    
        c.beginUpdate()
        try: # In update...
            c.endEditing()
            undoData = u.beforeMoveNode(current)
            dirtyVnodeList = p.setAllAncestorAtFileNodesDirty()
            p.moveAfter(after)
            if inAtIgnoreRange and not p.inAtIgnoreRange():
                # The moved nodes have just become newly unignored.
                dirtyVnodeList2 = p.setDirty() # Mark descendent @thin nodes dirty.
                dirtyVnodeList.extend(dirtyVnodeList2)
            else: # No need to mark descendents dirty.
                dirtyVnodeList2 = p.setAllAncestorAtFileNodesDirty()
                dirtyVnodeList.extend(dirtyVnodeList2)
            c.setChanged(True)
            u.afterMoveNode(p,undoType,undoData,dirtyVnodeList=dirtyVnodeList)
        finally:
            c.selectPosition(p) # Also sets root position.
            c.endUpdate()
        c.updateSyntaxColorer(p) # Dragging can change syntax coloring.
    #@-node:AGP.20250415230112.617:c.dragAfter
    #@+node:AGP.20250415230112.618:c.dragCloneToNthChildOf
    def dragCloneToNthChildOf (self,p,parent,n):
    
        c = self ; u = c.undoer ; undoType = 'Clone Drag'
        current = c.currentPosition()
        inAtIgnoreRange = p.inAtIgnoreRange()
        
        c.beginUpdate()
        try: # In update...
            # g.trace("p,parent,n:",p.headString(),parent.headString(),n)
            clone = p.clone() # Creates clone & dependents, does not set undo.
            if not c.checkMoveWithParentWithWarning(clone,parent,True):
                clone.doDelete() # Destroys clone and makes p the current node.
                c.selectPosition(p) # Also sets root position.
                c.endUpdate(False) # Nothing has changed.
                return
            c.endEditing()
            undoData = u.beforeInsertNode(current)
            dirtyVnodeList = clone.setAllAncestorAtFileNodesDirty()
            clone.moveToNthChildOf(parent,n)
            if inAtIgnoreRange and not p.inAtIgnoreRange():
                # The moved nodes have just become newly unignored.
                dirtyVnodeList2 = p.setDirty() # Mark descendent @thin nodes dirty.
                dirtyVnodeList.extend(dirtyVnodeList2)
            else: # No need to mark descendents dirty.
               dirtyVnodeList2 =  p.setAllAncestorAtFileNodesDirty()
               dirtyVnodeList.extend(dirtyVnodeList2)
            c.setChanged(True)
            u.afterInsertNode(clone,undoType,undoData,dirtyVnodeList=dirtyVnodeList)
        finally:
            c.selectPosition(clone) # Also sets root position.
            c.endUpdate()
        c.updateSyntaxColorer(clone) # Dragging can change syntax coloring.
    #@-node:AGP.20250415230112.618:c.dragCloneToNthChildOf
    #@+node:AGP.20250415230112.619:c.dragToNthChildOf
    def dragToNthChildOf(self,p,parent,n):
    
        c = self ; u = c.undoer ; undoType = 'Drag'
        current = c.currentPosition()
        inAtIgnoreRange = p.inAtIgnoreRange()
        if not c.checkMoveWithParentWithWarning(p,parent,True): return
    
        c.beginUpdate()
        try: # In update...
            c.endEditing()
            undoData = u.beforeMoveNode(current)
            dirtyVnodeList = p.setAllAncestorAtFileNodesDirty()
            p.moveToNthChildOf(parent,n)
            if inAtIgnoreRange and not p.inAtIgnoreRange():
                # The moved nodes have just become newly unignored.
                dirtyVnodeList2 = p.setDirty() # Mark descendent @thin nodes dirty.
                dirtyVnodeList.extend(dirtyVnodeList2)
            else: # No need to mark descendents dirty.
                dirtyVnodeList2 = p.setAllAncestorAtFileNodesDirty()
                dirtyVnodeList.extend(dirtyVnodeList2)
            c.setChanged(True)
            u.afterMoveNode(p,undoType,undoData,dirtyVnodeList=dirtyVnodeList)
        finally:
            c.selectPosition(p) # Also sets root position.
            c.endUpdate()
        c.updateSyntaxColorer(p) # Dragging can change syntax coloring.
    #@-node:AGP.20250415230112.619:c.dragToNthChildOf
    #@+node:AGP.20250415230112.620:c.dragCloneAfter
    def dragCloneAfter (self,p,after):
    
        c = self ; u = c.undoer ; undoType = 'Clone Drag'
        current = c.currentPosition()
    
        c.beginUpdate()
        try: # In update...
            clone = p.clone() # Creates clone.  Does not set undo.
            if c.checkMoveWithParentWithWarning(clone,after.parent(),True):
                inAtIgnoreRange = clone.inAtIgnoreRange()
                c.endEditing()
                undoData = u.beforeInsertNode(current)
                dirtyVnodeList = clone.setAllAncestorAtFileNodesDirty()
                clone.moveAfter(after)
                if inAtIgnoreRange and not clone.inAtIgnoreRange():
                    # The moved node have just become newly unignored.
                    dirtyVnodeList2 = clone.setDirty() # Mark descendent @thin nodes dirty.
                    dirtyVnodeList.extend(dirtyVnodeList2)
                else: # No need to mark descendents dirty.
                    dirtyVnodeList2 = clone.setAllAncestorAtFileNodesDirty()
                    dirtyVnodeList.extend(dirtyVnodeList2)
                c.setChanged(True)
                u.afterInsertNode(clone,undoType,undoData,dirtyVnodeList=dirtyVnodeList)
                p = clone
            else:
                # g.trace("invalid clone drag")
                clone.doDelete()
        finally:
            c.selectPosition(p) # Also sets root position.
            c.endUpdate()
        c.updateSyntaxColorer(clone) # Dragging can change syntax coloring.
    #@nonl
    #@-node:AGP.20250415230112.620:c.dragCloneAfter
    #@-node:AGP.20250415230112.616:Dragging (commands)
    #@+node:AGP.20250415230112.621:Drawing Utilities (commands)
    #@+node:AGP.20250415230112.622:c.begin/endUpdate
    #@+at
    # **Important** These methods ensure that exactly zero or one (depending 
    # on the
    # argument to endUpdate) redraws exist within the section of code bounded 
    # by
    # c.beginUpdate and c.endUpdate. This greatly simplifies and clarifies the 
    # code.
    # 
    # Callers should ensure that every beginUpdate is matched with an 
    # endUpdate by
    # using the following pattern:
    #     c.beginUpdate()
    #     try:
    #         << whatever >>
    #     finally:
    #         c.endUpdate()
    #@-at
    #@@c
    
    def beginUpdate(self):
        
        '''Suppress redraws of the tree (except for explict calls to c.redraw_now)
        until the matching call to endUpdate.'''
        
        c = self
        c.frame.tree.beginUpdate()
        
    def endUpdate(self,flag=True,scroll=True):
        
        '''Redraw the screen if flag is True.'''
    
        c = self
        c.frame.tree.endUpdate(flag,scroll=scroll)
    
    BeginUpdate = beginUpdate # Compatibility with old scripts
    EndUpdate = endUpdate # Compatibility with old scripts
    #@-node:AGP.20250415230112.622:c.begin/endUpdate
    #@+node:AGP.20250415230112.623:c.bringToFront
    def bringToFront(self,set_focus=True):
        print "bringtofront"
        c = self
        c.frame.deiconify()
        
        if set_focus:
            bodyCtrl = c.frame.body.bodyCtrl
            # g.trace(g.app.gui.widget_name(bodyCtrl))
            bodyCtrl.update_idletasks()
            g.app.gui.set_focus(c,bodyCtrl)
    
    BringToFront = bringToFront # Compatibility with old scripts
    #@-node:AGP.20250415230112.623:c.bringToFront
    #@+node:AGP.20250415230112.624:c.xWantsFocusNow
    def bodyWantsFocusNow(self):
        c = self ; body = c.frame.body
        #g.trace(body and body.bodyCtrl)
        c.set_focus(body and body.bodyCtrl,force=True)
        
    def headlineWantsFocusNow(self,p):
        c = self
        c.set_focus(p and c.edit_widget(p),force=True)
        
    def logWantsFocusNow(self):
        c = self ; log = c.frame.log
        c.set_focus(log and log.logCtrl,force=True)
    
    def minibufferWantsFocusNow(self):
        c = self ; k = c.k
        k and k.minibufferWantsFocusNow()
        
    def treeWantsFocusNow(self):
        c = self ; tree = c.frame.tree
        c.set_focus(tree and tree.canvas,force=True)
        
    def widgetWantsFocusNow(self,w):
        c = self ; c.set_focus(w,force=True)
    #@-node:AGP.20250415230112.624:c.xWantsFocusNow
    #@+node:AGP.20250415230112.625:c.xWantsFocus
    def bodyWantsFocus(self):
        c = self ; body = c.frame.body
        c.request_focus(body and body.bodyCtrl)
    def headlineWantsFocus(self,p):
        c = self
        c.request_focus(p and c.edit_widget(p))
        
    def logWantsFocus(self):
        c = self ; log = c.frame.log
        c.request_focus(log and log.logCtrl)
        
    def minibufferWantsFocus(self):
        c = self ; k = c.k
        k and k.minibufferWantsFocus()
        
    def treeWantsFocus(self):
        c = self ; tree = c.frame.tree
        #g.print_stack()
        c.request_focus(tree and tree.canvas)
        
    def widgetWantsFocus(self,w):
        c = self ; c.request_focus(w)
    #@-node:AGP.20250415230112.625:c.xWantsFocus
    #@+node:AGP.20250415230112.626:c.widget_name
    def widget_name (self,widget):
        
        c = self
        
        return c.gui.widget_name(widget) or ''
    #@-node:AGP.20250415230112.626:c.widget_name
    #@+node:AGP.20250415230112.627:c.traceFocus
    trace_focus_count = 0
    
    def traceFocus (self,w):
        
        c = self
    
        if not g.app.unitTesting and c.config.getBool('trace_focus'):
            c.trace_focus_count += 1
            print '%4d' % (c.trace_focus_count),c.widget_name(w),g.callers(8)
    #@-node:AGP.20250415230112.627:c.traceFocus
    #@+node:AGP.20250415230112.628:c.restoreFocus
    def restoreFocus (self):
        
        '''Ensure that the focus eventually gets restored.'''
        
        c =self
        trace = not g.app.unitTesting and c.config.getBool('trace_focus')
    
        if c.requestedFocusWidget:
            c.hasFocusWidget = None # Force an update
        elif c.hasFocusWidget:
            c.requestedFocusWidget = c.hasFocusWidget
            c.hasFocusWidget = None # Force an update
        else:
            # Should not happen, except during unit testing.
            # c.masterFocusHandler sets c.hasFocusWidget,
            # so if it is not set here it is because this method cleared it.
            if not g.app.unitTesting: g.trace('oops: no requested or present widget.',g.callers())
            c.bodyWantsFocusNow()
        
        if c.inCommand:
            if trace: g.trace('expecting later call to c.masterFocusHandler')
            pass # A call to c.masterFocusHandler will surely happen.
        else:
            c.masterFocusHandler() # Do it now.
    #@-node:AGP.20250415230112.628:c.restoreFocus
    #@+node:AGP.20250415230112.629:c.redraw and c.redraw_now
    def redraw (self):
        c = self
        c.beginUpdate()
        c.endUpdate()
    
    def redraw_now (self):
        
        c = self
        
        if g.app.quitting or not c.exists or not hasattr(c.frame,'top'):
            return # nullFrame's do not have a top frame.
    
        c.frame.tree.redraw_now()
        if 0: # Interferes with new colorizer.
            c.frame.top.update_idletasks()
        
        if c.frame.requestRecolorFlag:
            c.frame.requestRecolorFlag = False
            c.recolor()
    
    # Compatibility with old scripts
    force_redraw = redraw_now
    #@-node:AGP.20250415230112.629:c.redraw and c.redraw_now
    #@+node:AGP.20250415230112.630:c.recolor_now
    def recolor_now(self,p=None,incremental=False,interruptable=True):
    
        c = self
        if p is None:
            p = c.currentPosition()
    
        c.frame.body.colorizer.colorize(p,incremental=incremental)#,interruptable=interruptable)
    #@-node:AGP.20250415230112.630:c.recolor_now
    #@+node:AGP.20250415230112.631:c.recolor & requestRecolor
    def recolor(self):
        c = self
        c.frame.body.recolor_now(c.currentPosition())
        
    def requestRecolor (self):
        
        c = self
        c.frame.requestRecolorFlag = True
    #@-node:AGP.20250415230112.631:c.recolor & requestRecolor
    #@+node:AGP.20250415230112.632:c.masterFocusHandler
    def masterFocusHandler (self):
        
        c = self ; 
        trace = not g.app.unitTesting and c.config.getBool('trace_masterFocusHandler')
        
        # Give priority to later requests, but default to previously set widget.
        w = c.requestedFocusWidget or c.hasFocusWidget
        
        if trace: print \
            'requested',c.widget_name(c.requestedFocusWidget),\
            'present',c.widget_name(c.hasFocusWidget)
        
        if c.hasFocusWidget and (
            not c.requestedFocusWidget or c.requestedFocusWidget == c.hasFocusWidget):
            if trace: print 'no change.',c.widget_name(w)
            c.requestedFocusWidget = None
        elif w:
            # Ignore whatever g.app.gui.get_focus might say.
            ok = g.app.gui.set_focus(c,w)
            if ok: c.hasFocusWidget = w
            c.requestedFocusWidget = None
        else:
            # This is not an error: it can arise because of a call to k.invalidateFocus.
            if trace: print '*'*20,'oops: moving to body pane.'
            c.bodyWantsFocusNow()
    
    restoreRequestedFocus = masterFocusHandler
    #@-node:AGP.20250415230112.632:c.masterFocusHandler
    #@+node:AGP.20250415230112.633:c.invalidateFocus
    def invalidateFocus (self):
        
        '''Indicate that the focus is in an invalid location, or is unknown.'''
        
        c = self
        c.requestedFocusWidget = None
        c.hasFocusWidget = None
        # g.trace(g.callers())
    #@-node:AGP.20250415230112.633:c.invalidateFocus
    #@+node:AGP.20250415230112.634:c.get/request/set_focus
    def get_focus (self):
        
        c = self
        return g.app.gui.get_focus(c)
        
    def get_requested_focus (self):
        
        c = self
        return c.requestedFocusWidget or c.hasFocusWidget or g.app.gui.get_focus(c)
        
    def request_focus(self,w):
    
        c = self
        if w: c.requestedFocusWidget = w
        c.traceFocus(w)
        
    def set_focus (self,w,force=False):
        
        c = self
        
        if force: # New in Leo 4.4.2: safer.
            c.hasFocusWidget = c.requestedFocusWidget = w
            g.app.gui.set_focus(c,w)
            c.traceFocus(w)
        else: # An optimization.
            c.requestedFocusWidget = w
            c.masterFocusHandler()
    #@-node:AGP.20250415230112.634:c.get/request/set_focus
    #@-node:AGP.20250415230112.621:Drawing Utilities (commands)
    #@+node:AGP.20250415230112.635:Enabling Menu Items
    #@+node:AGP.20250415230112.636:Slow routines: no longer used
    #@+node:AGP.20250415230112.637:canGoToNextDirtyHeadline (slow)
    def canGoToNextDirtyHeadline (self):
        
        c = self ; current = c.currentPosition()
    
        for p in c.allNodes_iter():
            if p != current and p.isDirty():
                return True
        
        return False
    #@-node:AGP.20250415230112.637:canGoToNextDirtyHeadline (slow)
    #@+node:AGP.20250415230112.638:canGoToNextMarkedHeadline (slow)
    def canGoToNextMarkedHeadline (self):
        
        c = self ; current = c.currentPosition()
            
        for p in c.allNodes_iter():
            if p != current and p.isMarked():
                return True
    
        return False
    #@-node:AGP.20250415230112.638:canGoToNextMarkedHeadline (slow)
    #@+node:AGP.20250415230112.639:canMarkChangedHeadline (slow)
    def canMarkChangedHeadlines (self):
        
        c = self
        
        for p in c.allNodes_iter():
            if p.isDirty():
                return True
        
        return False
    #@-node:AGP.20250415230112.639:canMarkChangedHeadline (slow)
    #@+node:AGP.20250415230112.640:canMarkChangedRoots (slow)
    def canMarkChangedRoots (self):
        
        c = self
        
        for p in c.allNodes_iter():
            if p.isDirty and p.isAnyAtFileNode():
                return True
    
        return False
    #@-node:AGP.20250415230112.640:canMarkChangedRoots (slow)
    #@-node:AGP.20250415230112.636:Slow routines: no longer used
    #@+node:AGP.20250415230112.641:canClone (new for hoist)
    def canClone (self):
    
        c = self
        
        if c.hoistStack:
            current = c.currentPosition()
            bunch = c.hoistStack[-1]
            return current != bunch.p
        else:
            return True
    #@-node:AGP.20250415230112.641:canClone (new for hoist)
    #@+node:AGP.20250415230112.642:canContractAllHeadlines
    def canContractAllHeadlines (self):
        
        c = self
        
        for p in c.allNodes_iter():
            if p.isExpanded():
                return True
    
        return False
    #@-node:AGP.20250415230112.642:canContractAllHeadlines
    #@+node:AGP.20250415230112.643:canContractAllSubheads
    def canContractAllSubheads (self):
    
        c = self ; current = c.currentPosition()
        
        for p in current.subtree_iter():
            if p != current and p.isExpanded():
                return True
    
        return False
    #@-node:AGP.20250415230112.643:canContractAllSubheads
    #@+node:AGP.20250415230112.644:canContractParent
    def canContractParent (self):
    
        c = self
        return c.currentPosition().parent()
    #@-node:AGP.20250415230112.644:canContractParent
    #@+node:AGP.20250415230112.645:canContractSubheads
    def canContractSubheads (self):
        
        c = self ; current = c.currentPosition()
    
        for child in current.children_iter():
            if child.isExpanded():
                return True
            
        return False
    #@-node:AGP.20250415230112.645:canContractSubheads
    #@+node:AGP.20250415230112.646:canCutOutline & canDeleteHeadline
    def canDeleteHeadline (self):
        
        c = self ; p = c.currentPosition()
    
        return p.hasParent() or p.hasThreadBack() or p.hasNext()
    
    canCutOutline = canDeleteHeadline
    #@-node:AGP.20250415230112.646:canCutOutline & canDeleteHeadline
    #@+node:AGP.20250415230112.647:canDemote
    def canDemote (self):
    
        c = self
        return c.currentPosition().hasNext()
    #@-node:AGP.20250415230112.647:canDemote
    #@+node:AGP.20250415230112.648:canExpandAllHeadlines
    def canExpandAllHeadlines (self):
        
        c = self
        
        for p in c.allNodes_iter():
            if not p.isExpanded():
                return True
    
        return False
    #@-node:AGP.20250415230112.648:canExpandAllHeadlines
    #@+node:AGP.20250415230112.649:canExpandAllSubheads
    def canExpandAllSubheads (self):
    
        c = self
        
        for p in c.currentPosition().subtree_iter():
            if not p.isExpanded():
                return True
            
        return False
    #@-node:AGP.20250415230112.649:canExpandAllSubheads
    #@+node:AGP.20250415230112.650:canExpandSubheads
    def canExpandSubheads (self):
    
        c = self ; current = c.currentPosition()
        
        for p in current.children_iter():
            if p != current and not p.isExpanded():
                return True
    
        return False
    #@-node:AGP.20250415230112.650:canExpandSubheads
    #@+node:AGP.20250415230112.651:canExtract, canExtractSection & canExtractSectionNames
    def canExtract (self):
    
        c = self ; body = c.frame.body
        return body and body.hasTextSelection()
        
    canExtractSectionNames = canExtract
            
    def canExtractSection (self):
    
        c = self ; body = c.frame.body
        if not body: return False
        
        s = body.getSelectedText()
        if not s: return False
    
        line = g.get_line(s,0)
        i1 = line.find("<<")
        j1 = line.find(">>")
        i2 = line.find("@<")
        j2 = line.find("@>")
        return -1 < i1 < j1 or -1 < i2 < j2
    #@-node:AGP.20250415230112.651:canExtract, canExtractSection & canExtractSectionNames
    #@+node:AGP.20250415230112.652:canFindMatchingBracket
    def canFindMatchingBracket (self):
        
        c = self ; brackets = "()[]{}"
        c1 = c.frame.body.getCharAtInsertPoint()
        c2 = c.frame.body.getCharBeforeInsertPoint()
        return (c1 and c1 in brackets) or (c2 and c2 in brackets)
    #@-node:AGP.20250415230112.652:canFindMatchingBracket
    #@+node:AGP.20250415230112.653:canHoist & canDehoist
    def canDehoist(self):
        
        return len(self.hoistStack) > 0
            
    def canHoist(self):
        
        c = self
        
        # N.B.  This is called at idle time, so minimizing positions is crucial!
        if c.hoistStack:
            bunch = c.hoistStack[-1]
            return bunch.p and not c.isCurrentPosition(bunch.p)
        elif c.currentPositionIsRootPosition():
            return c.currentPositionHasNext()
        else:
            return True
    #@-node:AGP.20250415230112.653:canHoist & canDehoist
    #@+node:AGP.20250415230112.654:canMoveOutlineDown
    def canMoveOutlineDown (self):
    
        c = self ; current = c.currentPosition()
            
        p = current.visNext()
        while p and current.isAncestorOf(p):
            p.moveToVisNext()
    
        if c.hoistStack:
            bunch = c.hoistStack[-1]
            return p and p != bunch.p and bunch.p.isAncestorOf(p)
        else:
            return p
    #@-node:AGP.20250415230112.654:canMoveOutlineDown
    #@+node:AGP.20250415230112.655:canMoveOutlineLeft
    def canMoveOutlineLeft (self):
    
        c = self ; p = c.currentPosition()
    
        if c.hoistStack:
            bunch = c.hoistStack[-1]
            if p and p.hasParent():
                p.moveToParent()
                return p != bunch.p and bunch.p.isAncestorOf(p)
            else:
                return False
        else:
            return p and p.hasParent()
    #@-node:AGP.20250415230112.655:canMoveOutlineLeft
    #@+node:AGP.20250415230112.656:canMoveOutlineRight
    def canMoveOutlineRight (self):
    
        c = self ; p = c.currentPosition()
        
        if c.hoistStack:
            bunch = c.hoistStack[-1]
            return p and p.hasBack() and p != bunch.p
        else:
            return p and p.hasBack()
    #@-node:AGP.20250415230112.656:canMoveOutlineRight
    #@+node:AGP.20250415230112.657:canMoveOutlineUp
    def canMoveOutlineUp (self):
    
        c = self ; p = c.currentPosition()
        if not p: return False
        
        pback = p.visBack()
        if not pback: return False
    
        if c.hoistStack:
            bunch = c.hoistStack[-1]
            return bunch.p != p and bunch.p.isAncestorOf(pback)
        else:
            return True
    #@-node:AGP.20250415230112.657:canMoveOutlineUp
    #@+node:AGP.20250415230112.658:canPasteOutline
    def canPasteOutline (self,s=None):
    
        c = self
        if s == None:
            s = g.app.gui.getTextFromClipboard()
        if not s:
            return False
    
        # g.trace(s)
        if g.match(s,0,g.app.prolog_prefix_string):
            return True
        elif len(s) > 0:
            return c.importCommands.stringIsValidMoreFile(s)
        else:
            return False
    #@-node:AGP.20250415230112.658:canPasteOutline
    #@+node:AGP.20250415230112.659:canPromote
    def canPromote (self):
    
        c = self ; v = c.currentVnode()
        return v and v.hasChildren()
    #@-node:AGP.20250415230112.659:canPromote
    #@+node:AGP.20250415230112.660:canRevert
    def canRevert (self):
    
        # c.mFileName will be "untitled" for unsaved files.
        c = self
        return (c.frame and c.mFileName and c.isChanged())
    #@-node:AGP.20250415230112.660:canRevert
    #@+node:AGP.20250415230112.661:canSelect....
    # 7/29/02: The shortcuts for these commands are now unique.
    
    def canSelectThreadBack (self):
        c = self ; p = c.currentPosition()
        return p.hasThreadBack()
        
    def canSelectThreadNext (self):
        c = self ; p = c.currentPosition()
        return p.hasThreadNext()
    
    def canSelectVisBack (self):
        c = self ; p = c.currentPosition()
        return p.hasVisBack()
        
    def canSelectVisNext (self):
        c = self ; p = c.currentPosition()
        return p.hasVisNext()
    #@-node:AGP.20250415230112.661:canSelect....
    #@+node:AGP.20250415230112.662:canShiftBodyLeft/Right
    def canShiftBodyLeft (self):
    
        c = self ; body = c.frame.body
        return body and body.getAllText()
    
    canShiftBodyRight = canShiftBodyLeft
    #@-node:AGP.20250415230112.662:canShiftBodyLeft/Right
    #@+node:AGP.20250415230112.663:canSortChildren, canSortSiblings
    def canSortChildren (self):
        
        c = self ; p = c.currentPosition()
        return p and p.hasChildren()
    
    def canSortSiblings (self):
    
        c = self ; p = c.currentPosition()
        return p and (p.hasNext() or p.hasBack())
    #@-node:AGP.20250415230112.663:canSortChildren, canSortSiblings
    #@+node:AGP.20250415230112.664:canUndo & canRedo
    def canUndo (self):
    
        c = self
        return c.undoer.canUndo()
        
    def canRedo (self):
    
        c = self
        return c.undoer.canRedo()
    #@-node:AGP.20250415230112.664:canUndo & canRedo
    #@+node:AGP.20250415230112.665:canUnmarkAll
    def canUnmarkAll (self):
        
        c = self
        
        for p in c.allNodes_iter():
            if p.isMarked():
                return True
    
        return False
    #@-node:AGP.20250415230112.665:canUnmarkAll
    #@-node:AGP.20250415230112.635:Enabling Menu Items
    #@+node:AGP.20250415230112.666:Getters & Setters
    #@+node:AGP.20250415230112.667:Getters
    #@+node:AGP.20250415230112.668:c.currentPosition
    def currentPosition (self,copy=True):
        
        """Return the presently selected position."""
        
        c = self
    
        if c._currentPosition:
            # New in Leo 4.4.2: *always* return a copy.
            return c._currentPosition.copy()
        else:
            return c.nullPosition()
        
    # For compatibiility with old scripts.
    currentVnode = currentPosition
    #@-node:AGP.20250415230112.668:c.currentPosition
    #@+node:AGP.20250415230112.669:c.edit_widget
    def edit_widget (self,p):
        
        c = self
        
        return p and c.frame.tree.edit_widget(p)
    #@nonl
    #@-node:AGP.20250415230112.669:c.edit_widget
    #@+node:AGP.20250415230112.670:c.fileName & shortFileName
    # Compatibility with scripts
    
    def fileName (self):
    
        return self.mFileName
    
    def shortFileName (self):
        
        return g.shortFileName(self.mFileName)
    
    shortFilename = shortFileName
    #@-node:AGP.20250415230112.670:c.fileName & shortFileName
    #@+node:AGP.20250415230112.671:c.findRootPosition New in 4.4.2
    #@+at 
    #@nonl
    # Aha! The Commands class can easily recompute the root position::
    # 
    #     c.setRootPosition(c.findRootPosition(p))
    # 
    # Any command that changes the outline should call this code.
    # 
    # As a result, the fundamental p and v methods that alter trees need never
    # convern themselves about reporting the changed root.  A big improvement.
    #@-at
    #@@c
    
    def findRootPosition (self,p):
        
        '''Return the root position of the outline containing p.'''
        
        c = self ; p = p.copy()
        
        while p and p.hasParent():
            p.moveToParent()
            
        while p and p.hasBack():
            p.moveToBack()
            
        # g.trace(p and p.headString())
    
        return p
    #@nonl
    #@-node:AGP.20250415230112.671:c.findRootPosition New in 4.4.2
    #@+node:AGP.20250415230112.672:c.is...Position
    #@+node:AGP.20250415230112.673:c.currentPositionIsRootPosition
    def currentPositionIsRootPosition (self):
        
        """Return True if the current position is the root position.
        
        This method is called during idle time, so not generating positions
        here fixes a major leak.
        """
        
        c = self
        
        return (
            c._currentPosition and c._rootPosition and
            c._currentPosition == c._rootPosition)
    #@-node:AGP.20250415230112.673:c.currentPositionIsRootPosition
    #@+node:AGP.20250415230112.674:c.currentPositionHasNext
    def currentPositionHasNext (self):
        
        """Return True if the current position is the root position.
        
        This method is called during idle time, so not generating positions
        here fixes a major leak.
        """
        
        c = self ; current = c._currentPosition 
        
        return current and current.hasNext()
    #@-node:AGP.20250415230112.674:c.currentPositionHasNext
    #@+node:AGP.20250415230112.675:c.isCurrentPosition
    def isCurrentPosition (self,p):
        
        c = self
        
        if p is None or c._currentPosition is None:
            return False
        else:
            return p.isEqual(c._currentPosition)
    #@-node:AGP.20250415230112.675:c.isCurrentPosition
    #@+node:AGP.20250415230112.676:c.isRootPosition
    def isRootPosition (self,p):
        
        c = self
        
        if p is None or c._rootPosition is None:
            return False
        else:
            return p.isEqual(c._rootPosition)
    #@-node:AGP.20250415230112.676:c.isRootPosition
    #@-node:AGP.20250415230112.672:c.is...Position
    #@+node:AGP.20250415230112.677:c.isChanged
    def isChanged (self):
    
        return self.changed
    #@-node:AGP.20250415230112.677:c.isChanged
    #@+node:AGP.20250415230112.678:c.lastVisible
    def lastVisible(self):
        
        """Move to the last visible node of the entire tree."""
    
        c = self ; p = c.rootPosition()
        
        # Move to the last top-level node.
        while p.hasNext():
            p.moveToNext()
        assert(p.isVisible())
    
        # Move to the last visible child.
        while p.hasChildren() and p.isExpanded():
            p.moveToLastChild()
        
        return p
    #@-node:AGP.20250415230112.678:c.lastVisible
    #@+node:AGP.20250415230112.679:c.nullPosition
    def nullPosition (self):
        
        c = self ; v = None
        return leoNodes.position(v,[])
    #@-node:AGP.20250415230112.679:c.nullPosition
    #@+node:AGP.20250415230112.680:c.positionExists
    def positionExists(self,p):
        
        """Return True if a position exists in c's tree"""
        
        c = self ; p = p.copy()
    
        # This code must be fast.
        root = c.rootPosition()
    
        while p:
            # g.trace(p.headString(),'parent',p.parent(),'back',p.back())
            if p.equal(root):
                return True
            if p.hasParent():
                p.moveToParent()
            else:
                p.moveToBack()
            
        # g.trace('does not exist in root:',root.headString())
        return False
    #@-node:AGP.20250415230112.680:c.positionExists
    #@+node:AGP.20250415230112.681:c.rootPosition
    def rootPosition(self):
        
        """Return the root position."""
        
        c = self
        
        if self._rootPosition:
            return self._rootPosition.copy()
        else:
            return  c.nullPosition()
    
    # For compatibiility with old scripts.
    rootVnode = rootPosition
    #@nonl
    #@-node:AGP.20250415230112.681:c.rootPosition
    #@-node:AGP.20250415230112.667:Getters
    #@+node:AGP.20250415230112.682:Setters
    #@+node:AGP.20250415230112.683:c.appendStringToBody
    def appendStringToBody (self,p,s,encoding="utf-8"):
        
        c = self
        if not s: return
        
        body = p.bodyString()
        assert(g.isUnicode(body))
        s = g.toUnicode(s,encoding)
    
        c.setBodyString(p,body + s,encoding)
    #@-node:AGP.20250415230112.683:c.appendStringToBody
    #@+node:AGP.20250415230112.684:c.clearAllMarked
    def clearAllMarked (self):
        
        c = self
    
        for p in c.allNodes_iter():
            p.v.clearMarked()
    #@-node:AGP.20250415230112.684:c.clearAllMarked
    #@+node:AGP.20250415230112.685:c.clearAllVisited
    def clearAllVisited (self):
    
        c = self
    
        for p in c.allNodes_iter():
            p.v.clearVisited()
            p.v.t.clearVisited()
            p.v.t.clearWriteBit()
    #@-node:AGP.20250415230112.685:c.clearAllVisited
    #@+node:AGP.20250415230112.686:c.clearMarked
    def clearMarked  (self,p):
        
        c = self
        p.v.clearMarked()
        g.doHook("clear-mark",c=c,p=p,v=p)
    #@nonl
    #@-node:AGP.20250415230112.686:c.clearMarked
    #@+node:AGP.20250415230112.687:c.setBodyString
    def setBodyString (self,p,s,encoding="utf-8"):
    
        c = self ; v = p.v
        if not c or not v: return
    
        s = g.toUnicode(s,encoding)
        current = c.currentPosition()
        # 1/22/05: Major change: the previous test was: 'if p == current:'
        # This worked because commands work on the presently selected node.
        # But setRecentFiles may change a _clone_ of the selected node!
        if current and p.v.t==current.v.t:
            # Revert to previous code, but force an empty selection.
            c.frame.body.setSelectionAreas(s,None,None)
            c.frame.body.setTextSelection(None)
            # This code destoys all tags, so we must recolor.
            c.recolor()
            
        # Keep the body text in the tnode up-to-date.
        if v.t.bodyString != s:
            v.setTnodeText(s)
            
            v.t.setSelection(0,0)
            p.setDirty()
            if not c.isChanged():
                c.setChanged(True)
    #@-node:AGP.20250415230112.687:c.setBodyString
    #@+node:AGP.20250415230112.688:c.setChanged
    def setChanged (self,changedFlag):
    
        c = self
        if not c.frame: return
    
        # Clear all dirty bits _before_ setting the caption.
        # Clear all dirty bits except orphaned @file nodes
        if not changedFlag:
            # g.trace("clearing all dirty bits")
            for p in c.allNodes_iter():
                if p.isDirty() and not (p.isAtFileNode() or p.isAtNorefFileNode()):
                    p.clearDirty()
    
        # Update all derived changed markers.
        c.changed = changedFlag
        s = c.frame.getTitle()
        if len(s) > 2 and not c.loading: # don't update while loading.
            if changedFlag:
                if s [0] != '*': c.frame.setTitle("* " + s)
            else:
                if s[0:2]=="* ": c.frame.setTitle(s[2:])
    #@-node:AGP.20250415230112.688:c.setChanged
    #@+node:AGP.20250415230112.689:c.setCurrentPosition
    def setCurrentPosition (self,p):
        
        """Set the presently selected position. For internal use only.
        
        Client code should use c.selectPosition instead."""
        
        c = self
        
        # g.trace(p.headString(),g.callers())
        
        if p:
            # Important: p.equal requires c._currentPosition to be non-None.
            if c._currentPosition and p.equal(c._currentPosition):
                pass # We have already made a copy.
            else: # Must make a copy _now_
                c._currentPosition = p.copy()
                
            # New in Leo 4.4.2: always recompute the root position here.
            # This *guarantees* that c.rootPosition always returns the proper value.
            c.setRootPosition(c.findRootPosition(c._currentPosition))
        else:
            c._currentPosition = None
    
    # For compatibiility with old scripts.
    setCurrentVnode = setCurrentPosition
    #@nonl
    #@-node:AGP.20250415230112.689:c.setCurrentPosition
    #@+node:AGP.20250415230112.690:c.setHeadString
    def setHeadString (self,p,s,encoding="utf-8"):
    
        c = self ; t = c.edit_widget(p)
        
        p.initHeadString(s,encoding)
    
        if t:
            state = t.cget("state")
            # g.trace(state,s)
            t.configure(state="normal")
            t.delete("1.0","end")
            t.insert("end",s)
            t.configure(state=state,width=c.frame.tree.headWidth(s=s))
    
        p.setDirty()
    #@nonl
    #@-node:AGP.20250415230112.690:c.setHeadString
    #@+node:AGP.20250415230112.691:c.setLog
    def setLog (self):
        
        c = self
    
        if c.exists:
            try:
                # c.frame or c.frame.log may not exist.
                g.app.setLog(c.frame.log)
            except AttributeError:
                pass
    #@-node:AGP.20250415230112.691:c.setLog
    #@+node:AGP.20250415230112.692:c.setMarked
    def setMarked (self,p):
        
        c = self
        p.v.setMarked()
        g.doHook("set-mark",c=c,p=p,v=p)
    #@nonl
    #@-node:AGP.20250415230112.692:c.setMarked
    #@+node:AGP.20250415230112.693:c.setRootPosition
    def setRootPosition(self,p):
        
        """Set the root positioin."""
    
        c = self
        
        # g.trace(p.headString(),g.callers())
        
        if p:
            # Important: p.equal requires c._rootPosition to be non-None.
            if c._rootPosition and p.equal(c._rootPosition):
                pass # We have already made a copy.
            else:
                # We must make a copy _now_.
                c._rootPosition = p.copy()
        else:
            c._rootPosition = None
    #@nonl
    #@-node:AGP.20250415230112.693:c.setRootPosition
    #@+node:AGP.20250415230112.694:c.setRootVnode New in 4.4.2
    def setRootVnode (self, v):
        
        c = self
        newRoot = leoNodes.position(v,[])
        c.setRootPosition(newRoot)
    #@nonl
    #@-node:AGP.20250415230112.694:c.setRootVnode New in 4.4.2
    #@+node:AGP.20250415230112.695:c.topPosition & c.setTopPosition
    def topPosition(self):
        
        """Return the root position."""
        
        c = self
        
        if c._topPosition:
            return c._topPosition.copy()
        else:
            return c.nullPosition()
    
    def setTopPosition(self,p):
        
        """Set the root positioin."""
        
        c = self
    
        if p:
            c._topPosition = p.copy()
        else:
            c._topPosition = c.nullPosition()
        
    # Define these for compatibiility with old scripts.
    topVnode = topPosition
    setTopVnode = setTopPosition
    #@-node:AGP.20250415230112.695:c.topPosition & c.setTopPosition
    #@+node:AGP.20250415230112.696:c.trimTrailingLines
    def trimTrailingLines (self,p):
    
        """Trims trailing blank lines from a node.
        
        It is surprising difficult to do this during Untangle."""
    
        c = self
        body = p.bodyString()
        lines = string.split(body,'\n')
        i = len(lines) - 1 ; changed = False
        while i >= 0:
            line = lines[i]
            j = g.skip_ws(line,0)
            if j + 1 == len(line):
                del lines[i]
                i -= 1 ; changed = True
            else: break
        if changed:
            body = string.join(body,'') + '\n' # Add back one last newline.
            # g.trace(body)
            c.setBodyString(p,body)
            # Don't set the dirty bit: it would just be annoying.
    #@nonl
    #@-node:AGP.20250415230112.696:c.trimTrailingLines
    #@-node:AGP.20250415230112.682:Setters
    #@-node:AGP.20250415230112.666:Getters & Setters
    #@+node:AGP.20250415230112.697:Selecting & Updating (commands)
    #@+node:AGP.20250415230112.698:c.editPosition
    # Selects v: sets the focus to p and edits p.
    
    def editPosition(self,p,selectAll=False):
    
        c = self ; k = c.k
    
        if p:
            c.selectPosition(p)
            c.frame.tree.editLabel(p,selectAll=selectAll)
            
            if k:
                k.setDefaultUnboundKeyAction()
                k.showStateAndMode()
    #@-node:AGP.20250415230112.698:c.editPosition
    #@+node:AGP.20250415230112.699:c.endEditing (calls tree.endEditLabel)
    # Ends the editing in the outline.
    
    def endEditing(self):
        
        c = self
        c.frame.tree.endEditLabel()
    #@-node:AGP.20250415230112.699:c.endEditing (calls tree.endEditLabel)
    #@+node:AGP.20250415230112.700:c.selectPosition
    def selectPosition(self,p,updateBeadList=True):
        
        """Select a new position."""
    
        c = self
        
        # g.trace(p.headString(),g.callers())
    
        c.frame.tree.select(p,updateBeadList)
        
        # New in Leo 4.4.2.
        c.setCurrentPosition(p)
            # Do *not* test whether the position exists!
            # We may be in the midst of an undo.
    
    selectVnode = selectPosition
    #@-node:AGP.20250415230112.700:c.selectPosition
    #@+node:AGP.20250415230112.701:c.selectVnodeWithEditing
    # Selects the given node and enables editing of the headline if editFlag is True.
    
    def selectVnodeWithEditing(self,v,editFlag):
    
        c = self
        if editFlag:
            c.editPosition(v)
        else:
            c.selectVnode(v)
    
    selectPositionWithEditing = selectVnodeWithEditing
    #@-node:AGP.20250415230112.701:c.selectVnodeWithEditing
    #@+node:AGP.20250415230112.702:c.onCanvasKey
    def onCanvasKey (self,event):
        
        '''Navigate to the next headline starting with ch = event.char.
        If ch is uppercase, search all headlines; otherwise search only visible headlines.
        This is modelled on Windows explorer.'''
        
        if not event or not event.char or not event.keysym.isalnum():
            return
        c  = self ; p = c.currentPosition() ; p1 = p.copy()
        ch = event.char ; all = ch.isupper()
        found = False
        extend = self.navQuickKey()
        attempts = g.choose(extend,(True,False),(False,))
        for extend2 in attempts:
            p = p1.copy()
            while 1:
                if all:
                    p.moveToThreadNext()
                else:
                    p.moveToVisNext()
                if not p:
                    p = c.rootPosition()
                if p == p1: # Never try to match the same position.
                    # g.trace('failed',extend2)
                    found = False ; break
                newPrefix = c.navHelper(p,ch,extend2)
                if newPrefix:
                    found = True ; break
            if found: break
        if found:
            if all: c.frame.tree.expandAllAncestors(p)
            c.selectPosition(p)
            c.navTime = time.clock()
            c.navPrefix = newPrefix
            # g.trace('extend',extend,'extend2',extend2,'navPrefix',c.navPrefix,'p',p.headString())
        else:
            c.navTime = None
            c.navPrefix = ''
        c.treeWantsFocusNow()
    #@nonl
    #@+node:AGP.20250415230112.703:c.navQuickKey
    def navQuickKey (self):
        
        '''return true if there are two quick outline navigation keys
        in quick succession.
        
        Returns False if @float outline_nav_extend_delay setting is 0.0 or unspecified.'''
        
        c = self
       
        deltaTime = c.config.getFloat('outline_nav_extend_delay')
    
        if deltaTime in (None,0.0):
            return False
        else:
            nearTime = c.navTime and time.clock() - c.navTime < deltaTime
            return nearTime
    #@nonl
    #@-node:AGP.20250415230112.703:c.navQuickKey
    #@+node:AGP.20250415230112.704:c.navHelper
    def navHelper (self,p,ch,extend):
        
        c = self ; h = p.headString().lower()
        
        if extend:
            prefix = c.navPrefix + ch
            return h.startswith(prefix.lower()) and prefix
    
        if h.startswith(ch):
            return ch
        
        # New feature: search for first non-blank character after @x for common x.
        if ch != '@' and h.startswith('@'):
            for s in ('button','command','file','thin','asis','nosent','noref'):
                prefix = '@'+s
                if h.startswith('@'+s):
                    while 1:
                        n = len(prefix)
                        ch2 = n < len(h) and h[n] or ''
                        if ch2.isspace():
                            prefix = prefix + ch2
                        else: break
                    if len(prefix) < len(h) and h.startswith(prefix + ch.lower()):
                        return prefix + ch
        return ''
    #@nonl
    #@-node:AGP.20250415230112.704:c.navHelper
    #@-node:AGP.20250415230112.702:c.onCanvasKey
    #@-node:AGP.20250415230112.697:Selecting & Updating (commands)
    #@+node:AGP.20250415230112.705:Syntax coloring interface
    #@+at 
    #@nonl
    # These routines provide a convenient interface to the syntax colorer.
    #@-at
    #@+node:AGP.20250415230112.706:updateSyntaxColorer
    def updateSyntaxColorer(self,v):
    
        self.frame.body.updateSyntaxColorer(v)
    #@-node:AGP.20250415230112.706:updateSyntaxColorer
    #@-node:AGP.20250415230112.705:Syntax coloring interface
    #@+node:AGP.20250415230112.707:qlink()
    def qlink(self,event=None,p=None,force=False):    #agp qlink
        
        
        if not p:
            p = self.currentPosition()
        
        v = p.v
        
        if g.qlinks == None:
            g.qlinks = {}
        
        if p not in g.qlinks.keys() or force:
            if not hasattr(v,"unknownAttributes"):
                v.unknownAttributes = ua = {}
            else:
                ua	=	v.unknownAttributes
            
            ua["qlink"] = 1
            
            #add link in tree pane
            outerframe,editframe,bodyframe,treeframe,subtreeframe,logframe,qlinkframe,font = self.frame.guiframes
            
            def qlink_onclick(event):
                node = event.widget.p
                #print "qlink goto",node
                self.beginUpdate()
                if not node.isVisible():
                    for p in node.parents_iter():
                        p.expand()
                self.selectPosition(node)
                self.endUpdate()
            
            
            
            bg,fg = g.theme['bg'],g.theme['fg']
            #qlink = Tk.Label(   qlinkframe,text=v.headString(),anchor='w',relief='groove',bd=1,padx=0,pady=0,font=font,#bg='gray20',
            #                    activebackground='white',activeforeground='black'
            #)
            import tkFont
            font_height = tkFont.Font(font=font).metrics('linespace')
            height=font_height+2
            midh = height/2+1
            
            
            head = v.headString()
            headw = font.measure(head)
            
            qlink = Tk.Canvas(qlinkframe,relief='groove',bd=0,height=height,
                                highlightthickness=0,highlightbackground=bg,highlightcolor=fg,
                                bg=qlinkframe.cget('bg')#g.color_mul(0.7,qlinkframe.cget('bg'))
            
                            )
            qlink.font=font
            
            
            #qlink.create_rectangle(0,0,2000,height,fill=bg,activefill="gray60",activestipple="gray25")
            qlink.create_line(0,midh,10,midh,fill=fg)
            image=self.frame.tree.getIconImage("box%02d.png" % v.computeIcon())
            qlink.create_image(8,midh,anchor='w',image=image)
            
            
            #qtext = Tk.Text(qlink,fg=fg,bg=bg,state = 'normal',height=1,highlightthickness=0,bd=0)
            #qtext = Tk.Label(   qlink,text=head,image=image, anchor='w',relief='groove',bd=1,padx=0,pady=0,font=font,#bg='gray20',
            #                    activebackground='white',activeforeground='black'
            #)
            #qlink.create_window(35,midh,anchor="w",window=qtext)
            #qtext.delete("1.0","end")
            #qtext.insert("end",head)
            #qtext.configure(state='disabled')
            
            head = 4*' '+head+30*' '
            headw = font.measure(head)
            qlink.qtextid = qlink.create_text(headw/2,midh,text=head,font=font,fill=g.theme['fg'],activefill="white")
            
            qlink.pack(side='top',fill='x',padx=0,pady=1)
            qlink.bind('<Button-1>',qlink_onclick)
            qlink.p = p.copy()
            qlink.midh=midh
            
            g.qlinks[qlink.p] = qlink
            
            #print 'add qlink',v,ua["qlink"]
        
        else: # remove qlink
            del v.unknownAttributes['qlink']
            for k in g.qlinks.keys():
                if k == p:
                    #print 'qlink del',k
                    g.qlinks[k].destroy()
                    del g.qlinks[k]
            
    #@nonl
    #@-node:AGP.20250415230112.707:qlink()
    #@+node:AGP.20250415230112.708:qlink_scan()
    def qlink_scan(self,node=None):    #agp qlink
        
        return # agp fixme
        
        #if node == None:
        #    print "qlink scan"
        #    node = self.rootPosition()
        #root = c.rootPosition()
        
        for p in self.all_positions_iter():#node.children_iter():
            v = p.v
            if hasattr(v,"unknownAttributes"):
                if "qlink" in v.unknownAttributes:
                    #print 'qlink add attr'
                    self.qlink(p=p,force=True)
                    
            #self.qlink_scan(p)
            
        
    #@nonl
    #@-node:AGP.20250415230112.708:qlink_scan()
    #@+node:AGP.20250415230112.709:qlink_clear()
    def qlink_clear(self):    #agp qlink
        
        if g.qlinks != None:
            qlinks = g.qlinks
            for k in qlinks.keys():
                qlinks[k].destroy()
                
        g.qlinks = {}
        
    #@nonl
    #@-node:AGP.20250415230112.709:qlink_clear()
    #@-others

class Commands (baseCommands):
    """A class that implements most of Leo's commands."""
    pass
#@-node:AGP.20250415230112.331:class commands
#@+node:AGP.20250415230112.710:class configSettings
class configSettings:
    
    """A class to hold config settings for commanders."""
    
    #@    @+others
    #@+node:AGP.20250415230112.711:configSettings.__init__
    def __init__ (self,c):
        
        self.c = c
        
        self.defaultBodyFontSize = g.app.config.defaultBodyFontSize
        self.defaultLogFontSize  = g.app.config.defaultLogFontSize
        self.defaultMenuFontSize = g.app.config.defaultMenuFontSize
        self.defaultTreeFontSize = g.app.config.defaultTreeFontSize
        
        for key in g.app.config.encodingIvarsDict.keys():
            if key != '_hash':
                self.initEncoding(key)
            
        for key in g.app.config.ivarsDict.keys():
            if key != '_hash':
                self.initIvar(key)
    #@+node:AGP.20250415230112.712:initIvar
    def initIvar(self,key):
        
        c = self.c
        
        # N.B. The key is munged.
        bunch = g.app.config.ivarsDict.get(key)
        ivarName = bunch.ivar
        val = g.app.config.get(c,ivarName,kind=None) # kind is ignored anyway.
    
        if val or not hasattr(self,ivarName):
            # g.trace('c.configSettings',c.shortFileName(),ivarName,val)
            setattr(self,ivarName,val)
    #@-node:AGP.20250415230112.712:initIvar
    #@+node:AGP.20250415230112.713:initEncoding
    def initEncoding (self,key):
        
        c = self.c
        
        # N.B. The key is munged.
        bunch = g.app.config.encodingIvarsDict.get(key)
        encodingName = bunch.ivar
        encoding = g.app.config.get(c,encodingName,kind='string')
        
        # New in 4.4b3: use the global setting as a last resort.
        if encoding:
            # g.trace('c.configSettings',c.shortFileName(),encodingName,encoding)
            setattr(self,encodingName,encoding)
        else:
            encoding = getattr(g.app.config,encodingName)
            # g.trace('g.app.config',c.shortFileName(),encodingName,encoding)
            setattr(self,encodingName,encoding)
    
        if encoding and not g.isValidEncoding(encoding):
            g.es("bad %s: %s" % (encodingName,encoding))
    #@-node:AGP.20250415230112.713:initEncoding
    #@-node:AGP.20250415230112.711:configSettings.__init__
    #@+node:AGP.20250415230112.714:Getters
    def getFontFromParams(self,family,size,slant,weight,defaultSize=12):
        return g.app.config.getFontFromParams(self.c,
            family,size,slant,weight,defaultSize=defaultSize)
    
    def getRecentFiles (self):
        return g.app.config.getRecentFiles()
    
    def get(self,setting,theType):
        return g.app.config.get(self.c,setting,theType)
    
    def getAbbrevDict(self):         return g.app.config.getAbbrevDict(self.c)
    def getBool      (self,setting): return g.app.config.getBool     (self.c,setting)
    def getColor     (self,setting): return g.app.config.getColor    (self.c,setting)
    def getDirectory (self,setting): return g.app.config.getDirectory(self.c,setting)
    def getInt       (self,setting): return g.app.config.getInt      (self.c,setting)
    def getFloat     (self,setting): return g.app.config.getFloat    (self.c,setting)
    def getFontDict  (self,setting): return g.app.config.getFontDict (self.c,setting)
    def getLanguage  (self,setting): return g.app.config.getLanguage (self.c,setting)
    def getRatio     (self,setting): return g.app.config.getRatio    (self.c,setting)
    def getShortcut  (self,setting,):return g.app.config.getShortcut (self.c,setting)
    def getString    (self,setting): return g.app.config.getString   (self.c,setting)
    #@-node:AGP.20250415230112.714:Getters
    #@+node:AGP.20250415230112.715:Setters... (c.configSettings)
    #@+node:AGP.20250415230112.716:setRecentFiles (c.configSettings)
    def setRecentFiles (self,files):
        
        '''Update the recent files list.'''
    
        # Append the files to the global list.
        g.app.config.appendToRecentFiles(files)
    #@-node:AGP.20250415230112.716:setRecentFiles (c.configSettings)
    #@+node:AGP.20250415230112.717:set & setString
    def set (self,p,setting,val):
        
        return g.app.config.setString(self.c,setting,val)
        
    setString = set
    #@-node:AGP.20250415230112.717:set & setString
    #@-node:AGP.20250415230112.715:Setters... (c.configSettings)
    #@-others
#@-node:AGP.20250415230112.710:class configSettings
#@-others
#@-node:AGP.20250415230112.329:@thin leoCommands.py
#@-leo
