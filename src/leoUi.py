# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:AGP.20250415230112.2925:@thin leoUi.py
#@@first

"""A module containing the base leoGui class.

This class and its subclasses hides the details of which gui is actually being used.
Leo's core calls this class to allocate all gui objects.

Plugins may define their own gui classes by setting g.app.gui."""

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import leoFind
import leoTkinterDialog

import leoColor

import leoUndo

import leoNodes
from leoNodes import position
import leoFind

import leo

import tkFont
import tkFileDialog
import os
import string
import sys
import Tkinter as Tk
from PIL import Image,ImageTk
import threading
import time
import traceback
import _ctypes
import re


#@+others
#@+node:AGP.20260224172326:Globals
#@+node:AGP.20260224172735:create_window()
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
#@-node:AGP.20260224172735:create_window()
#@+node:AGP.20260224172029:createRootWindow()
def createRootWindow():

    """Create a hidden Tk root window."""

    self.root = root = Tk.Tk()
    
    root.withdraw()
    
    from binascii import unhexlify
    
    wid = g.app.gui.root.winfo_id()
    
    root.title("Leo Main Window")
    
    
    self.setDefaultIcon()
    if g.app.config:
        self.getDefaultConfigFont(g.app.config)
        
    root.withdraw()
    
    

    return root
