#! /usr/bin/env python
#@+leo-ver=4-thin
#@+node:AGP.20250415230112.3:@thin leo.py 
#@@first

"""Entry point for Leo in Python."""

#@@language python
#@@tabwidth -4


# Warning: do not import any Leo modules here!
# Doing so would make g.app invalid in the imported files.
import os
import string
import sys

#@+others
#@+node:AGP.20250415230112.4:run & allies
def run(fileName=None,pymacs=None,*args,**keywords):
    
    """Initialize and run Leo"""
    
    
    if not isValidPython(): return
    #@    << import leoGlobals and leoApp >>
    #@+node:AGP.20250415230112.5:<< import leoGlobals and leoApp >>
    # Import leoGlobals, but do NOT set g.
    try:
        import leoGlobals
    except ImportError:
        print "Error importing leoGlobals.py"
    
    # Create the application object.
    try:
        import leoApp
        leoGlobals.app = leoApp.LeoApp()
    except ImportError:
        print "Error importing leoApp.py"
        
    # NOW we can set g.
    g = leoGlobals
    assert(g.app)
    #@-node:AGP.20250415230112.5:<< import leoGlobals and leoApp >>
    #@nl
    
    g.exe_dir = exe_dir
    g.computeStandardDirectories()
    
    import leoLang
    
    leoLang.import_languages()
    
    if pymacs:
        script = windowFlag = False
    else:
        script, windowFlag = getBatchScript() # Do early so we can compute verbose next.
    
    verbose = script is None
    g.app.setLeoID(verbose=verbose) # Force the user to set g.app.leoID.
    
    #@    << import leoNodes and leoConfig >>
    #@+node:AGP.20250415230112.6:<< import leoNodes and leoConfig >>
    try:
        import leoNodes
    except ImportError:
        print "Error importing leoNodes.py"
        import traceback ; traceback.print_exc()
    try:
        import leoConfig
    except ImportError:
        print "Error importing leoConfig.py"
        import traceback ; traceback.print_exc()
    #@-node:AGP.20250415230112.6:<< import leoNodes and leoConfig >>
    #@nl
    
    g.app.nodeIndices = leoNodes.nodeIndices(g.app.leoID)
    g.app.config = leoConfig.configClass()
    
    fileName = completeFileName(fileName)
    reportDirectories(verbose)
    

    # Read settings *after* setting g.app.config.
    # Read settings *before* opening plugins.  This means if-gui has effect only in per-file settings.
    g.app.config.readSettingsFiles(fileName,verbose)
    
    #
    
    g.app.setEncoding()
    

    if pymacs:
        createNullGuiWithScript(None)
    elif script:
        if windowFlag:
            g.app.createTkGui() # Creates global windows.
            g.app.gui.setScript(script)
            sys.args = []
        else:
            createNullGuiWithScript(script)
        fileName = None
    
    # Load plugins. Plugins may create g.app.gui.
    g.doHook("start1")
    
    if g.app.killed: return # Support for g.app.forceShutdown.
    
    # Create the default gui if needed.
    if g.app.gui == None:
        g.app.createTkGui() # Creates global windows.
        
    
    
    # Initialize tracing and statistics.
    g.init_sherlock(args)
    
    # New in 4.3: clear g.app.initing _before_ creating the frame.
    g.app.initing = False # "idle" hooks may now call g.app.forceShutdown.
    
    # Create the main frame.  Show it and all queued messages.
    c,frame = createFrame(fileName)
    if not frame: return
    
    g.app.trace_gc          = c.config.getBool('trace_gc')
    g.app.trace_gc_calls    = c.config.getBool('trace_gc_calls')
    g.app.trace_gc_verbose  = c.config.getBool('trace_gc_verbose')
    
    if g.app.disableSave:
        g.es("disabling save commands",color=g.theme['error'])
    
    g.app.writeWaitingLog()
    p = c.currentPosition()
    g.doHook("start2",c=c,p=p,v=p,fileName=fileName)
    
    if c.config.getBool('allow_idle_time_hook'):
        g.enableIdleTimeHook()
    
    if not fileName:
        c.redraw_now()
    
    c.bodyWantsFocus()
    
    g.app.gui.runMainLoop()
#@+node:AGP.20250415230112.7:isValidPython
def isValidPython():

    message = """\
Leo requires Python 2.2.1 or higher.
You may download Python from http://python.org/download/
"""
    try:
        # This will fail if True/False are not defined.
        import leoGlobals as g
    except ImportError:
        print "isValidPython: can not import leoGlobals"
        return 0
    except:
        print "isValidPytyhon: unexpected exception: import leoGlobals.py as g"
        import traceback ; traceback.print_exc()
        return 0
    try:
        version = '.'.join([str(sys.version_info[i]) for i in (0,1,2)])
        ok = g.CheckVersion(version,'2.2.1')
        if not ok:
            print message
            g.app.gui.runAskOkDialog(None,"Python version error",message=message,text="Exit")
        return ok
    except:
        print "isValidPython: unexpected exception: g.CheckVersion"
        import traceback ; traceback.print_exc()
        return 0
