#@+leo-ver=4-thin
#@+node:AGP.20250415230112.2797:@thin leoFrame.py
"""The base classes for all Leo Windows, their body, log and tree panes, key bindings and menus.

These classes should be overridden to create frames for a particular gui."""

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import leoColor
import leoMenu
import leoUndo

import re

#@<< About handling events >>
#@+node:AGP.20250415230112.2798:<< About handling events >>
#@+at
# Leo must handle events or commands that change the text in the outline or 
# body
# panes. We must ensure that headline and body text corresponds to the vnode 
# and
# tnode corresponding to presently selected outline, and vice versa. For 
# example,
# when the user selects a new headline in the outline pane, we must ensure 
# that:
# 
# 1) All vnodes and tnodes have up-to-date information and
# 
# 2) the body pane is loaded with the correct data.
# 
# Early versions of Leo attempted to satisfy these conditions when the user
# switched outline nodes. Such attempts never worked well; there were too many
# special cases. Later versions of Leo use a much more direct approach: every
# keystroke in the body pane updates the presently selected tnode immediately.
# 
# The leoTree class contains all the event handlers for the tree pane, and the
# leoBody class contains the event handlers for the body pane. The following
# convenience methods exists:
# 
# - body.updateBody & tree.updateBody:
#     Called by k.masterCommand after any keystroke not handled by 
# k.masterCommand.
#     These are suprising complex.
# 
# - body.bodyChanged & tree.headChanged:
#     Called by commands throughout Leo's core that change the body or 
# headline.
#     These are thin wrappers for updateBody and updateTree.
#@-at
#@-node:AGP.20250415230112.2798:<< About handling events >>
#@nl

#@+others
#@+node:AGP.20250415230112.2799:class leoBody
class leoBody:
    
    """The base class for the body pane in Leo windows."""
    
    #@    @+others
    #@+node:AGP.20250415230112.2800:leoBody.__init__
    def __init__ (self,frame,parentFrame):
    
        self.frame = frame
        self.c = frame.c
        self.forceFullRecolorFlag = False
        frame.body = self
        
        # May be overridden in subclasses...
        self.bodyCtrl = self
        self.numberOfEditors = 1
        
        # Must be overridden in subclasses...
        self.colorizer = None
    #@-node:AGP.20250415230112.2800:leoBody.__init__
    #@+node:AGP.20250415230112.2801:oops
    def oops (self):
        
        g.trace("leoBody oops:", g.callers(), "should be overridden in subclass")
    #@-node:AGP.20250415230112.2801:oops
    #@+node:AGP.20250415230112.2802:leoBody.setFontFromConfig
    def setFontFromConfig (self,w=None):
        
        self.oops()
    #@-node:AGP.20250415230112.2802:leoBody.setFontFromConfig
    #@+node:AGP.20250415230112.2803:Must be overriden in subclasses
    def createBindings (self,w=None):
        self.oops()
    
    def createControl (self,frame,parentFrame,p):
        self.oops()
        
    def initialRatios (self):
        self.oops()
        
    def onBodyChanged (self,undoType,oldSel=None,oldText=None,oldYview=None):
        self.oops()
        
    def setBodyFontFromConfig (self):
        self.oops()
    #@+node:AGP.20250415230112.2804:Bounding box (Tk spelling)
    def bbox(self,index):
    
        self.oops()
    #@-node:AGP.20250415230112.2804:Bounding box (Tk spelling)
    #@+node:AGP.20250415230112.2805:Color tags (Tk spelling)
    def tag_add (self,tagName,index1,index2):
    
        self.oops()
    
    def tag_bind (self,tagName,event,callback):
    
        self.oops()
    
    def tag_configure (self,colorName,**keys):
    
        self.oops()
    
    def tag_delete(self,tagName):
    
        self.oops()
    
    def tag_remove (self,tagName,index1,index2):
        self.oops()
    #@-node:AGP.20250415230112.2805:Color tags (Tk spelling)
    #@+node:AGP.20250415230112.2806:Configuration (Tk spelling)
    def cget(self,*args,**keys):
        
        self.oops()
        
    def configure (self,*args,**keys):
        
        self.oops()
    #@-node:AGP.20250415230112.2806:Configuration (Tk spelling)
    #@+node:AGP.20250415230112.2807:Editors
    def addEditor (self,event=None):
        pass
        
    def cycleEditorFocus (self,event=None):
        pass
        
    def deleteEditor (self,event=None):
        pass
        
    def selectMainEditor (self,p):
        pass
        
    def setEditorColors (self,bg,fg):
        pass
        
    def updateEditors (self):
        pass
    #@-node:AGP.20250415230112.2807:Editors
    #@+node:AGP.20250415230112.2808:Focus
    def hasFocus (self):
        
        self.oops()
        
    def setFocus (self):
        
        self.oops()
    #@-node:AGP.20250415230112.2808:Focus
    #@+node:AGP.20250415230112.2809:Height & width
    def getBodyPaneHeight (self):
        
        self.oops()
    
    def getBodyPaneWidth (self):
        
        self.oops()
    #@-node:AGP.20250415230112.2809:Height & width
    #@+node:AGP.20250415230112.2810:Idle time...
    def scheduleIdleTimeRoutine (self,function,*args,**keys):
    
        self.oops()
    #@-node:AGP.20250415230112.2810:Idle time...
    #@+node:AGP.20250415230112.2811:Indices
    def adjustIndex (self,index,offset):
        self.oops()
        
    def compareIndices(self,i,rel,j):
        self.oops()
        
    def convertRowColumnToIndex (self,row,column):
        self.oops()
        
    def convertIndexToRowColumn (self,index):
        self.oops()
        
    def getImageIndex (self,image):
        self.oops()
        
    def getPythonInsertionPoint (self,t=None,s=None):
        self.oops()
        
    def setPythonInsertionPoint (self,i,t=None,s=None):
        self.oops()
    #@-node:AGP.20250415230112.2811:Indices
    #@+node:AGP.20250415230112.2812:Insert point
    def getBeforeInsertionPoint (self):
        self.oops()
    
    def getInsertionPoint (self):
        self.oops()
        
    def getCharAtInsertPoint (self):
        self.oops()
    
    def getCharBeforeInsertPoint (self):
        self.oops()
        
    def makeInsertPointVisible (self):
        self.oops()
        
    def setInsertionPoint (self,index):
        self.oops()
    
    def setInsertionPointToEnd (self):
        self.oops()
        
    def setInsertPointToStartOfLine (self,lineNumber): # zero-based line number
        self.oops()
    #@-node:AGP.20250415230112.2812:Insert point
    #@+node:AGP.20250415230112.2813:Menus
    def bind (self,*args,**keys):
        
        self.oops()
    #@-node:AGP.20250415230112.2813:Menus
    #@+node:AGP.20250415230112.2814:Selection
    def deleteTextSelection (self):
        self.oops()
        
    def getSelectedText (self):
        self.oops()
        
    def getTextSelection (self,sort=True):
        self.oops()
        
    def hasTextSelection (self):
        self.oops()
        
    def selectAllText (self,event=None):
        self.oops()
        
    def setTextSelection (self,i,j=None,insert='sel.end'):
        self.oops()
    #@-node:AGP.20250415230112.2814:Selection
    #@+node:AGP.20250415230112.2815:Text
    #@+node:AGP.20250415230112.2816:delete...
    def deleteAllText(self):
        self.oops()
    
    def deleteCharacter (self,index):
        self.oops()
        
    def deleteLastChar (self):
        self.oops()
        
    def deleteLine (self,lineNumber): # zero based line number.
        self.oops()
        
    def deleteLines (self,line1,numberOfLines): # zero based line numbers.
        self.oops()
        
    def deleteRange (self,index1,index2):
        self.oops()
    #@-node:AGP.20250415230112.2816:delete...
    #@+node:AGP.20250415230112.2817:get...
    def getAllText (self):
        self.oops()
        
    def getCharAtIndex (self,index):
        self.oops()
        
    def getInsertLines (self):
        self.oops()
        return None,None,None
        
    def getSelectionAreas (self):
        self.oops()
        return None,None,None
        
    def getSelectionLines (self):
        self.oops()
        return None,None,None
        
    def getTextRange (self,index1,index2):
        self.oops()
    #@-node:AGP.20250415230112.2817:get...
    #@+node:AGP.20250415230112.2818:Insert...
    def insertAtInsertPoint (self,s):
        
        self.oops()
        
    def insertAtEnd (self,s):
        
        self.oops()
        
    def insertAtStartOfLine (self,lineNumber,s):
        
        self.oops()
    #@-node:AGP.20250415230112.2818:Insert...
    #@+node:AGP.20250415230112.2819:setSelectionAreas
    def setSelectionAreas (self,before,sel,after):
        self.oops()
    #@-node:AGP.20250415230112.2819:setSelectionAreas
    #@-node:AGP.20250415230112.2815:Text
    #@+node:AGP.20250415230112.2820:Visibility & scrolling
    def makeIndexVisible (self,index):
        self.oops()
        
    def setFirstVisibleIndex (self,index):
        self.oops()
        
    def getYScrollPosition (self):
        self.oops()
        
    def setYScrollPosition (self,scrollPosition):
        self.oops()
        
    def scrollUp (self):
        self.oops()
        
    def scrollDown (self):
        self.oops()
    #@-node:AGP.20250415230112.2820:Visibility & scrolling
    #@-node:AGP.20250415230112.2803:Must be overriden in subclasses
    #@+node:AGP.20250415230112.2821:Coloring
    # It's weird to have the tree class be responsible for coloring the body pane!
    
    def getColorizer(self):
        
        return self.colorizer
    
    def recolor_now(self,p,incremental=False):
    
        self.colorizer.colorize(p.copy(),incremental)
    
    
        
    def updateSyntaxColorer(self,p):
        
        return self.colorizer.updateSyntaxColorer(p.copy())
    #@-node:AGP.20250415230112.2821:Coloring
    #@-others
