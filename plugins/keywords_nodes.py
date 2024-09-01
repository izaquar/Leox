#@+leo-ver=4-thin
#@+node:AGP.20240831123716:@thin keywords_nodes.py
#@<< docstring >>
#@+node:AGP.20240831123716.1:<< docstring >>
'''A plugin to add keywords to a language'''
#@nonl
#@-node:AGP.20240831123716.1:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4

# Contributed by agp

#@<< imports >>
#@+node:AGP.20240831123716.2:<< imports >>

import leoGlobals as g
import leoPlugins
import leoColor
#@-node:AGP.20240831123716.2:<< imports >>
#@nl
__version__ = '1.0'

current_knode = None
    
#@+others
#@+node:AGP.20240831123716.4:init
def init ():
    leoPlugins.registerHandler(('new','open2'), on_open)
    leoPlugins.registerHandler("select2", on_select2)
    g.plugin_signon(__name__)
            
    return True
#@nonl
#@-node:AGP.20240831123716.4:init
#@+node:AGP.20240831123716.22:on_open
#  scan the outline and process @read nodes.
def on_open (tag,keywords):

    c = keywords.get("c")
    if not c: return

    v = c.rootVnode()
    g.es("scanning for @keywords nodes...",color="blue")
    #c.beginUpdate()
    while v:
        h = v.headString()
        if g.match_word(h,0,"@keywords"):
            update_keywords(v)
            
        v = v.threadNext()
    #c.endUpdate()
#@nonl
#@-node:AGP.20240831123716.22:on_open
#@+node:AGP.20240831123716.26:on_select2
def on_select2 (tag,keywords):
    global current_knode
    
    c = keywords.get("c")
    v = c.currentVnode()
    
    if current_knode != None and current_knode != v:
        update_keywords(current_knode)
    
    current_knode = None
    
    
    h = v.headString()
    if g.match_word(h,0,"@keywords"):
        current_knode = v
    
#@-node:AGP.20240831123716.26:on_select2
#@+node:AGP.20240831131440:update_keywords(v)
def update_keywords(v):
    
    h = v.headString()
    lang = h[10:]
    langk = lang+"_keywords"
    bc = leoColor.baseColorizer
    
    if hasattr(bc,langk):
        kwds = getattr(bc, langk)
        for kw in v.bodyString().split():
            if kw not in kwds:
                kwds.append(kw)
        g.es(lang+" keywords updated!",color="blue")
    else:
        g.es(lang+" is an invalid language!",color="red")
#@nonl
#@-node:AGP.20240831131440:update_keywords(v)
#@-others
#@nonl
#@-node:AGP.20240831123716:@thin keywords_nodes.py
#@-leo
