#@+leo-ver=4-thin
#@+node:ekr.20031218072017.3439:@thin leoPlugins.py
"""Install and run Leo plugins.

On startup:
- doPlugins() calls loadHandlers() to import all
  mod_XXXX.py files in the Leo directory.
- Imported files should register hook handlers using the
  registerHandler and registerExclusiveHandler functions.
  Only one "exclusive" function is allowed per hook.

After startup:
- doPlugins() calls doHandlersForTag() to handle the hook.
- The first non-None return is sent back to Leo.
"""

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import glob

handlers = {}
loadedModules = {} # Keys are module names, values are modules.
loadingModuleNameStack = [] # The stack of module names.  Top is the module being loaded.

#@+others
#@+node:ekr.20050102094729:callTagHandler
def callTagHandler (bunch,tag,keywords):

    handler = bunch.fn ; moduleName = bunch.moduleName
    
    # if tag != 'idle': print 'callTagHandler',tag,keywords.get('c')

    # Make sure the new commander exists.
    if tag == 'idle':
        for key in ('c','new_c'):
            c = keywords.get(key)
            if c:
                # Make sure c exists and has a frame.
                if not c.exists or not hasattr(c,'frame'):
                    print 'skipping tag: c does not exists or does not have a frame.'
                    return None

    # Calls to registerHandler from inside the handler belong to moduleName.
    global loadingModuleNameStack
    loadingModuleNameStack.append(moduleName)
    result = handler(tag,keywords)
    loadingModuleNameStack.pop()
    return result
#@-node:ekr.20050102094729:callTagHandler
#@+node:ekr.20031218072017.3442:doHandlersForTag
def doHandlersForTag (tag,keywords):
    
    """Execute all handlers for a given tag, in alphabetical order.
    
    All exceptions are caught by the caller, doHook."""

    global handlers

    if g.app.killed:
        return None

    if handlers.has_key(tag):
        bunches = handlers.get(tag)
        # Execute hooks in some random order.
        # Return if one of them returns a non-None result.
        for bunch in bunches:
            val = callTagHandler(bunch,tag,keywords)
            if val is not None:
                return val

    if handlers.has_key("all"):
        bunches = handlers.get('all')
        for bunch in bunches:
            callTagHandler(bunch,tag,keywords)

    return None
#@-node:ekr.20031218072017.3442:doHandlersForTag
#@+node:ekr.20041001161108:doPlugins
def doPlugins(tag,keywords):
    
    if g.app.killed:
        return
        
    # g.trace(tag)
    
    if tag == "start1":
        loadHandlers()

    return doHandlersForTag(tag,keywords)
#@-node:ekr.20041001161108:doPlugins
#@+node:ekr.20041111124831:getHandlersForTag
def getHandlersForTag(tags):
    
    import types

    if type(tags) in (types.TupleType,types.ListType):
        result = []
        for tag in tags:
            fn = getHandlersForOneTag(tag) 
            result.append((tag,fn),)
        return result
    else:
        return getHandlersForOneTag(tags)

def getHandlersForOneTag (tag):

    global handlers

    bunch = handlers.get(tag)
    return bunch.fn
#@-node:ekr.20041111124831:getHandlersForTag
#@+node:ekr.20041114113029:getPluginModule
def getPluginModule (moduleName):
    
    global loadedModules
    
    return loadedModules.get(moduleName)
#@-node:ekr.20041114113029:getPluginModule
#@+node:ekr.20041001160216:isLoaded
def isLoaded (name):
    
    if name.endswith('.py'): name = name[:-3]
    
    return name in g.app.loadedPlugins
