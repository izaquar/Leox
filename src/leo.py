#! /usr/bin/env python
# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:AGP.20250415230112.3:@thin leo.py 
#@@first
#@@first
"""Entry point for Leo in Python."""

#@@language python
#@@tabwidth -4


if __name__ == "__main__":
    
    import leo # this execute the following else statement

    try:
        leo.run(leo.fileName)
    except Exception:
        import traceback ; traceback.print_exc()


else: #build the leo module
    
    import leo          #import leo to access module as object, availlable everywhere
    
    import os
    import string
    import sys
    
    #@    @+others
    #@+node:AGP.20260302220705:Code Structure
    #@+at 
    # leo.py
    #     root_node
    #     log(),es()
    #     config
    #     ui.py
    #         body
    #         tree
    #         log
    #@-at
    #@nonl
    #@-node:AGP.20260302220705:Code Structure
    #@+node:AGP.20260225204401:Globals
    verbose = True
    loading = False
    
    logq = []       #log message queue for early log, (string,
    HooksDict = {}
        
    
    #loadDir,leoDir,homeDir,extensionsDir,configDir,testDir,user_xresources_path = None
    
    fileName = None
    fileDir = None
    
    root_vnode = None
    
    Files = []  #opened LEOFILE
    
    #@-node:AGP.20260225204401:Globals
    #@+node:AGP.20251209201647:MonkeyPatchElementTree
    import xml.etree.ElementTree as ET
    
    #@+others
    #@+node:AGP.20251209201647.1:_serialize_xml
    def _serialize_xml(write, elem, encoding, qnames, namespaces):
        tag = elem.tag
        text = elem.text
        if tag is ET.Comment:
            write("<!--%s-->" % ET._encode(text, encoding))
        elif tag is ET.ProcessingInstruction:
            write("<?%s?>" % ET._encode(text, encoding))
        else:
            tag = qnames[tag]
            if tag is None:
                if text:
                    write(ET._escape_cdata(text, encoding))
                for e in elem:
                    _serialize_xml(write, e, encoding, qnames, None)
            else:
                write("<" + tag)
                items = elem.items()
                if items or namespaces:
                    if namespaces:
                        for v, k in sorted(namespaces.items(),
                                           key=lambda x: x[1]):  # sort on prefix
                            if k:
                                k = ":" + k
                            write(" xmlns%s=\"%s\"" % (
                                k.encode(encoding),
                                ET._escape_attrib(v, encoding)
                                ))
                    #for k, v in sorted(items):  # lexical order
                    for k, v in items: # Monkey patch
                        if isinstance(k, ET.QName):
                            k = k.text
                        if isinstance(v, ET.QName):
                            v = qnames[v.text]
                        else:
                            v = ET._escape_attrib(v, encoding)
                        write(" %s=\"%s\"" % (qnames[k], v))
                if text or len(elem):
                    write(">")
                    if text:
                        write(ET._escape_cdata(text, encoding))
                    for e in elem:
                        _serialize_xml(write, e, encoding, qnames, None)
                    write("</" + tag + ">")
                else:
                    write(" />")
        if elem.tail:
            write(ET._escape_cdata(elem.tail, encoding))
    #@nonl
    #@-node:AGP.20251209201647.1:_serialize_xml
    #@+node:AGP.20251209201647.2:class OrderedXMLTreeBuilder
    class OrderedXMLTreeBuilder(ET.XMLTreeBuilder):
        
        def _start_list(self, tag, attrib_in):
            
            from collections import OrderedDict
            
            fixname = self._fixname
            tag = fixname(tag)
            attrib = OrderedDict()
            if attrib_in:
                for i in range(0, len(attrib_in), 2):
                    attrib[fixname(attrib_in[i])] = self._fixtext(attrib_in[i+1])
            return self._target.start(tag, attrib)
    #@nonl
    #@-node:AGP.20251209201647.2:class OrderedXMLTreeBuilder
    #@-others
    
    #Monkey Patch ElementTree for ordered attributes, only for python < 3.7
    ET._serialize_xml = _serialize_xml
    #@nonl
    #@-node:AGP.20251209201647:MonkeyPatchElementTree
    #@+node:AGP.20260222220434:functions
    #@+node:AGP.20251129092248:log()
    def log(s,nl=True,color="blue",do_print=True):
        
        if do_print:
            print s
        
        
        if nl:
            s += "\n"
        
        logq.append((s,color))
        
        
        
    #@nonl
    #@-node:AGP.20251129092248:log()
    #@+node:AGP.20251128195844:get_filename()
    def get_filename():
        
        if len(sys.argv) > 1:
            if sys.platform=="win32": # Windows
                fileName = string.join(sys.argv[1:],' ')
            else:
                fileName = sys.argv[1]
        else:
            fileName = None
        
        if verbose: log("Input file: "+str(fileName))
        
        # This may not be necessary
        #fileName = os.path.join(os.getcwd(),fileName)
        
        return fileName
    #@nonl
    #@-node:AGP.20251128195844:get_filename()
    #@+node:AGP.20251128194353:get_directories()
    def get_directories():
        
        
        #g.app.loadDir = 
        loadDir =  os.path.dirname(__file__)
        
        #g.app.leoDir = 
        leoDir = os.path.dirname(loadDir)
        if verbose: log("Leox directory: "+leoDir)
        #g.app.homeDir = 
        homeDir = os.path.expanduser('~')
        if verbose: log("Home directory: "+homeDir)
        
        #g.app.extensionsDir = 
        extensionsDir = leoDir+"/extensions"
        
        #g.app.globalConfigDir = 
        configDir = leoDir+"/config"
        
        #g.app.testDir = 
        testDir = leoDir+"/test"
            
        #g.app.user_xresources_path = 
        user_xresources_path = homeDir+"/.leo_xresources"
        
        return loadDir,leoDir,homeDir,extensionsDir,configDir,testDir,user_xresources_path
        
        
    #@nonl
    #@-node:AGP.20251128194353:get_directories()
    #@+node:AGP.20251130101935:train_autocomplete()
    def train_autocomplete():
        import autocomplete as ac
        
        fi = file(leoDir+"\\plugins\\xcc_nodes.py").read()
        
        ac.models.train_models(fi,None)
        
        print "training done"
        
        print ac.predict_currword('On')
        print ac.predict('= ','On')
    #@nonl
    #@-node:AGP.20251130101935:train_autocomplete()
    #@+node:AGP.20250415230112.4:run()
    def run(fileName=None,pymacs=None,*args,**keywords):
        
        g.app.gui.runMainLoop()
    #@-node:AGP.20250415230112.4:run()
    #@+node:AGP.20251205182122:do_hooks()
    def do_hooks(tag,*args,**keywords):
        hlist = HooksDict.get(tag,None)
        if hlist:
            for h in hlist:
                try:
                    res = h(keywords)
                    print "do_hooks",tag,h
                except Exception:
                    import traceback;traceback.print_exc()
                    
                    
                #if res != None:
                #    return res
    
    #@-node:AGP.20251205182122:do_hooks()
    #@+node:AGP.20251205181702:add_hook()
    def add_hook(tag,f):
        hlist = HooksDict.get(tag,[])
        hlist.append(f)
        HooksDict[tag] = hlist
    #@-node:AGP.20251205181702:add_hook()
    #@+node:AGP.20251205181702.1:remove_hook()
    def remove_hook(tag,f):
        hlist = HooksDict.get(tag,None)
        if hlist:
            if f in hlist:
                hlist.remove(f)
                HooksDict[tag] = hlist
    #@nonl
    #@-node:AGP.20251205181702.1:remove_hook()
    #@+node:AGP.20251129100123:create_window()
    def create_window():
        
        g.doHook("start1")  # Load plugins. 
        
        if app.killed: exit() # Support for g.app.forceShutdown.
        
        if app.gui == None: app.createTkGui() # Create the default gui if needed.Plugins may have create app.gui.
        
        #app.initing = False # New in 4.3: clear g.app.initing _before_ creating the frame.
                                # "idle" hooks may now call g.app.forceShutdown.
        
        # Create the main frame.   it and all queued messages.
        if fileName:
            if g.os_path_exists(fileName):
                ok, frame = g.openWithFileName(fileName,None)
                c = frame.c
                #if ok:
                #    return frame.c,frame
        else:
            print "new commander"
            # Create a _new_ frame & indicate it is the startup window.
            c,frame = g.app.newLeoCommanderAndFrame(fileName=fileName)
        
            frame.setInitialWindowGeometry()
            frame.resizePanesToRatio(frame.ratio,frame.secondary_ratio)
        
            frame.startupWindow = True
            
            g.doHook("new",old_c=None,c=c,new_c=c)  # 3/2/05: Call the 'new' hook for compatibility with plugins.
    
        # Report the failure to open the file.
        #if fileName:
        #    g.es("File not found: " + fileName)
    
        frame.show()
        
        if not frame: exit()
        
        if app.disableSave:
            g.es("disabling save commands",color=g.theme['error'])
        
        app.writeWaitingLog()
        
        p = c.currentPosition()
        g.doHook("start2",c=c,p=p,v=p,fileName=fileName)
        
        if c.config.getBool('allow_idle_time_hook'):
            g.enableIdleTimeHook()
        
        if not fileName:
            c.redraw_now()
        
        #c.bodyWantsFocus()
        frame.tree.focus_set()
    #@nonl
    #@-node:AGP.20251129100123:create_window()
    #@-node:AGP.20260222220434:functions
    #@+node:AGP.20260225192425:Commands
    #@+node:AGP.20260225192425.1:leofile_Open()
    def leofile_Open(filename):
        if not g.doHook("open1",old_c=c,c=c,new_c=c,fileName=filename):
            theFile = open(filename,'rb')
            c.fileCommands.open(theFile,filename,readAtFileNodesFlag=True)#close theFile
            
            
        leo.fileDir = c.frame.openDirectory = g.os_path_abspath(g.os_path_dirname(filename))
        g.doHook("open2",old_c=c,c=c,new_c=c.frame.c,fileName=filename)
            
        c.frame.body.colorizer.scan_tree()
        c.frame.body.colorizer.colorize(c.currentPosition())
    #@nonl
    #@-node:AGP.20260225192425.1:leofile_Open()
    #@+node:AGP.20260403085814:leofile_New()
    def New_File():
        pass
    #@nonl
    #@-node:AGP.20260403085814:leofile_New()
    #@+node:AGP.20260403091711:leofile_Close()
    #@-node:AGP.20260403091711:leofile_Close()
    #@+node:AGP.20260403085814.1:New_Window()
    #@-node:AGP.20260403085814.1:New_Window()
    #@+node:AGP.20260403091711.1:Close_Window()
    #@-node:AGP.20260403091711.1:Close_Window()
    #@+node:AGP.20260403085814.2:OpenInNewWindoow()
    #@-node:AGP.20260403085814.2:OpenInNewWindoow()
    #@-node:AGP.20260225192425:Commands
    #@+node:AGP.20251209190042:class LEOFILE
    class LEOFILE:
        #@    @+others
        #@+node:AGP.20260309221039:__init__()
        def __init__(self):
            
            
            self.filename = None    #file path and name
            
            self.root_vnode = None
            self.current_vnode = None
            
            self.changed = False
            
            
        #@nonl
        #@-node:AGP.20260309221039:__init__()
        #@+node:AGP.20251209170331:load()
        def load(self,filename):
            import xml.etree.ElementTree as ET
            import leo
            #from core import NDATA,log#,InsertChildNode
            leo.loading = True
            
            tree = ET.parse(filename,OrderedXMLTreeBuilder())
            
            log("loading "+filename)
            
            root = tree.getroot()
            
            globals_elmt = self.globals_elmt = root.find('globals')
            
            """
            if globals_elmt != None:
                #FileGlobals.update(globals_elmt.items())
                #print FileGlobals
                
                #for c in list(globals_elmt):
                #    FileGlobals[c.tag] = dict(c.items())
                    
                pos = globals_elmt.find('global_window_position')
                if ui and pos is not None:
                    attr = pos.attrib
                    pos = ( int(attr.get('left')),
                            int(attr.get('top')),
                            int(attr.get('width')),
                            int(attr.get('height')) )
                    
                    #print pos
                    print 'set pos',pos
                    ui.Position(pos)
            """
            
            tnodes = self.tnodes = {}
            
            tnodes_elmt = root.find('tnodes')
            for tnode in tnodes_elmt:
                #create tnode and set bodyString
                ndata = tnodes[tnode.attrib['tx']] = leoNodes.tnode(tnode.text)#(tnode.text,tnode.attrib.copy(),[])
                
            
            #@    @+others
            #@+node:AGP.20251209170331.1:load_vnode()
            def load_vnode(elmt):
                
                attribs = elmt.attrib.copy()
                #print attribs
                t = self.tnodes[attribs.pop('t')]
                
                
                v = leoNodes.vnode(t)
                
                if v not in t.vnodeList:        #why not done in vnode contructor?
                    t.vnodeList.append(v)
                
                #@    @+others
                #@+node:AGP.20251209200730:get status bits
                #clonedBit   = 0x01 # True: vnode has clone mark.
                # not used = 0x02
                #expandedBit = 0x04 # True: vnode is expanded.
                #markedBit   = 0x08 # True: vnode is marked
                #orphanBit   = 0x10 # True: vnode saved in .leo file, not derived file.
                #selectedBit = 0x20 # True: vnode is current vnode.
                #topBit      = 0x40 # True: vnode was top vnode when saved.
                    
                a = attribs.pop('a',None)
                if a:
                    if 'E' in a:#Expanded
                        v.statusBits |= 0x10
                            
                    if 'M' in a:#Marked
                        v.statusBits |= 0x02
                        
                    if 'O' in a:#Orphane
                        v.statusBits |= 0x10
                        
                    if 'T' in a:#Top
                        v.statusBits |= 0x40
                        
                    if 'V' in a:#current
                        #print 'selected',v
                        v.statusBits |= 0x20
                        self.selected_vnode = v
                #@-node:AGP.20251209200730:get status bits
                #@-others
                
                mod = attribs.pop('mod',None)
                if mod:
                    v.mod = mod
                
                attribs.pop('tnodeList',None)   #used for?
                
                prev_child = None
                for child_elmt in elmt:
                    if child_elmt.tag == "v":
                        vchild = load_vnode(child_elmt)
                        if prev_child:
                            vchild.linkAfter(prev_child)
                        else:
                            vchild.linkAsNthChild(v,0)
                        
                        prev_child = vchild
                        
                    if child_elmt.tag == "vh":
                        #print child_elmt.text
                        v.initHeadString(child_elmt.text)
                
                #whats left are unknown attributes
                if len(attribs):
                    #print attribs
                    v.unknownAttributes = attribs
                
                return v
                
            #@nonl
            #@-node:AGP.20251209170331.1:load_vnode()
            #@-others
            
            #import vnodes
            vnodes_elmt = root.find('vnodes')
            
            root_vnode = self.root_vnode = None
            prev_vnode = None
            for vnode_elmt in vnodes_elmt:
                
                v = load_vnode(vnode_elmt)
                
                if not prev_vnode:
                    root_vnode = self.root_vnode = v
                else:
                    v.linkAfter(prev_vnode)
                    
                prev_vnode = v
            
            leo.loading = False
        
            return root_vnode
        #@-node:AGP.20251209170331:load()
        #@+node:AGP.20260225185708:save()
        def save(filename,root = None):
            
            from xml.etree.ElementTree import Element,SubElement
            #from core import log
            
            log("saving "+filename)
            
            vtail = ["\n"]
            
            leofile = Element('leo_file')
            leofile.text = "\n"
            
            se = SubElement(leofile,'leo_header',{'file_format':"2",'tnodes':"0",'max_tnode_index':"0", 'clone_windows':"0"})
            se.tail = "\n"
            
            ge = SubElement(leofile,'globals',{"body_outline_ratio":"0.382"})
            ge.tail = "\n"
            
            se = SubElement(ge,'global_window_position',{"top":"68","left":"374","height":"709","width":"1162"})
            se.tail = "\n\t"
            
            se = SubElement(ge,'global_log_window_position',{"top":"0","left":"0","height":"0","width":"0"})
            se.tail = "\n"
            
            vnodes = SubElement(leofile,'vnodes')
            vnodes.text = "\n"
            vnodes.tail = "\n"
            
            tnodes = SubElement(leofile,'tnodes')
            tnodes.text = "\n"
            tnodes.tail = "\n"
            
            tnodes_ids = []
            parents = [vnodes]
            
            #@    @+others
            #@+node:AGP.20260225185708.1:node_start()
            def node_start(node):
                
                
                if node.handler:
                    handler = Handlers.get(node.handler)
                    if handler:
                        handler.save(node)
                
                
                attribs = node.attribs
                
                if not attribs:
                    attribs = {}
                        
                a = ""
                    
                if node.expanded():
                    a += "E"
                if node.marked():
                    a += "M"
                if ui and node == ui.Tree.selected_node:
                    a += "V"
                if a != "":
                    attribs['a']=a
                
                
                
                newparent = SubElement(parents[-1],'v',attribs)
                    
                newparent.tail = "\n"#"".join(vtail)
                
                #push if parent
                if node.child:
                    #newparent.text = "".join(vtail)
                    vtail.append("\t")
                    parents.append(newparent)
                    
                #update tnodes
                vh = SubElement(newparent,'vh')
                vh.text = node.title
                if node.child:
                    vh.tail = "\n"#"".join(vtail)
                        
                tx = node.attribs.get('t')
                newparent.attrib["t"] = tx
                    
                if tx not in tnodes_ids:
                            
                    tnodes_ids.append(tx)            
                    attribs = node.attribs
                    #print tx
                    newtnode = SubElement(tnodes,'t',{'tx':tx})#,'mod':node.mod
                            
                    newtnode.text = node.content
                    newtnode.tail = "\n"
                            
            #@-node:AGP.20260225185708.1:node_start()
            #@+node:AGP.20260225185708.2:node_end()
            def node_end(node):
                
                #pop if parent
                if node.child :
                    #vtail.pop(-1)
                    parents.pop(-1)
                        
                if not node.next:# and len(vtail):
                    vtail.pop(-1)
            #@nonl
            #@-node:AGP.20260225185708.2:node_end()
            #@-others
            
            
                
            
            
            #ParseTree(node_start,node_end)
            for node in Root.children():
                res = node.parse(start,end)        
                if res != None:
                    return res
                
            return None
            
            tree = ET.ElementTree(leofile)
            #tree.write("filename.xml")
            tree.write(filename+"_save",'utf-8',True)
            
        
        #@-node:AGP.20260225185708:save()
        #@-others
    #@nonl
    #@-node:AGP.20251209190042:class LEOFILE
    #@+node:AGP.20260221183613:class LEOAPP
    class LEOAPP:
    
        """A class representing the Leo application itself.
        
        Ivars of this class are Leo's global variables."""
        
        #@    @+others
        #@+node:AGP.20250415230112.15:__init__()
        def __init__(self):
        
            # These ivars are the global vars of this program.
            self.afterHandler = None
            self.batchMode = False # True: run in batch mode.
            self.commandName = None # The name of the command being executed.
            self.config = None # The leoConfig instance.
            self.count = 0 # General purpose debugging count.
            self.debug = False # True: enable extra debugging tests (not used at present).
                # WARNING: this could greatly slow things down.
            self.debugSwitch = 0
                # 0: default behavior
                # 1: full traces in g.es_exception.
                # 2: call pdb.set_trace in g.es_exception, etc.
            self.disableSave = False
            self.globalConfigDir = None # The directory that is assumed to contain the global configuration files.
            self.globalOpenDir = None # The directory last used to open a file.
            self.gui = None # The gui class.
            #self.hasOpenWithMenu = False # True: open with plugin has been loaded.
            self.hookError = False # True: suppress further calls to hooks.
            self.hookFunction = None # Application wide hook function.
            self.homeDir = None # The user's home directory.
            self.idle_imported = False # True: we have done an import idle
            self.idleTimeDelay = 100 # Delay in msec between calls to "idle time" hook.
            self.idleTimeHook = False # True: the global idleTimeHookHandler will reshedule itself.
            #self.initing = True # True: we are initiing the app.
            self.killed = False # True: we are about to destroy the root window.
            self.leoID = None # The id part of gnx's.
            self.loadDir = None # The directory from which Leo was loaded.
            self.loadedPlugins = [] # List of loaded plugins that have signed on.
            self.log = None # The LeoFrame containing the present log.
            self.logIsLocked = False # True: no changes to log are allowed.
            self.logWaiting = [] # List of messages waiting to go to a log.
            self.menuWarningsGiven = False # True: supress warnings in menu code.
            self.nodeIndices = None # Singleton node indices instance.
            self.numberOfWindows = 0 # Number of opened windows.
            #self.openWithFiles = [] # List of data used by Open With command.
            #self.openWithFileNum = 0 # Used to generate temp file names for Open With command.
            #self.openWithTable = None # The table passed to createOpenWithMenuFromTable.
            self.positions = 0 # Count of the number of positions generated.
            self.quitting = False # True if quitting.  Locks out some events.
            self.realMenuNameDict = {} # Contains translations of menu names and menu item names.
            self.root = None # The hidden main window. Set later.
            self.searchDict = {} # For communication between find/change scripts.
            self.scanErrors = 0 # The number of errors seen by g.scanError.
            self.scriptDict = {} # For communication between Execute Script command and scripts.
            self.statsDict = {} # Statistics dict used by g.stat, g.clear_stats, g.print_stats.
            self.trace = False # True: enable debugging traces.
            self.trace_gc = False # defined in run()
            self.trace_gc_calls = False # defined in run()
            self.trace_gc_verbose = False # defined in run()
            self.trace_gc_inited = False
            self.tracePositions = False
            self.trace_list = [] # "Sherlock" argument list for tracing().
            self.tkEncoding = "utf-8"
            self.unicodeErrorGiven = True # True: suppres unicode tracebacks.
            self.unitTestDict = {} # For communication between unit tests and code.
            self.unitTesting = False # True if unit testing.
            self.user_xresources_path = None # Resource file for Tk/tcl.
            self.windowList = [] # Global list of all frames.  Does not include hidden root window.
        
            # Global panels.  Destroyed when Leo ends.
            self.pythonFrame = None
            
            #@    << Define global constants >>
            #@+node:AGP.20250415230112.16:<< define global constants >>
            self.prolog_string = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
            
            # New in leo.py 3.0
            self.prolog_prefix_string = "<?xml version=\"1.0\" encoding="
            self.prolog_postfix_string = "?>"
            
            # leo.py 3.11
            self.use_unicode = True # True: use new unicode logic.
            #@-node:AGP.20250415230112.16:<< define global constants >>
            #@nl
            #@    << Define global data structures >>
            #@+node:AGP.20250415230112.17:<< define global data structures >> app
            # Internally, lower case is used for all language names.
            self.language_delims_dict = {
                "ada" : "--",
                "actionscript" : "// /* */", #jason 2003-07-03
                "c" : "// /* */", # C, C++ or objective C.
                "csharp" : "// /* */", # C#
                "cpp" : "// /* */",# C++.
                "css" : "/* */", # 4/1/04
                "cweb" : "@q@ @>", # Use the "cweb hack"
                "elisp" : ";",
                "forth" : "\\_ _(_ _)", # Use the "REM hack"
                "fortran" : "C",
                "fortran90" : "!",
                "html" : "<!-- -->",
                "java" : "// /* */",
                "latex" : "%",
                "lua" : "--",  # ddm 13/02/06
                "pascal" : "// { }",
                "perl" : "#",
                "perlpod" : "# __=pod__ __=cut__", # 9/25/02: The perlpod hack.
                "php" : "//",
                "plain" : "#", # We must pick something.
                "plsql" : "-- /* */", # SQL scripts qt02537 2005-05-27
                "python" : "#",
                "rapidq" : "'", # fil 2004-march-11
                "rebol" : ";",  # jason 2003-07-03
                "shell" : "#",  # shell scripts
                "tcltk" : "#",
                "unknown" : "#" } # Set when @comment is seen.
            
            self.language_extension_dict = {
                "ada" : "ads",
                "actionscript" : "as", #jason 2003-07-03
                "c" : "c",
                "cpp" : "cpp",
                "css" : "css", # 4/1/04
                "cweb" : "w",
                "elisp" : "el",
                "forth" : "forth",
                "fortran" : "f",
                "fortran90" : "f",
                "html" : "html",
                "java" : "java",
                "latex" : "tex", # 1/8/04
                "lua" : "lua",  # ddm 13/02/06
                "noweb" : "nw",
                "pascal" : "p",
                # "perl" : "perl",
                # "perlpod" : "perl",
                "perl" : "pl",      # 11/7/05
                "perlpod" : "pod",  # 11/7/05
                "php" : "php",
                "plain" : "txt",
                "python" : "py",
                "plsql" : "sql", # qt02537 2005-05-27
                "rapidq" : "bas", # fil 2004-march-11
                "rebol" : "r",    # jason 2003-07-03
                "shell" : "sh",   # DS 4/1/04
                "tex" : "tex",
                "tcltk" : "tcl",
                "unknown" : "txt" } # Set when @comment is seen.
                
            self.extension_dict = {
                "ads"   : "ada",
                "adb"   : "ada",
                "as"    : "actionscript",
                "bas"   : "rapidq",
                "c"     : "c",
                "cpp"   : "cpp",
                "css"   : "css",
                "el"    : "elisp",
                "forth" : "forth",
                "f"     : "fortran90", # or fortran ?
                "html"  : "html",
                "java"  : "java",
                "lua" : "lua",  # ddm 13/02/06
                "noweb" : "nw",
                "p"     : "pascal",
                # "perl"  : "perl",
                "pl"    : "perl",   # 11/7/05
                "pod"   : "perlpod", # 11/7/05
                "php"   : "php",
                "py"    : "python",
                "sql"   : "plsql", # qt02537 2005-05-27
                "r"     : "rebol",
                "sh"    : "shell",
                "tex"   : "tex",
                "txt"   : "plain",
                "tcl"   : "tcltk",
                "w"     : "cweb" }
            #@-node:AGP.20250415230112.17:<< define global data structures >> app
            #@nl
            
            #@    @+others
            #@+node:AGP.20260222155555:old module level init
            
            g.app = self
            
            self.loadDir = leo.loadDir
            self.leoDir = leo.leoDir
            self.homeDir = leo.homeDir
            self.extensionsDir = leo.extensionsDir
            self.globalConfigDir = leo.configDir
            self.testDir = leo.testDir
            self.user_xresources_path = leo.user_xresources_path
            
            self.setLeoID(verbose= leo.verbose) # Force the user to set g.app.leoID.
            
            self.nodeIndices = leoNodes.nodeIndices(self.leoID)
            
            
            #Create config and read settings
            #leo.config = g.config = self.config = leoConfig.configClass()
            
            #self.config.readSettingsFiles(leo.configDir+"\\leoSettings.leo",leo.verbose)    #
            
            
            #self.setEncoding()
            #@nonl
            #@-node:AGP.20260222155555:old module level init
            #@-others
            
        #@-node:AGP.20250415230112.15:__init__()
        #@+node:AGP.20250415230112.18:closeLeoWindow
        def closeLeoWindow (self,frame):
            
            """Attempt to close a Leo window.
            
            Return False if the user veto's the close."""
            
            c = frame.c
            
            if c.promptingForClose:
                # There is already a dialog open asking what to do.
                return False
                
            g.app.config.writeRecentFilesFile(c) # Make sure .leoRecentFiles.txt is written.
        
            if c.changed:
                c.promptingForClose = True
                veto = frame.promptForSave()
                c.promptingForClose = False
                if veto: return False
        
            g.app.setLog(None) # no log until we reactive a window.
            
            g.doHook("close-frame",c=c) # This may remove frame from the window list.
            
            if frame in g.app.windowList:
                g.app.destroyWindow(frame)
            
            if g.app.windowList:
                # Pick a window to activate so we can set the log.
                w = g.app.windowList[0]
                w.deiconify()
                w.lift()
                w.c.setLog()
                w.c.bodyWantsFocusNow()
            else:
                g.app.finishQuit()
        
            return True # The window has been closed.
        #@-node:AGP.20250415230112.18:closeLeoWindow
        #@+node:AGP.20250415230112.19:createTkGui
        def createTkGui (self,fileName=None):
            
            # Do NOT omit fileName param: it is used in plugin code.
            
            """A convenience routines for plugins to create the default Tk gui class."""
            
            import leoGui # Do this import after app module is fully imported.
        
            leo.ui = g.app.gui = leoGui.leoUi()
            
            g.app.root = root = g.app.gui.createRootWindow()
            
            try:
                g.gen_theme()
            except:
                import traceback
                traceback.print_exc()
            
            g.app.gui.finishCreate()
            
            # agp color theme
            # agp option
            
        #@-node:AGP.20250415230112.19:createTkGui
        #@+node:AGP.20250415230112.20:destroyAllOpenWithFiles
        def destroyAllOpenWithFiles (self):
        
            """Try to remove temp files created with the Open With command.
            
            This may fail if the files are still open."""
            
            # We can't use g.es here because the log stream no longer exists.
        
            for theDict in self.openWithFiles[:]: # 7/10/03.
                g.app.destroyOpenWithFileWithDict(theDict)
                
            # Delete the list so the gc can recycle Leo windows!
            g.app.openWithFiles = []
        #@-node:AGP.20250415230112.20:destroyAllOpenWithFiles
        #@+node:AGP.20250415230112.21:destroyOpenWithFilesForFrame
        def destroyOpenWithFilesForFrame (self,frame):
            
            """Close all "Open With" files associated with frame"""
            
            # Make a copy of the list: it may change in the loop.
            openWithFiles = g.app.openWithFiles
        
            for theDict in openWithFiles[:]: # 6/30/03
                c = theDict.get("c")
                if c.frame == frame:
                    g.app.destroyOpenWithFileWithDict(theDict)
        #@-node:AGP.20250415230112.21:destroyOpenWithFilesForFrame
        #@+node:AGP.20250415230112.22:destroyOpenWithFileWithDict
        def destroyOpenWithFileWithDict (self,theDict):
            
            path = theDict.get("path")
            if path and g.os_path_exists(path):
                try:
                    os.remove(path)
                    print "deleting temp file:", g.shortFileName(path)
                except:
                    print "can not delete temp file:", path
                    
            # Remove theDict from the list so the gc can recycle the Leo window!
            g.app.openWithFiles.remove(theDict)
        #@-node:AGP.20250415230112.22:destroyOpenWithFileWithDict
        #@+node:AGP.20250415230112.23:destroyWindow
        def destroyWindow (self,frame):
            
            # g.trace(frame in g.app.windowList,frame)
                
            #g.app.destroyOpenWithFilesForFrame(frame)
        
            if frame in g.app.windowList:
                g.app.windowList.remove(frame)
                # g.trace(g.app.windowList)
        
            # force the window to go away now.
            # Important: this also destroys all the objects of the commander.
            frame.destroySelf()
        #@-node:AGP.20250415230112.23:destroyWindow
        #@+node:AGP.20250415230112.24:finishQuit
        def finishQuit(self):
            
            # forceShutdown may already have fired the "end1" hook.
            if not g.app.killed:
                g.doHook("end1")
        
            #self.destroyAllOpenWithFiles()
            
            if g.app.gui:
                g.app.gui.destroySelf()
                
            g.app.killed = True
                # Disable all further hooks and events.
                # Alas, "idle" events can still be called even after the following code.
        
            if 0: # Do not use g.trace here!
                print "finishQuit",g.app.killed
                
            if g.app.afterHandler:
                # TK bug: This appears to have no effect, at least on Windows.
                # print "finishQuit: cancelling",g.app.afterHandler
                if g.app.gui and g.app.gui.guiName() == "tkinter":
                    self.root.after_cancel(g.app.afterHandler)
                g.app.afterHandler = None
        #@-node:AGP.20250415230112.24:finishQuit
        #@+node:AGP.20250415230112.25:forceShutdown
        def forceShutdown (self):
            
            """Forces an immediate shutdown of Leo at any time.
            
            In particular, may be called from plugins during startup."""
            
            # Wait until everything is quiet before really quitting.
            g.doHook("end1")
            
            self.log = None # Disable writeWaitingLog
            self.killed = True # Disable all further hooks.
            
            for w in self.windowList[:]:
                self.destroyWindow(w)
        
            self.finishQuit()
        #@-node:AGP.20250415230112.25:forceShutdown
        #@+node:AGP.20250415230112.26:onQuit
        def onQuit (self,event=None):
            
            '''Exit Leo, prompting to save unsaved outlines first.'''
            
            g.app.quitting = True
            
            while g.app.windowList:
                w = g.app.windowList[0]
                if not g.app.closeLeoWindow(w):
                    break
        
            if g.app.windowList:
                g.app.quitting = False # If we get here the quit has been disabled.
        #@-node:AGP.20250415230112.26:onQuit
        #@+node:AGP.20250415230112.27:setEncoding
        #@+at 
        #@nonl
        # According to Martin v. Löwis, getdefaultlocale() is broken, and 
        # cannot be fixed. The workaround is to copy the 
        # g.getpreferredencoding() function from locale.py in Python 2.3a2.  
        # This function is now in leoGlobals.py.
        #@-at
        #@@c
        
        def setEncoding (self):
            
            """Set g.app.tkEncoding."""
            import locale
            locale_encoding = locale.getpreferredencoding()
            
            sys_encoding = sys.getdefaultencoding()
        
            for (encoding,src) in (
                (self.config.tkEncoding,"config"),
                (locale_encoding,"locale"),
                (sys_encoding,"sys"),
                ("utf-8","default")):
            
                if g.isValidEncoding (encoding):
                    self.tkEncoding = encoding
                    # g.trace(self.tkEncoding,src)
                    break
                elif encoding:
                    color = "red" if self.tkEncoding=="ascii" else "blue"
                    g.trace("ignoring invalid %s encoding: %s" % (src,encoding),color=color)
        #@-node:AGP.20250415230112.27:setEncoding
        #@+node:AGP.20250415230112.28:setLeoID
        def setLeoID (self,verbose=True):
        
            tag = ".leoID.txt"
            homeDir = g.app.homeDir
            globalConfigDir = g.app.globalConfigDir
            loadDir = g.app.loadDir
            
            verbose = not g.app.unitTesting
            #
            #@nonl
            #@<< return if we can set leoID from sys.leoID >>
            #@+node:AGP.20250415230112.29:<< return if we can set leoID from sys.leoID>>
            # This would be set by in Python's sitecustomize.py file.
            
            nonConstantAttr = "leoID"
            
            if hasattr(sys,nonConstantAttr):
                g.app.leoID = getattr(sys,nonConstantAttr)
                if verbose: g.es_print("leoID = " + g.app.leoID, color='red')
                return
            else:
                g.app.leoID = None
            #@-node:AGP.20250415230112.29:<< return if we can set leoID from sys.leoID>>
            #@nl
            #@    << return if we can set leoID from "leoID.txt" >>
            #@+node:AGP.20250415230112.30:<< return if we can set leoID from "leoID.txt" >>
            for theDir in (homeDir,globalConfigDir,loadDir):
                # N.B. We would use the _working_ directory if theDir is None!
                if theDir:
                    try:
                        fn = g.os_path_join(theDir,tag)
                        f = open(fn,'r')
                        s = f.readline()
                        f.close()
                        if s and len(s) > 0:
                            g.app.leoID = s.strip()
                            if verbose:
                                g.es_print("leoID = %s (in %s)" % (g.app.leoID,theDir), color="red")
                            return
                        elif verbose:
                            g.es_print("empty %s (in %s)" % (tag,theDir), color = "red")
                    except IOError:
                        g.app.leoID = None
                        # g.es("%s not found in %s" % (tag,theDir),color="red")
                    except Exception:
                        g.app.leoID = None
                        g.es_print('Unexpected exception in app.setLeoID',color='red')
                        g.es_exception()
            #@-node:AGP.20250415230112.30:<< return if we can set leoID from "leoID.txt" >>
            #@nl
            #
            #@nonl
            #@<< return if we can set leoID from os.getenv('USER') >>
            #@+node:AGP.20250415230112.31:<< return if we can set leoID from os.getenv('USER') >>
            try:
                theId = os.getenv('USER')
                if theId:
                    if verbose: g.es_print("using os.getenv('USER'): %s " % (repr(theId)),color='red')
                    g.app.leoID = theId
                    return
                    
            except Exception:
                pass
            #@-node:AGP.20250415230112.31:<< return if we can set leoID from os.getenv('USER') >>
            #@nl
            #@    << put up a dialog requiring a valid id >>
            #@+node:AGP.20250415230112.32:<< put up a dialog requiring a valid id >>
            # New in 4.1: get an id for gnx's.  Plugins may set g.app.leoID.
            
            # Create an emergency gui and a Tk root window.
            g.app.createTkGui("startup")
            
            # Bug fix: 2/6/05: put result in g.app.leoID.
            g.app.leoID = g.app.gui.runAskLeoIDDialog()
            
            # g.trace(g.app.leoID)
            g.es_print("leoID = %s" % (repr(g.app.leoID)),color="blue")
            #@-node:AGP.20250415230112.32:<< put up a dialog requiring a valid id >>
            #@nl
            #@    << attempt to create leoID.txt >>
            #@+node:AGP.20250415230112.33:<< attempt to create leoID.txt >>
            for theDir in (homeDir,globalConfigDir,loadDir):
                # N.B. We would use the _working_ directory if theDir is None!
                if theDir:
                    cant = "can not create %s in %s" % (tag,theDir)
                    try:
                        fn = g.os_path_join(theDir,tag)
                        f = open(fn,'w')
                        f.write(g.app.leoID)
                        f.close()
                        if g.os_path_exists(fn):
                            s = "%s created in %s" % (tag,theDir)
                            g.es_print(s, color="red")
                            return
                        else:
                            g.es(cant,color='red')
                    except IOError:
                        g.es(cant,color='red')
            #@-node:AGP.20250415230112.33:<< attempt to create leoID.txt >>
            #@nl
        #@-node:AGP.20250415230112.28:setLeoID
        #@+node:AGP.20250415230112.34:askLeoID
        def askLeoID (self,verbose=True):
        
            tag = ".leoID.txt"
            homeDir = g.app.homeDir
            globalConfigDir = g.app.globalConfigDir
            loadDir = g.app.loadDir
            
            verbose = not g.app.unitTesting
            #@    << put up a dialog requiring a valid id >>
            #@+node:AGP.20250415230112.35:<< put up a dialog requiring a valid id >>
            # New in 4.1: get an id for gnx's.  Plugins may set g.app.leoID.
            
            
            # Bug fix: 2/6/05: put result in g.app.leoID.
            id = g.app.gui.runAskLeoIDDialog()
            print id
            return
            if id == "":
                g.es("failed to get a valid id!",color="red")
                return
            else:
                g.app.leoID = id
            
            # g.trace(g.app.leoID)
            g.es_print("leoID = %s" % (repr(g.app.leoID)),color="blue")
            #@-node:AGP.20250415230112.35:<< put up a dialog requiring a valid id >>
            #@nl
            #@    << attempt to create leoID.txt >>
            #@+node:AGP.20250415230112.36:<< attempt to create leoID.txt >>
            for theDir in (homeDir,globalConfigDir,loadDir):
                # N.B. We would use the _working_ directory if theDir is None!
                if theDir:
                    cant = "can not create %s in %s" % (tag,theDir)
                    try:
                        fn = g.os_path_join(theDir,tag)
                        f = open(fn,'w')
                        f.write(g.app.leoID)
                        f.close()
                        if g.os_path_exists(fn):
                            s = "%s created in %s" % (tag,theDir)
                            g.es_print(s, color="red")
                            return
                        else:
                            g.es(cant,color='red')
                    except IOError:
                        g.es(cant,color='red')
            #@-node:AGP.20250415230112.36:<< attempt to create leoID.txt >>
            #@nl
        #@-node:AGP.20250415230112.34:askLeoID
        #@+node:AGP.20250415230112.37:setLog, lockLog, unlocklog
        def setLog (self,log):
        
            """set the frame to which log messages will go"""
            
            # print "setLog:",tag,"locked:",self.logIsLocked,log
            if not self.logIsLocked:
                self.log = log
        
        def lockLog(self):
            """Disable changes to the log"""
            self.logIsLocked = True
            
        def unlockLog(self):
            """Enable changes to the log"""
            self.logIsLocked = False
        #@-node:AGP.20250415230112.37:setLog, lockLog, unlocklog
        #@+node:AGP.20250415230112.38:writeWaitingLog
        def writeWaitingLog (self):
        
            # g.trace(g.app.gui,self.log)
        
            if self.log:
                if 1: ## not self.log.isNull: # The test for isNull would probably interfere with batch mode.
                    for s,color in self.logWaiting:
                        g.es(s,color=color,newline=0) # The caller must write the newlines.
                    self.logWaiting = []
            else:
                print 'writeWaitingLog: still no log!'
        #@-node:AGP.20250415230112.38:writeWaitingLog
        #@+node:AGP.20250415230112.39:newLeoCommanderAndFrame
        def newLeoCommanderAndFrame(self,fileName,updateRecentFiles=True):
            
            """Create a commander and its view frame for the Leo main window."""
            
            app = self
            
            import leoCommands
            
            if not fileName: fileName = ""
            #@    << compute the window title >>
            #@+node:AGP.20250415230112.40:<< compute the window title >>
            # Set the window title and fileName
            if fileName:
                title = g.computeWindowTitle(fileName)
            else:
                s = "untitled"
                n = g.app.numberOfWindows
                if n > 0:
                    s += str(n)
                title = g.computeWindowTitle(s)
                g.app.numberOfWindows = n+1
            #@-node:AGP.20250415230112.40:<< compute the window title >>
            #@nl
        
            # Create an unfinished frame to pass to the commanders.
            frame = app.gui.createLeoFrame(title)
            
            # Create the commander and its subcommanders.
            c = leoCommands.Commands(frame,fileName)#
            
            #if not app.initing:
            g.doHook("before-create-leo-frame",c=c) # Was 'onCreate': too confusing.
                
            frame.finishCreate(c)
            
            c.finishCreate(frame)   #Commands <- require (ui)
            
            # Create the menu last so that we can use the key handler for shortcuts.
            p = c.currentPosition()
            if not g.doHook("menu1",c=c,p=p,v=p):
                frame.menu.createMenuBar(c.frame)   #Menus <- require (shortcut,command)
            
            
            # Finish initing the subcommanders.
            c.undoer.clearUndoState() # Menus must exist at this point.
            
            if updateRecentFiles:
                c.updateRecentFiles(fileName)
            
            
            #if not g.app.initing:
            g.doHook("after-create-leo-frame",c=c)
            
        
            return c,frame
        #@-node:AGP.20250415230112.39:newLeoCommanderAndFrame
        #@-others
    #@nonl
    #@-node:AGP.20260221183613:class LEOAPP
    #@+node:AGP.20260222223302:class CONFIG
    class CONFIG:
        """A class to manage configuration settings."""
        #@    << class data >>
        #@+node:AGP.20260222223302.1:<<  class data >>
        #@+others
        #@+node:AGP.20260222223302.2:defaultsDict
        #@+at 
        #@nonl
        # This contains only the "interesting" defaults.
        # Ints and bools default to 0, floats to 0.0 and strings to "".
        #@-at
        #@@c
        
        defaultBodyFontSize = 9 if sys.platform=="win32" else 12
        defaultLogFontSize  = 8 if sys.platform=="win32" else 12
        defaultMenuFontSize = 9 if sys.platform=="win32" else 12
        defaultTreeFontSize = 9 if sys.platform=="win32" else 12
        
        defaultsDict = {'_hash':'defaultsDict'}
        
        defaultsData = (
            # compare options...
            ("ignore_blank_lines","bool",True),
            ("limit_count","int",9),
            ("print_mismatching_lines","bool",True),
            ("print_trailing_lines","bool",True),
            # find/change options...
            ("search_body","bool",True),
            ("whole_word","bool",True),
            # Prefs panel.
            ("default_target_language","language","python"),
            ("target_language","language","python"), # Bug fix: 6/20,2005.
            ("tab_width","int",-4),
            ("page_width","int",132),
            ("output_doc_chunks","bool",True),
            ("tangle_outputs_header","bool",True),
            # Syntax coloring options...
            # Defaults for colors are handled by leoColor.py.
            ("color_directives_in_plain_text","bool",True),
            ("underline_undefined_section_names","bool",True),
            # Window options...
            ("allow_clone_drags","bool",True),
            ("body_pane_wraps","bool",True),
            ("body_text_font_family","family","Courier"),
            ("body_text_font_size","size",defaultBodyFontSize),
            ("body_text_font_slant","slant","roman"),
            ("body_text_font_weight","weight","normal"),
            ("enable_drag_messages","bool",True),
            ("headline_text_font_family","string",None),
            ("headline_text_font_size","size",defaultLogFontSize),
            ("headline_text_font_slant","slant","roman"),
            ("headline_text_font_weight","weight","normal"),
            ("log_text_font_family","string",None),
            ("log_text_font_size","size",defaultLogFontSize),
            ("log_text_font_slant","slant","roman"),
            ("log_text_font_weight","weight","normal"),
            ("initial_window_height","int",600),
            ("initial_window_width","int",800),
            ("initial_window_left","int",10),
            ("initial_window_top","int",10),
            ("initial_splitter_orientation","string","vertical"),
            ("initial_vertical_ratio","ratio",0.5),
            ("initial_horizontal_ratio","ratio",0.3),
            ("initial_horizontal_secondary_ratio","ratio",0.5),
            ("initial_vertical_secondary_ratio","ratio",0.7),
            ("outline_pane_scrolls_horizontally","bool",False),
            ("split_bar_color","color","LightSteelBlue2"),
            ("split_bar_relief","relief","groove"),
            ("split_bar_width","int",7),
        )
        #@-node:AGP.20260222223302.2:defaultsDict
        #@+node:AGP.20260222223302.3:define encodingIvarsDict
        encodingIvarsDict = {'_hash':'encodingIvarsDict'}
        
        encodingIvarsData = (
            ("default_derived_file_encoding","string","utf-8"),
            ("new_leo_file_encoding","string","UTF-8"),
                # Upper case for compatibility with previous versions.
            ("tkEncoding","string",None),
                # Defaults to None so it doesn't override better defaults.
        )
        #@-node:AGP.20260222223302.3:define encodingIvarsDict
        #@+node:AGP.20260222223302.4:ivarsDict
        # Each of these settings sets the corresponding ivar.
        # Also, the c.configSettings settings class inits the corresponding commander ivar.
        ivarsDict = {'_hash':'ivarsDict'}
        
        ivarsData = (
            ("at_root_bodies_start_in_doc_mode","bool",True),
                # For compatibility with previous versions.
            ("create_nonexistent_directories","bool",False),
            ("output_initial_comment","string",""),
                # "" for compatibility with previous versions.
            ("output_newline","string","nl"),
            ("page_width","int","132"),
            ("read_only","bool",True),
                # Make sure we don't alter an illegal leoConfig.txt file!
            ("redirect_execute_script_output_to_log_pane","bool",False),
            ("relative_path_base_directory","string","!"),
            ("remove_sentinels_extension","string",".txt"),
            ("save_clears_undo_buffer","bool",False),
            ("stylesheet","string",None),
            ("tab_width","int",-4),
            ("target_language","language","python"), # Bug fix: added: 6/20/2005.
            ("trailing_body_newlines","string","asis"),
            ("use_plugins","bool",True),
                # New in 4.3: use_plugins = True by default.
            
            ("undo_granularity","string","word"),
                # "char","word","line","node"
            ("write_strips_blank_lines","bool",False),
        )
        #@-node:AGP.20260222223302.4:ivarsDict
        #@-others
            
        # List of dictionaries to search.  Order not too important.
        dictList = [ivarsDict,encodingIvarsDict,defaultsDict]
        
        # Keys are commanders.  Values are optionsDicts.
        localOptionsDict = {}
        
        localOptionsList = []
            
        # Keys are setting names, values are type names.
        warningsDict = {} # Used by get() or allies.
        #@-node:AGP.20260222223302.1:<<  class data >>
        #@nl
        #@    @+others
        #@+node:AGP.20260222223437:class settingsTreeParser
        class settingsTreeParser:
            
            '''A class that inits settings found in an @settings tree. Used by read settings logic.'''
        
            
            # These are the canonicalized names.  Case is ignored, as are '_' and '-' characters.
        
            basic_types = [
                # Headlines have the form @kind name = var
                'bool','color','directory','int','ints',
                'float','path','ratio','shortcut','string','strings']
        
            control_types = [
                'abbrev','font','if','ifgui','ifplatform','ignore','mode','page',
                'settings','shortcuts','config']
        
            
            
            #@    @+others
            #@+node:AGP.20260222223437.1:__init__()
            def __init__(self,vroot,config):
                
                self.config = config
                self.vroot = vroot
                self.recentFiles = [] # List of recent files.
                #self.shortcutsDict = {}
                        # Keys are cononicalized shortcut names, values are bunches.
                
                #self.shortcuts = {}
                #self.settings = {}
                
                # Keys are settings names, values are (type,value) tuples.
                self.settingsDict = {}
                
                # Keys are canonicalized names.
                self.dispatchDict = {
                    'config':       self.doConfig, # New agp 
                    'abbrev':       self.doAbbrev, # New in 4.4.1 b2.
                    'bool':         self.doBool,
                    'color':        self.doColor,
                    'directory':    self.doDirectory,
                    'font':         self.doFont,
                    'if':           self.doIf,
                    # 'ifgui':        self.doIfGui,  # Removed in 4.4 b3.
                    'ifplatform':   self.doIfPlatform,
                    'ignore':       self.doIgnore,
                    'int':          self.doInt,
                    'ints':         self.doInts,
                    'float':        self.doFloat,
                    #'mode':         self.doMode, # New in 4.4b1.
                    'path':         self.doPath,
                    'page':         self.doPage,
                    'ratio':        self.doRatio,
                    # 'shortcut':     self.doShortcut, # Removed in 4.4.1 b1.
                    'shortcuts':    self.doShortcuts,
                    'string':       self.doString,
                    'strings':      self.doStrings,
                }
            #@-node:AGP.20260222223437.1:__init__()
            #@+node:AGP.20260222223437.2:error
            def error (self,s):
            
                print s
            
                # Does not work at present because we are using a null Gui.
                g.es(s,color="blue")
            #@-node:AGP.20260222223437.2:error
            #@+node:AGP.20260222223437.3:kind handlers
            #@+node:AGP.20260222223437.4:doConfig
            def doConfig(self,p,kind,name,val):
                
                #import Tkinter as tk
                #from tkFont import Font
                
                s = p.bodyString()
                lines = g.splitLines(s)
                
                d = {}
                setattr(g,name,d)
                
                gd = {"shade":g.color_shade,
                #        "Font":Font
                }
                #print "GAPPROOT",g.app.root
                
                
                
                
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        
                                
                        elms = line.split("=",1)
                        k = elms[0].strip()
                        if len(elms) > 1:
                            val = elms[1].strip()
                        else:
                            val = elms[0]
                        
                        try:
                            #print name,k,val
                            if val != None:
                                d[k] = eval(val,gd,d)
                                #print k
                            if line.startswith("*"):
                                if len(line.split("*"))==2:
                                    d[k[1:].lower()] = eval(val,gd,d)
                                
                                #print k
                            
                        except Exception as e:
                            pass
                            import traceback ; traceback.print_exc()
                            print "Config error in",name,k,e
                
                #print "Config",name,d
                
                self.set('config',name,d)
            #@-node:AGP.20260222223437.4:doConfig
            #@+node:AGP.20260222223437.5:doAbbrev
            def doAbbrev (self,p,kind,name,val):
                
                d = {}
                s = p.bodyString()
                lines = g.splitLines(s)
                for line in lines:
                    line = line.strip()
                    if line and not g.match(line,0,'#'):
                        name,val = self.parseAbbrevLine(line)
                        if name: d [val] = name
                        
                self.set (p,'abbrev','abbrev',d)
            #@-node:AGP.20260222223437.5:doAbbrev
            #@+node:AGP.20260222223437.6:doBool
            def doBool (self,p,kind,name,val):
            
                if val in ('True','true','1'):
                    self.set(kind,name,True)
                elif val in ('False','false','0'):
                    self.set(kind,name,False)
                else:
                    self.valueError(p,kind,name,val)
            #@-node:AGP.20260222223437.6:doBool
            #@+node:AGP.20260222223437.7:doColor
            def doColor (self,p,kind,name,val):
                
                # At present no checking is done.
                val = val.lstrip('"').rstrip('"')
                val = val.lstrip("'").rstrip("'")
            
                self.set(kind,name,val)
            #@-node:AGP.20260222223437.7:doColor
            #@+node:AGP.20260222223437.8:doDirectory & doPath
            def doDirectory (self,p,kind,name,val):
                
                # At present no checking is done.
                self.set(kind,name,val)
            
            doPath = doDirectory
            #@-node:AGP.20260222223437.8:doDirectory & doPath
            #@+node:AGP.20260222223437.9:doFloat
            def doFloat (self,p,kind,name,val):
                
                try:
                    val = float(val)
                    self.set(kind,name,val)
                except ValueError:
                    self.valueError(kind,name,val)
            #@-node:AGP.20260222223437.9:doFloat
            #@+node:AGP.20260222223437.10:doFont
            def doFont (self,p,kind,name,val):
                
                d = self.parseFont(p)
                
                # Set individual settings.
                for key in ('family','size','slant','weight'):
                    data = d.get(key)
                    if data is not None:
                        name,val = data
                        setKind = key
                        self.set(setKind,name,val)
            #@-node:AGP.20260222223437.10:doFont
            #@+node:AGP.20260222223437.11:doIf
            def doIf(self,p,kind,name,val):
                
                g.trace("'if' not supported yet")
                return None
            #@-node:AGP.20260222223437.11:doIf
            #@+node:AGP.20260222223437.12:doIfGui
            #@+at 
            #@nonl
            # Alas, @if-gui can't be made to work. The problem is that plugins 
            # can set
            # g.app.gui, but plugins need settings so the leoSettings.leo 
            # files must be parsed
            # before g.app.gui.guiName() is known.
            #@-at
            #@@c
            
            if 0:
            
                def doIfGui (self,p,kind,name,val):
                    
                    # g.trace(repr(name))
                    
                    if not g.app.gui or not g.app.gui.guiName():
                        s = '@if-gui has no effect: g.app.gui not defined yet'
                        g.es_print(s,color='blue')
                        return "skip"
                    elif g.app.gui.guiName().lower() == name.lower():
                        return None
                    else:
                        return "skip"
            #@-node:AGP.20260222223437.12:doIfGui
            #@+node:AGP.20260222223437.13:doIfPlatform
            def doIfPlatform (self,p,kind,name,val):
                
                # g.trace(sys.platform,repr(name))
            
                if sys.platform.lower() == name.lower():
                    return None
                else:
                    return "skip"
            #@-node:AGP.20260222223437.13:doIfPlatform
            #@+node:AGP.20260222223437.14:doIgnore
            def doIgnore(self,p,kind,name,val):
            
                return "skip"
            #@-node:AGP.20260222223437.14:doIgnore
            #@+node:AGP.20260222223437.15:doInt
            def doInt (self,p,kind,name,val):
                
                try:
                    val = int(val)
                    self.set(kind,name,val)
                except ValueError:
                    self.valueError(p,kind,name,val)
            #@-node:AGP.20260222223437.15:doInt
            #@+node:AGP.20260222223437.16:doInts
            def doInts (self,p,kind,name,val):
                
                '''We expect either:
                @ints [val1,val2,...]aName=val
                @ints aName[val1,val2,...]=val'''
            
                name = name.strip() # The name indicates the valid values.
                i = name.find('[')
                j = name.find(']')
                
                # g.trace(kind,name,val)
            
                if -1 < i < j:
                    items = name[i+1:j]
                    items = items.split(',')
                    name = name[:i]+name[j+1:].strip()
                    # g.trace(name,items)
                    try:
                        items = [int(item.strip()) for item in items]
                    except ValueError:
                        items = []
                        self.valueError(p,'ints[]',name,val)
                        return
                    kind = "ints[%s]" % (','.join([str(item) for item in items]))
                    try:
                        val = int(val)
                    except ValueError:
                        self.valueError(p,'int',name,val)
                        return
                    if val not in items:
                        self.error("%d is not in %s in %s" % (val,kind,name))
                        return
            
                    # g.trace(repr(kind),repr(name),val)
            
                    # At present no checking is done.
                    self.set(kind,name,val)
            #@-node:AGP.20260222223437.16:doInts
            #@+node:AGP.20260222223437.17:doPage
            def doPage(self,p,kind,name,val):
            
                pass # Ignore @page this while parsing settings.
            #@-node:AGP.20260222223437.17:doPage
            #@+node:AGP.20260222223437.18:doRatio
            def doRatio (self,p,kind,name,val):
                
                try:
                    val = float(val)
                    if 0.0 <= val <= 1.0:
                        self.set(kind,name,val)
                    else:
                        self.valueError(p,kind,name,val)
                except ValueError:
                    self.valueError(p,kind,name,val)
            #@-node:AGP.20260222223437.18:doRatio
            #@+node:AGP.20260222223437.19:doShortcuts()
            def doShortcuts(self,p,kind,name,val,s=None):
                
                # g.trace(self.c.fileName(),name)
            
                #c = self.c
                d = self.shortcutsDict
                if s is None: s = p.bodyString()
                lines = g.splitLines(s)
                for line in lines:
                    line = line.strip()
                    if line and not g.match(line,0,'#'):
                        #print "doshorcut",name,val,
                        name,val = self.parseShortcutLine(line)
                        #print name,val
                        if val is not None:
                            d [name] = val
                            self.set("shortcut",name,val)
                            self.setShortcut(name,val)
            #@-node:AGP.20260222223437.19:doShortcuts()
            #@+node:AGP.20260222223437.20:doString
            def doString (self,p,kind,name,val):
                
                # At present no checking is done.
                self.set(kind,name,val)
            #@-node:AGP.20260222223437.20:doString
            #@+node:AGP.20260222223437.21:doStrings
            def doStrings (self,p,kind,name,val):
                
                '''We expect one of the following:
                @strings aName[val1,val2...]=val
                @strings [val1,val2,...]aName=val'''
                
                name = name.strip()
                i = name.find('[')
                j = name.find(']')
            
                if -1 < i < j:
                    items = name[i+1:j]
                    items = items.split(',')
                    items = [item.strip() for item in items]
                    name = name[:i]+name[j+1:].strip()
                    kind = "strings[%s]" % (','.join(items))
                    # g.trace(repr(kind),repr(name),val)
            
                    # At present no checking is done.
                    self.set(kind,name,val)
            #@-node:AGP.20260222223437.21:doStrings
            #@-node:AGP.20260222223437.3:kind handlers
            #@+node:AGP.20260222223437.22:munge
            def munge(self,s):
            
                return g.app.config.canonicalizeSettingName(s)
            #@-node:AGP.20260222223437.22:munge
            #@+node:AGP.20260222223437.23:oops
            def oops (self):
                print ("parserBaseClass oops:",
                    g.callers(),
                    "must be overridden in subclass")
            #@-node:AGP.20260222223437.23:oops
            #@+node:AGP.20260222223437.24:parsers
            #@+node:AGP.20260222223437.25:fontSettingNameToFontKind
            def fontSettingNameToFontKind (self,name):
                
                s = name.strip()
                if s:
                    for tag in ('_family','_size','_slant','_weight'):
                        if s.endswith(tag):
                            return tag[1:]
            
                return None
            #@-node:AGP.20260222223437.25:fontSettingNameToFontKind
            #@+node:AGP.20260222223437.26:parseFont
            def parseFont (self,p):
                
                d = {
                    'comments': [],
                    'family': None,
                    'size': None,
                    'slant': None,
                    'weight': None,
                }
            
                s = p.bodyString()
                lines = g.splitLines(s)
            
                for line in lines:
                    self.parseFontLine(line,d)
                    
                comments = d.get('comments')
                d['comments'] = '\n'.join(comments)
                    
                return d
            #@-node:AGP.20260222223437.26:parseFont
            #@+node:AGP.20260222223437.27:parseFontLine
            def parseFontLine (self,line,d):
                
                s = line.strip()
                if not s: return
                
                try:
                    s = str(s)
                except UnicodeError:
                    pass
                
                if g.match(s,0,'#'):
                    s = s[1:].strip()
                    comments = d.get('comments')
                    comments.append(s)
                    d['comments'] = comments
                else:
                    # name is everything up to '='
                    i = s.find('=')
                    if i == -1:
                        name = s ; val = None
                    else:
                        name = s[:i].strip()
                        val = s[i+1:].strip()
                        val = val.lstrip('"').rstrip('"')
                        val = val.lstrip("'").rstrip("'")
            
                    fontKind = self.fontSettingNameToFontKind(name)
                    if fontKind:
                        d[fontKind] = name,val # Used only by doFont.
            #@-node:AGP.20260222223437.27:parseFontLine
            #@+node:AGP.20260222223437.28:parseHeadline
            def parseHeadline (self,s):
                
                """Parse a headline of the form @kind:name=val
                Return (kind,name,val)."""
            
                kind = name = val = None
            
                if g.match(s,0,'@'):
                    i = g.skip_id(s,1,chars='-')
                    kind = s[1:i].strip()
                    if kind:
                        # name is everything up to '='
                        j = s.find('=',i)
                        if j == -1:
                            name = s[i:].strip()
                        else:
                            name = s[i:j].strip()
                            # val is everything after the '='
                            val = s[j+1:].strip()
            
                # g.trace("%50s %10s %s" %(name,kind,val))
                return kind,name,val
            #@-node:AGP.20260222223437.28:parseHeadline
            #@+node:AGP.20260222223437.29:parseShortcutLine (g.app.config)
            def parseShortcutLine (self,s):
                
                '''Parse a shortcut line.  Valid forms:
                    
                --> entry-command
                settingName = shortcut
                settingName ! paneName = shortcut
                command-name -> mode-name = binding
                command-name -> same = binding
                '''
                
                name = val = nextMode = None ; nextMode = 'none'
                i = g.skip_ws(s,0)
               
                if g.match(s,i,'-->'): # New in 4.4.1 b1: allow mode-entry commands.
                    j = g.skip_ws(s,i+3)
                    i = g.skip_id(s,j,'-')
                    entryCommandName = s[j:i]
                    return None,g.Bunch(entryCommandName=entryCommandName)
                
                j = i
                i = g.skip_id(s,j,'-') # New in 4.4: allow Emacs-style shortcut names.
                name = s[j:i]
                if not name: return None,None
                
                # New in Leo 4.4b2.
                i = g.skip_ws(s,i)
                if g.match(s,i,'->'): # New in 4.4: allow pane-specific shortcuts.
                    j = g.skip_ws(s,i+2)
                    i = g.skip_id(s,j)
                    nextMode = s[j:i]
                    
                i = g.skip_ws(s,i)
                if g.match(s,i,'!'): # New in 4.4: allow pane-specific shortcuts.
                    j = g.skip_ws(s,i+1)
                    i = g.skip_id(s,j)
                    pane = s[j:i]
                    if not pane.strip(): pane = 'all'
                else: pane = 'all'
            
                i = g.skip_ws(s,i)
                if g.match(s,i,'='):
                    i = g.skip_ws(s,i+1)
                    val = s[i:]
                       
                # New in 4.4: Allow comments after the shortcut.
                # Comments must be preceded by whitespace.
                comment = ''
                if val:
                    i = val.find('#')
                    if i > 0 and val[i-1] in (' ','\t'):
                        # comment = val[i:].strip()
                        val = val[:i].strip()
            
                # g.trace(pane,name,val,s)
                return name,val
            #@-node:AGP.20260222223437.29:parseShortcutLine (g.app.config)
            #@+node:AGP.20260222223437.30:parseAbbrevLine (g.app.config)
            def parseAbbrevLine (self,s):
                
                '''Parse an abbreviation line:
                command-name = abbreviation
                return (command-name,abbreviation)
                '''
            
                i = j = g.skip_ws(s,0)
                i = g.skip_id(s,i,'-') # New in 4.4: allow Emacs-style shortcut names.
                name = s[j:i]
                if not name: return None,None
            
                i = g.skip_ws(s,i)
                if not g.match(s,i,'='): return None,None
            
                i = g.skip_ws(s,i+1)
                val = s[i:].strip()
                # Ignore comments after the shortcut.
                i = val.find('#')
                if i > -1: val = val[:i].strip()
            
                if val: return name,val
                else:   return None,None
            #@-node:AGP.20260222223437.30:parseAbbrevLine (g.app.config)
            #@-node:AGP.20260222223437.24:parsers
            #@+node:AGP.20260222223437.31:set()
            def set(self,kind,name,val):
                
                """Init the setting for name to val."""
                
                #print "parser set",kind,name,val
                #print "set()",name,val
                self.settingsDict[name] = val
            #@-node:AGP.20260222223437.31:set()
            #@+node:AGP.20260222223437.32:setShortcut()
            def setShortcut (self,name,val):
                
                #c = self.c
                
                # None is a valid value for val.
                key = name.lower()
                rawKey = key.replace('&','')
                self.set(rawKey,"shortcut",val)
                #print "setShortcut",rawKey,val
                # g.trace(bunch.pane,rawKey,bunch.val)
            #@-node:AGP.20260222223437.32:setShortcut()
            #@+node:AGP.20260222223437.33:traverse()
            def traverse(self):
                
                #c = self.c
                
                p = self.config.settingsRoot(self.vroot)
                
                if not p:
                    # g.trace('no settings tree for %s' % c)
                    return None
            
                self.settingsDict = {}
                self.shortcutsDict = {}
                after = p.nodeAfterTree()
                
                while p and p != after:
                    result = self.visitNode(p)
                    # g.trace(result,p.headString())
                    if result == "skip":
                        if 0:
                            s = 'skipping settings in %s' % p.headString()
                            g.es_print(s,color='blue')
                        p.moveToNodeAfterTree()
                    else:
                        p.moveToThreadNext()
                        
                return self.settingsDict
            #@-node:AGP.20260222223437.33:traverse()
            #@+node:AGP.20260222223437.34:valueError
            def valueError (self,p,kind,name,val):
                
                """Give an error: val is not valid for kind."""
                
                self.error("%s is not a valid %s for %s" % (val,kind,name))
            #@-node:AGP.20260222223437.34:valueError
            #@+node:AGP.20260222223437.35:visitNode()
            def visitNode (self,p):
                
                """Init any settings found in node p."""
                
                # g.trace(p.headString())
                
                munge = self.config.munge
            
                kind,name,val = self.parseHeadline(p.headString())
                kind = munge(kind)
                
                if kind == "settings":
                    pass
                elif kind not in self.control_types and val in (u'None',u'none','None','none','',None):
                    # None is valid for all data types.
                    #print "visit1",p,kind,name,val
                    self.set(kind,name,None)
                    
                elif kind in self.control_types or kind in self.basic_types:
                    f = self.dispatchDict.get(kind)
                    try:
                        #print "visit2",p,kind,name,val
                        return f(p,kind,name,val)
                    except TypeError:
                        g.es_exception()
                        print "*** no handler",kind
                elif name:
                    # self.error("unknown type %s for setting %s" % (kind,name))
                    # Just assume the type is a string.
                    #print "visit3",p,kind,name,val
                    self.set(kind,name,val)
                
                return None
            #@-node:AGP.20260222223437.35:visitNode()
            #@-others
        #@-node:AGP.20260222223437:class settingsTreeParser
        #@+node:AGP.20260222223302.5:__init__()
        def __init__(self,filename=None):
            
            self.configsExist = False # True when we successfully open a setting file.
            self.defaultFont = None # Set in gui.getDefaultConfigFont.
            self.defaultFontFamily = None # Set in gui.getDefaultConfigFont.
            self.globalConfigFile = None # Set in initSettingsFiles
            self.homeFile = None # Set in initSettingsFiles
            self.inited = False
            self.modeCommandsDict = {} # For use by @mode logic. Keys are command names, values are g.Bunches.
            self.myGlobalConfigFile = None
            self.myHomeConfigFile = None
            self.recentFilesFiles = [] # List of g.Bunches describing .leoRecentFiles.txt files.
            self.write_recent_files_as_needed = False # Will be set later.
            
            # Inited later...
            self.panes = None
            self.sc = None
            self.tree = None
        
            self.initDicts()
            self.initIvarsFromSettings()
            self.initSettingsFiles()
            self.initRecentFiles()
            
            self.settings = {}
            
            if filename:
                self.readSettingsFiles(filename)
        #@nonl
        #@-node:AGP.20260222223302.5:__init__()
        #@+node:AGP.20260222223302.6:initDicts
        def initDicts (self):
            
            # Only the settings parser needs to search all dicts.
            self.dictList = [self.defaultsDict]
        
            for key,kind,val in self.defaultsData:
                self.defaultsDict[key] = val
                
            for key,kind,val in self.ivarsData:
                self.ivarsDict[key] = val
        
            for key,kind,val in self.encodingIvarsData:
                self.encodingIvarsDict[key] = val
        #@-node:AGP.20260222223302.6:initDicts
        #@+node:AGP.20260222223302.7:initIvarsFromSettings()
        def initIvarsFromSettings (self):
            
            for ivar in self.encodingIvarsDict.keys():
                if ivar != '_hash':
                    setattr(self,ivar,self.encodingIvarsDict.get(ivar))
                
            for ivar in self.ivarsDict.keys():
                if ivar != '_hash':
                    setattr(self,ivar,self.ivarsDict.get(ivar))
        #@-node:AGP.20260222223302.7:initIvarsFromSettings()
        #@+node:AGP.20260222223302.8:initRecentFiles
        def initRecentFiles (self):
        
            self.recentFiles = []
        #@-node:AGP.20260222223302.8:initRecentFiles
        #@+node:AGP.20260222223302.9:initSettingsFiles
        def initSettingsFiles (self):
            
            """Set self.globalConfigFile, self.homeFile and self.myConfigFile."""
            
            settingsFile = 'leoSettings.leo'
            mySettingsFile = 'myLeoSettings.leo'
            
            for ivar,theDir,fileName in (
                ('globalConfigFile',    leo.configDir,  settingsFile),
                ('homeFile',            leo.homeDir,          settingsFile),
                ('myGlobalConfigFile',  leo.configDir,  mySettingsFile),
                ('myHomeConfigFile',    leo.homeDir,          mySettingsFile),
            ):
                # The same file may be assigned to multiple ivars:
                # readSettingsFiles checks for such duplications.
                path = g.os_path_join(theDir,fileName)
                if g.os_path_exists(path):
                    setattr(self,ivar,path)
                else:
                    setattr(self,ivar,None)
        #@-node:AGP.20260222223302.9:initSettingsFiles
        #@+node:AGP.20260222223302.10:Getters... (g.app.config)
        #@+node:AGP.20260222223302.11:canonicalizeSettingName (munge)
        def canonicalizeSettingName (self,name):
            
            if name is None:
                return None
        
            name = name.lower()
            for ch in ('-','_',' ','\n'):
                name = name.replace(ch,'')
                
            return g.choose(name,name,None)
            
        munge = canonicalizeSettingName
        #@-node:AGP.20260222223302.11:canonicalizeSettingName (munge)
        #@+node:AGP.20260222223302.12:config.findSettingsPosition
        def findSettingsPosition (self,vroot,setting):
            
            """Return the position for the setting in the @settings tree for c."""
            
            munge = self.munge
            
            root = self.settingsRoot(vroot)
            if not root:
                return leoNodes.nullPosition()
                
            setting = munge(setting)
                
            for p in root.subtree_iter():
                h = munge(p.headString())
                if h == setting:
                    return p.copy()
            
            return leoNodes.nullPosition()
        #@-node:AGP.20260222223302.12:config.findSettingsPosition
        #@+node:AGP.20260222223302.13:get()
        def get (self,setting,kind):
            
            """Get the setting"""
            #print "getcfg",setting,kind
            return self.settings.get(setting,None)
        #@-node:AGP.20260222223302.13:get()
        #@+node:AGP.20260222223302.14:exists()
        def exists (self,setting,kind):
            
            '''Return true if a setting of the given kind exists, even if it is None.'''
        
            if setting in self.settings.keys():
                return True
        
            return False
        #@-node:AGP.20260222223302.14:exists()
        #@+node:AGP.20260222223302.15:getAbbrevDict
        def getAbbrevDict(self):
            
            """Search all dictionaries for the setting & check it's type"""
            
            d = self.get('abbrev','abbrev')
            return d or {}
        #@-node:AGP.20260222223302.15:getAbbrevDict
        #@+node:AGP.20260222223302.16:getBool
        def getBool(self,setting,default=None):
            
            """Search all dictionaries for the setting & check it's type"""
            
            val = self.get(setting,"bool")
            
            if val in (True,False):
                return val
            else:
                return default
        #@-node:AGP.20260222223302.16:getBool
        #@+node:AGP.20260222223302.17:getColor
        def getColor(self,setting):
            
            """Search all dictionaries for the setting & check it's type"""
            
            return self.get(setting,"color")
        #@-node:AGP.20260222223302.17:getColor
        #@+node:AGP.20260222223302.18:getDirectory
        def getDirectory (self,setting):
            
            """Search all dictionaries for the setting & check it's type"""
            
            theDir = self.getString(setting)
        
            if g.os_path_exists(theDir) and g.os_path_isdir(theDir):
                 return theDir
            else:
                return None
        #@-node:AGP.20260222223302.18:getDirectory
        #@+node:AGP.20260222223302.19:getFloat
        def getFloat (self,setting):
            
            """Search all dictionaries for the setting & check it's type"""
            
            val = self.get(setting,"float")
            try:
                val = float(val)
                return val
            except TypeError:
                return None
        #@-node:AGP.20260222223302.19:getFloat
        #@+node:AGP.20260222223302.20:getFontFromParams (config)
        def getFontFromParams(self,c,family,size,slant,weight,defaultSize=12):
        
            """Compute a font from font parameters.
        
            Arguments are the names of settings to be use.
            We default to size=12, slant="roman", weight="normal".
        
            We return None if there is no family setting so we can use system default fonts."""
        
            family = self.get(c,family,"family")
            if family in (None,""):
                family = self.defaultFontFamily
        
            size = self.get(c,size,"size")
            if size in (None,0): size = defaultSize
            
            slant = self.get(c,slant,"slant")
            if slant in (None,""): slant = "roman"
        
            weight = self.get(c,weight,"weight")
            if weight in (None,""): weight = "normal"
            
            # g.trace(g.callers(3),family,size,slant,weight,g.shortFileName(c.mFileName))
            
            return g.app.gui.getFontFromParams(family,size,slant,weight)
        #@-node:AGP.20260222223302.20:getFontFromParams (config)
        #@+node:AGP.20260222223302.21:getInt
        def getInt (self,setting):
            
            """Search all dictionaries for the setting & check it's type"""
            
            val = self.get(setting,"int")
            try:
                val = int(val)
                return val
            except TypeError:
                return None
        #@-node:AGP.20260222223302.21:getInt
        #@+node:AGP.20260222223302.22:getLanguage
        def getLanguage (self,setting):
            
            """Return the setting whose value should be a language known to Leo."""
            
            language = self.getString(setting)
            # g.trace(setting,language)
            
            return language
        #@-node:AGP.20260222223302.22:getLanguage
        #@+node:AGP.20260222223302.23:getRatio
        def getRatio (self,setting):
            
            """Search all dictionaries for the setting & check it's type"""
            
            val = self.get(setting,"ratio")
            try:
                val = float(val)
                if 0.0 <= val <= 1.0:
                    return val
                else:
                    return None
            except TypeError:
                return None
        #@-node:AGP.20260222223302.23:getRatio
        #@+node:AGP.20260222223302.24:getRecentFiles
        def getRecentFiles (self):
        
            return self.recentFiles
        #@-node:AGP.20260222223302.24:getRecentFiles
        #@+node:AGP.20260222223302.25:getShortcut()
        def getShortcut (self,shortcutName):
            
            '''Return rawKey,accel for shortcutName'''
            
            key = shortcutName.lower()
            key = key.replace('&','') # Allow '&' in names.
            sc = self.get(key,"shortcut")
            #print "getShortcut",shortcutName,key,sc
            return key,sc
        
        #@-node:AGP.20260222223302.25:getShortcut()
        #@+node:AGP.20260222223302.26:getString
        def getString(self,setting):
            
            """Search all dictionaries for the setting & check it's type"""
        
            return self.get(setting,"string")
        #@-node:AGP.20260222223302.26:getString
        #@+node:AGP.20260222223302.27:setCommandsIvars
        # Sets ivars of c that can be overridden by leoConfig.txt
        
        def setCommandsIvars (self,c):
        
            data = (
                ("default_tangle_directory","tangle_directory","directory"),
                ("default_target_language","target_language","language"),
                ("output_doc_chunks","output_doc_flag","bool"),
                ("page_width","page_width","int"),
                ("run_tangle_done.py","tangle_batch_flag","bool"),
                ("run_untangle_done.py","untangle_batch_flag","bool"),
                ("tab_width","tab_width","int"),
                ("tangle_outputs_header","use_header_flag","bool"),
            )
            
            for setting,ivar,theType in data:
                val = g.app.config.get(setting,theType)
                
                print "setcivars",setting,val
                if val is None:
                    if not hasattr(c,setting):
                        setattr(c,setting,None)
                        # g.trace(setting,None)
                else:
                    
                    setattr(c,setting,val)
                    # g.trace(setting,val)
        #@-node:AGP.20260222223302.27:setCommandsIvars
        #@+node:AGP.20260222223302.28:settingsRoot
        def settingsRoot (self,v):
            for p in leoNodes.position(v).all_iter():
                if p.headString().rstrip() == "@settings":
                    return p.copy()
            else:
                return leoNodes.nullPosition()
        #@-node:AGP.20260222223302.28:settingsRoot
        #@-node:AGP.20260222223302.10:Getters... (g.app.config)
        #@+node:AGP.20260222223302.29:Setters (g.app.config)
        #@+node:AGP.20260222223302.30:set()
        def set (self,setting,kind,val):
            
            '''Set the setting.  Not called during initialization.'''
            self.settings[setting] = val
        
        #@-node:AGP.20260222223302.30:set()
        #@+node:AGP.20260222223302.31:setString
        def setString (self,c,setting,val):
            
            self.set(setting,"string",val)
        #@-node:AGP.20260222223302.31:setString
        #@+node:AGP.20260222223302.32:setIvarsFromSettings (g.app.config)
        def setIvarsFromSettings (self,c):
        
            '''Init g.app.config ivars or c's ivars from settings.
            
            - Called from readSettingsFiles with c = None to init g.app.config ivars.
            - Called from c.__init__ to init corresponding commmander ivars.'''
            
            # Ingore temporary commanders created by readSettingsFiles.
            if not self.inited: return
        
            # g.trace(c)
            d = self.ivarsDict
            for key in d:
                if key != '_hash':
                    val = self.get(key,"")
                    #print key,ivar,val
                        
                    if c:
                        #print "setcivars",key,val
                        setattr(c,key,val)
                    else:
                        #print "setselfivars",key,val
                        setattr(self,key,val)
        #@-node:AGP.20260222223302.32:setIvarsFromSettings (g.app.config)
        #@+node:AGP.20260222223302.33:appendToRecentFiles (g.app.config)
        def appendToRecentFiles (self,files):
            
            files = [theFile.strip() for theFile in files]
            
            # g.trace(files)
            
            def munge(name):
                name = name or ''
                return g.os_path_normpath(name).lower()
            
            for name in files:
                # Remove all variants of name.
                for name2 in self.recentFiles:
                    if munge(name) == munge(name2):
                        self.recentFiles.remove(name2)
        
                self.recentFiles.append(name)
        #@-node:AGP.20260222223302.33:appendToRecentFiles (g.app.config)
        #@+node:AGP.20260222223302.34:setRecentFiles (c.configSettings)
        def setRecentFiles (self,files):
            
            '''Update the recent files list.'''
        
            # Append the files to the global list.
            self.appendToRecentFiles(files)
        #@-node:AGP.20260222223302.34:setRecentFiles (c.configSettings)
        #@-node:AGP.20260222223302.29:Setters (g.app.config)
        #@+node:AGP.20260222223302.35:Scanning @settings (g.app.config)
        #@+node:AGP.20260222223302.36:readSettingsFiles()
        def readSettingsFiles (self,fileName,verbose=True):
                
            self.write_recent_files_as_needed = False # Will be set later.
        
            if verbose:
                leo.log('reading settings in %s' % fileName)
            #c = self.openSettingsFile(path)
            leofile = leo.LEOFILE()
            vroot = leofile.load(fileName)
            if vroot:
                d = self.readSettings(vroot)
                if d:
                    self.settings.update(d)
            
            
            # Read all .leoRecentFiles.txt files.
            # The order of files in this list affects the order of the recent files list.
            
            #localConfigPath = g.os_path_dirname(localConfigFile)
            #for path in (
                #g.app.homeDir,
                #g.app.globalConfigDir,
                #localConfigPath,
            #):
            #    if path:
            #        ok = self.readRecentFilesFile(path)
                    
            #if self.write_recent_files_as_needed:
            #    self.createRecentFiles()
        
            self.inited = True
            self.setIvarsFromSettings(None)
        #@-node:AGP.20260222223302.36:readSettingsFiles()
        #@+node:AGP.20260222223302.37:readSettings()
        # Called to read all leoSettings.leo files.
        # Also called when opening an .leo file to read @settings tree.
        
        def readSettings (self,vroot):
            
            """Read settings from a file that may contain an @settings tree."""
        
            parser = self.settingsTreeParser(vroot,self)
            d = parser.traverse()
            
            
        
            return d
        #@-node:AGP.20260222223302.37:readSettings()
        #@+node:AGP.20260222223302.38:updateSettings()
        def updateSettings (self,vroot,localFlag):
        
            d = self.readSettings(vroot)
            
            if d:
                self.settings.update(d)
        
        #@-node:AGP.20260222223302.38:updateSettings()
        #@-node:AGP.20260222223302.35:Scanning @settings (g.app.config)
        #@+node:AGP.20260222223302.39:Reading and writing .leoRecentFiles.txt (g.app.config)
        #@+node:AGP.20260222223302.40:createRecentFiles
        def createRecentFiles (self):
            
            '''Trye to reate .leoRecentFiles.txt in
            - the users home directory first,
            - Leo's config directory second.'''
        
            for theDir in (g.app.homeDir,g.app.globalConfigDir):
                if theDir:
                    try:
                        fileName = g.os_path_join(theDir,'.leoRecentFiles.txt')
                        f = file(fileName,'w')
                        f.close()
                        g.es_print('created %s' % (fileName),color='red')
                        return
                    except Exception:
                        g.es_print('can not create %s' % (fileName),color='red')
                        g.es_exception()
        #@nonl
        #@-node:AGP.20260222223302.40:createRecentFiles
        #@+node:AGP.20260222223302.41:readRecentFilesFile
        def readRecentFilesFile (self,path):
        
            fileName = g.os_path_join(path,'.leoRecentFiles.txt')
            ok = g.os_path_exists(fileName)
            if ok:
            
                print ('reading %s' % fileName)
                lines = file(fileName).readlines()
                if lines and self.munge(lines[0])=='readonly':
                    lines = lines[1:]
                if lines:
                    lines = [g.toUnicode(g.os_path_normpath(line),'utf-8') for line in lines]
                    self.appendToRecentFiles(lines)
                    
            return ok
        #@nonl
        #@-node:AGP.20260222223302.41:readRecentFilesFile
        #@+node:AGP.20260222223302.42:writeRecentFilesFile()
        def writeRecentFilesFile (self,c):
            
            '''Write the appropriate .leoRecentFiles.txt file.'''
            
            tag = '.leoRecentFiles.txt'
            
            if g.app.unitTesting:
                return
            
            localFileName = c.fileName()
            if localFileName:
                localPath,junk = g.os_path_split(localFileName)
            else:
                localPath = None
                
            for path in (localPath,g.app.globalConfigDir,g.app.homeDir):
                if path:
                    fileName = g.os_path_join(path,tag)
                    if g.os_path_exists(fileName):
                        print ('wrote %s' % fileName)
                        self.writeRecentFilesFileHelper(fileName)
                        return
            else:
                # g.trace('----- not found: %s' % g.os_path_join(localPath,tag))
                return
        #@-node:AGP.20260222223302.42:writeRecentFilesFile()
        #@+node:AGP.20260222223302.43:writeRecentFilesFileHelper()
        def writeRecentFilesFileHelper (self,fileName):
            # g.trace(fileName)
            
            # Don't update the file if it begins with read-only.
            theFile = None
            try:
                theFile = file(fileName)
                lines = theFile.readlines()
                if lines and self.munge(lines[0])=='readonly':
                    # g.trace('read-only: %s' %fileName)
                    return
            except IOError:
                # The user may have erased a file.  Not an error.
                if theFile: theFile.close()
        
            theFile = None
            try:
                # g.trace('writing',fileName)
                theFile = file(fileName,'w')
                if self.recentFiles:
                    lines = [g.toEncodedString(line,'utf-8') for line in self.recentFiles]
                    theFile.write('\n'.join(lines))
                else:
                    theFile.write('\n')
        
            except IOError:
                # The user may have erased a file.  Not an error.
                pass
                    
            except Exception:
                g.es('unexpected exception writing %s' % fileName,color='red')
                g.es_exception()
            
            if theFile:
                theFile.close()
        #@-node:AGP.20260222223302.43:writeRecentFilesFileHelper()
        #@-node:AGP.20260222223302.39:Reading and writing .leoRecentFiles.txt (g.app.config)
        #@+node:AGP.20260222223302.44:canonicalizeMenuName()
        def canonicalizeMenuName (self,name):
            
            return ''.join([ch for ch in name.lower() if ch.isalnum()])
        #@nonl
        #@-node:AGP.20260222223302.44:canonicalizeMenuName()
        #@-others
    #@-node:AGP.20260222223302:class CONFIG
    #@-others
    
    

    loadDir,leoDir,homeDir,extensionsDir,configDir,testDir,user_xresources_path = get_directories()

    fileName = get_filename()

    import leoLang as lang
    import leoGlobals as g
    import leoNodes
    
    #train_autocomplete()
    
    app = g.app = LEOAPP()
    
    #Create config and read settings
    config = g.config = app.config = CONFIG(configDir+"\\leoSettings.leo")

    app.setEncoding()
    
    #exe_dir,exe_name = os.path.split(sys.argv[0]) # agp... fix frozen exe
    #exe_dir,exe_name = os.getcwd(),sys.argv[0]
    
    #create_window()
    import leoUi as ui
    
    #Load file
    if fileName and fileName != "":
        leofile_Open(fileName)
    
#@nonl
#@-node:AGP.20250415230112.3:@thin leo.py 
#@-leo
