#@+leo-ver=4-thin
#@+node:AGP.20250415230112.718:@thin leoConfig.py
#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import leoGui

import sys
import leo
import leoNodes


#@+others
#@+node:AGP.20250415230112.720:class settingsTreeParser
class settingsTreeParser:
    
    '''A class that inits settings found in an @settings tree. Used by read settings logic.'''

    
    # These are the canonicalized names.  Case is ignored, as are '_' and '-' characters.

    basic_types = [
        # Headlines have the form @kind name = var
        'bool','color','directory','int','ints',
        'float','path','ratio','shortcut','string','strings']

    control_types = [
        'abbrev','font','if','ifgui','ifplatform','ignore','mode','page',
        'settings','shortcuts','config']

    
    
    #@    @+others
    #@+node:AGP.20250415230112.722:__init__()
    def __init__(self,vroot):
        
        self.vroot = vroot
        self.recentFiles = [] # List of recent files.
        #self.shortcutsDict = {}
                # Keys are cononicalized shortcut names, values are bunches.
        
        #self.shortcuts = {}
        #self.settings = {}
        
        # Keys are settings names, values are (type,value) tuples.
        self.settingsDict = {}
        
        # Keys are canonicalized names.
        self.dispatchDict = {
            'config':       self.doConfig, # New agp 
            'abbrev':       self.doAbbrev, # New in 4.4.1 b2.
            'bool':         self.doBool,
            'color':        self.doColor,
            'directory':    self.doDirectory,
            'font':         self.doFont,
            'if':           self.doIf,
            # 'ifgui':        self.doIfGui,  # Removed in 4.4 b3.
            'ifplatform':   self.doIfPlatform,
            'ignore':       self.doIgnore,
            'int':          self.doInt,
            'ints':         self.doInts,
            'float':        self.doFloat,
            #'mode':         self.doMode, # New in 4.4b1.
            'path':         self.doPath,
            'page':         self.doPage,
            'ratio':        self.doRatio,
            # 'shortcut':     self.doShortcut, # Removed in 4.4.1 b1.
            'shortcuts':    self.doShortcuts,
            'string':       self.doString,
            'strings':      self.doStrings,
        }
    #@-node:AGP.20250415230112.722:__init__()
    #@+node:AGP.20250415230112.724:error
    def error (self,s):
    
        print s
    
        # Does not work at present because we are using a null Gui.
        g.es(s,color="blue")
    #@-node:AGP.20250415230112.724:error
    #@+node:AGP.20250415230112.725:kind handlers
    #@+node:AGP.20250415230112.726:doConfig
    def doConfig(self,p,kind,name,val):
        
        #import Tkinter as tk
        #from tkFont import Font
        
        s = p.bodyString()
        lines = g.splitLines(s)
        
        d = {}
        setattr(g,name,d)
        
        gd = {"shade":g.color_shade,
        #        "Font":Font
        }
        #print "GAPPROOT",g.app.root
        
        
        
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith("#"):
                
                        
                elms = line.split("=",1)
                k = elms[0].strip()
                if len(elms) > 1:
                    val = elms[1].strip()
                else:
                    val = elms[0]
                
                try:
                    #print name,k,val
                    if val != None:
                        d[k] = eval(val,gd,d)
                        #print k
                    if line.startswith("*"):
                        if len(line.split("*"))==2:
                            d[k[1:].lower()] = eval(val,gd,d)
                        
                        #print k
                    
                except Exception as e:
                    pass
                    import traceback ; traceback.print_exc()
                    print "Config error in",name,k,e
        
        #print "Config",name,d
        
        self.set('config',name,d)
    #@-node:AGP.20250415230112.726:doConfig
    #@+node:AGP.20250415230112.727:doAbbrev
    def doAbbrev (self,p,kind,name,val):
        
        d = {}
        s = p.bodyString()
        lines = g.splitLines(s)
        for line in lines:
            line = line.strip()
            if line and not g.match(line,0,'#'):
                name,val = self.parseAbbrevLine(line)
                if name: d [val] = name
                
        self.set (p,'abbrev','abbrev',d)
    #@-node:AGP.20250415230112.727:doAbbrev
    #@+node:AGP.20250415230112.728:doBool
    def doBool (self,p,kind,name,val):
    
        if val in ('True','true','1'):
            self.set(kind,name,True)
        elif val in ('False','false','0'):
            self.set(kind,name,False)
        else:
            self.valueError(p,kind,name,val)
    #@-node:AGP.20250415230112.728:doBool
    #@+node:AGP.20250415230112.729:doColor
    def doColor (self,p,kind,name,val):
        
        # At present no checking is done.
        val = val.lstrip('"').rstrip('"')
        val = val.lstrip("'").rstrip("'")
    
        self.set(kind,name,val)
    #@-node:AGP.20250415230112.729:doColor
    #@+node:AGP.20250415230112.730:doDirectory & doPath
    def doDirectory (self,p,kind,name,val):
        
        # At present no checking is done.
        self.set(kind,name,val)
    
    doPath = doDirectory
    #@-node:AGP.20250415230112.730:doDirectory & doPath
    #@+node:AGP.20250415230112.731:doFloat
    def doFloat (self,p,kind,name,val):
        
        try:
            val = float(val)
            self.set(kind,name,val)
        except ValueError:
            self.valueError(kind,name,val)
    #@-node:AGP.20250415230112.731:doFloat
    #@+node:AGP.20250415230112.732:doFont
    def doFont (self,p,kind,name,val):
        
        d = self.parseFont(p)
        
        # Set individual settings.
        for key in ('family','size','slant','weight'):
            data = d.get(key)
            if data is not None:
                name,val = data
                setKind = key
                self.set(setKind,name,val)
    #@-node:AGP.20250415230112.732:doFont
    #@+node:AGP.20250415230112.733:doIf
    def doIf(self,p,kind,name,val):
        
        g.trace("'if' not supported yet")
        return None
    #@-node:AGP.20250415230112.733:doIf
    #@+node:AGP.20250415230112.734:doIfGui
    #@+at 
    #@nonl
    # Alas, @if-gui can't be made to work. The problem is that plugins can set
    # g.app.gui, but plugins need settings so the leoSettings.leo files must 
    # be parsed
    # before g.app.gui.guiName() is known.
    #@-at
    #@@c
    
    if 0:
    
        def doIfGui (self,p,kind,name,val):
            
            # g.trace(repr(name))
            
            if not g.app.gui or not g.app.gui.guiName():
                s = '@if-gui has no effect: g.app.gui not defined yet'
                g.es_print(s,color='blue')
                return "skip"
            elif g.app.gui.guiName().lower() == name.lower():
                return None
            else:
                return "skip"
    #@-node:AGP.20250415230112.734:doIfGui
    #@+node:AGP.20250415230112.735:doIfPlatform
    def doIfPlatform (self,p,kind,name,val):
        
        # g.trace(sys.platform,repr(name))
    
        if sys.platform.lower() == name.lower():
            return None
        else:
            return "skip"
    #@-node:AGP.20250415230112.735:doIfPlatform
    #@+node:AGP.20250415230112.736:doIgnore
    def doIgnore(self,p,kind,name,val):
    
        return "skip"
    #@-node:AGP.20250415230112.736:doIgnore
    #@+node:AGP.20250415230112.737:doInt
    def doInt (self,p,kind,name,val):
        
        try:
            val = int(val)
            self.set(kind,name,val)
        except ValueError:
            self.valueError(p,kind,name,val)
    #@-node:AGP.20250415230112.737:doInt
    #@+node:AGP.20250415230112.738:doInts
    def doInts (self,p,kind,name,val):
        
        '''We expect either:
        @ints [val1,val2,...]aName=val
        @ints aName[val1,val2,...]=val'''
    
        name = name.strip() # The name indicates the valid values.
        i = name.find('[')
        j = name.find(']')
        
        # g.trace(kind,name,val)
    
        if -1 < i < j:
            items = name[i+1:j]
            items = items.split(',')
            name = name[:i]+name[j+1:].strip()
            # g.trace(name,items)
            try:
                items = [int(item.strip()) for item in items]
            except ValueError:
                items = []
                self.valueError(p,'ints[]',name,val)
                return
            kind = "ints[%s]" % (','.join([str(item) for item in items]))
            try:
                val = int(val)
            except ValueError:
                self.valueError(p,'int',name,val)
                return
            if val not in items:
                self.error("%d is not in %s in %s" % (val,kind,name))
                return
    
            # g.trace(repr(kind),repr(name),val)
    
            # At present no checking is done.
            self.set(kind,name,val)
    #@-node:AGP.20250415230112.738:doInts
    #@+node:AGP.20250415230112.741:doPage
    def doPage(self,p,kind,name,val):
    
        pass # Ignore @page this while parsing settings.
    #@-node:AGP.20250415230112.741:doPage
    #@+node:AGP.20250415230112.742:doRatio
    def doRatio (self,p,kind,name,val):
        
        try:
            val = float(val)
            if 0.0 <= val <= 1.0:
                self.set(kind,name,val)
            else:
                self.valueError(p,kind,name,val)
        except ValueError:
            self.valueError(p,kind,name,val)
    #@-node:AGP.20250415230112.742:doRatio
    #@+node:AGP.20250415230112.743:doShortcuts()
    def doShortcuts(self,p,kind,name,val,s=None):
        
        # g.trace(self.c.fileName(),name)
    
        #c = self.c
        d = self.shortcutsDict
        if s is None: s = p.bodyString()
        lines = g.splitLines(s)
        for line in lines:
            line = line.strip()
            if line and not g.match(line,0,'#'):
                #print "doshorcut",name,val,
                name,val = self.parseShortcutLine(line)
                #print name,val
                if val is not None:
                    d [name] = val
                    self.set("shortcut",name,val)
                    self.setShortcut(name,val)
    #@-node:AGP.20250415230112.743:doShortcuts()
    #@+node:AGP.20250415230112.744:doString
    def doString (self,p,kind,name,val):
        
        # At present no checking is done.
        self.set(kind,name,val)
    #@-node:AGP.20250415230112.744:doString
    #@+node:AGP.20250415230112.745:doStrings
    def doStrings (self,p,kind,name,val):
        
        '''We expect one of the following:
        @strings aName[val1,val2...]=val
        @strings [val1,val2,...]aName=val'''
        
        name = name.strip()
        i = name.find('[')
        j = name.find(']')
    
        if -1 < i < j:
            items = name[i+1:j]
            items = items.split(',')
            items = [item.strip() for item in items]
            name = name[:i]+name[j+1:].strip()
            kind = "strings[%s]" % (','.join(items))
            # g.trace(repr(kind),repr(name),val)
    
            # At present no checking is done.
            self.set(kind,name,val)
    #@-node:AGP.20250415230112.745:doStrings
    #@-node:AGP.20250415230112.725:kind handlers
    #@+node:AGP.20250415230112.746:munge
    def munge(self,s):
    
        return g.app.config.canonicalizeSettingName(s)
    #@-node:AGP.20250415230112.746:munge
    #@+node:AGP.20250415230112.747:oops
    def oops (self):
        print ("parserBaseClass oops:",
            g.callers(),
            "must be overridden in subclass")
    #@-node:AGP.20250415230112.747:oops
    #@+node:AGP.20250415230112.748:parsers
    #@+node:AGP.20250415230112.749:fontSettingNameToFontKind
    def fontSettingNameToFontKind (self,name):
        
        s = name.strip()
        if s:
            for tag in ('_family','_size','_slant','_weight'):
                if s.endswith(tag):
                    return tag[1:]
    
        return None
    #@-node:AGP.20250415230112.749:fontSettingNameToFontKind
    #@+node:AGP.20250415230112.750:parseFont
    def parseFont (self,p):
        
        d = {
            'comments': [],
            'family': None,
            'size': None,
            'slant': None,
            'weight': None,
        }
    
        s = p.bodyString()
        lines = g.splitLines(s)
    
        for line in lines:
            self.parseFontLine(line,d)
            
        comments = d.get('comments')
        d['comments'] = '\n'.join(comments)
            
        return d
    #@-node:AGP.20250415230112.750:parseFont
    #@+node:AGP.20250415230112.751:parseFontLine
    def parseFontLine (self,line,d):
        
        s = line.strip()
        if not s: return
        
        try:
            s = str(s)
        except UnicodeError:
            pass
        
        if g.match(s,0,'#'):
            s = s[1:].strip()
            comments = d.get('comments')
            comments.append(s)
            d['comments'] = comments
        else:
            # name is everything up to '='
            i = s.find('=')
            if i == -1:
                name = s ; val = None
            else:
                name = s[:i].strip()
                val = s[i+1:].strip()
                val = val.lstrip('"').rstrip('"')
                val = val.lstrip("'").rstrip("'")
    
            fontKind = self.fontSettingNameToFontKind(name)
            if fontKind:
                d[fontKind] = name,val # Used only by doFont.
    #@-node:AGP.20250415230112.751:parseFontLine
    #@+node:AGP.20250415230112.752:parseHeadline
    def parseHeadline (self,s):
        
        """Parse a headline of the form @kind:name=val
        Return (kind,name,val)."""
    
        kind = name = val = None
    
        if g.match(s,0,'@'):
            i = g.skip_id(s,1,chars='-')
            kind = s[1:i].strip()
            if kind:
                # name is everything up to '='
                j = s.find('=',i)
                if j == -1:
                    name = s[i:].strip()
                else:
                    name = s[i:j].strip()
                    # val is everything after the '='
                    val = s[j+1:].strip()
    
        # g.trace("%50s %10s %s" %(name,kind,val))
        return kind,name,val
    #@-node:AGP.20250415230112.752:parseHeadline
    #@+node:AGP.20250415230112.753:parseShortcutLine (g.app.config)
    def parseShortcutLine (self,s):
        
        '''Parse a shortcut line.  Valid forms:
            
        --> entry-command
        settingName = shortcut
        settingName ! paneName = shortcut
        command-name -> mode-name = binding
        command-name -> same = binding
        '''
        
        name = val = nextMode = None ; nextMode = 'none'
        i = g.skip_ws(s,0)
       
        if g.match(s,i,'-->'): # New in 4.4.1 b1: allow mode-entry commands.
            j = g.skip_ws(s,i+3)
            i = g.skip_id(s,j,'-')
            entryCommandName = s[j:i]
            return None,g.Bunch(entryCommandName=entryCommandName)
        
        j = i
        i = g.skip_id(s,j,'-') # New in 4.4: allow Emacs-style shortcut names.
        name = s[j:i]
        if not name: return None,None
        
        # New in Leo 4.4b2.
        i = g.skip_ws(s,i)
        if g.match(s,i,'->'): # New in 4.4: allow pane-specific shortcuts.
            j = g.skip_ws(s,i+2)
            i = g.skip_id(s,j)
            nextMode = s[j:i]
            
        i = g.skip_ws(s,i)
        if g.match(s,i,'!'): # New in 4.4: allow pane-specific shortcuts.
            j = g.skip_ws(s,i+1)
            i = g.skip_id(s,j)
            pane = s[j:i]
            if not pane.strip(): pane = 'all'
        else: pane = 'all'
    
        i = g.skip_ws(s,i)
        if g.match(s,i,'='):
            i = g.skip_ws(s,i+1)
            val = s[i:]
               
        # New in 4.4: Allow comments after the shortcut.
        # Comments must be preceded by whitespace.
        comment = ''
        if val:
            i = val.find('#')
            if i > 0 and val[i-1] in (' ','\t'):
                # comment = val[i:].strip()
                val = val[:i].strip()
    
        # g.trace(pane,name,val,s)
        return name,val
    #@-node:AGP.20250415230112.753:parseShortcutLine (g.app.config)
    #@+node:AGP.20250415230112.754:parseAbbrevLine (g.app.config)
    def parseAbbrevLine (self,s):
        
        '''Parse an abbreviation line:
        command-name = abbreviation
        return (command-name,abbreviation)
        '''
    
        i = j = g.skip_ws(s,0)
        i = g.skip_id(s,i,'-') # New in 4.4: allow Emacs-style shortcut names.
        name = s[j:i]
        if not name: return None,None
    
        i = g.skip_ws(s,i)
        if not g.match(s,i,'='): return None,None
    
        i = g.skip_ws(s,i+1)
        val = s[i:].strip()
        # Ignore comments after the shortcut.
        i = val.find('#')
        if i > -1: val = val[:i].strip()
    
        if val: return name,val
        else:   return None,None
    #@-node:AGP.20250415230112.754:parseAbbrevLine (g.app.config)
    #@-node:AGP.20250415230112.748:parsers
    #@+node:AGP.20250415230112.755:set()
    def set(self,kind,name,val):
        
        """Init the setting for name to val."""
        
        #print "parser set",kind,name,val
        #print "set()",name,val
        self.settingsDict[name] = val
    #@-node:AGP.20250415230112.755:set()
    #@+node:AGP.20250415230112.756:setShortcut()
    def setShortcut (self,name,val):
        
        #c = self.c
        
        # None is a valid value for val.
        key = name.lower()
        rawKey = key.replace('&','')
        self.set(rawKey,"shortcut",val)
        #print "setShortcut",rawKey,val
        # g.trace(bunch.pane,rawKey,bunch.val)
    #@-node:AGP.20250415230112.756:setShortcut()
    #@+node:AGP.20250415230112.757:traverse()
    def traverse(self):
        
        #c = self.c
        
        p = g.app.config.settingsRoot(self.vroot)
        
        if not p:
            # g.trace('no settings tree for %s' % c)
            return None
    
        self.settingsDict = {}
        self.shortcutsDict = {}
        after = p.nodeAfterTree()
        
        while p and p != after:
            result = self.visitNode(p)
            # g.trace(result,p.headString())
            if result == "skip":
                if 0:
                    s = 'skipping settings in %s' % p.headString()
                    g.es_print(s,color='blue')
                p.moveToNodeAfterTree()
            else:
                p.moveToThreadNext()
                
        return self.settingsDict
    #@-node:AGP.20250415230112.757:traverse()
    #@+node:AGP.20250415230112.758:valueError
    def valueError (self,p,kind,name,val):
        
        """Give an error: val is not valid for kind."""
        
        self.error("%s is not a valid %s for %s" % (val,kind,name))
    #@-node:AGP.20250415230112.758:valueError
    #@+node:AGP.20250415230112.812:visitNode()
    def visitNode (self,p):
        
        """Init any settings found in node p."""
        
        # g.trace(p.headString())
        
        munge = g.app.config.munge
    
        kind,name,val = self.parseHeadline(p.headString())
        kind = munge(kind)
        
        if kind == "settings":
            pass
        elif kind not in self.control_types and val in (u'None',u'none','None','none','',None):
            # None is valid for all data types.
            #print "visit1",p,kind,name,val
            self.set(kind,name,None)
            
        elif kind in self.control_types or kind in self.basic_types:
            f = self.dispatchDict.get(kind)
            try:
                #print "visit2",p,kind,name,val
                return f(p,kind,name,val)
            except TypeError:
                g.es_exception()
                print "*** no handler",kind
        elif name:
            # self.error("unknown type %s for setting %s" % (kind,name))
            # Just assume the type is a string.
            #print "visit3",p,kind,name,val
            self.set(kind,name,val)
        
        return None
    #@-node:AGP.20250415230112.812:visitNode()
    #@-others
