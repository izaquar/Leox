# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:AGP.20250415230112.2925:@thin leoGui.py
#@@first

"""A module containing the base leoGui class.

This class and its subclasses hides the details of which gui is actually being used.
Leo's core calls this class to allocate all gui objects.

Plugins may define their own gui classes by setting g.app.gui."""

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import leoFrame # for null gui.

#@+others
#@+node:AGP.20250415230112.2926:class leoGui
class leoGui:
    
    """The base class of all gui classes.
    
    Subclasses are expected to override all do-nothing methods of this class."""
    
    #@    << define leoGui file types >>
    #@+node:AGP.20250415230112.2927:<< define leoGui file types >> (not used yet)
    allFullFiletypes = [
        ("All files",   "*"),
        ("C/C++ files", "*.c"),
        ("C/C++ files", "*.cpp"),
        ("C/C++ files", "*.h"),
        ("C/C++ files", "*.hpp"),
        ("Java files",  "*.java"),
        ("Lua files",   "*.lua"),
        ("Pascal files","*.pas"),
        ("Python files","*.py")]
        # To do: *.php, *.php3, *.php4")
    pythonFullFiletypes = [
        ("Python files","*.py"),
        ("All files","*"),
        ("C/C++ files","*.c"),
        ("C/C++ files","*.cpp"),
        ("C/C++ files","*.h"),
        ("C/C++ files","*.hpp"),
        ("Java files","*.java"),
        ("Lua files",   "*.lua"),
        ("Pascal files","*.pas")]
        # To do: *.php, *.php3, *.php4")
    textFullFiletypes = [
        ("Text files","*.txt"),
        ("C/C++ files","*.c"),
        ("C/C++ files","*.cpp"),
        ("C/C++ files","*.h"),
        ("C/C++ files","*.hpp"),
        ("Java files","*.java"),
        ("Lua files",   "*.lua"),
        ("Pascal files","*.pas"),
        ("Python files","*.py"),
        ("All files","*")]
        # To do: *.php, *.php3, *.php4")
    CWEBTextAllFiletypes = [
        ("CWEB files","*.w"),
        ("Text files","*.txt"),
        ("All files", "*")]
    leoAllFiletypes = [
        ("Leo files","*.leo"),
        ("All files","*")]
    leoFiletypes = [
        ("Leo files","*.leo")]
    nowebTextAllFiletypes = [
        ("Noweb files","*.nw"),
        ("Text files", "*.txt"),
        ("All files",  "*")]
    textAllFiletypes = [
        ("Text files","*.txt"),
        ("All files", "*")]
    #@-node:AGP.20250415230112.2927:<< define leoGui file types >> (not used yet)
    #@nl
    
    #@    @+others
    #@+node:AGP.20250415230112.2928:app.gui Birth & death
    #@+node:AGP.20250415230112.2929: leoGui.__init__
    def __init__ (self,guiName):
        
        # g.trace("leoGui",guiName,g.callers())
        
        self.lastFrame = None
        self.leoIcon = None
        self.mGuiName = guiName
        self.mainLoop = None
        self.root = None
        self.script = None
        self.utils = None
        self.isNullGui = False
    #@-node:AGP.20250415230112.2929: leoGui.__init__
    #@+node:AGP.20250415230112.2930:stubs
    #@+node:AGP.20250415230112.2931:createRootWindow
    def createRootWindow(self):
    
        """Create the hidden root window for the gui.
        
        Nothing needs to be done if the root window need not exist."""
    
        self.oops()
    #@-node:AGP.20250415230112.2931:createRootWindow
    #@+node:AGP.20250415230112.2932:destroySelf
    def destroySelf (self):
    
        self.oops()
    #@-node:AGP.20250415230112.2932:destroySelf
    #@+node:AGP.20250415230112.2933:finishCreate
    def finishCreate (self):
    
        """Do any remaining chores after the root window has been created."""
    
        self.oops()
    #@-node:AGP.20250415230112.2933:finishCreate
    #@+node:AGP.20250415230112.2934:killGui
    def killGui(self,exitFlag=True):
    
        """Destroy the gui.
        
        The entire Leo application should terminate if exitFlag is True."""
    
        self.oops()
    #@-node:AGP.20250415230112.2934:killGui
    #@+node:AGP.20250415230112.2935:recreateRootWindow
    def recreateRootWindow(self):
    
        """Create the hidden root window of the gui
        after a previous gui has terminated with killGui(False)."""
    
        self.oops()
    #@-node:AGP.20250415230112.2935:recreateRootWindow
    #@+node:AGP.20250415230112.2936:runMainLoop
    def runMainLoop(self):
    
        """Run the gui's main loop."""
    
        self.oops()
    #@-node:AGP.20250415230112.2936:runMainLoop
    #@-node:AGP.20250415230112.2930:stubs
    #@-node:AGP.20250415230112.2928:app.gui Birth & death
    #@+node:AGP.20250415230112.2937:app.gui dialogs
    def runAboutLeoDialog(self,c,version,theCopyright,url,email):
        """Create and run Leo's About Leo dialog."""
        self.oops()
        
    def runAskLeoIDDialog(self):
        """Create and run a dialog to get g.app.LeoID."""
        self.oops()
    
    def runAskOkDialog(self,c,title,message=None,text="Ok"):
        """Create and run an askOK dialog ."""
        self.oops()
    
    def runAskOkCancelNumberDialog(self,c,title,message):
        """Create and run askOkCancelNumber dialog ."""
        self.oops()
    
    def runAskYesNoDialog(self,c,title,message=None):
        """Create and run an askYesNo dialog."""
        self.oops()
    
    def runAskYesNoCancelDialog(self,c,title,
        message=None,yesMessage="Yes",noMessage="No",defaultButton="Yes"):
        """Create and run an askYesNoCancel dialog ."""
        self.oops()
    #@-node:AGP.20250415230112.2937:app.gui dialogs
    #@+node:AGP.20250415230112.2938:app.gui file dialogs
    def runOpenFileDialog(self,title,filetypes,defaultextension,multiple=False):
    
        """Create and run an open file dialog ."""
    
        self.oops()
    
    def runSaveFileDialog(self,initialfile,title,filetypes,defaultextension):
    
        """Create and run a save file dialog ."""
        
        self.oops()
    #@-node:AGP.20250415230112.2938:app.gui file dialogs
    #@+node:AGP.20250415230112.2939:app.gui panels
    # New in 4.3: it is not an error to call these...
        
    def createComparePanel(self,c):
        """Create Compare panel."""
        
    def createFindPanel(self,c):
        """Create a hidden Find panel."""
        
    def createLeoFrame(self,title):
        """Create a new Leo frame."""
    #@-node:AGP.20250415230112.2939:app.gui panels
    #@+node:AGP.20250415230112.2940:app.gui utils
    #@+at 
    #@nonl
    # Subclasses are expected to subclass all of the following methods.
    # 
    # These are all do-nothing methods: callers are expected to check for None 
    # returns.
    # 
    # The type of commander passed to methods depends on the type of frame or 
    # dialog being created.  The commander may be a Commands instance or one 
    # of its subcommanders.
    #@-at
    #@+node:AGP.20250415230112.2941:Clipboard
    def replaceClipboardWith (self,s):
        
        self.oops()
    
    def getTextFromClipboard (self):
        
        self.oops()
    #@-node:AGP.20250415230112.2941:Clipboard
    #@+node:AGP.20250415230112.2942:Dialog utils
    def attachLeoIcon (self,window):
        """Attach the Leo icon to a window."""
        self.oops()
        
    def center_dialog(self,dialog):
        """Center a dialog."""
        self.oops()
        
    def create_labeled_frame (self,parent,caption=None,relief="groove",bd=2,padx=0,pady=0):
        """Create a labeled frame."""
        self.oops()
        
    def get_window_info (self,window):
        """Return the window information."""
        self.oops()
    #@-node:AGP.20250415230112.2942:Dialog utils
    #@+node:AGP.20250415230112.2943:Focus
    def get_focus(self,frame):
    
        """Return the widget that has focus, or the body widget if None."""
    
        self.oops()
            
    def set_focus(self,commander,widget):
    
        """Set the focus of the widget in the given commander if it needs to be changed."""
        
        self.oops()
        
    def widget_wants_focus(self,commander,widget):
    
        """Indicate that a widget want to get focus."""
        
        self.oops()
    #@-node:AGP.20250415230112.2943:Focus
    #@+node:AGP.20250415230112.2944:Font
    def getFontFromParams(self,family,size,slant,weight,defaultSize=12):
        
        pass
        # self.oops()
    #@-node:AGP.20250415230112.2944:Font
    #@+node:AGP.20250415230112.2945:Idle time
    def setIdleTimeHook (self,idleTimeHookHandler):
        
        # print 'leoGui:setIdleTimeHook'
        pass # Not an error.
        
    def setIdleTimeHookAfterDelay (self,idleTimeHookHandler):
        
        # print 'leoGui:setIdleTimeHookAfterDelay'
        pass # Not an error.
    #@-node:AGP.20250415230112.2945:Idle time
    #@+node:AGP.20250415230112.2946:Index
    def compareIndices (self,t,n1,rel,n2):
        self.oops()
    
    def firstIndex (self):
        self.oops()
        
    def getindex (self,body,index):
        self.oops()
        return 0,0
        
    def lastIndex (self):
        self.oops()
        
    def moveIndexBackward(self,index,n):
        self.oops()
        
    def moveIndexForward(self,t,index,n):
        self.oops()
        
    def moveIndexToNextLine(self,t,index):
        self.oops()
    
    def toGuiIndex (self,s,w,index):
        self.oops()
        
    def toPythonIndex (self,s,w,index):
       self.oops()
    #@nonl
    #@-node:AGP.20250415230112.2946:Index
    #@+node:AGP.20250415230112.2947:isTextWidget
    def isTextWidget (self,w):
        
        '''Return True if w is a Text widget suitable for text-oriented commands.'''
        
        self.oops()
    #@-node:AGP.20250415230112.2947:isTextWidget
    #@+node:AGP.20250415230112.2948:Selection
    def getSelectionRange (self,t):
        return 0,0
        
    def getSelectedText (self,t):
        return u""
        
    def getTextSelection (self,t,sort=True):
        return 0,0
        
    def hasSelection (self,widget):
        return False
    
    def selectAllText (self,w,insert='end-1c'):
        pass
        
    def setSelectionRangeWithLength(self,t,start,length,insert='sel.end'):
        pass
        
    def setTextSelection (self,t,start,end,insert='sel.end'):
        pass
        
    setSelectionRange = setTextSelection
    #@-node:AGP.20250415230112.2948:Selection
    #@-node:AGP.20250415230112.2940:app.gui utils
    #@+node:AGP.20250415230112.2949:guiName
    def guiName(self):
        
        try:
            return self.mGuiName
        except:
            return "invalid gui name"
    #@-node:AGP.20250415230112.2949:guiName
    #@+node:AGP.20250415230112.2950:setScript
    def setScript (self,script=None,scriptFileName=None):
    
        self.script = script
        self.scriptFileName = scriptFileName
    #@-node:AGP.20250415230112.2950:setScript
    #@+node:AGP.20250415230112.2951:widget_name
    def widget_name (self,w):
        
        return w and hasattr(w,'_name') and w._name or repr(w)
    #@-node:AGP.20250415230112.2951:widget_name
    #@+node:AGP.20250415230112.2952:oops
    def oops (self):
        
        # It is not usually an error to call methods of this class.
        # However, this message is useful when writing gui plugins.
        if 0:
            print "leoGui oops", g.callers(), "should be overridden in subclass"
    #@-node:AGP.20250415230112.2952:oops
    #@-others
