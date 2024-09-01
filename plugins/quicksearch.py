#@+leo-ver=4-thin
#@+node:AGP.20230214101615:@thin quicksearch.py
#@<< doc string >>
#@+node:AGP.20230214101615.1:<< doc string >>
'''Add a quick search to Leo's toolbar.

A search box which behaves like a web site search is added, along with
a "GO" button to do quick searches right from the main Leo window. All the
current search options are retained except that "search body text" is
explicitely set - mainly because this is by far the most common use case.

Pressing <CR> while editing the text automatically does a search. Repeated
searches can be done by clicking the "GO" button.

The combo box also stores a list of previous searches, which can be
selected to quickly repeat a search. When activating a previous
search the original search mode is used.

Still to do:

- incremental search
- reverse search
- persist recent searches across Leo sessions
- use INI file to set options for list size etc
'''
#@nonl
#@-node:AGP.20230214101615.1:<< doc string >>
#@nl

#@@language python
#@@tabwidth -4

__version__ = "0.7"

#@<< version history >>
#@+node:AGP.20230214101615.2:<< version history >>
#@+at
# 0.4 EKR: Don't mess with button width on MacOS/darwin.
# 
# 0.5 EKR: Create a separate SearchBox instance for each open window.
# - This eliminates problems when multiple windows are open.
# 0.6 EKR: Changes required by revisions of leoFind.leoFind class in Leo 4.3:
# - Removed '_flag' suffixes in OPTION_LIST.
# - Added c arg to QuickFind ctor.
#     - We now have per-commander find panels.
# - update_ivars
#     - Changed name from set_ivars.
#     - Call setattr(self,key,0), not setattr(c,key+'_flag',0)
#     - No more _flag hack.
#     - Set self ivars, not c ivars.
# - Changed init_s_text to init_s_ctrl.
#     - Changed s_text to s_ctrl.
# 0.7 EKR: Fixed crasher in Leo 4.4 by initing self.p in Quickfind ctor.
#@-at
#@nonl
#@-node:AGP.20230214101615.2:<< version history >>
#@nl
#@<< imports >>
#@+node:AGP.20230214101615.3:<< imports >>
import leoGlobals as g
import leoPlugins

import leoFind

Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)

#import ttk

import sys
import pickle,zlib,base64

#import leoEditCommands.py #leoEditCommands.py->createEditCommanders(c)
                            #c.searchCommands.findTabHandler
#@nonl
#@-node:AGP.20230214101615.3:<< imports >>
#@nl


#@+others
#@+node:AGP.20230214101615.5:onCreate
def onCreate(tag, keywords):
    
    # Not ok for unit testing: can't use unitTestGui.
    if g.app.unitTesting:
        return

    c = keywords.get("c")
    searchbox = SearchBox(c)
    
    
    #search.addWidgets()
#@nonl
#@-node:AGP.20230214101615.5:onCreate
#@+node:AGP.20230217110614:class History
class History(Tk.Entry):
    #@    @+others
    #@+node:AGP.20230217110614.1:__init__()
    def __init__(self,parent,width=30,bd=2,):
        
        self.var = Tk.StringVar()
        
        Tk.Entry.__init__(self,parent,width=30,bd=2,exportselection=0,textvariable=self.var)#,takefocus=1))
        
        self.bind("<Key>", self.onKey)
        self.bind("<FocusIn>", self.onFocusIn)
        self.bind("<FocusOut>", self.onFocusOut)
        self.bind("<Button-1>", self.onLeftClick)
        
        self.history = []
        self.lmenu = None
        
        self.action = None
        
        
    
        
        
    #@nonl
    #@-node:AGP.20230217110614.1:__init__()
    #@+node:AGP.20230217112453:onKey
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
    #@-node:AGP.20230217112453:onKey
    #@+node:AGP.20230217110614.2:onFocusIn()
    def onFocusIn(self,event):
        self.select_range(0, Tk.END)
    #@-node:AGP.20230217110614.2:onFocusIn()
    #@+node:AGP.20230217110626:onFocusOut()
    def onFocusOut(self,event):
        if self.lmenu != None:
            self.lmenu.destroy()
            self.lmenu = None
    #@nonl
    #@-node:AGP.20230217110626:onFocusOut()
    #@+node:AGP.20230217110937:onLeftClick()
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
    #@-node:AGP.20230217110937:onLeftClick()
    #@+node:AGP.20230217111007:onMenuLeftClick()
    def onMenuLeftClick(self,event):
        self.var.set(self.lmenu.get(self.lmenu.curselection()[0]))
        self.focus_set()
        
        self.lmenu.destroy()
        self.lmenu = None
        
        return "break"
    #@nonl
    #@-node:AGP.20230217111007:onMenuLeftClick()
    #@+node:AGP.20230217110956:onMenuMotion()
    def onMenuMotion(self,event):
        self.lmenu.selection_clear(0,Tk.END)
        self.lmenu.selection_set(self.lmenu.nearest(event.y))
    #@nonl
    #@-node:AGP.20230217110956:onMenuMotion()
    #@-others
