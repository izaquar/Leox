#@+leo-ver=4-thin
#@+node:ktenney.20041211072654.1:@thin at_view.py
#@<< docstring >>
#@+node:ekr.20041231104454:<< docstring >>
'''A plugin that supports ``@clip``, ``@view`` and ``@strip`` nodes.

- Selecting a headline containing ``@clip`` appends the contents of the clipboard to
  the end of the body pane.

- Double clicking the icon box of a node whose headline contains ``@view <path-to-file>``
  places the contents of the file in the body pane.

- Double clicking the icon box of a node whose headline contains ``@strip <path-to-file>``
  places the contents of the file in the body pane, with all sentinels removed.

This plugin also accumulates the effect of all ``@path`` nodes.
'''
#@nonl
#@-node:ekr.20041231104454:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4
#@@pagewidth 80

__version__ = "0.7"
#@<< version history >>
#@+node:ktenney.20041211072654.3:<< version history >>
#@+at
# 
# 0.1 KT 2004/12/07 begin converting @button to plugin
# 
# 0.2 EKR style changes:
#     - Uses g.trace to simplify all traces.
#     - Removed comments originating from style guide.
#     - Defined __version__ only in root node.
# 0.3 EKR:
#     - Used g.importExtension to import path and win32clipboard.
#     - Added extensive comments to module's doc string.
#     - Added comments to class View node.
#     - Commented out several traces.
#     - Handle @verbatim sentinels in strip()
#     - Fix bug in strip: set path = currentPath.abspath()
# 0.4 EKR:
#     - Handle case where self.c has been destroyed in idle handler.
# 0.5 EKR:
#     - Corrected and expanded doc string.
# 0.6 EKR:
#     - Added better error message if can't load extensions.
# 0.7 EKR:
#     - Simplified code, fixed bugs and improved error messages.
#@-at
#@nonl
#@-node:ktenney.20041211072654.3:<< version history >>
#@nl
#@<< imports >>
#@+node:ktenney.20041211072654.4:<< imports >>
import leoGlobals as g
import leoPlugins

path           = g.importExtension('path',          pluginName=__name__,verbose=True)
win32clipboard = g.importExtension('win32clipboard',pluginName=__name__,verbose=True)
#@nonl
#@-node:ktenney.20041211072654.4:<< imports >>
#@nl

#@+others
#@+node:ktenney.20041211072654.6:onCreate
def onCreate(tag, keywords):

    c = keywords.get("c")
    if not c: return
    myView = View(c)

    # Register the handlers...
    leoPlugins.registerHandler("icondclick2", myView.icondclick2)
    leoPlugins.registerHandler("idle", myView.idle)
    g.plugin_signon(__name__)