#@-node:AGP.20250415230112.2799:class leoBody
#@+node:AGP.20250415230112.2822:class leoFrame
class leoFrame:
    
    """The base class for all Leo windows."""
    
    instances = 0
    
    #@    @+others
    #@+node:AGP.20250415230112.2823:  leoFrame.__init__
    def __init__ (self,gui):
        
        self.c = None # Must be created by subclasses.
        self.title = None # Must be created by subclasses.
        self.gui = gui
        
        # Objects attached to this frame.
        self.colorPanel = None 
        self.comparePanel = None
        self.findPanel = None
        self.fontPanel = None
        self.isNullFrame = False
        self.keys = None
        self.menu = None
        self.miniBufferWidget = None # New in 4.4.
        self.prefsPanel = None
        self.statusLine = None
        self.useMiniBufferWidget = False # New in 4.4
    
        # Gui-independent data
        self.componentsDict = {} # Keys are names, values are componentClass instances.
        self.es_newlines = 0 # newline count for this log stream
        self.openDirectory = ""
        self.requestRecolorFlag = False
        self.saved=False # True if ever saved
        self.splitVerticalFlag,self.ratio, self.secondary_ratio = True,0.5,0.5 # Set by initialRatios later.
        self.startupWindow=False # True if initially opened window
        self.stylesheet = None # The contents of <?xml-stylesheet...?> line.
        self.tab_width = 0 # The tab width in effect in this pane.
    #@-node:AGP.20250415230112.2823:  leoFrame.__init__
    #@+node:AGP.20250415230112.2824: Must be defined in subclasses
    #@+node:AGP.20250415230112.2825: gui-dependent commands
    # In the Edit menu...
    def OnCopy  (self,event=None): self.oops()
    def OnCut   (self,event=None): self.oops()
    def OnPaste (self,event=None): self.oops()
    
    def OnCutFromMenu  (self,event=None):     self.oops()
    def OnCopyFromMenu (self,event=None):     self.oops()
    def OnPasteFromMenu (self,event=None):    self.oops()
    
    def copyText  (self,event=None): self.oops()
    def cutText   (self,event=None): self.oops()
    def pasteText (self,event=None,middleButton=False): self.oops()
    
    def abortEditLabelCommand (self,event=None): self.oops()
    def endEditLabelCommand   (self,event=None): self.oops()
    def insertHeadlineTime    (self,event=None): self.oops()
    
    # Expanding and contracting panes.
    def contractPane         (self,event=None): self.oops()
    def expandPane           (self,event=None): self.oops()
    def contractBodyPane     (self,event=None): self.oops()
    def contractLogPane      (self,event=None): self.oops()
    def contractOutlinePane  (self,event=None): self.oops()
    def expandLogPane        (self,event=None): self.oops()
    def fullyExpandBodyPane  (self,event=None): self.oops()
    def fullyExpandLogPane   (self,event=None): self.oops()
    def fullyExpandPane      (self,event=None): self.oops()
    def fullyExpandOutlinePane (self,event=None): self.oops()
    def hideBodyPane         (self,event=None): self.oops()
    def hideLogPane          (self,event=None): self.oops()
    def hidePane             (self,event=None): self.oops()
    def hideOutlinePane      (self,event=None): self.oops()
        
    expandBodyPane = contractOutlinePane
    expandOutlinePane = contractBodyPane
    
    # In the Window menu...
    def cascade              (self,event=None): self.oops()
    def equalSizedPanes      (self,event=None): self.oops()
    def hideLogWindow        (self,event=None): self.oops()
    def minimizeAll          (self,event=None): self.oops()
    def resizeToScreen       (self,event=None): self.oops()
    def toggleActivePane     (self,event=None): self.oops()
    def toggleSplitDirection (self,event=None): self.oops()
    
    # In help menu...
    def leoHelp (self,event=None): self.oops()
    #@-node:AGP.20250415230112.2825: gui-dependent commands
    #@+node:AGP.20250415230112.2826:bringToFront, deiconify, lift & update
    def bringToFront (self):
        
        self.oops()
    
    def deiconify (self):
        
        self.oops()
        
    def lift (self):
        
        self.oops()
        
    def update (self):
        
        self.oops()
    #@-node:AGP.20250415230112.2826:bringToFront, deiconify, lift & update
    #@+node:AGP.20250415230112.2827:config stuff...
    #@+node:AGP.20250415230112.2828:resizePanesToRatio
    def resizePanesToRatio (self,ratio,secondary_ratio):
        
        pass
    #@-node:AGP.20250415230112.2828:resizePanesToRatio
    #@+node:AGP.20250415230112.2829:setInitialWindowGeometry
    def setInitialWindowGeometry (self):
        
        self.oops()
    #@-node:AGP.20250415230112.2829:setInitialWindowGeometry
    #@+node:AGP.20250415230112.2830:setTopGeometry
    def setTopGeometry (self,w,h,x,y,adjustSize=True):
        
        self.oops()
    #@-node:AGP.20250415230112.2830:setTopGeometry
    #@-node:AGP.20250415230112.2827:config stuff...
    #@+node:AGP.20250415230112.2831:leoFrame.unpack/repack...
    def repackBodyPane (self):
        
        self.oops()
    
    def repackFrameWidgets (self):
        
        self.oops()
        
    def unpackFrameWidgets (self):
        
        self.oops()
        
    def unpackBodyPane (self):
        
        self.oops()
    #@-node:AGP.20250415230112.2831:leoFrame.unpack/repack...
    #@-node:AGP.20250415230112.2824: Must be defined in subclasses
    #@+node:AGP.20250415230112.2832:setTabWidth
    def setTabWidth (self,w):
        
        # Subclasses may override this to affect drawing.
        self.tab_width = w
    #@-node:AGP.20250415230112.2832:setTabWidth
    #@+node:AGP.20250415230112.2833:getTitle & setTitle
    def getTitle (self):
        return self.title
        
    def setTitle (self,title):
        self.title = title
    #@-node:AGP.20250415230112.2833:getTitle & setTitle
    #@+node:AGP.20250415230112.2834:initialRatios
    def initialRatios (self):
        
        c = self.c
    
        s = c.config.get("initial_splitter_orientation","string")
        verticalFlag = s == None or (s != "h" and s != "horizontal")
    
        if verticalFlag:
            r = c.config.getRatio("initial_vertical_ratio")
            if r == None or r < 0.0 or r > 1.0: r = 0.5
            r2 = c.config.getRatio("initial_vertical_secondary_ratio")
            if r2 == None or r2 < 0.0 or r2 > 1.0: r2 = 0.8
        else:
            r = c.config.getRatio("initial_horizontal_ratio")
            if r == None or r < 0.0 or r > 1.0: r = 0.3
            r2 = c.config.getRatio("initial_horizontal_secondary_ratio")
            if r2 == None or r2 < 0.0 or r2 > 1.0: r2 = 0.8
    
        # g.trace(r,r2)
        return verticalFlag,r,r2
    #@-node:AGP.20250415230112.2834:initialRatios
    #@+node:AGP.20250415230112.2835:longFileName & shortFileName
    def longFileName (self):
    
        return self.c.mFileName
        
    def shortFileName (self):
    
        return g.shortFileName(self.c.mFileName)
    #@-node:AGP.20250415230112.2835:longFileName & shortFileName
    #@+node:AGP.20250415230112.2836:oops
    def oops(self):
        
        print "leoFrame oops:", g.callers(), "should be overridden in subclass"
    #@-node:AGP.20250415230112.2836:oops
    #@+node:AGP.20250415230112.2837:promptForSave
    def promptForSave (self):
        
        """Prompt the user to save changes.
        
        Return True if the user vetos the quit or save operation."""
        
        c = self.c
        name = g.choose(c.mFileName,c.mFileName,self.title)
        theType = g.choose(g.app.quitting, "quitting?", "closing?")
    
        answer = g.app.gui.runAskYesNoCancelDialog(c,
            "Confirm",
            'Save changes to %s before %s' % (name,theType))
            
        # print answer
        if answer == "cancel":
            return True # Veto.
        elif answer == "no":
            return False # Don't save and don't veto.
        else:
            if not c.mFileName:
                #@            << Put up a file save dialog to set mFileName >>
                #@+node:AGP.20250415230112.2838:<< Put up a file save dialog to set mFileName >>
                # Make sure we never pass None to the ctor.
                if not c.mFileName:
                    c.mFileName = ""
                
                c.mFileName = g.app.gui.runSaveFileDialog(
                    initialfile = c.mFileName,
                    title="Save",
                    filetypes=[("Leo files", "*.leo")],
                    defaultextension=".leo")
                c.bringToFront()
                #@-node:AGP.20250415230112.2838:<< Put up a file save dialog to set mFileName >>
                #@nl
            if c.mFileName:
                ok = c.fileCommands.save(c.mFileName)
                return not ok # New in 4.2: Veto if the save did not succeed.
            else:
                return True # Veto.
    #@-node:AGP.20250415230112.2837:promptForSave
    #@+node:AGP.20250415230112.2839:scanForTabWidth
    # Similar to code in scanAllDirectives.
    
    def scanForTabWidth (self,p):
    
        c = self.c ; w = c.tab_width
    
        for p in p.self_and_parents_iter():
            s = p.v.t.bodyString
            theDict = g.get_directives_dict(s)
            #@        << set w and break on @tabwidth >>
            #@+node:AGP.20250415230112.2840:<< set w and break on @tabwidth >>
            if theDict.has_key("tabwidth"):
                
                val = g.scanAtTabwidthDirective(s,theDict,issue_error_flag=False)
                if val and val != 0:
                    w = val
                    break
            #@-node:AGP.20250415230112.2840:<< set w and break on @tabwidth >>
            #@nl
    
        c.frame.setTabWidth(w)
    #@-node:AGP.20250415230112.2839:scanForTabWidth
    #@+node:AGP.20250415230112.2841:xWantsFocus
    # For compatibility with old scripts.
    # Using the commander methods directly is recommended.
    
    def bodyWantsFocus(self):
        return self.c.bodyWantsFocus()
       
    def headlineWantsFocus(self,p):
        return self.c.headlineWantsFocus(p)
        
    def logWantsFocus(self):
        return self.c.logWantsFocus()
        
    def minibufferWantsFocus(self):
        return self.c.minibufferWantsFocus()
    #@-node:AGP.20250415230112.2841:xWantsFocus
    #@-others
