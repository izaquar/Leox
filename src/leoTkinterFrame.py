# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:ekr.20031218072017.3939:@thin leoTkinterFrame.py
#@@first

#@@language python
#@@tabwidth -4
#@@pagewidth 80

#@<< imports >>
#@+node:ekr.20041221070525:<< imports >>
import leoGlobals as g

import leoColor,leoFrame,leoNodes
import leoTkinterMenu
import leoTkinterTree
import leoFind

import Tkinter as Tk
import tkFont
import os
import string
import sys

#Pmw = g.importExtension("Pmw",pluginName="leoTkinterFrame.py",verbose=False)

# The following imports _are_ used.
__pychecker__ = '--no-import'
import threading
import time
#@-node:ekr.20041221070525:<< imports >>
#@nl

#@+others
#@+node:AGP.20231124085841:class History
class History(Tk.Entry):
    #@    @+others
    #@+node:AGP.20231124085841.1:__init__()
    def __init__(self,c,parent,width=30,bd=2,):
        
        self.var = Tk.StringVar()
        
        Tk.Entry.__init__(self,parent,width=30,bd=2,
                            highlightthickness=1,#highlightcolor=g.theme['accent'],
                            exportselection=0,textvariable=self.var)#,font=c.frame.iconbarfont)#,takefocus=1))
        
        self.bind("<Key>", self.onKey)
        self.bind("<FocusIn>", self.onFocusIn)
        self.bind("<FocusOut>", self.onFocusOut)
        self.bind("<Button-1>", self.onLeftClick)
        
        self.history = []
        self.lmenu = None
        
        self.action = None
        
        
    
        
        
    #@nonl
    #@-node:AGP.20231124085841.1:__init__()
    #@+node:AGP.20231124085841.2:onKey
    def onKey (self,event=None): 
        """Called when the user presses a key in the text entry box"""
        
        if self.lmenu != None:
            self.lmenu.destroy()
            self.lmenu = None
        
        if event.keysym == "Return":
            sv = self.var.get()
            if sv != "" and not sv in self.history:
                self.history.insert(0,sv)
                
            if self.action != None:
                self.action()
    #@-node:AGP.20231124085841.2:onKey
    #@+node:AGP.20231124085841.3:onFocusIn()
    def onFocusIn(self,event):
        self.select_range(0, Tk.END)
    #@-node:AGP.20231124085841.3:onFocusIn()
    #@+node:AGP.20231124085841.4:onFocusOut()
    def onFocusOut(self,event):
        if self.lmenu != None:
            self.lmenu.destroy()
            self.lmenu = None
    #@nonl
    #@-node:AGP.20231124085841.4:onFocusOut()
    #@+node:AGP.20231124085841.5:onLeftClick()
    def onLeftClick(self,event):
        
        if self.lmenu != None:
            self.lmenu.destroy()
            self.lmenu = None
        
        h = self.history
        if len(h) > 0:
            self.lmenu = lmenu = Tk.Listbox(
                                                self.winfo_toplevel(),
                                                width=30,
                                                height=len(h),
                                                takefocus=0,
                                                bg="white",
                                                activestyle="none",
                                                selectmode=Tk.SINGLE
                                            )
            
            lmenu.bind("<Motion>", self.onMenuMotion)
            lmenu.bind("<Button-1>", self.onMenuLeftClick)
            
            
            for s in h:
                lmenu.insert(Tk.END,s)
            
            
            
            x= event.widget.winfo_x()
            y= event.widget.winfo_y()
            h= event.widget.winfo_height()
            
            #print x,y,h
            lmenu.place(x=x+1,y=y+h,anchor=Tk.NW)
            
            
        
            
        
    #@nonl
    #@-node:AGP.20231124085841.5:onLeftClick()
    #@+node:AGP.20231124085841.6:onMenuLeftClick()
    def onMenuLeftClick(self,event):
        self.var.set(self.lmenu.get(self.lmenu.curselection()[0]))
        self.focus_set()
        
        self.lmenu.destroy()
        self.lmenu = None
        
        return "break"
    #@nonl
    #@-node:AGP.20231124085841.6:onMenuLeftClick()
    #@+node:AGP.20231124085841.7:onMenuMotion()
    def onMenuMotion(self,event):
        self.lmenu.selection_clear(0,Tk.END)
        self.lmenu.selection_set(self.lmenu.nearest(event.y))
    #@nonl
    #@-node:AGP.20231124085841.7:onMenuMotion()
    #@-others
#@nonl
#@-node:AGP.20231124085841:class History
#@+node:AGP.20231124085809:class SearchBox
class SearchBox(leoFind.leoFind):

    #@    @+others
    #@+node:AGP.20231124085809.1:__init__()
    def __init__ (self,c):
        # Init the base class.
        leoFind.leoFind.__init__(self,c)
        
        self.c = c
        self.s_ctrl = Tk.Text() # Used by find.search()
        
        #self.top = self #leo will call panel.top.destroy() in destroyallpanels()... see destroy() dummy
        
        #c.searchCommands.openFindTab(show=False)
        #self.finder = c.searchCommands.findTabHandler 
        #print self.findtab.dict.keys()
        
        c.searchCommands.finder = self
        
        self.finder = self
        
        self.rmenu = None
        
        
        
        
        #@    @+others
        #@+node:AGP.20231124085809.2:init vars
        #tkinter ivars
        #self.searchvar = Tk.StringVar()
        #self.changevar = Tk.StringVar()
        
        self.dict = vd = {}
        
        for key in self.intKeys:
            vd[key] = Tk.IntVar()
        
        for key in self.newStringKeys:
            vd[key] = Tk.StringVar()
        
                
        #set some default options
        vd["search_headline"].set(1)
        vd["search_body"].set(1)
        vd["ignore_case"].set(1)
        vd["wrap"].set(1)
        vd["radio-search-scope"].set("entire-outline")
        
        #for k in vd.keys():
        #    print k,vd[k].get()
        #@nonl
        #@-node:AGP.20231124085809.2:init vars
        #@+node:AGP.20231124085809.3:create widgets
        #create widgets
        
        if not hasattr(c.frame,"iconFrame"):    #fix for nullframe
            return None
        
        self.toolbar = toolbar = c.frame.menuFrame
        
        c.frame.searchbox = self
        
        self.changebox = cb = History(c,toolbar)
        cb.bind("<MouseWheel>",c.frame.TopMouseWheel)
        
        self.tolabel = Tk.Label(toolbar,text="To")#,font=c.frame.iconbarfont)
        
        
        self.searchbox = sb = History(c,toolbar)   
        sb.bind("<MouseWheel>",c.frame.TopMouseWheel)
        #sb.bind("<Key>", self.onKey)
        sb.bind("<Button-3>", self.onRightClick)
        
        self.action_button = ab = Tk.Menubutton(toolbar,text="Find",activebackground="light sky blue")#,font=c.frame.iconbarfont)
        
        
        self.action_menu = am = Tk.Menu(ab,tearoff=0,takefocus=0)
        ab["menu"] = am
        
        self.find_repack()
        
        #@+others
        #@+node:AGP.20231124085809.4:Options menu
        self.rmenu = rmenu = Tk.Menu(self.searchbox.winfo_toplevel(),tearoff=0,takefocus=1)
            
        vd = self.dict
            
        #for k in vd.keys():
        #    print k,vd[k].get()
        
        fg = rmenu['fg']
        
        rmenu.add_checkbutton(label="Search Headline",variable=vd["search_headline"],selectcolor=fg)
        rmenu.add_checkbutton(label="Search Body",variable=vd["search_body"],selectcolor=fg)
            
            
        rmenu.add_separator()
        #rmenu.add_command(label="_________________")
            
        rmenu.add_radiobutton(label="Entire Outline",variable=vd["radio-search-scope"],value="entire-outline",selectcolor=fg)
        rmenu.add_radiobutton(label="Suboutline Only",variable=vd["radio-search-scope"],value="suboutline-only",selectcolor=fg)
        rmenu.add_radiobutton(label="Node Only",variable=vd["radio-search-scope"],value="node-only",selectcolor=fg)
        rmenu.add_separator()
        rmenu.add_checkbutton(label="Mark Finds",variable=vd["mark_finds"],selectcolor=fg)
        rmenu.add_checkbutton(label="Mark Changes",variable=vd["mark_changes"],selectcolor=fg)
            
        rmenu.add_checkbutton(label="Ignore Case",columnbreak=1,variable=vd["ignore_case"],selectcolor=fg)
        rmenu.add_checkbutton(label="Whole Word", variable=vd["whole_word"],selectcolor=fg)
        rmenu.add_separator()
        rmenu.add_checkbutton(label="Wrap Around",variable=vd["wrap"],selectcolor=fg)
        rmenu.add_checkbutton(label="Reverse",variable=vd["reverse"],selectcolor=fg)
        rmenu.add_checkbutton(label="Contract Tree",variable=vd["collapse"],selectcolor=fg)
        rmenu.add_separator()
        rmenu.add_checkbutton(label="Regexp",variable=vd["pattern_match"],selectcolor=fg)
        rmenu.add_command(label="    ")
        #@-node:AGP.20231124085809.4:Options menu
        #@-others
        #@-node:AGP.20231124085809.3:create widgets
        #@-others
        
        
    #@nonl
    #@-node:AGP.20231124085809.1:__init__()
    #@+node:AGP.20231124085809.5:config()
    def config(self,dic):
        pass
    #@nonl
    #@-node:AGP.20231124085809.5:config()
    #@+node:AGP.20231124085809.6:setFocus()
    def SetFocus(self):
        self.searchbox.focus_set()
    #@nonl
    #@-node:AGP.20231124085809.6:setFocus()
    #@+node:AGP.20231124085809.7:onFocusIn()
    def onFocusIn(self,event):
        self.searchbox.select_range(0, Tk.END)
    #@-node:AGP.20231124085809.7:onFocusIn()
    #@+node:AGP.20231124085809.8:onFocusOut()
    def onFocusOut(self,event):
        if self.lmenu != None:
            self.lmenu.destroy()
            self.lmenu = None
    #@nonl
    #@-node:AGP.20231124085809.8:onFocusOut()
    #@+node:AGP.20231124085809.9:onkey
    def onKey (self,event=None): 
        """Called when the user presses a key in the text entry box"""
        
        
        if self.lmenu != None:
            self.lmenu.destroy()
            self.lmenu = None
            
        
        #print event.keysym
        
        if event.keysym == "Return":
            sv = self.searchvar.get()
            if sv != "" and not sv in self.history:
                self.history.insert(0,sv)
                #self.searchbox.after_idle(self.doSearch)
            
            # when using fintab
            #self.finder.find_ctrl.delete("1.0","end")
            #self.finder.find_ctrl.insert("1.0",sv)
            
            c = self.c
            
            #if c.frame.findPanel != self.finder:
            #c.frame.findPanel = self.finder
            c.searchCommands.findTabHandler = self.finder
            
            self.p = c.currentPosition() # Bug fix: 5/14/06
            
            #c.findNext()
            #c.searchCommands.findTabFindNext()
            self.findNextCommand(c)
            
            
                
    #@nonl
    #@-node:AGP.20231124085809.9:onkey
    #@+node:AGP.20231124085809.10:testcommand()
    def testcommand(self):
        print "testcommand",self
    #@-node:AGP.20231124085809.10:testcommand()
    #@+node:AGP.20231124085809.11:onRightClick()
    def onRightClick(self,event):    
        try:
            self.rmenu.tk_popup(event.x_root+1,event.y_root-10)
        finally:
            self.rmenu.grab_release()
    #@-node:AGP.20231124085809.11:onRightClick()
    #@+node:AGP.20231124085809.12:find_repack()
    def find_repack(self):
        
        self.changebox.pack_forget()
        self.tolabel.pack_forget()
        self.searchbox.pack_forget()
        self.action_button.pack_forget()
    
        #self.changebox.pack(side="right", padx=0, pady=0,fill="y", expand=0)
        #self.tolabel.pack(side="right", padx=2, pady=0,fill="y", expand=0)
        self.searchbox.pack(side="right", padx=2, pady=0,fill="y", expand=0)
        self.action_button.pack(side="right", padx=3, pady=0,fill="y", expand=0)
        
        self.action_button.config(text="Find")
        
        am = self.action_menu
        am.delete(0, am.index(Tk.END))
        
        am.add_command(label="Find Next",command=self.findNextCommand)
        am.add_command(label="Find Prev",command=self.findNextCommand)
        am.add_command(label="Find All",command=self.findAllCommand)
        am.add_command(label="Clone Find All",command=self.cloneFindAllCommand)
        am.add_separator()
        am.add_command(label="Change Mode",command=self.change_repack)
        
        
        
        self.searchbox.action = self.changebox.action = self.findNextCommand
    #@nonl
    #@-node:AGP.20231124085809.12:find_repack()
    #@+node:AGP.20231124085809.13:change_repack()
    def change_repack(self):
        self.changebox.pack_forget()
        self.tolabel.pack_forget()
        self.searchbox.pack_forget()
        self.action_button.pack_forget()
    
        self.changebox.pack(side="right", padx=0, pady=0,fill="y", expand=0)
        self.tolabel.pack(side="right", padx=2, pady=0,fill="y", expand=0)
        self.searchbox.pack(side="right", padx=0, pady=0,fill="y", expand=0)
        self.action_button.pack(side="right", padx=2, pady=0,fill="y", expand=0)
        
        self.action_button.config(text="Change")
        
        am = self.action_menu
        am.delete(0, am.index(Tk.END))
        
        am.add_command(label="Change Next",command=self.changeNextCommand)
        am.add_command(label="Change Prev",command=self.changePrevCommand)
        am.add_command(label="Change All",command=self.changeAllCommand)
        am.add_command(label="Change And Find",command=self.changeThenFindCommand)
        am.add_command(label="Change Selection",command=self.changeCommand)
        am.add_separator()
        am.add_command(label="Find Mode",command=self.find_repack)
        
        self.searchbox.action = self.changebox.action = self.changeNextCommand
    #@nonl
    #@-node:AGP.20231124085809.13:change_repack()
    #@+node:AGP.20231124085809.14: Top level
    #@+node:AGP.20231124085809.15:findAllCommand
    def findAllCommand (self,event=None):
        self.p = self.c.currentPosition()
        self.setup_command()
        self.findAll()
    #@-node:AGP.20231124085809.15:findAllCommand
    #@+node:AGP.20231124085809.16:findAgainCommand
    def findAgainCommand (self):
        self.findNextCommand()
        return True
    #@-node:AGP.20231124085809.16:findAgainCommand
    #@+node:AGP.20231124085809.17:cloneFindAllCommand
    def cloneFindAllCommand (self,event=None):
        self.p = self.c.currentPosition()
        self.setup_command()
        self.clone_find_all = True
        self.findAll()
        self.clone_find_all = False
    #@-node:AGP.20231124085809.17:cloneFindAllCommand
    #@+node:AGP.20231124085809.18:findNext/PrevCommand
    def findNextCommand (self,event=None):
        self.p = self.c.currentPosition()
        self.setup_command()
        return self.findNext()
        
    def findPrevCommand (self,event=None):
        self.p = self.c.currentPosition()
        self.setup_command()
        self.reverse = not self.reverse
        ret = self.findNext()
        self.reverse = not self.reverse
        return ret
    #@nonl
    #@-node:AGP.20231124085809.18:findNext/PrevCommand
    #@+node:AGP.20231124085809.19:change/ThenFindCommand
    def changeNextCommand (self,event=None):
        if self.findNextCommand():
            self.changeCommand()
            
    def changePrevCommand (self,event=None):
        if self.findPrevCommand():
            self.changeCommand()
    
    def changeCommand (self,event=None):
        self.p = self.c.currentPosition()
        self.setup_command()
        self.change()
        
    def changeAllCommand (self,event=None):
        self.p = self.c.currentPosition()
        self.setup_command()
        self.changeAll()
        
    def changeThenFindCommand(self,event=None):
        self.p = self.c.currentPosition()
        self.setup_command()
        self.changeThenFind()
    
    
    #@-node:AGP.20231124085809.19:change/ThenFindCommand
    #@-node:AGP.20231124085809.14: Top level
    #@+node:AGP.20231124085809.20:update_ivars
    def update_ivars (self):
        
        """Called just before doing a find to update ivars."""
    
        for key in self.intKeys:
            # g.trace('settattr',key,False)
            setattr(self, key,False)
    
        self.change_text = self.changebox.var.get()
        self.find_text = self.searchbox.var.get()
    
        # Set options
        
        vd = self.dict
        
        for k in self.dict.keys():
            setattr(self, k, vd[k].get())
    #@nonl
    #@-node:AGP.20231124085809.20:update_ivars
    #@+node:AGP.20231124085809.21:init_s_ctrl
    def init_s_ctrl (self,s):
        t = self.s_ctrl
        t.delete("1.0","end")
        t.insert("end",s)
        t.mark_set("insert",g.choose(self.reverse,"end","1.0"))
        return t
    #@-node:AGP.20231124085809.21:init_s_ctrl
    #@-others