#@-node:ekr.20041001160216:isLoaded
#@+node:ekr.20031218072017.3440:loadHandlers
def loadHandlers():

    """Load all enabled plugins from the plugins directory"""
    
    plugins_path = g.os_path_join(g.app.loadDir,"..","plugins")
    manager_path = g.os_path_join(plugins_path,"pluginsManager.txt")
    
    files = glob.glob(g.os_path_join(plugins_path,"*.py"))
    files = [g.os_path_abspath(theFile) for theFile in files]
    
    #@    << set enabled_files from pluginsManager.txt >>
    #@+node:ekr.20031218072017.3441:<< set enabled_files from pluginsManager.txt >>
    if not g.os_path_exists(manager_path):
        enabled_files = files   #agp return
        disabled_files = []
        
    else:
    # New in 4.3: The first reference to a plugin in pluginsManager.txt controls.
    
        enabled_files = []
        disabled_files = []
        try:
            theFile = open(manager_path)
            #print 'manager path',manager_path
            lines = theFile.readlines()
            for s in lines:
                s = s.strip()
                if s:
                    if g.match(s,0,"#"):
                        s = s[1:].strip()
                        # Kludge: ignore comment lines containing a blank or not ending in '.py'.
                        if s and s.find(' ') == -1 and s[-3:] == '.py':
                            path = g.os_path_abspath(g.os_path_join(plugins_path,s))
                            if path not in enabled_files and path not in disabled_files:
                                # print 'disabled',path
                                disabled_files.append(path)
                    else:
                        path = g.os_path_abspath(g.os_path_join(plugins_path,s))
                        if path not in enabled_files and path not in disabled_files:
                            # print 'enbled',path
                            enabled_files.append(path)
            theFile.close()
        except IOError:
            g.es("Can not open: " + manager_path)
            # Don't import leoTest initially.  It causes problems.
            import leoTest ; leoTest.fail()
            return
        
    #@-node:ekr.20031218072017.3441:<< set enabled_files from pluginsManager.txt >>
    #@nl
    
    # Load plugins in the order they appear in the enabled_files list.
    g.es("Loading plugins: ",newline=False, color="blue") #agp
    if files and enabled_files:
        for theFile in enabled_files:
            if theFile in files:
                head,tail = g.os.path.split(theFile)
                g.es(tail+" ",newline=False, color="blue")
                loadOnePlugin(theFile)
                
    #g.es("Done!")
    # Note: g.plugin_signon adds module names to g.app.loadedPlugins 
    if g.app.loadedPlugins:
        g.es("%d plugins loaded" % (len(g.app.loadedPlugins)), color="blue")
#@-node:ekr.20031218072017.3440:loadHandlers
#@+node:ekr.20041113113140:loadOnePlugin
def loadOnePlugin (moduleOrFileName, verbose=False):
    
    global loadedModules,loadingModuleNameStack
    
    # g.trace(moduleOrFileName, g.callers())
    
    if moduleOrFileName.endswith('.py'):
        moduleName = moduleOrFileName [:-3]
    else:
        moduleName = moduleOrFileName
    moduleName = g.shortFileName(moduleName)

    if isLoaded(moduleName):
        module = loadedModules.get(moduleName)
        if verbose:
            s = 'plugin %s already loaded' % moduleName
            g.es_print(s,color="blue")
        return module

    plugins_path = g.os_path_join(g.app.loadDir,"..","plugins")
    moduleName = g.toUnicode(moduleName,g.app.tkEncoding)
    
    # This import will typically result in calls to registerHandler.
    # if the plugin does _not_ use the init top-level function.
    loadingModuleNameStack.append(moduleName)
    #print moduleName #agp
    result = g.importFromPath(moduleName,plugins_path)
    loadingModuleNameStack.pop()
    
    if result:
        loadingModuleNameStack.append(moduleName)
        try:
            # Indicate success only if init_result is True.
            init_result = result.init()
            if init_result:
                loadedModules[moduleName] = result
            else:
                g.es_print('%s.%s failed' % (moduleName,init_result),color="red")
                result = None
        except AttributeError:
            # No top-level init function.
            # Guess that the module was loaded correctly.
            loadedModules[moduleName] = result
        loadingModuleNameStack.pop()
        
    if result is None:
        s = 'can not load enabled %s plugin' % moduleName
        g.es_print(s,color="red")
    elif verbose:
        s = 'loaded %s plugin' % moduleName
        g.es_print(s,color="blue")
    
    return result
#@nonl
#@-node:ekr.20041113113140:loadOnePlugin
#@+node:ekr.20050110191444:printHandlers
def printHandlers (moduleName=None):
    
    if moduleName:
        print 'handlers for %s...' % moduleName
    else:
        print 'all plugin handlers...'

    modules = {}
    for tag in handlers.keys():
        bunches = handlers.get(tag)
        for bunch in bunches:
            name = bunch.moduleName
            tags = modules.get(name,[])
            tags.append(tag)
            modules[name] = tags
    keys = modules.keys()
    keys.sort()
    for key in keys:
        tags = modules.get(key)
        if moduleName in (None,key):
            for tag in tags:
                print '%25s %s' % (tag,key)
#@-node:ekr.20050110191444:printHandlers
#@+node:ekr.20031218072017.3444:registerExclusiveHandler
def registerExclusiveHandler(tags, fn):
    
    """ Register one or more exclusive handlers"""
    
    import types
    
    if type(tags) in (types.TupleType,types.ListType):
        for tag in tags:
            registerOneExclusiveHandler(tag,fn)
    else:
        registerOneExclusiveHandler(tags,fn)
            