#@-node:AGP.20250415230112.2822:class leoFrame
#@+node:AGP.20250415230112.2842:class leoLog
class leoLog:
    
    """The base class for the log pane in Leo windows."""
    
    #@    @+others
    #@+node:AGP.20250415230112.2843:leoLog.__init__
    def __init__ (self,frame,parentFrame):
        
        self.frame = frame
        if frame: # 7/16/05: Allow no commander for Null logs.
            self.c = frame.c
        else:
            self.c = None
        self.enabled = True
        self.newlines = 0
        self.isNull = False
    
        # Note: self.logCtrl is None for nullLog's.
        self.logCtrl = self.createControl(parentFrame)
        #self.setFontFromConfig()
        #self.setColorFromConfig()
    #@-node:AGP.20250415230112.2843:leoLog.__init__
    #@+node:AGP.20250415230112.2844:leoLog.configure
    def configure (self,*args,**keys):
        
        self.oops()
    #@-node:AGP.20250415230112.2844:leoLog.configure
    #@+node:AGP.20250415230112.2845:leoLog.configureBorder
    def configureBorder(self,border):
        
        self.oops()
    #@-node:AGP.20250415230112.2845:leoLog.configureBorder
    #@+node:AGP.20250415230112.2846:leoLog.createControl
    def createControl (self,parentFrame):
        
        self.oops()
    #@-node:AGP.20250415230112.2846:leoLog.createControl
    #@+node:AGP.20250415230112.2847:leoLog.enable & disable
    def enable (self,enabled=True):
        
        self.enabled = enabled
        
    def disable (self):
        
        self.enabled = False
    #@-node:AGP.20250415230112.2847:leoLog.enable & disable
    #@+node:AGP.20250415230112.2848:leoLog.oops
    def oops (self):
        
        print "leoLog oops:", g.callers(), "should be overridden in subclass"
    #@-node:AGP.20250415230112.2848:leoLog.oops
    #@+node:AGP.20250415230112.2849:leoLog.setFontFromConfig & setColorFromConfig
    def setFontFromConfig (self):
        
        self.oops()
        
    def setColorFromConfig (self):
        
        self.oops()
    #@-node:AGP.20250415230112.2849:leoLog.setFontFromConfig & setColorFromConfig
    #@+node:AGP.20250415230112.2850:leoLog.onActivateLog
    def onActivateLog (self,event=None):
    
        self.c.setLog()
    #@-node:AGP.20250415230112.2850:leoLog.onActivateLog
    #@+node:AGP.20250415230112.2851:leoLog.put & putnl
    # All output to the log stream eventually comes here.
    
    def put (self,s,color=None,tabName='Log'):
        self.oops()
    
    def putnl (self,tabName='Log'):
        self.oops()
    #@-node:AGP.20250415230112.2851:leoLog.put & putnl
    #@-others
