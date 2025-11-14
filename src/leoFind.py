#@+leo-ver=4-thin
#@+node:AGP.20250415230112.2739:@thin leoFind.py
#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import re

#@<< Theory of operation of find/change >>
#@+node:AGP.20250415230112.2740:<< Theory of operation of find/change >>
#@+at 
#@nonl
# The find and change commands are tricky; there are many details that must be 
# handled properly. This documentation describes the leo.py code. Previous 
# versions of Leo used an inferior scheme.  The following principles govern 
# the leoFind class:
# 
# 1. Find and Change commands initialize themselves using only the state of 
# the present Leo window. In particular, the Find class must not save internal 
# state information from one invocation to the next. This means that when the 
# user changes the nodes, or selects new text in headline or body text, those 
# changes will affect the next invocation of any Find or Change command. 
# Failure to follow this principle caused all kinds of problems in the Borland 
# and Macintosh codes. There is one exception to this rule: we must remember 
# where interactive wrapped searches start. This principle simplifies the code 
# because most ivars do not persist. However, each command must ensure that 
# the Leo window is left in a state suitable for restarting the incremental 
# (interactive) Find and Change commands. Details of initialization are 
# discussed below.
# 
# 2. The Find and Change commands must not change the state of the outline or 
# body pane during execution. That would cause severe flashing and slow down 
# the commands a great deal. In particular, c.selectVnode and c.editPosition 
# methods must not be called while looking for matches.
# 
# 3. When incremental Find or Change commands succeed they must leave the Leo 
# window in the proper state to execute another incremental command. We 
# restore the Leo window as it was on entry whenever an incremental search 
# fails and after any Find All and Change All command.
# 
# Initialization involves setting the self.c, self.p, self.in_headline, 
# self.wrapping and self.s_ctrl ivars. Setting self.in_headline is tricky; we 
# must be sure to retain the state of the outline pane until initialization is 
# complete. Initializing the Find All and Change All commands is much easier 
# because such initialization does not depend on the state of the Leo window.
# 
# Using Tk.Text widgets for both headlines and body text results in a huge 
# simplification of the code. Indeed, the searching code does not know whether 
# it is searching headline or body text. The search code knows only that 
# self.s_ctrl is a Tk.Text widget that contains the text to be searched or 
# changed and the insert and sel Tk attributes of self.search_text indicate 
# the range of text to be searched. Searching headline and body text 
# simultaneously is complicated. The selectNextPosition() method handles the 
# many details involved by setting self.s_ctrl and its insert and sel 
# attributes.
#@-at
#@-node:AGP.20250415230112.2740:<< Theory of operation of find/change >>
#@nl