#@-node:AGP.20231124085809:class SearchBox
#@+node:ekr.20031218072017.3940:class leoTkinterFrame
class leoTkinterFrame (leoFrame.leoFrame):
    
    """A class that represents a Leo window rendered in Tk/tkinter."""

    #@    @+others
    #@+node:ekr.20031218072017.1801:__init__ (tkFrame)
    def __init__(self,title,gui):
    
        # Init the base class.
        leoFrame.leoFrame.__init__(self,gui)
    
        self.title = title
    
        leoTkinterFrame.instances += 1
    
        self.c = None # Set in finishCreate.
        self.iconBar = None
        
        self.lastx = -1
    
        #self.trace_status_line = None # Set in finishCreate.
        #@    << set the leoTkinterFrame ivars >>
        #@+node:ekr.20031218072017.1802:<< set the leoTkinterFrame ivars >>
        # "Official ivars created in createLeoFrame and its allies.
        self.bar1 = None
        self.bar2 = None
        self.body = None
        self.bodyBar = None
        self.bodyCtrl = None
        self.bodyXBar = None
        self.f1 = self.f2 = None
        self.findPanel = None # Inited when first opened.
        self.iconBarComponentName = 'iconBar'
        self.iconFrame = None 
        self.log = None
        self.canvas = None
        self.outerFrame = None
        self.statusFrame = None
        self.statusLineComponentName = 'statusLine'
        self.statusText = None 
        self.statusLabel = None 
        self.top = None
        self.tree = None
        self.treeBar = None
        
        # Used by event handlers...
        self.controlKeyIsDown = False # For control-drags
        self.draggedItem = None
        self.isActive = True
        self.redrawCount = 0
        self.wantedWidget = None
        self.wantedCallbackScheduled = False
        self.scrollWay = None
        #@-node:ekr.20031218072017.1802:<< set the leoTkinterFrame ivars >>
        #@nl
        
        self.topgeometry = 800,600,30,30
    #@-node:ekr.20031218072017.1801:__init__ (tkFrame)
    #@+node:ekr.20031218072017.3942:__repr__ (tkFrame)
    def __repr__ (self):
    
        return "<leoTkinterFrame: %s>" % self.title
    #@-node:ekr.20031218072017.3942:__repr__ (tkFrame)
    #@+node:ekr.20031218072017.2176:finishCreate()
    def finishCreate (self,c):
        
        f = self ; f.c = c
        # g.trace('tkFrame')
        
        # This must be done after creating the commander.
        f.splitVerticalFlag,f.ratio,f.secondary_ratio = f.initialRatios()
        #f.splitVerticalFlag = True  # agp
        
        #@    @+others
        #@+node:AGP.20231115182509:Toplevel
        #f.createOuterFrames()
        f.top = top = Tk.Toplevel()
        g.app.gui.attachLeoIcon(top)
        top.title(f.title)
        top.minsize(30,10) # In grid units.
            
        if g.os_path_exists(g.app.user_xresources_path):
            f.top.option_readfile(g.app.user_xresources_path)
            
        top.protocol("WM_DELETE_WINDOW", f.OnCloseLeoEvent)
        top.bind("<Button-1>", f.OnActivateLeoEvent)
        
        self.MWTarget = None
        #top.bind_all("<MouseWheel>", f.TopMouseWheel)
        # Create the outer frame, the 'hull' component.
        
        
        outerFrame = f.outerFrame = Tk.Frame(top,bd=0,bg=g.theme['shade'](0.5))
        outerFrame.pack(expand=1,fill="both")
        #@nonl
        #@-node:AGP.20231115182509:Toplevel
        #@+node:AGP.20231115175745:Menu / iconBar / Status
        mf = self.menuFrame = Tk.Frame(outerFrame,bd=1,relief="flat",name="menuframe")
        mf.pack(side='top',fill="x")
        
        
        #f.createStatusLine()
        StatusFrame = self.StatusFrame = Tk.Frame(outerFrame,name="statusframe")#,bd=1,relief="flat",bg=g.theme['shade'](0.5))
        StatusFrame.pack(side='bottom',fill="x",ipadx=5)
        
        sl = self.StatusLabel = Tk.Label(StatusFrame,bd=1,relief="flat",text="no status",bg=g.theme['shade'](0.5))
        sl.pack(side='left',fill="x",padx=3)
        
        
        
        text = "line 0: col 0"
        width = len(text) + 4
            
        self.RowColWidget = Tk.Label(StatusFrame,text=text,width=width,anchor="e")
        self.RowColWidget.pack(side="right",padx=3)
        
                
        self.searchbox = SearchBox(c)
        
        self.iconFrame = Tk.Frame(outerFrame,name="iconframe")#,bd=5,relief="groove",bg=g.theme['shade'](0.5))
        self.iconFrame.pack(side='top',fill="x")
        
        self.iconBar = self.iconBarClass(c,self.iconFrame)
        #@-node:AGP.20231115175745:Menu / iconBar / Status
        #@+node:AGP.20231115182509.1:Splitters
        #f.createSplitterComponents()
        #f.createLeoSplitters(f.outerFrame)
        f1,bar1,split1Pane1,split1Pane2 = self.create_splitter( outerFrame, self.splitVerticalFlag,'splitter1')
        f2,bar2,split2Pane1,split2Pane2 = self.create_splitter( split1Pane1, not self.splitVerticalFlag,'splitter2',split1Pane1)
            
        split1Pane1.config(relief='flat',bd=0)
            
        self.f1,self.bar1 = f1,bar1
        self.split1Pane1,self.split1Pane2 = split1Pane1,split1Pane2
        self.f2,self.bar2 = f2,bar2
        self.split2Pane1,self.split2Pane2 = split2Pane1,split2Pane2
        
        
        
        editframe = split1Pane1
        logframe=   split2Pane2
        self.treeframe = treeframe=  split2Pane1
        bodyframe=  split1Pane2
        
        
        
        qlinkframe = Tk.Frame(treeframe,cursor='hand2',name="qlinkframe")
        qlinkframe.pack(anchor='n',side='top',fill='x',pady=1)
        
        self.subtreeframe = subtreeframe = Tk.Frame(treeframe)
        subtreeframe.pack(expand=1,fill='both',pady=1)
        
        
        # Create the canvas, tree, log and body.
        f.canvas = f.create_tree_canvas(subtreeframe)
        f.tree   = leoTkinterTree.leoTkinterTree(c,f,f.canvas)
        f.log    = leoTkinterLog(f,logframe)
        f.body   = leoTkinterBody(f,bodyframe)
        
        
        
        
            
        # Yes, this an "official" ivar: this is a kludge.
        f.bodyCtrl = f.body.bodyCtrl
        
        # Configure.
        f.setTabWidth(c.tab_width)
        f.tree.setColorFromConfig()
        f.reconfigurePanes()
        #f.body.setFontFromConfig()
        #f.body.setColorFromConfig()
        
        self.guiframes = outerFrame,editframe,bodyframe,treeframe,subtreeframe,logframe,qlinkframe,f.tree.font
        
        
        
        
            
        
            
        
        #@-node:AGP.20231115182509.1:Splitters
        #@+node:AGP.20231116090212:Create first tree node
        #f.createFirstTreeNode()
        t = leoNodes.tnode()
        v = leoNodes.vnode(t)
        p = leoNodes.position(v,[])
        v.initHeadString("NewHeadline")
        p.moveToRoot(oldRoot=None)
        c.setRootPosition(p) # New in 4.4.2.
        c.editPosition(p)
        #@nonl
        #@-node:AGP.20231116090212:Create first tree node
        #@-others
        
        
        
        f.menu = leoTkinterMenu.leoTkinterMenu(f)
            # c.finishCreate calls f.createMenuBar later.
        
        c.setLog()
        g.app.windowList.append(f)
        c.initVersion()
        c.signOnWithVersion()
        f.miniBufferWidget = f.createMiniBufferWidget()
        c.bodyWantsFocusNow()
        #self.trace_status_line = c.config.getBool('trace_status_line')
        # f.enableTclTraces()
        
        #self.iconbarfont = c.config.getFontFromParams(
        #    "icon_bar_font_family", "icon_bar_font_size",
        #    "icon_bar_font_slant",  "icon_bar_font_weight",7)
        
        self.reconfigure()
        # Redraw the window before writing into it.
        self.setTopGeometry(*self.topgeometry)
        self.deiconify()
        self.lift()
        self.update()
        
        
    #@-node:ekr.20031218072017.2176:finishCreate()
    #@+node:ekr.20041221071131.1:create_tree_canvas()
    def create_tree_canvas(self,parentFrame,pack=True):
        
        frame = self
        c = self.c
        
        scrolls = c.config.getBool('outline_pane_scrolls_horizontally')
        scrolls = g.choose(scrolls,1,0)
        
        canvas = Tk.Canvas(parentFrame,name="canvas", bd=0,relief="sunken",takefocus=0)
        
        
        
        trace = self.c.config.getBool('trace_chapters') and not g.app.unitTesting
        if trace: g.trace(canvas)
            
    
        frame.treeBar = treeBar = g.app.gui.SCROLLBAR(parentFrame,1)#Tk.Scrollbar(parentFrame,name="treeBar")
        
        # Bind mouse wheel event to canvas
        if sys.platform == "win32": # Works on 98, crashes on XP.
            canvas.bind("<MouseWheel>", frame.TopMouseWheel) #agp
            if 0: # New in 4.3.
                #@            << workaround for mouse-wheel problems >>
                #@+node:ekr.20050119210541:<< workaround for mouse-wheel problems >>
                # Handle mapping of mouse-wheel to buttons 4 and 5.
                
                def mapWheel(e):
                    print e.num
                    if e.num == 2:
                        print 'b2'
                        self.canvas.xview(Tk.SCROLL, 1, Tk.UNITS)   # agp
                    if e.num == 4: # Button 4
                        e.delta = 120
                        return frame.OnMouseWheel(e)
                    elif e.num == 5: # Button 5
                        e.delta = -120
                        return frame.OnMouseWheel(e)
                
                canvas.bind("<ButtonPress>",mapWheel,add=1)
                #@-node:ekr.20050119210541:<< workaround for mouse-wheel problems >>
                #@nl
        
        canvas['yscrollcommand'] = self.setCallback
        treeBar.command  = self.yviewCallback
        treeBar.pack(side="right", fill="y")
        if scrolls: 
            treeXBar = g.app.gui.SCROLLBAR(parentFrame,0)#Tk.Scrollbar( parentFrame,name='treeXBar', orient="horizontal") 
            canvas['xscrollcommand'] = treeXBar.set 
            treeXBar.command = canvas.xview 
            treeXBar.pack(side="bottom", fill="x")
        
        if pack:
            canvas.pack(side='top',expand=1,fill="both")
    
        canvas.bind("<Button-1>", frame.OnActivateTree)
        canvas.bind("<Button-2>", frame.OnCanvasB2)
        canvas.bind("<B2-Motion>", frame.OnCanvasMotion)
        canvas.configure(xscrollincrement=8)
        
        # Handle mouse wheel in the outline pane.
        if sys.platform == "linux2": # This crashes tcl83.dll
            canvas.bind("<MouseWheel>", frame.OnMouseWheel)
        if 0:
            #@        << do scrolling by hand in a separate thread >>
            #@+node:ekr.20040709081208:<< do scrolling by hand in a separate thread >>
            # New in 4.3: replaced global way with scrollWay ivar.
            ev = threading.Event()
            
            def run(self=self,canvas=canvas,ev=ev):
            
                while 1:
                    ev.wait()
                    if self.scrollWay =='Down': canvas.yview("scroll", 1,"units")
                    else:                       canvas.yview("scroll",-1,"units")
                    time.sleep(.1)
            
            t = threading.Thread(target = run)
            t.setDaemon(True)
            t.start()
            
            def scrollUp(event): scrollUpOrDown(event,'Down')
            def scrollDn(event): scrollUpOrDown(event,'Up')
                
            def scrollUpOrDown(event,theWay):
                if event.widget!=canvas: return
                if 0: # This seems to interfere with scrolling.
                    if canvas.find_overlapping(event.x,event.y,event.x,event.y): return
                ev.set()
                self.scrollWay = theWay
                    
            def off(event,ev=ev,canvas=canvas):
                if event.widget!=canvas: return
                ev.clear()
            
            if 1: # Use shift-click
                # Shift-button-1 scrolls up, Shift-button-2 scrolls down
                canvas.bind_all('<Shift Button-3>',scrollDn)
                canvas.bind_all('<Shift Button-1>',scrollUp)
                canvas.bind_all('<Shift ButtonRelease-1>',off)
                canvas.bind_all('<Shift ButtonRelease-3>',off)
            else: # Use plain click.
                canvas.bind_all( '<Button-3>',scrollDn)
                canvas.bind_all( '<Button-1>',scrollUp)
                canvas.bind_all( '<ButtonRelease-1>',off)
                canvas.bind_all( '<ButtonRelease-3>',off)
            #@-node:ekr.20040709081208:<< do scrolling by hand in a separate thread >>
            #@nl
        
        # g.print_bindings("canvas",canvas)
        return canvas
    #@-node:ekr.20041221071131.1:create_tree_canvas()
    #@+node:AGP.20231106084502:create_splitter()
    def create_splitter(self,parent,verticalFlag,componentName,pf=None):
        
        c = self.c
        
        bg = parent.cget('bg')
        
        # Create the frames.
        if pf:
            f=pf
        else:
            f = Tk.Frame(parent,bd=0,relief="flat",bg=bg)
            f.pack(expand=1,fill="both")
        
        
        #bg = g.colorf_toh(*g.colorf_mul(0.9,*g.colors_tof(*parent.winfo_rgb(bg))))
        bg = g.color_mul(0.7,bg)
        
        f1 = Tk.Frame(f,bg=bg)
        f2 = Tk.Frame(f,bg=bg)
       
        #bar = Tk.Frame(f,bd=0,relief="flat",bg=bg)
        
        if verticalFlag:
            bar = Tk.Frame(f,name="hsplitter",class_="Splitter")#,bd=0,relief="flat",bg=bg)
        else:
            bar = Tk.Frame(f,name="vsplitter",class_="Splitter")#bd=0,relief="flat",bg=bg)
        
        #self.bindBar(bar,verticalFlag)
        bar.bind("<B1-Motion>", self.SplitterOnMouseDrag)
        bar.bind("<Button-1>", self.SplitterOnMouseDown)
        bar.bind("<Button-3>", self.SplitterOnRightMouseDown)
        
        
        bar.fparent=f
        bar.f1 = f1
        bar.f2 = f2
        bar.vflag = verticalFlag
        bar.bar=None
        
        
        #self.configureBar(bar,verticalFlag)
    
        # Get configuration settings.
        w = c.config.getInt("split_bar_width")
        relief = c.config.get("split_bar_relief","relief")
        color = c.config.getColor("split_bar_color") or g.theme['bg']
        
        if not w or w < 1: w = 7
        if not relief: relief = "flat"
        if not color: color = "LightSteelBlue2"
        
        relief = "flat"
        w=g.theme['splitbar_width']
        #color = bar.cget('bg')#g.color_theme["bg"]
        if verticalFlag:
            bar.configure(relief=relief,bg=color,cursor="sb_v_double_arrow")
        else:
            bar.configure(relief=relief,bg=color,cursor="sb_h_double_arrow")
        
        
        #self.placeSplitter(bar,f1,f2,verticalFlag)
        self.splitter_relplace(bar,0.5)
        
        
        
        return f, bar, f1, f2
    #@nonl
    #@-node:AGP.20231106084502:create_splitter()
    #@+node:AGP.20231106120102:splitter_relplace()
    def splitter_relplace(self,bar,ratio):
        parent = bar.fparent
        f1 = bar.f1
        f2 = bar.f2
        #print parent,f1,f2
        pwidth = parent.winfo_width()
        pheight = parent.winfo_height()
        t=parent.winfo_toplevel()
        
        #print "splitter relplace()",bar.vflag,pwidth,pheight,bar.fparent,bar.winfo_height()
        
        if bar.vflag: #y
            bar_rw = bar.cget("height")/float(pheight)
            #print "vert",bar_rw,bar.cget("height"),float(pheight)
            bar.place(anchor='nw', relx=0.0, rely=ratio,relwidth=1.0)
            f1.place(anchor='nw', relx=0.0, rely=0.0, relwidth=1.0, relheight=ratio)
            
            f2.place(anchor='nw', relx=0.0, rely=ratio+bar_rw, relwidth=1.0, relheight=1.0-ratio-bar_rw)
            
        else: #x
            bar_rw = bar.cget("width")/float(pwidth)
            #print "hori",bar_rw,bar.cget("width"),float(pwidth)
            bar.place(anchor='nw', relx=ratio, rely=0.0,relheight=1.0)
            f1.place(anchor='nw', relx=0.0, rely=0.0, relwidth=ratio, relheight=1.0)
            
            f2.place(anchor='nw', relx=ratio+bar_rw, rely=0.0, relwidth=1.0-ratio-bar_rw, relheight=1.0)
        
    
                    
        
    #@nonl
    #@-node:AGP.20231106120102:splitter_relplace()
    #@+node:AGP.20240830080234:TopMouseWheel()
    def TopMouseWheel(self,event=None): #agp
        #work around the default tkinter mousewheel focus routing
        
        t = self.top
        w =  t.winfo_containing(*t.winfo_pointerxy())
        
        if w.master == self.canvas:
            w = self.canvas
        
        
        #print 'tmw',widget
        
        if w != None and hasattr(w,"yview"):
            if event.delta < 1:
                w.yview(Tk.SCROLL, 1, Tk.UNITS)
            else:
                w.yview(Tk.SCROLL, -1, Tk.UNITS)
        
        return "break"
    #@-node:AGP.20240830080234:TopMouseWheel()
    #@+node:AGP.20231111111117:SplitterOnMouseDown()
    def SplitterOnMouseDown(self,event):
        #print "mousedown",event.x_root,event.y_root
        self.start = event.x_root,event.y_root
        
        
    #@nonl
    #@-node:AGP.20231111111117:SplitterOnMouseDown()
    #@+node:AGP.20240829212026:SplitterOnRightMouseDown()
    def SplitterOnRightMouseDown(self,event):
        #print "mousedown",event.x_root,event.y_root
        self.toggleTkSplitDirection(True)
        
    #@nonl
    #@-node:AGP.20240829212026:SplitterOnRightMouseDown()
    #@+node:AGP.20231116094617:SplitterOnMouseDrag()
    def SplitterOnMouseDrag(self,event):
        # x and y are the coordinates of the cursor relative to the bar, not the main window.
        bar = event.widget
        #x = event.x
        #y = event.y
        top = bar.winfo_toplevel()
        
        sx,sy = self.start
        self.start = x,y = event.x_root,event.y_root
        
        if bar.vflag:
            wMax = bar.fparent.winfo_height()
            offset = bar.winfo_y()+y-sy
            
        else:
            wMax = bar.fparent.winfo_width()        
            offset = bar.winfo_x()+x-sx
    
        # Adjust the pixels, not the frac.
        if offset < 3:
            offset = 3
        
        if offset > wMax - 2:
            offset = wMax - 2
        
        self.splitter_relplace(bar, float(offset) / wMax )
        
    #@nonl
    #@-node:AGP.20231116094617:SplitterOnMouseDrag()
    #@+node:ekr.20060915124834:resizePanesToRatio
    def resizePanesToRatio(self,ratio,ratio2):
        
        # g.trace(ratio,ratio2,g.callers())
        
        bar = self.bar1
        self.splitter_relplace(bar,ratio)
        
        bar = self.bar2
        
        self.splitter_relplace(bar,ratio2)
        
        #self.divideLeoSplitter(self.splitVerticalFlag,9.0/10)#,ratio)    #agp
        #self.divideLeoSplitter(not self.splitVerticalFlag,1.0/3)#,ratio2)
    #@nonl
    #@-node:ekr.20060915124834:resizePanesToRatio
    #@+node:ekr.20031218072017.998:Scrolling callbacks (frame)
    def setCallback (self,*args,**keys):
        
        """Callback to adjust the scrollbar.
        
        Args is a tuple of two floats describing the fraction of the visible area."""
    
        # g.trace(self.tree.redrawCount,args)
    
        apply(self.treeBar.set,args,keys)
    
        if self.tree and self.tree.allocateOnlyVisibleNodes:
            self.tree.setVisibleArea(args)
            
    def yviewCallback (self,*args,**keys):
        
        """Tell the canvas to scroll"""
        
        # g.trace(vyiewCallback",args,keys)
    
        if self.tree and self.tree.allocateOnlyVisibleNodes:
            self.tree.allocateNodesBeforeScrolling(args)
    
        apply(self.canvas.yview,args,keys)
    #@-node:ekr.20031218072017.998:Scrolling callbacks (frame)
    #@+node:ekr.20031218072017.3941: Birth & Death (tkFrame)
    #@+node:ekr.20051009044751:XcreateOuterFrames()
    def createOuterFrames (self):
    
        f = self ; c = f.c
        f.top = top = Tk.Toplevel()
        g.app.gui.attachLeoIcon(top)
        top.title(f.title)
        top.minsize(30,10) # In grid units.
        
        if g.os_path_exists(g.app.user_xresources_path):
            f.top.option_readfile(g.app.user_xresources_path)
        
        f.top.protocol("WM_DELETE_WINDOW", f.OnCloseLeoEvent)
        f.top.bind("<Button-1>", f.OnActivateLeoEvent)
        
        # These don't work on Windows. Because of bugs in window managers,
        # there is NO WAY to know which window is on top!
        if 0:
            f.top.bind("<Activate>",f.OnActivateLeoEvent)
            f.top.bind("<Deactivate>",f.OnDeactivateLeoEvent)
            f.top.bind("<Control-KeyPress>",f.OnControlKeyDown)
            f.top.bind("<Control-KeyRelease>",f.OnControlKeyUp)
        
        # Create the outer frame, the 'hull' component.
        f.outerFrame = Tk.Frame(top,bd=0,bg=g.theme['mid'])
        f.outerFrame.pack(expand=1,fill="both")
    #@nonl
    #@-node:ekr.20051009044751:XcreateOuterFrames()
    #@+node:AGP.20231112155626:XcreateSplitterComponents
    def xcreateSplitterComponents (self):
    
        f = self ; c = f.c
    
        f.createLeoSplitters(f.outerFrame)
        
        # Create the canvas, tree, log and body.
        
        
        
        f.canvas = f.createCanvas(f.split2Pane1)
        
        f.tree   = leoTkinterTree.leoTkinterTree(c,f,f.canvas)
        f.log    = leoTkinterLog(f,f.split2Pane2)
        f.body   = leoTkinterBody(f,f.split1Pane2)
        
        # Yes, this an "official" ivar: this is a kludge.
        f.bodyCtrl = f.body.bodyCtrl
        
        # Configure.
        f.setTabWidth(c.tab_width)
        f.tree.setColorFromConfig()
        f.reconfigurePanes()
        f.body.setFontFromConfig()
        f.body.setColorFromConfig()
        
        
        
        
    #@-node:AGP.20231112155626:XcreateSplitterComponents
    #@+node:ekr.20051009045208:XcreateSplitterComponents()
    def createSplitterComponents (self):
    
        f = self ; c = f.c
    
        f.createLeoSplitters(f.outerFrame)
        print g.theme['mid']
        f.outerFrame.config(bg=g.theme['mid'])
        
        editframe,logframe,treeframe,bodyframe,qlinkframe = self.guiframes
        
        
        
        subtreeframe = Tk.Frame(treeframe)
        
        
        bg = treeframe.cget('bg')
        bg = g.color_mul(0.5,bg)
        
        
        qlinkframe = Tk.Frame(treeframe,relief='groove',bd=0,
                                cursor='hand2',
                                bg = bg
                            )
        
        qlinkframe.pack(anchor='n',side='top',fill='x',pady=1)
        subtreeframe.pack(expand=1,fill='both',pady=1)
        
        
        
        # Create the canvas, tree, log and body.
        f.canvas = f.createCanvas(subtreeframe)
        f.tree   = leoTkinterTree.leoTkinterTree(c,f,f.canvas)
        f.log    = leoTkinterLog(f,logframe)
        f.body   = leoTkinterBody(f,bodyframe)
        
        self.guiframes = editframe,logframe,subtreeframe,bodyframe,qlinkframe,f.tree.font
        
        # Yes, this an "official" ivar: this is a kludge.
        f.bodyCtrl = f.body.bodyCtrl
        
        # Configure.
        f.setTabWidth(c.tab_width)
        f.tree.setColorFromConfig()
        f.reconfigurePanes()
        f.body.setFontFromConfig()
        f.body.setColorFromConfig()
    #@nonl
    #@-node:ekr.20051009045208:XcreateSplitterComponents()
    #@+node:ekr.20051009045404:XcreateFirstTreeNode()
    def createFirstTreeNode (self):
        
        f = self ; c = f.c
    
        t = leoNodes.tnode()
        v = leoNodes.vnode(t)
        p = leoNodes.position(v,[])
        v.initHeadString("NewHeadline")
        p.moveToRoot(oldRoot=None)
        c.setRootPosition(p) # New in 4.4.2.
        c.editPosition(p)
    #@-node:ekr.20051009045404:XcreateFirstTreeNode()
    #@+node:ekr.20051121092320:enableTclTraces()
    def enableTclTraces (self):
        
        c = self.c
    
        def tracewidget(event):
            g.trace('enabling widget trace')
            #Pmw.tracetk(event.widget, 1)
        
        def untracewidget(event):
            g.trace('disabling widget trace')
            #Pmw.tracetk(event.widget,0)
            
        def focusIn (event):
            print("Focus in  %s (%s)" % (
                event.widget,event.widget.winfo_class()))
            
        def focusOut (event):
            print("Focus out %s (%s)" % (
                event.widget,event.widget.winfo_class()))
    
        # Put this in unit tests before the assert:
        # c.frame.bar1.unbind_all("<FocusIn>")
        # c.frame.bar1.unbind_all("<FocusOut>")
    
        # Any widget would do:
        w = c.frame.bar1
        if 1:
            w.bind_all("<FocusIn>", focusIn)
            w.bind_all("<FocusOut>", focusOut)
        else:
            w.bind_all("<Control-1>", tracewidget)
            w.bind_all("<Control-Shift-1>", untracewidget)
    #@-node:ekr.20051121092320:enableTclTraces()
    #@+node:ekr.20031218072017.3944:Xf.createCanvas()
    def createCanvas (self,parentFrame,pack=True):
    
        # pageName is not used here: it is used for compatibility with the Chapters plugin.
    
        c = self.c
    
        scrolls = c.config.getBool('outline_pane_scrolls_horizontally')
        scrolls = g.choose(scrolls,1,0)
        canvas = self.createTkTreeCanvas(parentFrame,scrolls,pack)
    
        return canvas
    #@nonl
    #@-node:ekr.20031218072017.3944:Xf.createCanvas()
    #@+node:AGP.20231112155626.1:XcreateLeoSplitters
    #@+at 
    #@nonl
    # The key invariants used throughout this code:
    # 
    # 1. self.splitVerticalFlag tells the alignment of the main splitter and
    # 2. not self.splitVerticalFlag tells the alignment of the secondary 
    # splitter.
    # 
    # Only the general-purpose divideAnySplitter routine doesn't know about 
    # these
    # invariants. So most of this code is specialized for Leo's window. OTOH, 
    # creating
    # a single splitter window would be much easier than this code.
    #@-at
    #@@c
    
    def xcreateLeoSplitters (self,parentFrame):
        
        # Splitter 1 is the main splitter containing splitter2 and the body pane.
        f1,bar1,split1Pane1,split1Pane2 = self.createLeoTkSplitter( parentFrame, self.splitVerticalFlag,'splitter1')
        
        f1.config(bd=2,relief='sunken')
    
        self.f1,self.bar1 = f1,bar1
        self.split1Pane1,self.split1Pane2 = split1Pane1,split1Pane2
    
        # Splitter 2 is the secondary splitter containing the tree and log panes.
        f2,bar2,split2Pane1,split2Pane2 = self.createLeoTkSplitter( split1Pane1, not self.splitVerticalFlag,'splitter2')
    
        self.f2,self.bar2 = f2,bar2
        self.split2Pane1,self.split2Pane2 = split2Pane1,split2Pane2
        
    #@-node:AGP.20231112155626.1:XcreateLeoSplitters
    #@+node:ekr.20041221123325:createLeoSplitters & helpers
    def createLeoSplitters (self,parentFrame):
        #SparentFrame.update_idletasks()
        
        #print "create splitter",parentFrame.winfo_width(),parentFrame.winfo_height()
        
        # Splitter 1 is the main splitter containing splitter2 and the body pane.
        f1,bar1,split1Pane1,split1Pane2 = self.createLeoTkSplitter( parentFrame, False,'splitter1')
        #f1.config(bd=2,relief='sunken')
    
        self.f1,self.bar1 = f1,bar1
        self.split1Pane1,self.split1Pane2 = split1Pane1,split1Pane2
    
        # Splitter 2 is the secondary splitter containing the tree and log panes.
        f2,bar2,split2Pane1,split2Pane2 = self.createLeoTkSplitter( split1Pane1, True,'splitter2',split1Pane1)
        
        
        
        self.guiframes = editframe,logframe,treeframe,bodyframe,qlinkframe = (split1Pane1,split2Pane2,split2Pane1,split1Pane2,None)
        
        split1Pane1.config(relief='flat',bd=0)
        
        logframe.config(relief='groove',bd=0,highlightthickness=1)
        treeframe.config(relief='groove',bd=0,highlightthickness=1)
        bodyframe.config(relief='groove',bd=0,highlightthickness=1)#,padx=3,pady=3)
        
        
    
        self.f2,self.bar2 = f2,bar2
        self.split2Pane1,self.split2Pane2 = split2Pane1,split2Pane2
    #@nonl
    #@+node:AGP.20231104061353:Xsplitter_place()
    def Xsplitter_place(self,bar,delta):#AGP
        parent = bar.fparent
        f1 = bar.f1
        f2 = bar.f2
        #print parent,f1,f2
        pwidth = parent.winfo_width()
        pheight = parent.winfo_height()
        print pheight,
        
        if bar.vflag: #y
            print "splitter_place y",parent
            
            f1.place(
                    x=0,y=0,anchor='nw',
                    rely=0,relx=0,relwidth=0,relheight=0,
                    width=pwidth-6,
                    height=delta-6
                    )
            
            print "f1",delta,f1.winfo_height(),parent.winfo_height(),f1
            
            bar.place(x=0,y=delta,rely=0.0)
            delta += bar.winfo_height()
            f2.place(
                    x=0,y=delta-1,anchor='nw',
                    rely=0,relx=0,relwidth=0,relheight=0,
                    width=pwidth,
                    height=pheight-delta-6
                    )
            print "f2","height",pheight-delta-6,parent.winfo_height(),f2
        else: #x
            print "splitter_place x",parent
            bar.place(x=delta,y=0,relx=0.0)
            f1.place(
                    x=0,y=0,anchor='nw',
                    relx=0.0,rely=0,relwidth=0,relheight=0,
                    width=delta-3,
                    height=pheight
                    )
            print delta,parent.winfo_width(),pheight,f1
            
            
            delta += bar.winfo_width() 
            f2.place(
                    x=delta-2,y=0, anchor='nw',
                    relx=0,rely=0,relwidth=0,relheight=0,
                    width=pwidth-delta,
                    height=pheight
                    )
            print "f2","height",pheight,parent.winfo_height(),f2
    
            
            
                    
        
    #@nonl
    #@-node:AGP.20231104061353:Xsplitter_place()
    #@+node:ekr.20031218072017.3947:XbindBar
    def bindBar (self, bar, verticalFlag):
    
        if verticalFlag == self.splitVerticalFlag:
            bar.bind("<B1-Motion>", self.onDragMainSplitBar)
    
        else:
            bar.bind("<B1-Motion>", self.onDragSecondarySplitBar)
            
        bar.bind("<Button-1>", self.on_mouse_down)
    #@-node:ekr.20031218072017.3947:XbindBar
    #@+node:ekr.20031218072017.3949:divideAnySplitter
    # This is the general-purpose placer for splitters.
    # It is the only general-purpose splitter code in Leo.
    
    def divideAnySplitter (self, frac, verticalFlag, bar, pane1, pane2):
        print "divide any"
        if verticalFlag:
            # Panes arranged vertically; horizontal splitter bar
            bar.place(rely=frac)
            pane1.place(relheight=frac)
            pane2.place(relheight=1-frac)
        else:
            # Panes arranged horizontally; vertical splitter bar
            bar.place(relx=frac)
            pane1.place(relwidth=frac)
            pane2.place(relwidth=1-frac)
    #@-node:ekr.20031218072017.3949:divideAnySplitter
    #@+node:ekr.20031218072017.3950:divideLeoSplitter
    # Divides the main or secondary splitter, using the key invariant.
    def divideLeoSplitter (self, verticalFlag, frac):
    
        if self.splitVerticalFlag == verticalFlag:
            self.divideLeoSplitter1(frac,verticalFlag)
            self.ratio = frac # Ratio of body pane to tree pane.
        else:
            self.divideLeoSplitter2(frac,verticalFlag)
            self.secondary_ratio = frac # Ratio of tree pane to log pane.
    
    # Divides the main splitter.
    def divideLeoSplitter1 (self, frac, verticalFlag): 
        self.divideAnySplitter(frac, verticalFlag,self.bar1, self.split1Pane1, self.split1Pane2)
    
    # Divides the secondary splitter.
    def divideLeoSplitter2 (self, frac, verticalFlag): 
        self.divideAnySplitter (frac, verticalFlag,self.bar2, self.split2Pane1, self.split2Pane2)
    #@-node:ekr.20031218072017.3950:divideLeoSplitter
    #@+node:ekr.20031218072017.3951:onDrag...
    def onDragMainSplitBar (self, event):
        self.onDragSplitterBar(event,self.splitVerticalFlag)
    
    def onDragSecondarySplitBar (self, event):
        self.onDragSplitterBar(event,not self.splitVerticalFlag)
    
    def onDragSplitterBar (self, event, verticalFlag):
        
        # x and y are the coordinates of the cursor relative to the bar, not the main window.
        bar = event.widget
        x = event.x
        y = event.y
        top = bar.winfo_toplevel()
        
        sx,sy = self.start
        
        if bar.vflag:
            wMax = bar.fparent.winfo_height()
            offset = bar.winfo_y()+event.y_root-sy
            
        else:
            wMax = bar.fparent.winfo_width()        
            offset = bar.winfo_x()+event.x_root-sx
        
        self.start = event.x_root,event.y_root
    
        # Adjust the pixels, not the frac.
        if offset < 3: offset = 3
        if offset > wMax - 2: offset = wMax - 2
        
        # Redraw the splitter as the drag is occuring.
        frac = float(offset) / wMax
        self.splitter_relplace(bar,frac)
        
        
    #@nonl
    #@-node:ekr.20031218072017.3951:onDrag...
    #@+node:ekr.20031218072017.3952:placeSplitter
    def placeSplitter (self,bar,pane1,pane2,verticalFlag):
        print "place splitter"
        if verticalFlag:
            # Panes arranged vertically; horizontal splitter bar
            pane1.place(relx=0.5, rely =   0, anchor="n", relwidth=1.0, relheight=0.5)
            pane2.place(relx=0.5, rely = 1.0, anchor="s", relwidth=1.0, relheight=0.5)
            bar.place  (relx=0.5, rely = 0.5, anchor="c", relwidth=1.0)
        else:
            # Panes arranged horizontally; vertical splitter bar
            # adj gives tree pane more room when tiling vertically.
            adj = g.choose(verticalFlag != self.splitVerticalFlag,0.65,0.5)
            pane1.place(rely=0.5, relx =   0, anchor="w", relheight=1.0, relwidth=adj)
            pane2.place(rely=0.5, relx = 1.0, anchor="e", relheight=1.0, relwidth=1.0-adj)
            bar.place  (rely=0.5, relx = adj, anchor="c", relheight=1.0)
    #@-node:ekr.20031218072017.3952:placeSplitter
    #@-node:ekr.20041221123325:createLeoSplitters & helpers
    #@+node:ekr.20031218072017.3964:Destroying the frame
    #@+node:ekr.20031218072017.1975:destroyAllObjects
    def destroyAllObjects (self):
    
        """Clear all links to objects in a Leo window."""
    
        frame = self ; c = self.c ; tree = frame.tree ; body = self.body
    
        # Do this first.
        #@    << clear all vnodes and tnodes in the tree >>
        #@+node:ekr.20031218072017.1976:<< clear all vnodes and tnodes in the tree>>
        # Using a dict here is essential for adequate speed.
        vList = [] ; tDict = {}
        
        for p in c.allNodes_iter():
            vList.append(p.v)
            if p.v.t:
                key = id(p.v.t)
                if not tDict.has_key(key):
                    tDict[key] = p.v.t
        
        for key in tDict.keys():
            g.clearAllIvars(tDict[key])
        
        for v in vList:
            g.clearAllIvars(v)
        
        vList = [] ; tDict = {} # Remove these references immediately.
        #@-node:ekr.20031218072017.1976:<< clear all vnodes and tnodes in the tree>>
        #@nl
    
        # Destroy all ivars in subcommanders.
        g.clearAllIvars(c.atFileCommands)
        g.clearAllIvars(c.fileCommands)
        g.clearAllIvars(c.importCommands)
        g.clearAllIvars(c.tangleCommands)
        g.clearAllIvars(c.undoer)
        g.clearAllIvars(c)
        g.clearAllIvars(body.colorizer)
        g.clearAllIvars(body)
        g.clearAllIvars(tree)
    
        # This must be done last.
        frame.destroyAllPanels()
        g.clearAllIvars(frame)
    #@-node:ekr.20031218072017.1975:destroyAllObjects
    #@+node:ekr.20031218072017.3965:destroyAllPanels
    def destroyAllPanels (self):
    
        """Destroy all panels attached to this frame."""
        
        panels = (self.comparePanel, self.colorPanel, self.findPanel, self.fontPanel, self.prefsPanel)
    
        for panel in panels:
            if panel:
                panel.top.destroy()
    #@-node:ekr.20031218072017.3965:destroyAllPanels
    #@+node:ekr.20031218072017.1974:destroySelf (tkFrame)
    def destroySelf (self):
        
        # Remember these: we are about to destroy all of our ivars!
        top = self.top 
        c = self.c
        
        # Indicate that the commander is no longer valid.
        c.exists = False 
        
        # g.trace(self)
    
        # Important: this destroys all the object of the commander too.
        self.destroyAllObjects()
        
        c.exists = False # Make sure this one ivar has not been destroyed.
    
        top.destroy()
    #@-node:ekr.20031218072017.1974:destroySelf (tkFrame)
    #@-node:ekr.20031218072017.3964:Destroying the frame
    #@-node:ekr.20031218072017.3941: Birth & Death (tkFrame)
    #@+node:ekr.20041223104933:class statusLineClass
    class statusLineClass:
        
        '''A class representing the status line.'''
        
        #@    @+others
        #@+node:ekr.20031218072017.3961:Xctor
        def X__init__ (self,c,parentFrame):
            
            self.c = c
            self.colorTags = [] # list of color names used as tags.
            self.enabled = False
            self.isVisible = False
            self.lastRow = self.lastCol = 0
            self.log = c.frame.log
            #if 'black' not in self.log.colorTags:
            #    self.log.colorTags.append("black")
            
            self.parentFrame = parentFrame
            
            self.statusFrame = Tk.Frame(parentFrame,bd=2)
            
            text = "line 0, col 0"
            width = len(text) + 4
            
            self.labelWidget = Tk.Label(self.statusFrame,text=text,width=width,anchor="w")
            self.labelWidget.pack(side="left",padx=1)
            
            bg = self.statusFrame.cget("background")
            
            self.textWidget = Tk.Text(self.statusFrame,
                height=1,state="disabled",bg=bg,relief="groove",name='status-line')
            
            self.textWidget.pack(side="left",expand=1,fill="x")
            self.textWidget.bind("<Button-1>", self.onActivate)
        #@-node:ekr.20031218072017.3961:Xctor
        #@+node:AGP.20231106132502:__init__ ()
        def __init__ (self,c,parentFrame):
            
            self.c = c
            self.colorTags = [] # list of color names used as tags.
            self.enabled = False
            self.isVisible = False
            self.lastRow = self.lastCol = 0
            self.log = c.frame.log
            #if 'black' not in self.log.colorTags:
            #    self.log.colorTags.append("black")
            
            self.parentFrame = parentFrame
            
            
            text = "line 0, col 0"
            width = len(text) + 4
            
            self.labelWidget = Tk.Label(self.parentFrame,text=text,width=width,anchor="w")
            self.labelWidget.pack(side="left",padx=1)
            
            
        #@-node:AGP.20231106132502:__init__ ()
        #@+node:ekr.20031218072017.3962:clear
        def clear (self):
            pass
            t = self.textWidget
            if not t: return
            
            #trace = self.c.frame.trace_status_line and not g.app.unitTesting
            #if trace: g.trace(g.callers())
            
            t.configure(state="normal")
            t.delete("1.0","end")
            t.configure(state="disabled")
        #@-node:ekr.20031218072017.3962:clear
        #@+node:EKR.20040424153344:enable, disable & isEnabled
        def disable (self,background=None):
            pass
            c = self.c ; t = self.textWidget
            if t:
                if not background:
                    background = self.statusFrame.cget("background")
                t.configure(state="disabled",background=background)
            self.enabled = False
            c.bodyWantsFocus()
            
        def enable (self,background="white"):
            pass
            # g.trace()
            c = self.c ; t = self.textWidget
            if t:
                t.configure(state="normal",background=background)
                c.widgetWantsFocus(t)
            self.enabled = True
                
        def isEnabled(self):
            return self.enabled
        #@nonl
        #@-node:EKR.20040424153344:enable, disable & isEnabled
        #@+node:ekr.20041026132435:get
        def get (self):
            pass
            t = self.textWidget
            if t:
                return t.get("1.0","end")
            else:
                return ""
        #@-node:ekr.20041026132435:get
        #@+node:ekr.20041223114744:getFrame
        def getFrame (self):
            pass
            return self.statusFrame
        #@-node:ekr.20041223114744:getFrame
        #@+node:ekr.20050120093555:onActivate
        def onActivate (self,event=None):
            pass
            # Don't change background as the result of simple mouse clicks.
            background = self.statusFrame.cget("background")
            self.enable(background=background)
        #@-node:ekr.20050120093555:onActivate
        #@+node:ekr.20041223111916:pack & show
        def pack (self):
            pass
            if not self.isVisible:
                self.isVisible = True
                self.statusFrame.pack(fill="x",pady=1)
                
        show = pack
        #@-node:ekr.20041223111916:pack & show
        #@+node:ekr.20031218072017.3963:put (leoTkinterFrame:statusLineClass)
        def put(self,s,color=None):
            pass
            t = self.textWidget
            if not t: return
            
            #trace = self.c.frame.trace_status_line and not g.app.unitTesting
            #if trace: g.trace(s,g.callers())
            
            t.configure(state="normal")
                
            if color and color not in self.colorTags:
                self.colorTags.append(color)
                t.tag_config(color,foreground=color)
        
            if color:
                t.insert("end",s)
                t.tag_add(color,"end-%dc" % (len(s)+1),"end-1c")
                t.tag_config("black",foreground="black")
                t.tag_add("black","end")
            else:
                t.insert("end",s)
            
            t.configure(state="disabled")
        #@-node:ekr.20031218072017.3963:put (leoTkinterFrame:statusLineClass)
        #@+node:ekr.20041223111916.1:unpack & hide
        def unpack (self):
            pass
            if self.isVisible:
                self.isVisible = False
                self.statusFrame.pack_forget()
        
        hide = unpack
        #@-node:ekr.20041223111916.1:unpack & hide
        #@+node:ekr.20031218072017.1733:update (statusLine)
        def update (self):
            pass
            c = self.c ; w = c.frame.bodyCtrl ; lab = self.labelWidget
        
            if g.app.killed or not self.isVisible:
                return
        
            index = w.index("insert")
            row,col = g.app.gui.getindex(w,index)
            
            #print index,row,col
        
            if col > 0:
                s = w.get("%d.0" % (row),index)
                s = g.toUnicode(s,g.app.tkEncoding)
                col = g.computeWidth (s,c.tab_width)
            
            s = "line %d, col %d " % (row,col)
            # Important: this does not change the focus because labels never get focus.
            lab.configure(text=s)
            self.lastRow = row
            self.lastCol = col
        #@-node:ekr.20031218072017.1733:update (statusLine)
        #@-others
    #@-node:ekr.20041223104933:class statusLineClass
    #@+node:ekr.20041223102225:class iconBarClass
    class iconBarClass:
        
        '''A class representing the singleton Icon bar'''
        
        #@    @+others
        #@+node:ekr.20041223102225.1:__init__()
        def __init__ (self,c,parentFrame):
            
            self.c = c
            
            
            bg = parentFrame.cget('bg')
            bg = g.color_mul(0.7,bg)
            
            self.buttons = {} # Keys
            #self.menuFrame = Tk.Frame(parentFrame,bd=1,relief="flat",bg=bg) # ,background='blue')
            self.iconFrame = parentFrame#Tk.Frame(parentFrame,bd=1,relief="flat") # ,background='blue')
            self.parentFrame = parentFrame
            self.visible = False
        #@nonl
        #@-node:ekr.20041223102225.1:__init__()
        #@+node:ekr.20031218072017.3958:add
        def add(self,*args,**keys):
            
            """Add a button containing text or a picture to the icon bar.
            
            Pictures take precedence over text"""
            
            f = self.iconFrame
            text = keys.get('text')
            imagefile = keys.get('imagefile')
            image = keys.get('image')
            command = keys.get('command')
            bg = keys.get('bg')
        
            if not imagefile and not image and not text: return
        
            # First define n.
            try:
                g.app.iconWidgetCount += 1
                n = g.app.iconWidgetCount
            except:
                n = g.app.iconWidgetCount = 1
        
            if not command:
                def command():
                    print "command for widget %s" % (n)
        
            if imagefile or image:
                #@        << create a picture >>
                #@+node:ekr.20031218072017.3959:<< create a picture >>
                try:
                    if imagefile:
                        # Create the image.  Throws an exception if file not found
                        imagefile = g.os_path_join(g.app.loadDir,imagefile)
                        imagefile = g.os_path_normpath(imagefile)
                        image = Tk.PhotoImage(master=g.app.root,file=imagefile)
                        
                        # Must keep a reference to the image!
                        try:
                            refs = g.app.iconImageRefs
                        except:
                            refs = g.app.iconImageRefs = []
                    
                        refs.append((imagefile,image),)
                    
                    if not bg:
                        bg = f.cget("bg")
                
                    b = Tk.Button(f,image=image,relief="flat",bd=0,command=command,bg=bg)
                    b.pack(side="left",fill="y")
                    return b
                    
                except:
                    g.es_exception()
                    return None
                #@-node:ekr.20031218072017.3959:<< create a picture >>
                #@nl
            elif text:
                b = Tk.Button(f,text=text,command=command,bg=f['bg'])
                if sys.platform != 'darwin':
                    width = max(6,len(text))
                    b.configure(width=width)
                b.pack(side="left")#, fill="y")
                return b
                
            return None
        #@-node:ekr.20031218072017.3958:add
        #@+node:ekr.20031218072017.3956:clear
        def clear(self):
            
            """Destroy all the widgets in the icon bar"""
            
            f = self.iconFrame
            
            for slave in f.pack_slaves():
                slave.destroy()
            self.visible = False
        
            f.configure(height="30") # The default height.
            g.app.iconWidgetCount = 0
            g.app.iconImageRefs = []
        #@-node:ekr.20031218072017.3956:clear
        #@+node:ekr.20041223114821:getFrame
        def getFrame (self):
        
            return self.iconFrame
        #@-node:ekr.20041223114821:getFrame
        #@+node:ekr.20041223102225.2:pack (show)
        def pack (self):
            
            """Show the icon bar by repacking it"""
            
            if not self.visible:
                self.visible = True
                #self.menuFrame.pack(side='top',fill="x")
                self.iconFrame.pack(side='top',fill="x")
                
        show = pack
        #@-node:ekr.20041223102225.2:pack (show)
        #@+node:ekr.20031218072017.3955:unpack (hide)
        def unpack (self):
            
            """Hide the icon bar by unpacking it.
            
            A later call to show will repack it in a new location."""
            
            if self.visible:
                self.visible = False
                self.iconFrame.pack_forget()
                #self.menuFrame.pack_forget()
                
        hide = unpack
        #@-node:ekr.20031218072017.3955:unpack (hide)
        #@-others
    #@-node:ekr.20041223102225:class iconBarClass
    #@+node:ekr.20051014154752:Minibuffer methods
    #@+node:ekr.20060203115311:showMinibuffer
    def showMinibuffer (self):
        
        '''Make the minibuffer visible.'''
        
        frame = self
        
        if not frame.minibufferVisible:
            frame.minibufferFrame.pack(side='bottom',fill='x')
            frame.minibufferVisible = True
    #@-node:ekr.20060203115311:showMinibuffer
    #@+node:ekr.20060203115311.1:hideMinibuffer
    def hideMinibuffer (self):
        
        '''Hide the minibuffer.'''
        
        frame = self
        if frame.minibufferVisible:
            frame.minibufferFrame.pack_forget()
            frame.minibufferVisible = False
    #@-node:ekr.20060203115311.1:hideMinibuffer
    #@+node:ekr.20050920094212:f.createMiniBufferWidget
    def createMiniBufferWidget (self):
        
        '''Create the minbuffer below the status line.'''
        
        frame = self ; c = frame.c
    
        frame.minibufferFrame = f = Tk.Frame(frame.outerFrame,relief='flat',borderwidth=0)
        if c.showMinibuffer:
            f.pack(side='bottom',fill='x')
    
        lab = Tk.Label(f,text='mini-buffer',justify='left',anchor='nw',foreground='blue')
        lab.pack(side='left')
        
        if c.useTextMinibuffer:
            label = Tk.Text(f,height=1,relief='groove',background='lightgrey',name='minibuffer')
            label.pack(side='left',fill='x',expand=1,padx=2,pady=1)
        else:
            label = Tk.Label(f,relief='groove',justify='left',anchor='w',name='minibuffer')
            label.pack(side='left',fill='both',expand=1,padx=2,pady=1)
        
        frame.minibufferVisible = c.showMinibuffer
    
        return label
    #@-node:ekr.20050920094212:f.createMiniBufferWidget
    #@+node:ekr.20060203114017:f.setMinibufferBindings
    def setMinibufferBindings (self):
        
        '''Create bindings for the minibuffer..'''
        
        f = self ; c = f.c ; k = c.k ; t = f.miniBufferWidget
        
        if not c.useTextMinibuffer: return
        
        for kind,callback in (
            ('<Key>',           k.masterKeyHandler),
            ('<Button-1>',      k.masterClickHandler),
            ('<Button-3>',      k.masterClick3Handler),
            ('<Double-1>',      k.masterDoubleClickHandler),
            ('<Double-3>',      k.masterDoubleClick3Handler),
        ):
            t.bind(kind,callback)
    
        if 0:
            if sys.platform.startswith('win'):
                # Support Linux middle-button paste easter egg.
                t.bind("<Button-2>",frame.OnPaste)
    #@-node:ekr.20060203114017:f.setMinibufferBindings
    #@-node:ekr.20051014154752:Minibuffer methods
    #@+node:ekr.20031218072017.3953:Icon area methods (compatibility)
    def addIconButton (self,*args,**keys):
        return self.iconBar and self.iconBar.add(*args,**keys)
    
    def clearIconBar (self):
        if self.iconBar: self.iconBar.clear()
    
    def createIconBar (self):
        f = self ; c = f.c
        if not f.iconBar:
            f.iconBar = f.iconBarClass(c,f.outerFrame)
            f.iconFrame = f.iconBar.iconFrame
            f.menuFrame = f.iconBar.menuFrame
            f.iconBar.pack()
        return f.iconBar
        
    def getIconBar(self):
        return self.iconBar
    getIconBarObject = getIconBar
    
    def hideIconBar (self):
        if self.iconBar: self.iconBar.hide()
    #@nonl
    #@-node:ekr.20031218072017.3953:Icon area methods (compatibility)
    #@+node:ekr.20041223105114.1:Status line methods (compatibility)
    def createStatusLine (self):
        f = self ; c = f.c
        if not self.statusLine:
            f.statusLine  = statusLine = f.statusLineClass(c,f.outerFrame)
            #f.statusFrame = statusLine.statusFrame
            #f.statusLabel = statusLine.labelWidget
            #f.statusText  = statusLine.textWidget
            #statusLine.pack()
        return self.statusLine
    
    def clearStatusLine (self):
        if self.statusLine: self.statusLine.clear()
        
    def disableStatusLine (self,background=None):
        if self.statusLine: self.statusLine.disable(background)
    
    def enableStatusLine (self,background="white"):
        if self.statusLine: self.statusLine.enable(background)
    
    def getStatusLine (self):
        return self.statusLine
        
    getStatusObject = getStatusLine
        
    def putStatusLine (self,s,color=None):
        if self.statusLine: self.statusLine.put(s,color)
        
    def setFocusStatusLine (self):
        if self.statusLine: self.statusLine.setFocus()
    
    def statusLineIsEnabled(self):
        return self.statusLine and self.statusLine.isEnabled()
        
    def updateStatusLine(self):
        # agp if self.statusLine: self.statusLine.update()
        c = self.c ; w = c.frame.bodyCtrl
    
        if g.app.killed:
            return
    
        index = w.index("insert")
        row,col = g.app.gui.getindex(w,index)
        
        #print index,row,col
    
        if col > 0:
            s = w.get("%d.0" % (row),index)
            s = g.toUnicode(s,g.app.tkEncoding)
            col = g.computeWidth (s,c.tab_width)
        
        s = "line %d, col %d " % (row,col)
        # Important: this does not change the focus because labels never get focus.
        self.RowColWidget.configure(text=s)
        
    #@nonl
    #@-node:ekr.20041223105114.1:Status line methods (compatibility)
    #@+node:ekr.20031218072017.3967:Configuration (tkFrame)
    #@+node:AGP.20231115175745.1:reconfigure()
    def reconfigure(self):
        
        leocfg = self.c.config
        
        cadd,cmul,cscale = g.color_add,g.color_mul,g.colorf_scale
        
        #u=0.25
        #bg= cadd( cmul( 1.0-u,g.color_theme['bg']), cmul( u,g.color_theme['fg']) )
        bg = g.theme['shade'](0.3)
        #bg=g.color_theme['bg']
        #self.menuFrame.config(relief='groove',bd=0,bg=bg)
        self.iconFrame.config(relief='groove',bd=0,bg=g.theme['shade'](0.25))
        self.StatusFrame.config(relief='groove',bd=0,bg=bg)
        self.StatusLabel.config(bd=0,bg=bg)
        self.RowColWidget.config(relief='groove',bd=0,bg=bg)
        
        bg75 = cmul(0.75,bg)
        
        if hasattr(self,"searchbox"):
            sb = self.searchbox
            sb.searchbox.config(bg=bg75)
            sb.changebox.config(bg=bg75)
            sb.tolabel.config(bg=bg)
            sb.action_button.config(bg=bg)
        
        
        
        
        
        
        outerframe,editframe,bodyframe,treeframe,subtreeframe,logframe,qlinkframe,treefont = self.guiframes
        
        self.bar1.config(bg=bg)
        self.bar2.config(bg=bg)
        
        
        outerframe.config(bg=g.theme['bg'])
        
        hlc = cscale(g.theme['fg'],0.6)#"#DDDDFF"
        
        frame_default = dict(relief='groove',bd=0,highlightthickness=1)
        
        logframe.config(**frame_default)
        subtreeframe.config(**frame_default)
        bodyframe.config(**frame_default)
        
        qlinkframe.config(**frame_default)
        qlinkframe.config(highlightbackground=hlc,bg=g.theme['shade'](0.20))
        #self.canvas.config()
        
        #body_cfg = leocfg.get('body','config')
        #self.body.bodyCtrl.config(**body_cfg)
        
        
            
        #bg = treeframe.cget('bg')
        #bg = g.color_mul(0.5,bg)
    
    #@-node:AGP.20231115175745.1:reconfigure()
    #@+node:ekr.20031218072017.3968:XconfigureBar
    def configureBar (self,bar,verticalFlag):
        #print "config bar"
        c = self.c
    
        # Get configuration settings.
        w = c.config.getInt("split_bar_width")
        if not w or w < 1: w = 7
        relief = c.config.get("split_bar_relief","relief")
        if not relief: relief = "flat"
        color = c.config.getColor("split_bar_color") or g.theme['bg']
        
        if not color: color = "LightSteelBlue2"
        relief = "flat"
        w=5
        color = bar.cget('bg')#g.color_theme["bg"]
        try:
            if verticalFlag:
                # Panes arranged vertically; horizontal splitter bar
                bar.configure(relief=relief,height=w,bg=color,cursor="sb_v_double_arrow")
            else:
                # Panes arranged horizontally; vertical splitter bar
                bar.configure(relief=relief,width=w,bg=color,cursor="sb_h_double_arrow")
        except: # Could be a user error. Use all defaults
            g.es("exception in user configuration for splitbar")
            g.es_exception()
            if verticalFlag:
                # Panes arranged vertically; horizontal splitter bar
                bar.configure(height=w,cursor="sb_v_double_arrow")
            else:
                # Panes arranged horizontally; vertical splitter bar
                bar.configure(width=w,cursor="sb_h_double_arrow")
    #@-node:ekr.20031218072017.3968:XconfigureBar
    #@+node:ekr.20031218072017.3969:configureBarsFromConfig
    def configureBarsFromConfig (self):
        #print "config bar from config"
        c = self.c
    
        w = c.config.getInt("split_bar_width")
        if not w or w < 1: w = 7
        
        relief = c.config.get("split_bar_relief","relief")
        if not relief or relief == "": relief = "flat"
    
        color = c.config.getColor("split_bar_color")
        if not color or color == "": color = "LightSteelBlue2"
    
        if self.splitVerticalFlag:
            bar1,bar2=self.bar1,self.bar2
        else:
            bar1,bar2=self.bar2,self.bar1
            
        try:
            bar1.configure(relief=relief,height=w,bg=color)
            bar2.configure(relief=relief,width=w,bg=color)
        except: # Could be a user error.
            g.es("exception in user configuration for splitbar")
            g.es_exception()
    #@-node:ekr.20031218072017.3969:configureBarsFromConfig
    #@+node:ekr.20031218072017.2246:reconfigureFromConfig
    def reconfigureFromConfig (self):
        
        frame = self ; c = frame.c
        
        #frame.tree.setFontFromConfig()
        #frame.tree.setColorFromConfig()
        
        #frame.configureBarsFromConfig()
        
        #frame.body.setFontFromConfig()
        #frame.body.setColorFromConfigt()
        
        #frame.setTabWidth(c.tab_width)
        #frame.log.setFontFromConfig()
        #frame.log.setColorFromConfig()
    
        c.redraw_now()
    #@-node:ekr.20031218072017.2246:reconfigureFromConfig
    #@+node:ekr.20031218072017.1625:setInitialWindowGeometry
    def setInitialWindowGeometry(self):
        
        """Set the position and size of the frame to config params."""
        
        c = self.c
        
        h = c.config.getInt("initial_window_height") or 500
        w = c.config.getInt("initial_window_width") or 600
        x = c.config.getInt("initial_window_left") or 10
        y = c.config.getInt("initial_window_top") or 10
        
        if h and w and x and y:
            self.setTopGeometry(w,h,x,y)
    #@-node:ekr.20031218072017.1625:setInitialWindowGeometry
    #@+node:ekr.20031218072017.722:setTabWidth
    def setTabWidth (self, w):
        
        try: # This can fail when called from scripts
            # Use the present font for computations.
            font = self.bodyCtrl.cget("font")
            root = g.app.root # 4/3/03: must specify root so idle window will work properly.
            font = tkFont.Font(root=root,font=font)
            tabw = font.measure(" " * abs(w)) # 7/2/02
            self.bodyCtrl.configure(tabs=tabw)
            self.tab_width = w
            # g.trace(w,tabw)
        except:
            g.es_exception()
            pass
    #@-node:ekr.20031218072017.722:setTabWidth
    #@+node:ekr.20031218072017.1540:f.setWrap
    def setWrap (self,p):
        
        c = self.c
        theDict = g.scanDirectives(c,p)
        if not theDict: return
        
        wrap = theDict.get("wrap")
        if self.body.wrapState == wrap: return
    
        self.body.wrapState = wrap
        # g.trace(wrap)
        if wrap:
            self.bodyCtrl.configure(wrap="word")
            self.bodyXBar.pack_forget()
        else:
            self.bodyCtrl.configure(wrap="none")
            # Bug fix: 3/10/05: We must unpack the text area to make the scrollbar visible.
            self.bodyCtrl.pack_forget()
            self.bodyXBar.pack(side="bottom", fill="x")
            self.bodyCtrl.pack(expand=1,fill="both")
    #@-node:ekr.20031218072017.1540:f.setWrap
    #@+node:ekr.20031218072017.2307:setTopGeometry
    def setTopGeometry(self,w,h,x,y,adjustSize=True):
        self.topgeometry = w,h,x,y
        # Put the top-left corner on the screen.
        x = max(10,x) ; y = max(10,y)
        
        if adjustSize:
            top = self.top
            sw = top.winfo_screenwidth()
            sh = top.winfo_screenheight()
    
            # Adjust the size so the whole window fits on the screen.
            w = min(sw-10,w)
            h = min(sh-10,h)
    
            # Adjust position so the whole window fits on the screen.
            if x + w > sw: x = 10
            if y + h > sh: y = 10
        
        geom = "%dx%d%+d%+d" % (w,h,x,y)
        
        self.top.geometry(geom)
    #@-node:ekr.20031218072017.2307:setTopGeometry
    #@+node:ekr.20031218072017.3970:reconfigurePanes (use config bar_width)
    def reconfigurePanes (self):
        #print "reconfigurePanes"
        c = self.c
        #print "reconfiguepanes"
        border = c.config.getInt('additional_body_text_border')
        if border == None: border = 0
        
        # The body pane needs a _much_ bigger border when tiling horizontally.
        #border = g.choose(self.splitVerticalFlag,2+border,6+border)
        #self.bodyCtrl.configure(bd=border)
        
        # The log pane needs a slightly bigger border when tiling vertically.
        #border = g.choose(self.splitVerticalFlag,4,2) 
        #self.log.configureBorder(border)
    #@-node:ekr.20031218072017.3970:reconfigurePanes (use config bar_width)
    #@-node:ekr.20031218072017.3967:Configuration (tkFrame)
    #@+node:ekr.20031218072017.3971:Event handlers (tkFrame)
    #@+node:ekr.20031218072017.3972:frame.OnCloseLeoEvent
    # Called from quit logic and when user closes the window.
    # Returns True if the close happened.
    
    def OnCloseLeoEvent(self):
        
        f = self ; c = f.c
        
        if c.inCommand:
            g.trace('requesting window close')
            c.requestCloseWindow = True
        else:
            g.app.closeLeoWindow(self)
    #@-node:ekr.20031218072017.3972:frame.OnCloseLeoEvent
    #@+node:ekr.20031218072017.3973:frame.OnControlKeyUp/Down
    def OnControlKeyDown (self,event=None):
        
        __pychecker__ = '--no-argsused' # event not used.
        
        self.controlKeyIsDown = True
        
    def OnControlKeyUp (self,event=None):
        
        __pychecker__ = '--no-argsused' # event not used.
    
        self.controlKeyIsDown = False
    #@-node:ekr.20031218072017.3973:frame.OnControlKeyUp/Down
    #@+node:ekr.20031218072017.3975:OnActivateBody (tkFrame)
    def OnActivateBody (self,event=None):
        
        __pychecker__ = '--no-argsused' # event not used.
    
        try:
            frame = self ; c = frame.c
            c.setLog()
            w = c.get_focus()
            if w != c.frame.body.bodyCtrl:
                frame.tree.OnDeactivate()
            c.bodyWantsFocus()
        except:
            g.es_event_exception("activate body")
            
        return 'break'
    #@-node:ekr.20031218072017.3975:OnActivateBody (tkFrame)
    #@+node:ekr.20031218072017.2253:OnActivateLeoEvent, OnDeactivateLeoEvent
    def OnActivateLeoEvent(self,event=None):
        
        '''Handle a click anywhere in the Leo window.'''
        
        __pychecker__ = '--no-argsused' # event.
    
        self.c.setLog()
    
    def OnDeactivateLeoEvent(self,event=None):
        
        pass # This causes problems on the Mac.
    #@-node:ekr.20031218072017.2253:OnActivateLeoEvent, OnDeactivateLeoEvent
    #@+node:ekr.20031218072017.3976:OnActivateTree
    def OnActivateTree (self,event=None):
    
        try:
            frame = self ; c = frame.c
            c.setLog()
    
            if 0: # Do NOT do this here!
                # OnActivateTree can get called when the tree gets DE-activated!!
                c.bodyWantsFocus()
                
        except:
            g.es_event_exception("activate tree")
    #@-node:ekr.20031218072017.3976:OnActivateTree
    #@+node:ekr.20031218072017.3977:OnBodyClick, OnBodyRClick (Events)
    def OnBodyClick (self,event=None):
    
        try:
            c = self.c ; p = c.currentPosition()
            if not g.doHook("bodyclick1",c=c,p=p,v=p,event=event):
                self.OnActivateBody(event=event)
            g.doHook("bodyclick2",c=c,p=p,v=p,event=event)
        except:
            g.es_event_exception("bodyclick")
    
    def OnBodyRClick(self,event=None):
        
        try:
            c = self.c ; p = c.currentPosition()
            if not g.doHook("bodyrclick1",c=c,p=p,v=p,event=event):
                return "break" #pass # By default Leo does nothing.     mod by AGP
            g.doHook("bodyrclick2",c=c,p=p,v=p,event=event)
        except:
            g.es_event_exception("bodyrclick")
    #@-node:ekr.20031218072017.3977:OnBodyClick, OnBodyRClick (Events)
    #@+node:ekr.20031218072017.3978:OnBodyDoubleClick (Events)
    def OnBodyDoubleClick (self,event=None):
    
        try:
            c = self.c ; p = c.currentPosition()
            if event and not g.doHook("bodydclick1",c=c,p=p,v=p,event=event):
                c.editCommands.extendToWord(event) # Handles unicode properly.
            g.doHook("bodydclick2",c=c,p=p,v=p,event=event)
        except:
            g.es_event_exception("bodydclick")
            
        return "break" # Restore this to handle proper double-click logic.
    #@-node:ekr.20031218072017.3978:OnBodyDoubleClick (Events)
    #@+node:ekr.20031218072017.1803:OnMouseWheel (Tomaz Ficko)
    # Contributed by Tomaz Ficko.  This works on some systems.
    # On XP it causes a crash in tcl83.dll.  Clearly a Tk bug.
    
    def OnMouseWheel(self, event=None):
        #print "omw"
        try:
            if event.delta < 1:
                self.canvas.yview(Tk.SCROLL, 1, Tk.UNITS)
            else:
                self.canvas.yview(Tk.SCROLL, -1, Tk.UNITS)
        except:
            g.es_event_exception("scroll wheel")
    
        return "break"
    #@-node:ekr.20031218072017.1803:OnMouseWheel (Tomaz Ficko)
    #@+node:AGP.20231020155235:OnCanvasB2 (agp)
    def OnCanvasB2(self, event=None):
        self.lastx = event.x
        return  
    #@-node:AGP.20231020155235:OnCanvasB2 (agp)
    #@+node:AGP.20231020122619:OnCanvasMotion (agp)
    def OnCanvasMotion(self, event=None):
        try:
            x = event.x_root    # agp        
        
            if self.lastx != -1:
                if x < self.lastx:
                    self.canvas.xview(Tk.SCROLL, 1, Tk.UNITS)
                elif x > self.lastx:
                    self.canvas.xview(Tk.SCROLL, -1, Tk.UNITS)
                else:
                    return
            
            self.lastx = x
        
        except:
            g.es_event_exception("canvas motion")
    
        return "break"
    #@-node:AGP.20231020122619:OnCanvasMotion (agp)
    #@+node:ekr.20061016071937:OnPaste (To support middle-button paste)
    def OnPaste (self,event=None):
        
        return self.pasteText(event=event,middleButton=True)
    #@nonl
    #@-node:ekr.20061016071937:OnPaste (To support middle-button paste)
    #@-node:ekr.20031218072017.3971:Event handlers (tkFrame)
    #@+node:ekr.20031218072017.3979:Gui-dependent commands
    #@+node:ekr.20060209110128:Minibuffer commands... (tkFrame)
    
    #@+node:ekr.20060209110128.1:contractPane
    def contractPane (self,event=None):
        
        '''Contract the selected pane.'''
        
        f = self ; c = f.c
        w = c.get_requested_focus()
        wname = c.widget_name(w)
    
        # g.trace(wname)
        if not w: return
        
        if wname.startswith('body'):
            f.contractBodyPane()
        elif wname.startswith('log'):
            f.contractLogPane()
        elif wname.startswith('head') or wname.startswith('canvas'):
            f.contractOutlinePane()
    #@-node:ekr.20060209110128.1:contractPane
    #@+node:ekr.20060209110128.2:expandPane
    def expandPane (self,event=None):
        
        '''Expand the selected pane.'''
    
        f = self ; c = f.c
            
        w = c.get_requested_focus()
        wname = c.widget_name(w)
    
        # g.trace(wname)
        if not w: return
        
        if wname.startswith('body'):
            f.expandBodyPane()
        elif wname.startswith('log'):
            f.expandLogPane()
        elif wname.startswith('head') or wname.startswith('canvas'):
            f.expandOutlinePane()
    #@-node:ekr.20060209110128.2:expandPane
    #@+node:ekr.20060210123852:fullyExpandPane
    def fullyExpandPane (self,event=None):
        
        '''Fully expand the selected pane.'''
    
        f = self ; c = f.c
            
        w = c.get_requested_focus()
        wname = c.widget_name(w)
    
        # g.trace(wname)
        if not w: return
        
        if wname.startswith('body'):
            f.fullyExpandBodyPane()
        elif wname.startswith('log'):
            f.fullyExpandLogPane()
        elif wname.startswith('head') or wname.startswith('canvas'):
            f.fullyExpandOutlinePane()
    #@-node:ekr.20060210123852:fullyExpandPane
    #@+node:ekr.20060209143933:hidePane
    def hidePane (self,event=None):
        
        '''Completely contract the selected pane.'''
    
        f = self ; c = f.c
            
        w = c.get_requested_focus()
        wname = c.widget_name(w)
    
        g.trace(wname)
        if not w: return
        
        if wname.startswith('body'):
            f.hideBodyPane()
            c.treeWantsFocusNow()
        elif wname.startswith('log'):
            f.hideLogPane()
            c.bodyWantsFocusNow()
        elif wname.startswith('head') or wname.startswith('canvas'):
            f.hideOutlinePane()
            c.bodyWantsFocusNow()
    #@-node:ekr.20060209143933:hidePane
    #@+node:ekr.20060209110936:expand/contract/hide...Pane
    #@+at 
    #@nonl
    # The first arg to divideLeoSplitter means the following:
    # 
    #     f.splitVerticalFlag: use the primary   (tree/body) ratio.
    # not f.splitVerticalFlag: use the secondary (tree/log) ratio.
    #@-at
    #@@c
    
    def contractBodyPane (self,event=None):
        '''Contract the body pane.'''
        f = self ; r = min(1.0,f.ratio+0.1)
        f.divideLeoSplitter(f.splitVerticalFlag,r)
    
    def contractLogPane (self,event=None):
        '''Contract the log pane.'''
        f = self ; r = min(1.0,f.ratio+0.1)
        f.divideLeoSplitter(not f.splitVerticalFlag,r)
    
    def contractOutlinePane (self,event=None):
        '''Contract the outline pane.'''
        f = self ; r = max(0.0,f.ratio-0.1)
        f.divideLeoSplitter(f.splitVerticalFlag,r)
        
    def expandBodyPane (self,event=None):
        '''Expand the body pane.'''
        self.contractOutlinePane()
    
    def expandLogPane(self,event=None):
        '''Expand the log pane.'''
        f = self ; r = max(0.0,f.ratio-0.1)
        f.divideLeoSplitter(not f.splitVerticalFlag,r)
        
    def expandOutlinePane (self,event=None):
        '''Expand the outline pane.'''
        self.contractBodyPane()
    #@-node:ekr.20060209110936:expand/contract/hide...Pane
    #@+node:ekr.20060210123852.1:fullyExpand/hide...Pane
    def fullyExpandBodyPane (self,event=None):
        '''Fully expand the body pane.'''
        f = self ; f.divideLeoSplitter(f.splitVerticalFlag,0.0)
    
    def fullyExpandLogPane (self,event=None):
        '''Fully expand the log pane.'''
        f = self ; f.divideLeoSplitter(not f.splitVerticalFlag,0.0)
    
    def fullyExpandOutlinePane (self,event=None):
        '''Fully expand the outline pane.'''
        f = self ; f.divideLeoSplitter(f.splitVerticalFlag,1.0)
        
    def hideBodyPane (self,event=None):
        '''Completely contract the body pane.'''
        f = self ; f.divideLeoSplitter(f.splitVerticalFlag,1.0)
    
    def hideLogPane (self,event=None):
        '''Completely contract the log pane.'''
        f = self ; f.divideLeoSplitter(not f.splitVerticalFlag,1.0)
    
    def hideOutlinePane (self,event=None):
        '''Completely contract the outline pane.'''
        f = self ; f.divideLeoSplitter(f.splitVerticalFlag,0.0)
    #@-node:ekr.20060210123852.1:fullyExpand/hide...Pane
    #@-node:ekr.20060209110128:Minibuffer commands... (tkFrame)
    #@+node:ekr.20031218072017.3980:Edit Menu...
    #@+node:ekr.20031218072017.3981:abortEditLabelCommand
    def abortEditLabelCommand (self,event=None):
        
        '''End editing of a headline and revert to its previous value.'''
        
        frame = self ; c = frame.c ; tree = frame.tree
        p = c.currentPosition() ; w = c.edit_widget(p)
        
        if g.app.batchMode:
            c.notValidInBatchMode("Abort Edit Headline")
            return
            
        # g.trace('isEditing',p == tree.editPosition(),'revertHeadline',repr(tree.revertHeadline))
            
        if w and p == tree.editPosition():
            # Revert the headline text.
            w.delete("1.0","end")
            w.insert("end",tree.revertHeadline)
            p.initHeadString(tree.revertHeadline)
            c.beginUpdate()
            try:
                c.endEditing()
                c.selectPosition(p)
            finally:
                c.endUpdate()
    #@-node:ekr.20031218072017.3981:abortEditLabelCommand
    #@+node:ekr.20031218072017.3982:endEditLabelCommand
    def endEditLabelCommand (self,event=None):
        
        '''End editing of a headline and move focus to the body pane.'''
        #print "stayintree:",c.config.getBool('stayInTreeAfterEditHeadline')
        frame = self ; c = frame.c
        if g.app.batchMode:
            c.notValidInBatchMode("End Edit Headline")
        else:
            c.endEditing()
            
            if c.config.getBool('stayInTreeAfterEditHeadline'):
                c.treeWantsFocusNow()
            else:
                c.bodyWantsFocusNow() 
    #@nonl
    #@-node:ekr.20031218072017.3982:endEditLabelCommand
    #@+node:ekr.20031218072017.3983:insertHeadlineTime
    def insertHeadlineTime (self,event=None):
        
        '''Insert a date/time stamp in the headline of the selected node.'''
    
        frame = self ; c = frame.c ; p = c.currentPosition()
        
        if g.app.batchMode:
            c.notValidInBatchMode("Insert Headline Time")
            return
            
        c.editPosition(p)
        c.frame.tree.setEditLabelState(p)
        w = c.edit_widget(p)
        if w:
            time = c.getTime(body=False)
            if 1: # We can't know if we were already editing, so insert at end.
                g.app.gui.setSelectionRange(w,'end','end')
                w.insert('end',time)
            else:
                i, j = g.app.gui.getTextSelection(w)
                if i != j:
                    w.delete(i,j)
                w.insert("insert",time)
            c.frame.tree.onHeadChanged(p,'Insert Headline Time')
    #@-node:ekr.20031218072017.3983:insertHeadlineTime
    #@+node:ekr.20031218072017.840:Cut/Copy/Paste (tkFrame)
    #@+node:ekr.20051011072903.2:copyText
    def copyText (self,event=None):
        
        '''Copy the selected text from the widget to the clipboard.'''
        
        f = self ; c = f.c ; w = event and event.widget
        if not w or not g.app.gui.isTextWidget(w): return
    
        # Set the clipboard text.
        i,j = g.app.gui.getTextSelection(w)
        if i != j:
            s = w.get(i,j)
            g.app.gui.replaceClipboardWith(s)
            
    OnCopyFromMenu = copyText
    #@-node:ekr.20051011072903.2:copyText
    #@+node:ekr.20051011072049.2:cutText
    def cutText (self,event=None):
        
        '''Invoked from the mini-buffer and from shortcuts.'''
        
        f = self ; c = f.c ; w = event and event.widget
        if not w or not g.app.gui.isTextWidget(w): return
    
        name = c.widget_name(w)
        oldSel = g.app.gui.getTextSelection(w)
        oldText = g.app.gui.getAllText(w)
        i,j = g.app.gui.getTextSelection(w)
        
        # Update the widget and set the clipboard text.
        s = w.get(i,j)
        if i != j:
            w.delete(i,j)
            g.app.gui.replaceClipboardWith(s)
    
        if name.startswith('body'):
            c.frame.body.forceFullRecolor()
            c.frame.body.onBodyChanged('Cut',oldSel=oldSel,oldText=oldText)
        elif name.startswith('head'):
            # The headline is not officially changed yet.
            # p.initHeadString(s)
            s=g.app.gui.getAllText(w)
            w.configure(width=f.tree.headWidth(s=s))
        else: pass
    
    OnCutFromMenu = cutText
    #@-node:ekr.20051011072049.2:cutText
    #@+node:ekr.20051011072903.5:pasteText
    def pasteText (self,event=None,middleButton=False):
    
        '''Paste the clipboard into a widget.
        If middleButton is True, support x-windows middle-mouse-button easter-egg.'''
    
        f = self ; c = f.c ; w = event and event.widget
        if not w or not g.app.gui.isTextWidget(w): return
    
        wname = c.widget_name(w)
        i,j = oldSel = g.app.gui.getTextSelection(w)  # Returns insert point if no selection.
        oldText = w.get('1.0','end')
        
        # print 'pasteText',i,j,middleButton,wname,repr(c.k.previousSelection)
        
        if middleButton and c.k.previousSelection:
            start,end = c.k.previousSelection
            s = w.get(start,end)
            c.k.previousSelection = None
        else:
            s = s1 = g.app.gui.getTextFromClipboard()
        
        singleLine = wname.startswith('head') or wname.startswith('minibuffer')
        
        if singleLine:
            # Strip trailing newlines so the truncation doesn't cause confusion.
            while s and s [ -1] in ('\n','\r'):
                s = s [: -1]
    
        try:
            # Update the widget.
            if i != j:
                w.delete(i,j)
            w.insert(i,s)
        
            if wname.startswith('body'):
                c.frame.body.forceFullRecolor()
                c.frame.body.onBodyChanged('Paste',oldSel=oldSel,oldText=oldText)
            elif singleLine:
                s = w.get('1.0','end')
                while s and s [ -1] in ('\n','\r'):
                    s = s [: -1]
                if wname.startswith('head'):
                    # The headline is not officially changed yet.
                    # p.initHeadString(s)
                    w.configure(width=f.tree.headWidth(s=s))
            else: pass
        except Exception:
            pass # Tk sometimes throws weird exceptions here.
            
        return 'break' # Essential
    
    OnPasteFromMenu = pasteText
    #@-node:ekr.20051011072903.5:pasteText
    #@+node:AGP.20230208143607:swapText
    def swapText(self,event=None,middleButton=False): #agp
    
        '''Paste the clipboard into a widget.
        If middleButton is True, support x-windows middle-mouse-button easter-egg.'''
    
        f = self ; c = f.c ; w = event and event.widget
        if not w or not g.app.gui.isTextWidget(w): return
    
        
        # get the selected text agp
        i,j = g.app.gui.getTextSelection(w)
        if i != j:
            text_to_cb = w.get(i,j)
            #g.app.gui.replaceClipboardWith(s)
        
        
        
        
        wname = c.widget_name(w)
        i,j = oldSel = g.app.gui.getTextSelection(w)  # Returns insert point if no selection.
        oldText = w.get('1.0','end')
        
        # print 'pasteText',i,j,middleButton,wname,repr(c.k.previousSelection)
        
        if middleButton and c.k.previousSelection:
            start,end = c.k.previousSelection
            s = w.get(start,end)
            c.k.previousSelection = None
        else:
            s = s1 = g.app.gui.getTextFromClipboard()
        
        singleLine = wname.startswith('head') or wname.startswith('minibuffer')
        
        if singleLine:
            # Strip trailing newlines so the truncation doesn't cause confusion.
            while s and s [ -1] in ('\n','\r'):
                s = s [: -1]
    
        try:
            # Update the widget.
            if i != j:
                w.delete(i,j)
            w.insert(i,s)
        
            
            if wname.startswith('body'):
                c.frame.body.forceFullRecolor()
                c.frame.body.onBodyChanged('Paste',oldSel=oldSel,oldText=oldText)
            elif singleLine:
                s = w.get('1.0','end')
                while s and s [ -1] in ('\n','\r'):
                    s = s [: -1]
                if wname.startswith('head'):
                    # The headline is not officially changed yet.
                    # p.initHeadString(s)
                    w.configure(width=f.tree.headWidth(s=s))
            else: pass
            
            #put text_to_cb agp
            g.app.gui.replaceClipboardWith(text_to_cb)
            
        except Exception:
            pass # Tk sometimes throws weird exceptions here.
        
        
        
        return 'break' # Essential
    
    OnPasteFromMenu = pasteText
    #@-node:AGP.20230208143607:swapText
    #@-node:ekr.20031218072017.840:Cut/Copy/Paste (tkFrame)
    #@-node:ekr.20031218072017.3980:Edit Menu...
    #@+node:ekr.20031218072017.3984:Window Menu...
    #@+node:ekr.20031218072017.3985:toggleActivePane
    def toggleActivePane (self,event=None):
        
        '''Toggle the focus between the outline and body panes.'''
        
        frame = self ; c = frame.c
    
        if c.get_focus() == frame.bodyCtrl:
            c.treeWantsFocusNow()
        else:
            c.endEditing()
            c.bodyWantsFocusNow()
    #@-node:ekr.20031218072017.3985:toggleActivePane
    #@+node:ekr.20031218072017.3986:cascade
    def cascade (self,event=None):
        
        '''Cascade all Leo windows.'''
    
        x,y,delta = 10,10,10
        for frame in g.app.windowList:
            top = frame.top
    
            # Compute w,h
            top.update_idletasks() # Required to get proper info.
            geom = top.geometry() # geom = "WidthxHeight+XOffset+YOffset"
            dim,junkx,junky = string.split(geom,'+')
            w,h = string.split(dim,'x')
            w,h = int(w),int(h)
    
            # Set new x,y and old w,h
            frame.setTopGeometry(w,h,x,y,adjustSize=False)
    
            # Compute the new offsets.
            x += 30 ; y += 30
            if x > 200:
                x = 10 + delta ; y = 40 + delta
                delta += 10
    #@-node:ekr.20031218072017.3986:cascade
    #@+node:ekr.20031218072017.3987:equalSizedPanes
    def equalSizedPanes (self,event=None):
        
        '''Make the outline and body panes have the same size.'''
    
        frame = self
        print "equalsizedpanes"
        frame.resizePanesToRatio(0.5,frame.secondary_ratio)
    #@-node:ekr.20031218072017.3987:equalSizedPanes
    #@+node:ekr.20031218072017.3988:hideLogWindow
    def hideLogWindow (self,event=None):
        
        frame = self
        frame.divideLeoSplitter2(0.99, not frame.splitVerticalFlag)
    #@-node:ekr.20031218072017.3988:hideLogWindow
    #@+node:ekr.20031218072017.3989:minimizeAll
    def minimizeAll (self,event=None):
    
        '''Minimize all Leo's windows.'''
        
        self.minimize(g.app.pythonFrame)
        for frame in g.app.windowList:
            self.minimize(frame)
            self.minimize(frame.findPanel)
        
    def minimize(self,frame):
    
        if frame and frame.top.state() == "normal":
            frame.top.iconify()
    #@-node:ekr.20031218072017.3989:minimizeAll
    #@+node:ekr.20031218072017.3990:toggleSplitDirection (tkFrame)
    # The key invariant: self.splitVerticalFlag tells the alignment of the main splitter.
    
    def toggleSplitDirection (self,event=None):
        
        '''Toggle the split direction in the present Leo window.'''
        
        # Switch directions.
        c = self.c
        self.splitVerticalFlag = not self.splitVerticalFlag
        orientation = g.choose(self.splitVerticalFlag,"vertical","horizontal")
        c.config.set("initial_splitter_orientation","string",orientation)
        
        self.toggleTkSplitDirection(self.splitVerticalFlag)
    #@+node:AGP.20240829193937:toggleTkSplitDirection
    def toggleTkSplitDirection (self,verticalFlag):
    
        
        frame = self
        bar1 = self.bar1 ; bar2 = self.bar2
        
        bar1.place_forget()
        bar2.place_forget()
        
        
        bar1.vflag = not bar1.vflag
        
        if bar1.vflag:
            bar1.configure(cursor="sb_v_double_arrow")
        
        else:
            bar1.configure(cursor="sb_h_double_arrow")
            
        
        
        bar2.vflag = not bar2.vflag
        if bar2.vflag:
            bar2.configure(cursor="sb_v_double_arrow")
        else:
            bar2.configure(cursor="sb_h_double_arrow")
        
        
        
        self.splitter_relplace(bar1,0.5)
        self.splitter_relplace(bar2,0.5)
        
    
        
    #@-node:AGP.20240829193937:toggleTkSplitDirection
    #@+node:ekr.20041221122440.2:XtoggleTkSplitDirection
    def XtoggleTkSplitDirection (self,verticalFlag):
    
        # Abbreviations.
        frame = self
        bar1 = self.bar1 ; bar2 = self.bar2
        split1Pane1,split1Pane2 = self.split1Pane1,self.split1Pane2
        split2Pane1,split2Pane2 = self.split2Pane1,self.split2Pane2
        # Reconfigure the bars.
        bar1.place_forget()
        bar2.place_forget()
        
        
        self.configureBar(bar1,verticalFlag)
        self.configureBar(bar2,not verticalFlag)
        # Make the initial placements again.
        self.placeSplitter(bar1,split1Pane1,split1Pane2,verticalFlag)
        self.placeSplitter(bar2,split2Pane1,split2Pane2,not verticalFlag)
        # Adjust the log and body panes to give more room around the bars.
        self.reconfigurePanes()
        # Redraw with an appropriate ratio.
        vflag,ratio,secondary_ratio = frame.initialRatios()
        print "togglesplit"
        self.resizePanesToRatio(ratio,secondary_ratio)
    #@-node:ekr.20041221122440.2:XtoggleTkSplitDirection
    #@-node:ekr.20031218072017.3990:toggleSplitDirection (tkFrame)
    #@+node:EKR.20040422130619:resizeToScreen
    def resizeToScreen (self,event=None):
        
        '''Resize the Leo window so it fill the entire screen.'''
        
        top = self.top
        
        w = top.winfo_screenwidth()
        h = top.winfo_screenheight()
    
        if sys.platform == 'darwin':
            # Must leave room to get at very small resizing area.
            geom = "%dx%d%+d%+d" % (w-20,h-55,10,25)
        else:
            # Fill almost the entire screen.
            # Works on Windows. YMMV for other platforms.
            geom = "%dx%d%+d%+d" % (w-8,h-46,0,0)
       
        top.geometry(geom)
    #@-node:EKR.20040422130619:resizeToScreen
    #@-node:ekr.20031218072017.3984:Window Menu...
    #@+node:ekr.20031218072017.3991:Help Menu...
    #@+node:ekr.20031218072017.3992:leoHelp
    def leoHelp (self,event=None):
        
        '''Open Leo's offline tutorial.'''
        
        frame = self ; c = frame.c
        
        theFile = g.os_path_join(g.app.loadDir,"..","doc","sbooks.chm")
    
        if g.os_path_exists(theFile):
            os.startfile(theFile)
        else:
            answer = g.app.gui.runAskYesNoDialog(c,
                "Download Tutorial?",
                "Download tutorial (sbooks.chm) from SourceForge?")
    
            if answer == "yes":
                try:
                    if 0: # Download directly.  (showProgressBar needs a lot of work)
                        url = "http://umn.dl.sourceforge.net/sourceforge/leo/sbooks.chm"
                        import urllib
                        self.scale = None
                        urllib.urlretrieve(url,theFile,self.showProgressBar)
                        if self.scale:
                            self.scale.destroy()
                            self.scale = None
                    else:
                        url = "http://prdownloads.sourceforge.net/leo/sbooks.chm?download"
                        import webbrowser
                        os.chdir(g.app.loadDir)
                        webbrowser.open_new(url)
                except:
                    g.es("exception dowloading sbooks.chm")
                    g.es_exception()
    #@+node:ekr.20031218072017.3993:showProgressBar
    def showProgressBar (self,count,size,total):
    
        # g.trace("count,size,total:",count,size,total)
        if self.scale == None:
            #@        << create the scale widget >>
            #@+node:ekr.20031218072017.3994:<< create the scale widget >>
            top = Tk.Toplevel()
            top.title("Download progress")
            self.scale = scale = Tk.Scale(top,state="normal",orient="horizontal",from_=0,to=total)
            scale.pack()
            top.lift()
            #@-node:ekr.20031218072017.3994:<< create the scale widget >>
            #@nl
        self.scale.set(count*size)
        self.scale.update_idletasks()
    #@-node:ekr.20031218072017.3993:showProgressBar
    #@-node:ekr.20031218072017.3992:leoHelp
    #@-node:ekr.20031218072017.3991:Help Menu...
    #@-node:ekr.20031218072017.3979:Gui-dependent commands
    #@+node:ekr.20050120083053:Delayed Focus (tkFrame)
    #@+at 
    #@nonl
    # New in 4.3. The proper way to change focus is to call 
    # c.frame.xWantsFocus.
    # 
    # Important: This code never calls select, so there can be no race 
    # condition here
    # that alters text improperly.
    #@-at
    #@-node:ekr.20050120083053:Delayed Focus (tkFrame)
    #@+node:ekr.20031218072017.3995:Tk bindings...
    def bringToFront (self):
        self.top.deiconify()
        self.top.lift()
    
    def getFocus(self):
        """Returns the widget that has focus, or body if None."""
        try:
            # This method is unreliable while focus is changing.
            # The call to update_idletasks may help.  Or not.
            self.top.update_idletasks()
            f = self.top.focus_displayof()
        except Exception:
            f = None
        if f:
            return f
        else:
            return self.bodyCtrl
            
    def getTitle (self):
        return self.top.title()
        
    def setTitle (self,title):
        return self.top.title(title)
        
    def get_window_info(self):
        return g.app.gui.get_window_info(self.top)
        
    def iconify(self):
        self.top.iconify()
    
    def deiconify (self):
        self.top.deiconify()
        
    def lift (self):
        self.top.lift()
        
    def update (self):
        self.top.update()
    #@-node:ekr.20031218072017.3995:Tk bindings...
    #@-others