#@-node:AGP.20250415230112.2842:class leoLog
#@+node:AGP.20250415230112.2852:class leoTree
# This would be useful if we removed all the tree redirection routines.
# However, those routines are pretty ingrained into Leo...

class leoTree:
    
    """The base class for the outline pane in Leo windows."""
    
    #@    @+others
    #@+node:AGP.20250415230112.2853:  tree.__init__ (base class)
    def __init__ (self,frame):
        
        self.frame = frame
        self.c = frame.c
    
        self.edit_text_dict = {}
            # New in 3.12: keys vnodes, values are edit_widget (Tk.Text widgets)
            # New in 4.2: keys are vnodes, values are pairs (p,Tk.Text).
        
        # "public" ivars: correspond to setters & getters.
        self._editPosition = None
        self.redrawCount = 0 # For traces
    #@-node:AGP.20250415230112.2853:  tree.__init__ (base class)
    #@+node:AGP.20250415230112.2854: Must be defined in subclasses
    #@+node:AGP.20250415230112.2855:Colors & Fonts
    def setColorFromConfig (self):
        self.oops()
    
    def getFont(self):
        self.oops()
        
    def setFont(self,font=None,fontName=None):
        self.oops()
        
    def setFontFromConfig (self):
        self.oops()
    #@-node:AGP.20250415230112.2855:Colors & Fonts
    #@+node:AGP.20250415230112.2856:Drawing
    def drawIcon(self,v,x=None,y=None):
        self.oops()
    
    def redraw_now(self,scroll=True):
        self.oops()
    #@-node:AGP.20250415230112.2856:Drawing
    #@+node:AGP.20250415230112.2857:Edit label
    def editLabel(self,v,selectAll=False):
        
        self.oops()
    
    def endEditLabel(self):
        self.oops()
    
    def setEditLabelState(self,v,selectAll=False):
        
        self.oops()
    #@-node:AGP.20250415230112.2857:Edit label
    #@+node:AGP.20250415230112.2858:Scrolling
    def scrollTo(self,p):
        self.oops()
        
    idle_scrollTo = scrollTo # For compatibility.
    #@-node:AGP.20250415230112.2858:Scrolling
    #@+node:AGP.20250415230112.2859:Selecting
    def select(self,p,updateBeadList=True):
        
        self.oops()
    #@-node:AGP.20250415230112.2859:Selecting
    #@+node:AGP.20250415230112.2860:Tree operations
    def expandAllAncestors(self,v):
        
        self.oops()
    #@-node:AGP.20250415230112.2860:Tree operations
    #@-node:AGP.20250415230112.2854: Must be defined in subclasses
    #@+node:AGP.20250415230112.2861:Getters/Setters (tree)
    def getEditTextDict(self,v):
        # New in 4.2: the default is an empty list.
        return self.edit_text_dict.get(v,[])
    
    def editPosition(self):
        return self._editPosition
    
    def setEditPosition(self,p):
        self._editPosition = p
    #@-node:AGP.20250415230112.2861:Getters/Setters (tree)
    #@+node:AGP.20250415230112.2862:oops
    def oops(self):
        
        print "leoTree oops:", g.callers(), "should be overridden in subclass"
    #@-node:AGP.20250415230112.2862:oops
    #@+node:AGP.20250415230112.2863:tree.OnIconDoubleClick (@url)
    def OnIconDoubleClick (self,p):
    
        # Note: "icondclick" hooks handled by vnode callback routine.
    
        c = self.c
        s = p.headString().strip()
        if g.match_word(s,0,"@url"):
            url = s[4:].strip()
            if url.lstrip().startswith('--'):
                # Get the url from the first body line.
                lines = p.bodyString().split('\n')
                url = lines and lines[0] or ''
            else:
                #@            << stop the url after any whitespace >>
                #@+node:AGP.20250415230112.2864:<< stop the url after any whitespace  >>
                # For safety, the URL string should end at the first whitespace, unless quoted.
                # This logic is also found in the UNL plugin so we don't have to change the 'unl1' hook.
                
                url = url.replace('\t',' ')
                
                # Strip quotes.
                i = -1
                if url and url[0] in ('"',"'"):
                    i = url.find(url[0],1)
                    if i > -1:
                        url = url[1:i]
                
                if i == -1:
                    # Not quoted or no matching quote.
                    i = url.find(' ')
                    if i > -1:
                        if 0: # No need for a warning.  Assume everything else is a comment.
                            g.es("ignoring characters after space in url:"+url[i:])
                            g.es("use %20 instead of spaces")
                        url = url[:i]
                #@-node:AGP.20250415230112.2864:<< stop the url after any whitespace  >>
                #@nl
            if not g.doHook("@url1",c=c,p=p,v=p,url=url):
                # Note: the UNL plugin has its own notion of what a good url is.
                #@            << check the url; return if bad >>
                #@+node:AGP.20250415230112.2865:<< check the url; return if bad >>
                if not url or len(url) == 0:
                    g.es("no url following @url")
                    return
                    
                #@+at 
                #@nonl
                # A valid url is (according to D.T.Hein):
                # 
                # 3 or more lowercase alphas, followed by,
                # one ':', followed by,
                # one or more of: (excludes !"#;<>[\]^`|)
                #   $%&'()*+,-./0-9:=?@A-Z_a-z{}~
                # followed by one of: (same as above, except no minus sign or 
                # comma).
                #   $%&'()*+/0-9:=?@A-Z_a-z}~
                #@-at
                #@@c
                
                urlPattern = "[a-z]{3,}:[\$-:=?-Z_a-z{}~]+[\$-+\/-:=?-Z_a-z}~]"
                
                # 4/21/03: Add http:// if required.
                if not re.match('^([a-z]{3,}:)',url):
                    url = 'http://' + url
                if not re.match(urlPattern,url):
                    g.es("invalid url: "+url)
                    return
                #@-node:AGP.20250415230112.2865:<< check the url; return if bad >>
                #@nl
                #@            << pass the url to the web browser >>
                #@+node:AGP.20250415230112.2866:<< pass the url to the web browser >>
                #@+at 
                #@nonl
                # Most browsers should handle the following urls:
                #   ftp://ftp.uu.net/public/whatever.
                #   http://localhost/MySiteUnderDevelopment/index.html
                #   file://home/me/todolist.html
                #@-at
                #@@c
                
                try:
                    import os
                    os.chdir(g.app.loadDir)
                    if g.match(url,0,"file:") and url[-4:]==".leo":
                        ok,frame = g.openWithFileName(url[5:],c)
                    else:
                        import webbrowser
                        
                        # Mozilla throws a weird exception, then opens the file!
                        try: webbrowser.open(url)
                        except: pass
                except:
                    g.es("exception opening " + url)
                    g.es_exception()
                #@nonl
                #@-node:AGP.20250415230112.2866:<< pass the url to the web browser >>
                #@nl
            g.doHook("@url2",c=c,p=p,v=p)
    
        return 'break' # 11/19/06
    #@nonl
    #@-node:AGP.20250415230112.2863:tree.OnIconDoubleClick (@url)
    #@+node:AGP.20250415230112.2867:tree.enableDrawingAfterException
    def enableDrawingAfterException (self):
        pass
    #@-node:AGP.20250415230112.2867:tree.enableDrawingAfterException
    #@-others