#@nonl
#@-node:AGP.20230217110614:class History
#@+node:AGP.20230214101615.6:class SearchBox
class SearchBox(leoFind.leoFind):

    #@    @+others
    #@+node:AGP.20230214101615.7:__init__()
    def __init__ (self,c):
        # Init the base class.
        leoFind.leoFind.__init__(self,c)
        
        self.c = c
        self.s_ctrl = Tk.Text() # Used by find.search()
        
        self.top = self #leo will call panel.top.destroy() in destroyallpanels()... see destroy() dummy
        
        #c.searchCommands.openFindTab(show=False)
        #self.finder = c.searchCommands.findTabHandler 
        #print self.findtab.dict.keys()
        
        c.searchCommands.findTabHandler = self
        
        self.finder = self
        
        self.rmenu = None
        
        
        
        
        #@    @+others
        #@+node:AGP.20230216131200:init vars
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
        vd["radio-search-scope"].set("entire-outline")
        
        #for k in vd.keys():
        #    print k,vd[k].get()
        #@nonl
        #@-node:AGP.20230216131200:init vars
        #@+node:AGP.20230216131200.1:create widgets
        #create widgets
        self.toolbar = toolbar = c.frame.iconFrame
        
        
        self.changebox = cb = History(toolbar)
        
        
        self.tolabel = Tk.Label(toolbar,text="To")
        
        
        self.searchbox = sb = History(toolbar)   
        
        #sb.bind("<Key>", self.onKey)
        sb.bind("<Button-3>", self.onRightClick)
        
        self.action_button = ab = Tk.Menubutton(toolbar,text="Find",activebackground="light sky blue")
        
        
        self.action_menu = am = Tk.Menu(ab,tearoff=0,takefocus=0)
        ab["menu"] = am
        
        self.find_repack()
        
        #@-node:AGP.20230216131200.1:create widgets
        #@+node:AGP.20230218142713:Options menu
        self.rmenu = rmenu = Tk.Menu(self.searchbox.winfo_toplevel(),tearoff=0,takefocus=1)
            
        vd = self.dict
            
        #for k in vd.keys():
        #    print k,vd[k].get()
            
        rmenu.add_checkbutton(label="Search Headline",variable=vd["search_headline"])
        rmenu.add_checkbutton(label="Search Body",variable=vd["search_body"])
            
            
        rmenu.add_separator()
        #rmenu.add_command(label="_________________")
            
        rmenu.add_radiobutton(label="Entire Outline",variable=vd["radio-search-scope"],value="entire-outline")
        rmenu.add_radiobutton(label="Suboutline Only",variable=vd["radio-search-scope"],value="suboutline-only")
        rmenu.add_radiobutton(label="Node Only",variable=vd["radio-search-scope"],value="node-only")
            
        rmenu.add_separator()
        rmenu.add_checkbutton(label="Mark Finds",variable=vd["mark_finds"])
        rmenu.add_checkbutton(label="Mark Changes",variable=vd["mark_changes"])
            
        rmenu.add_checkbutton(label="Ignore Case",columnbreak=1,variable=vd["ignore_case"])
        rmenu.add_checkbutton(label="Whole Word", variable=vd["whole_word"])
        rmenu.add_checkbutton(label="Wrap Around",variable=vd["wrap"])
        rmenu.add_checkbutton(label="Reverse",variable=vd["reverse"])
        rmenu.add_checkbutton(label="Regexp",variable=vd["pattern_match"])
        #@nonl
        #@-node:AGP.20230218142713:Options menu
        #@-others
        
        
    #@nonl
    #@-node:AGP.20230214101615.7:__init__()
    #@+node:AGP.20230215183000:onFocusIn()
    def onFocusIn(self,event):
        self.searchbox.select_range(0, Tk.END)
    #@-node:AGP.20230215183000:onFocusIn()
    #@+node:AGP.20230215152338:onFocusOut()
    def onFocusOut(self,event):
        if self.lmenu != None:
            self.lmenu.destroy()
            self.lmenu = None
    #@nonl
    #@-node:AGP.20230215152338:onFocusOut()
    #@+node:AGP.20230214101615.12:onkey
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
    #@-node:AGP.20230214101615.12:onkey
    #@+node:AGP.20230218130414:testcommand()
    def testcommand(self):
        print "testcommand",self
    #@-node:AGP.20230218130414:testcommand()
    #@+node:AGP.20230214114431:onRightClick()
    def onRightClick(self,event):    
        try:
            self.rmenu.tk_popup(event.x_root+1,event.y_root-10)
        finally:
            self.rmenu.grab_release()
    #@-node:AGP.20230214114431:onRightClick()
    #@+node:AGP.20230218011003:find_repack()
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
    #@-node:AGP.20230218011003:find_repack()
    #@+node:AGP.20230218011952:change_repack()
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
    #@-node:AGP.20230218011952:change_repack()
    #@+node:AGP.20230216123933:destroy() dummy
    def destroy(self):
        pass
    #@nonl
    #@-node:AGP.20230216123933:destroy() dummy
    #@+node:AGP.20230216122007:leoFind implements
    #@+node:AGP.20230216235537: Top level
    #@+node:AGP.20230216235537.1:findAllCommand
    def findAllCommand (self,event=None):
        self.p = self.c.currentPosition()
        self.setup_command()
        self.findAll()
    #@-node:AGP.20230216235537.1:findAllCommand
    #@+node:AGP.20230216235537.2:findAgainCommand
    def findAgainCommand (self):
        self.findNextCommand()
        return True
    #@-node:AGP.20230216235537.2:findAgainCommand
    #@+node:AGP.20230216235537.3:cloneFindAllCommand
    def cloneFindAllCommand (self,event=None):
        self.p = self.c.currentPosition()
        self.setup_command()
        self.clone_find_all = True
        self.findAll()
        self.clone_find_all = False
    #@-node:AGP.20230216235537.3:cloneFindAllCommand
    #@+node:AGP.20230216235537.4:findNext/PrefCommand
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
    #@-node:AGP.20230216235537.4:findNext/PrefCommand
    #@+node:AGP.20230216235537.5:change/ThenFindCommand
    def changeNextCommand (self,event=None):
        if self.findNextCommand():
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
    
    
    #@-node:AGP.20230216235537.5:change/ThenFindCommand
    #@-node:AGP.20230216235537: Top level
    #@+node:AGP.20230214101615.17:update_ivars
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
    #@-node:AGP.20230214101615.17:update_ivars
    #@+node:AGP.20230214101615.18:init_s_ctrl
    def init_s_ctrl (self,s):
        t = self.s_ctrl
        t.delete("1.0","end")
        t.insert("end",s)
        t.mark_set("insert",g.choose(self.reverse,"end","1.0"))
        return t
    #@-node:AGP.20230214101615.18:init_s_ctrl
    #@-node:AGP.20230216122007:leoFind implements
    #@-others
#@-node:AGP.20230214101615.6:class SearchBox
#@-others

if Tk: # OK for unit testing.

    if g.app.gui is None:
        g.app.createTkGui(__file__)

    if g.app.gui.guiName() == "tkinter":
        leoPlugins.registerHandler("after-create-leo-frame", onCreate)
        g.plugin_signon(__name__)
        
#@-node:AGP.20230214101615:@thin quicksearch.py
#@-leo