#@nonl
#@-node:ktenney.20041211072654.6:onCreate
#@+node:ktenney.20041211072654.7:class View
class View:
    
    '''A class to support @view, @strip and @clip nodes.'''

    #@    @+others
    #@+node:ktenney.20041211072654.8:__init__
    def __init__ (self,c):
        
        self.c = c
        # g.trace('View')
    #@nonl
    #@-node:ktenney.20041211072654.8:__init__
    #@+node:ktenney.20041211072654.9:icondclick2
    def icondclick2 (self, tag, keywords):
        
        self.current = self.c.currentPosition()
        hs = self.current.headString()
    
        g.trace(hs)
        
        if hs.startswith('@view'):
            self.view()
            
        if hs.startswith('@strip'):
            self.strip()
    #@nonl
    #@-node:ktenney.20041211072654.9:icondclick2
    #@+node:ktenney.20041211203715:idle
    def idle(self, tag, keywords):
        
        try:
            self.current = self.c.currentPosition()
        except AttributeError:
            # c has been destroyed.
            return
    
        s = self.current.headString()
        if s.startswith("@clip"):
            self.clip()
    #@nonl
    #@-node:ktenney.20041211203715:idle
    #@+node:ktenney.20041211072654.10:view
    def view(self):
        
        '''Place the contents of a file in the body pane
        
        the file is either in the current headstring, 
        or found by ascending the tree
        '''
    
        # get a path object for this position
        currentPath = self.getCurrentPath()
    
        # g.trace(currentPath.exists(),currentPath)
    
        if currentPath.exists():
            g.es('currentPath: %s' % currentPath.abspath())
            if currentPath.isfile():
                self.processFile(currentPath, self.current)
    
            if currentPath.isdir():
                self.processDirectory(currentPath, self.current)
        else:
            g.es('path does not exist: %s' % (str(currentPath)),color='blue')
    #@nonl
    #@-node:ktenney.20041211072654.10:view
    #@+node:ktenney.20041212102137:clip
    def clip(self):
        
        '''Watch the clipboard, and copy new items to the body.'''
        
        if not win32clipboard:
            return
    
        c = self.c
        divider = '\n' + ('_-' * 34) + '\n'
        win32clipboard.OpenClipboard()
        clipboard = ""
        if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT):
            clipboard = win32clipboard.GetClipboardData()
        else:
            banner = '*' * 8
            clipboard = banner + 'Image data was copied to the clipboard' + banner
    
        win32clipboard.CloseClipboard()
        
        body = self.current.bodyString().split(divider)
        if not body[0] == clipboard:
            g.es('clipboard now holds %s' % clipboard)
            body.insert(0, clipboard)
            c.setBodyText(self.current,divider.join(body))
    #@nonl
    #@-node:ktenney.20041212102137:clip
    #@+node:ktenney.20041211072654.15:strip
    def strip(self):
        
        '''Display a file with all sentinel lines removed'''
        
        # get a path object for this position
        c = self.c
        currentPath = self.getCurrentPath()
        
        # g.trace(currentPath.exists(),currentPath)
        
        if currentPath.exists():
            path = currentPath.abspath()
            s = 'currentPath: %s' % path
            print s ; g.es(s)
            filelines = path.lines()
            # Add an @ignore directive.
            lines = ['@ignore\n']
            verbatim = False
            for line in filelines:
                if verbatim:
                    lines.append(line)
                    verbatim = False
                elif line.strip().startswith('#@verbatim'):
                    verbatim = True
                elif not line.strip().startswith('#@'):
                    lines.append(line)
            c.setBodyText(self.current,''.join(lines))
        else:
            g.es('path does not exist: %s' % (str(currentPath)),color='blue')
    #@nonl
    #@-node:ktenney.20041211072654.15:strip
    #@+node:ktenney.20041211072654.11:getCurrentPath
    def getCurrentPath(self):
    
        """ traverse the current tree and build a path
            using all @path statements found
        """
        pathFragments = []
        
        # we are currently in a @view node; get the file or directory name
        pathFragments.append(self.getPathFragment(self.current))
        
        for p in self.current.parents_iter():
            pathFragments.append(self.getPathFragment(p))
                
        if pathFragments:
            currentPath = path.path(pathFragments.pop())
            while pathFragments:
                # pop takes the last appended, which is at the top of the tree
                # build a path from the fragments
                currentPath = currentPath / path.path(pathFragments.pop())
                
        return currentPath.normpath()
    #@nonl
    #@-node:ktenney.20041211072654.11:getCurrentPath
    #@+node:ktenney.20041211072654.12:getPathFragment
    def getPathFragment (self,p):
    
        """
        Return the path fragment if this node is a @path or @view or any @file node.
        """
    
        head = p.headString()
    
        for s in ('@path','@view','@strip','@file','@thin','@nosent','@asis'):
            if head.startswith(s):
                fragment = head [head.find(' '):].strip()
                # g.trace(repr(fragment))
                return fragment
    
        return ''
    #@nonl
    #@-node:ktenney.20041211072654.12:getPathFragment
    #@+node:ktenney.20041211072654.13:processFile
    def processFile(self, path, node):
        
        """parameters are a path object and a node.
           the path is a file, place it's contents into the node
        """
        
        g.trace(node)
    
        self.c.setBodyText(node,''.join(path.lines()))
    #@nonl
    #@-node:ktenney.20041211072654.13:processFile
    #@+node:ktenney.20041211072654.14:processDirectory
    def processDirectory(self, path, node):
        
        """
        create child nodes for each member of the directory
        
        @path is a path object for a directory
        @node is the node to work with
        """
    
        # delete all nodes before creating, to avoid duplicates
        while node.firstChild():
            node.firstChild().doDelete(node)
        
        for file in path.files():
            child = node.insertAsLastChild()
            c.setHeadString(child,'@view %s' % file.name)
    
        for file in path.dirs():
           child = node.insertAsLastChild()
           c.setHeadString(child,'@view %s' % file.name)
        
    #@nonl
    #@-node:ktenney.20041211072654.14:processDirectory
    #@-others
#@nonl
#@-node:ktenney.20041211072654.7:class View
#@-others

if path and win32clipboard: # Ok for unit testing.
    leoPlugins.registerHandler("after-create-leo-frame",onCreate)
elif not g.app.unitTesting:
    s = 'at_view plugin not loaded: win32Clipboard not present.'
    g.es_print(s)
#@nonl
#@-node:ktenney.20041211072654.1:@thin at_view.py
#@-leo