#@-node:AGP.20250415230112.720:class settingsTreeParser
#@+node:AGP.20250415230112.760:class configClass
class configClass:
    """A class to manage configuration settings."""
    #@    << class data >>
    #@+node:AGP.20250415230112.761:<<  class data >>
    #@+others
    #@+node:AGP.20250415230112.762:defaultsDict
    #@+at 
    #@nonl
    # This contains only the "interesting" defaults.
    # Ints and bools default to 0, floats to 0.0 and strings to "".
    #@-at
    #@@c
    
    defaultBodyFontSize = g.choose(sys.platform=="win32",9,12)
    defaultLogFontSize  = g.choose(sys.platform=="win32",8,12)
    defaultMenuFontSize = g.choose(sys.platform=="win32",9,12)
    defaultTreeFontSize = g.choose(sys.platform=="win32",9,12)
    
    defaultsDict = {'_hash':'defaultsDict'}
    
    defaultsData = (
        # compare options...
        ("ignore_blank_lines","bool",True),
        ("limit_count","int",9),
        ("print_mismatching_lines","bool",True),
        ("print_trailing_lines","bool",True),
        # find/change options...
        ("search_body","bool",True),
        ("whole_word","bool",True),
        # Prefs panel.
        ("default_target_language","language","python"),
        ("target_language","language","python"), # Bug fix: 6/20,2005.
        ("tab_width","int",-4),
        ("page_width","int",132),
        ("output_doc_chunks","bool",True),
        ("tangle_outputs_header","bool",True),
        # Syntax coloring options...
        # Defaults for colors are handled by leoColor.py.
        ("color_directives_in_plain_text","bool",True),
        ("underline_undefined_section_names","bool",True),
        # Window options...
        ("allow_clone_drags","bool",True),
        ("body_pane_wraps","bool",True),
        ("body_text_font_family","family","Courier"),
        ("body_text_font_size","size",defaultBodyFontSize),
        ("body_text_font_slant","slant","roman"),
        ("body_text_font_weight","weight","normal"),
        ("enable_drag_messages","bool",True),
        ("headline_text_font_family","string",None),
        ("headline_text_font_size","size",defaultLogFontSize),
        ("headline_text_font_slant","slant","roman"),
        ("headline_text_font_weight","weight","normal"),
        ("log_text_font_family","string",None),
        ("log_text_font_size","size",defaultLogFontSize),
        ("log_text_font_slant","slant","roman"),
        ("log_text_font_weight","weight","normal"),
        ("initial_window_height","int",600),
        ("initial_window_width","int",800),
        ("initial_window_left","int",10),
        ("initial_window_top","int",10),
        ("initial_splitter_orientation","string","vertical"),
        ("initial_vertical_ratio","ratio",0.5),
        ("initial_horizontal_ratio","ratio",0.3),
        ("initial_horizontal_secondary_ratio","ratio",0.5),
        ("initial_vertical_secondary_ratio","ratio",0.7),
        ("outline_pane_scrolls_horizontally","bool",False),
        ("split_bar_color","color","LightSteelBlue2"),
        ("split_bar_relief","relief","groove"),
        ("split_bar_width","int",7),
    )
    #@-node:AGP.20250415230112.762:defaultsDict
    #@+node:AGP.20250415230112.763:define encodingIvarsDict
    encodingIvarsDict = {'_hash':'encodingIvarsDict'}
    
    encodingIvarsData = (
        ("default_derived_file_encoding","string","utf-8"),
        ("new_leo_file_encoding","string","UTF-8"),
            # Upper case for compatibility with previous versions.
        ("tkEncoding","string",None),
            # Defaults to None so it doesn't override better defaults.
    )
    #@-node:AGP.20250415230112.763:define encodingIvarsDict
    #@+node:AGP.20250415230112.764:ivarsDict
    # Each of these settings sets the corresponding ivar.
    # Also, the c.configSettings settings class inits the corresponding commander ivar.
    ivarsDict = {'_hash':'ivarsDict'}
    
    ivarsData = (
        ("at_root_bodies_start_in_doc_mode","bool",True),
            # For compatibility with previous versions.
        ("create_nonexistent_directories","bool",False),
        ("output_initial_comment","string",""),
            # "" for compatibility with previous versions.
        ("output_newline","string","nl"),
        ("page_width","int","132"),
        ("read_only","bool",True),
            # Make sure we don't alter an illegal leoConfig.txt file!
        ("redirect_execute_script_output_to_log_pane","bool",False),
        ("relative_path_base_directory","string","!"),
        ("remove_sentinels_extension","string",".txt"),
        ("save_clears_undo_buffer","bool",False),
        ("stylesheet","string",None),
        ("tab_width","int",-4),
        ("target_language","language","python"), # Bug fix: added: 6/20/2005.
        ("trailing_body_newlines","string","asis"),
        ("use_plugins","bool",True),
            # New in 4.3: use_plugins = True by default.
        
        ("undo_granularity","string","word"),
            # "char","word","line","node"
        ("write_strips_blank_lines","bool",False),
    )
    #@-node:AGP.20250415230112.764:ivarsDict
    #@-others
        
    # List of dictionaries to search.  Order not too important.
    dictList = [ivarsDict,encodingIvarsDict,defaultsDict]
    
    # Keys are commanders.  Values are optionsDicts.
    localOptionsDict = {}
    
    localOptionsList = []
        
    # Keys are setting names, values are type names.
    warningsDict = {} # Used by get() or allies.
    #@-node:AGP.20250415230112.761:<<  class data >>
    #@nl
    #@    @+others
    #@+node:AGP.20250415230112.766:__init__()
    def __init__(self):
        
        self.configsExist = False # True when we successfully open a setting file.
        self.defaultFont = None # Set in gui.getDefaultConfigFont.
        self.defaultFontFamily = None # Set in gui.getDefaultConfigFont.
        self.globalConfigFile = None # Set in initSettingsFiles
        self.homeFile = None # Set in initSettingsFiles
        self.inited = False
        self.modeCommandsDict = {} # For use by @mode logic. Keys are command names, values are g.Bunches.
        self.myGlobalConfigFile = None
        self.myHomeConfigFile = None
        self.recentFilesFiles = [] # List of g.Bunches describing .leoRecentFiles.txt files.
        self.write_recent_files_as_needed = False # Will be set later.
        
        # Inited later...
        self.panes = None
        self.sc = None
        self.tree = None
    
        self.initDicts()
        self.initIvarsFromSettings()
        self.initSettingsFiles()
        self.initRecentFiles()
        
        self.settings = {}
    #@-node:AGP.20250415230112.766:__init__()
    #@+node:AGP.20250415230112.767:initDicts
    def initDicts (self):
        
        # Only the settings parser needs to search all dicts.
        self.dictList = [self.defaultsDict]
    
        for key,kind,val in self.defaultsData:
            self.defaultsDict[key] = val
            
        for key,kind,val in self.ivarsData:
            self.ivarsDict[key] = val
    
        for key,kind,val in self.encodingIvarsData:
            self.encodingIvarsDict[key] = val
    #@-node:AGP.20250415230112.767:initDicts
    #@+node:AGP.20250415230112.768:initIvarsFromSettings()
    def initIvarsFromSettings (self):
        
        for ivar in self.encodingIvarsDict.keys():
            if ivar != '_hash':
                setattr(self,ivar,self.encodingIvarsDict.get(ivar))
            
        for ivar in self.ivarsDict.keys():
            if ivar != '_hash':
                setattr(self,ivar,self.ivarsDict.get(ivar))
    #@-node:AGP.20250415230112.768:initIvarsFromSettings()
    #@+node:AGP.20250415230112.771:initRecentFiles
    def initRecentFiles (self):
    
        self.recentFiles = []
    #@-node:AGP.20250415230112.771:initRecentFiles
    #@+node:AGP.20250415230112.772:initSettingsFiles
    def initSettingsFiles (self):
        
        """Set self.globalConfigFile, self.homeFile and self.myConfigFile."""
        
        settingsFile = 'leoSettings.leo'
        mySettingsFile = 'myLeoSettings.leo'
        
        for ivar,theDir,fileName in (
            ('globalConfigFile',    leo.configDir,  settingsFile),
            ('homeFile',            leo.homeDir,          settingsFile),
            ('myGlobalConfigFile',  leo.configDir,  mySettingsFile),
            ('myHomeConfigFile',    leo.homeDir,          mySettingsFile),
        ):
            # The same file may be assigned to multiple ivars:
            # readSettingsFiles checks for such duplications.
            path = g.os_path_join(theDir,fileName)
            if g.os_path_exists(path):
                setattr(self,ivar,path)
            else:
                setattr(self,ivar,None)
    #@-node:AGP.20250415230112.772:initSettingsFiles
    #@+node:AGP.20250415230112.773:Getters... (g.app.config)
    #@+node:AGP.20250415230112.774:canonicalizeSettingName (munge)
    def canonicalizeSettingName (self,name):
        
        if name is None:
            return None
    
        name = name.lower()
        for ch in ('-','_',' ','\n'):
            name = name.replace(ch,'')
            
        return g.choose(name,name,None)
        
    munge = canonicalizeSettingName
    #@-node:AGP.20250415230112.774:canonicalizeSettingName (munge)
    #@+node:AGP.20250415230112.775:config.findSettingsPosition
    def findSettingsPosition (self,vroot,setting):
        
        """Return the position for the setting in the @settings tree for c."""
        
        munge = self.munge
        
        root = self.settingsRoot(vroot)
        if not root:
            return leoNodes.nullPosition()
            
        setting = munge(setting)
            
        for p in root.subtree_iter():
            h = munge(p.headString())
            if h == setting:
                return p.copy()
        
        return leoNodes.nullPosition()
    #@-node:AGP.20250415230112.775:config.findSettingsPosition
    #@+node:AGP.20250415230112.776:get()
    def get (self,setting,kind):
        
        """Get the setting"""
        #print "getcfg",setting,kind
        return self.settings.get(setting,None)
    #@-node:AGP.20250415230112.776:get()
    #@+node:AGP.20250415230112.779:exists()
    def exists (self,setting,kind):
        
        '''Return true if a setting of the given kind exists, even if it is None.'''
    
        if setting in self.settings.keys():
            return True
    
        return False
    #@-node:AGP.20250415230112.779:exists()
    #@+node:AGP.20250415230112.780:getAbbrevDict
    def getAbbrevDict(self):
        
        """Search all dictionaries for the setting & check it's type"""
        
        d = self.get('abbrev','abbrev')
        return d or {}
    #@-node:AGP.20250415230112.780:getAbbrevDict
    #@+node:AGP.20250415230112.781:getBool
    def getBool(self,setting,default=None):
        
        """Search all dictionaries for the setting & check it's type"""
        
        val = self.get(setting,"bool")
        
        if val in (True,False):
            return val
        else:
            return default
    #@-node:AGP.20250415230112.781:getBool
    #@+node:AGP.20250415230112.782:getColor
    def getColor(self,setting):
        
        """Search all dictionaries for the setting & check it's type"""
        
        return self.get(setting,"color")
    #@-node:AGP.20250415230112.782:getColor
    #@+node:AGP.20250415230112.783:getDirectory
    def getDirectory (self,setting):
        
        """Search all dictionaries for the setting & check it's type"""
        
        theDir = self.getString(setting)
    
        if g.os_path_exists(theDir) and g.os_path_isdir(theDir):
             return theDir
        else:
            return None
    #@-node:AGP.20250415230112.783:getDirectory
    #@+node:AGP.20250415230112.784:getFloat
    def getFloat (self,setting):
        
        """Search all dictionaries for the setting & check it's type"""
        
        val = self.get(setting,"float")
        try:
            val = float(val)
            return val
        except TypeError:
            return None
    #@-node:AGP.20250415230112.784:getFloat
    #@+node:AGP.20250415230112.785:getFontFromParams (config)
    def getFontFromParams(self,c,family,size,slant,weight,defaultSize=12):
    
        """Compute a font from font parameters.
    
        Arguments are the names of settings to be use.
        We default to size=12, slant="roman", weight="normal".
    
        We return None if there is no family setting so we can use system default fonts."""
    
        family = self.get(c,family,"family")
        if family in (None,""):
            family = self.defaultFontFamily
    
        size = self.get(c,size,"size")
        if size in (None,0): size = defaultSize
        
        slant = self.get(c,slant,"slant")
        if slant in (None,""): slant = "roman"
    
        weight = self.get(c,weight,"weight")
        if weight in (None,""): weight = "normal"
        
        # g.trace(g.callers(3),family,size,slant,weight,g.shortFileName(c.mFileName))
        
        return g.app.gui.getFontFromParams(family,size,slant,weight)
    #@-node:AGP.20250415230112.785:getFontFromParams (config)
    #@+node:AGP.20250415230112.786:getInt
    def getInt (self,setting):
        
        """Search all dictionaries for the setting & check it's type"""
        
        val = self.get(setting,"int")
        try:
            val = int(val)
            return val
        except TypeError:
            return None
    #@-node:AGP.20250415230112.786:getInt
    #@+node:AGP.20250415230112.787:getLanguage
    def getLanguage (self,setting):
        
        """Return the setting whose value should be a language known to Leo."""
        
        language = self.getString(setting)
        # g.trace(setting,language)
        
        return language
    #@-node:AGP.20250415230112.787:getLanguage
    #@+node:AGP.20250415230112.788:getRatio
    def getRatio (self,setting):
        
        """Search all dictionaries for the setting & check it's type"""
        
        val = self.get(setting,"ratio")
        try:
            val = float(val)
            if 0.0 <= val <= 1.0:
                return val
            else:
                return None
        except TypeError:
            return None
    #@-node:AGP.20250415230112.788:getRatio
    #@+node:AGP.20250415230112.789:getRecentFiles
    def getRecentFiles (self):
    
        return self.recentFiles
    #@-node:AGP.20250415230112.789:getRecentFiles
    #@+node:AGP.20250415230112.790:getShortcut()
    def getShortcut (self,shortcutName):
        
        '''Return rawKey,accel for shortcutName'''
        
        key = shortcutName.lower()
        key = key.replace('&','') # Allow '&' in names.
        sc = self.get(key,"shortcut")
        #print "getShortcut",shortcutName,key,sc
        return key,sc
    
    #@-node:AGP.20250415230112.790:getShortcut()
    #@+node:AGP.20250415230112.791:getString
    def getString(self,setting):
        
        """Search all dictionaries for the setting & check it's type"""
    
        return self.get(setting,"string")
    #@-node:AGP.20250415230112.791:getString
    #@+node:AGP.20250415230112.792:setCommandsIvars
    # Sets ivars of c that can be overridden by leoConfig.txt
    
    def setCommandsIvars (self,c):
    
        data = (
            ("default_tangle_directory","tangle_directory","directory"),
            ("default_target_language","target_language","language"),
            ("output_doc_chunks","output_doc_flag","bool"),
            ("page_width","page_width","int"),
            ("run_tangle_done.py","tangle_batch_flag","bool"),
            ("run_untangle_done.py","untangle_batch_flag","bool"),
            ("tab_width","tab_width","int"),
            ("tangle_outputs_header","use_header_flag","bool"),
        )
        
        for setting,ivar,theType in data:
            val = g.app.config.get(setting,theType)
            
            print "setcivars",setting,val
            if val is None:
                if not hasattr(c,setting):
                    setattr(c,setting,None)
                    # g.trace(setting,None)
            else:
                
                setattr(c,setting,val)
                # g.trace(setting,val)
    #@-node:AGP.20250415230112.792:setCommandsIvars
    #@+node:AGP.20250415230112.793:settingsRoot
    def settingsRoot (self,v):
        for p in leoNodes.position(v).all_iter():
            if p.headString().rstrip() == "@settings":
                return p.copy()
        else:
            return leoNodes.nullPosition()
    #@-node:AGP.20250415230112.793:settingsRoot
    #@-node:AGP.20250415230112.773:Getters... (g.app.config)
    #@+node:AGP.20250415230112.794:Setters (g.app.config)
    #@+node:AGP.20250415230112.795:set()
    def set (self,setting,kind,val):
        
        '''Set the setting.  Not called during initialization.'''
        self.settings[setting] = val
    
    #@-node:AGP.20250415230112.795:set()
    #@+node:AGP.20250415230112.796:setString
    def setString (self,c,setting,val):
        
        self.set(setting,"string",val)
    #@-node:AGP.20250415230112.796:setString
    #@+node:AGP.20250415230112.797:setIvarsFromSettings (g.app.config)
    def setIvarsFromSettings (self,c):
    
        '''Init g.app.config ivars or c's ivars from settings.
        
        - Called from readSettingsFiles with c = None to init g.app.config ivars.
        - Called from c.__init__ to init corresponding commmander ivars.'''
        
        # Ingore temporary commanders created by readSettingsFiles.
        if not self.inited: return
    
        # g.trace(c)
        d = self.ivarsDict
        for key in d:
            if key != '_hash':
                val = self.get(key,"")
                #print key,ivar,val
                    
                if c:
                    #print "setcivars",key,val
                    setattr(c,key,val)
                else:
                    #print "setselfivars",key,val
                    setattr(self,key,val)
    #@-node:AGP.20250415230112.797:setIvarsFromSettings (g.app.config)
    #@+node:AGP.20250415230112.798:appendToRecentFiles (g.app.config)
    def appendToRecentFiles (self,files):
        
        files = [theFile.strip() for theFile in files]
        
        # g.trace(files)
        
        def munge(name):
            name = name or ''
            return g.os_path_normpath(name).lower()
        
        for name in files:
            # Remove all variants of name.
            for name2 in self.recentFiles:
                if munge(name) == munge(name2):
                    self.recentFiles.remove(name2)
    
            self.recentFiles.append(name)
    #@-node:AGP.20250415230112.798:appendToRecentFiles (g.app.config)
    #@+node:AGP.20260221193141:setRecentFiles (c.configSettings)
    def setRecentFiles (self,files):
        
        '''Update the recent files list.'''
    
        # Append the files to the global list.
        self.appendToRecentFiles(files)
    #@-node:AGP.20260221193141:setRecentFiles (c.configSettings)
    #@-node:AGP.20250415230112.794:Setters (g.app.config)
    #@+node:AGP.20250415230112.799:Scanning @settings (g.app.config)
    #@+node:AGP.20250415230112.801:readSettingsFiles()
    def readSettingsFiles (self,fileName,verbose=True):
            
        self.write_recent_files_as_needed = False # Will be set later.
    
        if verbose:
            leo.log('reading settings in %s' % fileName)
        #c = self.openSettingsFile(path)
        leofile = leo.LEOFILE()
        vroot = leofile.load(fileName)
        if vroot:
            d = self.readSettings(vroot)
            if d:
                self.settings.update(d)
        
        
        # Read all .leoRecentFiles.txt files.
        # The order of files in this list affects the order of the recent files list.
        
        #localConfigPath = g.os_path_dirname(localConfigFile)
        #for path in (
            #g.app.homeDir,
            #g.app.globalConfigDir,
            #localConfigPath,
        #):
        #    if path:
        #        ok = self.readRecentFilesFile(path)
                
        #if self.write_recent_files_as_needed:
        #    self.createRecentFiles()
    
        self.inited = True
        self.setIvarsFromSettings(None)
    #@-node:AGP.20250415230112.801:readSettingsFiles()
    #@+node:AGP.20250415230112.803:readSettings()
    # Called to read all leoSettings.leo files.
    # Also called when opening an .leo file to read @settings tree.
    
    def readSettings (self,vroot):
        
        """Read settings from a file that may contain an @settings tree."""
    
        parser = settingsTreeParser(vroot)
        d = parser.traverse()
        
        
    
        return d
    #@-node:AGP.20250415230112.803:readSettings()
    #@+node:AGP.20250415230112.804:updateSettings()
    def updateSettings (self,vroot,localFlag):
    
        d = self.readSettings(vroot)
        
        if d:
            self.settings.update(d)
    
    #@-node:AGP.20250415230112.804:updateSettings()
    #@-node:AGP.20250415230112.799:Scanning @settings (g.app.config)
    #@+node:AGP.20250415230112.805:Reading and writing .leoRecentFiles.txt (g.app.config)
    #@+node:AGP.20250415230112.806:createRecentFiles
    def createRecentFiles (self):
        
        '''Trye to reate .leoRecentFiles.txt in
        - the users home directory first,
        - Leo's config directory second.'''
    
        for theDir in (g.app.homeDir,g.app.globalConfigDir):
            if theDir:
                try:
                    fileName = g.os_path_join(theDir,'.leoRecentFiles.txt')
                    f = file(fileName,'w')
                    f.close()
                    g.es_print('created %s' % (fileName),color='red')
                    return
                except Exception:
                    g.es_print('can not create %s' % (fileName),color='red')
                    g.es_exception()
    #@nonl
    #@-node:AGP.20250415230112.806:createRecentFiles
    #@+node:AGP.20250415230112.807:readRecentFilesFile
    def readRecentFilesFile (self,path):
    
        fileName = g.os_path_join(path,'.leoRecentFiles.txt')
        ok = g.os_path_exists(fileName)
        if ok:
        
            print ('reading %s' % fileName)
            lines = file(fileName).readlines()
            if lines and self.munge(lines[0])=='readonly':
                lines = lines[1:]
            if lines:
                lines = [g.toUnicode(g.os_path_normpath(line),'utf-8') for line in lines]
                self.appendToRecentFiles(lines)
                
        return ok
    #@nonl
    #@-node:AGP.20250415230112.807:readRecentFilesFile
    #@+node:AGP.20250415230112.808:writeRecentFilesFile()
    def writeRecentFilesFile (self,c):
        
        '''Write the appropriate .leoRecentFiles.txt file.'''
        
        tag = '.leoRecentFiles.txt'
        
        if g.app.unitTesting:
            return
        
        localFileName = c.fileName()
        if localFileName:
            localPath,junk = g.os_path_split(localFileName)
        else:
            localPath = None
            
        for path in (localPath,g.app.globalConfigDir,g.app.homeDir):
            if path:
                fileName = g.os_path_join(path,tag)
                if g.os_path_exists(fileName):
                    print ('wrote %s' % fileName)
                    self.writeRecentFilesFileHelper(fileName)
                    return
        else:
            # g.trace('----- not found: %s' % g.os_path_join(localPath,tag))
            return
    #@-node:AGP.20250415230112.808:writeRecentFilesFile()
    #@+node:AGP.20250415230112.809:writeRecentFilesFileHelper()
    def writeRecentFilesFileHelper (self,fileName):
        # g.trace(fileName)
        
        # Don't update the file if it begins with read-only.
        theFile = None
        try:
            theFile = file(fileName)
            lines = theFile.readlines()
            if lines and self.munge(lines[0])=='readonly':
                # g.trace('read-only: %s' %fileName)
                return
        except IOError:
            # The user may have erased a file.  Not an error.
            if theFile: theFile.close()
    
        theFile = None
        try:
            # g.trace('writing',fileName)
            theFile = file(fileName,'w')
            if self.recentFiles:
                lines = [g.toEncodedString(line,'utf-8') for line in self.recentFiles]
                theFile.write('\n'.join(lines))
            else:
                theFile.write('\n')
    
        except IOError:
            # The user may have erased a file.  Not an error.
            pass
                
        except Exception:
            g.es('unexpected exception writing %s' % fileName,color='red')
            g.es_exception()
        
        if theFile:
            theFile.close()
    #@-node:AGP.20250415230112.809:writeRecentFilesFileHelper()
    #@-node:AGP.20250415230112.805:Reading and writing .leoRecentFiles.txt (g.app.config)
    #@+node:AGP.20251210181936:canonicalizeMenuName()
    def canonicalizeMenuName (self,name):
        
        return ''.join([ch for ch in name.lower() if ch.isalnum()])
    #@nonl
    #@-node:AGP.20251210181936:canonicalizeMenuName()
    #@-others
#@-node:AGP.20250415230112.760:class configClass
#@-others
#@-node:AGP.20250415230112.718:@thin leoConfig.py
#@-leo
