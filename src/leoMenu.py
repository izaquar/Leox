#@+leo-ver=4-thin
#@+node:AGP.20250415230112.2969:@thin leoMenu.py
"""Gui-independent menu handling for Leo."""

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import string
import sys

#@+others
#@+node:AGP.20250415230112.2970:class leoMenu
class leoMenu:
    
    """The base class for all Leo menus."""
    
    #@    @+others
    #@+node:AGP.20250415230112.2971: leoMenu.__init__
    def __init__ (self,frame):
        
        # g.trace('leoMenu',g.callers())
        
        self.c = c = frame.c
        self.frame = frame
        self.menus = {} # Menu dictionary.
        self.menuShortcuts = {}
        
        # To aid transition to emacs-style key handling.
        self.useCmdMenu = c.config.getBool('useCmdMenu')
        
        self.newBinding = True
            # True if using new binding scheme.
            # You can set this to False in an emergency to revert to the old way.
    
        if 0: # Must be done much later.
            self.defineMenuTables()
    #@-node:AGP.20250415230112.2971: leoMenu.__init__
    #@+node:AGP.20250415230112.2972:oops
    def oops (self):
    
        print "leoMenu oops:", g.callers(), "should be overridden in subclass"
    #@-node:AGP.20250415230112.2972:oops
    #@+node:AGP.20250415230112.2973:Gui-independent menu enablers
    #@+node:AGP.20250415230112.2974:updateAllMenus
    def updateAllMenus (self):
        
        """The Tk "postcommand" callback called when a click happens in any menu.
        
        Updates (enables or disables) all menu items."""
    
        # Allow the user first crack at updating menus.
        c = self.c
        #print "update all menu"
        if c and c.exists:
            c.setLog()
            p = c.currentPosition()
        
            if not g.doHook("menu2",c=c,p=p,v=p):
                self.updateFileMenu()
                self.updateEditMenu()
                self.updateOutlineMenu()
    #@nonl
    #@-node:AGP.20250415230112.2974:updateAllMenus
    #@+node:AGP.20250415230112.2975:updateFileMenu
    def updateFileMenu (self):
        
        c = self.c ; frame = c.frame
        if not c: return
    
        try:
            enable = frame.menu.enableMenu
            menu = frame.menu.getMenu("File")
            enable(menu,"Revert To Saved", c.canRevert())
            #enable(menu,"Open With...", g.app.hasOpenWithMenu)
        except:
            g.es("exception updating File menu")
            g.es_exception()
    #@-node:AGP.20250415230112.2975:updateFileMenu
    #@+node:AGP.20250415230112.2976:updateEditMenu
    def updateEditMenu (self):
    
        c = self.c ; frame = c.frame ; gui = g.app.gui
        if not c: return
        try:
            # Top level Edit menu...
            enable = frame.menu.enableMenu
            menu = frame.menu.getMenu("Edit")
            c.undoer.enableMenuItems()
            #@        << enable cut/paste >>
            #@+node:AGP.20250415230112.2977:<< enable cut/paste >>
            if frame.body.hasFocus():
                data = frame.body.getSelectedText()
                canCut = data and len(data) > 0
            else:
                # This isn't strictly correct, but we can't get the Tk headline selection.
                canCut = True
            
            enable(menu,"Cut",canCut)
            enable(menu,"Copy",canCut)
            
            data = gui.getTextFromClipboard()
            canPaste = data and len(data) > 0
            enable(menu,"Paste",canPaste)
            #@-node:AGP.20250415230112.2977:<< enable cut/paste >>
            #@nl
            if 0: # Always on for now.
                menu = frame.menu.getMenu("Find...")
                enable(menu,"Find Next",c.canFind())
                flag = c.canReplace()
                enable(menu,"Replace",flag)
                enable(menu,"Replace, Then Find",flag)
            # Edit Body submenu...
            menu = frame.menu.getMenu("Edit Body...")
            enable(menu,"Extract Section",c.canExtractSection())
            enable(menu,"Extract Names",c.canExtractSectionNames())
            enable(menu,"Extract",c.canExtract())
            enable(menu,"Match Brackets",c.canFindMatchingBracket())
        except:
            g.es("exception updating Edit menu")
            g.es_exception()
    #@-node:AGP.20250415230112.2976:updateEditMenu
    #@+node:AGP.20250415230112.2978:updateOutlineMenu
    def updateOutlineMenu (self):
    
        c = self.c ; frame = c.frame
        if not c: return
    
        p = c.currentPosition()
        hasParent = p.hasParent()
        hasBack = p.hasBack()
        hasNext = p.hasNext()
        hasChildren = p.hasChildren()
        isExpanded = p.isExpanded()
        isCloned = p.isCloned()
        isMarked = p.isMarked()
    
        try:
            enable = frame.menu.enableMenu
            #@        << enable top level outline menu >>
            #@+node:AGP.20250415230112.2979:<< enable top level outline menu >>
            menu = frame.menu.getMenu("Outline")
            enable(menu,"Cut Node",c.canCutOutline())
            enable(menu,"Delete Node",c.canDeleteHeadline())
            enable(menu,"Paste Node",c.canPasteOutline())
            enable(menu,"Paste Node As Clone",c.canPasteOutline())
            enable(menu,"Clone Node",c.canClone()) # 1/31/04
            enable(menu,"Sort Siblings",c.canSortSiblings())
            enable(menu,"Hoist",c.canHoist())
            enable(menu,"De-Hoist",c.canDehoist())
            #@-node:AGP.20250415230112.2979:<< enable top level outline menu >>
            #@nl
            #@        << enable expand/contract submenu >>
            #@+node:AGP.20250415230112.2980:<< enable expand/Contract submenu >>
            menu = frame.menu.getMenu("Expand/Contract...")
            enable(menu,"Contract Parent",c.canContractParent())
            enable(menu,"Contract Node",hasChildren and isExpanded)
            enable(menu,"Contract Or Go Left",(hasChildren and isExpanded) or hasParent)
            enable(menu,"Expand Node",hasChildren and not isExpanded)
            enable(menu,"Expand Prev Level",hasChildren and isExpanded)
            enable(menu,"Expand Next Level",hasChildren)
            enable(menu,"Expand To Level 1",hasChildren and isExpanded)
            enable(menu,"Expand Or Go Right",hasChildren)
            for i in xrange(2,9):
                frame.menu.enableMenu(menu,"Expand To Level " + str(i), hasChildren)
            #@-node:AGP.20250415230112.2980:<< enable expand/Contract submenu >>
            #@nl
            #@        << enable move submenu >>
            #@+node:AGP.20250415230112.2981:<< enable move submenu >>
            menu = frame.menu.getMenu("Move...")
            enable(menu,"Move Down",c.canMoveOutlineDown())
            enable(menu,"Move Left",c.canMoveOutlineLeft())
            enable(menu,"Move Right",c.canMoveOutlineRight())
            enable(menu,"Move Up",c.canMoveOutlineUp())
            enable(menu,"Promote",c.canPromote())
            enable(menu,"Demote",c.canDemote())
            #@-node:AGP.20250415230112.2981:<< enable move submenu >>
            #@nl
            #@        << enable go to submenu >>
            #@+node:AGP.20250415230112.2982:<< enable go to submenu >>
            menu = frame.menu.getMenu("Go To...")
            enable(menu,"Go Prev Visited",c.beadPointer > 1)
            enable(menu,"Go Next Visited",c.beadPointer + 1 < len(c.beadList))
            enable(menu,"Go To Prev Visible",c.canSelectVisBack())
            enable(menu,"Go To Next Visible",c.canSelectVisNext())
            if 0: # These are too slow.
                enable(menu,"Go To Next Marked",c.canGoToNextMarkedHeadline())
                enable(menu,"Go To Next Changed",c.canGoToNextDirtyHeadline())
            enable(menu,"Go To Next Clone",isCloned)
            enable(menu,"Go To Prev Node",c.canSelectThreadBack())
            enable(menu,"Go To Next Node",c.canSelectThreadNext())
            enable(menu,"Go To Parent",hasParent)
            enable(menu,"Go To Prev Sibling",hasBack)
            enable(menu,"Go To Next Sibling",hasNext)
            #@-node:AGP.20250415230112.2982:<< enable go to submenu >>
            #@nl
            #@        << enable mark submenu >>
            #@+node:AGP.20250415230112.2983:<< enable mark submenu >>
            menu = frame.menu.getMenu("Mark/Unmark...")
            label = g.choose(isMarked,"Unmark","Mark")
            frame.menu.setMenuLabel(menu,0,label)
            enable(menu,"Mark Subheads",hasChildren)
            if 0: # These are too slow.
                enable(menu,"Mark Changed Items",c.canMarkChangedHeadlines())
                enable(menu,"Mark Changed Roots",c.canMarkChangedRoots())
            enable(menu,"Mark Clones",isCloned)
            #@-node:AGP.20250415230112.2983:<< enable mark submenu >>
            #@nl
        except:
            g.es("exception updating Outline menu")
            g.es_exception()
    #@-node:AGP.20250415230112.2978:updateOutlineMenu
    #@+node:AGP.20250415230112.2984:hasSelection
    # Returns True if text in the outline or body text is selected.
    
    def hasSelection (self):
        
        body = self.frame.body
    
        if body:
            first, last = body.getTextSelection()
            return first != last
        else:
            return False
    #@-node:AGP.20250415230112.2984:hasSelection
    #@-node:AGP.20250415230112.2973:Gui-independent menu enablers
    #@+node:AGP.20250415230112.2985:Gui-independent menu routines
    #@+node:AGP.20250415230112.2986:capitalizeMinibufferMenuName
    def capitalizeMinibufferMenuName (self,s,removeHyphens):
        
        result = []
        for i in xrange(len(s)):
            ch = s[i]
            prev = i > 0 and s[i-1] or ''
            prevprev = i > 1 and s[i-2] or ''
            if (
                i == 0 or
                i == 1 and prev == '&' or
                prev == '-' or
                prev == '&' and prevprev == '-'
            ):
                result.append(ch.capitalize())
            elif removeHyphens and ch == '-':
                result.append(' ')
            else:
                result.append(ch)
        return ''.join(result)
    #@nonl
    #@-node:AGP.20250415230112.2986:capitalizeMinibufferMenuName
    #@+node:AGP.20250415230112.2987:createMenusFromTables & helpers
    def createMenusFromTables (self):
        
        c = self.c
        
        self.defineMenuTables()
        
        self.createFileMenuFromTable()
        self.createEditMenuFromTable()
        self.createOutlineMenuFromTable()
        
        g.doHook("create-optional-menus",c=c)
        
        if self.useCmdMenu:
            self.createCmndsMenuFromTable()
            
        
        
        #self.createWindowMenuFromTable()
        self.createHelpMenuFromTable()
    #@+node:AGP.20250415230112.2988:createFileMenuFromTable
    def createFileMenuFromTable (self):
        
        c = self.c
        
        fileMenu = self.createNewMenu("&File")
        
        self.createMenuEntries(fileMenu,self.fileMenuTopTable)
        #self.createNewMenu("Open &With...","File")
        #@    << create the recent files submenu >>
        #@+node:AGP.20250415230112.2989:<< create the recent files submenu >>
        self.createNewMenu("Open Recent &File...","File")
        c.recentFiles = c.config.getRecentFiles()
        
        if 0: # Not needed, and causes problems in wxWindows...
            self.createRecentFilesMenuItems()
        #@-node:AGP.20250415230112.2989:<< create the recent files submenu >>
        #@nl
        self.createMenuEntries(fileMenu,self.fileMenuTop2Table)
        
        self.add_separator(fileMenu)
        #@    << create the read/write submenu >>
        #@+node:AGP.20250415230112.2990:<< create the read/write submenu >>
        readWriteMenu = self.createNewMenu("&Read/Write...","File")
        
        self.createMenuEntries(readWriteMenu,self.fileMenuReadWriteMenuTable)
        #@-node:AGP.20250415230112.2990:<< create the read/write submenu >>
        #@nl
        #@    << create the tangle submenu >>
        #@+node:AGP.20250415230112.2991:<< create the tangle submenu >>
        tangleMenu = self.createNewMenu("Tan&gle...","File")
        
        self.createMenuEntries(tangleMenu,self.fileMenuTangleMenuTable)
        #@-node:AGP.20250415230112.2991:<< create the tangle submenu >>
        #@nl
        #@    << create the untangle submenu >>
        #@+node:AGP.20250415230112.2992:<< create the untangle submenu >>
        untangleMenu = self.createNewMenu("&Untangle...","File")
        
        self.createMenuEntries(untangleMenu,self.fileMenuUntangleMenuTable)
        #@-node:AGP.20250415230112.2992:<< create the untangle submenu >>
        #@nl
        #@    << create the import submenu >>
        #@+node:AGP.20250415230112.2993:<< create the import submenu >>
        importMenu = self.createNewMenu("&Import...","File")
        
        self.createMenuEntries(importMenu,self.fileMenuImportMenuTable)
        #@-node:AGP.20250415230112.2993:<< create the import submenu >>
        #@nl
        #@    << create the export submenu >>
        #@+node:AGP.20250415230112.2994:<< create the export submenu >>
        exportMenu = self.createNewMenu("&Export...","File")
        
        self.createMenuEntries(exportMenu,self.fileMenuExportMenuTable)
        #@-node:AGP.20250415230112.2994:<< create the export submenu >>
        #@nl
        self.add_separator(fileMenu)
        self.createMenuEntries(fileMenu,self.fileMenuTop3MenuTable)
    #@-node:AGP.20250415230112.2988:createFileMenuFromTable
    #@+node:AGP.20250415230112.2995:createEditMenuFromTable
    def createEditMenuFromTable (self):
    
        editMenu = self.createNewMenu("&Edit")
        self.createMenuEntries(editMenu,self.editMenuTopTable)
    
        #@    << create the edit body submenu >>
        #@+node:AGP.20250415230112.2996:<< create the edit body submenu >>
        editBodyMenu = self.createNewMenu("Edit &Body...","Edit")
        
        self.createMenuEntries(editBodyMenu,self.editMenuEditBodyTable)
        #@-node:AGP.20250415230112.2996:<< create the edit body submenu >>
        #@nl
        #@    << create the edit headline submenu >>
        #@+node:AGP.20250415230112.2997:<< create the edit headline submenu >>
        editHeadlineMenu = self.createNewMenu("Edit &Headline...","Edit")
        
        self.createMenuEntries(editHeadlineMenu,self.editMenuEditHeadlineTable)
        #@-node:AGP.20250415230112.2997:<< create the edit headline submenu >>
        #@nl
        #@    << create the find submenu >>
        #@+node:AGP.20250415230112.2998:<< create the find submenu >>
        findMenu = self.createNewMenu("&Find...","Edit")
        
        #self.createMenuEntries(findMenu,self.editMenuFindMenuTable)
        
        findMenu.add_command(label="Find/Change Next",accelerator="F3",command=self.c.searchCommands.findTabFindNext)
        findMenu.add_command(label="Find/Change Prev",accelerator="F2",command=self.c.searchCommands.findTabFindPrev)
        findMenu.add_separator()
        findMenu.add_command(label="Find/Change All",command=self.c.searchCommands.findTabFindAll)
        findMenu.add_command(label="Clone Find All",command=self.c.searchCommands.findTabFindAll)
        
        
        #@-node:AGP.20250415230112.2998:<< create the find submenu >>
        #@nl
        
        self.createMenuEntries(editMenu,self.editMenuTop2Table)
    #@-node:AGP.20250415230112.2995:createEditMenuFromTable
    #@+node:AGP.20250415230112.2999:createOutlineMenuFromTable
    def createOutlineMenuFromTable (self):
    
        outlineMenu = self.createNewMenu("&Outline")
        
        self.createMenuEntries(outlineMenu,self.outlineMenuTopMenuTable)
        
        #@    << create check submenu >>
        #@+node:AGP.20250415230112.3000:<< create check submenu >>
        checkOutlineMenu = self.createNewMenu("Chec&k...","Outline")
        
        self.createMenuEntries(checkOutlineMenu,self.outlineMenuCheckOutlineMenuTable)
        #@-node:AGP.20250415230112.3000:<< create check submenu >>
        #@nl
        #@    << create expand/contract submenu >>
        #@+node:AGP.20250415230112.3001:<< create expand/contract submenu >>
        expandMenu = self.createNewMenu("E&xpand/Contract...","Outline")
        
        self.createMenuEntries(expandMenu,self.outlineMenuExpandContractMenuTable)
        #@-node:AGP.20250415230112.3001:<< create expand/contract submenu >>
        #@nl
        #@    << create move submenu >>
        #@+node:AGP.20250415230112.3002:<< create move submenu >>
        moveSelectMenu = self.createNewMenu("&Move...","Outline")
        
        self.createMenuEntries(moveSelectMenu,self.outlineMenuMoveMenuTable)
        #@-node:AGP.20250415230112.3002:<< create move submenu >>
        #@nl
        #@    << create mark submenu >>
        #@+node:AGP.20250415230112.3003:<< create mark submenu >>
        markMenu = self.createNewMenu("M&ark/Unmark...","Outline")
        
        self.createMenuEntries(markMenu,self.outlineMenuMarkMenuTable)
        #@-node:AGP.20250415230112.3003:<< create mark submenu >>
        #@nl
        #@    << create goto submenu >>
        #@+node:AGP.20250415230112.3004:<< create goto submenu >>
        gotoMenu = self.createNewMenu("&Go To...","Outline")
        
        self.createMenuEntries(gotoMenu,self.outlineMenuGoToMenuTable)
        #@-node:AGP.20250415230112.3004:<< create goto submenu >>
        #@nl
    #@-node:AGP.20250415230112.2999:createOutlineMenuFromTable
    #@+node:AGP.20250415230112.3005:createCmndsMenuFromTable
    def createCmndsMenuFromTable (self):
        
        cmdsMenu = self.createNewMenu('&Cmds')
        
        if 0: # Now in the minibuffer table.
            # Used in top table: q,u,x
            self.createMenuEntries(cmdsMenu,self.cmdsMenuTopTable)
    
        for name,table in (
            # &: a,b,c,d,f,g,h,i,m,n,o,p,r,s,t
            ('&Abbrev...',          self.cmdsMenuAbbrevTable),
            ('Body E&ditors',       self.cmdsMenuBodyEditorsTable),
            ('&Buffers...',         self.cmdsMenuBuffersTable),
            ('&Cursor/Selection...',[]),
            ('&Focus...',           self.cmdsMenuFocusTable),
            ('&Macro...',           self.cmdsMenuMacroTable),
            ('M&inibuffer',         self.cmdsMenuMinibufferTable),
            ('&Panes...',           self.cmdsMenuPanesTable),
            ('Pic&kers...',         self.cmdsMenuPickersTable),
            ('&Rectangles...',      self.cmdsMenuRectanglesTable),
            ('Re&gisters...',       self.cmdsMenuRegistersTable),
            ('Scr&olling...',       self.cmdsMenuScrollTable),
            ('Spell C&heck...',     self.cmdsMenuSpellCheckTable),
            ('&Text Commands',      self.cmdsMenuTextTable),
            ('Toggle Setti&ngs',     self.cmdsMenuToggleTable),
        ):
            menu = self.createNewMenu(name,'&Cmds')
            self.createMenuEntries(menu,table)
    
        for name,table in (
            # &: b,e,f,s,t,x
            ('Cursor &Back...',                     self.cursorMenuBackTable),
            ('Cursor Back &Extend Selection...',    self.cursorMeuuBackExtendTable),
            ('Cursor Extend &To...',                self.cursorMenuExtendTable),
            ('Cursor &Forward...',                  self.cursorMenuForwardTable),
            ('Cursor Forward E&xtend Selection...', self.cursorMenuForwardExtendTable),
        ):
            menu = self.createNewMenu(name,'C&ursor/Selection...')
            self.createMenuEntries(menu,table)
    #@nonl
    #@-node:AGP.20250415230112.3005:createCmndsMenuFromTable
    #@+node:AGP.20250415230112.3006:createWindowMenuFromTable
    def createWindowMenuFromTable (self):
    
        windowMenu = self.createNewMenu("&Window")
        
        self.createMenuEntries(windowMenu,self.windowMenuTopTable)
    #@-node:AGP.20250415230112.3006:createWindowMenuFromTable
    #@+node:AGP.20250415230112.3007:createHelpMenuFromTable
    def createHelpMenuFromTable (self):
    
        if sys.platform == 'darwin':
            self.getMacHelpMenu()
        else:
            helpMenu = self.createNewMenu("&Help")
            self.createMenuEntries(helpMenu,self.helpMenuTable)
    #@nonl
    #@-node:AGP.20250415230112.3007:createHelpMenuFromTable
    #@-node:AGP.20250415230112.2987:createMenusFromTables & helpers
    #@+node:AGP.20250415230112.3008:defineMenuTables & helpers
    def defineMenuTables (self):
        
        self.defineEditMenuTables()
        self.defineFileMenuTables()
        self.defineOutlineMenuTables()
        self.defineWindowMenuTables()
    
        if self.useCmdMenu:
            self.defineCmdsMenuTables()
    
        self.defineHelpMenuTables()
    
    #@+node:AGP.20250415230112.3009:defineEditMenuTables & helpers
    def defineEditMenuTables (self):
    
        self.defineEditMenuTopTable()
        self.defineEditMenuEditBodyTable()
        self.defineEditMenuEditHeadlineTable()
        self.defineEditMenuFindMenuTable()
        self.defineEditMenuTop2Table()
    #@+node:AGP.20250415230112.3010:defineEditMenuTopTable
    def defineEditMenuTopTable (self):
        
        self.editMenuTopTable = [
            # &: u,r reserved for undo/redo: a,d,p,t,y.
            # & (later): e,g,n,v.
            ("Can't Undo",'undo'),
            ("Can't Redo",'redo'), 
            '-',
            ('Cu&t','cut-text'),
            ('Cop&y','copy-text'),
            ('&Paste','paste-text'),
            ('&Delete','backward-delete-char'),
            ('Select &All','select-all'),
            '-',
        ]
    #@-node:AGP.20250415230112.3010:defineEditMenuTopTable
    #@+node:AGP.20250415230112.3011:defineEditMenuEditBodyTable
    def defineEditMenuEditBodyTable (self):
        
        self.editMenuEditBodyTable = [
            # Shortcuts a,b,d,e,i,l,m,n,r,s,t,u
            '*extract-&section',
            '*extract-&names',
            '*&extract',
            '-',
            '*convert-all-b&lanks',
            '*convert-all-t&abs',
            '*convert-&blanks',
            '*convert-&tabs',
            '*insert-body-&time',
            '*&reformat-paragraph',
            '-',
            '*&indent-region',
            '*&unindent-region',
            '*&match-brackets',
            '*add-comments',
            '*delete-comments',
        ]
    #@-node:AGP.20250415230112.3011:defineEditMenuEditBodyTable
    #@+node:AGP.20250415230112.3012:defineEditMenuEditHeadlineTable
    def defineEditMenuEditHeadlineTable (self):
        
        self.editMenuEditHeadlineTable = [
            '*edit-&headline',
            '*&end-edit-headline',
            '*&abort-edit-headline',
            '*insert-headline-&time',
            '*toggle-&angle-brackets',
        ]
    #@-node:AGP.20250415230112.3012:defineEditMenuEditHeadlineTable
    #@+node:AGP.20250415230112.3013:defineEditMenuFindMenuTable
    def defineEditMenuFindMenuTable (self):
        
        self.editMenuFindMenuTable = [
            # &: a,b,c,d,e,f,h,i,l,n,o,p,q,r,s,u,w,x
            #'*&open-find-tab',
            #'*&hide-find-tab',
            #'*search-&with-present-options',
            #'-',
            '*find-&next',
            '*find-&prev',
            '-',
            '*find-&all',
            '*clone-fi&nd-all',
            '-',
            '*&change-next',
            '*change-a&ll',
            #'-',
            #'*&find-character',
            #'*find-character-extend-&selection',
            #'*&backward-find-character',
            #'*backward-find-character-&extend-selection',
            #'-',
            #'*&isearch-forward',
            #'*isea&rch-backward',
            #'*isearch-forward-rege&xp',
            #'*isearch-backward-regex&p',
            #'-',
            #'*&query-replace',
            #'*q&uery-replace-regex',
        ]
    #@-node:AGP.20250415230112.3013:defineEditMenuFindMenuTable
    #@+node:AGP.20250415230112.3014:defineEditMenuTop2Table
    def defineEditMenuTop2Table (self):
        
        c = self.c
    
        try:        show = c.frame.body.getColorizer().showInvisibles
        except:     show = False
        label = g.choose(show,"Hide In&visibles","Show In&visibles")
            
        self.editMenuTop2Table = [
            '*&goto-line-number',
            '*&execute-script',
            (label,'toggle-invisibles'),
            #("Setti&ngs",'open-leoSettings-leo'),
        ]
    
        # Top-level shortcuts earlier: a,d,p,t,u,y,z
        # Top-level shortcuts here: e,g,n,v
    #@-node:AGP.20250415230112.3014:defineEditMenuTop2Table
    #@-node:AGP.20250415230112.3009:defineEditMenuTables & helpers
    #@+node:AGP.20250415230112.3015:defineFileMenuTables & helpers
    def defineFileMenuTables (self):
    
        self.defineFileMenuTopTable()
        self.defineFileMenuTop2Table()
        self.defineFileMenuReadWriteMenuTable()
        self.defineFileMenuTangleMenuTable()
        self.defineFileMenuUntangleMenuTable()
        self.defineFileMenuImportMenuTable()
        self.defineFileMenuExportMenuTable()
        self.defineFileMenuTop3MenuTable()
    #@+node:AGP.20250415230112.3016:defineFileMenuTopTable
    def defineFileMenuTopTable (self):
        
        self.fileMenuTopTable = [
            '*&new',
            ('&Open...','open-outline'),
        ]
    #@-node:AGP.20250415230112.3016:defineFileMenuTopTable
    #@+node:AGP.20250415230112.3017:defineFileMenuTop2Table
    def defineFileMenuTop2Table (self):
        
        self.fileMenuTop2Table = [
            '-',
            ('&Close','close-window'),
            ('&Save','save-file'),
            ('Save &As','save-file-as'),
            ('Save &To','save-file-to'),
            ('Re&vert To Saved','revert'),
        ]
    #@-node:AGP.20250415230112.3017:defineFileMenuTop2Table
    #@+node:AGP.20250415230112.3018:defineFileMenuReadWriteMenuTable
    def defineFileMenuReadWriteMenuTable (self):
        
        self.fileMenuReadWriteMenuTable = [
            '*&read-outline-only',
            ('Read @file &Nodes','read-at-file-nodes'),
            ('Write &Dirty @file Nodes','write-dirty-at-file-nodes'),
            ('Write &Missing @file Nodes','write-missing-at-file-nodes'),
            '*write-&outline-only',
            ('&Write @file Nodes','write-at-file-nodes'),
        ]
    #@-node:AGP.20250415230112.3018:defineFileMenuReadWriteMenuTable
    #@+node:AGP.20250415230112.3019:defineFileMenuTangleMenuTable
    def defineFileMenuTangleMenuTable (self):
        
        self.fileMenuTangleMenuTable = [
            '*tangle-&all',
            '*tangle-&marked',
            '*&tangle',
        ]
    #@-node:AGP.20250415230112.3019:defineFileMenuTangleMenuTable
    #@+node:AGP.20250415230112.3020:defineFileMenuUntangleMenuTable
    def defineFileMenuUntangleMenuTable (self):
        
        self.fileMenuUntangleMenuTable = [
            '*untangle-&all',
            '*untangle-&marked',
            '*&untangle',
        ]
    #@-node:AGP.20250415230112.3020:defineFileMenuUntangleMenuTable
    #@+node:AGP.20250415230112.3021:defineFileMenuImportMenuTable
    def defineFileMenuImportMenuTable (self):
        
        self.fileMenuImportMenuTable = [
            #&: c,d,f,n,o,r,
            '*import-&derived-file',
            ('Import To @&file','import-at-file'),
            ('Import To @&root','import-at-root'),
            '*import-&cweb-files',
            '*import-&noweb-files',
            '*import-flattened-&outline',
        ]
    #@-node:AGP.20250415230112.3021:defineFileMenuImportMenuTable
    #@+node:AGP.20250415230112.3022:defineFileMenuExportMenuTable
    def defineFileMenuExportMenuTable (self):
        
        self.fileMenuExportMenuTable = [
            '*export-&headlines',
            '*outline-to-&cweb',
            '*outline-to-&noweb',
            '*&flatten-outline',
            '*&remove-sentinels',
            '*&weave',
        ]
    #@-node:AGP.20250415230112.3022:defineFileMenuExportMenuTable
    #@+node:AGP.20250415230112.3023:defineFileMenuTop3MenuTable
    def defineFileMenuTop3MenuTable (self):
        
        self.fileMenuTop3MenuTable = [
            ('Set Leo ID','set-leo-id'),
            ('E&xit','exit-leo')
        ]
    #@-node:AGP.20250415230112.3023:defineFileMenuTop3MenuTable
    #@-node:AGP.20250415230112.3015:defineFileMenuTables & helpers
    #@+node:AGP.20250415230112.3024:defineOutlineMenuTables & helpers
    def defineOutlineMenuTables (self):
    
        self.defineOutlineMenuTopMenuTable()
        self.defineOutlineMenuCheckOutlineMenuTable()
        self.defineOutlineMenuExpandContractMenuTable()
        self.defineOutlineMenuMoveMenuTable()
        self.defineOutlineMenuMarkMenuTable()
        self.defineOutlineMenuGoToMenuTable()
    #@+node:AGP.20250415230112.3025:defineOutlineMenuTopMenuTable
    def defineOutlineMenuTopMenuTable (self):
    
        self.outlineMenuTopMenuTable = [
            '*c&ut-node',
            '*c&opy-node',
            '*&paste-node',
            ('Pas&te Node As Clone','paste-retaining-clones'),
            '*&delete-node',
            '-',
            '*&insert-node',
            '*&clone-node',
            '*sort-childre&n',
            '*&sort-siblings',
            '-',
            '*&hoist',
            ('D&e-Hoist','de-hoist'), # To preserve the '-' in De-Hoist.
            '-',
        ]
        # Ampersand bindings:  a,b,c,d,e,h,i,n,o,p,t,s,y
        # Bindings for entries that go to submenus: a,g,k,m,x
    #@-node:AGP.20250415230112.3025:defineOutlineMenuTopMenuTable
    #@+node:AGP.20250415230112.3026:defineOutlineMenuCheckOutlineMenuTable
    def defineOutlineMenuCheckOutlineMenuTable (self):
        
        self.outlineMenuCheckOutlineMenuTable = [
            # &: a,c,d,o
            '*check-&outline',
            '*&dump-outline',
            '-',
            '*check-&all-python-code',
            '*&check-python-code',
        ]
    #@-node:AGP.20250415230112.3026:defineOutlineMenuCheckOutlineMenuTable
    #@+node:AGP.20250415230112.3027:defineOutlineMenuExpandContractMenuTable
    def defineOutlineMenuExpandContractMenuTable (self):
        
        self.outlineMenuExpandContractMenuTable = [
            '*&contract-all',
            '*contract-&node',
            '*contract-&parent',
            '*contract-or-go-&left',
            '-',
            '*expand-p&rev-level',
            '*expand-n&ext-level',
            '*expand-and-go-right',
            '*expand-or-go-right',
            '-',
            '*expand-to-level-&1',
            '*expand-to-level-&2',
            '*expand-to-level-&3',
            '*expand-to-level-&4',
            '*expand-to-level-&5',
            '*expand-to-level-&6',
            '*expand-to-level-&7',
            '*expand-to-level-&8',
            '-',
            '*expand-&all',
            '*expand-n&ode',
        ]
    #@-node:AGP.20250415230112.3027:defineOutlineMenuExpandContractMenuTable
    #@+node:AGP.20250415230112.3028:defineOutlineMenuMoveMenuTable
    def defineOutlineMenuMoveMenuTable (self):
        
        self.outlineMenuMoveMenuTable = [
            ('Move &Down','move-outline-down'),
            ('Move &Left','move-outline-left'),
            ('Move &Right','move-outline-right'),
            ('Move &Up','move-outline-up'),
            '-',
            '*&promote',
            '*&demote',
        ]
    #@-node:AGP.20250415230112.3028:defineOutlineMenuMoveMenuTable
    #@+node:AGP.20250415230112.3029:defineOutlineMenuMarkMenuTable
    def defineOutlineMenuMarkMenuTable (self):
        
        self.outlineMenuMarkMenuTable = [
            '*&mark',
            '*mark-&subheads',
            '*mark-changed-&items',
            '*mark-changed-&roots',
            '*mark-&clones',
            '*&unmark-all',
        ]
    #@-node:AGP.20250415230112.3029:defineOutlineMenuMarkMenuTable
    #@+node:AGP.20250415230112.3030:defineOutlineMenuGoToMenuTable
    def defineOutlineMenuGoToMenuTable (self):
    
        self.outlineMenuGoToMenuTable = [
            # &: a,c,d,e,g,i,l,m,n,o,p,r,s,t,v,x
            ('Go Prev Visite&d','go-back'),
            ('Go Next Visited','go-forward'),
            ('Go To P&rev Node','goto-prev-node'),
            ('Go To N&ext Node','goto-next-node'),
            '-',
            ('Go To Next &Marked','goto-next-marked'),
            ('Go To Next &Changed','goto-next-changed'),
            ('Go To Next &Clone','goto-next-clone'),
            '-',
            ('&Go To First Node','goto-first-node'),
            ('G&o To Prev Visible','goto-prev-visible'),
            ('Go To Ne&xt Visible','goto-next-visible'),
            ('Go To L&ast Node','goto-last-node'),
            ('Go To Last &Visible','goto-last-visible'),
            '-',
            ('Go To &Parent','goto-parent'),
            ('Go To First &Sibling','goto-first-sibling'),
            ('Go To Last S&ibling','goto-last-sibling'),
            ('Go To Prev Sibli&ng','goto-prev-sibling'),
            ('Go To Next Siblin&g','goto-next-sibling'),
        ]
    #@-node:AGP.20250415230112.3030:defineOutlineMenuGoToMenuTable
    #@-node:AGP.20250415230112.3024:defineOutlineMenuTables & helpers
    #@+node:AGP.20250415230112.3031:defineCmdsMenuTables & helpers
    def defineCmdsMenuTables (self):
        
        if 0: # Replaced by minibuffer submenu.
            self.defineCmdsMenuTopTable()
    
        self.defineCmdsMenuAbbrevTable()
        self.defineCmdsMenuBodyEditorsTable()
        self.defineCmdsMenuBuffersTable()
        self.defineCmdsMenuCursorTable()
        self.defineCmdsMenuFocusTable()
        self.defineCmdsMenuMacroTable()
        self.defineCmdsMenuMinibufferTable()
        self.defineCmdsMenuPanesTable()
        self.defineCmdsMenuPickersTable()
        self.defineCmdsMenuRectanglesTable()
        self.defineCmdsMenuRegistersTable()
        self.defineCmdsMenuScrollTable()
        self.defineCmdsMenuSpellCheckTable()
        self.defineCmdsMenuTextTable()
        self.defineCmdsMenuToggleTable()
    #@nonl
    #@+node:AGP.20250415230112.3032:defineCmdsMenuAbbrevTable
    def defineCmdsMenuAbbrevTable (self):
        
        self.cmdsMenuAbbrevTable = [
            # &: a,e,i,k,l,r,w,v
            'abbre&v-mode',
            '-',
            '&list-abbrevs',
            '&read-abbrev-file',
            '&write-abbrev-file',
            '-',
            '&add-global-abbrev',
            '&inverse-add-global-abbrev',
            '&kill-all-abbrevs',
            '-',
            # 'expand-abbrev', # Not a command
            '&expand-region-abbrevs',
        ]
    #@-node:AGP.20250415230112.3032:defineCmdsMenuAbbrevTable
    #@+node:AGP.20250415230112.3033:defineCmdsMenuBodyEditorsTable
    def defineCmdsMenuBodyEditorsTable (self):
    
        self.cmdsMenuBodyEditorsTable = [
            # &: a,c,d
            '&add-editor',
            '&cycle-editor-focus',
            '&delete-editor',
        ]
    #@nonl
    #@-node:AGP.20250415230112.3033:defineCmdsMenuBodyEditorsTable
    #@+node:AGP.20250415230112.3034:defineCmdsMenuBufferTable
    def defineCmdsMenuBuffersTable (self):
    
        self.cmdsMenuBuffersTable = [
            '&append-to-buffer',
            '&kill-buffer',
            'list-&buffers',
            '&list-buffers-alphabetically',
            '&prepend-to-buffer',
            '&rename-buffer',
            '&switch-to-buffer',
        ]
    #@-node:AGP.20250415230112.3034:defineCmdsMenuBufferTable
    #@+node:AGP.20250415230112.3035:defineCmdsMenuCursorTable
    def defineCmdsMenuCursorTable (self):
    
        self.cursorMenuBackTable = [
            # &: b,c,l,p,s,v,w
            'back-&char',
            'back-&paragraph',
            'back-&sentence',
            'back-&word',
            '-',
            'beginning-of-&buffer',
            'beginning-of-&line',
            '-',
            'pre&vious-line',
        ]
        
        self.cursorMeuuBackExtendTable = [
            # &: b,c,l,p,s,v,w
            'back-&char-extend-selection',
            'back-&paragraph-extend-selection',
            'back-&sentence-extend-selection',
            'back-&word-extend-selection',
            '-',
            'beginning-of-&buffer-extend-selection',
            'beginning-of-&line-extend-selection',
            '-',
            'pre&vious-line-extend-selection',
        ]
        
        self.cursorMenuExtendTable = [
            # &: l,p,s,w
            'extend-to-&line',
            'extend-to-&paragraph',
            'extend-to-&sentence',
            'extend-to-&word',
        ]
        
        self.cursorMenuForwardTable = [
            # &: b,c,e,l,n,p,s,w
            'end-of-&buffer',
            'end-of-&line',
            '-',
            'forward-&char',
            'forward-&paragraph',
            'forward-&sentence',
            'forward-&end-word',
            'forward-&word',
            '-',
            '&next-line',
        ]
        
        self.cursorMenuForwardExtendTable = [
            # &: b,c,e,l,n,p,s,w
            'end-of-&buffer-extend-selection',
            'end-of-&line-extend-selection',
            '-',
            'forward-&char-extend-selection',
            'forward-&paragraph-extend-selection',
            'forward-&sentence-extend-selection',
            'forward-&end-word-extend-selection',
            'forward-&word-extend-selection',#
            '-',
            '&next-line-extend-selection',    
        ]
    #@nonl
    #@-node:AGP.20250415230112.3035:defineCmdsMenuCursorTable
    #@+node:AGP.20250415230112.3036:defineCmdsMenuFocusTable
    def defineCmdsMenuFocusTable (self):
    
        self.cmdsMenuFocusTable = [
            '&cycle-all-focus',
            'focus-to-&body',          
            'focus-to-&log',             
            'focus-to-&minibuffer',     
            'focus-to-&tree',             
        ]
    #@-node:AGP.20250415230112.3036:defineCmdsMenuFocusTable
    #@+node:AGP.20250415230112.3037:defineCmdsMenuMacroTable
    def defineCmdsMenuMacroTable (self):
    
        self.cmdsMenuMacroTable = [
            '&load-file',
            '-',
            '&start-kbd-macro',
            '&end-kbd-macro',
            '&name-last-kbd-macro',
            '-',
            '&call-last-keyboard-macro',
            '&insert-keyboard-macro',
        ]
    #@-node:AGP.20250415230112.3037:defineCmdsMenuMacroTable
    #@+node:AGP.20250415230112.3038:defineCmdsMenuMinibufferTable
    def defineCmdsMenuMinibufferTable (self):
        
        self.cmdsMenuMinibufferTable = [
            # &: f,h,i,q,r,s,v
            '&full-command',
            'keyboard-&quit',
            '&repeat-complex-command',
            '&view-lossage',
            '-',
            '&show-mini-buffer',
            'h&ide-mini-buffer',
            '-',
            '&help-for-minibuffer',
        ]
    #@-node:AGP.20250415230112.3038:defineCmdsMenuMinibufferTable
    #@+node:AGP.20250415230112.3039:defineCmdsMenuPanesTable
    def defineCmdsMenuPanesTable (self):
    
        self.cmdsMenuPanesTable = [
            # &: a,b,d,f,l,n,o,p,u,x,y
            'contract-&body-pane',
            'contract-&log-pane',
            'contract-&outline-pane',
            'contract-&pane',
            '-',
            'expand-bo&dy-pane',
            'expand-lo&g-pane',
            'expand-o&utline-pane',
            'expand-pa&ne',
            '-',
            '&fully-expand-body-pane',
            'full&y-expand-log-pane',
            'fully-e&xpand-outline-pane',
            'fully-exp&and-pane',
        ]
        
    #@nonl
    #@-node:AGP.20250415230112.3039:defineCmdsMenuPanesTable
    #@+node:AGP.20250415230112.3040:defineCmdsMenuPickersTable
    def defineCmdsMenuPickersTable (self):
        
        self. cmdsMenuPickersTable = [
            'show-&colors',
            'show-find-&options',
            'show-&fonts',
        ]
    #@nonl
    #@-node:AGP.20250415230112.3040:defineCmdsMenuPickersTable
    #@+node:AGP.20250415230112.3041:defineCmdsMenuRectanglesTable
    def defineCmdsMenuRectanglesTable (self):
    
        self.cmdsMenuRectanglesTable = [
            '&clear-rectangle',
            'c&lose-rectangle',
            '&delete-rectangle',
            '&kill-rectangle',
            '&open-rectangle',
            '&string-rectangle',
            '&yank-rectangle',
        ]
    #@-node:AGP.20250415230112.3041:defineCmdsMenuRectanglesTable
    #@+node:AGP.20250415230112.3042:defineCmdsMenuRegistersTable
    def defineCmdsMenuRegistersTable (self):
    
        self.cmdsMenuRegistersTable = [
            # &: a,c,e,i,j,n,p,r,v
            '&append-to-register',
            'copy-r&ectangle-to-register',
            '&copy-to-register',
            'i&ncrement-register',
            '&insert-register',
            '&jump-to-register',
            # 'number-to-register',
            '&point-to-register',
            'p&repend-to-register',
            '&view-register',
        ]
    #@-node:AGP.20250415230112.3042:defineCmdsMenuRegistersTable
    #@+node:AGP.20250415230112.3043:defineCmdsMenuScrollTable
    def defineCmdsMenuScrollTable (self):
    
        self.cmdsMenuScrollTable = [
            # &: c,d,e,f,l,o,p,r,v,x
            'scroll-outline-down-&line',
            'scroll-outline-down-&page',
            'scroll-outline-le&ft',
            'scroll-outline-&right',
            's&croll-outline-up-line',
            'scr&oll-outline-up-page',
            '-',
            'scroll-&down',
            'scroll-&up',
            '-',
            'scroll-down-&extend-selection',
            'scroll-up-e&xtend-selection',
        ]
    #@nonl
    #@-node:AGP.20250415230112.3043:defineCmdsMenuScrollTable
    #@+node:AGP.20250415230112.3044:defineCmdsMenuSpellCheckTable
    def defineCmdsMenuSpellCheckTable (self):
    
        self.cmdsMenuSpellCheckTable = [
            '&open-spell-tab',
            'spell-&change',
            'spell-change-&then-find',
            'spell-&find',
            'spell-&ignore',
        ]
    #@-node:AGP.20250415230112.3044:defineCmdsMenuSpellCheckTable
    #@+node:AGP.20250415230112.3045:defineCmdsMenuTextTable
    def defineCmdsMenuTextTable (self):
    
        self.cmdsMenuTextTable = [
            # &: a,b,c,d,e,f,g,i,l,m,n,o,p,r,s,u
            '&beautify',
            'beautify-&all',
            '-',
            'center-&line',
            'center-&region',
            '-',
            '&capitalize-word',
            '&downcase-word',
            '&upcase-word',
            '-',
            'd&owncase-region',
            'u&pcase-region',
            '-',
            '&indent-region',
            'indent-r&elative',
            'indent-ri&gidly',
            'u&nindent-region',
            '-',
            'sort-colu&mns',
            'sort-&fields',
            '&sort-lines',
        ]
    #@nonl
    #@-node:AGP.20250415230112.3045:defineCmdsMenuTextTable
    #@+node:AGP.20250415230112.3046:defineCmdsMenuToggleTable
    def defineCmdsMenuToggleTable (self):
    
        self.cmdsMenuToggleTable = [
            # &: d,e,m,s,t,u,v
            'toggle-a&utocompleter',
            'toggle-call&tips',
            'toggle-&extend-mode',
            'toggle-input-&state',
            'toggle-in&visibles',
            'toggle-&mini-buffer',
            'toggle-split-&direction',
            '-',
            # &: a,b,c,f,h,i,r,w,x
            'toggle-find-&ignore-case-option',
            'toggle-find-in-&body-option',
            'toggle-find-in-&headline-option',
            'toggle-find-mark-&changes-option',
            'toggle-find-mark-&finds-option',
            'toggle-find-rege&x-option',
            'toggle-find-&reverse-option',
            'toggle-find-&word-option',
            'toggle-find-wrap-&around-option',
        ]
    #@-node:AGP.20250415230112.3046:defineCmdsMenuToggleTable
    #@-node:AGP.20250415230112.3031:defineCmdsMenuTables & helpers
    #@+node:AGP.20250415230112.3047:defineWindowMenuTables
    def defineWindowMenuTables (self):
        
        self.windowMenuTopTable = [
            # &: a,c,e,m,o,p,r,s
            '*&equal-sized-panes',
            '*toggle-&active-pane',
            '*toggle-&split-direction',
            '-',
            '*&resize-to-screen',
            '*&cascade-windows',
            '*&minimize-all',
            #'-',
            #'*&open-compare-window',
            #'*open-&python-window',
        ]
    #@-node:AGP.20250415230112.3047:defineWindowMenuTables
    #@+node:AGP.20250415230112.3048:defineHelpMenuTables
    def defineHelpMenuTables (self):
        
        self.helpMenuTable = [
            # &: a,b,c,d,f,h,l,m,n,o,p,r,s,t,u
            ('&About Leox...',   'about-leo'),
            #('Online &Home Page',       'open-online-home'),
            #'*open-online-&tutorial',
            #'*open-&users-guide',
            '-',
            ('Documentation',   'open-leoDocs-leo'),
            ('Plugins',         'open-leoPlugins-leo'),
            ('Settings',        'open-leoSettings-leo'),
            #('Open &myLeoSettings.leo', 'open-myLeoSettings-leo'),
            #('Open scr&ipts.leo',       'open-scripts-leo'),
            #'-',
            #'*he&lp-for-minibuffer',
            #'*help-for-&command',
            #'-',
            #'*&apropos-autocompletion',
            #'*apropos-&bindings',
            #'*apropos-&find-commands',
            '-',
            '*pri&nt-bindings',
            #'*print-c&ommands',
        ]
    #@-node:AGP.20250415230112.3048:defineHelpMenuTables
    #@-node:AGP.20250415230112.3008:defineMenuTables & helpers
    #@+node:AGP.20250415230112.3049:Helpers
    #@+node:AGP.20250415230112.3050:canonicalizeMenuName & cononicalizeTranslatedMenuName
    def canonicalizeMenuName (self,name):
        
        return ''.join([ch for ch in name.lower() if ch.isalnum()])
        
    def canonicalizeTranslatedMenuName (self,name):
        
        return ''.join([ch for ch in name.lower() if ch not in u'& \t\n\r'])
    
    #@-node:AGP.20250415230112.3050:canonicalizeMenuName & cononicalizeTranslatedMenuName
    #@+node:AGP.20250415230112.3051:computeOldStyleShortcutKey
    def computeOldStyleShortcutKey (self,s):
        
        '''Compute the old-style shortcut key for @shortcuts entries.'''
        
        return ''.join([ch for ch in s.strip().lower() if ch.isalnum()])
    #@-node:AGP.20250415230112.3051:computeOldStyleShortcutKey
    #@+node:AGP.20250415230112.3052:createMenuEntries
    def createMenuEntries (self,menu,table,dynamicMenu=False):
            
        '''Create a menu entry from the table.
        New in 4.4: this method shows the shortcut in the menu,
        but this method **never** binds any shortcuts.'''
        
        c = self.c ; f = c.frame ; k = c.k
        if g.app.unitTesting: return
        for data in table:
            #@        << get label & command or continue >>
            #@+node:AGP.20250415230112.3053:<< get label & command or continue >>
            if type(data) == type(''):
                # New in Leo 4.4.2: Can use the same string for both the label and the command string.
                ok = True
                s = data
                removeHyphens = s and s[0]=='*'
                if removeHyphens: s = s[1:]
                label = self.capitalizeMinibufferMenuName(s,removeHyphens)
                #print label
                command = s.replace('&','').lower()
                if label == '-':
                    self.add_separator(menu)
                    continue # That's all.
            else:
                ok = type(data) in (type(()), type([])) and len(data) in (2,3)
                if ok:
                    if len(data) == 2:
                        # New in 4.4b2: command can be a minibuffer-command name (a string)
                        label,command = data
                    else:
                        # New in 4.4: we ignore shortcuts bound in menu tables.
                        label,junk,command = data
                        
                    if label in (None,'-'):
                        self.add_separator(menu)
                        continue # That's all.
                else:
                    g.trace('bad data in menu table: %s' % repr(data))
                    continue # Ignore bad data
            #@nonl
            #@-node:AGP.20250415230112.3053:<< get label & command or continue >>
            #@nl
            #@        << compute commandName & accel from label & command >>
            #@+node:AGP.20250415230112.3054:<< compute commandName & accel from label & command >>
            # New in 4.4b2: command can be a minibuffer-command name (a string)
            minibufferCommand = type(command) == type('')
            accel = None
            if minibufferCommand:
                commandName = command 
                command = c.commandsDict.get(commandName)
                if command:
                    rawKey,bunchList = c.config.getShortcut(commandName)
                    # Pick the first entry that is not a mode.
                    for bunch in bunchList:
                        if not bunch.pane.endswith('-mode'):
                            # g.trace('1',bunch)
                            accel = bunch and bunch.val
                            if bunch.pane  == 'text': break # New in Leo 4.4.2: prefer text bindings.
                else:
                    if not g.app.unitTesting and not dynamicMenu:
                        # Don't warn during unit testing.
                        # This may come from a plugin that normally isn't enabled.
                        #g.trace('No inverse for %s' % commandName)
                        pass
                    continue # There is no way to make this menu entry.
            else:
                # First, get the old-style name.
                commandName = self.computeOldStyleShortcutKey(label)
                rawKey,bunchList = c.config.getShortcut(commandName)
                for bunch in bunchList:
                    if not bunch.pane.endswith('-mode'):
                        # g.trace('2',bunch)
                        accel = bunch and bunch.val ; break
                # Second, get new-style name.
                if not accel:
                    #@        << compute emacs_name >>
                    #@+node:AGP.20250415230112.3055:<< compute emacs_name >>
                    #@+at 
                    #@nonl
                    # One not-so-horrible kludge remains.
                    # 
                    # The cut/copy/paste commands in the menu tables are not 
                    # the same as the methods
                    # actually bound to cut/copy/paste-text minibuffer 
                    # commands, so we must do a bit
                    # of extra translation to discover whether the user has 
                    # overridden their
                    # bindings.
                    #@-at
                    #@@c
                    
                    if command in (f.OnCutFromMenu,f.OnCopyFromMenu,f.OnPasteFromMenu):
                        emacs_name = '%s-text' % commandName
                    else:
                        try: # User errors in the table can cause this.
                            emacs_name = k.inverseCommandsDict.get(command.__name__)
                        except Exception:
                            emacs_name = None
                    #@-node:AGP.20250415230112.3055:<< compute emacs_name >>
                    #@nl
                        # Contains the not-so-horrible kludge.
                    if emacs_name:
                        commandName = emacs_name
                        rawKey,bunchList = c.config.getShortcut(emacs_name)
                        # Pick the first entry that is not a mode.
                        for bunch in bunchList:
                            if not bunch.pane.endswith('-mode'):
                                accel = bunch.val ; break
                                # g.trace('2',bunch)
                    elif not dynamicMenu:
                        #g.trace('No inverse for %s' % commandName)
                        pass
            #@-node:AGP.20250415230112.3054:<< compute commandName & accel from label & command >>
            #@nl
            accelerator = stroke = k.shortcutFromSetting(accel) or ''
            accelerator = accelerator and g.stripBrackets(k.prettyPrintKey(accelerator))
            def masterMenuCallback (k=k,stroke=stroke,command=command,commandName=commandName):
                return k.masterMenuHandler(stroke,command,commandName)
            realLabel = self.getRealMenuName(label)
            amp_index = realLabel.find("&")
            realLabel = realLabel.replace("&","")
            if sys.platform == 'darwin':
                #@            << clear accelerator if it is a plain key >>
                #@+node:AGP.20250415230112.3056:<< clear accelerator if it is a plain key >>
                for z in ('Alt','Ctrl','Command'):
                    if accelerator.find(z) != -1:
                        break # Found.
                else:
                    accelerator = ''
                #@-node:AGP.20250415230112.3056:<< clear accelerator if it is a plain key >>
                #@nl
            self.add_command(menu,label=realLabel,
                accelerator=accelerator,
                command=masterMenuCallback,
                underline=amp_index)
    #@-node:AGP.20250415230112.3052:createMenuEntries
    #@+node:AGP.20250415230112.3057:createMenuItemsFromTable
    def createMenuItemsFromTable (self,menuName,table,dynamicMenu=False):
        
        try:
            menu = self.getMenu(menuName)
            if menu == None:
                print "menu does not exist: ",menuName
                g.es("menu does not exist: ",menuName)
                return
            self.createMenuEntries(menu,table,dynamicMenu=dynamicMenu)
        except:
            s = "exception creating items for %s menu" % menuName
            g.es_print(s)
            g.es_exception()
            
        g.app.menuWarningsGiven = True
    #@-node:AGP.20250415230112.3057:createMenuItemsFromTable
    #@+node:AGP.20250415230112.3058:createNewMenu agp
    def createNewMenu (self,menuName,parentName=None,before=None,postc=None):
        
        if not postc:
            postc=self.updateAllMenus
        
        try:
            parent = None
            
            menu = self.getMenu(menuName)
            if menu:
                g.es("menu already exists: " + menuName,color="red")
            else:
                if parentName and parentName!='top':
                    parent = self.getMenu(parentName)
            
                menu = self.new_menu(parent,tearoff=0,postc=postc)
                
                label = self.getRealMenuName(menuName)
                amp_index = label.find("&")
                label = label.replace("&","")
                
                self.setMenu(menuName,menu)
                
                
                if parent:
                    #print parent,parentName,menuName
                    if before: # Insert the menu before the "before" menu.
                        index_label = self.getRealMenuName(before)
                        amp_index = index_label.find("&")
                        index_label = index_label.replace("&","")
                        index = parent.index(index_label)
                        self.insert_cascade(parent,index=index,label=label,menu=menu,underline=amp_index)
                    else:
                        self.add_cascade(parent,label=label,menu=menu,underline=amp_index)
                else:
                    menu.mb.config(text=label)
                    
                return menu
        except:
            g.es("exception creating " + menuName + " menu")
            g.es_exception()
            return None
    #@-node:AGP.20250415230112.3058:createNewMenu agp
    #@+node:AGP.20250415230112.3059:xcreateNewMenu
    def xcreateNewMenu (self,menuName,parentName="top",before=None):
    
        try:
            parent = self.getMenu(parentName) # parent may be None.
            menu = self.getMenu(menuName)
            if menu:
                g.es("menu already exists: " + menuName,color="red")
            else:
                menu = self.new_menu(parent,tearoff=0)
                self.setMenu(menuName,menu)
                label = self.getRealMenuName(menuName)
                amp_index = label.find("&")
                label = label.replace("&","")
                if before: # Insert the menu before the "before" menu.
                    index_label = self.getRealMenuName(before)
                    amp_index = index_label.find("&")
                    index_label = index_label.replace("&","")
                    index = parent.index(index_label)
                    self.insert_cascade(parent,index=index,label=label,menu=menu,underline=amp_index)
                else:
                    self.add_cascade(parent,label=label,menu=menu,underline=amp_index)
                    pass
                return menu
        except:
            g.es("exception creating " + menuName + " menu")
            g.es_exception()
            return None
    #@-node:AGP.20250415230112.3059:xcreateNewMenu
    #@+node:AGP.20250415230112.3060:createOpenWithMenuFromTable & helper
    def createOpenWithMenuFromTable (self,table):
        
        '''Entries in the table passed to createOpenWithMenuFromTable are
    tuples of the form (commandName,shortcut,data).
    
    - command is one of "os.system", "os.startfile", "os.spawnl", "os.spawnv" or "exec".
    - shortcut is a string describing a shortcut, just as for createMenuItemsFromTable.
    - data is a tuple of the form (command,arg,ext).
    
    Leo executes command(arg+path) where path is the full path to the temp file.
    If ext is not None, the temp file has the given extension.
    Otherwise, Leo computes an extension based on the @language directive in effect.'''
    
        c = self.c
        g.app.openWithTable = table # Override any previous table.
        # Delete the previous entry.
        parent = self.getMenu("File")
        label = self.getRealMenuName("Open &With...")
        amp_index = label.find("&")
        label = label.replace("&","")
        try:
            index = parent.index(label)
            parent.delete(index)
        except:
            try:
                index = parent.index("Open With...")
                parent.delete(index)
            except: return
        # Create the Open With menu.
        openWithMenu = self.createOpenWithMenu(parent,label,index,amp_index)
        self.setMenu("Open With...",openWithMenu)
        # Create the menu items in of the Open With menu.
        for entry in table:
            if len(entry) != 3: # 6/22/03
                g.es("createOpenWithMenuFromTable: invalid data",color="red")
                return
        self.createOpenWithMenuItemsFromTable(openWithMenu,table)
        for entry in table:
            name,shortcut,data = entry
            c.k.bindOpenWith (shortcut,name,data)
    #@+node:AGP.20250415230112.3061:createOpenWithMenuItemsFromTable
    def createOpenWithMenuItemsFromTable (self,menu,table):
        
        '''Create an entry in the Open with Menu from the table.
        
        Each entry should be a sequence with 2 or 3 elements.'''
        
        c = self.c ; k = c.k
    
        if g.app.unitTesting: return
    
        for data in table:
            #@        << get label, accelerator & command or continue >>
            #@+node:AGP.20250415230112.3062:<< get label, accelerator & command or continue >>
            ok = (
                type(data) in (type(()), type([])) and
                len(data) in (2,3)
            )
                
            if ok:
                if len(data) == 2:
                    label,openWithData = data ; accelerator = None
                else:
                    label,accelerator,openWithData = data
                    accelerator = k.shortcutFromSetting(accelerator)
                    accelerator = accelerator and g.stripBrackets(k.prettyPrintKey(accelerator))
            else:
                g.trace('bad data in Open With table: %s' % repr(data))
                continue # Ignore bad data
            #@-node:AGP.20250415230112.3062:<< get label, accelerator & command or continue >>
            #@nl
            realLabel = self.getRealMenuName(label)
            underline=realLabel.find("&")
            realLabel = realLabel.replace("&","")
            callback = self.defineOpenWithMenuCallback(openWithData)
        
            self.add_command(menu,label=realLabel,
                accelerator=accelerator or '',
                command=callback,underline=underline)
    #@-node:AGP.20250415230112.3061:createOpenWithMenuItemsFromTable
    #@-node:AGP.20250415230112.3060:createOpenWithMenuFromTable & helper
    #@+node:AGP.20250415230112.3063:createRecentFilesMenuItems (leoMenu)
    def createRecentFilesMenuItems (self):
        
        c = self.c
        recentFilesMenu = self.getMenu("Open Recent File...")
        
        # Delete all previous entries.
        self.delete_range(recentFilesMenu,0,len(c.recentFiles)+2)
        
        # Create the first two entries.
        table = (
            ("Clear Recent Files",None,c.clearRecentFiles),
            ("-",None,None))
        self.createMenuEntries(recentFilesMenu,table)
        
        # Create all the other entries.
        i = 3
        for name in c.recentFiles:
            def recentFilesCallback (event=None,c=c,name=name):
                c.openRecentFile(name)
            accel_ch = (string.digits + string.letters.upper()) # Not a unicode problem.
            label = "%s %s" % (accel_ch[i-2],g.computeWindowTitle(name))
            self.add_command(recentFilesMenu,label=label,command=recentFilesCallback,underline=0)
            i += 1
    #@-node:AGP.20250415230112.3063:createRecentFilesMenuItems (leoMenu)
    #@+node:AGP.20250415230112.3064:defineMenuCallback
    def defineMenuCallback(self,command,name,minibufferCommand):
        
        if minibufferCommand:
            
            # Create a dummy event as a signal to doCommand.
            event = g.Bunch(keysym='',char='',widget='')
            
            # The first parameter must be event, and it must default to None.
            def minibufferMenuCallback(event=event,self=self,command=command,label=name):
                
                c = self.c
                return c.doCommand(command,label,event)
        
            return minibufferMenuCallback
            
        else:
        
            # The first parameter must be event, and it must default to None.
            def legacyMenuCallback(event=None,self=self,command=command,label=name):
                
                c = self.c
                return c.doCommand(command,label)
        
            return legacyMenuCallback
    #@-node:AGP.20250415230112.3064:defineMenuCallback
    #@+node:AGP.20250415230112.3065:defineOpenWithMenuCallback
    def defineOpenWithMenuCallback(self,data):
        
        # The first parameter must be event, and it must default to None.
        def openWithMenuCallback(event=None,self=self,data=data):
            return self.c.openWith(data=data)
    
        return openWithMenuCallback
    #@-node:AGP.20250415230112.3065:defineOpenWithMenuCallback
    #@+node:AGP.20250415230112.3066:deleteMenu
    def deleteMenu (self,menuName):
    
        try:
            menu = self.getMenu(menuName)
            if menu:
                self.destroy(menu)
                self.destroyMenu(menuName)
            else:
                g.es("can't delete menu: " + menuName)
        except:
            g.es("exception deleting " + menuName + " menu")
            g.es_exception()
    #@-node:AGP.20250415230112.3066:deleteMenu
    #@+node:AGP.20250415230112.3067:deleteMenuItem
    def deleteMenuItem (self,itemName,menuName="top"):
        
        """Delete itemName from the menu whose name is menuName."""
    
        try:
            menu = self.getMenu(menuName)
            if menu:
                realItemName = self.getRealMenuName(itemName)
                self.delete(menu,realItemName)
            else:
                g.es("menu not found: " + menuName)
        except:
            g.es("exception deleting " + itemName + " from " + menuName + " menu")
            g.es_exception()
    #@-node:AGP.20250415230112.3067:deleteMenuItem
    #@+node:AGP.20250415230112.3068:get/setRealMenuName & setRealMenuNamesFromTable
    # Returns the translation of a menu name or an item name.
    
    def getRealMenuName (self,menuName):
    
        cmn = self.canonicalizeTranslatedMenuName(menuName)
        return g.app.realMenuNameDict.get(cmn,menuName)
        
    def setRealMenuName (self,untrans,trans):
    
        cmn = self.canonicalizeTranslatedMenuName(untrans)
        g.app.realMenuNameDict[cmn] = trans
    
    def setRealMenuNamesFromTable (self,table):
    
        try:
            for untrans,trans in table:
                self.setRealMenuName(untrans,trans)
        except:
            g.es("exception in setRealMenuNamesFromTable")
            g.es_exception()
    #@-node:AGP.20250415230112.3068:get/setRealMenuName & setRealMenuNamesFromTable
    #@+node:AGP.20250415230112.3069:getMenu, setMenu, destroyMenu
    def getMenu (self,menuName):
    
        cmn = self.canonicalizeMenuName(menuName)
        return self.menus.get(cmn)
        
    def setMenu (self,menuName,menu):
        
        cmn = self.canonicalizeMenuName(menuName)
        self.menus [cmn] = menu
        
    def destroyMenu (self,menuName):
        
        cmn = self.canonicalizeMenuName(menuName)
        del self.menus[cmn]
    #@-node:AGP.20250415230112.3069:getMenu, setMenu, destroyMenu
    #@-node:AGP.20250415230112.3049:Helpers
    #@-node:AGP.20250415230112.2985:Gui-independent menu routines
    #@+node:AGP.20250415230112.3070:Must be overridden in menu subclasses
    #@+node:AGP.20250415230112.3071:9 Routines with Tk spellings
    def add_cascade (self,parent,label,menu,underline):
        self.oops()
        
    def add_command (self,menu,**keys):
        self.oops()
        
    def add_separator(self,menu):
        self.oops()
        
    def bind (self,bind_shortcut,callback):
        self.oops()
    
    def delete (self,menu,realItemName):
        self.oops()
        
    def delete_range (self,menu,n1,n2):
        self.oops()
    
    def destroy (self,menu):
        self.oops()
    
    def insert_cascade (self,parent,index,label,menu,underline):
        self.oops()
    
    def new_menu(self,parent,tearoff=0):
        self.oops()
    #@-node:AGP.20250415230112.3071:9 Routines with Tk spellings
    #@+node:AGP.20250415230112.3072:9 Routines with new spellings
    def activateMenu (self,menuName): # New in Leo 4.4b2.
        self.oops()
    
    def clearAccel (self,menu,name):
        self.oops()
    
    def createMenuBar (self,frame):
        self.oops()
        
    if 0: # Now defined in the base class
        def createOpenWithMenuFromTable (self,table):
            self.oops()
    
        def defineMenuCallback(self,command,name):
            self.oops()
            
        def defineOpenWithMenuCallback(self,command):
            self.oops()
        
    def disableMenu (self,menu,name):
        self.oops()
        
    def enableMenu (self,menu,name,val):
        self.oops()
        
    def getManuLabel (self,menu):
        self.oops()
        
    def setMenuLabel (self,menu,name,label,underline=-1):
        self.oops()
    #@-node:AGP.20250415230112.3072:9 Routines with new spellings
    #@-node:AGP.20250415230112.3070:Must be overridden in menu subclasses
    #@-others
#@-node:AGP.20250415230112.2970:class leoMenu
#@+node:AGP.20250415230112.3073:class nullMenu
class nullMenu(leoMenu):
    
    """A null menu class for testing and batch execution."""
    
    
    #@    @+others
    #@+node:AGP.20250415230112.3074:ctor
    def __init__ (self,frame):
        
        # Init the base class.
        leoMenu.__init__(self,frame)
    #@-node:AGP.20250415230112.3074:ctor
    #@+node:AGP.20250415230112.3075:oops
    def oops (self):
    
        # g.trace("leoMenu", g.callers())
        pass
    #@-node:AGP.20250415230112.3075:oops
    #@-others
#@-node:AGP.20250415230112.3073:class nullMenu
#@-others
#@-node:AGP.20250415230112.2969:@thin leoMenu.py
#@-leo