#@-node:AGP.20250415230112.2926:class leoGui
#@+node:AGP.20250415230112.2953:class nullGui (leoGui)
class nullGui(leoGui):
    
    """Null gui class."""
    
    #@    @+others
    #@+node:AGP.20250415230112.2954:Birth & death
    #@+node:AGP.20250415230112.2955: nullGui.__init__
    def __init__ (self,guiName):
        
        # g.trace("nullGui")
        
        leoGui.__init__ (self,guiName) # init the base class.
        
        self.script = None
        self.lastFrame = None
        self.isNullGui = True
    #@-node:AGP.20250415230112.2955: nullGui.__init__
    #@+node:AGP.20250415230112.2956: nullGui.__getattr__
    if 0: # This causes no end of problems.
    
        def __getattr__(self,attr):
    
            g.trace("nullGui",attr)
            return nullObject()
    #@-node:AGP.20250415230112.2956: nullGui.__getattr__
    #@+node:AGP.20250415230112.2957:nullGui.createLeoFrame
    def createLeoFrame(self,title):
        
        """Create a null Leo Frame."""
        
        # print 'nullGui.createLeoFrame'
        
        gui = self
        self.lastFrame = leoFrame.nullFrame(title,gui)
        return self.lastFrame
    #@-node:AGP.20250415230112.2957:nullGui.createLeoFrame
    #@+node:AGP.20250415230112.2958:attachLeoIcon
    def attachLeoIcon (self,w):
        
        pass
    #@-node:AGP.20250415230112.2958:attachLeoIcon
    #@+node:AGP.20250415230112.2959:createRootWindow
    def createRootWindow(self):
        pass
    #@-node:AGP.20250415230112.2959:createRootWindow
    #@+node:AGP.20250415230112.2960:finishCreate
    def finishCreate (self):
        pass
    #@-node:AGP.20250415230112.2960:finishCreate
    #@+node:AGP.20250415230112.2961:runMainLoop
    def runMainLoop(self):
    
        """Run the gui's main loop."""
        
        if self.script:
            frame = self.lastFrame
            g.app.log = frame.log
            # g.es("Start of batch script...\n")
            self.lastFrame.c.executeScript(script=self.script)
            # g.es("\nEnd of batch script")
        
        # Getting here will terminate Leo.
    #@-node:AGP.20250415230112.2961:runMainLoop
    #@-node:AGP.20250415230112.2954:Birth & death
    #@+node:AGP.20250415230112.2962:oops
    def oops(self):
            
        """Default do-nothing method for nullGui class.
        
        It is NOT an error to use this method."""
        
        # It is not usually an error to call methods of this class.
        # However, this message is useful when writing gui plugins.
        if 0:
            g.trace("nullGui",g.callers())
    #@-node:AGP.20250415230112.2962:oops
    #@-others