#@-node:ekr.20031218072017.3940:class leoTkinterFrame
#@+node:ekr.20031218072017.3996:class leoTkinterBody
class leoTkinterBody (leoFrame.leoBody):
    
    """A class that represents the body pane of a Tkinter window."""

    #@    @+others
    #@+node:ekr.20031218072017.2182:__init__()
    def __init__ (self,frame,parentFrame):
        
        # g.trace("leoTkinterBody")
        
        # Call the base class constructor.
        leoFrame.leoBody.__init__(self,frame,parentFrame)
        
        c = self.c ; p = c.currentPosition()
        self.editor_name = None
        self.editor_v = None
        self.editorWidgets = {} # keys are pane names, values are Tk.Text widgets
    
        self.trace_onBodyChanged = c.config.getBool('trace_onBodyChanged')
        self.bodyCtrl = self.createControl(frame,parentFrame,p)
        self.colorizer = leoColor.colorizer(c)
        
        self.colorizer.configure_tags()
        
    #@nonl
    #@-node:ekr.20031218072017.2182:__init__()
    #@+node:ekr.20031218072017.838:createBindings()
    def createBindings (self,w=None):
    
        '''(tkBody) Create gui-dependent bindings.
        These are *not* made in nullBody instances.'''
        
        frame = self.frame ; c = self.c ; k = c.k
        if not w: w = self.bodyCtrl
        
        w.bind('<Key>', k.masterKeyHandler)
        
        w.bind('<ButtonRelease-1>', self.OnLRelease)
        
    
        for kind,func,handler in (
            ('<Button-1>',  frame.OnBodyClick,          k.masterClickHandler),
            ('<Button-3>',  frame.OnBodyRClick,         k.masterClick3Handler),
            ('<Double-1>',  frame.OnBodyDoubleClick,    k.masterDoubleClickHandler),
            ('<Double-3>',  None,                       k.masterDoubleClick3Handler),
            ('<Button-2>',  frame.OnPaste,              k.masterClickHandler),
        ):
            def bodyClickCallback(event,handler=handler,func=func):
                return handler(event,func)
    
            w.bind(kind,bodyClickCallback)
    #@nonl
    #@-node:ekr.20031218072017.838:createBindings()
    #@+node:ekr.20031218072017.3998:createControl()
    def createControl (self,frame,parentFrame,p):
        
        c = self.c
        
        # New in 4.4.1: make the parent frame a Pmw.PanedWidget.
        self.numberOfEditors = 1 ; name = '1'
        self.totalNumberOfEditors = 1
        
        orient = c.config.getString('editor_orientation') or 'horizontal'
        if orient not in ('horizontal','vertical'): orient = 'horizontal'
       
        #self.pb = pb = Pmw.PanedWidget(parentFrame,orient=orient)
        #parentFrame = pb.add(name)
        #pb.pack(expand=1,fill='both') # Must be done after the first page created.
       
        w = self.createTextWidget(frame,parentFrame,p,name)
        self.editorWidgets[name] = w
    
        return w
    #@-node:ekr.20031218072017.3998:createControl()
    #@+node:ekr.20060528100747.3:createTextWidget()
    def createTextWidget (self,frame,parentFrame,p,name):   #agp
        
        c = self.c
        
        #parentFrame.configure(bg='LightSteelBlue1')
    
        wrap = c.config.getBool('body_pane_wraps')
        wrap = g.choose(wrap,"word","none")
        
        # Setgrid=1 cause severe problems with the font panel.
        body = w = Tk.Text(parentFrame, name='bodytext', bd=0, relief="flat", setgrid=0, wrap=wrap,padx=10,pady=10)
        
        body.bind("<MouseWheel>",frame.TopMouseWheel)
        #print str(body),body['font']
        
        frame.bodyBar = self.bodyBar = bodyBar = g.app.gui.SCROLLBAR(parentFrame,1)
        #Tk.Scrollbar(parentFrame,name='bodyBar',bg="black",troughcolor="black")
        
        def yscrollCallback(x,y,bodyBar=bodyBar,w=w):
            # g.trace(x,y)
            if hasattr(w,'leo_scrollBarSpot'):
                w.leo_scrollBarSpot = (x,y)
            return bodyBar.set(x,y)
       
        body['yscrollcommand'] = yscrollCallback # bodyBar.set
    
        bodyBar.command =  body.yview   #['command']
        
        bodyBar.pack(side="right", fill="y")
        
        
        
        # Always create the horizontal bar.
        frame.bodyXBar = self.bodyXBar = bodyXBar = g.app.gui.SCROLLBAR(parentFrame,0)
        #Tk.Scrollbar(parentFrame,name='bodyXBar',orient="horizontal")
        body['xscrollcommand'] = bodyXBar.set
        bodyXBar.command = body.xview    #['command']
        
        
        if wrap == "none":
            # g.trace(parentFrame)
            pass
        
        bodyXBar.pack(side="bottom", fill="x")
            
        body.pack(expand=1,fill="both")
    
        self.wrapState = wrap
    
        if 0: # Causes the cursor not to blink.
            body.configure(insertofftime=0)
            
        # Inject ivars
        if name == '1':
            w.leo_p = w.leo_v = None # Will be set when the second editor is created.
        else:
            w.leo_p = p.copy()
            w.leo_v = body.leo_p.v
        w.leo_active = True
        w.leo_frame = parentFrame
        w.leo_name = name
        w.leo_label = None
        w.leo_label_s = None
        w.leo_scrollBarSpot = None
        w.leo_insertSpot = None
        w.leo_selection = None
    
        return w
    #@nonl
    #@-node:ekr.20060528100747.3:createTextWidget()
    #@+node:ekr.20041217135735.1:setColorFromConfig
    def setColorFromConfig (self,w=None):   #agp
        
        c = self.c
        if not w: w = self.bodyCtrl
        leocfg = c.config
        
        
        
        #w.config(insertbackground='white')
        #print w['insertbackground']
        
        bg =    leocfg.getColor("body_text_background_color")
        
        # g.trace(id(w),bg)
        if bg:
            w.configure(bg=bg)
        
        
        fg = c.config.getColor("body_text_foreground_color")
        
        if fg:
            w.configure(fg=fg,insertbackground=fg)
        
        #self.bodyBar.configure(bg=bg, troughcolor=fg)
        #self.bodyXBar.configure(bg=bg, troughcolor=fg)
        
        
    
        #bg = c.config.getColor("body_insertion_cursor_color")
        #if bg:
        #    w.configure(insertbackground=bg)
            
        sel_bg = c.config.getColor('body_text_selection_background_color') or 'Gray80'
        w.configure(selectbackground=sel_bg)
        
    
        sel_fg = c.config.getColor('body_text_selection_foreground_color') or 'gray10'
        w.configure(selectforeground=sel_fg)
        
      
        if sys.platform != "win32": # Maybe a Windows bug.
            fg = c.config.getColor("body_cursor_foreground_color")
            bg = c.config.getColor("body_cursor_background_color")
            if fg and bg:
                cursor="xterm" + " " + fg + " " + bg
                w.configure(cursor=cursor)
    
    #@-node:ekr.20041217135735.1:setColorFromConfig
    #@+node:ekr.20031218072017.2183:setFontFromConfig
    def setFontFromConfig (self,w=None):
    
        c = self.c
        
        if not w: w = self.bodyCtrl
        
        font = c.config.getFontFromParams(
            "body_text_font_family", "body_text_font_size",
            "body_text_font_slant",  "body_text_font_weight",
            c.config.defaultBodyFontSize)
        
        
        self.fontRef = font # ESSENTIAL: retain a link to font.
        w.configure(font=font)
    
        # g.trace("BODY",body.cget("font"),font.cget("family"),font.cget("weight"))
    #@-node:ekr.20031218072017.2183:setFontFromConfig
    #@+node:ekr.20060528100747:Editors
    #@+at 
    #@nonl
    # **Important**: body.bodyCtrl and body.frame.bodyCtrl must always be the 
    # same.
    #@-at
    #@+node:ekr.20060530204135:recolorWidget
    def recolorWidget (self,w):
    
        c = self.c ; old_w = self.bodyCtrl
        
        # g.trace(id(w),c.currentPosition().headString())
        
        # Save.
        self.bodyCtrl = self.frame.bodyCtrl = w
        
        c.recolor_now(interruptable=False) # Force a complete recoloring.
        
        # Restore.
        self.bodyCtrl = self.frame.bodyCtrl = old_w
    #@nonl
    #@-node:ekr.20060530204135:recolorWidget
    #@+node:ekr.20060530210057:create/select/unselect/Label
    def unselectLabel (self,w):
        
        # g.trace(w.leo_name,w.leo_label_s)
        if not w.leo_label: self.createLabel(w)
        w.leo_label.configure(text=w.leo_label_s,bg='LightSteelBlue1')
            
    def selectLabel (self,w):
        
        # g.trace(w.leo_name,w.leo_label_s)
        # g.trace(self.numberOfEditors)
        if self.numberOfEditors > 1:
            if not w.leo_label: self.createLabel(w)
            w.leo_label.configure(text=w.leo_label_s,bg='white')
        elif w.leo_label:
            w.leo_label.pack_forget()
            w.leo_label = None
    
    def createLabel (self,w):
    
        w.leo_label = Tk.Label(w.leo_frame)
        w.pack_forget()
        w.leo_label.pack(side='top')
        w.pack(expand=1,fill='both')
    #@-node:ekr.20060530210057:create/select/unselect/Label
    #@+node:ekr.20060528100747.1:addEditor
    def addEditor (self,event=None):
        
        '''Add another editor to the body pane.'''
        
        c = self.c ; p = c.currentPosition()
         
        self.totalNumberOfEditors += 1
        self.numberOfEditors += 1
        if self.numberOfEditors == 2:
            # Inject the ivars into the first editor.
            w = self.editorWidgets.get('1')
            w.leo_p = p.copy()
            w.leo_v = w.leo_p.v
            w.leo_label_s = p.headString()
            self.selectLabel(w) # Immediately create the label in the old editor.
       
        name = '%d' % self.totalNumberOfEditors
        pane = self.pb.add(name)
        panes = self.pb.panes()
        minSize = float(1.0/float(len(panes)))
        
        #@    << create label and text widgets >>
        #@+node:ekr.20060528110922:<< create label and text widgets >>
        f = Tk.Frame(pane)
        f.pack(side='top',expand=1,fill='both')
        
        w = self.createTextWidget(self.frame,f,name=name,p=p)
        
        w.delete('1.0','end')
        w.insert('end',p.bodyString())
        w.see('1.0')
        #self.setFontFromConfig(w=w)
        #self.setColorFromConfig(w=w)
        self.createBindings(w=w)
        c.k.completeAllBindingsForWidget(w)
        
        self.recolorWidget(w)
        #@-node:ekr.20060528110922:<< create label and text widgets >>
        #@nl
        self.editorWidgets[name] = w
    
        for pane in panes:
            self.pb.configurepane(pane,size=minSize)
        
        self.pb.updatelayout()
        self.bodyCtrl = self.frame.bodyCtrl = w
        self.selectEditor(w)
        self.updateEditors()
        c.bodyWantsFocusNow()
    #@-node:ekr.20060528100747.1:addEditor
    #@+node:ekr.20060606090542:setEditorColors
    def setEditorColors (self,bg,fg):
        
        c = self.c ; d = self.editorWidgets
    
        for key in d.keys():
            w2 = d.get(key)
            # g.trace(id(w2),bg,fg)
            try:
                w2.configure(bg=bg,fg=fg)
            except Exception:
                g.es_exception()
                pass
    #@-node:ekr.20060606090542:setEditorColors
    #@+node:ekr.20060528170438:cycleEditorFocus
    def cycleEditorFocus (self,event=None):
        
        '''Cycle keyboard focus between the body text editors.'''
        
        c = self.c ; d = self.editorWidgets ; w = self.bodyCtrl
        values = d.values()
        if len(values) > 1:
            i = values.index(w) + 1
            if i == len(values): i = 0
            w2 = d.values()[i]
            assert(w!=w2)
            self.selectEditor(w2)
            self.bodyCtrl = self.frame.bodyCtrl = w2
            # print '***',g.app.gui.widget_name(w2),id(w2)
    
        return 'break'
    #@-node:ekr.20060528170438:cycleEditorFocus
    #@+node:ekr.20060528113806:deleteEditor
    def deleteEditor (self,event=None):
        
        '''Delete the presently selected body text editor.'''
        
        w = self.bodyCtrl ; d = self.editorWidgets
        
        if len(d.keys()) == 1: return
        
        name = w.leo_name
        
        del d [name] 
        self.pb.delete(name)
        panes = self.pb.panes()
        minSize = float(1.0/float(len(panes)))
        
        for pane in panes:
            self.pb.configurepane(pane,size=minSize)
            
        # Select another editor.
        w = d.values()[0]
        self.bodyCtrl = self.frame.bodyCtrl = w
        self.numberOfEditors -= 1
        self.selectEditor(w)
    #@-node:ekr.20060528113806:deleteEditor
    #@+node:ekr.20061017082211:onClick
    def onClick (self,event): #disabled in masterclick
        
        c = self.c ; k = c.k
        w = event and event.widget
        wname = c.widget_name(w)
        
        if wname.startswith('body'):
            # A hack to support middle-button pastes: remember the previous selection.
            
            #agp x, y = event.x, event.y
            #agp k.previousSelection = g.app.gui.getSelectionRange(w)
            #agp i = w.index('@%s,%s' % (x,y))
            # g.trace(x,y,i)
            #agp g.app.gui.setTextSelection(w,i,i,insert=i)
            #agp c.editCommands.setMoveCol(i)
            print "onclick",event
            c.frame.updateStatusLine()
            self.selectEditor(w)
        else:
            g.trace('can not happen')
    #@nonl
    #@-node:ekr.20061017082211:onClick
    #@+node:AGP.20231103121616:OnLRelease
    def OnLRelease (self,event):
        self.c.frame.updateStatusLine()
        
    #@nonl
    #@-node:AGP.20231103121616:OnLRelease
    #@+node:ekr.20061017083312:selectEditor
    def selectEditor(self,w):
        
        c = self.c ; d = self.editorWidgets
        trace = False
        if trace: g.trace(g.app.gui.widget_name(w),id(w),g.callers())
        if w.leo_p is None:
            if trace: g.trace('no w.leo_p') 
            return 'break'
        # Inactivate the previously active editor.
        # Don't capture ivars here! selectMainEditor keeps them up-to-date.
        for key in d.keys():
            w2 = d.get(key)
            if w2 != w and w2.leo_active:
                w2.leo_active = False
                self.unselectLabel(w2)
                w2.leo_scrollBarSpot = w2.yview()
                w2.leo_insertSpot = g.app.gui.getInsertPoint(w2)
                w2.leo_selection = g.app.gui.getSelectionRange(w2)
                # g.trace('inactive:',id(w2),'scroll',w2.leo_scrollBarSpot,'ins',w2.leo_insertSpot)
                break
        else:
            if trace: g.trace('no active editor!')
        
        # Careful, leo_p may not exist.
        if not c.positionExists(w.leo_p):
            if trace: g.trace('does not exist',w.leo_name)
            for p2 in c.allNodes_iter():
                if p2.v == w.leo_v:
                    w.leo_p = p2.copy()
                    break
            else:
                 # This *can* happen when selecting a deleted node.
                w.leo_p = c.currentPosition()
                if trace: g.trace('previously deleted node')
                return 'break'
    
        self.frame.bodyCtrl = self.bodyCtrl = w # Must change both ivars!
        w.leo_active = True
        c.selectPosition(w.leo_p,updateBeadList=True) # Calls selectMainEditor.
        c.recolor_now()
        #@    << restore the selection, insertion point and the scrollbar >>
        #@+node:ekr.20061017083312.1:<< restore the selection, insertion point and the scrollbar >>
        # g.trace('active:',id(w),'scroll',w.leo_scrollBarSpot,'ins',w.leo_insertSpot)
        
        if w.leo_insertSpot:
            g.app.gui.setInsertPoint(w,w.leo_insertSpot)
            w.see(w.leo_insertSpot)
        else:
            g.app.gui.setInsertPoint(w,'1.0')
            
        if w.leo_scrollBarSpot:
            first,last = w.leo_scrollBarSpot
            w.yview('moveto',first)
        
        if w.leo_selection:
            try:
                start,end = w.leo_selection
                g.app.gui.setSelectionRange(w,start,end)
            except Exception:
                pass
        #@-node:ekr.20061017083312.1:<< restore the selection, insertion point and the scrollbar >>
        #@nl
        c.bodyWantsFocusNow()
        return 'break'
    #@nonl
    #@-node:ekr.20061017083312:selectEditor
    #@+node:ekr.20060528132829:selectMainEditor
    def selectMainEditor (self,p):
        
        
        '''Called from tree.select to select the present body editor.'''
    
        c = self.c ; p = c.currentPosition() ; w = self.bodyCtrl
    
        # Don't inject ivars if there is only one editor.
        if w.leo_p is not None:
            # Keep w's ivars up-to-date.
            w.leo_p = p.copy()
            w.leo_v = p.v
            w.leo_label_s = p.headString()
            self.selectLabel(w)
            # g.trace(w.leo_name,p.headString())
    #@-node:ekr.20060528132829:selectMainEditor
    #@+node:ekr.20060528131618:updateEditors
    def updateEditors (self):
        
        c = self.c ; p = c.currentPosition()
        d = self.editorWidgets
        if len(d.keys()) < 2: return # There is only the main widget.
    
        for key in d.keys():
            w = d.get(key)
            v = w.leo_v
            if v and v == p.v and w != self.bodyCtrl:
                w.delete('1.0','end')
                w.insert('end',p.bodyString())
                # g.trace('update',w,v)
                self.recolorWidget(w)
        c.frame.bodyWantsFocus()
    #@-node:ekr.20060528131618:updateEditors
    #@-node:ekr.20060528100747:Editors
    #@+node:ekr.20031218072017.1329:onBodyChanged (tkBody)
    # This is the only key handler for the body pane.
    def onBodyChanged (self,undoType,oldSel=None,oldText=None,oldYview=None):
        
        '''Update Leo after the body has been changed.'''
        
        body = self ; c = self.c ; bodyCtrl = body.bodyCtrl
        trace = self.trace_onBodyChanged
        p = c.currentPosition()
        insert = bodyCtrl.index('insert')
        ch = g.choose(insert=='1.0','',bodyCtrl.get('insert-1c'))
        ch = g.toUnicode(ch,g.app.tkEncoding)
        newText = g.app.gui.getAllText(bodyCtrl) # Note: getAllText converts to unicode.
        # g.trace('newText',repr(newText))
        newSel = g.app.gui.getTextSelection(bodyCtrl)
        if oldText is None: oldText = p.bodyString()
        changed = oldText != newText
        if trace:
            g.trace(repr(ch),'changed:',changed)
            g.trace('newText:',repr(newText))
        if changed:
            c.undoer.setUndoTypingParams(p,undoType,
                oldText=oldText,newText=newText,oldSel=oldSel,newSel=newSel,oldYview=oldYview)
            p.v.setTnodeText(newText)
            p.v.t.insertSpot = body.getInsertionPoint()
            #@        << recolor the body >>
            #@+node:ekr.20051026083733.6:<< recolor the body >>
            body.colorizer.interrupt()
            c.frame.scanForTabWidth(p)
            body.recolor_now(p,incremental=not self.forceFullRecolorFlag)
            self.forceFullRecolorFlag = False
            #@-node:ekr.20051026083733.6:<< recolor the body >>
            #@nl
            if not c.changed: c.setChanged(True)
            self.updateEditors()
            #@        << redraw the screen if necessary >>
            #@+node:ekr.20051026083733.7:<< redraw the screen if necessary >>
            c.beginUpdate()
            try:
                redraw_flag = False
                # Update dirty bits.
                # p.setDirty() sets all cloned and @file dirty bits.
                if not p.isDirty() and p.setDirty():
                    redraw_flag = True
                    
                # Update icons. p.v.iconVal may not exist during unit tests.
                val = p.computeIcon()
                if not hasattr(p.v,"iconVal") or val != p.v.iconVal:
                    p.v.iconVal = val
                    redraw_flag = True
            finally:
                c.endUpdate(redraw_flag)
            #@-node:ekr.20051026083733.7:<< redraw the screen if necessary >>
            #@nl
    #@-node:ekr.20031218072017.1329:onBodyChanged (tkBody)
    #@+node:ekr.20031218072017.4003:Focus (tkBody)
    def hasFocus (self):
        
        return self.bodyCtrl == self.frame.top.focus_displayof()
        
    def setFocus (self):
        
        self.c.widgetWantsFocus(self.bodyCtrl)
    #@-node:ekr.20031218072017.4003:Focus (tkBody)
    #@+node:ekr.20031218072017.3999:forceRecolor
    def forceFullRecolor (self):
        
        self.forceFullRecolorFlag = True
    #@-node:ekr.20031218072017.3999:forceRecolor
    #@+node:ekr.20031218072017.4000:Tk bindings (tkBbody)
    #@+at
    # I could have used this to redirect all calls from the body class and the 
    # bodyCtrl to Tk. OTOH:
    # 
    # 1. Most of the wrappers do more than the old Tk routines now and
    # 2. The wrapper names are more discriptive than the Tk names.
    # 
    # Still, using the Tk names would have had its own appeal.  If I had 
    # prefixed the tk routine with tk_ the __getatt__ routine could have 
    # stripped it off!
    #@-at
    #@@c
    
    if 0: # This works.
        def __getattr__(self,attr):
            return getattr(self.bodyCtrl,attr)
            
    if 0: # This would work if all tk wrapper routines were prefixed with tk_
        def __getattr__(self,attr):
            if attr[0:2] == "tk_":
                return getattr(self.bodyCtrl,attr[3:])
    #@+node:ekr.20031218072017.4001:Bounding box (Tk spelling)
    def bbox(self,index):
    
        return self.bodyCtrl.bbox(index)
    #@-node:ekr.20031218072017.4001:Bounding box (Tk spelling)
    #@+node:ekr.20031218072017.4002:Color tags (Tk spelling)
    # Could have been replaced by the __getattr__ routine above...
    # 12/19/03: no: that would cause more problems.
    
    def tag_add (self,tagName,index1,index2):
        self.bodyCtrl.tag_add(tagName,index1,index2)
    
    def tag_bind (self,tagName,event,callback):
        self.bodyCtrl.tag_bind(tagName,event,callback)
    
    def tag_configure (self,colorName,**keys):
        self.bodyCtrl.tag_configure(colorName,keys)
    
    def tag_delete(self,tagName):
        self.bodyCtrl.tag_delete(tagName)
        
    def tag_names(self,*args): # New in Leo 4.4.1.
        return self.bodyCtrl.tag_names(*args)
    
    def tag_remove (self,tagName,index1,index2):
        return self.bodyCtrl.tag_remove(tagName,index1,index2)
    #@-node:ekr.20031218072017.4002:Color tags (Tk spelling)
    #@+node:ekr.20031218072017.2184:Configuration (Tk spelling)
    def cget(self,*args,**keys):
        
        val = self.bodyCtrl.cget(*args,**keys)
        
        if g.app.trace:
            g.trace(val,args,keys)
    
        return val
        
    def configure (self,*args,**keys):
        
        # g.trace(args,keys)
        print "configure body"
        return self.bodyCtrl.configure(*args,**keys)
    #@-node:ekr.20031218072017.2184:Configuration (Tk spelling)
    #@+node:ekr.20031218072017.4004:Height & width
    def getBodyPaneHeight (self):
        
        return self.bodyCtrl.winfo_height()
    
    def getBodyPaneWidth (self):
        
        return self.bodyCtrl.winfo_width()
    #@-node:ekr.20031218072017.4004:Height & width
    #@+node:ekr.20031218072017.4005:Idle time...
    def scheduleIdleTimeRoutine (self,function,*args,**keys):
    
        self.bodyCtrl.after_idle(function,*args,**keys)
    #@-node:ekr.20031218072017.4005:Idle time...
    #@+node:ekr.20031218072017.4006:Indices (leoTkinterBody)
    #@+node:ekr.20031218072017.4007:adjustIndex
    def adjustIndex (self,index,offset):
        
        t = self.bodyCtrl
        return t.index("%s + %dc" % (t.index(index),offset))
    #@-node:ekr.20031218072017.4007:adjustIndex
    #@+node:ekr.20031218072017.4008:compareIndices
    def compareIndices(self,i,rel,j):
    
        return self.bodyCtrl.compare(i,rel,j)
    #@-node:ekr.20031218072017.4008:compareIndices
    #@+node:ekr.20031218072017.4009:convertRowColumnToIndex
    def convertRowColumnToIndex (self,row,column):
        
        return self.bodyCtrl.index("%s.%s" % (row,column))
    #@-node:ekr.20031218072017.4009:convertRowColumnToIndex
    #@+node:ekr.20031218072017.4010:convertIndexToRowColumn
    def convertIndexToRowColumn (self,index):
        
        index = self.bodyCtrl.index(index)
        start, end = string.split(index,'.')
        return int(start),int(end)
    #@-node:ekr.20031218072017.4010:convertIndexToRowColumn
    #@+node:ekr.20031218072017.4011:getImageIndex
    def getImageIndex (self,image):
        
        return self.bodyCtrl.index(image)
    #@-node:ekr.20031218072017.4011:getImageIndex
    #@+node:ekr.20031218072017.4012:tkIndex (internal use only)
    def tkIndex(self,index):
        
        """Returns the canonicalized Tk index."""
        
        if index == "start": index = "1.0"
        
        return self.bodyCtrl.index(index)
    #@-node:ekr.20031218072017.4012:tkIndex (internal use only)
    #@-node:ekr.20031218072017.4006:Indices (leoTkinterBody)
    #@+node:ekr.20031218072017.4013:Insert point
    #@+node:ekr.20050710102922:get/setPythonInsertionPoint
    def getPythonInsertionPoint (self,t=None,s=None):
        
        b = self
        if t is None: t = self.bodyCtrl
        if s is None: s = t.get('1.0','end')
        i = t.index("insert")
        row,col = b.convertIndexToRowColumn(i)
        
        return g.convertRowColToPythonIndex(s,row-1,col)
        
    def setPythonInsertionPoint (self,i,t=None,s=None):
        
        if t is None: t = self.bodyCtrl
        if s is None: s = t.get('1.0','end')
        row,col = g.convertPythonIndexToRowCol(s,i)
        t.mark_set( 'insert','%d.%d' % (row+1,col))
    #@-node:ekr.20050710102922:get/setPythonInsertionPoint
    #@+node:ekr.20031218072017.495:getInsertionPoint & getBeforeInsertionPoint
    def getBeforeInsertionPoint (self):
        
        return self.bodyCtrl.index("insert-1c")
    
    def getInsertionPoint (self):
        
        return self.bodyCtrl.index("insert")
    #@-node:ekr.20031218072017.495:getInsertionPoint & getBeforeInsertionPoint
    #@+node:ekr.20031218072017.4014:getCharAtInsertPoint & getCharBeforeInsertPoint
    def getCharAtInsertPoint (self):
        
        s = self.bodyCtrl.get("insert")
        return g.toUnicode(s,g.app.tkEncoding)
    
    def getCharBeforeInsertPoint (self):
    
        s = self.bodyCtrl.get("insert -1c")
        return g.toUnicode(s,g.app.tkEncoding)
    #@-node:ekr.20031218072017.4014:getCharAtInsertPoint & getCharBeforeInsertPoint
    #@+node:ekr.20031218072017.4015:makeInsertPointVisible
    def makeInsertPointVisible (self):
        
        self.bodyCtrl.see("insert") # -5l")
    #@-node:ekr.20031218072017.4015:makeInsertPointVisible
    #@+node:ekr.20031218072017.4016:setInsertionPointTo...
    def setInsertionPoint (self,index):
        self.bodyCtrl.mark_set("insert",index)
    
    def setInsertionPointToEnd (self):
        self.bodyCtrl.mark_set("insert","end")
        
    def setInsertPointToStartOfLine (self,lineNumber): # zero-based line number
        self.bodyCtrl.mark_set("insert",str(1+lineNumber)+".0 linestart")
    #@-node:ekr.20031218072017.4016:setInsertionPointTo...
    #@-node:ekr.20031218072017.4013:Insert point
    #@+node:ekr.20031218072017.4017:Menus
    def bind (self,*args,**keys):
        
        return self.bodyCtrl.bind(*args,**keys)
    #@-node:ekr.20031218072017.4017:Menus
    #@+node:ekr.20031218072017.4018:Selection
    #@+node:ekr.20031218072017.4019:deleteTextSelection
    def deleteTextSelection (self):
        
        t = self.bodyCtrl
        sel = t.tag_ranges("sel")
        if len(sel) == 2:
            start,end = sel
            if t.compare(start,"!=",end):
                t.delete(start,end)
    #@-node:ekr.20031218072017.4019:deleteTextSelection
    #@+node:ekr.20031218072017.4020:getSelectedText
    def getSelectedText (self):
        
        """Return the selected text of the body frame, converted to unicode."""
    
        start, end = self.getTextSelection()
        if start and end and start != end:
            s = self.bodyCtrl.get(start,end)
            if s is None:
                return u""
            else:
                return g.toUnicode(s,g.app.tkEncoding)
        else:
            return u'' # Bug fix: 1/8/06
    #@-node:ekr.20031218072017.4020:getSelectedText
    #@+node:ekr.20031218072017.4021:getTextSelection
    def getTextSelection (self,sort=True):
        
        """Return a tuple representing the selected range of body text.
        
        Return a tuple giving the insertion point if no range of text is selected."""
    
        w = self.bodyCtrl
        
        sel = w.tag_ranges("sel")
    
        if len(sel) == 2:
            # New in 4.4a5: match behavior of g.app.gui.getTextSelection.
            if sort:
                i,j = sel
                if w.compare(i, ">", j):
                    i,j = j,i
            return sel
        else:
            # Return the insertion point if there is no selected text.
            insert = w.index("insert")
            return insert,insert
    #@-node:ekr.20031218072017.4021:getTextSelection
    #@+node:ekr.20050710104804:getPythonTextSelection
    def getPythonTextSelection (self):
        
        """Return a tuple representing the selected range of body text.
        
        Return a tuple giving the insertion point if no range of text is selected."""
    
        b = self ; t = self.bodyCtrl
        sel = t.tag_ranges("sel")
    
        if len(sel) == 2:
            s = t.get('1.0','end')
            i,j = sel
            row,col = b.convertIndexToRowColumn(i)
            i1 = g.convertRowColToPythonIndex(s,row-1,col)
            row,col = b.convertIndexToRowColumn(j)
            i2 = g.convertRowColToPythonIndex(s,row-1,col)
            return i1,i2
        else:
            # Return the insertion point if there is no selected text.
            i = self.getPythonTextSelection()
            return i,i
    #@-node:ekr.20050710104804:getPythonTextSelection
    #@+node:ekr.20050710104804.1:setPythonTextSelection
    def setPythonTextSelection(self,i,j):
    
        t = self.bodyCtrl
        s = t.get('1.0','end')
        row,col = g.convertPythonIndexToRowCol(s,i)
        i1 = '%d.%d' % (row+1,col)
        row,col = g.convertPythonIndexToRowCol(s,j)
        i2 = '%d.%d' % (row+1,col)
        g.app.gui.setTextSelection(self.bodyCtrl,i1,i2)
    #@-node:ekr.20050710104804.1:setPythonTextSelection
    #@+node:ekr.20031218072017.4022:hasTextSelection
    def hasTextSelection (self):
    
        sel = self.bodyCtrl.tag_ranges("sel")
        return sel and len(sel) == 2
    #@-node:ekr.20031218072017.4022:hasTextSelection
    #@+node:ekr.20031218072017.4023:selectAllText
    def selectAllText (self,event=None):
        
        '''Select all text in the presently selected pane.'''
        
        c = self.c ; k = c.k
    
        try:
            w = c.get_focus() ; wname = c.widget_name(w)
            n = 0
            if wname.startswith('head'):
                s = w.get('1.0','end')
                while s.endswith('\n') or s.endswith('\r'):
                    s = s[:-1] ; n += 1
                g.app.gui.setTextSelection(w,'1.0','end - %dc' % (n))
            elif wname.startswith('mini'):
                i,j = k.getEditableTextRange()
                g.app.gui.setTextSelection(w,i,j)
            else:
                g.app.gui.setTextSelection(w,'1.0','end - %dc' % (n))
        except:
            # g.es_exception()
            pass
    #@-node:ekr.20031218072017.4023:selectAllText
    #@+node:ekr.20031218072017.4024:setTextSelection (tkinterBody)
    def setTextSelection (self,i,j=None,insert='sel.end'):
        
        # Allow the user to pass either a 2-tuple or two separate args.
        if i is None:
            i,j = "1.0","1.0"
        elif len(i) == 2:
            i,j = i
    
        g.app.gui.setTextSelection(self.bodyCtrl,i,j,insert)
    #@-node:ekr.20031218072017.4024:setTextSelection (tkinterBody)
    #@-node:ekr.20031218072017.4018:Selection
    #@+node:ekr.20031218072017.4025:Text
    #@+node:ekr.20031218072017.4026:delete...
    def deleteAllText(self):
        self.bodyCtrl.delete("1.0","end")
    
    def deleteCharacter (self,index):
        t = self.bodyCtrl
        t.delete(t.index(index))
        
    def deleteLastChar (self):
        self.bodyCtrl.delete("end-1c")
        
    def deleteLine (self,lineNumber): # zero based line number.
        self.bodyCtrl.delete(str(1+lineNumber)+".0","end")
        
    def deleteLines (self,line1,numberOfLines): # zero based line numbers.
        self.bodyCtrl.delete(str(1+line1)+".0",str(1+line1+numberOfLines-1)+".0 lineend")
        
    def deleteRange (self,index1,index2):
        t = self.bodyCtrl
        t.delete(t.index(index1),t.index(index2))
    #@-node:ekr.20031218072017.4026:delete...
    #@+node:ekr.20031218072017.4027:get...
    #@+node:ekr.20031218072017.4028:tkBody.getAllText
    def getAllText (self):
        
        """Return all the body text, converted to unicode."""
        
        s = self.bodyCtrl.get("1.0","end-1c") # New in 4.4.1: use end-1c.
    
        if s is None:
            return u""
        else:
            return g.toUnicode(s,g.app.tkEncoding)
    #@-node:ekr.20031218072017.4028:tkBody.getAllText
    #@+node:ekr.20031218072017.4029:getCharAtIndex
    def getCharAtIndex (self,index):
        
        """Return all the body text, converted to unicode."""
        
        s = self.bodyCtrl.get(index)
        if s is None:
            return u""
        else:
            return g.toUnicode(s,g.app.tkEncoding)
    #@-node:ekr.20031218072017.4029:getCharAtIndex
    #@+node:ekr.20031218072017.4030:getInsertLines
    def getInsertLines (self):
        
        """Return before,after where:
            
        before is all the lines before the line containing the insert point.
        sel is the line containing the insert point.
        after is all the lines after the line containing the insert point.
        
        All lines end in a newline, except possibly the last line."""
        
        t = self.bodyCtrl
    
        before = t.get("1.0","insert linestart")
        ins    = t.get("insert linestart","insert lineend + 1c")
        after  = t.get("insert lineend + 1c","end")
    
        before = g.toUnicode(before,g.app.tkEncoding)
        ins    = g.toUnicode(ins,   g.app.tkEncoding)
        after  = g.toUnicode(after ,g.app.tkEncoding)
    
        return before,ins,after
    #@-node:ekr.20031218072017.4030:getInsertLines
    #@+node:ekr.20031218072017.4031:getSelectionAreas
    def getSelectionAreas (self):
        
        """Return before,sel,after where:
            
        before is the text before the selected text
        (or the text before the insert point if no selection)
        sel is the selected text (or "" if no selection)
        after is the text after the selected text
        (or the text after the insert point if no selection)"""
    
        t = self.bodyCtrl
        
        sel_index = t.getTextSelection()
        if len(sel_index) == 2:
            i,j = sel_index
            sel = t.get(i,j)
        else:
            i = j = t.index("insert")
            sel = ""
    
        before = t.get("1.0",i)
        after  = t.get(j,"end")
        
        before = g.toUnicode(before,g.app.tkEncoding)
        sel    = g.toUnicode(sel,   g.app.tkEncoding)
        after  = g.toUnicode(after ,g.app.tkEncoding)
        return before,sel,after
    #@-node:ekr.20031218072017.4031:getSelectionAreas
    #@+node:ekr.20031218072017.2377:getSelectionLines (tkBody)
    def getSelectionLines (self):
        
        """Return before,sel,after where:
            
        before is the all lines before the selected text
        (or the text before the insert point if no selection)
        sel is the selected text (or "" if no selection)
        after is all lines after the selected text
        (or the text after the insert point if no selection)"""
        
        # At present, called only by c.getBodyLines.
    
        t = self.bodyCtrl
        sel_index = t.tag_ranges("sel") 
        if len(sel_index) != 2:
            if 1: # Choose the insert line.
                index = t.index("insert")
                sel_index = index,index
            else:
                return "","","" # Choose everything.
    
        i,j = sel_index
        
        i = t.index(str(i) + "linestart")   #agp
        j = t.index(str(j) + "lineend") # 10/24/03: -1c  # 11/4/03: no -1c.#agp
        before = g.toUnicode(t.get("1.0",i),g.app.tkEncoding)
        sel    = g.toUnicode(t.get(i,j),    g.app.tkEncoding)
        after  = g.toUnicode(t.get(j,"end-1c"),g.app.tkEncoding)
        
        # g.trace(i,j)
        return before,sel,after
    #@-node:ekr.20031218072017.2377:getSelectionLines (tkBody)
    #@+node:ekr.20031218072017.4032:getTextRange
    def getTextRange (self,index1,index2):
        
        t = self.bodyCtrl
        return t.get(t.index(index1),t.index(index2))
    #@-node:ekr.20031218072017.4032:getTextRange
    #@-node:ekr.20031218072017.4027:get...
    #@+node:ekr.20031218072017.4033:Insert...
    #@+node:ekr.20031218072017.4034:insertAtInsertPoint
    def insertAtInsertPoint (self,s):
        
        self.bodyCtrl.insert("insert",s)
    #@-node:ekr.20031218072017.4034:insertAtInsertPoint
    #@+node:ekr.20031218072017.4035:insertAtEnd
    def insertAtEnd (self,s):
        
        self.bodyCtrl.insert("end",s)
    #@-node:ekr.20031218072017.4035:insertAtEnd
    #@+node:ekr.20031218072017.4036:insertAtStartOfLine
    def insertAtStartOfLine (self,lineNumber,s):
        
        self.bodyCtrl.insert(str(1+lineNumber)+".0",s)
    #@-node:ekr.20031218072017.4036:insertAtStartOfLine
    #@-node:ekr.20031218072017.4033:Insert...
    #@+node:ekr.20031218072017.4037:setSelectionAreas (tkinterBody)
    def setSelectionAreas (self,before,sel,after):
        
        """Replace the body text by before + sel + after and
        set the selection so that the sel text is selected."""
    
        t = self.bodyCtrl ; gui = g.app.gui
        t.delete("1.0","end")
    
        if before: t.insert("1.0",before)
        sel_start = t.index("end-1c") # 10/24/03: -1c
    
        if sel: t.insert("end",sel)
        sel_end = t.index("end")
    
        if after:
            # A horrible Tk kludge.  Remove a trailing newline so we don't keep extending the text.
            if after[-1] == '\n':
                after = after[:-1]
            t.insert("end",after)
    
        gui.setTextSelection(t,sel_start,sel_end)
        # g.trace(sel_start,sel_end)
        
        return t.index(sel_start), t.index(sel_end)
    #@-node:ekr.20031218072017.4037:setSelectionAreas (tkinterBody)
    #@-node:ekr.20031218072017.4025:Text
    #@+node:ekr.20031218072017.4038:Visibility & scrolling
    def makeIndexVisible (self,index):
        
        self.bodyCtrl.see(index)
        
    def setFirstVisibleIndex (self,index):
        
        self.bodyCtrl.yview("moveto",index)
        
    def getYScrollPosition (self):
        
        return self.bodyCtrl.yview()
        
    def setYScrollPosition (self,scrollPosition):
    
        if len(scrollPosition) == 2:
            first,last = scrollPosition
        else:
            first = scrollPosition
        self.bodyCtrl.yview("moveto",first)
        
    def scrollUp (self):
        
        self.bodyCtrl.yview("scroll",-1,"units")
        
    def scrollDown (self):
    
        self.bodyCtrl.yview("scroll",1,"units")
    #@-node:ekr.20031218072017.4038:Visibility & scrolling
    #@-node:ekr.20031218072017.4000:Tk bindings (tkBbody)
    #@-others
