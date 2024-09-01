#@+leo-ver=4-thin
#@+node:AGP.20230207163742:@thin node_colors.py
#@<< docstring >>
#@+node:AGP.20230207163742.1:<< docstring >>
'''Allows you to colour nodes.  Add colors menu to nodes icons righ-click menu'''
#@nonl
#@-node:AGP.20230207163742.1:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4

#@<< imports >>
#@+node:AGP.20230207163742.2:<< imports >>
import leoGlobals as g
import leoPlugins
import leoTkinterTree

Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)
#import Tkinter as Tk
#pmw = g.importExtension("Pmw",pluginName=__name__,verbose=True,required=True)




import sys
#@nonl
#@-node:AGP.20230207163742.2:<< imports >>
#@nl
__version__ = "0.19"
#@<< version history >>
#@+node:AGP.20230207163742.3:<< version history >>
#@@killcolor

#@+at 
#@nonl
# Use and distribute under the same terms as leo itself.
# 
# Original code by Mark Ng <z3r0.00@gmail.com>
# 
# 0.5  Priority arrows and Archetype-based colouring of headline texts.
# 0.6  Arbitary headline colouring.
# 0.7  Colouring for node types. Added "Others" type option
# 0.8  Added "Clear Priority" option
# 0.8.1  Fixed popup location
# 0.8.2  Fixed unposting
# 0.9  Automatically colour @file and @ignore nodes
# 0.10 EKR:
# - Repackaged for leoPlugins.leo.
#     - Define g.  Eliminate from x import *.
# - Made code work with 4.3 code base:
#     - Override tree.setUnselectedHeadlineColors instead of 
# tree.setUnselectedLabelState
# - Create per-commander instances of cleoController in onCreate.
# - Converted some c/java style to python style.
# - Replaced string.find(s,...) by s.find(...) & removed import string.
# - show_menu now returns 'break':  fixes the 'popup menu is not unposting 
# bug)
# 0.11 EKR:
# - hasUD and getUD now make sure that the dict is actually a dict.
# 0.12 EKR:
# - Changed 'new_c' logic to 'c' logic.
# 0.13 EKR:
# - Installed patch roughly following code at 
# http://sourceforge.net/forum/message.php?msg_id=3517080
# - custom_colours now returns None for default.
# - Added override of setDisabledHeadlineColors so that color changes in 
# headlines happen immediately.
# - Removed checkmark menu item because there is no easy way to clear it.
# 0.14 EKR: Installed further patch to clear checkmark.
# 0.15 TNB:
# - Use dictionary of lists of canvas objects to allow removal
# - Removed code for painting over things
# - Try to track which commander/frame/tree is being used when more than
#   one Leo window open.  Not quite working, redraws are missed if you change
#   Leo windows by right clicking on the icon box, but all changes occur and
#   appear when a left click on the tree occurs.
# - Added rich_ries patch to darken colour of selected auto-colored headlines
# 0.16 TNB:
# - finally seem to have resolved all issues with multiple Leo windows
# - handlers now unregister when window closes
# 0.17 TNB:
# - don't write cleo.TkPickleVars into .leo file (but handle legacies)
# - don't write empty / all default value dictionaries into .leo file
# - added menu option to strip empty / all default value dictionaries from 
# .leo file
# 0.17.1 TNB:
# - added DanR's custom colour selection idea and progress bars
# 0.18 TNB:
# - added time required and recursive time/progress calc.
#   thanks again to DanR for pointers.
# 0.19 TNB:
# - added @project nodes for automatic display updates
# - added Show time to show times on nodes
# - added Find next todo
#@-at
#@-node:AGP.20230207163742.3:<< version history >>
#@nl

ok = Tk is not None
    
#@+others
#@+node:AGP.20230207163742.11:class TkPickleVar(Tk.Variable)
if ok: # Don't define this if import Tkinter failed.

    class TkPickleVar (Tk.Variable):
        "Required as target for Tk menu functions to write back into"
        
        def __setstate__(self,state):
            Tk.Variable.__init__(self)
            Tk.Variable.set(self,state)

        def __getstate__(self):
            p = Tk.Variable.get(self)
            # Beware of returning False!
            return p
#@nonl
#@-node:AGP.20230207163742.11:class TkPickleVar(Tk.Variable)
#@+node:AGP.20230207163742.12:init
def init():

    if ok:
        leoPlugins.registerHandler(('open2','new'), onCreate)
        g.plugin_signon(__name__)

    return ok
#@nonl
#@-node:AGP.20230207163742.12:init
#@+node:AGP.20230207163742.13:onCreate
def onCreate (tag,key):

    c = key.get('c')

    rcController(c)