#@-node:AGP.20260224172029:createRootWindow()
#@+node:AGP.20251128113631.2:class HISTORY
class HISTORY(Tk.Entry):
    #@    @+others
    #@+node:AGP.20251128113631.3:__init__()
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
    #@-node:AGP.20251128113631.3:__init__()
    #@+node:AGP.20251128113631.4:onKey
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
    #@-node:AGP.20251128113631.4:onKey
    #@+node:AGP.20251128113631.5:onFocusIn()
    def onFocusIn(self,event):
        self.select_range(0, Tk.END)
    #@-node:AGP.20251128113631.5:onFocusIn()
    #@+node:AGP.20251128113631.6:onFocusOut()
    def onFocusOut(self,event):
        if self.lmenu != None:
            self.lmenu.destroy()
            self.lmenu = None
    #@nonl
    #@-node:AGP.20251128113631.6:onFocusOut()
    #@+node:AGP.20251128113631.7:onLeftClick()
    def onLeftClick(self,event):
        
        if self.lmenu != None:
            self.lmenu.destroy()
            self.lmenu = None
        
        h = self.history
        if len(h) > 0:
            self.lmenu = lmenu = Tk.Listbox(
                                                self.winfo_toplevel(),
                                                width=self["width"],
                                                bg=self["background"],
                                                height=len(h),
                                                takefocus=0,
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
    #@-node:AGP.20251128113631.7:onLeftClick()
    #@+node:AGP.20251128113631.8:onMenuLeftClick()
    def onMenuLeftClick(self,event):
        self.var.set(self.lmenu.get(self.lmenu.curselection()[0]))
        self.focus_set()
        
        self.lmenu.destroy()
        self.lmenu = None
        
        return "break"
    #@nonl
    #@-node:AGP.20251128113631.8:onMenuLeftClick()
    #@+node:AGP.20251128113631.9:onMenuMotion()
    def onMenuMotion(self,event):
        self.lmenu.selection_clear(0,Tk.END)
        self.lmenu.selection_set(self.lmenu.nearest(event.y))
    #@nonl
    #@-node:AGP.20251128113631.9:onMenuMotion()
    #@-others
#@nonl
#@-node:AGP.20251128113631.2:class HISTORY
#@+node:AGP.20251128113631.10:class SEARCHBOX
class SEARCHBOX(leoFind.leoFind):

    #@    @+others
    #@+node:AGP.20251128113631.11:__init__()
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
        #@+node:AGP.20251128113631.12:init vars
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
        #@-node:AGP.20251128113631.12:init vars
        #@+node:AGP.20251128113631.13:create widgets
        #create widgets
        
        if not hasattr(c.frame,"iconFrame"):    #fix for nullframe
            return None
        
        self.toolbar = toolbar = c.frame.menuFrame
        
        c.frame.searchbox = self
        
        self.changebox = cb = HISTORY(c,toolbar)
        cb.bind("<MouseWheel>",c.frame.TopMouseWheel)
        
        self.tolabel = Tk.Label(toolbar,text="To")#,font=c.frame.iconbarfont)
        
        
        self.searchbox = sb = HISTORY(c,toolbar)   
        sb.bind("<MouseWheel>",c.frame.TopMouseWheel)
        #sb.bind("<Key>", self.onKey)
        sb.bind("<Button-3>", self.onRightClick)
        
        self.action_button = ab = Tk.Menubutton(toolbar,text="Find")#,font=c.frame.iconbarfont)
        
        
        self.action_menu = am = Tk.Menu(ab,tearoff=0,takefocus=0)
        ab["menu"] = am
        
        self.find_repack()
        
        #@+others
        #@+node:AGP.20251128113631.14:Options menu
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
        #@-node:AGP.20251128113631.14:Options menu
        #@-others
        #@-node:AGP.20251128113631.13:create widgets
        #@-others
        
        
    #@nonl
    #@-node:AGP.20251128113631.11:__init__()
    #@+node:AGP.20251128113631.15:config()
    def config(self,dic):
        pass
    #@nonl
    #@-node:AGP.20251128113631.15:config()
    #@+node:AGP.20251128113631.16:setFocus()
    def SetFocus(self):
        self.searchbox.focus_set()
    #@nonl
    #@-node:AGP.20251128113631.16:setFocus()
    #@+node:AGP.20251128113631.17:onFocusIn()
    def onFocusIn(self,event):
        self.searchbox.select_range(0, Tk.END)
    #@-node:AGP.20251128113631.17:onFocusIn()
    #@+node:AGP.20251128113631.18:onFocusOut()
    def onFocusOut(self,event):
        if self.lmenu != None:
            self.lmenu.destroy()
            self.lmenu = None
    #@nonl
    #@-node:AGP.20251128113631.18:onFocusOut()
    #@+node:AGP.20251128113631.19:onkey
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
    #@-node:AGP.20251128113631.19:onkey
    #@+node:AGP.20251128113631.20:testcommand()
    def testcommand(self):
        print "testcommand",self
    #@-node:AGP.20251128113631.20:testcommand()
    #@+node:AGP.20251128113631.21:onRightClick()
    def onRightClick(self,event):    
        try:
            self.rmenu.tk_popup(event.x_root+1,event.y_root-10)
        finally:
            self.rmenu.grab_release()
    #@-node:AGP.20251128113631.21:onRightClick()
    #@+node:AGP.20251128113631.22:find_repack()
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
    #@-node:AGP.20251128113631.22:find_repack()
    #@+node:AGP.20251128113631.23:change_repack()
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
    #@-node:AGP.20251128113631.23:change_repack()
    #@+node:AGP.20251128113631.24: Top level
    #@+node:AGP.20251128113631.25:findAllCommand
    def findAllCommand (self,event=None):
        self.p = self.c.currentPosition()
        self.setup_command()
        self.findAll()
    #@-node:AGP.20251128113631.25:findAllCommand
    #@+node:AGP.20251128113631.26:findAgainCommand
    def findAgainCommand (self):
        self.findNextCommand()
        return True
    #@-node:AGP.20251128113631.26:findAgainCommand
    #@+node:AGP.20251128113631.27:cloneFindAllCommand
    def cloneFindAllCommand (self,event=None):
        self.p = self.c.currentPosition()
        self.setup_command()
        self.clone_find_all = True
        self.findAll()
        self.clone_find_all = False
    #@-node:AGP.20251128113631.27:cloneFindAllCommand
    #@+node:AGP.20251128113631.28:findNext/PrevCommand
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
    #@-node:AGP.20251128113631.28:findNext/PrevCommand
    #@+node:AGP.20251128113631.29:change/ThenFindCommand
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
    
    
    #@-node:AGP.20251128113631.29:change/ThenFindCommand
    #@-node:AGP.20251128113631.24: Top level
    #@+node:AGP.20251128113631.30:update_ivars
    def update_ivars (self):
        
        """Called just before doing a find to update ivars."""
    
        for key in self.intKeys:
            # g.trace('settattr',key,False)
            setattr(self, key,False)
    
        self.change_text = self.changebox.var.get()
        self.find_text = self.searchbox.var.get()
    
        
        
        # Set options
        vd = self.dict
        
        
        
        
        for k in vd.keys():
            setattr(self, k, vd[k].get())
            #print k,getattr(self,k)
            
        search_scope = vd["radio-search-scope"].get()
        self.suboutline_only = g.choose(search_scope == "suboutline-only",1,0)
        self.node_only       = g.choose(search_scope == "node-only",1,0)
        self.selection       = g.choose(search_scope == "selection-only",1,0) # 11/9/03
        
        #print "****node_only",self.node_only
    #@nonl
    #@-node:AGP.20251128113631.30:update_ivars
    #@+node:AGP.20251128113631.31:init_s_ctrl
    def init_s_ctrl (self,s):
        t = self.s_ctrl
        t.delete("1.0","end")
        t.insert("end",s)
        t.mark_set("insert",g.choose(self.reverse,"end","1.0"))
        return t
    #@-node:AGP.20251128113631.31:init_s_ctrl
    #@-others
#@-node:AGP.20251128113631.10:class SEARCHBOX
#@+node:AGP.20251128111642.4:class SCROLLBAR
class SCROLLBAR(Tk.Frame):
    #@    @+others
    #@+node:AGP.20251128111642.5:__init__()
    def __init__(self,parent,dir,command=None,corner=False):
        
        self.corner = corner
        
        #self.width = sh_width = g.theme["scrollbar_width"]
        
        Tk.Frame.__init__(self,parent,class_="ScrollBar")
        #width = self.cget("width")
        
        self.active = self.option_get("activecolor","ScrollBar")#g.theme["shade"](0.5)
        inactive = self.inactive = self.option_get("inactivecolor","ScrollBar")
        
        if dir:
            self.width = self.cget("width")
            sh = self.shuttle = Tk.Frame(self,bg=inactive)
        else:
            self.width = self.cget("height")
            sh = self.shuttle = Tk.Frame(self,bg=inactive)
        
        
        self.parent = parent
        self.command = command
        self.dir = dir
        self.start = None
        self.data = None
        self.mousin = False
        
        sh.bind("<Motion>",self.on_move)
        sh.bind("<Button>",self.on_mouse_down)
        sh.bind("<ButtonRelease>",self.on_mouse_up)
        sh.bind("<Enter>",self.on_mouse_in)
        sh.bind("<Leave>",self.on_mouse_out)
        
        
    #@nonl
    #@-node:AGP.20251128111642.5:__init__()
    #@+node:AGP.20251128111642.6:on_move()
    def on_move(self,event):
        height = self.parent.winfo_height()
        if self.start != None:#event.state & 0x0100:
            #print "moving"
            if self.dir:
                off = (event.y_root - self.start)*1.0/self.winfo_height()
                self.start = event.y_root
            else:
                off = (event.x_root - self.start)*1.0/self.winfo_width()
                self.start = event.x_root
                
            self.command(Tk.MOVETO,self.offset+off)
            
            
    #@-node:AGP.20251128111642.6:on_move()
    #@+node:AGP.20251128111642.7:on_mouse_down()
    def on_mouse_down(self,event):
        if event.num == 1:
            if self.dir:
                self.start = event.y_root
            else:
                self.start = event.x_root
        
    #@nonl
    #@-node:AGP.20251128111642.7:on_mouse_down()
    #@+node:AGP.20251128111642.8:on_mouse_up()
    def on_mouse_up(self,event):
        if event.num == 1:
            self.start = None
        if not self.mousein:
            self.shuttle.config(bg=self.inactive)
        
    #@nonl
    #@-node:AGP.20251128111642.8:on_mouse_up()
    #@+node:AGP.20251128111642.9:on_mouse_in()
    def on_mouse_in(self,event):
        self.mousein = True
        self.shuttle.config(bg=self.active)
    #@nonl
    #@-node:AGP.20251128111642.9:on_mouse_in()
    #@+node:AGP.20251128111642.10:on_mouse_out()
    def on_mouse_out(self,event):
        if self.start == None:
            self.shuttle.config(bg=self.inactive)
            
        self.mousein = False
    #@nonl
    #@-node:AGP.20251128111642.10:on_mouse_out()
    #@+node:AGP.20251128111642.11:set()
    def set(self,a,b):
        #print "set",a,b
        self.offset = a = float(a)
        b=float(b)
        self.data = (a,b)
        #print "set",a,b
        
        
            
        if a==0.0 and b == 1.0:
            self.shuttle.place_forget()
            return
            
        if self.dir:
            if self.corner:
                h = float(self.winfo_height())
                corner_factor = (h-self.width)/h
                a *= corner_factor
                b *= corner_factor
            self.shuttle.place(relx=0.0,rely=a,relheight=b-a)
        else:
            if 0:#self.corner:
                w = float(self.winfo_width())
                corner_factor = (w-self.width)/w
                a *= corner_factor
                b *= corner_factor
            self.shuttle.place(rely=0.0,relx=a,relwidth=b-a)
            
    #@nonl
    #@-node:AGP.20251128111642.11:set()
    #@+node:AGP.20251128111642.12:get()
    def get(self):
        return self.data
    #@nonl
    #@-node:AGP.20251128111642.12:get()
    #@-others
#@nonl
#@-node:AGP.20251128111642.4:class SCROLLBAR
#@+node:AGP.20260224075828:class keyHandlerClass - moded #agpkey
class keyHandlerClass:
    
    '''A class to handle toplevel keyboard command.'''


    #@    @+others
    #@+node:AGP.20260224075828.1:__init__()
    def __init__ (self):    
        self.special_keys = ('Caps_Lock', 'Num_Lock', 'Control_L', 'Alt_L','Shift_L',
                                 'Control_R', 'Alt_R','Shift_R','Win_L','Win_R')
                                 
        self.keysym_trans ={
                            'asterisk':'*',
                            'equal':'=',
                            'minus':'-',
                            'plus':'+',
                            'period':'.',
                            'slash':'/'
                            }
        
        #self.getShortcuts()
        self.shortcuts = {}
        
        if leo.app.gui.root is not None:
            #print "bindall"
            leo.app.gui.root.bind_all('<Key>', self)
    
        
        
        
        
        
        
            
        
    #@nonl
    #@-node:AGP.20260224075828.1:__init__()
    #@+node:AGP.20260224075828.2:__call__()
    def __call__(self,event):
        #print "keyHandler()"+":"+event.keysym+":"+event.char
        
        char = event.char
        keysym = event.keysym
            
        if keysym in self.special_keys:
            return
        
        #create key-stroke
        statelist = []
        
        if event.state & 0x20000:# 	Alt
            statelist.append("Alt")
        if event.state & 0x0001:# 	shift
            statelist.append("Shift")
        if event.state & 0x0004:# 	Control
            statelist.append("Ctrl")
        
        trans = self.keysym_trans.get(keysym,None)
        
        if trans:#len(keysym) > 1:
            statelist.append(trans)
        else:
            statelist.append(keysym.title())
        
        keystroke =  "-".join(statelist)#.lower()
        
        print keystroke,char,keysym
        if keystroke in self.shortcuts:
            #print keystroke,"in shortcuts"
            cmd = self.shortcuts[keystroke]
            if cmd:                                 #call command
                print "keyHandler()->",keystroke,cmd
                cmd(event)
                return "break"
        
        #send event to widget
        return
    #@nonl
    #@-node:AGP.20260224075828.2:__call__()
    #@+node:AGP.20260224075828.3:getShortcuts()
    def getShortcuts(self):
        c = leo.c
        # get cmd name to func
        PublicCommands = c.leoCommands.getPublicCommands()
        PublicCommands.update(c.editCommands.getPublicCommands())
        PublicCommands.update(c.searchCommands.getPublicCommands())
        
        cmdkeys  =  PublicCommands.keys()
        cmdkeys.sort()    
        commands = {}
        
        settings = leo.config.settings
        #shortcut = key,cmdname
        
        #inverted_dict = {value: key for key, value in my_dict.items()}
        shortcuts = self.shortcuts = {}
        
        for cmd in cmdkeys:
            if cmd in settings:
                shortcuts[settings[cmd].title()] = PublicCommands[cmd]
                print settings[cmd].title(),cmd
            #cmdname = cmd.replace("-","").lower()
            #commands[cmdname] = PublicCommands[cmd]
        
        
        #print "KeyHandler shortcuts:",self.shortcuts
        #print "config shortcuts:",leo.config.shortcutsDict
    #@nonl
    #@-node:AGP.20260224075828.3:getShortcuts()
    #@+node:AGP.20260224075828.4:shortcutFromSetting()
    def shortcutFromSetting(self,s):
        
        # Replace all minus signs by plus signs, except a trailing minus:
        if not s: return
            
            
        if s.endswith('-'):
            s = s[:-1].replace('-','+') + '-'
        else:
            s = s.replace('-','+')
            
        #print "shortcutFromSetting",s
        
        return s
        
        
    def prettyPrintKey (self,stroke,brief=False):
        return stroke
    #@nonl
    #@-node:AGP.20260224075828.4:shortcutFromSetting()
    #@+node:AGP.20260224075828.5:setDefaultUnboundKeyAction (self):
    def setDefaultUnboundKeyAction (self):
        pass
        
        
    def showStateAndMode(self):
        pass
    #@-node:AGP.20260224075828.5:setDefaultUnboundKeyAction (self):
    #@+node:AGP.20260224075828.6:finishCreate()
    def finishCreate (self):
        #body = self.c.frame.body
        #body.bind('<Key>', self)
        #body.bind('<Key>', body.on_key,'+')
        #leo.app.gui.root.bind_all('<Key>', self)
        pass
    #@nonl
    #@-node:AGP.20260224075828.6:finishCreate()
    #@-others
#@-node:AGP.20260224075828:class keyHandlerClass - moded #agpkey
#@+node:AGP.20251128111642:class leoGui
class leoGui():
    
    """A class encapulating all calls to tkinter."""
    
    #@    @+others
    #@+node:AGP.20251128111642.13:__init__()
    def __init__ (self):
    
        # Initialize the base class.
        #leoGui.__init__(self,"tkinter")------------------------------
        self.lastFrame = None
        self.leoIcon = None
        self.mGuiName = "tkinter"
        self.mainLoop = None
        self.root = None
        self.script = None
        self.utils = None
        self.isNullGui = False
        #----------------------------------------------------------------
    
        self.bitmap_name = None
        self.bitmap = None
        self.win32clipboard = None
        self.defaultFont = None
        self.defaultFontFamily = None
        
        self.keyHandler = None
    #@-node:AGP.20251128111642.13:__init__()
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
    #@+node:AGP.20251128111642.15:createRootWindow()
    def createRootWindow(self):
    
        """Create a hidden Tk root window."""
    
        self.root = root = Tk.Tk()
        
        root.withdraw()
        
        from binascii import unhexlify
        
        wid = g.app.gui.root.winfo_id()
        
        root.title("Leo Main Window")
        
        
        self.setDefaultIcon()
        if g.app.config:
            self.getDefaultConfigFont(g.app.config)
            
        root.withdraw()
        
        
    
        return root
    #@-node:AGP.20251128111642.15:createRootWindow()
    #@+node:AGP.20251128111642.27:createLeoFrame()
    def createLeoFrame(self,title):
        """Create a new Leo frame."""
        
        # print 'tkGui.createLeoFrame'
    
        gui = self
        return leoFrame(title,gui)
    #@-node:AGP.20251128111642.27:createLeoFrame()
    #@+node:AGP.20251128111642.16:setDefaultIcon()
    def setDefaultIcon(self):
        
        """Set the icon to be used in all Leo windows.
        
        This code does nothing for Tk versions before 8.4.3."""
        
        gui = self
    
        try:
            version = gui.root.getvar("tk_patchLevel")
            # g.trace(repr(version),g.CheckVersion(version,"8.4.3"))
            if g.CheckVersion(version,"8.4.3") and sys.platform == "win32":
                
                # tk 8.4.3 or greater: load a 16 by 16 icon.
                path = g.os_path_join(g.app.loadDir,"..","Icons")
                if g.os_path_exists(path):
                    #theFile = g.os_path_join(path,"LeoApp16.ico")
                    theFile = g.os_path_join(path,"LeoxApp.ico")
                    if g.os_path_exists(path):
                        self.bitmap = theFile#Tk.BitmapImage(theFile)
                    else:
                        g.es("LeoApp.ico not in Icons directory", color="red")
                else:
                    g.es("Icons directory not found: "+path, color="red")
        except:
            print "exception setting bitmap"
            import traceback ; traceback.print_exc()
    #@-node:AGP.20251128111642.16:setDefaultIcon()
    #@+node:AGP.20251128111642.17:getDefaultConfigFont()
    def getDefaultConfigFont(self,config):
        
        """Get the default font from a new text widget."""
    
        if not self.defaultFontFamily:
            # WARNING: retain NO references to widgets or fonts here!
            t = Tk.Text()
            fn = t.cget("font")
            font = tkFont.Font(font=fn) 
            family = font.cget("family")
            self.defaultFontFamily = family[:]
            # print '***** getDefaultConfigFont',repr(family)
    
        config.defaultFont = None
        config.defaultFontFamily = self.defaultFontFamily
    #@-node:AGP.20251128111642.17:getDefaultConfigFont()
    #@+node:AGP.20251128111642.18:destroySelf()
    def destroySelf (self):
    
        if 0: # Works in Python 2.1 and 2.2.  Leaves Python window open.
            self.root.destroy()
            
        else: # Works in Python 2.3.  Closes Python window.
            self.root.quit()
    #@-node:AGP.20251128111642.18:destroySelf()
    #@+node:AGP.20251128111642.19:finishCreate (not used: must be present)
    def finishCreate (self):
        
        pass
        
        # g.trace('g.app.gui')
    #@-node:AGP.20251128111642.19:finishCreate (not used: must be present)
    #@+node:AGP.20251128111642.20:killGui (not used)
    def killGui(self,exitFlag=True):
        
        """Destroy a gui and terminate Leo if exitFlag is True."""
    
        pass # Not ready yet.
    #@-node:AGP.20251128111642.20:killGui (not used)
    #@+node:AGP.20251128111642.21:recreateRootWindow (not used)
    def recreateRootWindow(self):
        """A do-nothing base class to create the hidden root window of a gui
    
        after a previous gui has terminated with killGui(False)."""
        pass
    #@-node:AGP.20251128111642.21:recreateRootWindow (not used)
    #@+node:AGP.20251128111642.22:runMainLoop (tkGui)
    def runMainLoop(self):
    
        """Run tkinter's main loop."""
    
        if self.script:
            log = g.app.log
            if log:
                print 'Start of batch script...\n'
                log.c.executeScript(script=self.script)
                print 'End of batch script'
            else:
                print 'no log, no commander for executeScript in tkInterGui.runMainLoop'
        else:
             # g.trace("tkinterGui")
            self.root.mainloop()
    #@-node:AGP.20251128111642.22:runMainLoop (tkGui)
    #@+node:AGP.20251128111642.23:app.gui.Tkinter dialogs
    def runAboutLeoDialog(self,c,version,theCopyright,url,email):
        """Create and run a Tkinter About Leo dialog."""
        d = leoTkinterDialog.tkinterAboutLeo(c,version,theCopyright,url,email)
        return d.run(modal=False)
        
    def runAskLeoIDDialog(self):
        """Create and run a dialog to get g.app.LeoID."""
        d = leoTkinterDialog.tkinterAskLeoID()
        return d.run(modal=True)
    
    def runAskOkDialog(self,c,title,message=None,text="Ok"):
        """Create and run a Tkinter an askOK dialog ."""
        d = leoTkinterDialog.tkinterAskOk(c,title,message,text)
        return d.run(modal=True)
    
    def runAskOkCancelNumberDialog(self,c,title,message):
        """Create and run askOkCancelNumber dialog ."""
        d = leoTkinterDialog.tkinterAskOkCancelNumber(c,title,message)
        return d.run(modal=True)
    
    def runAskYesNoDialog(self,c,title,message=None):
        """Create and run an askYesNo dialog."""
        d = leoTkinterDialog.tkinterAskYesNo(c,title,message)
        return d.run(modal=True)
    
    def runAskYesNoCancelDialog(self,c,title,
        message=None,yesMessage="Yes",noMessage="No",defaultButton="Yes"):
        """Create and run an askYesNoCancel dialog ."""
        d = leoTkinterDialog.tkinterAskYesNoCancel(
            c,title,message,yesMessage,noMessage,defaultButton)
        return d.run(modal=True)
    #@-node:AGP.20251128111642.23:app.gui.Tkinter dialogs
    #@+node:AGP.20251128111642.24:app.gui.Tkinter file dialogs
    # We no longer specify default extensions so that we can open and save files without extensions.
    #@+node:AGP.20251128111642.25:runOpenFileDialog
    def runOpenFileDialog(self,title,filetypes,defaultextension,multiple=False):
    
        """Create and run an Tkinter open file dialog ."""
        
        initialdir = g.app.globalOpenDir or g.os_path_abspath(os.getcwd())
        
        if multiple:
            # askopenfilenames requires Python 2.3 and Tk 8.4.
            version = '.'.join([str(sys.version_info[i]) for i in (0,1,2)])
            if (
                g.CheckVersion(version,"2.3") and
                g.CheckVersion(self.root.getvar("tk_patchLevel"),"8.4")
            ):
                files = tkFileDialog.askopenfilenames(
                    title=title,filetypes=filetypes,initialdir=initialdir)
                # g.trace(files)
                return list(files)
            else:
                # Get one file and return it as a list.
                theFile = tkFileDialog.askopenfilename(
                    title=title,filetypes=filetypes,initialdir=initialdir)
                return [theFile]
        else:
            # Return a single file name as a string.
            return tkFileDialog.askopenfilename(
                title=title,filetypes=filetypes,initialdir=initialdir)
    #@-node:AGP.20251128111642.25:runOpenFileDialog
    #@+node:AGP.20251128111642.26:runSaveFileDialog
    def runSaveFileDialog(self,initialfile,title,filetypes,defaultextension):
    
        """Create and run an Tkinter save file dialog ."""
        
        initialdir=g.app.globalOpenDir or g.os_path_abspath(os.getcwd()),
    
        return tkFileDialog.asksaveasfilename(
            initialdir=initialdir,initialfile=initialfile,
            title=title,filetypes=filetypes)
    #@-node:AGP.20251128111642.26:runSaveFileDialog
    #@-node:AGP.20251128111642.24:app.gui.Tkinter file dialogs
    #@+node:AGP.20251128111642.28:app.gui.Tkinter.utils
    #@+node:AGP.20251128111642.29:Clipboard (tkGui)
    #@+at
    # 
    # The following are called only when g.app.gui.win32clipboard is not None, 
    # and
    # presently that never happens.
    #@-at
    #@+node:AGP.20251128111642.30:replaceClipboardWith
    def replaceClipboardWith (self,s):
    
        # g.app.gui.win32clipboard is always None.
        wcb = g.app.gui.win32clipboard
    
        if wcb:
            try:
                wcb.OpenClipboard(0)
                wcb.EmptyClipboard()
                wcb.SetClipboardText(s)
                wcb.CloseClipboard()
            except:
                g.es_exception()
        else:
            self.root.clipboard_clear()
            self.root.clipboard_append(s)
    #@-node:AGP.20251128111642.30:replaceClipboardWith
    #@+node:AGP.20251128111642.31:getTextFromClipboard
    def getTextFromClipboard (self):
        
        # g.app.gui.win32clipboard is always None.
        wcb = g.app.gui.win32clipboard
        
        if wcb:
            try:
                wcb.OpenClipboard(0)
                data = wcb.GetClipboardData()
                wcb.CloseClipboard()
                # g.trace(data)
                return data
            except TypeError:
                # g.trace(None)
                return None
            except:
                g.es_exception()
                return None
        else:
            try:
                s = self.root.selection_get(selection="CLIPBOARD")
                return s
            except:
                return None
    #@-node:AGP.20251128111642.31:getTextFromClipboard
    #@-node:AGP.20251128111642.29:Clipboard (tkGui)
    #@+node:AGP.20251128111642.32:Dialog
    #@+node:AGP.20251128111642.33:get_window_info
    # WARNING: Call this routine _after_ creating a dialog.
    # (This routine inhibits the grid and pack geometry managers.)
    
    def get_window_info (self,top):
        
        top.update_idletasks() # Required to get proper info.
    
        # Get the information about top and the screen.
        geom = top.geometry() # geom = "WidthxHeight+XOffset+YOffset"
        dim,x,y = string.split(geom,'+')
        w,h = string.split(dim,'x')
        w,h,x,y = int(w),int(h),int(x),int(y)
        
        return w,h,x,y
    #@-node:AGP.20251128111642.33:get_window_info
    #@+node:AGP.20251128111642.34:center_dialog
    def center_dialog(self,top):
    
        """Center the dialog on the screen.
    
        WARNING: Call this routine _after_ creating a dialog.
        (This routine inhibits the grid and pack geometry managers.)"""
    
        sw = top.winfo_screenwidth()
        sh = top.winfo_screenheight()
        w,h,x,y = self.get_window_info(top)
        
        # Set the new window coordinates, leaving w and h unchanged.
        x = (sw - w)/2
        y = (sh - h)/2
        top.geometry("%dx%d%+d%+d" % (w,h,x,y))
        
        return w,h,x,y
    #@-node:AGP.20251128111642.34:center_dialog
    #@+node:AGP.20251128111642.35:create_labeled_frame
    # Returns frames w and f.
    # Typically the caller would pack w into other frames, and pack content into f.
    
    def create_labeled_frame (self,parent,
        caption=None,relief="groove",bd=2,padx=0,pady=0):
    
        # Create w, the master frame.
        w = Tk.Frame(parent)
        w.grid(sticky="news")
        
        # Configure w as a grid with 5 rows and columns.
        # The middle of this grid will contain f, the expandable content area.
        w.columnconfigure(1,minsize=bd)
        w.columnconfigure(2,minsize=padx)
        w.columnconfigure(3,weight=1)
        w.columnconfigure(4,minsize=padx)
        w.columnconfigure(5,minsize=bd)
        
        w.rowconfigure(1,minsize=bd)
        w.rowconfigure(2,minsize=pady)
        w.rowconfigure(3,weight=1)
        w.rowconfigure(4,minsize=pady)
        w.rowconfigure(5,minsize=bd)
    
        # Create the border spanning all rows and columns.
        border = Tk.Frame(w,bd=bd,relief=relief) # padx=padx,pady=pady)
        border.grid(row=1,column=1,rowspan=5,columnspan=5,sticky="news")
        
        # Create the content frame, f, in the center of the grid.
        f = Tk.Frame(w,bd=bd)
        f.grid(row=3,column=3,sticky="news")
        
        # Add the caption.
        if caption and len(caption) > 0:
            caption = Tk.Label(parent,text=caption,highlightthickness=0,bd=0)
            caption.tkraise(w)
            caption.grid(in_=w,row=0,column=2,rowspan=2,columnspan=3,padx=4,sticky="w")
    
        return w,f
    #@-node:AGP.20251128111642.35:create_labeled_frame
    #@-node:AGP.20251128111642.32:Dialog
    #@+node:AGP.20251128111642.36:Focus
    #@+node:AGP.20251128111642.37:get_focus
    def get_focus(self,c):
        
        """Returns the widget that has focus, or body if None."""
    
        return c.frame.top.focus_displayof()
    #@-node:AGP.20251128111642.37:get_focus
    #@+node:AGP.20251128111642.38:set_focus (app.gui)
    set_focus_count = 0
    
    def set_focus(self,c,w):
        
        """Put the focus on the widget."""
    
                    
        if not g.app.unitTesting and c and c.config.getBool('trace_g.app.gui.set_focus'):
            self.set_focus_count += 1
            # Do not call trace here: that might affect focus!
            print 'gui.set_focus: %4d %10s %s' % (
                self.set_focus_count,c and c.shortFileName(),
                c and c.widget_name(w)), g.callers(5)
        
        if w:
            try:
                # It's possible that the widget doesn't exist now.
                w.focus_set()
                return True
            except Exception:
                # g.es_exception()
                return False
    #@-node:AGP.20251128111642.38:set_focus (app.gui)
    #@-node:AGP.20251128111642.36:Focus
    #@+node:AGP.20251128111642.39:Font
    #@+node:AGP.20251128111642.40:tkGui.getFontFromParams
    def getFontFromParams(self,family,size,slant,weight,defaultSize=12):
        
        family_name = family
        
        try:
            font = tkFont.Font(family=family,size=size,slant=slant,weight=weight)
            # if g.app.trace: g.trace(font)
            return font
        except:
            g.es("exception setting font from ",family_name)
            g.es("family,size,slant,weight:",family,size,slant,weight)
            # g.es_exception() # This just confuses people.
            return g.app.config.defaultFont
    #@-node:AGP.20251128111642.40:tkGui.getFontFromParams
    #@-node:AGP.20251128111642.39:Font
    #@+node:AGP.20251128111642.41:Icons
    #@+node:AGP.20251128111642.42:attachLeoIcon & createLeoIcon
    def attachLeoIcon (self,w):
        
        """Try to attach a Leo icon to the Leo Window.
        
        Use tk's wm_iconbitmap function if available (tk 8.3.4 or greater).
        Otherwise, try to use the Python Imaging Library and the tkIcon package."""
    
        if self.bitmap != None:
            # We don't need PIL or tkicon: this is tk 8.3.4 or greater.
            try:
                
                if sys.platform == "win32":
                    import ctypes
    
                    myappid = 'python.tkinter.leox' # arbitrary string
                    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
                
                w.wm_iconbitmap(self.bitmap)
            except:
                self.bitmap = None
        
        if self.bitmap == None:
            try:
                #@            << try to use the PIL and tkIcon packages to draw the icon >>
                #@+node:AGP.20251128111642.43:<< try to use the PIL and tkIcon packages to draw the icon >>
                #@+at 
                #@nonl
                # This code requires Fredrik Lundh's PIL and tkIcon packages:
                # 
                # Download PIL    from 
                # http://www.pythonware.com/downloads/index.htm#pil
                # Download tkIcon from http://www.effbot.org/downloads/#tkIcon
                # 
                # Many thanks to Jonathan M. Gilligan for suggesting this 
                # code.
                #@-at
                #@@c
                
                import Image
                import tkIcon
                
                # Wait until the window has been drawn once before attaching the icon in OnVisiblity.
                def visibilityCallback(event,self=self,w=w):
                    try: self.leoIcon.attach(w.winfo_id())
                    except: pass
                w.bind("<Visibility>",visibilityCallback)
                
                if not self.leoIcon:
                    # Load a 16 by 16 gif.  Using .gif rather than an .ico allows us to specify transparency.
                    icon_file_name = g.os_path_join(g.app.loadDir,'..','Icons','LeoWin.gif')
                    icon_file_name = g.os_path_normpath(icon_file_name)
                    icon_image = Image.open(icon_file_name)
                    if 1: # Doesn't resize.
                        self.leoIcon = self.createLeoIcon(icon_image)
                    else: # Assumes 64x64
                        self.leoIcon = tkIcon.Icon(icon_image)
                #@-node:AGP.20251128111642.43:<< try to use the PIL and tkIcon packages to draw the icon >>
                #@nl
            except:
                # import traceback ; traceback.print_exc()
                # g.es_exception()
                self.leoIcon = None
    #@+node:AGP.20251128111642.44:createLeoIcon
    # This code is adapted from tkIcon.__init__
    # Unlike the tkIcon code, this code does _not_ resize the icon file.
    
    def createLeoIcon (self,icon):
        
        try:
            import Image,_tkicon
            
            i = icon ; m = None
            # create transparency mask
            if i.mode == "P":
                try:
                    t = i.info["transparency"]
                    m = i.point(lambda i, t=t: i==t, "1")
                except KeyError: pass
            elif i.mode == "RGBA":
                # get transparency layer
                m = i.split()[3].point(lambda i: i == 0, "1")
            if not m:
                m = Image.new("1", i.size, 0) # opaque
            # clear unused parts of the original image
            i = i.convert("RGB")
            i.paste((0, 0, 0), (0, 0), m)
            # create icon
            m = m.tostring("raw", ("1", 0, 1))
            c = i.tostring("raw", ("BGRX", 0, -1))
            return _tkicon.new(i.size, c, m)
        except:
            return None
    #@-node:AGP.20251128111642.44:createLeoIcon
    #@-node:AGP.20251128111642.42:attachLeoIcon & createLeoIcon
    #@-node:AGP.20251128111642.41:Icons
    #@+node:AGP.20251128111642.45:Idle Time
    #@+node:AGP.20251128111642.46:tkinterGui.setIdleTimeHook
    def setIdleTimeHook (self,idleTimeHookHandler):
    
        if self.root:
            self.root.after_idle(idleTimeHookHandler)
    #@-node:AGP.20251128111642.46:tkinterGui.setIdleTimeHook
    #@+node:AGP.20251128111642.47:setIdleTimeHookAfterDelay
    def setIdleTimeHookAfterDelay (self,idleTimeHookHandler):
        
        if self.root:
            g.app.root.after(g.app.idleTimeDelay,idleTimeHookHandler)
    #@-node:AGP.20251128111642.47:setIdleTimeHookAfterDelay
    #@-node:AGP.20251128111642.45:Idle Time
    #@+node:AGP.20251128111642.48:Indices (Tk)
    #@+node:AGP.20251128111642.49:toGuiIndex & toPythonIndex
    def toGuiIndex (self,s,w,index):
        
        '''Convert a python index in string s into a Tk index in Tk.Text widget w.'''
        
        # A subtle point: s typically does not have Tk's trailing newline, so add it.
    
        row,col = g.convertPythonIndexToRowCol (s+'\n',index)
        index = w.index('%s.%s' % (row+1,col))
        return index
        
    def toPythonIndex (self,s,w,index):
        
        '''Convert a Tk index in Tk.Text widget w into a python index in string s.'''
        
        index = w.index(index)
        row, col = index.split('.') ; row, col = int(row), int(col)
        index = g.convertRowColToPythonIndex (s,row-1,col)
        return index
    #@-node:AGP.20251128111642.49:toGuiIndex & toPythonIndex
    #@+node:AGP.20251128111642.50:firstIndex
    def firstIndex (self):
    
        return "1.0"
    #@-node:AGP.20251128111642.50:firstIndex
    #@+node:AGP.20251128111642.51:lastIndex
    def lastIndex (self):
    
        return "end"
    #@-node:AGP.20251128111642.51:lastIndex
    #@+node:AGP.20251128111642.52:moveIndexBackward
    def moveIndexBackward(self,index,n):
    
        return "%s-%dc" % (index,n)
    #@-node:AGP.20251128111642.52:moveIndexBackward
    #@+node:AGP.20251128111642.53:moveIndexForward & moveIndexToNextLine
    def moveIndexForward(self,t,index,n):
    
        newpos = t.index("%s+%dc" % (index,n))
        
        return g.choose(t.compare(newpos,"==","end"),None,newpos)
        
    def moveIndexToNextLine(self,t,index):
    
        newpos = t.index("%s linestart + 1lines" % (index))
        
        return g.choose(t.compare(newpos,"==","end"),None,newpos)
    #@-node:AGP.20251128111642.53:moveIndexForward & moveIndexToNextLine
    #@+node:AGP.20251128111642.54:compareIndices
    def compareIndices (self,t,n1,rel,n2):
        
        try:
            return t.compare(n1,rel,n2)
        except Exception:
            return False
    #@-node:AGP.20251128111642.54:compareIndices
    #@+node:AGP.20251128111642.55:getindex
    def getindex(self,text,index):
        
        """Convert string index of the form line.col into a tuple of two ints."""
        
        return tuple(map(int,string.split(text.index(index), ".")))
    #@-node:AGP.20251128111642.55:getindex
    #@-node:AGP.20251128111642.48:Indices (Tk)
    #@+node:AGP.20251128111642.56:Insert Point
    #@+node:AGP.20251128111642.57:getInsertPoint
    def getInsertPoint(self,t):
        
        try:
            return t.index("insert")
        except Exception:
            return '1.0'
    #@-node:AGP.20251128111642.57:getInsertPoint
    #@+node:AGP.20251128111642.58:setInsertPoint
    def setInsertPoint (self,t,pos):
    
        try:
            t.mark_set("insert",pos)
        except Exception:
            pass
    #@-node:AGP.20251128111642.58:setInsertPoint
    #@-node:AGP.20251128111642.56:Insert Point
    #@+node:AGP.20251128111642.59:Selection
    #@+node:AGP.20251128111642.60:getSelectionRange
    def getSelectionRange (self,t):
        
        try:
            # Warning: this can return None.
            return t.tag_ranges("sel")
        except Exception:
            return 0,0
    #@-node:AGP.20251128111642.60:getSelectionRange
    #@+node:AGP.20251128111642.61:getSelectedText
    def getSelectedText (self,t):
    
        start, end = self.getTextSelection(t)
        if start and end and start != end:
            s = t.get(start,end)
            if s is None:
                return u""
            else:
                return g.toUnicode(s,g.app.tkEncoding)
        else:
            return u""
    #@-node:AGP.20251128111642.61:getSelectedText
    #@+node:AGP.20251128111642.62:getTextSelection
    def getTextSelection (self,t,sort=True):
        
        """Return a tuple representing the selected range of t, a Tk.Text widget.
        
        Return a tuple giving the insertion point if no range of text is selected."""
    
        # To get the current selection.
        try:
            sel = t.tag_ranges("sel")
        except Exception:
            return 0,0
    
        if len(sel) == 2:
            i,j = sel
            if sort:
                if t.compare(i, ">", j):
                    i,j = j,i
            return i,j
        else:
            # Return the insertion point if there is no selected text.
            insert = t.index("insert")
        return insert,insert
    #@-node:AGP.20251128111642.62:getTextSelection
    #@+node:AGP.20251128111642.63:hasSelection
    def hasSelection (self,widget):
        
        i,j = self.getTextSelection(widget)
        return i and j and i != j
    #@-node:AGP.20251128111642.63:hasSelection
    #@+node:AGP.20251128111642.64:selectAllText (new in 4.4.1)
    def selectAllText (self,w,insert='end-1c'):
        
        '''Select all text of the widget, *not* including the extra newline.'''
        
        self.setTextSelection(w,'1.0','end-1c',insert=insert)
    #@-node:AGP.20251128111642.64:selectAllText (new in 4.4.1)
    #@+node:AGP.20251128111642.65:setSelectionRangeWithLength
    def setSelectionRangeWithLength(self,t,start,length,insert='sel.end'):
        
        return g.app.gui.setTextSelection(t,start,"%s+%dc" % (start,length),insert=insert)
    #@-node:AGP.20251128111642.65:setSelectionRangeWithLength
    #@+node:AGP.20251128111642.66:setTextSelection & setSelectionRange
    def setTextSelection (self,t,start,end,insert='sel.end'):
        
        """tk gui: set the selection range in Tk.Text widget t."""
    
        if not start or not end:
            return
            
        try:
            if t.compare(start, ">", end):
                start,end = end,start
                
            t.tag_remove("sel","1.0",start)
            t.tag_add("sel",start,end)
            t.tag_remove("sel",end,"end")
            
            # New in 4.4a5: this logic ensures compatibility with previous code.
            if insert == 'sel.end':
                g.app.gui.setInsertPoint(t,end)
            elif insert is not None:
                g.app.gui.setInsertPoint(t,insert)
        except Exception:
            pass
        
    setSelectionRange = setTextSelection
    #@-node:AGP.20251128111642.66:setTextSelection & setSelectionRange
    #@-node:AGP.20251128111642.59:Selection
    #@+node:AGP.20251128111642.67:Text
    #@+node:AGP.20251128111642.68:g.app.gui.getAllText
    def getAllText (self,t):
        
        """Return all the text of Tk.Text widget t converted to unicode."""
    
        s = t.get("1.0","end-1c") # New in 4.4.1: use end-1c.
    
        if s is None:
            return u""
        else:
            return g.toUnicode(s,g.app.tkEncoding)
    #@-node:AGP.20251128111642.68:g.app.gui.getAllText
    #@+node:AGP.20251128111642.69:getCharAfterIndex
    def getCharAfterIndex (self,t,index):
        
        if t.compare(index + "+1c",">=","end"):
            return None
        else:
            ch = t.get(index + "+1c")
            return g.toUnicode(ch,g.app.tkEncoding)
    #@-node:AGP.20251128111642.69:getCharAfterIndex
    #@+node:AGP.20251128111642.70:getCharAtIndex
    def getCharAtIndex (self,t,index):
        ch = t.get(index)
        return g.toUnicode(ch,g.app.tkEncoding)
    #@-node:AGP.20251128111642.70:getCharAtIndex
    #@+node:AGP.20251128111642.71:getCharBeforeIndex
    def getCharBeforeIndex (self,t,index):
        
        index = t.index(index)
        if index == "1.0":
            return None
        else:
            ch = t.get(index + "-1c")
            return g.toUnicode(ch,g.app.tkEncoding)
    #@-node:AGP.20251128111642.71:getCharBeforeIndex
    #@+node:AGP.20251128111642.72:getLineContainingIndex
    def getLineContainingIndex (self,t,index):
    
        line = t.get(index + " linestart", index + " lineend")
        return g.toUnicode(line,g.app.tkEncoding)
    #@-node:AGP.20251128111642.72:getLineContainingIndex
    #@+node:AGP.20251128111642.73:replaceSelectionRangeWithText (leoTkinterGui)
    def replaceSelectionRangeWithText (self,t,start,end,text):
    
        t.delete(start,end)
        t.insert(start,text)
    #@-node:AGP.20251128111642.73:replaceSelectionRangeWithText (leoTkinterGui)
    #@-node:AGP.20251128111642.67:Text
    #@+node:AGP.20251128111642.74:Visibility
    #@+node:AGP.20251128111642.75:makeIndexVisible
    def makeIndexVisible(self,t,index):
    
        return t.see(index)
    #@-node:AGP.20251128111642.75:makeIndexVisible
    #@-node:AGP.20251128111642.74:Visibility
    #@+node:AGP.20251128111642.76:isTextWidget
    def isTextWidget (self,w):
        
        '''Return True if w is a Text widget suitable for text-oriented commands.'''
        
        return w and isinstance(w,Tk.Text)
    #@-node:AGP.20251128111642.76:isTextWidget
    #@-node:AGP.20251128111642.28:app.gui.Tkinter.utils
    #@-others
#@-node:AGP.20251128111642:class leoGui
#@+node:AGP.20251128113631.32:class leoFrame
class leoFrame():
    
    """A class that represents a Leo window rendered in Tk/tkinter."""

    #@    @+others
    #@+node:AGP.20251128113631.33:__init__()
    def __init__(self,title,gui):
    
        # Init the base class.----------------------------------------------------
        #leoFrame.__init__(self,gui)
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
        
        self.prefsPanel = None
        self.statusLine = None
        
    
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
    
        
        
        # subclass init -----------------------------------------------------------------
        self.title = title
    
        #leoTkinterFrame.instances += 1
    
        self.c = None # Set in finishCreate.
        self.iconBar = None
        
        self.lastx = -1
    
        #self.trace_status_line = None # Set in finishCreate.
        #@    << set the leoTkinterFrame ivars >>
        #@+node:AGP.20251128113631.34:<< set the leoTkinterFrame ivars >>
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
        #@-node:AGP.20251128113631.34:<< set the leoTkinterFrame ivars >>
        #@nl
        
        self.topgeometry = 800,600,30,30
    #@-node:AGP.20251128113631.33:__init__()
    #@+node:AGP.20251128113631.35:__repr__()
    def __repr__ (self):
    
        return "<leoTkinterFrame: %s>" % self.title
    #@-node:AGP.20251128113631.35:__repr__()
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
    
    #@-node:AGP.20250415230112.2841:xWantsFocus
    #@+node:AGP.20251128113631.36:finishCreate()
    def finishCreate (self,c):
        
        f = self ; f.c = c
        # g.trace('tkFrame')
        
        # This must be done after creating the commander.
        f.splitVerticalFlag,f.ratio,f.secondary_ratio = f.initialRatios()
        #f.splitVerticalFlag = True  # agp
        
        leo.gui.keyHandler = c.keyHandler = c.k = self.keyHandler = keyHandlerClass()
        
        #@    @+others
        #@+node:AGP.20251128113631.37:Toplevel
        #f.createOuterFrames()
        f.top = top = Tk.Toplevel()
        
        top.withdraw()
        
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
        #@-node:AGP.20251128113631.37:Toplevel
        #@+node:AGP.20251128113631.38:Menu / iconBar / Status
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
        
                
        self.searchbox = SEARCHBOX(c)
        
        self.iconFrame = Tk.Frame(outerFrame,name="iconframe",height =32)
        self.iconFrame.pack_propagate(0)
        #,bd=5,relief="groove",bg=g.theme['shade'](0.5))
        self.iconFrame.pack(side='top',fill="x",expand = False)
        
        self.iconBar = self.iconBarClass(c,self.iconFrame)
        #@-node:AGP.20251128113631.38:Menu / iconBar / Status
        #@+node:AGP.20251128113631.39:Splitters
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
        
        f.qlink = leoQlink(f,qlinkframe)
        
        
        self.subtreeframe = subtreeframe = Tk.Frame(treeframe)
        subtreeframe.pack(expand=1,fill='both',pady=1)
        
        
        # Create the canvas, tree, log and body.
        
        
        
        
        f.tree = leoTree(f,subtreeframe)
        f.log  = leoLog(f,logframe)
        f.body = leoBody(f,bodyframe)
        
        
        
        # Yes, this an "official" ivar: this is a kludge.
        f.bodyCtrl = f.body.bodyCtrl
        
        
        #if c.k:c.k.finishCreate()
        
        
        
        # Configure.
        f.setTabWidth(c.tab_width)
        #f.tree.setColorFromConfig()
        f.reconfigurePanes()
        #f.body.setFontFromConfig()
        #f.body.setColorFromConfig()
        
        self.guiframes = outerFrame,editframe,bodyframe,treeframe,subtreeframe,logframe,qlinkframe,f.tree.font
        
        
        
        
            
        
            
        
        #@-node:AGP.20251128113631.39:Splitters
        #@+node:AGP.20260224080304:KeyHandler and menu
        #@-node:AGP.20260224080304:KeyHandler and menu
        #@+node:AGP.20251128113631.40:Create first tree node
        #f.createFirstTreeNode()
        t = leoNodes.tnode()
        v = leoNodes.vnode(t)
        p = leoNodes.position(v,[])
        v.initHeadString("NewHeadline")
        p.moveToRoot(oldRoot=None)
        c.setRootPosition(p) # New in 4.4.2.
        c.editPosition(p)
        
        #@-node:AGP.20251128113631.40:Create first tree node
        #@-others
        
        self.keyHandler.getShortcuts()
        
        f.menu = leoMenu(f)
            # c.finishCreate calls f.createMenuBar later.
        
        
        
        
    
        
        
        #f.body.focus_set()
        
        
        
        
        g.app.log = self.log #c.setLog()
        g.app.windowList.append(f)
        c.initVersion()
        c.signOnWithVersion()
        
        
        
        c.bodyWantsFocusNow()
        
        #self.trace_status_line = c.config.getBool('trace_status_line')
        # f.enableTclTraces()
        
        #self.iconbarfont = c.config.getFontFromParams(
        #    "icon_bar_font_family", "icon_bar_font_size",
        #    "icon_bar_font_slant",  "icon_bar_font_weight",7)
        
        self.reconfigure()
        # Redraw the window before writing into it.
        
        self.setTopGeometry(*self.topgeometry)
        
        
        
        #self.show() #moved to various location to avoid flickers
        
        
    #@-node:AGP.20251128113631.36:finishCreate()
    #@+node:AGP.20251128113631.44:create_splitter()
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
    #@-node:AGP.20251128113631.44:create_splitter()
    #@+node:AGP.20251128113631.45:splitter_relplace()
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
    #@-node:AGP.20251128113631.45:splitter_relplace()
    #@+node:AGP.20251128113631.46:TopMouseWheel()
    def TopMouseWheel(self,event=None): #agp
        #work around the default tkinter mousewheel focus routing
        
        t = self.top
        w =  t.winfo_containing(*t.winfo_pointerxy())
        
        if w.master == self.canvas:
            w = self.canvas
        
        if event and event.state & 0x04:
            #print "CTRL-SCROLL",w
            
            import tkinter
            from tkinter.font import Font, nametofont
            
            #print tkinter.Font
            if hasattr(w,"on_zoom"):
                w.on_zoom(event.delta)
    
        
            return "break"
        
        #print 'tmw',widget
        
        if w != None and hasattr(w,"yview"):
            if hasattr(w,"nScroll"):
                nScroll = w.nScroll
            else:
                nScroll = 1        
            
            if event.delta < 1:
                w.yview_scroll( nScroll, Tk.UNITS)
            else:
                if w.yview()[0] != 0.0:
                    w.yview_scroll( -nScroll, Tk.UNITS)
        
        return "break"
    #@-node:AGP.20251128113631.46:TopMouseWheel()
    #@+node:AGP.20251128113631.47:SplitterOnMouseDown()
    def SplitterOnMouseDown(self,event):
        #print "mousedown",event.x_root,event.y_root
        self.start = event.x_root,event.y_root
        
        
    #@nonl
    #@-node:AGP.20251128113631.47:SplitterOnMouseDown()
    #@+node:AGP.20251128113631.48:SplitterOnRightMouseDown()
    def SplitterOnRightMouseDown(self,event):
        #print "mousedown",event.x_root,event.y_root
        self.toggleTkSplitDirection(True)
        
    #@nonl
    #@-node:AGP.20251128113631.48:SplitterOnRightMouseDown()
    #@+node:AGP.20251128113631.49:SplitterOnMouseDrag()
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
        
        top.update_idletasks()
        
    #@nonl
    #@-node:AGP.20251128113631.49:SplitterOnMouseDrag()
    #@+node:AGP.20251128113631.50:resizePanesToRatio
    def resizePanesToRatio(self,ratio=None,ratio2=None):
        
        # g.trace(ratio,ratio2,g.callers())
        if ratio == None:
            ratio = self.ratio
            
        if ratio2 == None:
            ratio2 = self.secondary_ratio
        
        
        self.splitter_relplace(self.bar1,ratio)
        self.splitter_relplace(self.bar2,ratio2)
        
        #self.divideLeoSplitter(self.splitVerticalFlag,9.0/10)#,ratio)    #agp
        #self.divideLeoSplitter(not self.splitVerticalFlag,1.0/3)#,ratio2)
    #@nonl
    #@-node:AGP.20251128113631.50:resizePanesToRatio
    #@+node:AGP.20251128113631.51:show()
    def show(self):
        # agp avoid startup flicker
        self.deiconify()
        self.lift()
        self.update()
        self.resizePanesToRatio()
    #@-node:AGP.20251128113631.51:show()
    #@+node:AGP.20251128113631.52:Scrolling callbacks (frame)
    def setCallback (self,*args,**keys):
        
        """Callback to adjust the scrollbar.
        
        Args is a tuple of two floats describing the fraction of the visible area."""
    
        # g.trace(self.tree.redrawCount,args)
    
        apply(self.treeBar.set,args,keys)
    
            
    def yviewCallback (self,*args,**keys):
        
        """Tell the canvas to scroll"""
        
        # g.trace(vyiewCallback",args,keys)
    
    
        apply(self.canvas.yview,args,keys)
    #@-node:AGP.20251128113631.52:Scrolling callbacks (frame)
    #@+node:AGP.20251128113631.68:Destroying the frame
    #@+node:AGP.20251128113631.69:destroyAllObjects
    def destroyAllObjects (self):
    
        """Clear all links to objects in a Leo window."""
    
        frame = self ; c = self.c ; tree = frame.tree ; body = self.body
    
        # Do this first.
        #@    << clear all vnodes and tnodes in the tree >>
        #@+node:AGP.20251128113631.70:<< clear all vnodes and tnodes in the tree>>
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
        #@-node:AGP.20251128113631.70:<< clear all vnodes and tnodes in the tree>>
        #@nl
    
        # Destroy all ivars in subcommanders.
        g.clearAllIvars(c.atFileCommands)
        g.clearAllIvars(c.fileCommands)
        g.clearAllIvars(c.importCommands)
        #g.clearAllIvars(c.tangleCommands)
        g.clearAllIvars(c.undoer)
        g.clearAllIvars(c)
        g.clearAllIvars(body.colorizer)
        g.clearAllIvars(body)
        g.clearAllIvars(tree)
    
        # This must be done last.
        frame.destroyAllPanels()
        g.clearAllIvars(frame)
    #@-node:AGP.20251128113631.69:destroyAllObjects
    #@+node:AGP.20251128113631.71:destroyAllPanels
    def destroyAllPanels (self):
    
        """Destroy all panels attached to this frame."""
        
        panels = (self.comparePanel, self.colorPanel, self.findPanel, self.fontPanel, self.prefsPanel)
    
        for panel in panels:
            if panel:
                panel.top.destroy()
    #@-node:AGP.20251128113631.71:destroyAllPanels
    #@+node:AGP.20251128113631.72:destroySelf (tkFrame)
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
    #@-node:AGP.20251128113631.72:destroySelf (tkFrame)
    #@-node:AGP.20251128113631.68:Destroying the frame
    #@+node:AGP.20251128113631.73:class iconBarClass
    class iconBarClass:
        
        '''A class representing the singleton Icon bar'''
        
        #@    @+others
        #@+node:AGP.20251128113631.74:__init__()
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
        #@-node:AGP.20251128113631.74:__init__()
        #@+node:AGP.20251128113631.75:add
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
                #@+node:AGP.20251128113631.76:<< create a picture >>
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
                #@-node:AGP.20251128113631.76:<< create a picture >>
                #@nl
            elif text:
                b = Tk.Button(f,text=text,command=command,bg=f['bg'])
                if sys.platform != 'darwin':
                    width = max(6,len(text))
                    b.configure(width=width)
                b.pack(side="left", fill="y")
                return b
                
            return None
        #@-node:AGP.20251128113631.75:add
        #@+node:AGP.20251128113631.77:clear
        def clear(self):
            
            """Destroy all the widgets in the icon bar"""
            
            f = self.iconFrame
            
            for slave in f.pack_slaves():
                slave.destroy()
            self.visible = False
        
            f.configure(height="30") # The default height.
            g.app.iconWidgetCount = 0
            g.app.iconImageRefs = []
        #@-node:AGP.20251128113631.77:clear
        #@+node:AGP.20251128113631.78:getFrame
        def getFrame (self):
        
            return self.iconFrame
        #@-node:AGP.20251128113631.78:getFrame
        #@+node:AGP.20251128113631.79:pack (show)
        def pack (self):
            
            """Show the icon bar by repacking it"""
            
            if not self.visible:
                self.visible = True
                #self.menuFrame.pack(side='top',fill="x")
                self.iconFrame.pack(side='top',fill="x")
                
        show = pack
        #@-node:AGP.20251128113631.79:pack (show)
        #@+node:AGP.20251128113631.80:unpack (hide)
        def unpack (self):
            
            """Hide the icon bar by unpacking it.
            
            A later call to show will repack it in a new location."""
            
            if self.visible:
                self.visible = False
                self.iconFrame.pack_forget()
                #self.menuFrame.pack_forget()
                
        hide = unpack
        #@-node:AGP.20251128113631.80:unpack (hide)
        #@-others
    #@-node:AGP.20251128113631.73:class iconBarClass
    #@+node:AGP.20251128113631.86:Icon area methods (compatibility)
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
    #@-node:AGP.20251128113631.86:Icon area methods (compatibility)
    #@+node:AGP.20251128113631.87:class statusLineClass
    class statusLineClass:
        
        '''A class representing the status line.'''
        
        #@    @+others
        #@+node:AGP.20251128113631.88:Xctor
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
        #@-node:AGP.20251128113631.88:Xctor
        #@+node:AGP.20251128113631.89:__init__ ()
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
            
            
        #@-node:AGP.20251128113631.89:__init__ ()
        #@+node:AGP.20251128113631.90:clear
        def clear (self):
            pass
            t = self.textWidget
            if not t: return
            
            #trace = self.c.frame.trace_status_line and not g.app.unitTesting
            #if trace: g.trace(g.callers())
            
            t.configure(state="normal")
            t.delete("1.0","end")
            t.configure(state="disabled")
        #@-node:AGP.20251128113631.90:clear
        #@+node:AGP.20251128113631.91:enable, disable & isEnabled
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
        #@-node:AGP.20251128113631.91:enable, disable & isEnabled
        #@+node:AGP.20251128113631.92:get
        def get (self):
            pass
            t = self.textWidget
            if t:
                return t.get("1.0","end")
            else:
                return ""
        #@-node:AGP.20251128113631.92:get
        #@+node:AGP.20251128113631.93:getFrame
        def getFrame (self):
            pass
            return self.statusFrame
        #@-node:AGP.20251128113631.93:getFrame
        #@+node:AGP.20251128113631.94:onActivate
        def onActivate (self,event=None):
            pass
            # Don't change background as the result of simple mouse clicks.
            background = self.statusFrame.cget("background")
            self.enable(background=background)
        #@-node:AGP.20251128113631.94:onActivate
        #@+node:AGP.20251128113631.95:pack & show
        def pack (self):
            pass
            if not self.isVisible:
                self.isVisible = True
                self.statusFrame.pack(fill="x",pady=1)
                
        show = pack
        #@-node:AGP.20251128113631.95:pack & show
        #@+node:AGP.20251128113631.96:put (leoTkinterFrame:statusLineClass)
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
        #@-node:AGP.20251128113631.96:put (leoTkinterFrame:statusLineClass)
        #@+node:AGP.20251128113631.97:unpack & hide
        def unpack (self):
            pass
            if self.isVisible:
                self.isVisible = False
                self.statusFrame.pack_forget()
        
        hide = unpack
        #@-node:AGP.20251128113631.97:unpack & hide
        #@+node:AGP.20251128113631.98:update (statusLine)
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
        #@-node:AGP.20251128113631.98:update (statusLine)
        #@-others
    #@-node:AGP.20251128113631.87:class statusLineClass
    #@+node:AGP.20251128113631.99:Status line methods (compatibility)
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
    #@-node:AGP.20251128113631.99:Status line methods (compatibility)
    #@+node:AGP.20251128113631.100:Configuration (tkFrame)
    #@+node:AGP.20251128113631.101:reconfigure()
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
    
    #@-node:AGP.20251128113631.101:reconfigure()
    #@+node:AGP.20251128113631.102:XconfigureBar
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
    #@-node:AGP.20251128113631.102:XconfigureBar
    #@+node:AGP.20251128113631.103:configureBarsFromConfig
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
    #@-node:AGP.20251128113631.103:configureBarsFromConfig
    #@+node:AGP.20251128113631.104:reconfigureFromConfig
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
    #@-node:AGP.20251128113631.104:reconfigureFromConfig
    #@+node:AGP.20251128113631.105:setInitialWindowGeometry
    def setInitialWindowGeometry(self):
        
        """Set the position and size of the frame to config params."""
        
        c = self.c
        #print "setInitialWindowGeometry"
        h = c.config.getInt("initial_window_height") or 500
        w = c.config.getInt("initial_window_width") or 600
        x = c.config.getInt("initial_window_left") or 10
        y = c.config.getInt("initial_window_top") or 10
        
        if h and w and x and y:
            self.setTopGeometry(w,h,x,y)
    #@-node:AGP.20251128113631.105:setInitialWindowGeometry
    #@+node:AGP.20251128113631.106:setTabWidth
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
    #@-node:AGP.20251128113631.106:setTabWidth
    #@+node:AGP.20251128113631.107:f.setWrap
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
    #@-node:AGP.20251128113631.107:f.setWrap
    #@+node:AGP.20251128113631.108:setTopGeometry
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
        #print "setTopGeometry"+geom
        self.top.geometry(geom)
    #@-node:AGP.20251128113631.108:setTopGeometry
    #@+node:AGP.20251128113631.109:reconfigurePanes (use config bar_width)
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
    #@-node:AGP.20251128113631.109:reconfigurePanes (use config bar_width)
    #@-node:AGP.20251128113631.100:Configuration (tkFrame)
    #@+node:AGP.20251128113631.110:Event handlers (tkFrame)
    #@+node:AGP.20251128113631.111:frame.OnCloseLeoEvent
    # Called from quit logic and when user closes the window.
    # Returns True if the close happened.
    
    def OnCloseLeoEvent(self):
        
        f = self ; c = f.c
        
        if c.inCommand:
            g.trace('requesting window close')
            c.requestCloseWindow = True
        else:
            g.app.closeLeoWindow(self)
    #@-node:AGP.20251128113631.111:frame.OnCloseLeoEvent
    #@+node:AGP.20251128113631.112:frame.OnControlKeyUp/Down
    def OnControlKeyDown (self,event=None):
        
        self.controlKeyIsDown = True
        
    def OnControlKeyUp (self,event=None):
        
        self.controlKeyIsDown = False
    #@-node:AGP.20251128113631.112:frame.OnControlKeyUp/Down
    #@+node:AGP.20251128113631.113:OnActivateBody (tkFrame)
    def OnActivateBody (self,event=None):
        
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
    #@-node:AGP.20251128113631.113:OnActivateBody (tkFrame)
    #@+node:AGP.20251128113631.114:OnActivateLeoEvent, OnDeactivateLeoEvent
    def OnActivateLeoEvent(self,event=None):
        
        '''Handle a click anywhere in the Leo window.'''
        
        self.c.setLog()
    
    def OnDeactivateLeoEvent(self,event=None):
        
        pass # This causes problems on the Mac.
    #@-node:AGP.20251128113631.114:OnActivateLeoEvent, OnDeactivateLeoEvent
    #@+node:AGP.20251128113631.115:OnActivateTree
    def OnActivateTree (self,event=None):
    
        try:
            frame = self ; c = frame.c
            c.setLog()
    
            if 0: # Do NOT do this here!
                # OnActivateTree can get called when the tree gets DE-activated!!
                c.bodyWantsFocus()
                
        except:
            g.es_event_exception("activate tree")
    #@-node:AGP.20251128113631.115:OnActivateTree
    #@+node:AGP.20251128113631.116:OnBodyClick, OnBodyRClick (Events)
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
    #@-node:AGP.20251128113631.116:OnBodyClick, OnBodyRClick (Events)
    #@+node:AGP.20251128113631.117:OnBodyDoubleClick (Events)
    def OnBodyDoubleClick (self,event=None):
    
        try:
            c = self.c ; p = c.currentPosition()
            if event and not g.doHook("bodydclick1",c=c,p=p,v=p,event=event):
                c.editCommands.extendToWord(event) # Handles unicode properly.
            g.doHook("bodydclick2",c=c,p=p,v=p,event=event)
        except:
            g.es_event_exception("bodydclick")
            
        return "break" # Restore this to handle proper double-click logic.
    #@-node:AGP.20251128113631.117:OnBodyDoubleClick (Events)
    #@+node:AGP.20251128113631.118:OnMouseWheel (Tomaz Ficko)
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
    #@-node:AGP.20251128113631.118:OnMouseWheel (Tomaz Ficko)
    #@+node:AGP.20251128113631.119:OnCanvasB2 (agp)
    def OnCanvasB2(self, event=None):
        self.lastx = event.x
        return  
    #@-node:AGP.20251128113631.119:OnCanvasB2 (agp)
    #@+node:AGP.20251128113631.120:OnCanvasMotion (agp)
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
    #@-node:AGP.20251128113631.120:OnCanvasMotion (agp)
    #@+node:AGP.20251128113631.121:OnPaste (To support middle-button paste)
    def OnPaste (self,event=None):
        
        return self.pasteText(event=event,middleButton=True)
    #@nonl
    #@-node:AGP.20251128113631.121:OnPaste (To support middle-button paste)
    #@-node:AGP.20251128113631.110:Event handlers (tkFrame)
    #@+node:AGP.20251128113631.122:Gui-dependent commands
    #@+node:AGP.20251128113631.123:Minibuffer commands... (tkFrame)
    
    #@+node:AGP.20251128113631.124:contractPane
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
    #@-node:AGP.20251128113631.124:contractPane
    #@+node:AGP.20251128113631.125:expandPane
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
    #@-node:AGP.20251128113631.125:expandPane
    #@+node:AGP.20251128113631.126:fullyExpandPane
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
    #@-node:AGP.20251128113631.126:fullyExpandPane
    #@+node:AGP.20251128113631.127:hidePane
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
    #@-node:AGP.20251128113631.127:hidePane
    #@+node:AGP.20251128113631.128:expand/contract/hide...Pane
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
    #@-node:AGP.20251128113631.128:expand/contract/hide...Pane
    #@+node:AGP.20251128113631.129:fullyExpand/hide...Pane
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
    #@-node:AGP.20251128113631.129:fullyExpand/hide...Pane
    #@-node:AGP.20251128113631.123:Minibuffer commands... (tkFrame)
    #@+node:AGP.20251128113631.130:Edit Menu...
    #@+node:AGP.20251128113631.131:abortEditLabelCommand
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
    #@-node:AGP.20251128113631.131:abortEditLabelCommand
    #@+node:AGP.20251128113631.132:endEditLabelCommand
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
    #@-node:AGP.20251128113631.132:endEditLabelCommand
    #@+node:AGP.20251128113631.133:insertHeadlineTime
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
    #@-node:AGP.20251128113631.133:insertHeadlineTime
    #@+node:AGP.20251128113631.134:Cut/Copy/Paste (tkFrame)
    #@+node:AGP.20251128113631.135:copyText
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
    #@-node:AGP.20251128113631.135:copyText
    #@+node:AGP.20251128113631.136:cutText
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
    #@-node:AGP.20251128113631.136:cutText
    #@+node:AGP.20251128113631.137:pasteText
    def pasteText (self,event=None,middleButton=False):
        #print "pastext"
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
        
        singleLine = wname.startswith('head')
        
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
    #@-node:AGP.20251128113631.137:pasteText
    #@+node:AGP.20251128113631.138:swapText
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
        
        singleLine = wname.startswith('head')
        
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
    #@-node:AGP.20251128113631.138:swapText
    #@-node:AGP.20251128113631.134:Cut/Copy/Paste (tkFrame)
    #@-node:AGP.20251128113631.130:Edit Menu...
    #@+node:AGP.20251128113631.139:Window Menu...
    #@+node:AGP.20251128113631.140:toggleActivePane
    def toggleActivePane (self,event=None):
        
        '''Toggle the focus between the outline and body panes.'''
        
        frame = self ; c = frame.c
    
        if c.get_focus() == frame.bodyCtrl:
            c.treeWantsFocusNow()
        else:
            c.endEditing()
            c.bodyWantsFocusNow()
    #@-node:AGP.20251128113631.140:toggleActivePane
    #@+node:AGP.20251128113631.141:cascade
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
    #@-node:AGP.20251128113631.141:cascade
    #@+node:AGP.20251128113631.142:equalSizedPanes
    def equalSizedPanes (self,event=None):
        
        '''Make the outline and body panes have the same size.'''
    
        frame = self
        print "equalsizedpanes"
        frame.resizePanesToRatio(0.5,frame.secondary_ratio)
    #@-node:AGP.20251128113631.142:equalSizedPanes
    #@+node:AGP.20251128113631.143:hideLogWindow
    def hideLogWindow (self,event=None):
        
        frame = self
        frame.divideLeoSplitter2(0.99, not frame.splitVerticalFlag)
    #@-node:AGP.20251128113631.143:hideLogWindow
    #@+node:AGP.20251128113631.144:minimizeAll
    def minimizeAll (self,event=None):
    
        '''Minimize all Leo's windows.'''
        
        self.minimize(g.app.pythonFrame)
        for frame in g.app.windowList:
            self.minimize(frame)
            self.minimize(frame.findPanel)
        
    def minimize(self,frame):
    
        if frame and frame.top.state() == "normal":
            frame.top.iconify()
    #@-node:AGP.20251128113631.144:minimizeAll
    #@+node:AGP.20251128113631.145:toggleSplitDirection (tkFrame)
    # The key invariant: self.splitVerticalFlag tells the alignment of the main splitter.
    
    def toggleSplitDirection (self,event=None):
        
        '''Toggle the split direction in the present Leo window.'''
        
        # Switch directions.
        c = self.c
        self.splitVerticalFlag = not self.splitVerticalFlag
        orientation = g.choose(self.splitVerticalFlag,"vertical","horizontal")
        c.config.set("initial_splitter_orientation","string",orientation)
        
        self.toggleTkSplitDirection(self.splitVerticalFlag)
    #@+node:AGP.20251128113631.146:toggleTkSplitDirection
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
        
    
        
    #@-node:AGP.20251128113631.146:toggleTkSplitDirection
    #@+node:AGP.20251128113631.147:XtoggleTkSplitDirection
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
    #@-node:AGP.20251128113631.147:XtoggleTkSplitDirection
    #@-node:AGP.20251128113631.145:toggleSplitDirection (tkFrame)
    #@+node:AGP.20251128113631.148:resizeToScreen
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
    #@-node:AGP.20251128113631.148:resizeToScreen
    #@-node:AGP.20251128113631.139:Window Menu...
    #@+node:AGP.20251128113631.149:Help Menu...
    #@+node:AGP.20251128113631.150:leoHelp
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
    #@+node:AGP.20251128113631.151:showProgressBar
    def showProgressBar (self,count,size,total):
    
        # g.trace("count,size,total:",count,size,total)
        if self.scale == None:
            #@        << create the scale widget >>
            #@+node:AGP.20251128113631.152:<< create the scale widget >>
            top = Tk.Toplevel()
            top.title("Download progress")
            self.scale = scale = Tk.Scale(top,state="normal",orient="horizontal",from_=0,to=total)
            scale.pack()
            top.lift()
            #@-node:AGP.20251128113631.152:<< create the scale widget >>
            #@nl
        self.scale.set(count*size)
        self.scale.update_idletasks()
    #@-node:AGP.20251128113631.151:showProgressBar
    #@-node:AGP.20251128113631.150:leoHelp
    #@-node:AGP.20251128113631.149:Help Menu...
    #@-node:AGP.20251128113631.122:Gui-dependent commands
    #@+node:AGP.20251128113631.153:Delayed Focus (tkFrame)
    #@+at 
    #@nonl
    # New in 4.3. The proper way to change focus is to call 
    # c.frame.xWantsFocus.
    # 
    # Important: This code never calls select, so there can be no race 
    # condition here
    # that alters text improperly.
    #@-at
    #@-node:AGP.20251128113631.153:Delayed Focus (tkFrame)
    #@+node:AGP.20251128113631.154:Tk bindings...
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
    #@-node:AGP.20251128113631.154:Tk bindings...
    #@-others
#@-node:AGP.20251128113631.32:class leoFrame
#@+node:AGP.20251128113631.155:class leoTree
class leoTree(Tk.Text):
    #@    @+others
    #@+node:AGP.20251128113631.160:vnodes status bits
    # Define the meaning of status bits in new vnodes.
    
    # Archived...
    #clonedBit   = 0x01 # True: vnode has clone mark.
    
    # not used = 0x02
    #expandedBit = 0x04 # True: vnode is expanded.
    #markedBit   = 0x08 # True: vnode is marked
    #orphanBit   = 0x10 # True: vnode saved in .leo file, not derived file.
    #selectedBit = 0x20 # True: vnode is current vnode.
    #topBit      = 0x40 # True: vnode was top vnode when saved.
    
    # Not archived...
    #dirtyBit    = 0x060
    #richTextBit = 0x080 # Determines whether we use <bt> or <btr> tags.
    #visitedBit  = 0x100
    #@nonl
    #@-node:AGP.20251128113631.160:vnodes status bits
    #@+node:AGP.20251128113631.156:__init__()
    def __init__(self,frame,parentFrame):
        
        self.frame = f = frame
        self.c = c = frame.c
        
        
        Tk.Text.__init__(self,parentFrame,wrap="none",name="treetext",cursor='arrow',padx=2,pady=2)
        self['font'] = self.option_get('font',"leotree")
        self.font = tkFont.Font(font = self['font'])
        
        self.time = 1#None
        self.nScroll = 1
        
        self.nline = 0
        self.nlist = []
        self.currentv = None
        self.current_line = 0 #1 based index
        self.lclick_done = False
        
        self.dragging = None
        
        
        self.colorizer = leoColor.colorizer(c,None)
        self.colorizer.sync_tags(self)
        
        self.bind('<Key>', leo.gui.keyHandler)
        self.bind('<Double-Button-1>',self.on_box_click)
        self.bind('<Motion>',self.void_event)
        #self.bind('<MouseWheel>',self.on_mw)
        self.bind("<MouseWheel>",frame.TopMouseWheel)
        self.bind("<Button-1>",self.on_left_click)
        self.bind("<Button-3>",self.on_right_click)
        self.bind("<Leave>",self.on_leave)
        
        self.tag_bind('box',"<Button-1>",self.on_box_click)
        
        
        self.tag_bind('icon',"<Button-1>",self.on_icon_click)
        self.tag_bind('icon',"<ButtonRelease-1>",self.on_icon_release)
        self.tag_bind('icon',"<Motion>",self.on_icon_move)
        
        self.tag_config('head',offset=3)
        self.tag_bind('head',"<Button-1>",self.on_head_click)
        self.tag_bind('head',"<Enter>",self.on_head_enter)
        self.tag_bind('head',"<Leave>",self.on_head_leave)
        
        self.tag_config('cnode',background="gray20")
        self.tag_raise('cnode')
        
        self.config(state="disabled")
        
        
        
        logBar = SCROLLBAR(parentFrame,1)#    Tk.Scrollbar(parentFrame,name="logBar")
    
        self['yscrollcommand'] = logBar.set
        logBar.command = self.yview
        logBar.pack(side="right", fill="y")
        
        logXBar = SCROLLBAR(parentFrame,0)#Tk.Scrollbar(parentFrame,name='logXBar',orient="horizontal") 
        self['xscrollcommand'] = logXBar.set 
        logXBar.command = self.xview 
        logXBar.pack(side="bottom", fill="x")
        
        self.pack(expand=1,fill='both')
        
        
        #@    @+others
        #@+node:AGP.20251128113631.157:node entry
        self.entry = Tk.Text(self,name='headentry',font=self['font'],height=1,padx=0,pady=0)
        self.entry.config(highlightthickness=1)
        #self.entry.bind('<Unmap>',self.on_entry_unmap)
        self.entry.bind('<Key>',self.on_entry_key)
        self.entry.bind('<FocusOut>',self.on_entry_focusout)
            
        self.entry_index = None
        #@nonl
        #@-node:AGP.20251128113631.157:node entry
        #@+node:AGP.20251128113631.158:Images
        self.baseimages = {}
        self.icons = {}
        
        self.iconlist = []
        self.boxlist = []
        self.branches = []
        self.imheader = []
        
        self.open_baseimages()    
        self.render_icons()
        #@nonl
        #@-node:AGP.20251128113631.158:Images
        #@+node:AGP.20251128113631.159:PopupMenuTable
        self.PopupMenuTable = [
            ("&Read @file Nodes",c.readAtFileNodes),
            ("&Write @file Nodes",c.fileCommands.writeAtFileNodes),
            #("-",None),
            #("&Tangle",c.tangle),
            #("&Untangle",c.untangle),
            #("-",None),
            #("Toggle Angle &Brackets",c.toggleAngleBrackets),
            ("-",None),
            ("Cut Node",c.cutOutline),
            ("Copy Node",c.copyOutline),
            ("&Paste Node",c.pasteOutline),
            ("&Delete Node",c.deleteOutline),
            ("-",None),
            ("&Insert Node",c.insertHeadline),
            ("&Clone Node",c.clone),
            ("Q-Link Node",self.frame.qlink.link), # agp qlink
            #("Sort C&hildren",c.sortChildren),
            #("&Sort Siblings",c.sortSiblings),
            ("-",None),
            #("Contract Parent",c.contractParent),
        ]
        #@nonl
        #@-node:AGP.20251128113631.159:PopupMenuTable
        #@-others
        
        #leo vars
        self.updateCount=0
        self.stayInTree = True
        self.redrawCount = 0
        self.canvas = self
        self._editPosition = None
        self.true_enter = False
        
        
    #@-node:AGP.20251128113631.156:__init__()
    #@+node:AGP.20251128113631.162:open_baseimages()
    def open_baseimages(self):
        
        if self.time:
            self.time = time.clock()
        
        
    
        
        leodir = g.app.leoDir
        bi = self.baseimages
        bi["box"] = Image.open(leodir+"/icons/white/box.png")
        bi["clone"] = Image.open(leodir+"/icons/white/clone.png")
        bi["content"] = Image.open(leodir+"/icons/white/content.png")
        bi["mark"] = Image.open(leodir+"/icons/white/mark.png")
        
        
        bi["minus"] = Image.open(leodir+"/icons/white/minus.png")
        bi["plus"] = Image.open(leodir+"/icons/white/plus.png")
        bi["branch"] = Image.open(leodir+"/icons/white/branch.png")
        bi["blank"] = Image.open(leodir+"/icons/white/blank.png")
        
        bi["branch0"] = Image.open(leodir+"/icons/white/branch0.png")
        bi["branch1"] = Image.open(leodir+"/icons/white/branch1.png")
        bi["branch2"] = Image.open(leodir+"/icons/white/branch2.png")
        bi["branch3"] = Image.open(leodir+"/icons/white/branch3.png")
        bi["branch4"] = Image.open(leodir+"/icons/white/branch4.png")
        bi["branch5"] = Image.open(leodir+"/icons/white/branch5.png")
        bi["branch6"] = Image.open(leodir+"/icons/white/branch6.png")
        bi["branch7"] = Image.open(leodir+"/icons/white/branch7.png")
        bi["branch8"] = Image.open(leodir+"/icons/white/branch8.png")
        bi["branch9"] = Image.open(leodir+"/icons/white/branch9.png")
        bi["branch10"] = Image.open(leodir+"/icons/white/branch10.png")
        bi["branch11"] = Image.open(leodir+"/icons/white/branch11.png")
        
        if self.time:
            print "OpenImages",time.clock()-self.time,"seconds"
    #@-node:AGP.20251128113631.162:open_baseimages()
    #@+node:AGP.20251128113631.163:render_icons()
    def render_icons(self):
        
        if self.time:
            self.time = time.clock()
        
        bi = self.baseimages
    
        sampling = Image.LANCZOS #= Image.NEAREST
        
        
        #@    @+others
        #@+node:AGP.20251128113631.164:Icons
        contentcolor = Image.new('RGBA', (128,64), g.theme['string'] or '#00DDFFFF')
        markcolor = Image.new('RGBA', (128,64), g.theme['accent'] or '#FF0000FF')
        clonecolor = Image.new('RGBA', (128,64), g.theme['keyword'] or '#FF0000FF')
        dirtycolor =  Image.new('RGBA', (128,64), g.theme['dirty'] or '#808080FF')
        
        fgcolor  =  Image.new('RGBA', (128,64), g.theme['fg'])
        bgcolor  =  Image.new('RGBA', (128,64), g.theme['bg'])
        
        
        box = bi["box"] #Image.open(leodir+"/icons/white/box.png")
        
        box_dirty =  Image.composite(dirtycolor,bgcolor,box)
        box =  Image.composite(fgcolor,bgcolor,box)
        
        
        clone = bi["clone"] #Image.open(leodir+"/icons/white/clone.png")
        clone =  Image.composite(clonecolor,clone,clone)
        
        content = bi["content"] #Image.open(leodir+"/icons/white/content.png")
        content =  Image.composite(contentcolor,content,content)
        
        mark = bi["mark"] #Image.open(leodir+"/icons/white/mark.png")
        mark =  Image.composite(markcolor,mark,mark)
        
        ih = int(self.font['size'] )
        iw = ih*2
        
        iconlist = self.iconlist = []
        
        #@+others
        #@-others
        
        for i in range(16):
            #print "icon",i
            if i & 8:
                im = box
            else:
                im = box_dirty
                
            
            if i & 1:
                im = Image.alpha_composite(im,content)
                
            if i & 2:
                im = Image.alpha_composite(im,mark)
            
            if i & 4:
                im = Image.alpha_composite(im,clone)
            
            im = im.resize( (iw, ih),sampling ) 
            #im.save(leodir+"/icons/box%02d.png" %i)
            iconlist.append( ImageTk.PhotoImage(im) )
            #self.icons["box%02d.png" % i] = ImageTk.PhotoImage(im)
        
        
        
        
        
        
        #@-node:AGP.20251128113631.164:Icons
        #@+node:AGP.20251206211840:branches
        #-----------------------------------------------------------------
        ih = int(self.font['size'] *2)
        iw = ih
        
        fgcolor  =  Image.new('RGBA', (128,128), g.theme['dirty'])
        bgcolor  =  Image.new('RGBA', (128,128), g.theme['bg'])
        
        png = bi["minus"] #Image.open(leodir+"/icons/white/minusnode.png")
        nodesize = (png.width,png.height)
        
        dirtyboxcolor =  Image.new('RGBA', nodesize, g.theme['fg'])
        
        #minus =  Image.composite(fgcolor,bgcolor,png).resize( (ih,ih),Image.LANCZOS )
        dirty_minus =  Image.composite(dirtyboxcolor,png,png)#.resize( (ih,ih),Image.LANCZOS )
        
        png = bi["plus"] #Image.open(leodir+"/icons/white/plusnode.png")
        dirty_plus =  Image.composite(dirtyboxcolor,png,png)#.resize( (ih,ih),Image.LANCZOS )
        #dirty_plus.save("C:\Users\izaqu\Desktop\dirty_plus.png")
        
        br = bi["branch"]
        br =  Image.composite(fgcolor,bgcolor,br).resize( (iw, ih),sampling )
        self.icons["branch"] = ImageTk.PhotoImage(br)
        
        br = bi["blank"]
        br =  Image.composite(fgcolor,bgcolor,br).resize( (iw, ih),sampling )
        self.icons["blank"] = ImageTk.PhotoImage(br)
        
        branches = self.branches = []
        
        for i in range(20):
            if i > 11: #child dirty
                j = i-8
                br = bi["branch%i" % j]
                br = Image.composite(fgcolor,bgcolor,br)
            
                if j < 8: #plus
                    br = Image.composite(dirty_plus,br,dirty_plus)
                else: #minus
                    br = Image.composite(dirty_minus,br,dirty_minus)
                    
                br =  br.resize( (iw, ih),sampling )
                
            else:
                br = bi["branch%i" % i]
                br =  Image.composite(fgcolor,bgcolor,br).resize( (iw, ih),sampling )
                
            branches.append( ImageTk.PhotoImage(br) )
        #@-node:AGP.20251206211840:branches
        #@-others
        
        
        
        
        if self.time:
            print "Render Icons:",time.clock()-self.time,"seconds"
    #@nonl
    #@-node:AGP.20251128113631.163:render_icons()
    #@+node:AGP.20251128113631.165:node_to_line()
    def node_to_line(self,v):
        try:
            return self.nlist.index(v)+1
        except:
            return 0
        
        """nid = str(id(v))
        
        for i in range(1,int(self.index('end').split('.')[0])):
            m = self.mark_next('%i.0' % i)
            
            if m == nid:
                return i
        
        return 0"""
    #@nonl
    #@-node:AGP.20251128113631.165:node_to_line()
    #@+node:AGP.20251128113631.166:node_render()
    def node_render(self,v,nline,nlist=None,single=False,text=None):
        
        if nlist != None:
            nlist.append(v)
        
        if not text: text = self
        
        #nline = self.nline
        nim = 0
        isfirst = islast =  False
        
        branch = 0
        icons = self.icons
        
        text.insert("end"," ",())
        nim += 1
        
        linend = "%i.end" % nline
        
        
        
        if not single:
        
            if not v._back and not v._parent:
                isfirst = True
                branch |= 1
        
            if not v._next:
                islast = True
                branch |= 2
            
            for im in self.imheader:
                text.image_create("end",image=im)
                nim +=1
            
            child = v.t._firstChild
            
            if child:
                if v.statusBits & 0x04: #.isExpanded():
                    branch |= 8
                else:
                    branch |= 4
                    
                    
                statusBits = v.statusBits
            
                if ( v.statusBits & v.childdirtyBit ) != 0:#p.ischildDirty():
                    branch += 8
        
            text.image_create("end", image=self.branches[ branch ] )
            nim += 1
        
            if child:
                text.tag_add('box',"%i.%i" % (nline,nim-1), linend)
            
              
        text.image_create("end", image=self.iconlist[ v.computeIcon() ],align='center' )
        nim += 1
        
        text.tag_add('icon',"%i.%i" % (nline,nim-1), linend)
        
        text.insert("end",v.headString())
        text.tag_add('head',"%i.%i" % (nline,nim), linend)
        
        if v == self.current_v and text == self:
            self.tag_add('cnode',"%i.%i" % (nline,nim), linend+"+1c")
            if self.scroll:
                self.scroll_line = nline
                #print "drawscroll"
                self.yview_scroll(nline, 'units')
                #self.see("insert")
        
        text.mark_set("%i" % id(v),"%i.0" % nline)
        text.insert("%i.end" % nline,"\n")
        
        self.colorizer.colorize_headline(position(v),text,nline,scan_parents=single)
        
        nline += 1
        
        #draw children
        if not single:
            if v.t._firstChild and v.statusBits & 0x04: #.isExpanded():
                if islast:
                    self.imheader.append(icons['blank'])
                else:
                    self.imheader.append(icons['branch'])
            
                #child = v.t._firstChild
                while child:
                    nline = text.node_render(child,nline,nlist)
                    child = child._next
                
                
                self.imheader.pop(-1)
            
        return nline
        
        
    #@-node:AGP.20251128113631.166:node_render()
    #@+node:AGP.20251128113631.171:node_from_mouse()
    def node_from_mouse(self):
        
        x,y = self.winfo_pointerxy()
        x = x - self.winfo_rootx()
        y = y - self.winfo_rooty()
        
        line = int(self.index("@%i,%i" % (x,y) ).split(".")[0])-1
        return self.nlist[line]
        
        
        #nid = self.mark_previous(index)
        #while nid in ('insert','tk::anchor1'):
        #    nid = self.mark_previous(nid)
        
        #return _ctypes.PyObj_FromPtr(int(nid))
    #@-node:AGP.20251128113631.171:node_from_mouse()
    #@+node:AGP.20251207163021:node_from_index()
    def node_from_index(self,index = 'current'):    
        line = int(self.index(index ).split(".")[0])-1
        
        nlist = self.nlist
        if line < len(self.nlist):
            return self.nlist[line]
        
        return None
        
        #nid = self.mark_previous(index)
        #while nid in ('insert','tk::anchor1'):
        #    nid = self.mark_previous(nid)
        #
        #return _ctypes.PyObj_FromPtr(int(nid))
    #@-node:AGP.20251207163021:node_from_index()
    #@+node:AGP.20251128113631.167:node_expand_to()
    def node_expand_to(self,v):
        
        '''Expand all ancestors without redrawing.
        
        Return a flag telling whether a redraw is needed.'''
        
        redraw_flag = False
        if v:
            v = v._parent
        
        while v:
            if not v.isExpanded():
                v.expand()
                redraw_flag = True
            v = v._parent
            
                
        
        return redraw_flag
        
    #@nonl
    #@-node:AGP.20251128113631.167:node_expand_to()
    #@+node:AGP.20251128113631.168:clear()
    def clear(self):
        self.delete('1.0','end')
        
        for m in self.mark_names():
            self.mark_unset(m)
            
        self.nline = 1
        self.imheader = [] #[self.icons['branch3']]
    #@-node:AGP.20251128113631.168:clear()
    #@+node:AGP.20251128113631.169:render() - redraw_now
    def render(self,scroll=False):
        
        if self.time:
            self.time = time.clock()
        
        
        c = self.c ;
        
        self.scroll = scroll
        if not scroll:
            self.save_scroll()
        
        self.current_v = c.currentPosition().v
        
    
        if True:# not g.doHook("redraw-entire-outline",c=c):
            
            c.setTopVnode(None)
            
            self.config(state="normal")
            
            #self.clear()
            self.delete('1.0','end')
        
            for m in self.mark_names():
                self.mark_unset(m)
            
            nlist = self.nlist = []
            nline = 1
            self.imheader = [] #[self.icons['branch3']]
            
            if c.hoistStack:
                v_node = c.hoistStack[-1].p.v
                
            else:
                v_node = c.rootPosition().v
            
            
            while v_node:
                nline = self.node_render(v_node,nline,self.nlist)
                
                v_node = v_node._next
            
            self.config(state="disabled")
                
        #g.doHook("after-redraw-outline",c=c)
        
        #nline = self.node_to_line(self.current_v)
        #if nline != 0:
        #    hs = self.tag_nextrange("head", "%i.0" % nline)[0]
        #    self.tag_add('cnode',hs, "%i.end+1c" % nline)
                    
        """if text == self and v == self.current_v:
            self.tag_add('cnode',"%i.%i" % (nline,nim), linend)
            if self.scroll:
                self.scroll_line = nline
                #print "drawscroll"
                self.yview_scroll(nline, 'units')
                #self.see("insert")"""
    
        if not scroll:
            self.load_scroll()
        
        c.masterFocusHandler()
        
        if self.time:
            print "Redraw Tree",time.clock()-self.time,"seconds"
        
    redraw_now = redraw = render# Compatibility
    #@-node:AGP.20251128113631.169:render() - redraw_now
    #@+node:AGP.20251128113631.170:select()
    def select(self,p,updateBeadList=True,v=None):
        #import traceback ; traceback.print_stack()
        
        
        c = self.c
        self.end_edit()
        
        if not v:
            if not p:
                return
            v = p.v
        else:
            p = position(v)
        
        c = self.c
        frame = c.frame
        body = frame.bodyCtrl
        
        old_v = self.currentv #c.currentPosition()
        #print p.v,old_p.v
        
        
        if p.v != old_v:
            old_p = position(self.currentv)
            self.currentv = p.v
            
            self.tag_remove('cnode','1.0','end')
            
            #self.current_v = v
            
            
            if not g.doHook("unselect1",c=c,new_p=p,old_p=old_p,new_v=p,old_v=old_p):
                if old_v:
    
                    old_v.t.scrollBarSpot = body.yview()
                    old_v.t.insertSpot = frame.body.getInsertionPoint()
    
            
            g.doHook("unselect2",c=c,new_p=p,old_p=old_p,new_v=p,old_v=old_p)
            
            
            if not g.doHook("select1",c=c,new_p=p,old_p=old_p,new_v=p,old_v=old_p):
                # Bug fix: we must always set this, even if we never edit the node.
                self.revertHeadline = p.headString()
                #frame.setWrap(p)
                
                # Always do this.  Otherwise there can be problems with trailing hewlines.
                s = g.toUnicode(p.v.t.bodyString,"utf-8")
                #self.setText(0,body,s)
                body.delete('1.0','end')
                body.insert('1.0',s)
    
                # We must do a full recoloring: we may be changing context!
                frame.body.recolor_now(p) # recolor now uses p.copy(), so this is safe.
    
                if v.t.scrollBarSpot != None:
                    first,last = v.t.scrollBarSpot
                    body.yview("moveto",first)
    
                if v.t.insertSpot != None:
                    body.mark_set("insert",v.t.insertSpot)
                    body.see(v.t.insertSpot)
                else:
                    body.mark_set("insert","1.0")
            
            
            
            c.setCurrentPosition(p)###
            
            if hasattr(p.t,"mod"):
                mod = p.t.mod.split(".")
                if len(mod) >1:
                    ts = mod[1]
                    ms = "  modified by %s on %s/%s/%s at %s:%s:%s" % (mod[0],ts[6:8],ts[4:6],ts[0:4],ts[8:10],ts[10:12],ts[12:14])
                    c.frame.StatusLabel.config(text=ms)
                else:
                    c.frame.StatusLabel.config(text="")
            else:
                c.frame.StatusLabel.config(text="")
            
            g.doHook("select2",c=c,new_p=p,old_p=old_p,new_v=p,old_v=old_p)
            g.doHook("select3",c=c,new_p=p,old_p=old_p,new_v=p,old_v=old_p)
            
            if self.node_expand_to(v): #need_redraw
                self.redraw()
            
            else:       #simply set the selection tag, for clones too
                #nline = self.node_to_line(v)
                nline = 0
                while 1:
                    try:
                        nline = self.nlist.index(v,nline) + 1 # raise ValueError when not found
                        hs = self.tag_nextrange("head", "%i.0" % nline)[0]
                        self.tag_add('cnode',hs, "%i.end+1c" % nline)
                        
                    except:
                        break
                
                """
                if nline != 0:
                    hs = self.tag_nextrange("head", "%i.0" % nline)[0]
                    self.tag_add('cnode',hs, "%i.end+1c" % nline)
                    
                
                else:
                    self.redraw(scroll=False)
                    
                """
    #@nonl
    #@-node:AGP.20251128113631.170:select()
    #@+node:AGP.20251128113631.172:begin_edit()
    def begin_edit(self,v,nline=None):
        print "begin_edit()"
        self.end_edit()
        
        if not nline:
            nline = self.node_to_line(v)
            
        if nline != 0:
                
            self.config(state="normal") #--------------------------
            
            linestart, linend = "%i.0" % nline, "%i.end" % nline
            range =  self.tag_nextrange('head', linestart, linend)
            self.old_headline = oh = self.get(*range)
                
            self.delete(*range)
            entry = self.entry
            entry.delete("1.0",'end')
            #entry.insert("1.0",oh)
            entry.insert("1.0",oh)
            entry.config(width=len(oh)+1)
            self.window_create(range[0],window = entry)
            entry.focus_set()
            
            self.config(state="disabled") #-------------------------
            
            self.edit_vnode = v
            self.entry_index = range[0]
            self.entry_line = nline
            print "begin_edit(2)",range[0],oh
                
            
    #@nonl
    #@-node:AGP.20251128113631.172:begin_edit()
    #@+node:AGP.20251128113631.173:end_edit()
    def end_edit(self):
        
        if self.entry_index:    #already editing
            print "end_edit()"
            self.config(state="normal") #--------------------------
            #print self.window_names()
            
            #new_headline = self.entry.get("1.0","end")
            new_headline = self.entry.get("1.0","1.end")
            #self.entry.delete(0,'end')
            self.entry.delete("1.0",'end')
            
            self.tag_remove('cnode','1.0','end')
            self.window_configure(self.entry_index,window='')
            self.insert(self.entry_index,new_headline)
            
            self.tag_add('head',self.entry_index,"%i.end" % self.entry_line)
            self.tag_add('cnode',self.entry_index, "%i.end+1c" % self.entry_line)
            
            self.colorizer.colorize_headline(position(self.edit_vnode),self,self.entry_line)
            self.config(state="disabled") #-------------------------
            
            self.entry_index = None
            
            
            #old OnHeadChanged
            if new_headline != self.old_headline:
                print "onheadchanged"
                c = self.c ; u = c.undoer
                undoType='Typing'
                ch = "\r"
                p = position(self.edit_vnode)
                
                p.setHeadString(new_headline) #because it setDirty()
                
                
                if g.doHook("headkey1",c=c,p=p,v=p,ch=ch):
                    return # The hook claims to have handled the event.
                
                undoData = u.beforeChangeNodeContents(p,oldHead=self.old_headline)
                
                if not c.changed:
                    c.setChanged(True)
                
                
                dirtyVnodeList = p.setDirty()
                u.afterChangeNodeContents(p,undoType,undoData,dirtyVnodeList=dirtyVnodeList)
                
                g.doHook("headkey2",c=c,p=p,v=p,ch=ch)
            
                #agp qlink
                """
                if g.qlinks != None:
                    for k in g.qlinks.keys():
                        if k == p:
                            qlink = g.qlinks[k]
                            head = 4*' '+p.v.headString()+30*' '
                            headw = qlink.font.measure(head)
                            qlink.itemconfigure(qlink.qtextid,text=head)
                            qlink.coords(qlink.qtextid,headw/2,qlink.midh)
                """
            
        
                #agp
           
                if self.true_enter:# and not self.stayInTreeAfterEditHeadline:
                    self.frame.body.focus_force()
                    #c.bodyWantsFocusNow()
                
                self.redraw_now(scroll=False)
                
            self.frame.body.focus_set()
            self.true_enter = False
    #@nonl
    #@-node:AGP.20251128113631.173:end_edit()
    #@+node:AGP.20260501152354:Getters/Setters (tree)
    def getEditTextDict(self,v):
        # New in 4.2: the default is an empty list.
        return self.edit_text_dict.get(v,[])
    
    def editPosition(self):
        return self._editPosition
    
    def setEditPosition(self,p):
        self._editPosition = p
    #@-node:AGP.20260501152354:Getters/Setters (tree)
    #@+node:AGP.20260414195137:editPosition()
    def editPosition(self):
        return position(self.currentv)
    #@nonl
    #@-node:AGP.20260414195137:editPosition()
    #@+node:AGP.20260414200317:edit_widget(p)
    def edit_widget(self,p):
        """Returns the Tk.Edit widget for position p."""
        #self.begin_edit(p.v)
        return self
    #@nonl
    #@-node:AGP.20260414200317:edit_widget(p)
    #@+node:AGP.20251128113631.174:save_scroll()
    def save_scroll(self):
        self.scroll_fraction =  (int(self.index('end').split('.')[0])-1) * self.yview()[0]
    #@nonl
    #@-node:AGP.20251128113631.174:save_scroll()
    #@+node:AGP.20251128113631.175:load_scroll()
    def load_scroll(self):
        new_fract = self.scroll_fraction / (int(self.index('end').split('.')[0])-1) *0.993       
        self.yview_moveto(new_fract)
    #@-node:AGP.20251128113631.175:load_scroll()
    #@+node:AGP.20251128113631.176:Events
    #@+node:AGP.20251128113631.188:on_box_click()
    def on_box_click(self,event,p=None): #also bound to double left click
        print "boxclick"
        
        self.end_edit()
        c = self.c ; p1 = c.currentPosition()
        
        if not p:
            #nid = self.mark_previous('current')
            #while nid in ('insert','tk::anchor1'):
            #    nid = self.mark_previous(nid)
            #v = _ctypes.PyObj_FromPtr(int(nid))
            v = self.node_from_index()
            if not v:
                return "break"
            p = position(v)
        else:
            v = p.v
        
        c.setLog()
        
        self.save_scroll()
        
        #print v_node,c.hoistStack,c.rootPosition().v
        #print c.rootPosition().v
        c.beginUpdate()
        try:
            if not g.doHook("boxclick1",c=c,p=p,v=p,event=event):
        
                if v != c.currentPosition().v:
                    #self.end_edit()
                    
                    
                    self.select(None,v=v)
                    
                if p.isExpanded():
                    p.contract()
                else:
                    p.expand()
                    
        
                if self.stayInTree:
                    c.treeWantsFocus()
                else:
                    c.bodyWantsFocus()
            
            #g.doHook("boxclick2",c=c,p=p,v=p,event=event)
            
        except Exception,e:
            print e
        c.endUpdate(scroll=False)
        self.load_scroll()
        
        self.lclick_done = True
        return "break"
            
    
    #@-node:AGP.20251128113631.188:on_box_click()
    #@+node:AGP.20251128113631.186:on_entry_key()
    def on_entry_key(self,event):
        #print event.char
        #print event.keysym
        print event.keysym
        if event.char == "\r":
            self.true_enter = True
            self.end_edit()
            #print "return"
        else:#if event.char in string.printable:
            self.entry.config(width=len(self.entry.get())+2)
        
    #@nonl
    #@-node:AGP.20251128113631.186:on_entry_key()
    #@+node:AGP.20260413085305:on_entry_focusout()
    def on_entry_focusout(self,event):
        self.end_edit()
    
        
    #@nonl
    #@-node:AGP.20260413085305:on_entry_focusout()
    #@+node:AGP.20251128113631.185:on_entry_unmap()
    def on_entry_unmap(self,event):
        head_txt = self.entry.get()
        
        self.config(state="normal") #--------------------------
                
                
        self.insert(self.entry_index,head_txt)
        self.entry_index = None    
                
        self.config(state="disabled") #-------------------------
        
        
        print 'unmap'
    #@nonl
    #@-node:AGP.20251128113631.185:on_entry_unmap()
    #@+node:AGP.20251128113631.179:on_head_enter()
    def on_head_enter(self,event):
        self.config(cursor="xterm")
    #@nonl
    #@-node:AGP.20251128113631.179:on_head_enter()
    #@+node:AGP.20251128113631.180:on_head_leave()
    def on_head_leave(self,event):
        self.config(cursor="arrow")
    #@nonl
    #@-node:AGP.20251128113631.180:on_head_leave()
    #@+node:AGP.20251128113631.181:on_head_click()
    def on_head_click(self,event):
        
        c = self.c
        
        #print "on_head_click"
        #nid = self.mark_previous('current')
        #while nid in ('insert','tk::anchor1'):
        #    nid = self.mark_previous(nid)
        #v = _ctypes.PyObj_FromPtr(int(nid))
        v = self.node_from_index()
        
        
        if v != c.currentPosition().v:
            
            self.end_edit()
            
            self.select(None,v=v)
        
        else: # edit label
            nline = int(self.index('current' ).split(".")[0])
            self.begin_edit(v,nline)
                
        self.lclick_done = True
        return 'break'
    #@nonl
    #@-node:AGP.20251128113631.181:on_head_click()
    #@+node:AGP.20251128113631.182:on_head_changed()
    def on_head_changed():
        pass
    #@nonl
    #@-node:AGP.20251128113631.182:on_head_changed()
    #@+node:AGP.20251128113631.183:onHeadChanged
    # Tricky code: do not change without careful thought and testing.
    
    def onHeadChanged (self,p,undoType='Typing'):
        #print "onHeadChanged()",undoType
        '''Officially change a headline.
        Set the old undo text to the previous revert point.'''
        
        c = self.c
        u = c.undoer
        w = c.edit_widget(p)
        
        if not w: return
        
        s = w.get('1.0','end')
        #@    << truncate s if it has multiple lines >>
        #@+node:AGP.20251128113631.184:<< truncate s if it has multiple lines >>
        # Remove one or two trailing newlines before warning of truncation.
        for i in (0,1):
            if s and s[-1] == '\n':
                if len(s) > 1: s = s[:-1]
                else: s = ''
        
        # Warn if there are multiple lines.
        i = s.find('\n')
        if i > -1:
            # g.trace(i,len(s),repr(s))
            g.es("Truncating headline to one line",color="blue")
            s = s[:i]
        
        limit = 1000
        if len(s) > limit:
            g.es("Truncating headline to %d characters" % (limit),color="blue")
            s = s[:limit]
        
        s = g.toUnicode(s or '',g.app.tkEncoding)
        #@-node:AGP.20251128113631.184:<< truncate s if it has multiple lines >>
        #@nl
        
        #changed = s != self.revertHeadline
        if s != self.revertHeadline:    #agp avoid generating false events
        
            ch = '\r' # New in 4.4: we only report the final keystroke.
            if g.doHook("headkey1",c=c,p=p,v=p,ch=ch):
                return # The hook claims to have handled the event.
        
        
            c.beginUpdate()
        
            try:
                # Make the change official, but undo to the *old* revert point.
                oldRevert = self.revertHeadline
                changed = s != oldRevert
                
                self.revertHeadline = s
                p.initHeadString(s)
                
                if changed:
                    undoData = u.beforeChangeNodeContents(p,oldHead=oldRevert)
                    if not c.changed: c.setChanged(True)
                    dirtyVnodeList = p.setDirty()
                    u.afterChangeNodeContents(p,undoType,undoData,dirtyVnodeList=dirtyVnodeList)
            finally:
                c.endUpdate(scroll=False) # New in 4.4.1
                
                if changed:    #agp moded and put at end of func
                    if self.stayInTreeAfterEditHeadline:
                        c.treeWantsFocus()
                #    else:
                #        c.bodyWantsFocusNow()
        
                    
            g.doHook("headkey2",c=c,p=p,v=p,ch=ch)
            
            #agp qlink
            if g.qlinks != None:
                for k in g.qlinks.keys():
                    if k == p:
                        qlink = g.qlinks[k]
                        head = 4*' '+p.v.headString()+30*' '
                        headw = qlink.font.measure(head)
                        qlink.itemconfigure(qlink.qtextid,text=head)
                        qlink.coords(qlink.qtextid,headw/2,qlink.midh)
        
        else: #agp
            c.beginUpdate()
            c.endUpdate(scroll=False)
        
        #agp
           
        if self.true_enter and not self.stayInTreeAfterEditHeadline:
            c.bodyWantsFocusNow()
        #else:
        #    c.treeWantsFocus()
                
        self.true_enter = False
    #@-node:AGP.20251128113631.183:onHeadChanged
    #@+node:AGP.20251128113631.187:on_icon_click()
    def on_icon_click(self,event):
        #print 'iconclick'
        c = self.c
        
        self.dragging = True
        #nid = self.mark_previous('current')
        #while nid in ('insert','tk::anchor1'):
        #    nid = self.mark_previous(nid)
        #v = _ctypes.PyObj_FromPtr(int(nid))
        v = self.node_from_index()
        
        if v != c.currentPosition().v:
            #self.end_edit()
            self.select(None,v=v)
        
        
        self.lclick_done = True
        
        return 'break'
    #@nonl
    #@-node:AGP.20251128113631.187:on_icon_click()
    #@+node:AGP.20251207113533:on_icon_release()
    def on_icon_release(self,e):
        self.config(cursor = 'arrow')
        dragged = self.dragging
        self.dragging = None
        if dragged != None and dragged != True:
            target = self.node_from_mouse()#'@%i,%i' % (e.x,e.y) )
            
            dragged = position(dragged)
            target = position(target)
            
            if target == dragged:
                return "break"
    
            #print "moving",dragged
            #print "after",target
            
            childFlag = target.hasChildren() and target.isExpanded()
            
            c = self.c
            if e.state & 0x0004:# 	Control # Clone p and move the clone.
                if childFlag:
                    c.dragCloneToNthChildOf(dragged,target,0)
                else:
                    c.dragCloneAfter(dragged,target)
            else: # Just drag p.
                if childFlag:
                    c.dragToNthChildOf(dragged,target,0)
                else:
                    c.dragAfter(dragged,target)
            
            self.render()
            
        
        
        return "break"
    #@nonl
    #@-node:AGP.20251207113533:on_icon_release()
    #@+node:AGP.20251207113645:on_icon_move()
    def on_icon_move(self,e):
        if self.dragging == True:
            self.config(cursor = 'hand2')
            print "setnode"
            self.dragging = self.node_from_index()#'@%i,%i' % (e.x,e.y) )
        
        #if self.dragging:
        #    print self.mouse_to_vnode('@%i,%i' % (e.x,e.y) )
        
        return "break"
    #@nonl
    #@-node:AGP.20251207113645:on_icon_move()
    #@+node:AGP.20251207135750:on_leave()
    def on_leave(self,event):
        self.dragging = None
        self.config(cursor = 'arrow')
    #@nonl
    #@-node:AGP.20251207135750:on_leave()
    #@+node:AGP.20251128113631.189:on_right_click()
    def on_right_click(self,e):
            
        
        txt_width = 200
        
        e.widget.focus()
        
        v = self.node_from_index()
        
        self.select(None,v=v)
                    
        rmenu = Tk.Menu(None,tearoff=0,takefocus=0)
        for (txt,cmd) in self.PopupMenuTable:
            if txt == '-':
                rmenu.add_separator()
            else:
                sclist = self.c.config.getShortcut(txt)[1]
                
                
                
                if sclist and len(sclist) > 0:
                    #print sclist[0].val
                    shortcut = sclist[0].val
                    rmenu.add_command(label=txt,accelerator=shortcut,command=cmd)
                else:
                    rmenu.add_command(label=txt,command=cmd)
            
        
        rmenu.tk_popup(e.x_root+1,e.y_root-10)
        #rmenu.post(e.x_root+1,e.y_root-10)
        
        return False
    #@nonl
    #@-node:AGP.20251128113631.189:on_right_click()
    #@+node:AGP.20251205095103:on_left_click()
    def on_left_click(self,e):
        #c = self.c ; p1 = c.currentPosition()
        #print "on_left_click"
        if not self.lclick_done:
            v = self.node_from_index()
            if v :
                self.select(None,v=v)
        
        self.lclick_done = False
    #@nonl
    #@-node:AGP.20251205095103:on_left_click()
    #@+node:AGP.20251128113631.178:on_mw
    def on_mw(self,event):
        start,end = self.yview()
        nline = int(self.index('end').split('.')[0])
        print nline*start,nline*end
    #@nonl
    #@-node:AGP.20251128113631.178:on_mw
    #@+node:AGP.20251128113631.190:on_zoom()
    def on_zoom(self,delta):
        #print "canvas onzoom"
        w = self
        
        try:
            f = tkFont.Font(name=w.cget("font"))
        except:
            f = tkFont.Font(name=w.cget("font"),exists=True)
                
        fdic = f.actual()
                
        if delta < 1:
            fdic['size'] += 1
        else:
            fdic['size'] -= 1
                
        self.font = w.fontref = tkFont.Font(**fdic)
        w.config(font=w.fontref)
        
        
        self.render_icons()
        
        #self.c.redraw_now()
        self.redraw_now()
        #self.drawTopTree()
    #@nonl
    #@-node:AGP.20251128113631.190:on_zoom()
    #@+node:AGP.20251128113631.177:void_event
    def void_event(self,event):
        return 'break'
    #@nonl
    #@-node:AGP.20251128113631.177:void_event
    #@-node:AGP.20251128113631.176:Events
    #@+node:AGP.20251128113631.191: Must be defined in subclasses
    #@+node:AGP.20251128113631.192:setHeadline()
    def setHeadline (self,p,s):
        
        '''Set the actual text of the headline widget.
        
        This is called from the undo/redo logic to change the text before redrawing.'''
        
        w = self.entry
        if w:
            w.configure(state='normal')
            w.delete(0,'end')
            if s.endswith('\n') or s.endswith('\r'):
                s = s[:-1]
            w.insert(0,s)
            self.revertHeadline = s
            # g.trace(repr(s),w.get('1.0','end'))
        else:
            g.trace('-'*20,'oops')
    #@-node:AGP.20251128113631.192:setHeadline()
    #@+node:AGP.20251128113631.193:OnDeactivate
    def OnDeactivate (self,event=None):
        
        pass
    #@nonl
    #@-node:AGP.20251128113631.193:OnDeactivate
    #@+node:AGP.20251128113631.194:Colors & Fonts
    def setColorFromConfig (self):
        self.oops()
    
    def getFont(self):
        self.oops()
        
    def setFont(self,font=None,fontName=None):
        self.oops()
        
    def setFontFromConfig (self):
        self.oops()
    #@-node:AGP.20251128113631.194:Colors & Fonts
    #@+node:AGP.20251128113631.195:Drawing
    def drawIcon(self,v,x=None,y=None):
        self.oops()
    
    #def redraw_now(self,scroll=True):
    #    self.oops()
    #@-node:AGP.20251128113631.195:Drawing
    #@+node:AGP.20251128113631.196:Edit label
    def editLabel (self,p,selectAll=False):
        self.begin_edit(p.v)
    
    def endEditLabel(self):
        self.end_edit()
    
    def setEditLabelState(self,v,selectAll=False):
        
        self.oops()
    #@-node:AGP.20251128113631.196:Edit label
    #@+node:AGP.20251128113631.197:Scrolling
    def scrollTo(self,p):
        self.oops()
        
    idle_scrollTo = scrollTo # For compatibility.
    #@-node:AGP.20251128113631.197:Scrolling
    #@+node:AGP.20251128113631.198:Tree operations
    def expandAllAncestors(self,v):
        
        self.oops()
    #@-node:AGP.20251128113631.198:Tree operations
    #@+node:AGP.20251128113631.199:setBindings()
    def setBindings(self):
        pass
        #frame = self.frame ; c = self.c ; k = c.k
        
        #self.entry.bind('<Key>', k.masterKeyHandler)
    #@-node:AGP.20251128113631.199:setBindings()
    #@+node:AGP.20251128113631.200:oops
    def oops(self):
        
        print "leoTree oops:", g.callers(), "should be overridden in subclass"
    #@-node:AGP.20251128113631.200:oops
    #@+node:AGP.20251128113631.203:destroy()
    def destroy(self):
        """ crash the closing process if not implemented """
        pass
    #@nonl
    #@-node:AGP.20251128113631.203:destroy()
    #@-node:AGP.20251128113631.191: Must be defined in subclasses
    #@+node:AGP.20251128113631.201:beginUpdate()
    def beginUpdate (self):
        
        self.updateCount += 1
        # g.trace('tree',id(self),self.updateCount,g.callers())
        
    
    #@-node:AGP.20251128113631.201:beginUpdate()
    #@+node:AGP.20251128113631.202:endUpdate()
    def endUpdate (self,flag,scroll=False):
        
        self.updateCount -= 1
        # g.trace(self.updateCount,'scroll',scroll,g.callers())
        
        if self.updateCount <= 0:
            
            #check is se
            
            
            if flag:
                self.redraw_now(scroll=scroll)
            
            if not scroll:  
                self.see(str(self.node_to_line(self.currentv))+".0")
                
                
            if self.updateCount < 0:
                g.trace("Can't happen: negative updateCount",g.callers())
    #@nonl
    #@-node:AGP.20251128113631.202:endUpdate()
    #@-others
#@nonl
#@-node:AGP.20251128113631.155:class leoTree
#@+node:AGP.20251128113631.204:class leoQlink
class leoQlink(Tk.Text):
    #@    @+others
    #@+node:AGP.20251128113631.205:__init__()
    def __init__(self,f,parentFrame):
        
        self.frame = f
        
        
        Tk.Text.__init__(self,parentFrame,wrap="none",name="treetext",cursor='arrow',height = 0,padx=2,pady=2)
        self['font'] = self.option_get('font',"treetext")
        self.font = tkFont.Font(font = self['font'])
        
        self.colorizer = leoColor.colorizer(f.c,None)
        self.colorizer.sync_tags(self)
        #print 'qlink height',self['height']
        #self.pack(expand=0)#,fill='both')
        
        self.links = []
        
        self.bind("<Button-3>",self.on_right_click)
        
        leo.add_hook("open2",self.after_open_file)
        
        
        
    #@nonl
    #@-node:AGP.20251128113631.205:__init__()
    #@+node:AGP.20251205183122:after_open_file()
    def after_open_file(self,*args,**keywords):
        self.scan()
    #@nonl
    #@-node:AGP.20251205183122:after_open_file()
    #@+node:AGP.20251205183411:scan()
    def scan(self,node=None):    #agp qlink
        
        for p in self.frame.c.all_positions_iter():#node.children_iter():
            v = p.v
            
            if hasattr(v,"unknownAttributes"):
                if "qlink" in v.unknownAttributes:
                    print 'qlink add attr'
                    self.link(p=p,force=True)
                    
            #self.qlink_scan(p)
            
        
    #@nonl
    #@-node:AGP.20251205183411:scan()
    #@+node:AGP.20251128113631.206:link()
    def link(self,event=None,p=None,force=False):    #agp qlink
        
        
        if not p:
            p = self.frame.c.currentPosition()
        
        v = p.v
        
        #if g.qlinks == None: g.qlinks = {}
        
        if v not in self.links or force:
            
            print 'qlink'
            
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
            
            import tkFont
            
            font_height = tkFont.Font(font=font).metrics('linespace')
            height=font_height+2
            midh = height/2+1
            
            
            head = v.headString()
            headw = font.measure(head)
            
            
            print "len " ,len(self.links)
            self.frame.tree.node_render(v, len(self.links)+1, self.links, single=True, text=self)
            
            
            self.config( height = len(self.links) )
            
            if len(self.links) == 1:
                self.pack(expand=1,fill='both')
                print "pack"
            #print 'add qlink',v,ua["qlink"]
        
        else: # remove qlink
            
            print 'unlink'
            del v.unknownAttributes['qlink']
            line = self.links.index(v)+1
            
            self.config(state="normal")
            self.delete( "%i.0"%line,"%i.end+1c"%line)
            self.config(state="normal")
            
            self.links.remove(v)
            
            if len(self.links) == 0:
                self.pack_forget()
            else:
                self.config( height = len(self.links) )
            
            
    #@nonl
    #@-node:AGP.20251128113631.206:link()
    #@+node:AGP.20251205185002:unlink()
    def unlink(self):
        
        print 'unlink',int(self.index("current").split(".")[0])-1
        
        v = self.links[int(self.index("current").split(".")[0])-1]
        del v.unknownAttributes['qlink']
        line = self.links.index(v)+1
            
        self.config(state="normal")
        self.delete( "%i.0"%line,"%i.end+1c"%line)
        self.config(state="normal")
            
        self.links.remove(v)
        
        
        self.config( height = len(self.links) )
        if len(self.links) == 0:
            self.pack_forget()
    #@nonl
    #@-node:AGP.20251205185002:unlink()
    #@+node:AGP.20251205184334:clear()
    def clear(self):
        print 'unlink all'
        
        self.config( height = 1 )
        
        for v in self.links:
            del v.unknownAttributes['qlink']
            line = self.links.index(v)+1
            
        
        
        self.config(state="normal")
        self.delete( "1.0","end")
        self.config(state="normal")
            
        self.links = []
        
        
        self.pack_forget()
        
    #@nonl
    #@-node:AGP.20251205184334:clear()
    #@+node:AGP.20251205184430:on_right_click()
    def on_right_click(self,e):
            
        
        txt_width = 200
        
        e.widget.focus()
        
        v = self.links[int(self.index("current").split(".")[0])-1]
        
        #self.select(None,v=v)
                    
        rmenu = Tk.Menu(None,tearoff=0,takefocus=0)
        
        
        
        rmenu.add_command(label="Unlink",command=self.unlink)
        rmenu.add_command(label="Unlink All",command=self.clear)
            
        
        rmenu.tk_popup(e.x_root+1,e.y_root-10)
        #rmenu.post(e.x_root+1,e.y_root-10)
        
        return False
    #@-node:AGP.20251205184430:on_right_click()
    #@+node:AGP.20260225200026:on delete node
    #@-node:AGP.20260225200026:on delete node
    #@-others
#@nonl
#@-node:AGP.20251128113631.204:class leoQlink
#@+node:AGP.20251128113631.207:class leoBody
class leoBody(Tk.Text):
    
    """A class that represents the body pane of a Tkinter window."""

    #@    @+others
    #@+node:AGP.20251128113631.208:__init__()
    def __init__ (self,frame,parentFrame):
        
        self.frame = frame
        c = self.c = frame.c
        self.forceFullRecolorFlag = False
        frame.body = self
        
        self.bodyCtrl = self
        
        Tk.Text.__init__(self,parentFrame, name='bodytext', bd=0, relief="flat", 
                            setgrid=0, wrap='non',padx=10,pady=10)
        
        import leoEditCommands
        
        #Key events sequence: keyhandler -> before_key -> Text -> after_key
        # keyhandler -> app level events (open,save etc...)
        # before_key -> special key event (insert tab, newline etc...)
        # Text -> default widget behaviour
        # after_key -> update changed data, flash matching bracket etc...
        self.bind('<Double-Button-1>',self.on_double_left_click)
        self.bind('<Key>', leo.gui.keyHandler)#,add="+") #after the default handler
        self.bind('<Key>', self.on_before_key,add="+")
        
    
        btags = list(self.bindtags())
        btags.insert(2,"pcb") #post class bindings
        self.bindtags( tuple(btags) )#tuple(btags[:2] + ["pcb"] + btags[2:]) )
        
        self.bind_class('pcb','<Key>', self.on_after_key)
        #print body.bind('<Key>')
        #print body.bindtags()
        
        
        
        self.nScroll = 3
        #body.zoomable = True
        #body.on_zoom = self.on_zoom
        
        
        self.bind("<MouseWheel>",frame.TopMouseWheel)
    
        
        frame.bodyBar = self.bodyBar = bodyBar = SCROLLBAR(parentFrame,1)
        
        def yscrollCallback(x,y,bodyBar=bodyBar,w=self):
            # g.trace(x,y)
            if hasattr(w,'leo_scrollBarSpot'):
                w.leo_scrollBarSpot = (x,y)
            return bodyBar.set(x,y)
       
        self['yscrollcommand'] = yscrollCallback # bodyBar.set
        bodyBar.command =  self.yview   #['command']
        bodyBar.pack(side="right", fill="y")
        
        # Always create the horizontal bar.
        frame.bodyXBar = self.bodyXBar = bodyXBar = SCROLLBAR(parentFrame,0)
        self['xscrollcommand'] = bodyXBar.set
        bodyXBar.command = self.xview
        bodyXBar.pack(side="bottom", fill="x")
            
        self.pack(expand=1,fill="both")
        
        #-------------------------------------------------
        self.colorizer = leoColor.colorizer(c,self.bodyCtrl)
        self.colorizer.configure_tags()
        
    #@nonl
    #@-node:AGP.20251128113631.208:__init__()
    #@+node:AGP.20251128113631.209:createBindings()
    def createBindings (self,w=None):
    
        '''(tkBody) Create gui-dependent bindings.
        These are *not* made in nullBody instances.'''
        
        print "binding",w
        
        frame = self.frame ; c = self.c ; k = c.k
        if not w: w = self.bodyCtrl
        
        w.bind('<Key>', k.masterKeyHandler)
        
        #w.bind('<ButtonRelease-1>', self.OnLRelease)
        
    
        for kind,func,handler in (
            ('<Button-1>',  frame.OnBodyClick,          k.masterClickHandler),
            ('<Button-3>',  frame.OnBodyRClick,         k.masterClick3Handler),
            ('<Double-1>',  frame.OnBodyDoubleClick,    k.masterDoubleClickHandler),
            ('<Double-3>',  None,                       k.masterDoubleClick3Handler),
            #('<Button-2>',  frame.OnPaste,              k.masterClickHandler), #agp
        ):
            def bodyClickCallback(event,handler=handler,func=func):
                return handler(event,func)
    
            w.bind(kind,bodyClickCallback)
    #@nonl
    #@-node:AGP.20251128113631.209:createBindings()
    #@+node:AGP.20251128113631.212:setColorFromConfig
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
    
    #@-node:AGP.20251128113631.212:setColorFromConfig
    #@+node:AGP.20251128113631.213:setFontFromConfig
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
    #@-node:AGP.20251128113631.213:setFontFromConfig
    #@+node:AGP.20251128113631.214:on_zoom()
    def on_zoom(self,delta):
        
        w = self.bodyCtrl
        
        try:
            f = tkFont.Font(name=w.cget("font"))
        except:
            f = tkFont.Font(name=w.cget("font"),exists=True)
                
        fdic = f.actual()
                
        if delta < 1:
            fdic['size'] += 1
        else:
            fdic['size'] -= 1
                
        w.fontref = tkFont.Font(**fdic)
        w.config(font=w.fontref)
    #@nonl
    #@-node:AGP.20251128113631.214:on_zoom()
    #@+node:AGP.20251129213151.3:updateEditors
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
    #@-node:AGP.20251129213151.3:updateEditors
    #@+node:AGP.20260307212508:Key event funcs
    #@+node:AGP.20260414132651:on_double_left_click()
    def on_double_left_click(self,event):
        c.editCommands.extendToWord(event)
        return "break"
    #@nonl
    #@-node:AGP.20260414132651:on_double_left_click()
    #@+node:AGP.20251202213207:on_before_key()
    def on_before_key(self,event):
        
        #Key events sequence: keyhandler -> before_key -> Text -> after_key
        # keyhandler -> app level events (open,save etc...)
        # before_key -> special key event (insert tab, newline etc...)
        # Text -> default widget behaviour
        # after_key -> update changed data, flash matching bracket etc...
        
        
        # here are intercepted:
            # the tab(\t) key for custom tab indent
            # the newline(\n \r) key for auto indent
            # the  backspace(\b backspace) key for back delete indent
        
        #print "body.on_before_key()",event.keysym,event.char#,self.get_text()
        # 	Alt : 0x20000 | shift : 0x0001 | 	Control : 0x0004
        
        if event.state & 0x20005: # we dont interfer if state keys are pressed
            return
        
        
        #special_keys = ('Caps_Lock', 'Num_Lock', 'Control_L', 'Alt_L','Shift_L', 'Control_R', 'Alt_R','Shift_R','Win_L','Win_R')
        
        keysym = event.keysym        
        ch = event.char
        
        
        
        if keysym == "Return":
            self.insert_newline()
            self.onBodyChanged('typing')
            return "break"
            
        if keysym == "BackSpace":
            self.backspace()
            self.onBodyChanged('typing')
            return "break"
            
        if keysym == "Tab":
            self.insert_tab()
            self.onBodyChanged('typing')
            return "break"
            
        
        
        #self.onBodyChanged('typing')
        
    #@nonl
    #@-node:AGP.20251202213207:on_before_key()
    #@+node:AGP.20260308153458:on_after_key()
    def on_after_key(self,event):
        
        """key strokes are intercepted and default tk text handler is overriden beacause:
             -this allow to update colorizing and node body text at each key.
            -the undo mechanism of the text widget is also overriden .
            -backspace (ie space vs tab deletion.
        """
        
        #print "body.on_after_key()",event.char,event.keysym,self.get_text()
        
        
        ch = event.char
        
        if ch != "" and ch in "([{}])":
            i = self.index("insert")
            self.flash_matching_bracket(i+"-1c",ch)
        
        
        
        
        
        self.onBodyChanged('typing')
    #@nonl
    #@-node:AGP.20260308153458:on_after_key()
    #@+node:AGP.20260307214251:get_selected_range()
    def get_selected_range(self,sort=True):
        
        """Return a tuple representing the selected range of t, a Tk.Text widget.
        
        Return a tuple giving the insertion point if no range of text is selected."""
    
        # To get the current selection.
        try:
            sel = self.tag_ranges("sel")
        except Exception:
            return 0,0
    
        if len(sel) == 2:
            i,j = sel
            if sort:
                if t.compare(i, ">", j):
                    i,j = j,i
            return i,j
        else:
            # Return the insertion point if there is no selected text.
            insert = self.index("insert")
        
        return insert,insert
    #@-node:AGP.20260307214251:get_selected_range()
    #@+node:AGP.20260307214559:get_text()
    def get_text(self,range=None):
        
        """Return all the text of Tk.Text widget t converted to unicode."""
        if range:
            start, end = range
            if start and end and start != end:
                s = t.get(start,end)
        else:
            start, end = "1.0","end-1c"
        
        
        s = self.get(start, end) # New in 4.4.1: use end-1c.
    
        if s is None:
            return u""
        else:
            return g.toUnicode(s,g.app.tkEncoding)
    #@-node:AGP.20260307214559:get_text()
    #@+node:AGP.20260307212508.5:flash_matching_bracket()
    def flash_matching_bracket (self,index,ch):
    
        s = self.get_text()
        i = g.app.gui.toPythonIndex(s,self,index)
        
        d = {}
        if ch in '([{':
            #for z in xrange(len(self.openBracketsList)):
            #    d [self.openBracketsList[z]] = self.closeBracketsList[z]
            d = {'(':')','[':']','{':'}'}
            reverse = False # Search forward
        else:
            #for z in xrange(len(self.openBracketsList)):
            #    d [self.closeBracketsList[z]] = self.openBracketsList[z]
            d = {')':'(',']':'[','}':'{'}
            reverse = True # Search backward
    
        delim2 = d.get(ch)
        #print "flash_matching_bracket()",i,ch,delim2,":",s
        j = g.skip_matching_python_delims(s,i,ch,delim2,reverse=reverse)
        
        if j != -1:
            j = g.app.gui.toGuiIndex(s,self,j)
            self.flashCharacter(j)
    #@-node:AGP.20260307212508.5:flash_matching_bracket()
    #@+node:AGP.20260307212508.6:flashCharacter()
    def flashCharacter(self,i):
        
        bg      =  'DodgerBlue1'
        fg      =  'white'
        flashes =  2
        delay   =  75
    
        def addFlashCallback(w,count,index):
            self.tag_add('flash',index,'%s+1c' % (index))
            self.after(delay,removeFlashCallback,self,count-1,index)
        
        def removeFlashCallback(w,count,index):
            self.tag_remove('flash','1.0','end')
            if count > 0:
                self.after(delay,addFlashCallback,self,count,index)
    
        try:
            self.tag_configure('flash',foreground=fg,background=bg)
            addFlashCallback(self,flashes,i)
        except Exception,e:
            #print e
            pass
    #@-node:AGP.20260307212508.6:flashCharacter()
    #@+node:AGP.20260307212508.9:insert_tab()
    def insert_tab(self,directives=None):
        
        if not directives:
            directives = g.scanDirectives(self.c)
        
        tab_width = directives.get("tabwidth",c.tab_width)
        w = self
        
        i,j = self.get_selected_range()
        if i != j:
            w.delete(i,j)
        
        if tab_width > 0:
            w.insert("insert",'\t')
        
        else:
            # Get the preceeding characters.
            s = w.get("insert linestart","insert")
        
            # Compute n, the number of spaces to insert.
            width = g.computeWidth(s,tab_width)
            n = abs(tab_width) - (width % abs(tab_width))
            w.insert("insert",' ' * n)
        
        return True #changed
    #@nonl
    #@-node:AGP.20260307212508.9:insert_tab()
    #@+node:AGP.20260308132701:insert_newline()
    def insert_newline(self):
        w = self
        i,j = self.get_selected_range()
    
        if i != j:
            # No auto-indent if there is selected text.
            w.delete(i,j)
            w.insert(i,"\n")
            return True
        else:
            w.insert(i,"\n")
            allow_in_nocolor = c.config.getBool('autoindent_in_nocolor_mode')
            if allow_in_nocolor or c.frame.body.colorizer.useSyntaxColoring(p) :
                # No auto-indent if in @nocolor mode or after a Change command.
                self.updateAutoIndent(p,w)
                return True
                
        return False
    #@nonl
    #@-node:AGP.20260308132701:insert_newline()
    #@+node:AGP.20260307212508.8:udpateAutoIndent
    # By David McNab:
    def updateAutoIndent (self,p,w):
    
        c = self.c ; d = g.scanDirectives(c)
        tab_width = d.get("tabwidth",c.tab_width) # Get the previous line.
        s = w.get("insert linestart - 1 lines","insert linestart -1c")
        
        # Add the leading whitespace to the present line.
        junk, width = g.skip_leading_ws_with_indent(s,0,tab_width)
        
        if s and len(s) > 0 and s [ -1] == ':':
            # For Python: increase auto-indent after colons.
            if c.frame.body.colorizer.scanColorDirectives(p) == "python":
                width += abs(tab_width)
        if True:#self.smartAutoIndent:
            # Determine if prev line has unclosed parens/brackets/braces
            bracketWidths = [width] ; tabex = 0
            for i in range(0,len(s)):
                if s [i] == '\t':
                    tabex += tab_width-1
                if s [i] in '([{':
                    bracketWidths.append(i+tabex+1)
                elif s [i] in '}])' and len(bracketWidths) > 1:
                    bracketWidths.pop()
            width = bracketWidths.pop()
        
        ws = g.computeLeadingWhitespace(width,tab_width)
        if ws:
            w.insert("insert",ws)
    #@-node:AGP.20260307212508.8:udpateAutoIndent
    #@+node:AGP.20260307224015:backspace()
    def backspace(self,event=None):
        
        '''Delete the character to the left of the cursor.'''
        
        #c = self.c ; p = c.currentPosition()
        w = self#.editWidget(event)
        if not w: return
        
        i,j = self.get_selected_range()
        # g.trace(wname,i,j)
    
        #self.beginCommand()
        d = g.scanDirectives(self.c)
        
        tab_width = d.get("tabwidth",c.tab_width)
        
        changed = True
        
        if i != j:
            w.delete(i,j)
        elif i == '1.0':
            changed = False # Bug fix: 1/6/06 (after a5 released).
        elif tab_width > 0:
            w.delete('insert-1c')
        else:
            s = prev = w.get("insert linestart","insert")
            n = len(prev)
            abs_width = abs(tab_width)
    
            # Delete up to this many spaces.
            n2 = (n % abs_width) or abs_width
            n2 = min(n,n2) ; count = 0
    
            while n2 > 0:
                n2 -= 1
                ch = prev[n-count-1]
                if ch != ' ': break
                else: count += 1
    
            # Make sure we actually delete something.
            w.delete("insert -%dc" % (max(1,count)),"insert")
        
        return changed
        #self.endCommand(changed=True,setLabel=False) # Necessary to make text changes stick.
        
    #@nonl
    #@-node:AGP.20260307224015:backspace()
    #@-node:AGP.20260307212508:Key event funcs
    #@+node:AGP.20251129213151:onBodyChanged()
    # This is the only key handler for the body pane.
    def onBodyChanged (self,undoType,oldSel=None,oldText=None,oldYview=None):
        
        '''Update Leo after the body has been changed.'''
        
        body = self ; c = self.c ; bodyCtrl = body.bodyCtrl
        
        p = c.currentPosition()
        
        insert = bodyCtrl.index('insert')
        ch = g.choose(insert=='1.0','',bodyCtrl.get('insert-1c'))
        
        ch = g.toUnicode(ch,g.app.tkEncoding)
        newText = g.app.gui.getAllText(bodyCtrl) # Note: getAllText converts to unicode.
        
        newSel = g.app.gui.getTextSelection(bodyCtrl)
        
        if oldText is None: oldText = p.bodyString()
        
        changed = oldText != newText
        #print "body changed",changed
        
        if changed:
            c.undoer.setUndoTypingParams(p,undoType,oldText=oldText,newText=newText,oldSel=oldSel,newSel=newSel,oldYview=oldYview)
            
            p.v.setTnodeText(newText)
            p.v.t.insertSpot = body.getInsertionPoint()
            
            c.frame.scanForTabWidth(p)
            body.recolor_now(p)
            #self.forceFullRecolorFlag = False
            
            if not c.changed: c.setChanged(True)
            
            # redraw the screen if necessary
            c.beginUpdate()
            try:
                redraw_flag = False
                # Update dirty bits. p.setDirty() sets all cloned and @file dirty bits.
                if not p.isDirty() and p.setDirty():
                    redraw_flag = True
            
                # Update icons. p.v.iconVal may not exist during unit tests.
                val = p.computeIcon()
                if not hasattr(p.v,"iconVal") or val != p.v.iconVal:
                    p.v.iconVal = val
                    redraw_flag = True
            finally:
                c.endUpdate(redraw_flag)
            
            g.doHook("bodychanged",c=c,p=p,oldText=oldText,newText = newText)
            
    #@-node:AGP.20251129213151:onBodyChanged()
    #@+node:AGP.20251128113631.232:Focus (tkBody)
    def hasFocus (self):
        
        return self.bodyCtrl == self.frame.top.focus_displayof()
        
    def setFocus (self):
        
        self.c.widgetWantsFocus(self.bodyCtrl)
    #@-node:AGP.20251128113631.232:Focus (tkBody)
    #@+node:AGP.20251128113631.233:forceFullRecolor()
    def forceFullRecolor(self):
        self.forceFullRecolorFlag = True
    #@-node:AGP.20251128113631.233:forceFullRecolor()
    #@+node:AGP.20251129202124:recolor_now()
    def recolor_now(self,p,incremental=False):
        self.colorizer.colorize(p.copy(),incremental)
        
    def updateSyntaxColorer(self,p):
        return self.colorizer.updateSyntaxColorer(p.copy())
    #@nonl
    #@-node:AGP.20251129202124:recolor_now()
    #@+node:AGP.20251128113631.234:Tk bindings (tkBbody)
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
    #@+node:AGP.20251128113631.238:Height & width
    def getBodyPaneHeight (self):
        
        return self.winfo_height()
    
    def getBodyPaneWidth (self):
        
        return self.winfo_width()
    #@-node:AGP.20251128113631.238:Height & width
    #@+node:AGP.20251128113631.239:Idle time...
    def scheduleIdleTimeRoutine (self,function,*args,**keys):
    
        self.after_idle(function,*args,**keys)
    #@-node:AGP.20251128113631.239:Idle time...
    #@+node:AGP.20251128113631.240:Indices (leoTkinterBody)
    #@+node:AGP.20251128113631.241:adjustIndex
    def adjustIndex (self,index,offset):
        
        t = self.bodyCtrl
        return t.index("%s + %dc" % (t.index(index),offset))
    #@-node:AGP.20251128113631.241:adjustIndex
    #@+node:AGP.20251128113631.242:compareIndices
    def compareIndices(self,i,rel,j):
    
        return self.bodyCtrl.compare(i,rel,j)
    #@-node:AGP.20251128113631.242:compareIndices
    #@+node:AGP.20251128113631.243:convertRowColumnToIndex
    def convertRowColumnToIndex (self,row,column):
        
        return self.bodyCtrl.index("%s.%s" % (row,column))
    #@-node:AGP.20251128113631.243:convertRowColumnToIndex
    #@+node:AGP.20251128113631.244:convertIndexToRowColumn
    def convertIndexToRowColumn (self,index):
        
        index = self.bodyCtrl.index(index)
        start, end = string.split(index,'.')
        return int(start),int(end)
    #@-node:AGP.20251128113631.244:convertIndexToRowColumn
    #@+node:AGP.20251128113631.245:getImageIndex
    def getImageIndex (self,image):
        
        return self.bodyCtrl.index(image)
    #@-node:AGP.20251128113631.245:getImageIndex
    #@+node:AGP.20251128113631.246:tkIndex (internal use only)
    def tkIndex(self,index):
        
        """Returns the canonicalized Tk index."""
        
        if index == "start": index = "1.0"
        
        return self.bodyCtrl.index(index)
    #@-node:AGP.20251128113631.246:tkIndex (internal use only)
    #@-node:AGP.20251128113631.240:Indices (leoTkinterBody)
    #@+node:AGP.20251128113631.247:Insert point
    #@+node:AGP.20251128113631.248:get/setPythonInsertionPoint
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
    #@-node:AGP.20251128113631.248:get/setPythonInsertionPoint
    #@+node:AGP.20251128113631.249:getInsertionPoint & getBeforeInsertionPoint
    def getBeforeInsertionPoint (self):
        
        return self.bodyCtrl.index("insert-1c")
    
    def getInsertionPoint (self):
        
        return self.bodyCtrl.index("insert")
    #@-node:AGP.20251128113631.249:getInsertionPoint & getBeforeInsertionPoint
    #@+node:AGP.20251128113631.250:getCharAtInsertPoint & getCharBeforeInsertPoint
    def getCharAtInsertPoint (self):
        
        s = self.bodyCtrl.get("insert")
        return g.toUnicode(s,g.app.tkEncoding)
    
    def getCharBeforeInsertPoint (self):
    
        s = self.bodyCtrl.get("insert -1c")
        return g.toUnicode(s,g.app.tkEncoding)
    #@-node:AGP.20251128113631.250:getCharAtInsertPoint & getCharBeforeInsertPoint
    #@+node:AGP.20251128113631.251:makeInsertPointVisible
    def makeInsertPointVisible (self):
        
        self.bodyCtrl.see("insert") # -5l")
    #@-node:AGP.20251128113631.251:makeInsertPointVisible
    #@+node:AGP.20251128113631.252:setInsertionPointTo...
    def setInsertionPoint (self,index):
        self.bodyCtrl.mark_set("insert",index)
    
    def setInsertionPointToEnd (self):
        self.bodyCtrl.mark_set("insert","end")
        
    def setInsertPointToStartOfLine (self,lineNumber): # zero-based line number
        self.bodyCtrl.mark_set("insert",str(1+lineNumber)+".0 linestart")
    #@-node:AGP.20251128113631.252:setInsertionPointTo...
    #@-node:AGP.20251128113631.247:Insert point
    #@+node:AGP.20251128113631.254:Selection
    #@+node:AGP.20251128113631.255:deleteTextSelection
    def deleteTextSelection (self):
        
        t = self.bodyCtrl
        sel = t.tag_ranges("sel")
        if len(sel) == 2:
            start,end = sel
            if t.compare(start,"!=",end):
                t.delete(start,end)
    #@-node:AGP.20251128113631.255:deleteTextSelection
    #@+node:AGP.20251128113631.256:getSelectedText
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
    #@-node:AGP.20251128113631.256:getSelectedText
    #@+node:AGP.20251128113631.257:getTextSelection
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
    #@-node:AGP.20251128113631.257:getTextSelection
    #@+node:AGP.20251128113631.258:getPythonTextSelection
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
    #@-node:AGP.20251128113631.258:getPythonTextSelection
    #@+node:AGP.20251128113631.259:setPythonTextSelection
    def setPythonTextSelection(self,i,j):
    
        t = self.bodyCtrl
        s = t.get('1.0','end')
        row,col = g.convertPythonIndexToRowCol(s,i)
        i1 = '%d.%d' % (row+1,col)
        row,col = g.convertPythonIndexToRowCol(s,j)
        i2 = '%d.%d' % (row+1,col)
        g.app.gui.setTextSelection(self.bodyCtrl,i1,i2)
    #@-node:AGP.20251128113631.259:setPythonTextSelection
    #@+node:AGP.20251128113631.260:hasTextSelection
    def hasTextSelection (self):
    
        sel = self.bodyCtrl.tag_ranges("sel")
        return sel and len(sel) == 2
    #@-node:AGP.20251128113631.260:hasTextSelection
    #@+node:AGP.20251128113631.261:selectAllText
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
    #@-node:AGP.20251128113631.261:selectAllText
    #@+node:AGP.20251128113631.262:setTextSelection (tkinterBody)
    def setTextSelection (self,i,j=None,insert='sel.end'):
        
        # Allow the user to pass either a 2-tuple or two separate args.
        if i is None:
            i,j = "1.0","1.0"
        elif len(i) == 2:
            i,j = i
    
        g.app.gui.setTextSelection(self.bodyCtrl,i,j,insert)
    #@-node:AGP.20251128113631.262:setTextSelection (tkinterBody)
    #@-node:AGP.20251128113631.254:Selection
    #@+node:AGP.20251128113631.263:Text
    #@+node:AGP.20251128113631.264:delete...
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
    #@-node:AGP.20251128113631.264:delete...
    #@+node:AGP.20251128113631.265:get...
    #@+node:AGP.20251128113631.266:tkBody.getAllText
    def getAllText (self):
        
        """Return all the body text, converted to unicode."""
        
        s = self.bodyCtrl.get("1.0","end-1c") # New in 4.4.1: use end-1c.
    
        if s is None:
            return u""
        else:
            return g.toUnicode(s,g.app.tkEncoding)
    #@-node:AGP.20251128113631.266:tkBody.getAllText
    #@+node:AGP.20251128113631.267:getCharAtIndex
    def getCharAtIndex (self,index):
        
        """Return all the body text, converted to unicode."""
        
        s = self.bodyCtrl.get(index)
        if s is None:
            return u""
        else:
            return g.toUnicode(s,g.app.tkEncoding)
    #@-node:AGP.20251128113631.267:getCharAtIndex
    #@+node:AGP.20251128113631.268:getInsertLines
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
    #@-node:AGP.20251128113631.268:getInsertLines
    #@+node:AGP.20251128113631.269:getSelectionAreas
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
    #@-node:AGP.20251128113631.269:getSelectionAreas
    #@+node:AGP.20251128113631.270:getSelectionLines (tkBody)
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
    #@-node:AGP.20251128113631.270:getSelectionLines (tkBody)
    #@+node:AGP.20251128113631.271:getTextRange
    def getTextRange (self,index1,index2):
        
        t = self.bodyCtrl
        return t.get(t.index(index1),t.index(index2))
    #@-node:AGP.20251128113631.271:getTextRange
    #@-node:AGP.20251128113631.265:get...
    #@+node:AGP.20251128113631.272:Insert...
    #@+node:AGP.20251128113631.273:insertAtInsertPoint
    def insertAtInsertPoint (self,s):
        
        self.bodyCtrl.insert("insert",s)
    #@-node:AGP.20251128113631.273:insertAtInsertPoint
    #@+node:AGP.20251128113631.274:insertAtEnd
    def insertAtEnd (self,s):
        
        self.bodyCtrl.insert("end",s)
    #@-node:AGP.20251128113631.274:insertAtEnd
    #@+node:AGP.20251128113631.275:insertAtStartOfLine
    def insertAtStartOfLine (self,lineNumber,s):
        
        self.bodyCtrl.insert(str(1+lineNumber)+".0",s)
    #@-node:AGP.20251128113631.275:insertAtStartOfLine
    #@-node:AGP.20251128113631.272:Insert...
    #@+node:AGP.20251128113631.276:setSelectionAreas (tkinterBody)
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
    #@-node:AGP.20251128113631.276:setSelectionAreas (tkinterBody)
    #@-node:AGP.20251128113631.263:Text
    #@+node:AGP.20251128113631.277:Visibility & scrolling
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
    #@-node:AGP.20251128113631.277:Visibility & scrolling
    #@-node:AGP.20251128113631.234:Tk bindings (tkBbody)
    #@+node:AGP.20251129203139:destroy()
    def destroy(self):
        """ crash the closing process if not implemented """
        pass
    #@nonl
    #@-node:AGP.20251129203139:destroy()
    #@-others
#@-node:AGP.20251128113631.207:class leoBody
#@+node:AGP.20251128113631.278:class leoLog
class leoLog():
    
    """A class that represents the log pane of a Tkinter window."""

    #@    @+others
    #@+node:AGP.20251128113631.279:__init__
    def __init__ (self,frame,parentFrame):
        
        # g.trace("leoTkinterLog")
        
        self.c = c = frame.c # Also set in the base constructor, but we need it here.
        
        self.colorTags = []
            # The list of color names used as tags in present tab.
            # This gest switched by selectTab.
    
        self.wrap = "none" #g.choose(c.config.getBool('log_pane_wraps'),"word","none")
    
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
        #leoLog.__init__(self,frame,parentFrame)----------------------------------
        self.frame = frame
        self.c = frame.c
        
        self.enabled = True
        self.newlines = 0
        self.isNull = False
    
        # Note: self.logCtrl is None for nullLog's.
        self.logCtrl = self.createControl(parentFrame)
        #------------------------------------------------------------------------
    #@nonl
    #@-node:AGP.20251128113631.279:__init__
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
    #@+node:AGP.20250415230112.2850:leoLog.onActivateLog
    def onActivateLog (self,event=None):
    
        self.c.setLog()
    #@-node:AGP.20250415230112.2850:leoLog.onActivateLog
    #@+node:AGP.20251128113631.280:createControl
    def createControl (self,parentFrame):
    
        c = self.c
        
        self.logCtrl = self.createTextWidget(parentFrame)
        
        
        return self.logCtrl
    #@-node:AGP.20251128113631.280:createControl
    #@+node:AGP.20251128113631.281:createTextWidget
    def createTextWidget (self,parentFrame):
        
        self.logNumber += 1
        
        self.logCtrl = log = Tk.Text(parentFrame,name="logtext",setgrid=0,wrap=self.wrap,bd=2,relief="flat")#,state='disabled')#bg="white")
        
        #print str(log),log['font']
        
        self.dim = 0.6
        log.bind('<FocusIn>',self.focus_in)
        log.bind('<FocusOut>',self.focus_out)
        log.bind("<MouseWheel>",self.frame.TopMouseWheel)
        
        
        log.bind("<Button-3>",self.OnRighClick)
        
        
        log.on_zoom = self.on_zoom
        
        
        logBar = SCROLLBAR(parentFrame,1)#    Tk.Scrollbar(parentFrame,name="logBar")
    
        log['yscrollcommand'] = logBar.set
        logBar.command = log.yview
        logBar.pack(side="right", fill="y")
        
        # rr 8/14/02 added horizontal elevator 
        if self.wrap == "none": 
            logXBar = SCROLLBAR(parentFrame,0)#Tk.Scrollbar(parentFrame,name='logXBar',orient="horizontal") 
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
    #@-node:AGP.20251128113631.281:createTextWidget
    #@+node:AGP.20251128113631.282:OnRighClick()
    def OnRighClick(self,e):
        print "log right click"
        
        
        
        rmenu = Tk.Menu(None,tearoff=0,takefocus=0)
        rmenu.add_command(label='Copy',command=self.c.frame.OnCopyFromMenu)
        rmenu.add_command(label='Wrap '+self.CycleWrap(False),command=self.CycleWrap)
    
        #rmenu.tk_popup(e.x_root-23,e.y_root+13)
        rmenu.tk_popup(e.x_root+1,e.y_root-10)
        #rmenu.post(e.x_root+1,e.y_root-10)
    #@nonl
    #@-node:AGP.20251128113631.282:OnRighClick()
    #@+node:AGP.20251128113631.283:CycleWrap()
    def CycleWrap(self,set=True):
        wm = self.logCtrl.cget('wrap')
        
        if wm == 'char':
            wm = 'word'
        elif wm == 'word':
            wm = 'none'
        elif wm == 'none':
            wm = 'char'
            
        if set:
            self.logCtrl.config(wrap = wm)
            
        return wm
    #@nonl
    #@-node:AGP.20251128113631.283:CycleWrap()
    #@+node:AGP.20251128113631.284:on_zoom()
    def on_zoom(self,delta):
        
        w = self.logCtrl
        
        try:
            f = tkFont.Font(name=w.cget("font"))
        except:
            f = tkFont.Font(name=w.cget("font"),exists=True)
                
        fdic = f.actual()
                
        if delta < 1:
            fdic['size'] += 1
        else:
            fdic['size'] -= 1
                
        w.fontref = tkFont.Font(**fdic)
        w.config(font=w.fontref)
    #@nonl
    #@-node:AGP.20251128113631.284:on_zoom()
    #@+node:AGP.20251128113631.285:focus_in()
    def focus_in(self,event):
        self.undim_text()
        
    #@nonl
    #@-node:AGP.20251128113631.285:focus_in()
    #@+node:AGP.20251128113631.286:focus_out()
    def focus_out(self,event):
        self.dim_text()
        
    #@-node:AGP.20251128113631.286:focus_out()
    #@+node:AGP.20251128113631.287:dim_text()
    def dim_text(self):
        log = self.logCtrl
        log.config(fg = g.color_mul(self.dim,self.full_fg) )
        for color in self.colorTags:
            c = log.tag_cget(color,"foreground")
            log.tag_config(color, foreground=g.color_mul(self.dim,c) )
            
        self.dimmed = True
    #@nonl
    #@-node:AGP.20251128113631.287:dim_text()
    #@+node:AGP.20251128113631.288:undim_text()
    def undim_text(self):
        log = self.logCtrl
        log.config(fg = self.full_fg )
        for color in self.colorTags:
            c = log.tag_cget(color,"foreground")
            log.tag_config(color, foreground=g.color_mul(1.0/self.dim,c) )
            
        self.dimmed = False
    #@nonl
    #@-node:AGP.20251128113631.288:undim_text()
    #@+node:AGP.20251128113631.289:makeTabMenu
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
    #@-node:AGP.20251128113631.289:makeTabMenu
    #@+node:AGP.20251128113631.290:Config & get/saveState
    #@+node:AGP.20251128113631.291:tkLog.configureBorder & configureFont
    def configureBorder(self,border):
        
        self.logCtrl.configure(bd=border)
        
    def configureFont(self,font):
        print 'cfgfony'
        self.logCtrl.configure(font=font)
    #@-node:AGP.20251128113631.291:tkLog.configureBorder & configureFont
    #@+node:AGP.20251128113631.292:tkLog.getFontConfig
    def getFontConfig (self):
    
        font = g.log['font']
        # g.trace(font)
        return font
    #@-node:AGP.20251128113631.292:tkLog.getFontConfig
    #@+node:AGP.20251128113631.293:tkLog.restoreAllState
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
    #@-node:AGP.20251128113631.293:tkLog.restoreAllState
    #@+node:AGP.20251128113631.294:tkLog.saveAllState
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
    #@-node:AGP.20251128113631.294:tkLog.saveAllState
    #@+node:AGP.20251128113631.295:tkLog.setColorFromConfig
    def setColorFromConfig (self):
        c = self.c
        
        
        
        bg = c.config.getColor("log_pane_background_color")
        
        
        
        try:
            self.logCtrl.configure(bg=bg)
        except:
            g.es("exception setting log pane background color")
            g.es_exception()
    #@-node:AGP.20251128113631.295:tkLog.setColorFromConfig
    #@+node:AGP.20251128113631.296:tkLog.setFontFromConfig
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
    #@-node:AGP.20251128113631.296:tkLog.setFontFromConfig
    #@-node:AGP.20251128113631.290:Config & get/saveState
    #@+node:AGP.20251128113631.297:Focus & update (tkLog)
    #@+node:AGP.20251128113631.298:tkLog.onActivateLog
    def onActivateLog (self,event=None):
    
        try:
            self.c.setLog()
            self.frame.tree.OnDeactivate()
            self.c.logWantsFocus()
        except:
            g.es_event_exception("activate log")
    #@-node:AGP.20251128113631.298:tkLog.onActivateLog
    #@+node:AGP.20251128113631.299:tkLog.hasFocus
    def hasFocus (self):
        
        return self.c.get_focus() == self.logCtrl
    #@-node:AGP.20251128113631.299:tkLog.hasFocus
    #@+node:AGP.20251128113631.300:forceLogUpdate
    def forceLogUpdate (self,s):
    
        if sys.platform == "darwin": # Does not work on MacOS X.
            try:
                print s, # Don't add a newline.
            except UnicodeError:
                # g.app may not be inited during scripts!
                print g.toEncodedString(s,'utf-8')
        else:
            self.logCtrl.update_idletasks()
    #@-node:AGP.20251128113631.300:forceLogUpdate
    #@-node:AGP.20251128113631.297:Focus & update (tkLog)
    #@+node:AGP.20251128113631.301:put & putnl (tkLog)
    #@+at 
    #@nonl
    # Printing uses self.logCtrl, so this code need not concern itself
    # with which tab is active.
    # 
    # Also, selectTab switches the contents of colorTags, so that is not 
    # concern.
    # It may be that Pmw will allow us to dispense with the colorTags logic...
    #@-at
    #@+node:AGP.20251128113631.302:put
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
            #@+node:AGP.20251128113631.303:<< put s to log control >>
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
            #@-node:AGP.20251128113631.303:<< put s to log control >>
            #@nl
            logCtrl.update_idletasks()
        else:
            #@        << put s to logWaiting and print s >>
            #@+node:AGP.20251128113631.304:<< put s to logWaiting and print s >>
            g.app.logWaiting.append((s,color),)
            
            print "Null tkinter log"
            
            if type(s) == type(u""):
                s = g.toEncodedString(s,"ascii")
            
            print s
            #@-node:AGP.20251128113631.304:<< put s to logWaiting and print s >>
            #@nl
    #@-node:AGP.20251128113631.302:put
    #@+node:AGP.20251128113631.305:putnl
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
    #@-node:AGP.20251128113631.305:putnl
    #@-node:AGP.20251128113631.301:put & putnl (tkLog)
    #@+node:AGP.20251128113631.306:Tab (TkLog)
    #@+node:AGP.20251128113631.307:clearTab
    def clearTab (self,tabName,wrap='none'):
        
        self.selectTab(tabName,wrap=wrap)
        t = self.logCtrl
        t and t.delete('1.0','end')
    #@-node:AGP.20251128113631.307:clearTab
    #@+node:AGP.20251128113631.308:createTab
    def createTab (self,tabName,wrap='none'):
        
        # g.trace(tabName,wrap)
        
        c = self.c ; k = c.k
        tabFrame = self.nb.add(tabName)
        self.menu = self.makeTabMenu(tabName)
        #@    << Create the tab's text widget >>
        #@+node:AGP.20251128113631.309:<< Create the tab's text widget >>
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
        #@-node:AGP.20251128113631.309:<< Create the tab's text widget >>
        #@nl
    
        if tabName != 'Log':
            # c.k doesn't exist when the log pane is created.
            # k.makeAllBindings will call setTabBindings('Log')
            self.setTabBindings(tabName)
    #@-node:AGP.20251128113631.308:createTab
    #@+node:AGP.20251128113631.310:cycleTabFocus
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
    #@-node:AGP.20251128113631.310:cycleTabFocus
    #@+node:AGP.20251128113631.311:deleteTab
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
    #@-node:AGP.20251128113631.311:deleteTab
    #@+node:AGP.20251128113631.312:hideTab
    def hideTab (self,tabName):
        
        self.selectTab('Log')
    #@-node:AGP.20251128113631.312:hideTab
    #@+node:AGP.20251128113631.313:getSelectedTab
    def getSelectedTab (self):
        
        return self.tabName
    #@-node:AGP.20251128113631.313:getSelectedTab
    #@+node:AGP.20251128113631.314:lower/raiseTab
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
    #@-node:AGP.20251128113631.314:lower/raiseTab
    #@+node:AGP.20251128113631.315:numberOfVisibleTabs
    def numberOfVisibleTabs (self):
        
        return len([val for val in self.frameDict.values() if val != None])
    #@-node:AGP.20251128113631.315:numberOfVisibleTabs
    #@+node:AGP.20251128113631.316:renameTab
    def renameTab (self,oldName,newName):
        
        label = self.nb.tab(oldName)
        label.configure(text=newName)
    #@-node:AGP.20251128113631.316:renameTab
    #@+node:AGP.20251128113631.317:selectTab
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
    #@-node:AGP.20251128113631.317:selectTab
    #@+node:AGP.20251128113631.318:setTabBindings
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
    #@-node:AGP.20251128113631.318:setTabBindings
    #@+node:AGP.20251128113631.319:Tab menu callbacks & helpers
    #@+node:AGP.20251128113631.320:onRightClick & onClick
    def onRightClick (self,event,menu):
        
        c = self.c
        menu.post(event.x_root,event.y_root)
        
        
    def onClick (self,event,tabName):
    
        self.selectTab(tabName)
    #@-node:AGP.20251128113631.320:onRightClick & onClick
    #@+node:AGP.20251128113631.321:newTabFromMenu
    def newTabFromMenu (self,tabName='Log'):
    
        self.selectTab(tabName)
        
        # This is called by getTabName.
        def selectTabCallback (newName):
            return self.selectTab(newName)
    
        self.getTabName(selectTabCallback)
    #@-node:AGP.20251128113631.321:newTabFromMenu
    #@+node:AGP.20251128113631.322:renameTabFromMenu
    def renameTabFromMenu (self,tabName):
    
        if tabName in ('Log','Completions'):
            g.es('can not rename %s tab' % (tabName),color='blue')
        else:
            def renameTabCallback (newName):
                return self.renameTab(tabName,newName)
    
            self.getTabName(renameTabCallback)
    #@-node:AGP.20251128113631.322:renameTabFromMenu
    #@+node:AGP.20251128113631.323:getTabName
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
    #@-node:AGP.20251128113631.323:getTabName
    #@-node:AGP.20251128113631.319:Tab menu callbacks & helpers
    #@-node:AGP.20251128113631.306:Tab (TkLog)
    #@-others
#@-node:AGP.20251128113631.278:class leoLog
#@+node:AGP.20250415230112.3560:class leoMenu
"""Tkinter menu handling for Leo."""

#@@language python
#@@tabwidth -4
#@@pagewidth 80



class leoMenu:
    """A class that represents a Leo window."""
    #@    @+others
    #@+node:AGP.20250415230112.3561:__init__()
    def __init__ (self,frame):
        
        # Init the base class.
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
        
        self.top = frame.top
        
        self.font = None#cc.config.getFontFromParams(
        #    'menu_text_font_family', 'menu_text_font_size',
        #    'menu_text_font_slant',  'menu_text_font_weight',
        #    c.config.defaultMenuFontSize)
    #@-node:AGP.20250415230112.3561:__init__()
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
    #@+node:AGP.20260221110401:createMenusFromTables()
    def createMenusFromTables(self):
        
        c = self.c
        
        #@    @+others
        #@+node:AGP.20260221111409:File
        fileMenu = self.createNewMenu("&File")
            
        fileMenuTopTable = [
                '*&new',
                ('&Open...','open-outline'),
                '-',
                ('&Close','close-window'),
                ('&Save','save-file'),
                ('Save &As','save-file-as'),
                ('Save &To','save-file-to'),
                ('Re&vert To Saved','revert'),
            ]
        
        self.createMenuEntries(fileMenu,fileMenuTopTable)
        
        #self.createNewMenu("Open &With...","File")
        #create the recent files submenu
        
            
        self.add_separator(fileMenu)
        
        
        #@+others
        #@+node:AGP.20260221140223:recent files submenu
        self.createNewMenu("Open Recent &File...","File")
        c.recentFiles = c.config.getRecentFiles()
        
        if 0: # Not needed, and causes problems in wxWindows...
            self.createRecentFilesMenuItems()
        #@-node:AGP.20260221140223:recent files submenu
        #@+node:AGP.20260221111928:read/write submenu
        fileMenuReadWriteMenuTable = [
                '*&read-outline-only',
                ('Read @file &Nodes','read-at-file-nodes'),
                ('Write &Dirty @file Nodes','write-dirty-at-file-nodes'),
                ('Write &Missing @file Nodes','write-missing-at-file-nodes'),
                '*write-&outline-only',
                ('&Write @file Nodes','write-at-file-nodes'),
            ]
        readWriteMenu = self.createNewMenu("&Read/Write...","File")
        self.createMenuEntries(readWriteMenu,fileMenuReadWriteMenuTable)
        #@nonl
        #@-node:AGP.20260221111928:read/write submenu
        #@+node:AGP.20260221111928.1:tangle submenu
        fileMenuTangleMenuTable = [
                '*tangle-&all',
                '*tangle-&marked',
                '*&tangle',
            ]
        tangleMenu = self.createNewMenu("Tan&gle...","File")
        self.createMenuEntries(tangleMenu,fileMenuTangleMenuTable)
        #@nonl
        #@-node:AGP.20260221111928.1:tangle submenu
        #@+node:AGP.20260221111928.2:untangle submenu
        fileMenuUntangleMenuTable = [
                '*untangle-&all',
                '*untangle-&marked',
                '*&untangle',
            ]
        untangleMenu = self.createNewMenu("&Untangle...","File")
        self.createMenuEntries(untangleMenu,fileMenuUntangleMenuTable)
        #@nonl
        #@-node:AGP.20260221111928.2:untangle submenu
        #@+node:AGP.20260221111928.3:import submenu
        self.fileMenuImportMenuTable = [
                #&: c,d,f,n,o,r,
                '*import-&derived-file',
                ('Import To @&file','import-at-file'),
                ('Import To @&root','import-at-root'),
                '*import-&cweb-files',
                '*import-&noweb-files',
                '*import-flattened-&outline',
            ]
        importMenu = self.createNewMenu("&Import...","File")
        self.createMenuEntries(importMenu,self.fileMenuImportMenuTable)
        #@nonl
        #@-node:AGP.20260221111928.3:import submenu
        #@+node:AGP.20260221111928.4:export submenu
        self.fileMenuExportMenuTable = [
                '*export-&headlines',
                '*outline-to-&cweb',
                '*outline-to-&noweb',
                '*&flatten-outline',
                '*&remove-sentinels',
                '*&weave',
            ]
        exportMenu = self.createNewMenu("&Export...","File")
        self.createMenuEntries(exportMenu,self.fileMenuExportMenuTable)
        #@nonl
        #@-node:AGP.20260221111928.4:export submenu
        #@-others
        
        
        self.add_separator(fileMenu)
        
        self.fileMenuTop3MenuTable = [
                ('Set Leo ID','set-leo-id'),
                ('E&xit','exit-leo')
            ]
        self.createMenuEntries(fileMenu,self.fileMenuTop3MenuTable)
        #@nonl
        #@-node:AGP.20260221111409:File
        #@+node:AGP.20260221112603.1:Edit
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
        
        
        editMenu = self.createNewMenu("&Edit")
        self.createMenuEntries(editMenu,self.editMenuTopTable)
        
        
        #@+others
        #@+node:AGP.20260221112603.2:edit body submenu
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
        
        editBodyMenu = self.createNewMenu("Edit &Body...","Edit")
        
        self.createMenuEntries(editBodyMenu,self.editMenuEditBodyTable)
        #@-node:AGP.20260221112603.2:edit body submenu
        #@+node:AGP.20260221112603.3:edit headline submenu
        self.editMenuEditHeadlineTable = [
                '*edit-&headline',
                '*&end-edit-headline',
                '*&abort-edit-headline',
                '*insert-headline-&time',
                '*toggle-&angle-brackets',
            ]
        
        editHeadlineMenu = self.createNewMenu("Edit &Headline...","Edit")
        
        self.createMenuEntries(editHeadlineMenu,self.editMenuEditHeadlineTable)
        #@-node:AGP.20260221112603.3:edit headline submenu
        #@+node:AGP.20260221112603.4:find submenu
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
        
        
        
        
        findMenu = self.createNewMenu("&Find...","Edit")
        
        #self.createMenuEntries(findMenu,self.editMenuFindMenuTable)
        
        findMenu.add_command(label="Find/Change Next",accelerator="F3",command=self.c.searchCommands.findTabFindNext)
        findMenu.add_command(label="Find/Change Prev",accelerator="F2",command=self.c.searchCommands.findTabFindPrev)
        findMenu.add_separator()
        findMenu.add_command(label="Find/Change All",command=self.c.searchCommands.findTabFindAll)
        findMenu.add_command(label="Clone Find All",command=self.c.searchCommands.findTabFindAll)
        
        
        #@-node:AGP.20260221112603.4:find submenu
        #@-others
        
        try:        show = c.frame.body.getColorizer().showInvisibles
        except:     show = False
        label = g.choose(show,"Hide In&visibles","Show In&visibles")
        self.editMenuTop2Table = [
                '*&goto-line-number',
                '*&execute-script',
                (label,'toggle-invisibles'),
                #("Setti&ngs",'open-leoSettings-leo'),
            ]
            
        self.createMenuEntries(editMenu,self.editMenuTop2Table)
        #@-node:AGP.20260221112603.1:Edit
        #@+node:AGP.20260221110401.12:Outline
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
        
        outlineMenu = self.createNewMenu("&Outline")
        self.createMenuEntries(outlineMenu,self.outlineMenuTopMenuTable)
        
        #@+others
        #@+node:AGP.20260221110401.13:check submenu
        self.outlineMenuCheckOutlineMenuTable = [
                # &: a,c,d,o
                '*check-&outline',
                '*&dump-outline',
                '-',
                '*check-&all-python-code',
                '*&check-python-code',
            ]
        
        checkOutlineMenu = self.createNewMenu("Chec&k...","Outline")
        self.createMenuEntries(checkOutlineMenu,self.outlineMenuCheckOutlineMenuTable)
        #@-node:AGP.20260221110401.13:check submenu
        #@+node:AGP.20260221110401.14:expand/contract submenu
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
        
        
        expandMenu = self.createNewMenu("E&xpand/Contract...","Outline")
        self.createMenuEntries(expandMenu,self.outlineMenuExpandContractMenuTable)
        #@-node:AGP.20260221110401.14:expand/contract submenu
        #@+node:AGP.20260221110401.15:move submenu
        self.outlineMenuMoveMenuTable = [
                ('Move &Down','move-outline-down'),
                ('Move &Left','move-outline-left'),
                ('Move &Right','move-outline-right'),
                ('Move &Up','move-outline-up'),
                '-',
                '*&promote',
                '*&demote',
            ]
        
        moveSelectMenu = self.createNewMenu("&Move...","Outline")
        self.createMenuEntries(moveSelectMenu,self.outlineMenuMoveMenuTable)
        #@-node:AGP.20260221110401.15:move submenu
        #@+node:AGP.20260221110401.16:mark submenu
        self.outlineMenuMarkMenuTable = [
                '*&mark',
                '*mark-&subheads',
                '*mark-changed-&items',
                '*mark-changed-&roots',
                '*mark-&clones',
                '*&unmark-all',
            ]
        
        markMenu = self.createNewMenu("M&ark/Unmark...","Outline")
        self.createMenuEntries(markMenu,self.outlineMenuMarkMenuTable)
        #@-node:AGP.20260221110401.16:mark submenu
        #@+node:AGP.20260221110401.17:create goto submenu
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
        
        gotoMenu = self.createNewMenu("&Go To...","Outline")
        self.createMenuEntries(gotoMenu,self.outlineMenuGoToMenuTable)
        #@-node:AGP.20260221110401.17:create goto submenu
        #@-others
        #@-node:AGP.20260221110401.12:Outline
        #@+node:AGP.20260221110401.20:Help
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
                #'*help-for-&command',
                #'-',
                #'*&apropos-autocompletion',
                #'*apropos-&bindings',
                #'*apropos-&find-commands',
                '-',
                '*pri&nt-bindings',
                #'*print-c&ommands',
            ]
        
        helpMenu = self.createNewMenu("&Help")
        self.createMenuEntries(helpMenu,self.helpMenuTable)
        #@nonl
        #@-node:AGP.20260221110401.20:Help
        #@-others
        
        g.doHook("create-optional-menus",c=c)
        
        #if self.useCmdMenu:
        #    self.createCmndsMenuFromTable()
            
        
        
        
    #@-node:AGP.20260221110401:createMenusFromTables()
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
            
            if type(data) == type(''):
        # New in Leo 4.4.2: Can use the same string for both the label and the command string.
                if data == '-':
                    self.add_separator(menu)
                    continue
    
                command = data.replace('*','').replace('&','').lower()
                label = command.replace('-',' ').title()
    
        
            elif type(data) in (type(()), type([])) and len(data) in (2,3):
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
    
            
            #print label,command
            
            
            accel = leo.config.settings.get(command) or ""
            if accel == "None": accel = ""
            
            
            #print label,command,accel
            accelerator = stroke = k.shortcutFromSetting(accel) or ''
            #print label,command,accelerator
            
            label = label.replace("&","")
            
            # get cmd name to func
            cmd = c.leoCommands.getPublicCommands().get(command,None)
            if not cmd:
                cmd = c.commandsDict.get(command,None)
            
            #print "createMenuEntries()" , label,accelerator,command,cmd
            
            self.add_command(menu, label=label, accelerator=accelerator, command=cmd)
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
    #@+node:AGP.20250415230112.3562:Activate menu commands
    #@+node:AGP.20250415230112.3563:tkMenu.activateMenu
    def activateMenu (self,menuName):
        
        c = self.c ;  top = c.frame.top
        topx,topy = top.winfo_rootx(),top.winfo_rooty()
        menu = c.frame.menu.getMenu(menuName)
    
        if menu:
            d = self.computeMenuPositions()
            x = d.get(menuName)
            if x is None:
                 x = 0 ; g.trace('oops, no menu offset: %s' % menuName)
            
            menu.tk_popup(topx+d.get(menuName,0),topy) # Fix by caugm.  Thanks!
        else:
            g.trace('oops, no menu: %s' % menuName)
    #@-node:AGP.20250415230112.3563:tkMenu.activateMenu
    #@+node:AGP.20250415230112.3564:tkMenu.computeMenuPositions
    def computeMenuPositions (self):
        
        # A hack.  It would be better to set this when creating the menus.
        menus = ('File','Edit','Outline','Plugins','Cmds','Window','Help')
        
        # Compute the *approximate* x offsets of each menu.
        d = {}
        n = 0
        for z in menus:
            menu = self.getMenu(z)
            fontName = menu.cget('font')
            font = tkFont.Font(font=fontName)
            # print '%8s' % (z),menu.winfo_reqwidth(),menu.master,menu.winfo_x()
            d [z] = n
            # A total hack: sorta works on windows.
            n += font.measure(z+' '*4)+1
            
        return d
    #@-node:AGP.20250415230112.3564:tkMenu.computeMenuPositions
    #@-node:AGP.20250415230112.3562:Activate menu commands
    #@+node:AGP.20250415230112.3565:getMacHelpMenu
    def getMacHelpMenu (self):
        
        try:
            topMenu = self.getMenu('top')
            # Use the name argument to create the special Macintosh Help menu.
            helpMenu = Tk.Menu(topMenu,name='help',tearoff=0)
            self.add_cascade(topMenu,label='Help',menu=helpMenu,underline=0)
            self.createMenuEntries(helpMenu,self.helpMenuTable)
            return helpMenu
    
        except Exception:
            g.trace('Can not get MacOS Help menu')
            g.es_exception()
            return None
    #@nonl
    #@-node:AGP.20250415230112.3565:getMacHelpMenu
    #@+node:AGP.20250415230112.3566:Tkinter menu bindings
    # See the Tk docs for what these routines are to do
    #@+node:AGP.20250415230112.3567:Methods with Tk spellings
    #@+node:AGP.20250415230112.3568:add_cascade
    def add_cascade (self,parent,label,menu,underline):
        
        """Wrapper for the Tkinter add_cascade menu method."""
        
        return parent.add_cascade(label=label,menu=menu,underline=underline)
    #@-node:AGP.20250415230112.3568:add_cascade
    #@+node:AGP.20250415230112.3569:add_command
    def add_command (self,menu,**keys):
        
        """Wrapper for the Tkinter add_command menu method."""
    
        return menu.add_command(**keys)
    #@-node:AGP.20250415230112.3569:add_command
    #@+node:AGP.20250415230112.3570:add_separator
    def add_separator(self,menu):
        
        """Wrapper for the Tkinter add_separator menu method."""
    
        menu.add_separator()
    #@-node:AGP.20250415230112.3570:add_separator
    #@+node:AGP.20250415230112.3571:bind
    def bind (self,bind_shortcut,callback):
        
        """Wrapper for the Tkinter bind menu method."""
        
        # g.trace(bind_shortcut)
    
        return self.top.bind(bind_shortcut,callback)
    #@-node:AGP.20250415230112.3571:bind
    #@+node:AGP.20250415230112.3572:delete
    def delete (self,menu,realItemName):
        
        """Wrapper for the Tkinter delete menu method."""
    
        return menu.delete(realItemName)
    #@-node:AGP.20250415230112.3572:delete
    #@+node:AGP.20250415230112.3573:delete_range
    def delete_range (self,menu,n1,n2):
        
        """Wrapper for the Tkinter delete menu method."""
    
        return menu.delete(n1,n2)
    #@-node:AGP.20250415230112.3573:delete_range
    #@+node:AGP.20250415230112.3574:destroy
    def destroy (self,menu):
        
        """Wrapper for the Tkinter destroy menu method."""
    
        return menu.destroy()
    #@-node:AGP.20250415230112.3574:destroy
    #@+node:AGP.20250415230112.3575:insert_cascade
    def insert_cascade (self,parent,index,label,menu,underline):
        
        """Wrapper for the Tkinter insert_cascade menu method."""
        
        return parent.insert_cascade(
            index=index,label=label,
            menu=menu,underline=underline)
    #@-node:AGP.20250415230112.3575:insert_cascade
    #@+node:AGP.20250415230112.3576:new_menu agp
    def new_menu(self,parent,tearoff=False,postc=None):
        
        """Wrapper for the Tkinter new_menu menu method."""
        rw = g.app.root
        bg = self.frame.menuFrame.cget('bg')
        
        #bg = g.colorf_mul(0.9,*colors_tof(*rw.winfo_rgb(bg)))
        
        
        if parent:    
            if self.font:
                try:
                    menu = Tk.Menu(parent,tearoff=tearoff,font=self.font,postcommand=postc)#,bd=0,bg=bg)
                except Exception:
                    g.es_exception()
                    return Tk.Menu(parent,tearoff=tearoff,postcommand=postc)
            else:
                
                menu = Tk.Menu(parent,tearoff=tearoff,bg=bg,postcommand=postc)
                #print "menu bg",bg
            
        else:
        
            mb = Tk.Menubutton(self.frame.menuFrame)#, relief='flat',bg=bg)
            menu = mb.m = Tk.Menu(mb,tearoff=tearoff,postcommand=postc)
            mb['menu'] = mb.m
            mb.m.mb = mb
        
            mb.pack(side='left')
            #print menu
            #print self.frame.iconFrame.winfo_children()
            
        return menu
    #@nonl
    #@-node:AGP.20250415230112.3576:new_menu agp
    #@+node:AGP.20250415230112.3577:xnew_menu
    def xnew_menu(self,parent,tearoff=False):
        
        """Wrapper for the Tkinter new_menu menu method."""
        
        bg= self.c.config.getColor("def_background_color")
        
        if self.font:
            try:
                return Tk.Menu(parent,tearoff=tearoff,bg=bg,font=self.font)
            except Exception:
                g.es_exception()
                return Tk.Menu(parent,tearoff=tearoff,bg=bg)
        else:
            return Tk.Menu(parent,tearoff=tearoff,bg=bg)
    #@-node:AGP.20250415230112.3577:xnew_menu
    #@-node:AGP.20250415230112.3567:Methods with Tk spellings
    #@+node:AGP.20250415230112.3578:Methods with other spellings (Tkmenu)
    #@+node:AGP.20250415230112.3579:clearAccel
    def clearAccel(self,menu,name):
        
        realName = self.getRealMenuName(name)
        realName = realName.replace("&","")
    
        menu.entryconfig(realName,accelerator='')
    #@-node:AGP.20250415230112.3579:clearAccel
    #@+node:AGP.20250415230112.3580:createMenuBar
    def createMenuBar(self,frame):
    
        top = frame.top
        
        # Note: font setting has no effect here.
        #topMenu = Tk.Menubutton(frame.iconFrame)#,postcommand=self.updateAllMenus)#top
        
        # Do gui-independent stuff.
        #self.setMenu("top",topMenu)
        self.createMenusFromTables()
        
        #topMenu.pack(side='top',fill='x')
        
        #top.config(menu=topMenu) # Display the menu. #agp menu
    #@-node:AGP.20250415230112.3580:createMenuBar
    #@+node:AGP.20250415230112.3581:createOpenWithMenu
    def createOpenWithMenu(self,parent,label,index,amp_index):
        
        '''Create a submenu.'''
        
        menu = Tk.Menu(parent,tearoff=0)
        parent.insert_cascade(index,label=label,menu=menu,underline=amp_index)
        return menu
    #@-node:AGP.20250415230112.3581:createOpenWithMenu
    #@+node:AGP.20250415230112.3582:disableMenu
    def disableMenu (self,menu,name):
        
        try:
            menu.entryconfig(name,state="disabled")
        except: 
            try:
                realName = self.getRealMenuName(name)
                realName = realName.replace("&","")
                menu.entryconfig(realName,state="disabled")
            except:
                print "disableMenu menu,name:",menu,name
                g.es_exception()
                pass
    #@-node:AGP.20250415230112.3582:disableMenu
    #@+node:AGP.20250415230112.3583:enableMenu
    # Fail gracefully if the item name does not exist.
    
    def enableMenu (self,menu,name,val):
        
        state = g.choose(val,"normal","disabled")
        try:
            menu.entryconfig(name,state=state)
        except:
            try:
                realName = self.getRealMenuName(name)
                realName = realName.replace("&","")
                menu.entryconfig(realName,state=state)
            except:
                print "enableMenu menu,name,val:",menu,name,val
                g.es_exception()
                pass
    #@-node:AGP.20250415230112.3583:enableMenu
    #@+node:AGP.20250415230112.3584:getMenuLabel
    def getMenuLabel (self,menu,name):
        
        '''Return the index of the menu item whose name (or offset) is given.
        Return None if there is no such menu item.'''
    
        try:
            index = menu.index(name)
        except:
            index = None
            
        return index
    #@-node:AGP.20250415230112.3584:getMenuLabel
    #@+node:AGP.20250415230112.3585:setMenuLabel
    def setMenuLabel (self,menu,name,label,underline=-1):
    
        try:
            if type(name) == type(0):
                # "name" is actually an index into the menu.
                menu.entryconfig(name,label=label,underline=underline)
            else:
                # Bug fix: 2/16/03: use translated name.
                realName = self.getRealMenuName(name)
                realName = realName.replace("&","")
                # Bug fix: 3/25/03" use tranlasted label.
                label = self.getRealMenuName(label)
                label = label.replace("&","")
                menu.entryconfig(realName,label=label,underline=underline)
        except:
            if not g.app.unitTesting:
                print "setMenuLabel menu,name,label:",menu,name,label
                g.es_exception()
    #@-node:AGP.20250415230112.3585:setMenuLabel
    #@-node:AGP.20250415230112.3578:Methods with other spellings (Tkmenu)
    #@-node:AGP.20250415230112.3566:Tkinter menu bindings
    #@-others
