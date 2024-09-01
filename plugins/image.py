#@+leo-ver=4-thin
#@+node:edream.110203113231.753:@thin image.py
'''Handle @image nodes.'''

#@+at
# Based on work by Gil Scwartz.
# Brent Burley provided many important insights. See:
# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52264
#@-at
#@@c

#@@language python
#@@tabwidth -4

#@<< imports >>
#@+node:ekr.20050101090207.1:<< imports >>
import leoGlobals as g
import leoPlugins

Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)

try:
    #import ImageTk
    from PIL import Image,ImageTk
except ImportError:
    #g.es_exception()
    ImageTk = None
#@nonl
#@-node:ekr.20050101090207.1:<< imports >>
#@nl
#@<< version history >>
#@+node:ekr.20060619092335:<< version history >>
#@@nocolor

#@+at
# 
# 1.3 EKR: Attempt to use ImageTk if it exists.
# Does not work on my machine, but that may be an installation problem.
# 
# 1.3exe AGP: Using ImageTk... require PIL/Pillow
#@-at
#@nonl
#@-node:ekr.20060619092335:<< version history >>
#@nl

__version__ = "1.3" # Set version for the plugin handler.

#@+others
#@+node:edream.110203113231.754:onSelect
def onSelect (tag,keywords):

    new_v = keywords.get("new_v")
    h = new_v.headString()
    if h[:7] == "@image ":
        filename = h[7:]
        #@        << Select Image >>
        #@+node:edream.110203113231.755:<< Select Image >>
        # Display the image file in the text pane, if you can find the file
        a = g.app
        c = keywords.get("c")
        body = c.frame.body
        photo = None
        
        if os.path.isfile(filename):
            print "IMAGETK",ImageTk 
            if ImageTk: # ImageTk understands several file formats.
                try:
                    #photo = ImageTk.PhotoImage(master=a.root, file=filename)
                    g.es("opening: %s" % (filename))
                    
                    photo = Image.open(filename)
                    
                    
                    pw = float(photo.width)
                    ph = float(photo.height)
            
                    bw = float(body.bodyCtrl.winfo_width())
                    bh = float(body.bodyCtrl.winfo_height())
                    
                    if pw > bw:
                        ph = bw/pw*ph
                        pw = bw
                
                    if ph > bh:
                        pw = bh/ph*pw
                        ph = bh
                    print "photo",bw,bh,pw,ph
                    photo = ImageTk.PhotoImage(photo.resize((int(pw), int(ph)), Image.ANTIALIAS))
            
                    padding = int((bw - pw - 16) / 2)
                    padding = max(0,padding)
                    a.gsimage = body.bodyCtrl.image_create("1.0",image=photo,padx=16,pady=16)
                    
                    
                except Exception:
                    g.es_exception()
                    g.es("ImageTk.PhotoImage failed")
                    return
                    
            # Nicely display the image at the center top and push the text below.
            a.gsphoto = photo # This is soooo important.
            
            
            
            
            
            
            
            
            
        else:
            g.es("warning: missing image file")
        #@nonl
        #@-node:edream.110203113231.755:<< Select Image >>
        #@nl
#@nonl
#@-node:edream.110203113231.754:onSelect
#@+node:edream.110203113231.756:onUnselect
def onUnselect (tag,keywords):

    a = g.app
    old_v = keywords.get("old_v")
    if old_v:
        h = old_v.headString()
        if h[:7] == "@image ":
            #@            << Unselect Image >>
            #@+node:edream.110203113231.757:<< Unselect Image >>
            # Erase image if it was previously displayed
            a = g.app ; c = keywords.get("c")
            
            if a.gsimage:
                try:
                     c.frame.body.bodyCtrl.delete(a.gsimage)
                except:
                    g.es("info: no image to erase")
            
            # And forget about it
            a.gsimage = None
            a.gsphoto = None
            #@-node:edream.110203113231.757:<< Unselect Image >>
            #@nl
    else: # Leo is initializing.
        a.gsphoto = None # Holds our photo file
        a.gsimage = None # Holds our image instance within the text pane
#@nonl
#@-node:edream.110203113231.756:onUnselect
#@-others

import os

if Tk: # Ok for unit testing.

    if g.app.gui is None:
        g.app.createTkGui(__file__)

    if g.app.gui.guiName() == "tkinter":
        
        leoPlugins.registerHandler("select2", onSelect)
        leoPlugins.registerHandler("unselect1", onUnselect)
        g.plugin_signon(__name__)
#@nonl
#@-node:edream.110203113231.753:@thin image.py
#@-leo