#@nonl
#@-node:AGP.20250415230112.7:isValidPython
#@+node:AGP.20250415230112.8:completeFileName (leo.py)
def completeFileName (fileName):
    
    import leoGlobals as g
    
    if not fileName:
        return None
        
    # This does not depend on config settings.
    fileName = g.os_path_join(os.getcwd(),fileName)

    head,ext = g.os_path_splitext(fileName)
    if not ext:
        fileName = fileName + ".leo"

    return fileName
#@-node:AGP.20250415230112.8:completeFileName (leo.py)
#@+node:AGP.20250415230112.9:createFrame (leo.py)
def createFrame (fileName):
    
    """Create a LeoFrame during Leo's startup process."""
    
    import leoGlobals as g

    # Try to create a frame for the file.
    if fileName:
        if g.os_path_exists(fileName):
            ok, frame = g.openWithFileName(fileName,None)
            if ok:
                return frame.c,frame

    # Create a _new_ frame & indicate it is the startup window.
    c,frame = g.app.newLeoCommanderAndFrame(fileName=fileName)
    
    frame.setInitialWindowGeometry()
    frame.resizePanesToRatio(frame.ratio,frame.secondary_ratio)
    
    frame.startupWindow = True
    # 3/2/05: Call the 'new' hook for compatibility with plugins.
    g.doHook("new",old_c=None,c=c,new_c=c)

    # Report the failure to open the file.
    if fileName:
        g.es("File not found: " + fileName)

    frame.show()

    return c,frame
#@nonl
#@-node:AGP.20250415230112.9:createFrame (leo.py)
#@+node:AGP.20250415230112.10:createNullGuiWithScript (leo.py)
def createNullGuiWithScript (script):
    
    import leoGlobals as g
    import leoGui
    
    g.app.batchMode = True
    g.app.gui = leoGui.nullGui("nullGui")
    if not g.app.root:
        g.app.root = g.app.gui.createRootWindow()
    g.app.gui.finishCreate()
    g.app.gui.setScript(script)
#@-node:AGP.20250415230112.10:createNullGuiWithScript (leo.py)
#@+node:AGP.20250415230112.11:getBatchScript
def getBatchScript ():
    
    import leoGlobals as g
    windowFlag = False
    
    name = None ; i = 1 # Skip the dummy first arg.
    while i + 1 < len(sys.argv):
        arg = sys.argv[i].strip().lower()
        if arg in ("--script","-script"):
            name = sys.argv[i+1].strip() ; break
        if arg in ("--script-window","-script-window"):
            name = sys.argv[i+1].strip() ; windowFlag = True ; break
        i += 1

    if not name:
        return None, windowFlag
    name = g.os_path_join(g.app.loadDir,name)
    try:
        f = None
        try:
            f = open(name,'r')
            script = f.read()
            # g.trace("script",script)
        except IOError:
            g.es_print("can not open script file: " + name, color=g.theme['error'])
            script = None
    finally:
        if f: f.close()
        return script, windowFlag
#@-node:AGP.20250415230112.11:getBatchScript
#@+node:AGP.20250415230112.12:reportDirectories
def reportDirectories(verbose):
    
    import leoGlobals as g
   
    if verbose:
        for kind,theDir in (
            ("global config",g.app.globalConfigDir),
            ("home",g.app.homeDir),
        ):
            g.es("%s dir: %s" % (kind,theDir),color="blue")
#@-node:AGP.20250415230112.12:reportDirectories
#@-node:AGP.20250415230112.4:run & allies
#@+node:AGP.20250415230112.13:profile
#@+at 
#@nonl
# To gather statistics, do the following in a Python window, not idle:
# 
#     import leo
#     leo.profile()  (this runs leo)
#     load leoDocs.leo (it is very slow)
#     quit Leo.
#@-at
#@@c

def profile ():
    
    """Gather and print statistics about Leo"""

    import profile, pstats
    
    # name = "c:/prog/test/leoProfile.txt"
    name = g.os_path_abspath(g.os_path_join(g.app.loadDir,'..','test','leoProfile.txt'))
    
    profile.run('leo.run()',name)

    p = pstats.Stats(name)
    p.strip_dirs()
    p.sort_stats('cum','file','name')
    p.print_stats()
#@-node:AGP.20250415230112.13:profile
#@-others

#cwdlog = file("cwd.log","w")

if __name__ == "__main__":
    #print sys.argv
    if len(sys.argv) > 1:
        if sys.platform=="win32": # Windows
            fileName = string.join(sys.argv[1:],' ')
        else:
            fileName = sys.argv[1]
        
        exe_dir,exe_name = os.path.split(sys.argv[0]) # agp... fix frozen exe
        
        #exe_dir,exe_name = os.getcwd(),sys.argv[0]
        
        try:
            run(fileName)
        except Exception,e:
            print e
        
    else:
        exe_dir,exe_name = os.getcwd(),sys.argv[0]
        run()
        
#    cwdlog.write(str(sys.argv))
#    cwdlog.write("\n"+exe_dir+"\n")
#    cwdlog.write(exe_name)

#cwdlog.close()
#@-node:AGP.20250415230112.3:@thin leo.py 
#@-leo