#@-node:AGP.20250415230112.3560:class leoMenu
#@+node:AGP.20260330091637:class leoNewMenu
"""Tkinter menu handling for Leo."""

#@@language python
#@@tabwidth -4
#@@pagewidth 80


class leoNewMenu:
    #@    @+others
    #@+node:AGP.20260330091637.1:__init__()
    def __init__ (self,frame):
        
        # Init the base class.
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
        
        self.top = frame.top
        
        self.font = None#cc.config.getFontFromParams(
        #    'menu_text_font_family', 'menu_text_font_size',
        #    'menu_text_font_slant',  'menu_text_font_weight',
        #    c.config.defaultMenuFontSize)
    
        #@    @+others
        #@+node:AGP.20260330093020:File
        file_menu_entries = [
                "New",c.new,None
                
            ]
        
        
        
        
        
        
        
        
        self.file_menu = self.newTopMenu("File")
        #@nonl
        #@-node:AGP.20260330093020:File
        #@-others
    #@nonl
    #@-node:AGP.20260330091637.1:__init__()
    #@+node:AGP.20260330093020.1:newTopMenu()
    def newTopMenu(self,text,postc=None):
        
        mb = Tk.Menubutton(self.frame.menuFrame,text)#, relief='flat',bg=bg)
        menu = mb.m = Tk.Menu(mb,tearoff=0,postcommand=postc)
        mb['menu'] = mb.m
        menu.button = mb
        
        mb.pack(side='left')
        
        return menu
    #@nonl
    #@-node:AGP.20260330093020.1:newTopMenu()
    #@+node:AGP.20260330091637.2:Gui-independent menu enablers
    #@+node:AGP.20260330091637.3:updateAllMenus
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
    #@-node:AGP.20260330091637.3:updateAllMenus
    #@+node:AGP.20260330091637.4:updateFileMenu
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
    #@-node:AGP.20260330091637.4:updateFileMenu
    #@+node:AGP.20260330091637.5:updateEditMenu
    def updateEditMenu (self):
    
        c = self.c ; frame = c.frame ; gui = g.app.gui
        if not c: return
        try:
            # Top level Edit menu...
            enable = frame.menu.enableMenu
            menu = frame.menu.getMenu("Edit")
            c.undoer.enableMenuItems()
            #@        << enable cut/paste >>
            #@+node:AGP.20260330091637.6:<< enable cut/paste >>
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
            #@-node:AGP.20260330091637.6:<< enable cut/paste >>
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
    #@-node:AGP.20260330091637.5:updateEditMenu
    #@+node:AGP.20260330091637.7:updateOutlineMenu
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
            #@+node:AGP.20260330091637.8:<< enable top level outline menu >>
            menu = frame.menu.getMenu("Outline")
            enable(menu,"Cut Node",c.canCutOutline())
            enable(menu,"Delete Node",c.canDeleteHeadline())
            enable(menu,"Paste Node",c.canPasteOutline())
            enable(menu,"Paste Node As Clone",c.canPasteOutline())
            enable(menu,"Clone Node",c.canClone()) # 1/31/04
            enable(menu,"Sort Siblings",c.canSortSiblings())
            enable(menu,"Hoist",c.canHoist())
            enable(menu,"De-Hoist",c.canDehoist())
            #@-node:AGP.20260330091637.8:<< enable top level outline menu >>
            #@nl
            #@        << enable expand/contract submenu >>
            #@+node:AGP.20260330091637.9:<< enable expand/Contract submenu >>
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
            #@-node:AGP.20260330091637.9:<< enable expand/Contract submenu >>
            #@nl
            #@        << enable move submenu >>
            #@+node:AGP.20260330091637.10:<< enable move submenu >>
            menu = frame.menu.getMenu("Move...")
            enable(menu,"Move Down",c.canMoveOutlineDown())
            enable(menu,"Move Left",c.canMoveOutlineLeft())
            enable(menu,"Move Right",c.canMoveOutlineRight())
            enable(menu,"Move Up",c.canMoveOutlineUp())
            enable(menu,"Promote",c.canPromote())
            enable(menu,"Demote",c.canDemote())
            #@-node:AGP.20260330091637.10:<< enable move submenu >>
            #@nl
            #@        << enable go to submenu >>
            #@+node:AGP.20260330091637.11:<< enable go to submenu >>
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
            #@-node:AGP.20260330091637.11:<< enable go to submenu >>
            #@nl
            #@        << enable mark submenu >>
            #@+node:AGP.20260330091637.12:<< enable mark submenu >>
            menu = frame.menu.getMenu("Mark/Unmark...")
            label = g.choose(isMarked,"Unmark","Mark")
            frame.menu.setMenuLabel(menu,0,label)
            enable(menu,"Mark Subheads",hasChildren)
            if 0: # These are too slow.
                enable(menu,"Mark Changed Items",c.canMarkChangedHeadlines())
                enable(menu,"Mark Changed Roots",c.canMarkChangedRoots())
            enable(menu,"Mark Clones",isCloned)
            #@-node:AGP.20260330091637.12:<< enable mark submenu >>
            #@nl
        except:
            g.es("exception updating Outline menu")
            g.es_exception()
    #@-node:AGP.20260330091637.7:updateOutlineMenu
    #@+node:AGP.20260330091637.13:hasSelection
    # Returns True if text in the outline or body text is selected.
    
    def hasSelection (self):
        
        body = self.frame.body
    
        if body:
            first, last = body.getTextSelection()
            return first != last
        else:
            return False
    #@-node:AGP.20260330091637.13:hasSelection
    #@-node:AGP.20260330091637.2:Gui-independent menu enablers
    #@+node:AGP.20260330091637.14:Gui-independent menu routines
    #@+node:AGP.20260330091637.15:capitalizeMinibufferMenuName
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
    #@-node:AGP.20260330091637.15:capitalizeMinibufferMenuName
    #@+node:AGP.20260330091637.16:createMenusFromTables()
    def createMenusFromTables(self):
        
        c = self.c
        
        #@    @+others
        #@+node:AGP.20260330091637.17:File
        fileMenu = self.createNewMenu("&File")
            
        fileMenuTopTable = [
                '*&new',
                ('&Open...','open-outline'),
                '-',
                ('&Close','close-window'),
                ('&Save','save-file'),
                ('Save &As','save-file-as'),
                ('Save &To','save-file-to'),
                ('Re&vert To Saved','revert'),
            ]
        
        self.createMenuEntries(fileMenu,fileMenuTopTable)
        
        #self.createNewMenu("Open &With...","File")
        #create the recent files submenu
        
            
        self.add_separator(fileMenu)
        
        
        #@+others
        #@+node:AGP.20260330091637.18:recent files submenu
        self.createNewMenu("Open Recent &File...","File")
        c.recentFiles = c.config.getRecentFiles()
        
        if 0: # Not needed, and causes problems in wxWindows...
            self.createRecentFilesMenuItems()
        #@-node:AGP.20260330091637.18:recent files submenu
        #@+node:AGP.20260330091637.19:read/write submenu
        fileMenuReadWriteMenuTable = [
                '*&read-outline-only',
                ('Read @file &Nodes','read-at-file-nodes'),
                ('Write &Dirty @file Nodes','write-dirty-at-file-nodes'),
                ('Write &Missing @file Nodes','write-missing-at-file-nodes'),
                '*write-&outline-only',
                ('&Write @file Nodes','write-at-file-nodes'),
            ]
        readWriteMenu = self.createNewMenu("&Read/Write...","File")
        self.createMenuEntries(readWriteMenu,fileMenuReadWriteMenuTable)
        #@nonl
        #@-node:AGP.20260330091637.19:read/write submenu
        #@+node:AGP.20260330091637.20:tangle submenu
        fileMenuTangleMenuTable = [
                '*tangle-&all',
                '*tangle-&marked',
                '*&tangle',
            ]
        tangleMenu = self.createNewMenu("Tan&gle...","File")
        self.createMenuEntries(tangleMenu,fileMenuTangleMenuTable)
        #@nonl
        #@-node:AGP.20260330091637.20:tangle submenu
        #@+node:AGP.20260330091637.21:untangle submenu
        fileMenuUntangleMenuTable = [
                '*untangle-&all',
                '*untangle-&marked',
                '*&untangle',
            ]
        untangleMenu = self.createNewMenu("&Untangle...","File")
        self.createMenuEntries(untangleMenu,fileMenuUntangleMenuTable)
        #@nonl
        #@-node:AGP.20260330091637.21:untangle submenu
        #@+node:AGP.20260330091637.22:import submenu
        self.fileMenuImportMenuTable = [
                #&: c,d,f,n,o,r,
                '*import-&derived-file',
                ('Import To @&file','import-at-file'),
                ('Import To @&root','import-at-root'),
                '*import-&cweb-files',
                '*import-&noweb-files',
                '*import-flattened-&outline',
            ]
        importMenu = self.createNewMenu("&Import...","File")
        self.createMenuEntries(importMenu,self.fileMenuImportMenuTable)
        #@nonl
        #@-node:AGP.20260330091637.22:import submenu
        #@+node:AGP.20260330091637.23:export submenu
        self.fileMenuExportMenuTable = [
                '*export-&headlines',
                '*outline-to-&cweb',
                '*outline-to-&noweb',
                '*&flatten-outline',
                '*&remove-sentinels',
                '*&weave',
            ]
        exportMenu = self.createNewMenu("&Export...","File")
        self.createMenuEntries(exportMenu,self.fileMenuExportMenuTable)
        #@nonl
        #@-node:AGP.20260330091637.23:export submenu
        #@-others
        
        
        self.add_separator(fileMenu)
        
        self.fileMenuTop3MenuTable = [
                ('Set Leo ID','set-leo-id'),
                ('E&xit','exit-leo')
            ]
        self.createMenuEntries(fileMenu,self.fileMenuTop3MenuTable)
        #@nonl
        #@-node:AGP.20260330091637.17:File
        #@+node:AGP.20260330091637.24:Edit
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
        
        
        editMenu = self.createNewMenu("&Edit")
        self.createMenuEntries(editMenu,self.editMenuTopTable)
        
        
        #@+others
        #@+node:AGP.20260330091637.25:edit body submenu
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
        
        editBodyMenu = self.createNewMenu("Edit &Body...","Edit")
        
        self.createMenuEntries(editBodyMenu,self.editMenuEditBodyTable)
        #@-node:AGP.20260330091637.25:edit body submenu
        #@+node:AGP.20260330091637.26:edit headline submenu
        self.editMenuEditHeadlineTable = [
                '*edit-&headline',
                '*&end-edit-headline',
                '*&abort-edit-headline',
                '*insert-headline-&time',
                '*toggle-&angle-brackets',
            ]
        
        editHeadlineMenu = self.createNewMenu("Edit &Headline...","Edit")
        
        self.createMenuEntries(editHeadlineMenu,self.editMenuEditHeadlineTable)
        #@-node:AGP.20260330091637.26:edit headline submenu
        #@+node:AGP.20260330091637.27:find submenu
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
        
        
        
        
        findMenu = self.createNewMenu("&Find...","Edit")
        
        #self.createMenuEntries(findMenu,self.editMenuFindMenuTable)
        
        findMenu.add_command(label="Find/Change Next",accelerator="F3",command=self.c.searchCommands.findTabFindNext)
        findMenu.add_command(label="Find/Change Prev",accelerator="F2",command=self.c.searchCommands.findTabFindPrev)
        findMenu.add_separator()
        findMenu.add_command(label="Find/Change All",command=self.c.searchCommands.findTabFindAll)
        findMenu.add_command(label="Clone Find All",command=self.c.searchCommands.findTabFindAll)
        
        
        #@-node:AGP.20260330091637.27:find submenu
        #@-others
        
        try:        show = c.frame.body.getColorizer().showInvisibles
        except:     show = False
        label = g.choose(show,"Hide In&visibles","Show In&visibles")
        self.editMenuTop2Table = [
                '*&goto-line-number',
                '*&execute-script',
                (label,'toggle-invisibles'),
                #("Setti&ngs",'open-leoSettings-leo'),
            ]
            
        self.createMenuEntries(editMenu,self.editMenuTop2Table)
        #@-node:AGP.20260330091637.24:Edit
        #@+node:AGP.20260330091637.28:Outline
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
        
        outlineMenu = self.createNewMenu("&Outline")
        self.createMenuEntries(outlineMenu,self.outlineMenuTopMenuTable)
        
        #@+others
        #@+node:AGP.20260330091637.29:check submenu
        self.outlineMenuCheckOutlineMenuTable = [
                # &: a,c,d,o
                '*check-&outline',
                '*&dump-outline',
                '-',
                '*check-&all-python-code',
                '*&check-python-code',
            ]
        
        checkOutlineMenu = self.createNewMenu("Chec&k...","Outline")
        self.createMenuEntries(checkOutlineMenu,self.outlineMenuCheckOutlineMenuTable)
        #@-node:AGP.20260330091637.29:check submenu
        #@+node:AGP.20260330091637.30:expand/contract submenu
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
        
        
        expandMenu = self.createNewMenu("E&xpand/Contract...","Outline")
        self.createMenuEntries(expandMenu,self.outlineMenuExpandContractMenuTable)
        #@-node:AGP.20260330091637.30:expand/contract submenu
        #@+node:AGP.20260330091637.31:move submenu
        self.outlineMenuMoveMenuTable = [
                ('Move &Down','move-outline-down'),
                ('Move &Left','move-outline-left'),
                ('Move &Right','move-outline-right'),
                ('Move &Up','move-outline-up'),
                '-',
                '*&promote',
                '*&demote',
            ]
        
        moveSelectMenu = self.createNewMenu("&Move...","Outline")
        self.createMenuEntries(moveSelectMenu,self.outlineMenuMoveMenuTable)
        #@-node:AGP.20260330091637.31:move submenu
        #@+node:AGP.20260330091637.32:mark submenu
        self.outlineMenuMarkMenuTable = [
                '*&mark',
                '*mark-&subheads',
                '*mark-changed-&items',
                '*mark-changed-&roots',
                '*mark-&clones',
                '*&unmark-all',
            ]
        
        markMenu = self.createNewMenu("M&ark/Unmark...","Outline")
        self.createMenuEntries(markMenu,self.outlineMenuMarkMenuTable)
        #@-node:AGP.20260330091637.32:mark submenu
        #@+node:AGP.20260330091637.33:create goto submenu
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
        
        gotoMenu = self.createNewMenu("&Go To...","Outline")
        self.createMenuEntries(gotoMenu,self.outlineMenuGoToMenuTable)
        #@-node:AGP.20260330091637.33:create goto submenu
        #@-others
        #@-node:AGP.20260330091637.28:Outline
        #@+node:AGP.20260330091637.34:Help
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
                #'*help-for-&command',
                #'-',
                #'*&apropos-autocompletion',
                #'*apropos-&bindings',
                #'*apropos-&find-commands',
                '-',
                '*pri&nt-bindings',
                #'*print-c&ommands',
            ]
        
        helpMenu = self.createNewMenu("&Help")
        self.createMenuEntries(helpMenu,self.helpMenuTable)
        #@nonl
        #@-node:AGP.20260330091637.34:Help
        #@-others
        
        g.doHook("create-optional-menus",c=c)
        
        #if self.useCmdMenu:
        #    self.createCmndsMenuFromTable()
            
        
        
        
    #@-node:AGP.20260330091637.16:createMenusFromTables()
    #@+node:AGP.20260330091637.35:Helpers
    #@+node:AGP.20260330091637.36:canonicalizeMenuName & cononicalizeTranslatedMenuName
    def canonicalizeMenuName (self,name):
        
        return ''.join([ch for ch in name.lower() if ch.isalnum()])
        
    def canonicalizeTranslatedMenuName (self,name):
        
        return ''.join([ch for ch in name.lower() if ch not in u'& \t\n\r'])
    
    #@-node:AGP.20260330091637.36:canonicalizeMenuName & cononicalizeTranslatedMenuName
    #@+node:AGP.20260330091637.37:computeOldStyleShortcutKey
    def computeOldStyleShortcutKey (self,s):
        
        '''Compute the old-style shortcut key for @shortcuts entries.'''
        
        return ''.join([ch for ch in s.strip().lower() if ch.isalnum()])
    #@-node:AGP.20260330091637.37:computeOldStyleShortcutKey
    #@+node:AGP.20260330091637.38:createMenuEntries
    def createMenuEntries (self,menu,table,dynamicMenu=False):
            
        '''Create a menu entry from the table.
        New in 4.4: this method shows the shortcut in the menu,
        but this method **never** binds any shortcuts.'''
        
        c = self.c ; f = c.frame ; k = c.k
        if g.app.unitTesting: return
        for data in table:
            
            if type(data) == type(''):
        # New in Leo 4.4.2: Can use the same string for both the label and the command string.
                if data == '-':
                    self.add_separator(menu)
                    continue
    
                command = data.replace('*','').replace('&','').lower()
                label = command.replace('-',' ').title()
    
        
            elif type(data) in (type(()), type([])) and len(data) in (2,3):
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
    
            
            #print label,command
            
            
            accel = leo.config.settings.get(command) or ""
            if accel == "None": accel = ""
            
            
            #print label,command,accel
            accelerator = stroke = k.shortcutFromSetting(accel) or ''
            #print label,command,accelerator
            
            label = label.replace("&","")
            
            # get cmd name to func
            cmd = c.leoCommands.getPublicCommands().get(command,None)
            if not cmd:
                cmd = c.commandsDict.get(command,None)
            
            #print "createMenuEntries()" , label,accelerator,command,cmd
            
            self.add_command(menu, label=label, accelerator=accelerator, command=cmd)
    #@-node:AGP.20260330091637.38:createMenuEntries
    #@+node:AGP.20260330091637.39:createMenuItemsFromTable
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
    #@-node:AGP.20260330091637.39:createMenuItemsFromTable
    #@+node:AGP.20260330091637.40:createNewMenu agp
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
    #@-node:AGP.20260330091637.40:createNewMenu agp
    #@+node:AGP.20260330091637.41:createOpenWithMenuFromTable & helper
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
    #@+node:AGP.20260330091637.42:createOpenWithMenuItemsFromTable
    def createOpenWithMenuItemsFromTable (self,menu,table):
        
        '''Create an entry in the Open with Menu from the table.
        
        Each entry should be a sequence with 2 or 3 elements.'''
        
        c = self.c ; k = c.k
    
        if g.app.unitTesting: return
    
        for data in table:
            #@        << get label, accelerator & command or continue >>
            #@+node:AGP.20260330091637.43:<< get label, accelerator & command or continue >>
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
            #@-node:AGP.20260330091637.43:<< get label, accelerator & command or continue >>
            #@nl
            realLabel = self.getRealMenuName(label)
            underline=realLabel.find("&")
            realLabel = realLabel.replace("&","")
            callback = self.defineOpenWithMenuCallback(openWithData)
        
            self.add_command(menu,label=realLabel,
                accelerator=accelerator or '',
                command=callback,underline=underline)
    #@-node:AGP.20260330091637.42:createOpenWithMenuItemsFromTable
    #@-node:AGP.20260330091637.41:createOpenWithMenuFromTable & helper
    #@+node:AGP.20260330091637.44:createRecentFilesMenuItems (leoMenu)
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
    #@-node:AGP.20260330091637.44:createRecentFilesMenuItems (leoMenu)
    #@+node:AGP.20260330091637.45:defineMenuCallback
    def defineMenuCallback(self,command,name,minibufferCommand):
        
        def legacyMenuCallback(event=None,self=self,command=command,label=name):
                
            c = self.c
            return c.doCommand(command,label)
        
        return legacyMenuCallback
    #@-node:AGP.20260330091637.45:defineMenuCallback
    #@+node:AGP.20260330091637.46:defineOpenWithMenuCallback
    def defineOpenWithMenuCallback(self,data):
        
        # The first parameter must be event, and it must default to None.
        def openWithMenuCallback(event=None,self=self,data=data):
            return self.c.openWith(data=data)
    
        return openWithMenuCallback
    #@-node:AGP.20260330091637.46:defineOpenWithMenuCallback
    #@+node:AGP.20260330091637.47:deleteMenu
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
    #@-node:AGP.20260330091637.47:deleteMenu
    #@+node:AGP.20260330091637.48:deleteMenuItem
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
    #@-node:AGP.20260330091637.48:deleteMenuItem
    #@+node:AGP.20260330091637.49:get/setRealMenuName & setRealMenuNamesFromTable
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
    #@-node:AGP.20260330091637.49:get/setRealMenuName & setRealMenuNamesFromTable
    #@+node:AGP.20260330091637.50:getMenu, setMenu, destroyMenu
    def getMenu (self,menuName):
    
        cmn = self.canonicalizeMenuName(menuName)
        return self.menus.get(cmn)
        
    def setMenu (self,menuName,menu):
        
        cmn = self.canonicalizeMenuName(menuName)
        self.menus [cmn] = menu
        
    def destroyMenu (self,menuName):
        
        cmn = self.canonicalizeMenuName(menuName)
        del self.menus[cmn]
    #@-node:AGP.20260330091637.50:getMenu, setMenu, destroyMenu
    #@-node:AGP.20260330091637.35:Helpers
    #@-node:AGP.20260330091637.14:Gui-independent menu routines
    #@+node:AGP.20260330091637.51:Activate menu commands
    #@+node:AGP.20260330091637.52:tkMenu.activateMenu
    def activateMenu (self,menuName):
        
        c = self.c ;  top = c.frame.top
        topx,topy = top.winfo_rootx(),top.winfo_rooty()
        menu = c.frame.menu.getMenu(menuName)
    
        if menu:
            d = self.computeMenuPositions()
            x = d.get(menuName)
            if x is None:
                 x = 0 ; g.trace('oops, no menu offset: %s' % menuName)
            
            menu.tk_popup(topx+d.get(menuName,0),topy) # Fix by caugm.  Thanks!
        else:
            g.trace('oops, no menu: %s' % menuName)
    #@-node:AGP.20260330091637.52:tkMenu.activateMenu
    #@+node:AGP.20260330091637.53:tkMenu.computeMenuPositions
    def computeMenuPositions (self):
        
        # A hack.  It would be better to set this when creating the menus.
        menus = ('File','Edit','Outline','Plugins','Cmds','Window','Help')
        
        # Compute the *approximate* x offsets of each menu.
        d = {}
        n = 0
        for z in menus:
            menu = self.getMenu(z)
            fontName = menu.cget('font')
            font = tkFont.Font(font=fontName)
            # print '%8s' % (z),menu.winfo_reqwidth(),menu.master,menu.winfo_x()
            d [z] = n
            # A total hack: sorta works on windows.
            n += font.measure(z+' '*4)+1
            
        return d
    #@-node:AGP.20260330091637.53:tkMenu.computeMenuPositions
    #@-node:AGP.20260330091637.51:Activate menu commands
    #@+node:AGP.20260330091637.54:getMacHelpMenu
    def getMacHelpMenu (self):
        
        try:
            topMenu = self.getMenu('top')
            # Use the name argument to create the special Macintosh Help menu.
            helpMenu = Tk.Menu(topMenu,name='help',tearoff=0)
            self.add_cascade(topMenu,label='Help',menu=helpMenu,underline=0)
            self.createMenuEntries(helpMenu,self.helpMenuTable)
            return helpMenu
    
        except Exception:
            g.trace('Can not get MacOS Help menu')
            g.es_exception()
            return None
    #@nonl
    #@-node:AGP.20260330091637.54:getMacHelpMenu
    #@+node:AGP.20260330091637.55:Tkinter menu bindings
    # See the Tk docs for what these routines are to do
    #@+node:AGP.20260330091637.56:Methods with Tk spellings
    #@+node:AGP.20260330091637.57:add_cascade
    def add_cascade (self,parent,label,menu,underline):
        
        """Wrapper for the Tkinter add_cascade menu method."""
        
        return parent.add_cascade(label=label,menu=menu,underline=underline)
    #@-node:AGP.20260330091637.57:add_cascade
    #@+node:AGP.20260330091637.58:add_command
    def add_command (self,menu,**keys):
        
        """Wrapper for the Tkinter add_command menu method."""
    
        return menu.add_command(**keys)
    #@-node:AGP.20260330091637.58:add_command
    #@+node:AGP.20260330091637.59:add_separator
    def add_separator(self,menu):
        
        """Wrapper for the Tkinter add_separator menu method."""
    
        menu.add_separator()
    #@-node:AGP.20260330091637.59:add_separator
    #@+node:AGP.20260330091637.60:bind
    def bind (self,bind_shortcut,callback):
        
        """Wrapper for the Tkinter bind menu method."""
        
        # g.trace(bind_shortcut)
    
        return self.top.bind(bind_shortcut,callback)
    #@-node:AGP.20260330091637.60:bind
    #@+node:AGP.20260330091637.61:delete
    def delete (self,menu,realItemName):
        
        """Wrapper for the Tkinter delete menu method."""
    
        return menu.delete(realItemName)
    #@-node:AGP.20260330091637.61:delete
    #@+node:AGP.20260330091637.62:delete_range
    def delete_range (self,menu,n1,n2):
        
        """Wrapper for the Tkinter delete menu method."""
    
        return menu.delete(n1,n2)
    #@-node:AGP.20260330091637.62:delete_range
    #@+node:AGP.20260330091637.63:destroy
    def destroy (self,menu):
        
        """Wrapper for the Tkinter destroy menu method."""
    
        return menu.destroy()
    #@-node:AGP.20260330091637.63:destroy
    #@+node:AGP.20260330091637.64:insert_cascade
    def insert_cascade (self,parent,index,label,menu,underline):
        
        """Wrapper for the Tkinter insert_cascade menu method."""
        
        return parent.insert_cascade(
            index=index,label=label,
            menu=menu,underline=underline)
    #@-node:AGP.20260330091637.64:insert_cascade
    #@+node:AGP.20260330091637.65:new_menu agp
    def new_menu(self,parent,tearoff=False,postc=None):
        
        """Wrapper for the Tkinter new_menu menu method."""
        rw = g.app.root
        bg = self.frame.menuFrame.cget('bg')
        
        #bg = g.colorf_mul(0.9,*colors_tof(*rw.winfo_rgb(bg)))
        
        
        if parent:    
            if self.font:
                try:
                    menu = Tk.Menu(parent,tearoff=tearoff,font=self.font,postcommand=postc)#,bd=0,bg=bg)
                except Exception:
                    g.es_exception()
                    return Tk.Menu(parent,tearoff=tearoff,postcommand=postc)
            else:
                
                menu = Tk.Menu(parent,tearoff=tearoff,bg=bg,postcommand=postc)
                #print "menu bg",bg
            
        else:
        
            mb = Tk.Menubutton(self.frame.menuFrame)#, relief='flat',bg=bg)
            menu = mb.m = Tk.Menu(mb,tearoff=tearoff,postcommand=postc)
            mb['menu'] = mb.m
            mb.m.mb = mb
        
            mb.pack(side='left')
            #print menu
            #print self.frame.iconFrame.winfo_children()
            
        return menu
    #@nonl
    #@-node:AGP.20260330091637.65:new_menu agp
    #@+node:AGP.20260330091637.66:xnew_menu
    def xnew_menu(self,parent,tearoff=False):
        
        """Wrapper for the Tkinter new_menu menu method."""
        
        bg= self.c.config.getColor("def_background_color")
        
        if self.font:
            try:
                return Tk.Menu(parent,tearoff=tearoff,bg=bg,font=self.font)
            except Exception:
                g.es_exception()
                return Tk.Menu(parent,tearoff=tearoff,bg=bg)
        else:
            return Tk.Menu(parent,tearoff=tearoff,bg=bg)
    #@-node:AGP.20260330091637.66:xnew_menu
    #@-node:AGP.20260330091637.56:Methods with Tk spellings
    #@+node:AGP.20260330091637.67:Methods with other spellings (Tkmenu)
    #@+node:AGP.20260330091637.68:clearAccel
    def clearAccel(self,menu,name):
        
        realName = self.getRealMenuName(name)
        realName = realName.replace("&","")
    
        menu.entryconfig(realName,accelerator='')
    #@-node:AGP.20260330091637.68:clearAccel
    #@+node:AGP.20260330091637.69:createMenuBar
    def createMenuBar(self,frame):
    
        top = frame.top
        
        # Note: font setting has no effect here.
        #topMenu = Tk.Menubutton(frame.iconFrame)#,postcommand=self.updateAllMenus)#top
        
        # Do gui-independent stuff.
        #self.setMenu("top",topMenu)
        self.createMenusFromTables()
        
        #topMenu.pack(side='top',fill='x')
        
        #top.config(menu=topMenu) # Display the menu. #agp menu
    #@-node:AGP.20260330091637.69:createMenuBar
    #@+node:AGP.20260330091637.70:createOpenWithMenu
    def createOpenWithMenu(self,parent,label,index,amp_index):
        
        '''Create a submenu.'''
        
        menu = Tk.Menu(parent,tearoff=0)
        parent.insert_cascade(index,label=label,menu=menu,underline=amp_index)
        return menu
    #@-node:AGP.20260330091637.70:createOpenWithMenu
    #@+node:AGP.20260330091637.71:disableMenu
    def disableMenu (self,menu,name):
        
        try:
            menu.entryconfig(name,state="disabled")
        except: 
            try:
                realName = self.getRealMenuName(name)
                realName = realName.replace("&","")
                menu.entryconfig(realName,state="disabled")
            except:
                print "disableMenu menu,name:",menu,name
                g.es_exception()
                pass
    #@-node:AGP.20260330091637.71:disableMenu
    #@+node:AGP.20260330091637.72:enableMenu
    # Fail gracefully if the item name does not exist.
    
    def enableMenu (self,menu,name,val):
        
        state = g.choose(val,"normal","disabled")
        try:
            menu.entryconfig(name,state=state)
        except:
            try:
                realName = self.getRealMenuName(name)
                realName = realName.replace("&","")
                menu.entryconfig(realName,state=state)
            except:
                print "enableMenu menu,name,val:",menu,name,val
                g.es_exception()
                pass
    #@-node:AGP.20260330091637.72:enableMenu
    #@+node:AGP.20260330091637.73:getMenuLabel
    def getMenuLabel (self,menu,name):
        
        '''Return the index of the menu item whose name (or offset) is given.
        Return None if there is no such menu item.'''
    
        try:
            index = menu.index(name)
        except:
            index = None
            
        return index
    #@-node:AGP.20260330091637.73:getMenuLabel
    #@+node:AGP.20260330091637.74:setMenuLabel
    def setMenuLabel (self,menu,name,label,underline=-1):
    
        try:
            if type(name) == type(0):
                # "name" is actually an index into the menu.
                menu.entryconfig(name,label=label,underline=underline)
            else:
                # Bug fix: 2/16/03: use translated name.
                realName = self.getRealMenuName(name)
                realName = realName.replace("&","")
                # Bug fix: 3/25/03" use tranlasted label.
                label = self.getRealMenuName(label)
                label = label.replace("&","")
                menu.entryconfig(realName,label=label,underline=underline)
        except:
            if not g.app.unitTesting:
                print "setMenuLabel menu,name,label:",menu,name,label
                g.es_exception()
    #@-node:AGP.20260330091637.74:setMenuLabel
    #@-node:AGP.20260330091637.67:Methods with other spellings (Tkmenu)
    #@-node:AGP.20260330091637.55:Tkinter menu bindings
    #@-others