#@-node:AGP.20230207163742.13:onCreate
#@+node:AGP.20230207163742.14:class rcController
class rcController:
    
    '''A per-commander class that recolors outlines.'''

    #@    @+others
    #@+node:AGP.20230207163742.15:__init__()
    def __init__ (self,c):
        
        self.c = c
        
        self.menu = None
        self.donePriority = 100
        self.smiley = None
    
        self.marks = []   # list of marks made on canvas
    
        self.typePickle = type(TkPickleVar())  # for testing old files
    
    
        # image ids should be a property of the node
        # use {marking,image id} as the kv pair.
        self.images = {}
        
        top = self.c.frame.top
        colors = self.colours = []
        
        for clr in g.theme.keys():
            cs = g.theme[clr]
            try:
                #print clr,cs,
                top.winfo_rgb(cs)
            except:
                #print "is not a color"
                continue
                
            #print "is a color"
            if cs not in colors:
                colors.append(cs)
        
        #self.colours = ['Black','Gray50','White','Red','Orange','Yellow','Green','Blue', 'Purple']
        
    
        
        
        # print "Cleo plugin: installing overrides for",self.c.shortFileName()
        tree = self.c.frame.tree # NOT leoTkinterTree.leoTkinterTree
        g.funcToMethod(self.setUnselectedHeadlineColors,tree)
        g.funcToMethod(self.setDisabledHeadlineColors,tree)
        
        #self.c.frame.tree.PopupMenuTable.append()
        
        
        self.handlers = [
            #("draw-outline-text-box",self.draw),
            #("redraw-entire-outline",self.clear_canvas),
            #("iconrclick1",self.show_menu),
            ("save1",self.dropEmptyAll),
            ("enable-popup-menu-items",self.show_menu),
            ("close-frame",self.close),
        ]
        for i in self.handlers:
            leoPlugins.registerHandler(i[0], i[1])
    #@nonl
    #@-node:AGP.20230207163742.15:__init__()
    #@+node:AGP.20230207163742.19:close
    def close(self, tag, key):
        "unregister handlers on closing commander"
        
        if self.c != key['c']: return  # not our problem
    
        for i in self.handlers:
            leoPlugins.unregisterHandler(i[0], i[1])
    #@-node:AGP.20230207163742.19:close
    #@+node:AGP.20230207163742.20:attributes...
    #@+at
    # These methods should really be part of vnode in accordance with the 
    # principles
    # of encapsulation and information hiding.
    # 
    # annotate was the previous name of this plugin, which is why the default 
    # values
    # for several keyword args is 'annotate'.
    #@-at
    #@nonl
    #@+node:AGP.20230207163742.24:getat
    def getat(self, node, attrib):
        "new attrbiute getter"
        
        if (not hasattr(node,'unknownAttributes') or
            not node.unknownAttributes.has_key("annotate") or
            not type(node.unknownAttributes["annotate"]) == type({}) or
            not node.unknownAttributes["annotate"].has_key(attrib)):
                
            if attrib == "priority":
                return 9999
            else:
                return ""
        
        x = node.unknownAttributes["annotate"][attrib]
        if type(x) == self.typePickle:
            node.unknownAttributes["annotate"][attrib] = x.get()
            return x.get()
        else:
            return x
    #@nonl
    #@-node:AGP.20230207163742.24:getat
    #@+node:AGP.20230207163742.26:setat
    def setat(self, node, attrib, val):
        "new attrbiute setter"
        
        isDefault = self.testDefault(attrib, val)
        
        if (not hasattr(node,'unknownAttributes') or
            not node.unknownAttributes.has_key("annotate") or
            type(node.unknownAttributes["annotate"]) != type({})):
            # dictionary doesn't exist
            
            if isDefault:
                return  # don't create dict. for default value
        
            if not hasattr(node,'unknownAttributes'):  # node has no unknownAttributes
                node.unknownAttributes = {}
                node.unknownAttributes["annotate"] = {}
            else:  # our private dictionary isn't present
                if (not node.unknownAttributes.has_key("annotate") or
                    type(node.unknownAttributes["annotate"]) != type({})):
                    node.unknownAttributes["annotate"] = {}
                
            node.unknownAttributes["annotate"][attrib] = val
            
            return
            
        # dictionary exists
        
        node.unknownAttributes["annotate"][attrib] = val
        
        if isDefault:  # check if all default, if so drop dict.
            self.dropEmpty(node, dictOk = True)
    #@-node:AGP.20230207163742.26:setat
    #@+node:AGP.20230207163742.25:testDefault
    def testDefault(self, attrib, val):
        "return true if val is default val for attrib"
        
        # if type(val) == self.typePickle: val = val.get()
        # not needed as only dropEmpty would call with such a thing, and it checks first
        
        return attrib == "priority" and val == 9999 or val == ""
    #@nonl
    #@-node:AGP.20230207163742.25:testDefault
    #@+node:AGP.20230207163742.27:dropEmptyAll
    def dropEmptyAll(self,tag,key):
        "search whole tree for empty nodes"
        
        cnt = 0
        c = key.get('c')
        #print "node_colors.c",self,c
        for p in c.allNodes_iter(): 
            if self.dropEmpty(p.v): cnt += 1
        
        g.es("cleo: dropped %d empty dictionaries" % cnt)
    #@-node:AGP.20230207163742.27:dropEmptyAll
    #@+node:AGP.20230207163742.28:dropEmpty
    def dropEmpty(self, node, dictOk = False):
    
        if (dictOk or
            hasattr(node,'unknownAttributes') and
            node.unknownAttributes.has_key("annotate") and
            type(node.unknownAttributes["annotate"]) == type({})):
                
            isDefault = True
            for ky, vl in node.unknownAttributes["annotate"].iteritems():
                if type(vl) == self.typePickle:
                    node.unknownAttributes["annotate"][ky] = vl = vl.get()
                if not self.testDefault(ky, vl):
                    isDefault = False
                    break
                    
            if isDefault:  # no non-defaults seen, drop the whole cleo dictionary
                del node.unknownAttributes["annotate"]
                self.c.setChanged(True)
                return True
                
        return False
        
    #@nonl
    #@-node:AGP.20230207163742.28:dropEmpty
    #@-node:AGP.20230207163742.20:attributes...
    #@+node:AGP.20230207163742.29:safe_del
    def safe_del(self, d, k):
        "delete a key from a dict. if present"
        if d.has_key(k): del d[k]
    #@nonl
    #@-node:AGP.20230207163742.29:safe_del
    #@+node:AGP.20230207163742.31:remove_colours
    def remove_colours(self,v):
    
        self.setat(v, 'fg', '')
        self.setat(v, 'bg', '')
        self.safe_del(self.pickles, 'fg')
        self.safe_del(self.pickles, 'bg')
        self.c.redraw()
    #@nonl
    #@-node:AGP.20230207163742.31:remove_colours
    #@+node:AGP.20230207163742.32:addvar_colour
    def addvar_colour(self,var):
        
        import tkColorChooser
        
        myColor = '#000080'
        myColor = tkColorChooser.askcolor(myColor)
        if myColor[0] == None:
            g.es("No colour selected")
            return
                
        myColor = "#%02x%02x%02x" % myColor[0]
    
        if not self.colours.count(myColor):
            self.colours.insert(0, myColor)
            g.es("Added %s to the colour list" % (myColor))
        else:
            g.es("%s already on the colour list" % (myColor))
        
        
        var.set(myColor)
        self.redraw()
    #@-node:AGP.20230207163742.32:addvar_colour
    #@+node:AGP.20230207163742.33:custom_colours
    # use return values to set the colours so no need to muck around when loading up files.
    
    def custom_colours(self,v):
    
        ''' Returns the vnodes custom colours if it has them '''
        
        fg, bg = None, None
    
        # XXX This is ugly and inefficient !!
        
        # User defined colours overrides all
        fgv = self.getat(v, 'fg') # d.get('fg')
        if fgv:
            f = fgv
            if f:
                fg = f
    
        bgv = self.getat(v, 'bg') # d.get('bg')
        if bgv:
            b = bgv
            if b:
                bg = b
    
        #print "> (%s,%s) %s" % (fg,bg,v.headString())
        return fg,bg
    #@nonl
    #@-node:AGP.20230207163742.33:custom_colours
    #@+node:AGP.20230207163742.53:setUnselectedHeadlineColors
    def setUnselectedHeadlineColors (self,p):
        
        # unlike handlers, override commands don't need to check self.c against other c
        c = self.c
       
        if hasattr(p,'edit_widget'):  #temporary cvs transitional code
            w = p.edit_widget()
        else:
            w = c.edit_widget(p)
    
        fg, bg = self.custom_colours(p.v)
        
        nt = self.c.frame.tree.nodetext
        
        fg = fg or nt['fg']#fg or g.theme['shade'](0.7)#c.config.getColor("headline_text_unselected_foreground_color") or tree.head_fg
        bg = bg or nt['bg']#bg or g.theme['shade'](0.05)#c.config.getColor("headline_text_unselected_background_color") or tree.head_bg
    
        try:
            w.configure(state="disabled",highlightthickness=0,fg=fg,bg=bg)
        except:
            g.es_exception()
    #@-node:AGP.20230207163742.53:setUnselectedHeadlineColors
    #@+node:AGP.20230207163742.54:setDisabledHeadlineColors
    def setDisabledHeadlineColors (self,p):
    
        c = self.c
        
        if hasattr(p,'edit_widget'):  #temporary cvs transitional code
            w = p.edit_widget()
        else:
            w = c.edit_widget(p)
    
        fg, bg = self.custom_colours(p.v)
        
        tree = self.c.frame.tree
        
        fg = fg or g.theme['shade'](0.9)#tree.head_bg
        bg = bg or g.theme['shade'](0.2)#tree.head_fg
        
    
        try:
            #w.configure(state="disabled",highlightthickness=0,fg=fg,bg=bg)
            w.configure(state="disabled",
            highlightthickness=0,
            fg=fg,
            bg=bg,
            selectbackground=tree.edithead_fg,
            selectforeground=tree.edithead_bg,
            highlightbackground=tree.edithead_bg)
        except:
            g.es_exception()
            
            
    #@-node:AGP.20230207163742.54:setDisabledHeadlineColors
    #@+node:AGP.20230207163742.58:colours_menu()
    def colours_menu(self,parent, p):
        
        self.prep_pickle(p.v, 'fg')
        self.prep_pickle(p.v, 'bg')
    
        for var in (self.pickles['fg'].get(), self.pickles['bg'].get()):
            if var and var != '' and var != 'Other' and not self.colours.count(var):
                self.colours.insert(0, var)
                g.es("Added %s to the colour list" % (var))
            
        
        
        for label,var in (('Foreground',self.pickles['fg']),('Background',self.pickles['bg'])):
            menu = Tk.Menu(parent,tearoff=0,takefocus=1)
            
            
            menu.add_command(label="Choose...", command=lambda v=var:self.addvar_colour(v))
            
            for color in self.colours:
                menu.add_radiobutton(label=color, variable=var, value=color, command=self.redraw, background=color)
            
            parent.add_cascade(label=label,underline=0,menu=menu)
    
    
        parent.add_command(label='Reset', underline=0,command=lambda v=p.v:self.remove_colours(v))
    #@-node:AGP.20230207163742.58:colours_menu()
    #@+node:AGP.20230207163742.64:show_menu()
    def show_menu (self,tag,k):
    
        if k['c'] != self.c: return  # not our problem
    
        if self.menu:
        #    # Destroy any previous popup.
        #    self.menu.unpost()
            self.menu.destroy()
            
        p = k['p']
        v = k['p'].v ## EKR
        
        self.pickles = {}  # clear dict. of TkPickleVars
        self.pickleV = v
        self.pickleP = p.copy()
        
        # Create the menu.
        #self.menu = menu = Tk.Menu(None,tearoff=0,takefocus=0)
        parent_menu = self.c.frame.tree.popupMenu
        
        # g.doHook("enable-popup-menu-items",c=c,p=p,v=p,event=event):
        self.menu = menu = Tk.Menu(None,tearoff=0,takefocus=0)
        self.colours_menu(menu,p)
        #print "show menu",self.menu
        parent_menu.add_separator()
        parent_menu.add_cascade(label="Colors",menu=self.menu)
        
        
        
        return False # continue menu creation in leo
    #@nonl
    #@-node:AGP.20230207163742.64:show_menu()
    #@+node:AGP.20230207174829:prep_pickle
    def prep_pickle(self, v, pkl, default = None):
        "prepare a TkPickleVar in self.pickles for a menu write back"
    
        self.pickles[pkl] = TkPickleVar()
        self.pickles[pkl].set(self.getat(v, pkl))
    #@-node:AGP.20230207174829:prep_pickle
    #@+node:AGP.20230207174930:redraw
    def redraw(self):
        "redraw after menu used"
        
        # IMPORTANT ASSUMPTION: called only after menu used
    
        # read updates from menu choice
        
        # Tk seems to use menu label when '' is used as value?
        # note, keys not present if coming via clear_all
        
        
        for ky, vl in self.pickles.iteritems():
            self.setat(self.pickleV, ky, vl.get())
    
        
        c = self.c
        c.setChanged(True)
        c.redraw_now()
    #@nonl
    #@-node:AGP.20230207174930:redraw
    #@-others
#@nonl
#@-node:AGP.20230207163742.14:class rcController
#@-others
#@nonl
#@-node:AGP.20230207163742:@thin node_colors.py
#@-leo
