#@+leo-ver=4
#@+node:@file version_file.py
#@<< docstring >>
#@+node:<< docstring >>
'''A plugin to update a VERSION file'''
#@nonl
#@-node:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4

# Contributed by agp

#@<< imports >>
#@+node:<< imports >>
import leoGlobals as g
import leoPlugins
import time,os
#@-node:<< imports >>
#@nl
__version__ = '1.0'

current_knode = None
    
#@+others
#@+node:init
def init ():
    leoPlugins.registerHandler("save2", on_save)
    g.plugin_signon(__name__)
            
    return True
#@nonl
#@-node:init
#@+node:on_save
def on_save(tag,keywords):
    c = keywords.get("c")
    if not c: return
    
    v = c.rootVnode()
    while v:
        h = v.headString()
        if g.match_word(h,0,"@version"):
            updateVersionFile(h[9:],c.frame.openDirectory)
            
        v = v.threadNext()
    
    
#@nonl
#@-node:on_save
#@+node:XupdateVersionFile()
def XupdateVersionFile(filename):
    #print "update version",filename
    path = os.path
    vdir = path.split(filename)[0]
    
    for f in os.listdir(vdir):
        name,ext = path.splitext(f)
        if name == "VERSION":
            try:
                vfile = open(vdir+"/"+f,"r+")
                version = vfile.readlines()
                if len(version) > 1:    return#error

                version = version[0].split(".")
                if len(version) > 1:
                    version[-1] = time.strftime("%Y%m%d%H%M%S",time.gmtime())
                else:
                    return
                    
                version = ".".join(version)
                vfile.seek(0)
                
                vfile.write(version)
                vfile.truncate()
                vfile.close()
                g.es(f+" = "+version)                
                
            except IOError:
                pass
        
#@nonl
#@-node:XupdateVersionFile()
#@+node:updateVersionFile()
def updateVersionFile(filename,opendir):
    #print "update version",filename
    #path = os.path
    #vdir = path.split(filename)[0]
    f = filename
    oldcwd = os.getcwd()
    if opendir != "":
        os.chdir(opendir)
    else:
        return
        
    try:
        
        #print os.getcwd(),opendir
        
        
        vfile = open(f,"r+")
        version = vfile.readlines()
        if len(version) > 1:    return#error

        version = version[0].split(".")
        if len(version) > 1:
            version[-1] = time.strftime("%Y%m%d%H%M%S",time.gmtime())
        else:
            return
                    
        version = ".".join(version)
        vfile.seek(0)
        vfile.write(version)
        vfile.truncate()
        vfile.close()
        
        g.es(f+" = "+version) #confirm update
        #print time.time()
                
    except IOError,e:
        pass#g.es(e,color="red") #silently fail
        
    os.chdir(oldcwd)
#@nonl
#@-node:updateVersionFile()
#@-others
#@nonl
#@-node:@file version_file.py
#@-leo
