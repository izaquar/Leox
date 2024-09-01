#@+leo-ver=4-thin
#@+node:AGP.20240902191147:@thin version_file.py
#@<< docstring >>
#@+node:AGP.20240902191147.1:<< docstring >>
'''A plugin to update a VERSION file'''
#@nonl
#@-node:AGP.20240902191147.1:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4

# Contributed by agp

#@<< imports >>
#@+node:AGP.20240902191147.2:<< imports >>
import leoGlobals as g
import leoPlugins
import time,os
#@-node:AGP.20240902191147.2:<< imports >>
#@nl
__version__ = '1.0'

current_knode = None
    
#@+others
#@+node:AGP.20240902191147.3:init
def init ():
    leoPlugins.registerHandler("save2", on_save)
    g.plugin_signon(__name__)
            
    return True
#@nonl
#@-node:AGP.20240902191147.3:init
#@+node:AGP.20240902191147.4:on_save
def on_save(tag,keywords):
    c = keywords.get("c")
    if not c: return
    
    v = c.rootVnode()
    while v:
        h = v.headString()
        if g.match_word(h,0,"@version"):
            updateVersionFile(h[9:])
            
        v = v.threadNext()
    
    
#@nonl
#@-node:AGP.20240902191147.4:on_save
#@+node:AGP.20240902191425:XupdateVersionFile()
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
#@-node:AGP.20240902191425:XupdateVersionFile()
#@+node:AGP.20240903161242:updateVersionFile()
def updateVersionFile(filename):
    #print "update version",filename
    #path = os.path
    #vdir = path.split(filename)[0]
    f = filename
    try:
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
        
#@nonl
#@-node:AGP.20240903161242:updateVersionFile()
#@-others
#@nonl
#@-node:AGP.20240902191147:@thin version_file.py
#@-leo