#@-node:AGP.20250415230112.2852:class leoTree
#@+node:AGP.20250415230112.2868:class nullBody
class nullBody (leoBody):
    
    #@    @+others
    #@+node:AGP.20250415230112.2869: nullBody.__init__
    def __init__ (self,frame,parentFrame):
        
        leoBody.__init__ (self,frame,parentFrame) # Init the base class.
    
        self.insertPoint = 0
        self.selection = 0,0
        self.s = "" # The body text
        
        self.colorizer = leoColor.nullColorizer(self.c)
    #@-node:AGP.20250415230112.2869: nullBody.__init__
    #@+node:AGP.20250415230112.2870:Utils (internal use)
    #@+node:AGP.20250415230112.2871:findStartOfLine
    def findStartOfLine (self,lineNumber):
        
        lines = g.splitLines(self.s)
        i = 0 ; index = 0
        for line in lines:
            if i == lineNumber: break
            i += 1
            index += len(line)
        return index
    #@-node:AGP.20250415230112.2871:findStartOfLine
    #@+node:AGP.20250415230112.2872:scanToStartOfLine
    def scanToStartOfLine (self,i):
        
        if i <= 0:
            return 0
            
        assert(self.s[i] != '\n')
        
        while i >= 0:
            if self.s[i] == '\n':
                return i + 1
        
        return 0
    #@-node:AGP.20250415230112.2872:scanToStartOfLine
    #@+node:AGP.20250415230112.2873:scanToEndOfLine
    def scanToEndOfLine (self,i):
        
        if i >= len(self.s):
            return len(self.s)
            
        assert(self.s[i] != '\n')
        
        while i < len(self.s):
            if self.s[i] == '\n':
                return i - 1
        
        return i
    #@-node:AGP.20250415230112.2873:scanToEndOfLine
    #@-node:AGP.20250415230112.2870:Utils (internal use)
    #@+node:AGP.20250415230112.2874:Must be overriden in subclasses
    def createBindings (self,w=None):
        self.oops()
    
    def createControl (self,frame,parentFrame):
        self.oops()
        
    def initialRatios (self):
        self.oops()
        
    def onBodyChanged (self,undoType,oldSel=None,oldText=None,oldYview=None):
        self.oops()
        
    def setBodyFontFromConfig (self):
        self.oops()
    #@+node:AGP.20250415230112.2875:Bounding box
    def bbox(self,index):
        return (0,0)
    #@-node:AGP.20250415230112.2875:Bounding box
    #@+node:AGP.20250415230112.2876:Color tags
    def tag_add (self,tagName,index1,index2):
        pass
    
    def tag_bind (self,tagName,event,callback):
        pass
    
    def tag_configure (self,colorName,**keys):
        pass
    
    def tag_delete(self,tagName):
        pass
    
    def tag_remove (self,tagName,index1,index2):
        pass
    #@-node:AGP.20250415230112.2876:Color tags
    #@+node:AGP.20250415230112.2877:Configuration
    def cget(self,*args,**keys):
        pass
        
    def configure (self,*args,**keys):
        pass
    #@-node:AGP.20250415230112.2877:Configuration
    #@+node:AGP.20250415230112.2878:Focus
    def hasFocus (self):
        return True
        
    def setFocus (self):
        pass
    #@-node:AGP.20250415230112.2878:Focus
    #@+node:AGP.20250415230112.2879:Height & width (use dummy values...)
    def getBodyPaneHeight (self):
        
        return 500
    
    def getBodyPaneWidth (self):
    
        return 600
    #@-node:AGP.20250415230112.2879:Height & width (use dummy values...)
    #@+node:AGP.20250415230112.2880:Idle time...
    def scheduleIdleTimeRoutine (self,function,*args,**keys):
    
        g.trace()
    #@-node:AGP.20250415230112.2880:Idle time...
    #@+node:AGP.20250415230112.2881:Indices
    def adjustIndex (self,index,offset):
        return index + offset
        
    def compareIndices(self,i,rel,j):
    
        return eval("%d %s %d" % (i,rel,j))
        
    def convertRowColumnToIndex (self,row,column):
        
        # Probably not used.
        n = self.findStartOfLine(row)
        g.trace(n + column)
        return n + column
        
    def convertIndexToRowColumn (self,index):
        
        # Probably not used.
        g.trace(index)
        return index
        
    def getImageIndex (self,image):
        self.oops()
    #@-node:AGP.20250415230112.2881:Indices
    #@+node:AGP.20250415230112.2882:Insert point
    def getBeforeInsertionPoint (self):
        return self.insertPoint - 1
    
    def getInsertionPoint (self):
        return self.insertPoint
        
    def getCharAtInsertPoint (self):
        try: return self.s[self.insertPoint]
        except: return None
    
    def getCharBeforeInsertPoint (self):
        try: return self.s[self.insertPoint - 1]
        except: return None
        
    def makeInsertPointVisible (self):
        pass
        
    def setInsertionPoint (self,index):
        self.insertPoint = index
    
    def setInsertionPointToEnd (self):
        self.insertPoint = len(self.s)
        
    def setInsertPointToStartOfLine (self,lineNumber): # zero-based line number
        self.insertPoint = self.findStartOfLine(lineNumber)
    #@-node:AGP.20250415230112.2882:Insert point
    #@+node:AGP.20250415230112.2883:Menus
    def bind (self,*args,**keys):
        pass
    #@-node:AGP.20250415230112.2883:Menus
    #@+node:AGP.20250415230112.2884:Selection
    def deleteTextSelection (self):
        i,j = self.selection
        self.s = self.s[:i] + self.s[j:]
        
    def getSelectedText (self):
        i,j = self.selection
        g.trace(self.s[i:j])
        return self.s[i:j]
        
    def getTextSelection (self,sort=True):
        # g.trace(self.selection)
        return self.selection
        
    def hasTextSelection (self):
        i,j = self.selection
        return i != j
        
    def selectAllText (self,event=None):
        self.selection = 0,len(self.s)
        
    def setTextSelection (self,i,j=None,insert='sel.end'):
        if i is None:
            self.selection = 0,0
        elif j is None:
            self.selection = i # a tuple
        else:
            self.selection = i,j
    #@-node:AGP.20250415230112.2884:Selection
    #@+node:AGP.20250415230112.2885:Text
    #@+node:AGP.20250415230112.2886:delete...
    def deleteAllText(self):
        self.insertPoint = 0
        self.selection = 0,0
        self.s = "" # The body text
    
    def deleteCharacter (self,index):
        self.s = self.s[:index] + self.s[index+1:]
        
    def deleteLastChar (self):
        if self.s:
            del self.s[-1]
        
    def deleteLine (self,lineNumber): # zero based line number.
        self.deleteLines(lineNumber,1)
        
    def deleteLines (self,lineNumber,numberOfLines): # zero based line numbers.
        n1 = self.findStartOfLine(lineNumber)
        n2 = self.findStartOfLine(lineNumber+numberOfLines+1)
        if n2:
            self.s = self.s[:n1] + self.s[n2:]
        else:
            self.s = self.s[:n1]
        
    def deleteRange (self,index1,index2):
        del self.s[index1:index2]
    #@-node:AGP.20250415230112.2886:delete...
    #@+node:AGP.20250415230112.2887:get...
    def getAllText (self):
        return g.toUnicode(self.s,g.app.tkEncoding)
        
    def getCharAtIndex (self,index):
        
        try:
            s = self.s[index]
            return g.toUnicode(s,g.app.tkEncoding)
        except: return None
        
    def getTextRange (self,index1,index2):
    
        s = self.s[index1:index2]
        return g.toUnicode(s,g.app.tkEncoding)
    #@+node:AGP.20250415230112.2888:getInsertLines
    def getInsertLines (self):
        
        """Return before,ins,after where:
            
        before is all the lines before the line containing the insert point.
        sel is the line containing the insert point.
        after is all the lines after the line containing the insert point.
        
        All lines end in a newline, except possibly the last line."""
    
        # DTHEIN 18-JAN-2004: NOTE: overridden by leoTkinterBody!!!!!!
        
        n1 = self.scanToStartOfLine(self.insertPoint)
        n2 = self.scanToEndOfLine(self.insertPoint)
        
        before = self.s[:n1]
        ins    = self.s[n1:n2+1] # 12/18/03: was sel(!)
        after  = self.s[n2+1:]
    
        before = g.toUnicode(before,g.app.tkEncoding)
        ins    = g.toUnicode(ins,   g.app.tkEncoding)
        after  = g.toUnicode(after ,g.app.tkEncoding)
    
        return before,ins,after
    #@-node:AGP.20250415230112.2888:getInsertLines
    #@+node:AGP.20250415230112.2889:getSelectionAreas
    def getSelectionAreas (self):
        
        """Return before,sel,after where:
            
        before is the text before the selected text
        (or the text before the insert point if no selection)
        sel is the selected text (or "" if no selection)
        after is the text after the selected text
        (or the text after the insert point if no selection)"""
        
        if not self.hasTextSelection():
            n1,n2 = self.insertPoint,self.insertPoint
        else:
            n2,n2 = self.selection
    
        before = self.s[:n1]
        sel    = self.s[n1:n2+1]
        after  = self.s[n2+1:]
        
        before = g.toUnicode(before,g.app.tkEncoding)
        sel    = g.toUnicode(sel,   g.app.tkEncoding)
        after  = g.toUnicode(after ,g.app.tkEncoding)
        return before,sel,after
    #@-node:AGP.20250415230112.2889:getSelectionAreas
    #@+node:AGP.20250415230112.2890:getSelectionLines (nullBody)
    def getSelectionLines (self):
        
        """Return before,sel,after where:
            
        before is all the lines before the selected text
        (or the text before the insert point if no selection)
        sel is the selected text (or the line containing the insert point if no selection)
        after is all lines after the selected text
        (or the text after the insert point if no selection)"""
        
        # At present, called only by c.getBodyLines.
        if not self.hasTextSelection():
            start,end = self.insertPoint,self.insertPoint
        else:
            start,end = self.selection
    
        n1 = self.scanToStartOfLine(start)
        n2 = self.scanToEndOfLine(end)
    
        before = self.s[:n1]
        sel    = self.s[n1:n2] # 12/8/03 was n2+1
        after  = self.s[n2+1:]
    
        before = g.toUnicode(before,g.app.tkEncoding)
        sel    = g.toUnicode(sel,   g.app.tkEncoding)
        after  = g.toUnicode(after ,g.app.tkEncoding)
        
        g.trace(n1,n2)
        return before,sel,after
    #@-node:AGP.20250415230112.2890:getSelectionLines (nullBody)
    #@-node:AGP.20250415230112.2887:get...
    #@+node:AGP.20250415230112.2891:Insert...
    def insertAtInsertPoint (self,s):
        
        i = self.insertPoint
        self.s = self.s[:i] + s + self.s[i:]
        
    def insertAtEnd (self,s):
        
        self.s = self.s + s
        
    def insertAtStartOfLine (self,lineNumber,s):
        
        i = self.findStartOfLine(lineNumber)
        self.s = self.s[:i] + s + self.s[i:]
    #@-node:AGP.20250415230112.2891:Insert...
    #@+node:AGP.20250415230112.2892:setSelectionAreas (nullFrame)
    def setSelectionAreas (self,before,sel,after):
        
        if before is None: before = ""
        if sel    is None: sel = ""
        if after  is None: after = ""
        
        self.s = before + sel + after
        
        self.selection = len(before), len(before) + len(sel)
    #@-node:AGP.20250415230112.2892:setSelectionAreas (nullFrame)
    #@-node:AGP.20250415230112.2885:Text
    #@+node:AGP.20250415230112.2893:Visibility & scrolling
    def makeIndexVisible (self,index):
        pass
        
    def setFirstVisibleIndex (self,index):
        pass
        
    def getYScrollPosition (self):
        return 0
        
    def setYScrollPosition (self,scrollPosition):
        pass
        
    def scrollUp (self):
        pass
        
    def scrollDown (self):
        pass
    #@-node:AGP.20250415230112.2893:Visibility & scrolling
    #@-node:AGP.20250415230112.2874:Must be overriden in subclasses
    #@+node:AGP.20250415230112.2894:setColorFromConfig & setFontFromConfig
    def setFontFromConfig (self):
        pass
        
    def setColorFromConfig (self):
        pass
    #@-node:AGP.20250415230112.2894:setColorFromConfig & setFontFromConfig
    #@+node:AGP.20250415230112.2895:oops
    def oops(self):
    
        g.trace("nullBody:", g.callers())
        pass
    #@-node:AGP.20250415230112.2895:oops
    #@-others