#@-node:ekr.20031218072017.3996:class leoTkinterBody
#@+node:ekr.20031218072017.4039:class leoTkinterLog
class leoTkinterLog (leoFrame.leoLog):
    
    """A class that represents the log pane of a Tkinter window."""

    #@    @+others
    #@+node:ekr.20031218072017.4040:__init__
    def __init__ (self,frame,parentFrame):
        
        # g.trace("leoTkinterLog")
        
        self.c = c = frame.c # Also set in the base constructor, but we need it here.
        
        self.colorTags = []
            # The list of color names used as tags in present tab.
            # This gest switched by selectTab.
    
        self.wrap = None #g.choose(c.config.getBool('log_pane_wraps'),"word","none")
        
        # New in 4.4a2: The log pane is a Pmw.Notebook...
    
        self.nb = None      # The Pmw.Notebook that holds all the tabs.
        self.colorTagsDict = {} # Keys are page names.  Values are saved colorTags lists.
        self.frameDict = {}  # Keys are page names. Values are Tk.Frames.
        self.logNumber = 0 # To create unique name fields for Tk.Text widgets.
        self.menu = None # A menu that pops up on right clicks in the hull or in tabs.
        self.textDict = {}  # Keys are page names. Values are Tk.Text widgets.
        self.newTabCount = 0 # Number of new tabs created.
        
        # Official status variables.  Can be used by client code.
        self.tabName = None # The name of the active tab.
        self.logCtrl = None # Same as self.textDict.get(self.tabName)
        self.tabFrame = None # Same as self.frameDict.get(self.tabName)
        
        self.dimmed = False
        
        # Call the base class constructor and calls createControl.
        leoFrame.leoLog.__init__(self,frame,parentFrame)
        
    #@nonl
    #@-node:ekr.20031218072017.4040:__init__
    #@+node:AGP.20231024191306:createControl
    def createControl (self,parentFrame):
    
        c = self.c
        
        self.logCtrl = self.createTextWidget(parentFrame)
        
        
        return self.logCtrl
    #@-node:AGP.20231024191306:createControl
    #@+node:ekr.20031218072017.4042:xcreateControl
    def xcreateControl (self,parentFrame):
    
        c = self.c
    
        self.nb = Pmw.NoteBook(parentFrame,
            borderwidth = 1, pagemargin = 0,
            raisecommand = self.raiseTab,
            lowercommand = self.lowerTab,
            arrownavigation = 0,
        )
        
        
        menu = self.makeTabMenu(tabName=None)
    
        def hullMenuCallback(event):
            g.trace()
            return self.onRightClick(event,menu)
    
        self.nb.bind('<Button-3>',hullMenuCallback)
    
        self.nb.pack(fill='both',expand=1)
        self.selectTab('Log') # create the tab and make it the active tab.
        return self.logCtrl
    #@-node:ekr.20031218072017.4042:xcreateControl
    #@+node:ekr.20051016103459:createTextWidget
    def createTextWidget (self,parentFrame):
        
        self.logNumber += 1
        
        self.logCtrl = log = Tk.Text(parentFrame,name="logtext",setgrid=0,wrap=self.wrap,bd=2,relief="flat")#,state='disabled')#bg="white")
        
        #print str(log),log['font']
        
        self.dim = 0.6
        log.bind('<FocusIn>',self.focus_in)
        log.bind('<FocusOut>',self.focus_out)
        log.bind("<MouseWheel>",self.frame.TopMouseWheel)
        logBar = g.app.gui.SCROLLBAR(parentFrame,1)#    Tk.Scrollbar(parentFrame,name="logBar")
    
        log['yscrollcommand'] = logBar.set
        logBar.command = log.yview
        
        logBar.pack(side="right", fill="y")
        # rr 8/14/02 added horizontal elevator 
        if self.wrap == "none": 
            logXBar = g.app.gui.SCROLLBAR(parentFrame,0)#Tk.Scrollbar(parentFrame,name='logXBar',orient="horizontal") 
            log['xscrollcommand'] = logXBar.set 
            logXBar.command = log.xview 
            logXBar.pack(side="bottom", fill="x")
        
        log.pack(expand=1, fill="both")
        
        
        log['state'] = 'disabled'
        self.full_fg = log['fg']
        
        log.tag_config("red", foreground=g.theme['error'] )
        log.tag_config("blue", foreground=g.theme['info'] )
        #print "set tags",g.theme['error'],g.theme['info']
        
        self.colorTags.append("red")
        self.colorTags.append("blue")
        
        self.dim_text()
        
        return log
    #@-node:ekr.20051016103459:createTextWidget
    #@+node:AGP.20231125102317:focus_in()
    def focus_in(self,event):
        self.undim_text()
        
    #@nonl
    #@-node:AGP.20231125102317:focus_in()
    #@+node:AGP.20231125102317.1:focus_out()
    def focus_out(self,event):
        self.dim_text()
        
    #@-node:AGP.20231125102317.1:focus_out()
    #@+node:AGP.20231125104049:dim_text()
    def dim_text(self):
        log = self.logCtrl
        log.config(fg = g.color_mul(self.dim,self.full_fg) )
        for color in self.colorTags:
            c = log.tag_cget(color,"foreground")
            log.tag_config(color, foreground=g.color_mul(self.dim,c) )
            
        self.dimmed = True
    #@nonl
    #@-node:AGP.20231125104049:dim_text()
    #@+node:AGP.20231125104049.1:undim_text()
    def undim_text(self):
        log = self.logCtrl
        log.config(fg = self.full_fg )
        for color in self.colorTags:
            c = log.tag_cget(color,"foreground")
            log.tag_config(color, foreground=g.color_mul(1.0/self.dim,c) )
            
        self.dimmed = False
    #@nonl
    #@-node:AGP.20231125104049.1:undim_text()
    #@+node:ekr.20051019134106.1:makeTabMenu
    def makeTabMenu (self,tabName=None):
    
        '''Create a tab popup menu.'''
    
        c = self.c
        hull = self.nb.component('hull') # A Tk.Canvas.
        
        menu = Tk.Menu(hull,tearoff=0)
        menu.add_command(label='New Tab',command=self.newTabFromMenu)
        
        if tabName:
            # Important: tabName is the name when the tab is created.
            # It is not affected by renaming, so we don't have to keep
            # track of the correspondence between this name and what is in the label.
            def deleteTabCallback():
                return self.deleteTab(tabName)
                
            label = g.choose(
                tabName in ('Find','Spell'),'Hide This Tab','Delete This Tab')
            menu.add_command(label=label,command=deleteTabCallback)
     
            def renameTabCallback():
                return self.renameTabFromMenu(tabName)
    
            menu.add_command(label='Rename This Tab',command=renameTabCallback)
    
        return menu
    #@-node:ekr.20051019134106.1:makeTabMenu
    #@+node:ekr.20051016095907.1:Config & get/saveState
    #@+node:ekr.20031218072017.4041:tkLog.configureBorder & configureFont
    def configureBorder(self,border):
        
        self.logCtrl.configure(bd=border)
        
    def configureFont(self,font):
        print 'cfgfony'
        self.logCtrl.configure(font=font)
    #@-node:ekr.20031218072017.4041:tkLog.configureBorder & configureFont
    #@+node:ekr.20031218072017.4043:tkLog.getFontConfig
    def getFontConfig (self):
    
        font = g.log['font']
        # g.trace(font)
        return font
    #@-node:ekr.20031218072017.4043:tkLog.getFontConfig
    #@+node:ekr.20041222043017:tkLog.restoreAllState
    def restoreAllState (self,d):
        
        '''Restore the log from a dict created by saveAllState.'''
        
        logCtrl = self.logCtrl
        
        logCtrl['state']='normal'
        
        #Restore the text.
        text = d.get('text')
        logCtrl.insert('end',text)
    
        # Restore all colors.
        colors = d.get('colors')
        for color in colors.keys():
            if color not in self.colorTags:
                self.colorTags.append(color)
                logCtrl.tag_config(color,foreground=color)
            items = list(colors.get(color))
            while items:
                start,stop = items[0],items[1]
                items = items[2:]
                logCtrl.tag_add(color,start,stop)
                
        logCtrl['state']='disabled'
    #@-node:ekr.20041222043017:tkLog.restoreAllState
    #@+node:ekr.20041222043017.1:tkLog.saveAllState
    def saveAllState (self):
        
        '''Return a dict containing all data needed to recreate the log in another widget.'''
        
        logCtrl = self.logCtrl ; colors = {}
    
        # Save the text
        text = logCtrl.get('1.0','end')
    
        # Save color tags.
        tag_names = logCtrl.tag_names()
        for tag in tag_names:
            if tag in self.colorTags:
                colors[tag] = logCtrl.tag_ranges(tag)
                
        d = {'text':text,'colors': colors}
        # g.trace('\n',g.dictToString(d))
        return d
    #@-node:ekr.20041222043017.1:tkLog.saveAllState
    #@+node:ekr.20041217135735.2:tkLog.setColorFromConfig
    def setColorFromConfig (self):
        c = self.c
        
        
        
        bg = c.config.getColor("log_pane_background_color")
        
        
        
        try:
            self.logCtrl.configure(bg=bg)
        except:
            g.es("exception setting log pane background color")
            g.es_exception()
    #@-node:ekr.20041217135735.2:tkLog.setColorFromConfig
    #@+node:ekr.20031218072017.4046:tkLog.setFontFromConfig
    def SetWidgetFontFromConfig (self,logCtrl=None):
    
        c = self.c
    
        if not logCtrl: logCtrl = self.logCtrl
    
        font = c.config.getFontFromParams(
            "log_text_font_family", "log_text_font_size",
            "log_text_font_slant", "log_text_font_weight",
            c.config.defaultLogFontSize)
    
        self.fontRef = font # ESSENTIAL: retain a link to font.
        #logCtrl.configure(font=g.log['font'])
    
        # g.trace("LOG",logCtrl.cget("font"),font.cget("family"),font.cget("weight"))
    
        bg = c.config.getColor("log_text_background_color")
        if bg:
            try: logCtrl.configure(bg=bg)
            except: pass
    
        fg = c.config.getColor("log_text_foreground_color")
        if fg:
            try: logCtrl.configure(fg=fg)
            except: pass
            
        ffg = self.full_fg = logCtrl.cget('fg')
        self.dim_text()
        #logCtrl.config(fg = g.color_mul(0.75,ffg) )
        
    setFontFromConfig = SetWidgetFontFromConfig # Renaming supresses a pychecker warning.
    #@-node:ekr.20031218072017.4046:tkLog.setFontFromConfig
    #@-node:ekr.20051016095907.1:Config & get/saveState
    #@+node:ekr.20051016095907.2:Focus & update (tkLog)
    #@+node:ekr.20031218072017.4045:tkLog.onActivateLog
    def onActivateLog (self,event=None):
    
        try:
            self.c.setLog()
            self.frame.tree.OnDeactivate()
            self.c.logWantsFocus()
        except:
            g.es_event_exception("activate log")
    #@-node:ekr.20031218072017.4045:tkLog.onActivateLog
    #@+node:ekr.20031218072017.4044:tkLog.hasFocus
    def hasFocus (self):
        
        return self.c.get_focus() == self.logCtrl
    #@-node:ekr.20031218072017.4044:tkLog.hasFocus
    #@+node:ekr.20050208133438:forceLogUpdate
    def forceLogUpdate (self,s):
    
        if sys.platform == "darwin": # Does not work on MacOS X.
            try:
                print s, # Don't add a newline.
            except UnicodeError:
                # g.app may not be inited during scripts!
                print g.toEncodedString(s,'utf-8')
        else:
            self.logCtrl.update_idletasks()
    #@-node:ekr.20050208133438:forceLogUpdate
    #@-node:ekr.20051016095907.2:Focus & update (tkLog)
    #@+node:ekr.20051016101927:put & putnl (tkLog)
    #@+at 
    #@nonl
    # Printing uses self.logCtrl, so this code need not concern itself
    # with which tab is active.
    # 
    # Also, selectTab switches the contents of colorTags, so that is not 
    # concern.
    # It may be that Pmw will allow us to dispense with the colorTags logic...
    #@-at
    #@+node:ekr.20031218072017.1473:put
    # All output to the log stream eventually comes here.
    def put (self,s,color=None,tabName='Log'):
        
        c = self.c
        
        # print 'tkLog.put',self.c.shortFileName(),tabName,g.callers()
    
        if g.app.quitting or not c or not c.exists:
            return
    
        #if tabName:
        #    self.selectTab(tabName)
        logCtrl = self.logCtrl
        if logCtrl:
            #@        << put s to log control >>
            #@+node:EKR.20040423082910:<< put s to log control >>
            logCtrl['state']='normal'
            if color:
                #print "log color:",color
                if color not in self.colorTags:
                    self.colorTags.append(color)
                    if self.dimmed:
                        fg = g.color_mul(self.dim,color)
                    else:
                        fg = color
                    
                    self.logCtrl.tag_config(color,foreground=fg)
                
                logCtrl.insert("end",s)
                logCtrl.tag_add(color,"end-%dc" % (len(s)+1),"end-1c")
                logCtrl.tag_add("black","end")
            else:
                logCtrl.insert("end",s)
            
            logCtrl.see("end")
            
            logCtrl['state']='disabled'
            
            self.forceLogUpdate(s)
            #@-node:EKR.20040423082910:<< put s to log control >>
            #@nl
            logCtrl.update_idletasks()
        else:
            #@        << put s to logWaiting and print s >>
            #@+node:EKR.20040423082910.1:<< put s to logWaiting and print s >>
            g.app.logWaiting.append((s,color),)
            
            print "Null tkinter log"
            
            if type(s) == type(u""):
                s = g.toEncodedString(s,"ascii")
            
            print s
            #@-node:EKR.20040423082910.1:<< put s to logWaiting and print s >>
            #@nl
    #@-node:ekr.20031218072017.1473:put
    #@+node:ekr.20051016101927.1:putnl
    def putnl (self,tabName='Log'):
    
        if g.app.quitting:
            return
        #if tabName:
        #    self.selectTab(tabName)
        logCtrl = self.logCtrl
        if logCtrl:
            logCtrl['state']='normal'
            logCtrl.insert("end",'\n')
            logCtrl.see("end")
            logCtrl['state']='disabled'
            self.forceLogUpdate('\n')
        else:
            # Put a newline to logWaiting and print newline
            g.app.logWaiting.append(('\n',"black"),)
            print "Null tkinter log"
            print
    #@-node:ekr.20051016101927.1:putnl
    #@-node:ekr.20051016101927:put & putnl (tkLog)
    #@+node:ekr.20051018061932:Tab (TkLog)
    #@+node:ekr.20051017212057:clearTab
    def clearTab (self,tabName,wrap='none'):
        
        self.selectTab(tabName,wrap=wrap)
        t = self.logCtrl
        t and t.delete('1.0','end')
    #@-node:ekr.20051017212057:clearTab
    #@+node:ekr.20051024173701:createTab
    def createTab (self,tabName,wrap='none'):
        
        # g.trace(tabName,wrap)
        
        c = self.c ; k = c.k
        tabFrame = self.nb.add(tabName)
        self.menu = self.makeTabMenu(tabName)
        #@    << Create the tab's text widget >>
        #@+node:ekr.20051018072306:<< Create the tab's text widget >>
        t = self.createTextWidget(tabFrame)
        
        # Set the background color.
        configName = 'log_pane_%s_tab_background_color' % tabName
        bg = c.config.getColor(configName) or g.theme['bg']#'MistyRose1'
        
        if wrap not in ('none','char','word'): wrap = 'none'
        try: t.configure(bg=bg,wrap=wrap)
        except Exception: pass # Could be a user error.
        
        self.SetWidgetFontFromConfig(logCtrl=t)
        
        self.frameDict [tabName] = tabFrame
        self.textDict [tabName] = t
        
        # Switch to a new colorTags list.
        if self.tabName:
            self.colorTagsDict [self.tabName] = self.colorTags [:]
        
        self.colorTags = ['black']
        self.colorTagsDict [tabName] = self.colorTags
        #@-node:ekr.20051018072306:<< Create the tab's text widget >>
        #@nl
    
        if tabName != 'Log':
            # c.k doesn't exist when the log pane is created.
            # k.makeAllBindings will call setTabBindings('Log')
            self.setTabBindings(tabName)
    #@-node:ekr.20051024173701:createTab
    #@+node:ekr.20060613131217:cycleTabFocus
    def cycleTabFocus (self,event=None,stop_w = None):
    
        '''Cycle keyboard focus between the tabs in the log pane.'''
    
        c = self.c ; d = self.frameDict # Keys are page names. Values are Tk.Frames.
        w = d.get(self.tabName)
        # g.trace(self.tabName,w)
        values = d.values()
        if self.numberOfVisibleTabs() > 1:
            i = i2 = values.index(w) + 1
            if i == len(values): i = 0
            tabName = d.keys()[i]
            self.selectTab(tabName)
            return 
    #@nonl
    #@-node:ekr.20060613131217:cycleTabFocus
    #@+node:ekr.20051018102027:deleteTab
    def deleteTab (self,tabName):
        
        if tabName == 'Log':
            pass
    
        elif tabName in ('Find','Spell'):
            self.selectTab('Log')
        
        elif tabName in self.nb.pagenames():
            self.nb.delete(tabName)
            self.colorTagsDict [tabName] = []
            self.textDict [tabName] = None
            self.frameDict [tabName] = None
            self.tabName = None
            self.selectTab('Log')
            
        # New in Leo 4.4b1.
        self.c.invalidateFocus()
        self.c.bodyWantsFocus()
    #@-node:ekr.20051018102027:deleteTab
    #@+node:ekr.20060204124347:hideTab
    def hideTab (self,tabName):
        
        __pychecker__ = '--no-argsused' # tabName
        
        self.selectTab('Log')
    #@-node:ekr.20060204124347:hideTab
    #@+node:ekr.20051027114433:getSelectedTab
    def getSelectedTab (self):
        
        return self.tabName
    #@-node:ekr.20051027114433:getSelectedTab
    #@+node:ekr.20051018061932.1:lower/raiseTab
    def lowerTab (self,tabName):
        
        if tabName:
            b = self.nb.tab(tabName) # b is a Tk.Button.
            b.config(bg='grey80')
        self.c.invalidateFocus()
        self.c.bodyWantsFocus()
    
    def raiseTab (self,tabName):
    
        if tabName:
            b = self.nb.tab(tabName) # b is a Tk.Button.
            b.config(bg='LightSteelBlue1')
        self.c.invalidateFocus()
        self.c.bodyWantsFocus()
    #@-node:ekr.20051018061932.1:lower/raiseTab
    #@+node:ekr.20060613131345:numberOfVisibleTabs
    def numberOfVisibleTabs (self):
        
        return len([val for val in self.frameDict.values() if val != None])
    #@-node:ekr.20060613131345:numberOfVisibleTabs
    #@+node:ekr.20051019170806:renameTab
    def renameTab (self,oldName,newName):
        
        label = self.nb.tab(oldName)
        label.configure(text=newName)
    #@-node:ekr.20051019170806:renameTab
    #@+node:ekr.20051016101724.1:selectTab
    def selectTab (self,tabName,wrap='none'):
    
        '''Create the tab if necessary and make it active.'''
    
        c = self.c ; tabFrame = self.frameDict.get(tabName)
    
        if tabFrame:
            # Switch to a new colorTags list.
            newColorTags = self.colorTagsDict.get(tabName)
            self.colorTagsDict [self.tabName] = self.colorTags [:]
            self.colorTags = newColorTags
        else:
            self.createTab(tabName,wrap=wrap)
            
        self.nb.selectpage(tabName)
        # Update the status vars.
        self.tabName = tabName
        self.logCtrl = self.textDict.get(tabName)
        self.tabFrame = self.frameDict.get(tabName)
    
        if 0: # Absolutely do not do this here!  It is a cause of the 'sticky focus' problem.
            c.widgetWantsFocusNow(self.logCtrl)
        return tabFrame
    #@-node:ekr.20051016101724.1:selectTab
    #@+node:ekr.20051022162730:setTabBindings
    def setTabBindings (self,tabName):
        return
        c = self.c ; k = c.k
        tab = self.nb.tab(tabName)
        w = self.textDict.get(tabName)
        
        # Send all event in the text area to the master handlers.
        for kind,handler in (
            ('<Key>',       k.masterKeyHandler),
            ('<Button-1>',  k.masterClickHandler),
            ('<Button-3>',  k.masterClick3Handler),
        ):
            w.bind(kind,handler)
        
        # Clicks in the tab area are harmless: use the old code.
        def tabMenuRightClickCallback(event,menu=self.menu):
            return self.onRightClick(event,menu)
            
        def tabMenuClickCallback(event,tabName=tabName):
            return self.onClick(event,tabName)
        
        tab.bind('<Button-1>',tabMenuClickCallback)
        tab.bind('<Button-3>',tabMenuRightClickCallback)
        
        k.completeAllBindingsForWidget(w)
    #@-node:ekr.20051022162730:setTabBindings
    #@+node:ekr.20051019134106:Tab menu callbacks & helpers
    #@+node:ekr.20051019134422:onRightClick & onClick
    def onRightClick (self,event,menu):
        
        c = self.c
        menu.post(event.x_root,event.y_root)
        
        
    def onClick (self,event,tabName):
    
        self.selectTab(tabName)
    #@-node:ekr.20051019134422:onRightClick & onClick
    #@+node:ekr.20051019140004.1:newTabFromMenu
    def newTabFromMenu (self,tabName='Log'):
    
        self.selectTab(tabName)
        
        # This is called by getTabName.
        def selectTabCallback (newName):
            return self.selectTab(newName)
    
        self.getTabName(selectTabCallback)
    #@-node:ekr.20051019140004.1:newTabFromMenu
    #@+node:ekr.20051019165401:renameTabFromMenu
    def renameTabFromMenu (self,tabName):
    
        if tabName in ('Log','Completions'):
            g.es('can not rename %s tab' % (tabName),color='blue')
        else:
            def renameTabCallback (newName):
                return self.renameTab(tabName,newName)
    
            self.getTabName(renameTabCallback)
    #@-node:ekr.20051019165401:renameTabFromMenu
    #@+node:ekr.20051019172811:getTabName
    def getTabName (self,exitCallback):
        
        canvas = self.nb.component('hull')
    
        # Overlay what is there!
        f = Tk.Frame(canvas)
        f.pack(side='top',fill='both',expand=1)
        
        row1 = Tk.Frame(f)
        row1.pack(side='top',expand=0,fill='x',pady=10)
        row2 = Tk.Frame(f)
        row2.pack(side='top',expand=0,fill='x')
    
        Tk.Label(row1,text='Tab name').pack(side='left')
    
        e = Tk.Entry(row1,background='white')
        e.pack(side='left')
    
        def getNameCallback (event=None):
            s = e.get().strip()
            f.pack_forget()
            if s: exitCallback(s)
            
        def closeTabNameCallback (event=None):
            f.pack_forget()
            
        b = Tk.Button(row2,text='Ok',width=6,command=getNameCallback)
        b.pack(side='left',padx=10)
        
        b = Tk.Button(row2,text='Cancel',width=6,command=closeTabNameCallback)
        b.pack(side='left')
    
        e.focus_force()
        e.bind('<Return>',getNameCallback)
    #@-node:ekr.20051019172811:getTabName
    #@-node:ekr.20051019134106:Tab menu callbacks & helpers
    #@-node:ekr.20051018061932:Tab (TkLog)
    #@-others
#@-node:ekr.20031218072017.4039:class leoTkinterLog
#@-others
#@-node:ekr.20031218072017.3939:@thin leoTkinterFrame.py
#@-leo