def registerOneExclusiveHandler(tag, fn):
    
    """Register one exclusive handler"""
    
    global handlers, loadingModuleNameStack
    try:
        moduleName = loadingModuleNameStack[-1]
    except IndexError:
        moduleName = '<no module>'
    
    if 0:
        if g.app.unitTesting: print
        print '%6s %15s %25s %s' % (g.app.unitTesting,moduleName,tag,fn.__name__)
    
    if g.app.unitTesting: return

    if handlers.has_key(tag):
        g.es("*** Two exclusive handlers for '%s'" % tag)
    else:
        bunch = g.Bunch(fn=fn,moduleName=moduleName,tag='handler')
        handlers = [bunch]
#@-node:ekr.20031218072017.3444:registerExclusiveHandler
#@+node:ekr.20031218072017.3443:registerHandler
def registerHandler(tags,fn):
    
    """ Register one or more handlers"""

    import types

    if type(tags) in (types.TupleType,types.ListType):
        for tag in tags:
            registerOneHandler(tag,fn)
    else:
        registerOneHandler(tags,fn)

def registerOneHandler(tag,fn):
    
    """Register one handler"""
    
    global handlers, loadingModuleNameStack
    try:
        moduleName = loadingModuleNameStack[-1]
    except IndexError:
        moduleName = '<no module>'
    
    if 0:
        if g.app.unitTesting: print
        print '%6s %15s %25s %s' % (g.app.unitTesting,moduleName,tag,fn.__name__)

    items = handlers.get(tag,[])
    if fn not in items:
        
        bunch = g.Bunch(fn=fn,moduleName=moduleName,tag='handler')
        items.append(bunch)
        
    # g.trace(tag) ; g.printList(items)
    handlers[tag] = items
#@-node:ekr.20031218072017.3443:registerHandler
#@+node:ekr.20050110182317:unloadOnePlugin
def unloadOnePlugin (moduleOrFileName,verbose=False):
    
    if moduleOrFileName [-3:] == ".py":
        moduleName = moduleOrFileName [:-3]
    else:
        moduleName = moduleOrFileName
    moduleName = g.shortFileName(moduleName)

    if moduleName in g.app.loadedPlugins:
        if verbose:
            print 'unloading',moduleName
        g.app.loadedPlugins.remove(moduleName)
        
    for tag in handlers.keys():
        bunches = handlers.get(tag)
        bunches = [bunch for bunch in bunches if bunch.moduleName != moduleName]
        handlers[tag] = bunches
#@-node:ekr.20050110182317:unloadOnePlugin
#@+node:ekr.20041111123313:unregisterHandler
def unregisterHandler(tags,fn):
    
    import types

    if type(tags) in (types.TupleType,types.ListType):
        for tag in tags:
            unregisterOneHandler(tag,fn)
    else:
        unregisterOneHandler(tags,fn)

def unregisterOneHandler (tag,fn):

    global handlers
    
    if 1: # New code
        bunches = handlers.get(tag)
        bunches = [bunch for bunch in bunches if bunch.fn != fn]
        handlers[tag] = bunches
    else:
        fn_list = handlers.get(tag)
        if fn_list:
            while fn in fn_list:
                fn_list.remove(fn)
            handlers[tag] = fn_list
            # g.trace(handlers.get(tag))