#@-node:AGP.20250415230112.2868:class nullBody
#@+node:AGP.20250415230112.2896:class nullFrame
class nullFrame (leoFrame):
    
    """A null frame class for tests and batch execution."""
    
    #@    @+others
    #@+node:AGP.20250415230112.2897: ctor
    def __init__ (self,title,gui,useNullUndoer=False):
    
        leoFrame.__init__(self,gui) # Init the base class.
        assert(self.c is None)
        
        self.isNullFrame = True
        self.title = title
        self.useNullUndoer = useNullUndoer
        
        # Default window position.
        self.w = 600
        self.h = 500
        self.x = 40
        self.y = 40
    #@-node:AGP.20250415230112.2897: ctor
    #@+node:AGP.20250415230112.2898:deiconfy, lift, update
    def deiconify (self):
        pass
        
    def lift (self):
        pass
        
    def update (self):
        pass
    #@-node:AGP.20250415230112.2898:deiconfy, lift, update
    #@+node:AGP.20250415230112.2899:destroySelf
    def destroySelf (self):
        
        pass
    #@-node:AGP.20250415230112.2899:destroySelf
    #@+node:AGP.20250415230112.2900:finishCreate
    def finishCreate(self,c):
    
        self.c = c
    
        # Create do-nothing component objects.
        self.tree = nullTree(frame=self)
        self.body = nullBody(frame=self,parentFrame=None)
        self.log  = nullLog (frame=self,parentFrame=None)
        self.menu = leoMenu.nullMenu(frame=self)
        
        assert(c.undoer)
        if self.useNullUndoer:
            c.undoer = leoUndo.nullUndoer(c)
    #@-node:AGP.20250415230112.2900:finishCreate
    #@+node:AGP.20250415230112.2901:get_window_info
    def get_window_info (self):
    
        """Return the window information."""
        
        # g.trace(self.w,self.h,self.x,self.y)
    
        return self.w,self.h,self.x,self.y
    #@-node:AGP.20250415230112.2901:get_window_info
    #@+node:AGP.20250415230112.2902:lift
    #@-node:AGP.20250415230112.2902:lift
    #@+node:AGP.20250415230112.2903:oops
    def oops(self):
        
        g.trace("nullFrame:", g.callers(5))
    #@-node:AGP.20250415230112.2903:oops
    #@+node:AGP.20250415230112.2904:setInitialWindowGeometry
    def setInitialWindowGeometry (self):
        pass
    #@-node:AGP.20250415230112.2904:setInitialWindowGeometry
    #@+node:AGP.20250415230112.2905:setTopGeometry
    def setTopGeometry (self,w,h,x,y,adjustSize=True):
        
        self.w = w
        self.h = h
        self.x = x
        self.y = y
    #@-node:AGP.20250415230112.2905:setTopGeometry
    #@-others