class leoFind:

    """The base class for Leo's Find commands."""

    #@    @+others
    #@+node:AGP.20250415230112.2741:leoFind.__init__
    def __init__ (self,c,title=None):
    
        self.c = c
        
        # Spell checkers use this class, so we can't always compute a title.
        if title:
            self.title = title
        else:
            #@        << compute self.title >>
            #@+node:AGP.20250415230112.2742:<< compute self.title >>
            if not c.mFileName:
                s = "untitled"
            else:
                path,s = g.os_path_split(c.mFileName)
                
            self.title = "Find/Change for %s" %  s
            #@-node:AGP.20250415230112.2742:<< compute self.title >>
            #@nl
    
        #@    << init the gui-independent ivars >>
        #@+node:AGP.20250415230112.2743:<< init the gui-independent ivars >>
        self.wrapPosition = None
        self.onlyPosition = None
        self.find_text = ""
        self.change_text = ""
        self.unstick = False
        
        #@+at
        # New in 4.3:
        # - These are the names of leoFind ivars. (no more _flag hack).
        # - There are no corresponding commander ivars to keep in synch 
        # (hurray!)
        # - These ivars are inited (in the subclass by init) when this class 
        # is created.
        # - These ivars are updated (in the subclass by update_ivars) just 
        # before doing any find.
        #@-at
        #@@c
        
        #@<< do dummy initialization to keep Pychecker happy >>
        #@+node:AGP.20250415230112.2744:<< do dummy initialization to keep Pychecker happy >>
        if 1:
            self.batch = None
            self.clone_find_all = None
            self.ignore_case = None
            self.node_only = None
            self.pattern_match = None
            self.search_headline = None
            self.search_body = None
            self.suboutline_only = None
            self.mark_changes = None
            self.mark_finds = None
            self.reverse = None
            self.script_search = None
            self.script_change = None
            self.selection_only = None
            self.wrap = None
            self.whole_word = None
            self.collapse = None
        #@-node:AGP.20250415230112.2744:<< do dummy initialization to keep Pychecker happy >>
        #@nl
        
        self.intKeys = [
            "batch","ignore_case", "node_only",
            "pattern_match", "search_headline", "search_body",
            "suboutline_only", "mark_changes", "mark_finds", "reverse",
            "script_search","script_change","selection_only",
            "wrap", "whole_word","collapse"
        ]
        
        self.newStringKeys = ["radio-find-type", "radio-search-scope"]
        
        # Ivars containing internal state...
        self.c = None # The commander for this search.
        self.clone_find_all = False
        self.p = None # The position being searched.  Never saved between searches!
        self.in_headline = False # True: searching headline text.
        self.s_ctrl = None # The search text for this search.
        self.searched_widget = None #the currently searched widget agp
        self.wrapping = False # True: wrapping is enabled.
            # This is _not_ the same as self.wrap for batch searches.
        
        #@+at 
        #@nonl
        # Initializing a wrapped search is tricky.  The search() method will 
        # fail if p==wrapPosition and pos >= wrapPos.  selectNextPosition() 
        # will fail if p == wrapPosition.  We set wrapPos on entry, before the 
        # first search.  We set wrapPosition in selectNextPosition after the 
        # first search fails.  We also set wrapPosition on exit if the first 
        # search suceeds.
        #@-at
        #@@c
        
        self.wrapPosition = None # The start of wrapped searches: persists between calls.
        self.onlyPosition = None # The starting node for suboutline-only searches.
        self.wrapPos = None # The starting position of the wrapped search: persists between calls.
        self.errors = 0
        self.selStart = self.selEnd = None # For selection-only searches.
        #@-node:AGP.20250415230112.2743:<< init the gui-independent ivars >>
        #@nl
    #@-node:AGP.20250415230112.2741:leoFind.__init__
    #@+node:AGP.20250415230112.2745:Top Level Buttons
    #@+node:AGP.20250415230112.2746:changeAllButton
    # The user has pushed the "Change All" button from the find panel.
    
    def changeAllButton(self):
    
        c = self.c
        self.setup_button()
        c.clearAllVisited() # Clear visited for context reporting.
    
        if self.script_change:
            self.doChangeAllScript()
        elif self.selection_only:
            self.change()
        else:
            self.changeAll()
    #@-node:AGP.20250415230112.2746:changeAllButton
    #@+node:AGP.20250415230112.2747:changeButton
    # The user has pushed the "Change" button from the find panel.
    
    def changeButton(self):
    
        self.setup_button()
    
        if self.script_change:
            self.doChangeScript()
        else:
            self.change()
    #@-node:AGP.20250415230112.2747:changeButton
    #@+node:AGP.20250415230112.2748:changeThenFindButton
    # The user has pushed the "Change Then Find" button from the find panel.
    
    def changeThenFindButton(self):
    
        self.setup_button()
    
        if self.script_change:
            self.doChangeScript()
            if self.script_search:
                self.doFindScript()
            else:
                self.findNext()
        else:
            if self.script_search:
                self.change()
                self.doFindScript()
            else:
                self.changeThenFind()
    #@-node:AGP.20250415230112.2748:changeThenFindButton
    #@+node:AGP.20250415230112.2749:findAllButton
    # The user has pushed the "Find All" button from the find panel.
    
    def findAllButton(self):
    
        c = self.c
        self.setup_button()
        c.clearAllVisited() # Clear visited for context reporting.
    
        if self.script_search:
            self.doFindAllScript()
        elif self.selection_only:
            self.findNext()
        else:
            self.findAll()
    #@-node:AGP.20250415230112.2749:findAllButton
    #@+node:AGP.20250415230112.2750:findButton
    # The user has pushed the "Find" button from the find panel.
    
    def findButton(self):
    
        self.setup_button()
    
        if self.script_search:
            self.doFindScript()
        else:
            self.findNext()
    #@-node:AGP.20250415230112.2750:findButton
    #@+node:AGP.20250415230112.2751:setup_button
    # Initializes a search when a button is pressed in the Find panel.
    
    def setup_button(self):
        #print "setup_button"
        c = self.c
        self.p = c.currentPosition()
    
        c.bringToFront()
        if 0: # We _must_ retain the editing status for incremental searches!
            c.endEditing()
    
        self.update_ivars()
        self.adjust_ivars()
    #@-node:AGP.20250415230112.2751:setup_button
    #@-node:AGP.20250415230112.2745:Top Level Buttons
    #@+node:AGP.20250415230112.2752:Top Level Commands
    #@+node:AGP.20250415230112.2753:changeCommand
    # The user has selected the "Replace" menu item.
    
    def changeCommand(self,c):
    
        self.setup_command()
    
        if self.script_search:
            self.doChangeScript()
        else:
            self.change()
    #@-node:AGP.20250415230112.2753:changeCommand
    #@+node:AGP.20250415230112.2754:changeThenFindCommand
    # The user has pushed the "Change Then Find" button from the Find menu.
    
    def changeThenFindCommand(self,c):
    
        self.setup_command()
    
        if self.script_search:
            self.doChangeScript()
            self.doFindScript()
        else:
            self.changeThenFind()
    #@-node:AGP.20250415230112.2754:changeThenFindCommand
    #@+node:AGP.20250415230112.2755:dismiss: defined in subclass class
    def dismiss (self):
        pass
    #@-node:AGP.20250415230112.2755:dismiss: defined in subclass class
    #@+node:AGP.20250415230112.2756:findNextCommand
    # The user has selected the "Find Next" menu item.
    
    def findNextCommand(self,c):
    
        self.setup_command()
    
        if self.script_search:
            self.doFindScript()
        else:
            self.findNext()
    #@-node:AGP.20250415230112.2756:findNextCommand
    #@+node:AGP.20250415230112.2757:findPreviousCommand
    # The user has selected the "Find Previous" menu item.
    
    def findPreviousCommand(self,c):
    
        self.setup_command()
    
        self.reverse = not self.reverse
    
        if self.script_search:
            self.doFindScript()
        else:
            self.findNext()
    
        self.reverse = not self.reverse
    #@-node:AGP.20250415230112.2757:findPreviousCommand
    #@+node:AGP.20250415230112.2758:handleUserClick
    def handleUserClick (self,p):
        
        """Reset suboutline-only search when the user clicks a headline."""
        
        try:
            if self.c and self.suboutline_only:
                # g.trace(p)
                self.onlyPosition = p.copy()
        except: pass
    #@-node:AGP.20250415230112.2758:handleUserClick
    #@+node:AGP.20250415230112.2759:setup_command
    # Initializes a search when a command is invoked from the menu.
    def setup_command(self):
    
        if 0: # We _must_ retain the editing status for incremental searches!
            self.c.endEditing()
    
        self.update_ivars()
        self.adjust_ivars()
    #@-node:AGP.20250415230112.2759:setup_command
    #@-node:AGP.20250415230112.2752:Top Level Commands
    #@+node:AGP.20250415230112.2760:Find/change utils
    #@+node:AGP.20250415230112.2761:find.adjust_ivars
    def adjust_ivars (self):
        
        '''New in 4.3.
        
        Adjust ivars, particularly the find and change text.
        This is called just before executing a command and
        just after calling update_ivars.
        
        Plugins may replace this code as desired.'''
        
        if 0:
            # The TkFind class now removes tailing newlines.
        
            ft = self.find_text
            if not ft: return
        
            # Remove a trailing newline unless that is all there is.
            if len(ft) > 1 and ft[-1] in ('\n','\r'):
                ft = ft[:-1]
                self.adjust_find_text(ft)
                if 0:
                    g.es('before:',repr(self.find_text))
                    g.es(' after:',repr(ft))
                self.find_text = ft
        
            return
    #@-node:AGP.20250415230112.2761:find.adjust_ivars
    #@+node:AGP.20250415230112.2762:batchChange (sets start of change-all group)
    #@+at 
    #@nonl
    # This routine performs a single batch change operation, updating the head 
    # or body string of p and leaving the result in s_ctrl.  We update the 
    # body if we are changing the body text of c.currentVnode().
    # 
    # s_ctrl contains the found text on entry and contains the changed text on 
    # exit.  pos and pos2 indicate the selection.  The selection will never be 
    # empty. NB: we can not assume that self.p is visible.
    #@-at
    #@@c
    
    def batchChange (self,pos1,pos2):
    
        c = self.c ; u = c.undoer
        p = self.p ; st = self.s_ctrl ; gui = g.app.gui
        # Replace the selection with self.change_text
        if gui.compareIndices(st,pos1, ">", pos2):
            pos1,pos2=pos2,pos1
        gui.replaceSelectionRangeWithText(st,pos1,pos2,self.change_text)
        s = gui.getAllText(st)
        # Update the selection.
        insert=g.choose(self.reverse,pos1,pos1+'+'+str(len(self.change_text))+'c')
        gui.setSelectionRange(st,insert,insert)
        gui.setInsertPoint(st,insert)
        # Update the node
        if self.in_headline:
            #@        << change headline >>
            #@+node:AGP.20250415230112.2763:<< change headline >>
            if len(s) > 0 and s[-1]=='\n': s = s[:-1]
            
            if s != p.headString():
                
                undoData = u.beforeChangeNodeContents(p)
            
                p.initHeadString(s)
                if self.mark_changes:
                    p.setMarked()
                p.setDirty()
                if not c.isChanged():
                    c.setChanged(True)
                
                u.afterChangeNodeContents(p,'Change Headline',undoData)
            #@-node:AGP.20250415230112.2763:<< change headline >>
            #@nl
        else:
            #@        << change body >>
            #@+node:AGP.20250415230112.2764:<< change body >>
            if len(s) > 0 and s[-1]=='\n': s = s[:-1]
            
            if s != p.bodyString():
                
                undoData = u.beforeChangeNodeContents(p)
            
                c.setBodyString(p,s)
                if self.mark_changes:
                    p.setMarked()
                p.setDirty()
                if not c.isChanged():
                    c.setChanged(True)
                 
                u.afterChangeNodeContents(p,'Change Body',undoData)
            #@-node:AGP.20250415230112.2764:<< change body >>
            #@nl
    #@-node:AGP.20250415230112.2762:batchChange (sets start of change-all group)
    #@+node:AGP.20250415230112.2765:change
    def change(self,event=None):
    
        if self.checkArgs():
            self.initInHeadline()
            self.changeSelection()
    #@-node:AGP.20250415230112.2765:change
    #@+node:AGP.20250415230112.2766:changeAll (sets end of change-all group)
    def changeAll(self):
    
        c = self.c ; u = c.undoer ; undoType = 'Change All'
        current = c.currentPosition()
        st = self.s_ctrl ; gui = g.app.gui
        if not self.checkArgs(): return
        self.initInHeadline()
        saveData = self.save()
        self.initBatchCommands()
        count = 0
        c.beginUpdate()
        try: # In update...
            u.beforeChangeGroup(current,undoType)
            while 1:
                pos1, pos2 = self.findNextMatch()
                if not pos1: break
                count += 1
                self.batchChange(pos1,pos2)
                line = gui.getLineContainingIndex(st,pos1)
                g.es(self.p.headString()+"->",newline=False)
                self.printLine(line,allFlag=True)
            p = c.currentPosition()
            u.afterChangeGroup(p,undoType,reportFlag=True)
            g.es("changed: %d instances" % (count))
        finally:
            c.endUpdate()
            self.restore(saveData)
    #@-node:AGP.20250415230112.2766:changeAll (sets end of change-all group)
    #@+node:AGP.20250415230112.2767:changeSelection
    # Replace selection with self.change_text.
    # If no selection, insert self.change_text at the cursor.
    
    def changeSelection(self):
    
        c = self.c ; p = self.p ; gui = g.app.gui
        # g.trace(self.in_headline)
        t = g.choose(self.in_headline,c.edit_widget(p),c.frame.bodyCtrl)
        oldSel = sel = gui.getTextSelection(t)
        if sel and len(sel) == 2:
            start,end = sel
            if start == end:
                sel = None
        if not sel or len(sel) != 2:
            g.es("No text selected")
            return False
    
        # Replace the selection in _both_ controls.
        start,end = oldSel
        change_text = self.change_text
        
        # Perform regex substitutions of \1, \2, ...\9 in the change text.
        if self.pattern_match and self.match_obj:
            groups = self.match_obj.groups()
            if groups:
                change_text = self.makeRegexSubs(change_text,groups)
        change_text = change_text.replace('\\n','\n').replace('\\t','\t')
                    
        gui.replaceSelectionRangeWithText(t,          start,end,change_text)
        gui.replaceSelectionRangeWithText(self.s_ctrl,start,end,change_text)
    
        # Update the selection for the next match.
        gui.setSelectionRangeWithLength(t,start,len(self.change_text))
        c.widgetWantsFocus(t)
    
        # No redraws here: they would destroy the headline selection.
        c.beginUpdate()
        try:
            if self.mark_changes:
                p.setMarked()
            if self.in_headline:
                c.frame.tree.onHeadChanged(p,'Change')
            else:
                c.frame.body.onBodyChanged('Change',oldSel=oldSel)
        finally:
            c.endUpdate(False)
            c.frame.tree.drawIcon(p) # redraw only the icon.
         
        return True
    #@+node:AGP.20250415230112.2768:makeRegexSubs
    def makeRegexSubs(self,s,groups):
        
        '''Carefully substitute group[i-1] for \i strings in s.
        The group strings may contain \i strings: they are *not* substituted.'''
        
        digits = '123456789'
        result = [] ; n = len(s)
        i = j = 0 # s[i:j] is the text between \i markers.
        while j < n:
            k = s.find('\\',j)
            if k == -1 or k + 1 >= n:
                break
            j = k + 1 ; ch = s[j]
            if ch in digits:
                j += 1
                result.append(s[i:k]) # Append up to \i
                i = j
                gn = int(ch)-1
                if gn < len(groups):
                    result.append(groups[gn]) # Append groups[i-1]
                else:
                    result.append('\\%s' % ch) # Append raw '\i'
        result.append(s[i:])
        return ''.join(result)
    #@-node:AGP.20250415230112.2768:makeRegexSubs
    #@-node:AGP.20250415230112.2767:changeSelection
    #@+node:AGP.20250415230112.2769:changeThenFind
    def changeThenFind(self):
    
        if not self.checkArgs():
            return
    
        self.initInHeadline()
        if self.changeSelection():
            self.findNext(False) # don't reinitialize
    #@-node:AGP.20250415230112.2769:changeThenFind
    #@+node:AGP.20250415230112.2770:doChange...Script
    def doChangeScript (self):
    
        g.app.searchDict["type"] = "change"
        self.runChangeScript()
    
    def doChangeAllScript (self):
    
        """The user has just pressed the Change All button with script-change box checked.
    
        N.B. Only this code is executed."""
    
        g.app.searchDict["type"] = "changeAll"
        while 1:
            self.runChangeScript()
            if not g.app.searchDict.get("continue"):
                break
    
    def runChangeScript (self):
    
        try:
            assert(self.script_change)
            exec self.change_text in {} # Use {} to get a pristine environment.
        except:
            g.es("exception executing change script")
            g.es_exception(full=False)
            g.app.searchDict["continue"] = False # 2/1/04
    #@-node:AGP.20250415230112.2770:doChange...Script
    #@+node:AGP.20250415230112.2771:doFind...Script
    def doFindScript (self):
    
        g.app.searchDict["type"] = "find"
        self.runFindScript()
    
    def doFindAllScript (self):
    
        """The user has just pressed the Find All button with script-find radio button checked.
    
        N.B. Only this code is executed."""
    
        g.app.searchDict["type"] = "findAll"
        while 1:
            self.runFindScript()
            if not g.app.searchDict.get("continue"):
                break
    
    def runFindScript (self):
    
        try:
            exec self.find_text in {} # Use {} to get a pristine environment.
        except:
            g.es("exception executing find script")
            g.es_exception(full=False)
            g.app.searchDict["continue"] = False # 2/1/04
    #@-node:AGP.20250415230112.2771:doFind...Script
    #@+node:AGP.20250415230112.2772:findAll
    def findAll(self):
    
        c = self.c ; t = self.s_ctrl ; u = c.undoer
        gui = g.app.gui ; undoType = 'Clone Find All'
        if not self.checkArgs():
            return
        self.initInHeadline()
        data = self.save()
        self.initBatchCommands()
        count = 0 ; clones = []
        while 1:
            pos, newpos = self.findNextMatch()
            if not pos: break
            count += 1
            line = gui.getLineContainingIndex(t,pos)
            g.es(self.p.headString()+"->",newline=False)
            self.printLine(line,allFlag=True)
            if self.clone_find_all and self.p.v.t not in clones:
                if not clones:
                    #@                << create the found node and begin the undo group >>
                    #@+node:AGP.20250415230112.2773:<< create the found node and begin the undo group >>
                    u.beforeChangeGroup(c.currentPosition(),undoType)
                    
                    undoData = u.beforeInsertNode(c.currentPosition())
                    
                    oldRoot = c.rootPosition()
                    found = oldRoot.insertAfter()
                    found.moveToRoot(oldRoot)
                    c.setHeadString(found,'Found: ' + self.find_text)
                    
                    u.afterInsertNode(found,undoType,undoData,dirtyVnodeList=[])
                    #@-node:AGP.20250415230112.2773:<< create the found node and begin the undo group >>
                    #@nl
                #@            << create a clone of p under the find node >>
                #@+node:AGP.20250415230112.2774:<< create a clone of p under the find node >>
                clones.append(self.p.v.t)
                undoData = u.beforeCloneNode(self.p)
                q = self.p.clone()
                q.moveToLastChildOf(found)
                u.afterCloneNode(q,undoType,undoData,dirtyVnodeList=[])
                #@-node:AGP.20250415230112.2774:<< create a clone of p under the find node >>
                #@nl
        if self.clone_find_all and clones:
            c.setRootPosition(c.findRootPosition(found)) # New in 4.4.2.
            u.afterChangeGroup(found,undoType,reportFlag=True) 
            c.selectPosition(found) # Recomputes root.
            c.setChanged(True)
              
        c.redraw_now()
        g.es("found: %d matches" % (count))
        self.restore(data)
    #@-node:AGP.20250415230112.2772:findAll
    #@+node:AGP.20250415230112.2775:findNext
    def findNext(self,initFlag=True):
    
        c = self.c
        if not self.checkArgs():
            return
    
        if initFlag:
            self.initInHeadline()
            data = self.save()
            self.initInteractiveCommands()
        else:
            data = self.save()
            
            #update the insert point of s_ctrl in case user changed it - agp
            #pos = gui.getInsertPoint(self.searched_widget)
            #gui.setInsertPoint(self.s_ctrl,pos)
           
        #print "findnext"
        pos, newpos = self.findNextMatch()
        
        if pos:
            self.showSuccess(pos,newpos)
            return True #agp
        else:
            #if self.wrapping:
            #    g.es("end of wrapped search")
            
            g.es("not found: " + "'" + self.find_text + "'")
            self.restore(data)
            
            return False #agp
    #@-node:AGP.20250415230112.2775:findNext
    #@+node:AGP.20250415230112.2776:findNextMatch
    # Resumes the search where it left off.
    # The caller must call set_first_incremental_search or set_first_batch_search.
    
    def findNextMatch(self):
    
        c = self.c
    
        if not self.search_headline and not self.search_body:
            return None, None
    
        if len(self.find_text) == 0:
            return None, None
    
        p = self.p
        
        self.wrapped  = False
        
        while p:
            pos, newpos = self.search()
            
            if pos:
                if self.mark_finds:
                    p.setMarked()
                    c.frame.tree.drawIcon(p) # redraw only the icon.
                
                return pos, newpos
            elif self.errors:
                return None,None # Abort the search.
            
            
            p = self.p = self.selectNextPosition()
            
                
        
        return None, None
    #@-node:AGP.20250415230112.2776:findNextMatch
    #@+node:AGP.20250415230112.2777:resetWrap
    def resetWrap (self,event=None):
    
        self.wrapPosition = None
        self.onlyPosition = None
    #@-node:AGP.20250415230112.2777:resetWrap
    #@+node:AGP.20250415230112.2778:search & helpers
    def search (self):
    
        """Search s_ctrl for self.find_text under the control of the
        whole_word, ignore_case, and pattern_match ivars.
        
        Returns (pos, newpos) or (None,None)."""
    
        c = self.c ; p = self.p ; w = self.s_ctrl ; gui = g.app.gui
        index = gui.getInsertPoint(w)
        # g.trace(g.app.gui.widget_name(w),index,p.headString())
        s = gui.getAllText(w)
        index = gui.toPythonIndex(s,w,index)
        stopindex = g.choose(self.reverse,0,len(s))
        
        
        #print "searh pos",index,stopindex
        pos,newpos = self.searchHelper( s, index, stopindex, self.find_text,
                                        backwards=self.reverse,nocase=self.ignore_case,regexp=self.pattern_match,word=self.whole_word)
        
        if pos == -1: return None,None
        
        pos    = gui.toGuiIndex(s,w,pos)
        newpos = gui.toGuiIndex(s,w,newpos)
        #@    << fail if we are passed the wrap point >>
        #@+node:AGP.20250415230112.2779:<< fail if we are passed the wrap point >>
        if self.wrapping and self.wrapPos and self.wrapPosition and p == self.wrapPosition:
            
            #print "wrap check",newpos,self.wrapPos
            
            if self.reverse and gui.compareIndices(w,pos, ">", self.wrapPos):
                #print "failed wrap pos"
                return None, None
        
            
            if not self.reverse and gui.compareIndices(w,newpos, "<", self.wrapPos):
                #print "failed wrap pos"
                return None, None
        #@-node:AGP.20250415230112.2779:<< fail if we are passed the wrap point >>
        #@nl
        gui.setTextSelection(w,pos,newpos,insert=newpos)
        return pos, newpos
    #@+node:AGP.20250415230112.2780:Search helpers...
    def searchHelper (self,s,i,j,pattern,backwards,nocase,regexp,word,swapij=True):
        
        if swapij and backwards: i,j = j,i
            
        # g.trace(backwards,i,j,repr(s[i:i+20]))
    
        if not s[i:j] or not pattern:
            # g.trace('empty',i,j)
            return -1,-1
            
        if regexp:
            pos,newpos = self.regexHelper(s,i,j,pattern,backwards,nocase)
        elif backwards:
            pos,newpos = self.backwardsHelper(s,i,j,pattern,nocase,word)
        else:
            pos,newpos = self.plainHelper(s,i,j,pattern,nocase,word)
    
        return pos,newpos
    #@+node:AGP.20250415230112.2781:regexHelper
    def regexHelper (self,s,i,j,pattern,backwards,nocase):
       
        try:
            flags = re.MULTILINE
            if nocase: flags |= re.IGNORECASE
            re_obj = re.compile(pattern,flags)
        except Exception:
            g.es('Invalid regular expression: %s' % (pattern),color='blue')
            self.errors += 1 # Abort the search.
            return -1, -1
            
        if backwards: # Scan to the last match.
            last_mo = None
            while 1:
                mo = re_obj.search(s,i,j)
                if mo is None: break
                i = mo.end()
                last_mo = mo
            self.match_obj = mo = last_mo
        else:
            self.match_obj = mo = re_obj.search(s,i,j)
            
        if mo is None:
            return -1, -1
        else:
            k  = mo.start()
            k2 = mo.end()
            if 0:
                g.trace('i: %d, j: %d k: %d, k2: %d, s[k:k2]: %s, len(s): %d, s[-1]: %s,' % (
                    i,j,k,k2,repr(s[k:k2]),len(s),repr(s[-1])))
            # g.trace('groups',mo.groups())
            if k == k2:
                return -1, -1 # A non-empty pattern can match an empty string.  Move on!
            else:
                return k, k2
    #@-node:AGP.20250415230112.2781:regexHelper
    #@+node:AGP.20250415230112.2782:backwardsHelper
    def backwardsHelper (self,s,i,j,pattern,nocase,word):
    
        if nocase:
            s = s.lower() ; pattern.lower()
    
        n = len(pattern)
        if word:
            while 1:
                k = s.rfind(pattern,i,j)
                # g.trace(i,j,k)
                if k == -1: return -1, -1
                if self.matchWord(s,k,pattern):
                    return k,k+n
                else:
                    j = max(0,k-1)
        else:
            k = s.rfind(pattern,i,j)
            # g.trace(i,j,k)
            if k == -1:
                return -1, -1
            else:
                return k,k+n
    #@-node:AGP.20250415230112.2782:backwardsHelper
    #@+node:AGP.20250415230112.2783:plainHelper
    def plainHelper (self,s,i,j,pattern,nocase,word):
        
        # g.trace(repr(s[i:i+20]))
        
        n = len(pattern)
        if nocase:
            s = s.lower() ; pattern = pattern.lower()
            pattern = pattern.replace('\\n','\n').replace('\\t','\t')
    
        if word:
            while 1:
                k = s.find(pattern,i,j)
                # g.trace(k,n)
                if k == -1: return -1, -1
                elif self.matchWord(s,k,pattern):
                    return k, k + n
                else: i = k + n
        else:
            k = s.find(pattern,i,j)
            if k == -1:
                return -1, -1
            else:
                return k, k + n
    #@-node:AGP.20250415230112.2783:plainHelper
    #@+node:AGP.20250415230112.2784:matchWord
    def matchWord(self,s,i,pattern):
        
        ok = g.match_word(s,i,pattern) and (
            i == 0 or not g.isWordChar(s[i-1]) or not g.isWordChar(s[i]))
    
        # g.trace(ok,repr(s),i)
        return ok
    #@-node:AGP.20250415230112.2784:matchWord
    #@-node:AGP.20250415230112.2780:Search helpers...
    #@-node:AGP.20250415230112.2778:search & helpers
    #@+node:AGP.20250415230112.2785:selectNextPosition
    # Selects the next node to be searched.
    
    def selectNextPosition(self):
    
        c = self.c
        p = self.p
    
        if self.selection_only:
            return None
            
        # Start suboutline only searches.
        if self.suboutline_only and not self.onlyPosition:
            self.onlyPosition = p
        
        # Start wrapped searches.
        if self.wrapping and not self.wrapPosition:
            self.wrapPosition = p
        
        if self.node_only:
            if self.wrapping and not self.wrapped:
                self.initNextText()
                self.wrapped = True
                g.es("search wrap around")
                return p
            return None
        
        if self.in_headline and self.search_body: # just switch to body pane.
            self.in_headline = False
            self.initNextText()        
            return p
        
        if self.reverse:
            p = p.threadBack()
        else:
            p = p.threadNext()
        
        if c.hoistStack:# New in 4.3: restrict searches to hoisted area.End searches outside hoisted area.
            if not p:
                if self.wrapping:
                    g.es('Wrap disabled in hoisted outlines',color='blue')
                return
            bunch = c.hoistStack[-1]
            if not bunch.p.isAncestorOf(p):
                g.es('Found match outside of hoisted outline',color='blue')
                return None
    
        # Wrap if needed.
        if not p and self.wrapping and not self.suboutline_only:
            if not self.wrapped:
                p = c.rootPosition()
                if self.reverse:    # Set search_v to the last node of the tree.
                    while p and p.next():
                        p = p.next()
                    if p:
                        p = p.lastNode()
                self.p = p
                self.initNextText()
                self.wrapped = True
                g.es("search wrap around")
            else:
                return None #End wrapped searches.
        
    
        # End suboutline only searches.
        if self.suboutline_only and p:
            if p == self.onlyPosition or not self.onlyPosition.isAncestorOf(p):
                if self.wrapping and not self.wrapped:
                    p = self.p = self.onlyPosition
                    self.initNextText()
                    self.wrapped = True
                    g.es("search wrap around")
                    return p
                    
                self.onlyPosition = None
                return None
        
        
        # p.copy not needed because the find code never calls p.moveToX.
        
        self.p = p # used in initNextText().
        if p: # select p and set the search point within p.
            self.in_headline = self.search_headline
            self.initNextText()
            
        
        return p
    #@-node:AGP.20250415230112.2785:selectNextPosition
    #@-node:AGP.20250415230112.2760:Find/change utils
    #@+node:AGP.20250415230112.2786:Initing & finalizing
    #@+node:AGP.20250415230112.2787:checkArgs
    def checkArgs (self):
    
        val = True
        if not self.search_headline and not self.search_body:
            g.es("not searching headline or body")
            val = False
        if len(self.find_text) == 0:
            g.es("empty find patttern")
            val = False
        return val
    #@-node:AGP.20250415230112.2787:checkArgs
    #@+node:AGP.20250415230112.2788:initBatchCommands
    # Initializes for the Find All and Change All commands.
    
    def initBatchCommands (self):
    
        c = self.c
        self.in_headline = self.search_headline # Search headlines first.
        self.errors = 0
    
        # Select the first node.
        if self.suboutline_only or self.node_only or self.selection_only:
            self.p = c.currentPosition()
            if self.selection_only: self.selStart,self.selEnd = c.frame.body.getTextSelection()
            else:                   self.selStart,self.selEnd = None,None
        else:
            p = c.rootPosition()
            if self.reverse:
                while p and p.next():
                    p = p.next()
                p = p.lastNode()
            self.p = p
    
        # Set the insert point.
        self.initBatchText()
    #@-node:AGP.20250415230112.2788:initBatchCommands
    #@+node:AGP.20250415230112.2789:initBatchText & initNextText
    # Returns s_ctrl with "insert" point set properly for batch searches.
    def initBatchText(self):
        p = self.p
        self.wrapping = False # Only interactive commands allow wrapping.
        s = g.choose(self.in_headline,p.headString(), p.bodyString())
        return self.init_s_ctrl(s)
    
    # Call this routine when moving to the next node when a search fails.
    # Same as above except we don't reset wrapping flag.
    def initNextText(self):
        p = self.p
        s = g.choose(self.in_headline,p.headString(), p.bodyString())
        return self.init_s_ctrl(s)
    #@-node:AGP.20250415230112.2789:initBatchText & initNextText
    #@+node:AGP.20250415230112.2790:initInHeadline
    # Guesses which pane to start in for incremental searches and changes.
    # This must not alter the current "insert" or "sel" marks.
    
    def initInHeadline (self):
    
        c = self.c ; p = self.p
    
        # Do not change this without careful thought and extensive testing!
        if self.search_headline and self.search_body:
            # A temporary expedient.
            if self.reverse:
                self.in_headline = False
            else:
                # Search headline first.
                self.in_headline = (
                    p == c.frame.tree.editPosition() and
                    c.get_focus() != c.frame.body.bodyCtrl)
        else:
            self.in_headline = self.search_headline
    #@-node:AGP.20250415230112.2790:initInHeadline
    #@+node:AGP.20250415230112.2791:initInteractiveCommands
    # For incremental searches
    
    def initInteractiveCommands(self):
    
        c = self.c ; p = self.p ; gui = g.app.gui
    
        self.errors = 0
        if self.in_headline:
            c.frame.tree.setEditPosition(p)
            self.searched_widget = t = c.edit_widget(p)
            sel = None
        else:
            self.searched_widget = t = c.frame.bodyCtrl
            sel = gui.getTextSelection(t)
        
        pos = gui.getInsertPoint(t)
        st = self.initNextText()
        c.widgetWantsFocus(t)
        gui.setInsertPoint(st,pos)
        
        if sel:
            self.selStart,self.selEnd = sel
        else:
            self.selStart,self.selEnd = None,None
        self.wrapping = self.wrap
        if self.wrap and self.wrapPosition == None:
            self.wrapPos = pos
            # Do not set self.wrapPosition here: that must be done after the first search.
    #@-node:AGP.20250415230112.2791:initInteractiveCommands
    #@+node:AGP.20250415230112.2792:printLine
    def printLine (self,line,allFlag=False):
    
        both = self.search_body and self.search_headline
        context = self.batch # "batch" now indicates context
    
        if allFlag and both and context:
            g.es('-' * 20,self.p.headString())
            theType = g.choose(self.in_headline,"head: ","body: ")
            g.es(theType + line)
        elif allFlag and context and not self.p.isVisited():
            # We only need to print the context once.
            g.es('-' * 20,self.p.headString())
            g.es(line)
            self.p.setVisited()
        else:
            g.es(line)
    #@-node:AGP.20250415230112.2792:printLine
    #@+node:AGP.20250415230112.2793:restore
    # Restores the screen after a search fails
    
    def restore (self,data):
    
        c = self.c ; gui = g.app.gui
        in_headline,p,t,insert,start,end = data
        
        c.frame.bringToFront() # Needed on the Mac
    
        # Don't try to reedit headline.
        c.selectPosition(p)
        
        if not in_headline:
            # Looks good and provides clear indication of failure or termination.
            gui.setSelectionRange(t,insert,insert)
            gui.setInsertPoint(t,insert)
            gui.makeIndexVisible(t,insert)
        
        #g.trace(c.widget_name(t))
        
        if 1: # I prefer always putting the focus in the body.
            c.invalidateFocus()
            c.bodyWantsFocusNow()
        else:
            c.widgetWantsFocusNow(t)
    #@-node:AGP.20250415230112.2793:restore
    #@+node:AGP.20250415230112.2794:save
    def save (self):
    
        c = self.c ; p = self.p ; gui = g.app.gui
        t = g.choose(self.in_headline,c.edit_widget(p),c.frame.bodyCtrl)
        insert = gui.getInsertPoint(t)
        sel = gui.getSelectionRange(t)
        if len(sel) == 2:
            start,end = sel
        else:
            start,end = None,None
        return (self.in_headline,p,t,insert,start,end)
    #@-node:AGP.20250415230112.2794:save
    #@+node:AGP.20250415230112.2795:showSuccess
    def showSuccess(self,pos,newpos):
    
        """Displays the final result.
    
        Returns self.dummy_vnode, c.edit_widget(p) or c.frame.bodyCtrl with
        "insert" and "sel" points set properly."""
    
        c = self.c ; p = self.p ; gui = g.app.gui
        sparseFind = c.config.getBool('collapse_nodes_during_finds')
        c.frame.bringToFront() # Needed on the Mac
        redraw = not p.isVisible()
        c.beginUpdate()
        try:
            if self.collapse:#sparseFind:
                # New in Leo 4.4.2: show only the 'sparse' tree when redrawing.
                for p in c.allNodes_iter():
                    if not p.isAncestorOf(self.p):
                        p.contract()
                        redraw = True
                for p in self.p.parents_iter():
                    if not p.isExpanded():
                        p.expand()
                        redraw = True
            p = self.p
            c.selectPosition(p)
        finally:
            c.endUpdate(redraw)
        if self.in_headline:
            c.editPosition(p)
        # Set the focus and selection after the redraw.
        t = g.choose(self.in_headline,c.edit_widget(p),c.frame.bodyCtrl)
        # g.trace(g.app.gui.widget_name(t),id(t),p.headString())
        insert = g.choose(self.reverse,pos,newpos)
        # New in 4.4a3: a much better way to ensure progress in backward searches.
        # g.trace(id(t),pos,newpos)
        c.widgetWantsFocusNow(t)
        gui.setSelectionRange(t,pos,newpos,insert=insert)
        # c.widgetWantsFocusNow(t)
        gui.makeIndexVisible(t,insert)
        if self.wrap and not self.wrapPosition:
            self.wrapPosition = self.p
    #@nonl
    #@-node:AGP.20250415230112.2795:showSuccess
    #@-node:AGP.20250415230112.2786:Initing & finalizing
    #@+node:AGP.20250415230112.2796:Must be overridden in subclasses
    def init_s_ctrl (self,s):
        self.oops()
    
    def bringToFront (self):
        self.oops()
       
    # New in 4.3: allows base class to adjust controls. 
    def adjust_find_text(self,s):
        self.oops()
    
    def oops(self):
        print ("leoFind oops:",
            g.callers(),"should be overridden in subclass")
            
    def update_ivars(self):
        self.oops()
    #@-node:AGP.20250415230112.2796:Must be overridden in subclasses
    #@-others
#@-node:AGP.20250415230112.2739:@thin leoFind.py
#@-leo