#@-node:AGP.20250415230112.2953:class nullGui (leoGui)
#@+node:AGP.20250415230112.2963:class unitTestGui (leoGui)
class unitTestGui(leoGui):
    
    """gui class for use by unit tests."""
    
    #@    @+others
    #@+node:AGP.20250415230112.2964: test.gui.__init__& destroySelf
    def __init__ (self,dict,trace=False):
        
        self.dict = dict
        self.oldGui = g.app.gui
        self.trace=trace
        
        # Init the base class
        leoGui.__init__ (self,"unitTestGui")
    
        g.app.gui = self
        
    def destroySelf (self):
        
        g.app.gui = self.oldGui
    #@-node:AGP.20250415230112.2964: test.gui.__init__& destroySelf
    #@+node:AGP.20250415230112.2965:dialogs (unitTestGui)
    def runAboutLeoDialog(self,c,version,theCopyright,url,email):
        return self.simulateDialog("aboutLeoDialog")
        
    def runAskLeoIDDialog(self):
        return self.simulateDialog("leoIDDialog")
    
    def runAskOkDialog(self,c,title,message=None,text="Ok"):
        return self.simulateDialog("okDialog","Ok")
    
    def runAskOkCancelNumberDialog(self,c,title,message):
        return self.simulateDialog("numberDialog",-1)
        
    def runOpenFileDialog(self,title,filetypes,defaultextension,multiple=False):
        return self.simulateDialog("openFileDialog")
    
    def runSaveFileDialog(self,initialfile,title,filetypes,defaultextension):
        return self.simulateDialog("saveFileDialog")
    
    def runAskYesNoDialog(self,c,title,message=None):
        return self.simulateDialog("yesNoDialog","no")
    
    def runAskYesNoCancelDialog(self,c,title,
        message=None,yesMessage="Yes",noMessage="No",defaultButton="Yes"):
        return self.simulateDialog("yesNoCancelDialog","cancel")
    #@-node:AGP.20250415230112.2965:dialogs (unitTestGui)
    #@+node:AGP.20250415230112.2966:dummy routines
    def getindex (self,body,index):
        return 0, 0
    
    def get_focus (self,frame):
        pass
    
    def set_focus (self,c,widget):
        pass
    
    def getInsertPoint (self,t):
        return 0
    
    def getSelectionRange (self,t):
        return None
    
    def getTextSelection (self,t,sort=True):
        return 0, 0
    
    def setInsertPoint (self,t,pos):
        pass
    
    def setSelectionRange (self,t,start,end,insert='sel.end'):
        pass
    
    def toGuiIndex (self,s,w,index):
        return 0
    
    def toPythonIndex (self,s,w,index):
        return 0
    #@-node:AGP.20250415230112.2966:dummy routines
    #@+node:AGP.20250415230112.2967:oops
    def oops(self):
        
        g.trace("unitTestGui",g.callers())
        
        if 0: # Fail the unit test.
            assert 0,"call to undefined method in unitTestMethod class"
    #@-node:AGP.20250415230112.2967:oops
    #@+node:AGP.20250415230112.2968:simulateDialog
    def simulateDialog (self,key,defaultVal=None):
        
        val = self.dict.get(key,defaultVal)
    
        if self.trace:
            print key, val
    
        return val
    #@-node:AGP.20250415230112.2968:simulateDialog
    #@-others
#@-node:AGP.20250415230112.2963:class unitTestGui (leoGui)
#@-others
#@-node:AGP.20250415230112.2925:@thin leoGui.py
#@-leo