#@-node:AGP.20250415230112.2896:class nullFrame
#@+node:AGP.20250415230112.2906:class nullLog
class nullLog (leoLog):
    
    #@    @+others
    #@+node:AGP.20250415230112.2907:nullLog.__init__
    def __init__ (self,frame=None,parentFrame=None):
            
        # Init the base class.
        leoLog.__init__(self,frame,parentFrame)
        self.isNull = True
    #@-node:AGP.20250415230112.2907:nullLog.__init__
    #@+node:AGP.20250415230112.2908:createControl
    def createControl (self,parentFrame):
        
        return None
    #@-node:AGP.20250415230112.2908:createControl
    #@+node:AGP.20250415230112.2909:oops
    def oops(self):
    
        g.trace("nullLog:", g.callers())
    #@-node:AGP.20250415230112.2909:oops
    #@+node:AGP.20250415230112.2910:put and putnl (nullLog)
    def put (self,s,color=None,tabName='Log'):
        if self.enabled:
            # g.trace('nullLog',s)
            g.rawPrint(s)
    
    def putnl (self,tabName='Log'):
        if self.enabled:
            g.rawPrint("")
    #@-node:AGP.20250415230112.2910:put and putnl (nullLog)
    #@+node:AGP.20250415230112.2911:tabs
    def clearTab        (self,tabName): pass
    def createTab       (self,tabName): pass
    def deleteTab       (self,tabName): pass
    def getSelectedTab          (self): pass
    def lowerTab        (self,tabName): pass
    def raiseTab        (self,tabName): pass
    def renameTab (self,oldName,newName): pass
    def selectTab       (self,tabName): pass
    def setTabBindings  (self,tabName): pass
    #@-node:AGP.20250415230112.2911:tabs
    #@+node:AGP.20250415230112.2912:setColorFromConfig & setFontFromConfig
    def setFontFromConfig (self):
        pass
        
    def setColorFromConfig (self):
        pass
    #@-node:AGP.20250415230112.2912:setColorFromConfig & setFontFromConfig
    #@-others