#@-node:AGP.20260330091637:class leoNewMenu
#@-node:AGP.20260224172326:Globals
#@+node:AGP.20260224172413:Initialisation
#import leoGui # Do this import after app module is fully imported.
#

g.doHook("start1")  # Load plugins.

app = leo.app

gui = leo.gui = g.app.gui = leoGui()
    
g.app.root = root = g.app.gui.createRootWindow()
    
try:
    g.gen_theme()
except:
    import traceback
    traceback.print_exc()

import leoCommands

fileName = leo.fileName
if not fileName: fileName = ""
#@<< compute the window title >>
#@+node:AGP.20260224174145:<< compute the window title >>
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
#@-node:AGP.20260224174145:<< compute the window title >>
#@nl

# Create an unfinished frame to pass to the commanders.
frame = gui.createLeoFrame(title)

# Create the commander and its subcommanders.
leo.c = c = leoCommands.Commands(frame,fileName)
    
#if not app.initing:
g.doHook("before-create-leo-frame",c=c) # Was 'onCreate': too confusing.
        
frame.finishCreate(c)
c.finishCreate(frame)
    
# Create the menu last so that we can use the key handler for shortcuts.
p = c.currentPosition()
if not g.doHook("menu1",c=c,p=p,v=p):
    frame.menu.createMenuBar(c.frame)   #Menus <- require (shortcut,command)
    

# Finish initing the subcommanders.
c.undoer.clearUndoState() # Menus must exist at this point.
    
c.updateRecentFiles(fileName)
    
    
#if not g.app.initing:
g.doHook("after-create-leo-frame",c=c)

frame.show()
    
#if not frame: exit()
    
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
frame.body.focus_set()

#OPEN THE FILE
#@nonl
#@-node:AGP.20260224172413:Initialisation
#@-others


#@-node:AGP.20250415230112.2925:@thin leoUi.py
#@-leo
