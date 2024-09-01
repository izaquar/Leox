#@+leo-ver=4-thin
#@+node:ekr.20031218072017.4100:@thin leoTkinterMenu.py
"""Tkinter menu handling for Leo."""

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import leoMenu
import Tkinter as Tk
import tkFont

class leoTkinterMenu (leoMenu.leoMenu):
    """A class that represents a Leo window."""
    #@    @+others
    #@+node:ekr.20031218072017.4102:__init__()
    def __init__ (self,frame):
        
        # Init the base class.
        leoMenu.leoMenu.__init__(self,frame)
        
        self.top = frame.top
        self.c = c = frame.c
        self.frame = frame
        
        self.font = None#cc.config.getFontFromParams(
        #    'menu_text_font_family', 'menu_text_font_size',
        #    'menu_text_font_slant',  'menu_text_font_weight',
        #    c.config.defaultMenuFontSize)
    #@-node:ekr.20031218072017.4102:__init__()
    #@+node:ekr.20060211101811:Activate menu commands
    #@+node:ekr.20060211100905.1:tkMenu.activateMenu
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
    #@-node:ekr.20060211100905.1:tkMenu.activateMenu
    #@+node:ekr.20060210133835.1:tkMenu.computeMenuPositions
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
    #@-node:ekr.20060210133835.1:tkMenu.computeMenuPositions
    #@-node:ekr.20060211101811:Activate menu commands
    #@+node:ekr.20060211144330.1:getMacHelpMenu
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
    #@-node:ekr.20060211144330.1:getMacHelpMenu
    #@+node:ekr.20031218072017.4103:Tkinter menu bindings
    # See the Tk docs for what these routines are to do
    #@+node:ekr.20031218072017.4104:Methods with Tk spellings
    #@+node:ekr.20031218072017.4105:add_cascade
    def add_cascade (self,parent,label,menu,underline):
        
        """Wrapper for the Tkinter add_cascade menu method."""
        
        return parent.add_cascade(label=label,menu=menu,underline=underline)
    #@-node:ekr.20031218072017.4105:add_cascade
    #@+node:ekr.20031218072017.4106:add_command
    def add_command (self,menu,**keys):
        
        """Wrapper for the Tkinter add_command menu method."""
    
        return menu.add_command(**keys)
    #@-node:ekr.20031218072017.4106:add_command
    #@+node:ekr.20031218072017.4107:add_separator
    def add_separator(self,menu):
        
        """Wrapper for the Tkinter add_separator menu method."""
    
        menu.add_separator()
    #@-node:ekr.20031218072017.4107:add_separator
    #@+node:ekr.20031218072017.4108:bind
    def bind (self,bind_shortcut,callback):
        
        """Wrapper for the Tkinter bind menu method."""
        
        # g.trace(bind_shortcut)
    
        return self.top.bind(bind_shortcut,callback)
    #@-node:ekr.20031218072017.4108:bind
    #@+node:ekr.20031218072017.4109:delete
    def delete (self,menu,realItemName):
        
        """Wrapper for the Tkinter delete menu method."""
    
        return menu.delete(realItemName)
    #@-node:ekr.20031218072017.4109:delete
    #@+node:ekr.20031218072017.4110:delete_range
    def delete_range (self,menu,n1,n2):
        
        """Wrapper for the Tkinter delete menu method."""
    
        return menu.delete(n1,n2)
    #@-node:ekr.20031218072017.4110:delete_range
    #@+node:ekr.20031218072017.4111:destroy
    def destroy (self,menu):
        
        """Wrapper for the Tkinter destroy menu method."""
    
        return menu.destroy()
    #@-node:ekr.20031218072017.4111:destroy
    #@+node:ekr.20031218072017.4112:insert_cascade
    def insert_cascade (self,parent,index,label,menu,underline):
        
        """Wrapper for the Tkinter insert_cascade menu method."""
        
        return parent.insert_cascade(
            index=index,label=label,
            menu=menu,underline=underline)
    #@-node:ekr.20031218072017.4112:insert_cascade
    #@+node:ekr.20031218072017.4113:new_menu agp
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
                
                menu = Tk.Menu(parent,tearoff=tearoff,bd=0,bg=bg,postcommand=postc)
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
    #@-node:ekr.20031218072017.4113:new_menu agp
    #@+node:AGP.20231020203607:xnew_menu
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
    #@-node:AGP.20231020203607:xnew_menu
    #@-node:ekr.20031218072017.4104:Methods with Tk spellings
    #@+node:ekr.20031218072017.4114:Methods with other spellings (Tkmenu)
    #@+node:ekr.20041228063406:clearAccel
    def clearAccel(self,menu,name):
        
        realName = self.getRealMenuName(name)
        realName = realName.replace("&","")
    
        menu.entryconfig(realName,accelerator='')
    #@-node:ekr.20041228063406:clearAccel
    #@+node:ekr.20031218072017.4115:createMenuBar
    def createMenuBar(self,frame):
    
        top = frame.top
        
        # Note: font setting has no effect here.
        #topMenu = Tk.Menubutton(frame.iconFrame)#,postcommand=self.updateAllMenus)#top
        
        # Do gui-independent stuff.
        #self.setMenu("top",topMenu)
        self.createMenusFromTables()
        
        #topMenu.pack(side='top',fill='x')
        
        #top.config(menu=topMenu) # Display the menu. #agp menu
    #@-node:ekr.20031218072017.4115:createMenuBar
    #@+node:ekr.20051022042645:createOpenWithMenu
    def createOpenWithMenu(self,parent,label,index,amp_index):
        
        '''Create a submenu.'''
        
        menu = Tk.Menu(parent,tearoff=0)
        parent.insert_cascade(index,label=label,menu=menu,underline=amp_index)
        return menu
    #@-node:ekr.20051022042645:createOpenWithMenu
    #@+node:ekr.20031218072017.4119:disableMenu
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
    #@-node:ekr.20031218072017.4119:disableMenu
    #@+node:ekr.20031218072017.4120:enableMenu
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
    #@-node:ekr.20031218072017.4120:enableMenu
    #@+node:ekr.20060622075612:getMenuLabel
    def getMenuLabel (self,menu,name):
        
        '''Return the index of the menu item whose name (or offset) is given.
        Return None if there is no such menu item.'''
    
        try:
            index = menu.index(name)
        except:
            index = None
            
        return index
    #@-node:ekr.20060622075612:getMenuLabel
    #@+node:ekr.20031218072017.4121:setMenuLabel
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
    #@-node:ekr.20031218072017.4121:setMenuLabel
    #@-node:ekr.20031218072017.4114:Methods with other spellings (Tkmenu)
    #@-node:ekr.20031218072017.4103:Tkinter menu bindings
    #@-others
#@-node:ekr.20031218072017.4100:@thin leoTkinterMenu.py
#@-leo
