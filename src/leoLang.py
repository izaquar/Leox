#@+leo-ver=4-thin
#@+node:AGP.20250415230112.299:@thin leoLang.py
"""Multi-language module for Leo."""

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leo

languages = {}

#@+others
#@+node:AGP.20250415230112.300:import_languages()
def import_languages():
    from imp import find_module,load_module
    from os import path,listdir
    import traceback
    langdir = leo.leoDir+"/config/languages"
    
    global languages
    
    
    langfiles = listdir(langdir)
    print "Importing Languages:",
    for f in langfiles:
        n,ext = path.splitext(f)
        
        if ext == ".py":
            try:
                lmod = load_module(n,*find_module(n,[langdir]))
                languages[n] = lmod
                if hasattr(lmod,"alias"):
                    for a in lmod.alias:
                        languages[a] = lmod
                
                print " ",n,
            except Exception,e:
                print ""
                print "Error Importing Languages:",n,e
                print traceback.print_exc()
            
    print ""
#@nonl
#@-node:AGP.20250415230112.300:import_languages()
#@-others

import_languages()

#@-node:AGP.20250415230112.299:@thin leoLang.py
#@-leo