#@-node:AGP.20250415230112.2906:class nullLog
#@+node:AGP.20250415230112.2913:class nullTree
class nullTree (leoTree):
    
    #@    @+others
    #@+node:AGP.20250415230112.2914: nullTree.__init__
    def __init__ (self,frame):
        
        leoTree.__init__(self,frame) # Init the base class.
        
        assert(self.frame)
        self.font = None
        self.fontName = None
        self.canvas = None
    #@-node:AGP.20250415230112.2914: nullTree.__init__
    #@+node:AGP.20250415230112.2915:oops
    def oops(self):
            
        # It is not an error to call this routine...
        g.trace("nullTree:", g.callers())
        pass
    #@-node:AGP.20250415230112.2915:oops
    #@+node:AGP.20250415230112.2916:Dummy operations...
    #@+node:AGP.20250415230112.2917:Drawing
    def beginUpdate (self):
        pass
        
    def endUpdate (self,flag,scroll=False):
        pass
    
    def enableDrawingAfterException (self):
        pass
    
    def drawIcon(self,v,x=None,y=None):
        pass
    
    def redraw_now(self,scroll=True):
        pass
    #@-node:AGP.20250415230112.2917:Drawing
    #@+node:AGP.20250415230112.2918:Edit label
    def editLabel(self,v,selectAll=False):
    
        pass
    
    def endEditLabel(self):
        pass
    
    def setEditLabelState(self,v,selectAll=False):
        
        pass
    #@-node:AGP.20250415230112.2918:Edit label
    #@+node:AGP.20250415230112.2919:Scrolling
    def scrollTo(self,p):
        pass
        
    idle_scrollTo = scrollTo # For compatibility.
    #@-node:AGP.20250415230112.2919:Scrolling
    #@+node:AGP.20250415230112.2920:Tree operations
    def expandAllAncestors(self,v):
    
        pass
    #@-node:AGP.20250415230112.2920:Tree operations
    #@+node:AGP.20250415230112.2921:edit_widget
    def edit_widget (self,c,p):
        
        self.oops()
    #@nonl
    #@-node:AGP.20250415230112.2921:edit_widget
    #@-node:AGP.20250415230112.2916:Dummy operations...
    #@+node:AGP.20250415230112.2922:getFont & setFont
    def getFont(self):
    
        return self.font
        
    def setFont(self,font=None,fontName=None):
    
        self.font = font
        self.fontName = fontName
    #@-node:AGP.20250415230112.2922:getFont & setFont
    #@+node:AGP.20250415230112.2923:setColorFromConfig & setFontFromConfig
    def setColorFromConfig (self):
        pass
        
    def setFontFromConfig (self):
        pass
    #@-node:AGP.20250415230112.2923:setColorFromConfig & setFontFromConfig
    #@+node:AGP.20250415230112.2924:select
    def select(self,p,updateBeadList=True):
        
        self.c.setCurrentPosition(p)
    
        self.frame.scanForTabWidth(p)
    #@-node:AGP.20250415230112.2924:select
    #@-others
#@-node:AGP.20250415230112.2913:class nullTree
#@-others
#@-node:AGP.20250415230112.2797:@thin leoFrame.py
#@-leo