#@-node:ekr.20041111123313:unregisterHandler
#@+node:ktenney.20060628092017.1:baseLeoPlugin
class baseLeoPlugin(object):
    #@    <<docstring>>
    #@+node:ktenney.20060628092017.2:<<docstring>>
    """A Convenience class to simplify plugin authoring
    
    .. contents::
    
    Usage
    =====
    
    
    Initialization
    --------------
    
    - import the base class::
        
        from leoPlugins import leoBasePlugin
    
    - create a class which inherits from leoBasePlugin::
        
        class myPlugin(leoBasePlugin):
            
    - in the __init__ method of the class, call the parent constructor::
        
        def __init__(self, tag, keywords):
            leoBasePlugin.__init__(self, tag, keywords)
            
    - put the actual plugin code into a method; for this example, the work
      is done by myPlugin.handler()
      
    - put the class in a file which lives in the <LeoDir>/plugins directory
        for this example it is named myPlugin.py
    
    - add code to register the plugin::
       
        leoPlugins.registerHandler("after-create-leo-frame", Hello)
            
    Configuration
    -------------
    
    baseLeoPlugins has 3 *methods* for setting commands
    
    - setCommand::
        
            def setCommand(self, commandName, handler, 
                    shortcut = None, pane = 'all', verbose = True):
    
    - setMenuItem::
        
            def setMenuItem(self, menu, commandName = None, handler = None):
    
    - setButton::
        
            def setButton(self, buttonText = None, commandName = None, color = None):
                
    *variables*
    
    :commandName:  the string typed into minibuffer to execute the ``handler``
     
    :handler:  the method in the class which actually does the work
     
    :shortcut:  the key combination to activate the command
     
    :menu:  a string designating on of the menus ('File', Edit', 'Outline', ...)
     
    :buttonText:  the text to put on the button if one is being created.
    
    Example
    =======
    
    Contents of file ``<LeoDir>/plugins/hello.py``::
    
        class Hello(baseLeoPlugin):
            def __init__(self, tag, keywords):
                
                # call parent __init__
                baseLeoPlugin.__init__(self, tag, keywords)
                
                # if the plugin object defines only one command, 
                # just give it a name. You can then create a button and menu entry
                self.setCommand('Hello', self.hello)
                self.setButton()
                self.setMenuItem('Cmds')
                
                # create a command with a shortcut
                self.setCommand('Hola', self.hola, 'Alt-Ctrl-H')
                
                # create a button using different text than commandName
                self.setButton('Hello in Spanish')
                
                # create a menu item with default text
                self.setMenuItem('Cmds')
                
                # define a command using setMenuItem 
                self.setMenuItem('Cmds', 'Ciao baby', self.ciao)
                                
            def hello(self, event):
                self.g.es( "hello from node %s" % self.c.currentPosition().headString())
        
            def hola(self, event):
                self.g.es( "hola from node %s" % self.c.currentPosition().headString())
                
            def ciao(self, event):
                self.g.es( "ciao baby (%s)" % self.c.currentPosition().headString())
                    
           
        leoPlugins.registerHandler("after-create-leo-frame", Hello)
        
    """
    #@-node:ktenney.20060628092017.2:<<docstring>>
    #@nl
    #@    <<baseLeoPlugin declarations>>
    #@+node:ktenney.20060628092017.3:<<baseLeoPlugin declarations>>
    import leoGlobals as g
    #@-node:ktenney.20060628092017.3:<<baseLeoPlugin declarations>>
    #@nl
    #@    @+others
    #@+node:ktenney.20060628092017.4:__init__
    def __init__(self, tag, keywords):
        
        """Set self.c to be the ``commander`` of the active node
        """
                    
        self.c = keywords['c']
        self.commandNames = []
    #@-node:ktenney.20060628092017.4:__init__
    #@+node:ktenney.20060628092017.5:setCommand
    def setCommand(self, commandName, handler, 
                    shortcut = None, pane = 'all', verbose = True):
        
        """Associate a command name with handler code, 
        optionally defining a keystroke shortcut
        """
        
        self.commandNames.append(commandName)
        
        self.commandName = commandName
        self.shortcut = shortcut
        self.handler = handler
        self.c.k.registerCommand (commandName, shortcut, handler, 
                                pane, verbose)
    #@-node:ktenney.20060628092017.5:setCommand
    #@+node:ktenney.20060628092017.6:setMenuItem
    def setMenuItem(self, menu, commandName = None, handler = None):
        
        """Create a menu item in 'menu' using text 'commandName' calling handler 'handler'
        if commandName and handler are none, use the most recently defined values
        """
        
        # setMenuItem can create a command, or use a previously defined one.
        if commandName is None:
            commandName = self.commandName
        # make sure commandName is in the list of commandNames                        
        else:
            if commandName not in self.commandNames:
                self.commandNames.append(commandName) 
                       
        if handler is None:
            handler = self.handler
            
        table = ((commandName, None, handler),)
        self.c.frame.menu.createMenuItemsFromTable(menu, table)
    #@-node:ktenney.20060628092017.6:setMenuItem
    #@+node:ktenney.20060628092017.7:setButton
    def setButton(self, buttonText = None, commandName = None, color = None):
        
        """Associate an existing command with a 'button'
        """
        
        if buttonText is None:
            buttonText = self.commandName
            
        if commandName is None:
            commandName = self.commandName       
        else:
            if commandName not in self.commandNames:
                raise NameError, "setButton error, %s is not a commandName" % commandName
            
        if color is None:
            color = 'grey'
        script = "c.k.simulateCommand('%s')" % self.commandName
        self.g.makeScriptButton(self.c, script=script, 
                                buttonText = buttonText, bg = color)
    #@-node:ktenney.20060628092017.7:setButton
    #@-others
#@-node:ktenney.20060628092017.1:baseLeoPlugin
#@-others
#@-node:ekr.20031218072017.3439:@thin leoPlugins.py
#@-leo
