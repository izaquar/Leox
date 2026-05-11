# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:AGP.20250415230112.1384:@thin leoGlobals.py
#@@first

"""Global constants, variables and utility functions used throughout Leo."""

#@@language python
#@@tabwidth -4
#@@pagewidth 80

from __future__ import generators # To make the code work in Python 2.2.

#@<< imports >>
#@+node:AGP.20250415230112.1385:<< imports >>
import leoGlobals as g # So code can use g below.
import leo
import leoLang

    
try:
    import gc
except ImportError:
    gc = None

import exceptions
import filecmp
import gettext
import operator
import os
if 0: # Do NOT import pdb here!  We shall define pdb as a _function_ below.
    import pdb
import re
import string
import sys
import tempfile
import time
import traceback
import types
import unicodedata

from PIL import Image,ImageTk,ImageColor
#@nonl
#@-node:AGP.20250415230112.1385:<< imports >>
#@nl
#@<< define general constants >>
#@+node:AGP.20250415230112.1386:<< define general constants >>
body_newline = '\n'
body_ignored_newline = '\r'
#@-node:AGP.20250415230112.1386:<< define general constants >>
#@nl
#@<< define global data structures >>
#@+node:AGP.20250415230112.1387:<< define global data structures >>
# Visible externally so plugins may add to the list of directives.

globalDirectiveList = [
    "color", "comment", "encoding", "header", "ignore", "killcolor",
    "language", "lineending", "nocolor", "noheader", "nowrap",
    "pagewidth", "path", "quiet", "root", "silent",
    "tabwidth", "terse", "unit", "verbose", "wrap"
    ,"keywords"]
#@-node:AGP.20250415230112.1387:<< define global data structures >>
#@nl

#app = None # The singleton app object.


#@+others
#@+node:AGP.20250415230112.1391:theme
#agp color
getrgb = ImageColor.getrgb
#@nonl
#@+node:AGP.20250415230112.1392:color_mul()
def color_mul(f,color):
    r,g,b = getrgb(color)
    #print "mulrgb",color,getrgb(color)
    #r,g,b = r*f/65536.0,g*f/65536.0,b*f/65536.0
    r,g,b = r*f,g*f,b*f
    #print "mulrgb",r,g,b
    #return "#%02x%02x%02x" % (r*256,g*256,b*256)
    return "#%02x%02x%02x" % (r,g,b)
#@nonl
#@-node:AGP.20250415230112.1392:color_mul()
#@+node:AGP.20250415230112.1393:color_add()
def color_add(c1,c2):
    r,g,b = getrgb(c1)
    #print "addrgb",c1,getrgb(c1),c2,getrgb(c2)
    r1,g1,b1 = getrgb(c2)
    #r,g,b = (r+r1)/65536.0,(g+g1)/65536.0,(b+b1)/65536.0
    r,g,b = (r+r1),(g+g1),(b+b1)
    return "#%02x%02x%02x" % (r,g,b)
#@nonl
#@-node:AGP.20250415230112.1393:color_add()
#@+node:AGP.20250415230112.1394:colors_tof()
def colors_tof(r,g,b):
    return r/65536.0,g/65536.0,b/65536.0
#@nonl
#@-node:AGP.20250415230112.1394:colors_tof()
#@+node:AGP.20250415230112.1395:colorf_center()
def colorf_center(r,g,b):
    return r-0.5,g-0.5,b-0.5
#@nonl
#@-node:AGP.20250415230112.1395:colorf_center()
#@+node:AGP.20250415230112.1396:colorf_add()
def colorf_add(a,r,g,b):
    return r+a,g+a,b+a
#@nonl
#@-node:AGP.20250415230112.1396:colorf_add()
#@+node:AGP.20250415230112.1397:colorf_mul()
def colorf_mul(f,r,g,b):
    return r*f,g*f,b*f
#@nonl
#@-node:AGP.20250415230112.1397:colorf_mul()
#@+node:AGP.20250415230112.1398:colorf_toh()
def colorf_toh(r,g,b):
    return "#%02x%02x%02x" % (r*256,g*256,b*256)
#@-node:AGP.20250415230112.1398:colorf_toh()
#@+node:AGP.20250415230112.1399:colorf_scale()
def colorf_scale(color,f):
    
    colors = colors_tof(*getrgb(color))
    colors = colorf_add(-0.5,*colors)
    colors = colorf_mul(f,*colors)
    colors = colorf_add(0.5,*colors)
    return colorf_toh(*colors)
#@nonl
#@-node:AGP.20250415230112.1399:colorf_scale()
#@+node:AGP.20250415230112.1400:color_scale()
def color_scale(f,color):
    
    colors = colors_tof(*getrgb(color))
    colors = colorf_add(-0.5,*colors)
    colors = colorf_mul(f,*colors)
    colors = colorf_add(0.5,*colors)
    return colorf_toh(*colors)
#@nonl
#@-node:AGP.20250415230112.1400:color_scale()
#@+node:AGP.20250415230112.1401:color_interp()
def color_interp(u,c1,c2):
    #cadd,cmul = g.color_add,g.color_mul
    
    return color_add( color_mul( 1.0-u,c1), color_mul( u,c2) )
#@nonl
#@-node:AGP.20250415230112.1401:color_interp()
#@+node:AGP.20250415230112.1402:color_shade()
def color_shade(u,fg=None,bg=None):
    cadd,cmul,cscale = g.color_add,g.color_mul,g.colorf_scale
    
    #leo_cfg = g.c.config.get('theme','config')
    theme = g.theme
    
    if not fg:
        fg = theme["foreground"]
    if not bg:
        bg = theme["background"]
    #print c1,c2
    return cadd( cmul( 1.0-u,bg), cmul( u,fg) )
#@nonl
#@-node:AGP.20250415230112.1402:color_shade()
#@+node:AGP.20250415230112.1403:load_ui_cfg()
def load_ui_cfg(): #agp ui
    
    uifile = file(g.app.leoDir+"/config/leo.ui")
    lines = uifile.readlines()
    
    d = {}
    setattr(g,"theme",d)
    
    gd = {"shade":g.color_shade}
    
    #ui_keys = []
    
    for line in lines:
        line = line.strip()
        if line:
            
            if line.startswith("#"):
                #ui_keys.append(line)
                continue
                    
            elms = line.split("=",1)
            k = elms[0].strip()
            if len(elms) > 1:
                val = elms[1].strip()
            else:
                val = elms[0]
            
            try:
                if val != None:
                    d[k] = eval(val,gd,d)
                if line.startswith("*"):
                    if len(line.split("*"))==2:
                        d[k[1:].lower()] = eval(val,gd,d)
            
                
            except Exception as e:
                pass
                import traceback ; traceback.print_exc()
                print "leo.ui error",k,e
    
    g.ui_cfg = d
#@-node:AGP.20250415230112.1403:load_ui_cfg()
#@+node:AGP.20250415230112.1404:gen_theme()
def gen_theme():
    
    contrast=1.0
    root = rw = g.app.root
    
    
    load_ui_cfg()
    
    theme = g.theme = {}
    theme["shade"] = g.color_shade
    
    for prop in ui_cfg.keys():
        #print prop
        if prop.startswith("*"):
            val = theme[prop[1:]] = ui_cfg[prop]
            #print "option add",prop
            root.option_add(prop,val)
        else:
            theme[prop] = ui_cfg[prop]
    
    theme["fg"] = fg = theme["foreground"]
    theme["bg"] = bg = theme["background"]
    
    
    bg = colors_tof(*rw.winfo_rgb(bg))
    fg = colors_tof(*rw.winfo_rgb(fg))
    
    bg = colorf_add(-0.5,*bg)
    fg = colorf_add(-0.5,*fg)
    
    #
    insert_bg = colorf_mul(1.0*contrast,*fg)
    outfg = colorf_mul(0.90*contrast,*fg)
    active_fg = colorf_mul(0.80*contrast,*fg)
    select_bg = colorf_mul(0.70*contrast,*fg)
    
    rb,gb,bb = bg
    rf,gf,bf = fg
    
    mid   = (rb+rf)/2, (gb+gf)/2, (bb+bf)/2
    
    select_fg = colorf_mul(0.70*contrast,*bg)
    active_bg = colorf_mul(0.80*contrast,*bg)
    outbg = colorf_mul(0.90*contrast,*bg)
    
    #
    insert_bg = colorf_add(0.5,*insert_bg)
    outfg = colorf_add(0.5,*outfg)
    active_fg = colorf_add(0.5,*active_fg)
    select_bg = colorf_add(0.5,*select_bg)
    
    mid  = colorf_add(0.5,*mid)
    
    select_fg = colorf_add(0.5,*select_fg)
    active_bg = colorf_add(0.5,*active_bg)
    outbg = colorf_add(0.5,*outbg)
    
    #
    insert_bg = colorf_toh(*insert_bg)
    outfg = colorf_toh(*outfg)
    active_fg = colorf_toh(*active_fg)
    select_bg = colorf_toh(*select_bg)
    
    mid  = colorf_toh(*mid)
    
    select_fg = colorf_toh(*select_fg)
    active_bg = colorf_toh(*active_bg)
    outbg = colorf_toh(*outbg)
    
    num_shade = 10
    incf = 1.0/num_shade
    #for u in range(num_shade);
    #    g.color_interp(u*inf,outbg,outfg)
    
    theme.update({
        #'shade':g.color_shade,
        #'bg': outbg,#self.getColor(None,"def_background_color"),
        #'fg': outfg,#self.getColor(None,"def_foreground_color"),
        #'selectbackground': select_bg,#self.getColor(None,"def_sel_bg_color"),
        #'selectforeground': select_fg,#self.getColor(None,"def_sel_fg_color"),
        #'insertbackground': insert_bg,#self.getColor(None,"def_insert_bg_color"),
        #'mark':'#FF0000FF',
        #'clone':'#FF0000FF',
        #'content':'#00DDFFFF',
        #'dirty':'#808080FF',
    })
    """root.option_add("*background",outbg)#g.color_theme['bg']) #agp
    root.option_add("*foreground",outfg)#g.color_theme['fg'])
    root.option_add("*selectbackground",select_bg)#g.color_theme['selectbackground'])
    root.option_add("*selectforeground",select_fg)#g.color_theme['selectforeground'])
    root.option_add("*insertBackground",insert_bg)#g.color_theme['insertbackground'])
    
    root.option_add("*borderColor",outfg)
    root.option_add("*Button*relief",'groove')
    root.option_add("*Scrollbar*width",0)
    root.option_add("*Menu*borderWidth",1)
    
    root.option_add("Checkbutton*selectcolor",outfg)"""
    
    #render_icons()
#@nonl
#@-node:AGP.20250415230112.1404:gen_theme()
#@-node:AGP.20250415230112.1391:theme
#@+node:AGP.20250415230112.1407:Commands & Directives
#@+node:AGP.20250415230112.1408:Compute directories... (leoGlobals)
#@+node:AGP.20250415230112.1409:computeGlobalConfigDir
def computeGlobalConfigDir():
    
    import leoGlobals as g
    
    encoding = g.startupEncoding()

    try:
        theDir = sys.leo_config_directory
    except AttributeError:
        theDir = g.os_path_join(g.app.loadDir,"..","config")
        
    if theDir:
        theDir = g.os_path_abspath(theDir)
        
    if (
        not theDir or
        not g.os_path_exists(theDir,encoding) or
        not g.os_path_isdir(theDir,encoding)
    ):
        theDir = None
    
    return theDir
#@-node:AGP.20250415230112.1409:computeGlobalConfigDir
#@+node:AGP.20250415230112.1410:computeHomeDir
def computeHomeDir():
    
    """Returns the user's home directory."""
    
    import leoGlobals as g

    encoding = g.startupEncoding()
    # dotDir = g.os_path_abspath('./',encoding)
    home = os.getenv('HOME',default=None)

    if home and len(home) > 1 and home[0]=='%' and home[-1]=='%':
        # Get the indirect reference to the true home.
        home = os.getenv(home[1:-1],default=None)

    if home:
        # N.B. This returns the _working_ directory if home is None!
        # This was the source of the 4.3 .leoID.txt problems.
        home = g.os_path_abspath(home,encoding)
        if (
            not g.os_path_exists(home,encoding) or
            not g.os_path_isdir(home,encoding)
        ):
            home = None

    # g.trace(home)
    return home
#@-node:AGP.20250415230112.1410:computeHomeDir
#@+node:AGP.20250415230112.1411:computeLeoDir
def computeLeoDir ():
    
    loadDir = g.app.loadDir
    
    g.app.leoDir = theDir = g.os_path_dirname(loadDir)
    
    if theDir not in sys.path:
        sys.path.append(theDir)
        
    if 0: # This is required so we can do import leo (as a package)
        theParentDir = g.os_path_dirname(theDir)
        if theParentDir not in sys.path:
            sys.path.append(theParentDir)
#@-node:AGP.20250415230112.1411:computeLeoDir
#@+node:AGP.20250415230112.1412:computeLoadDir
def computeLoadDir():
    
    """Returns the directory containing leo.py."""
    
    import leoGlobals as g

    try:
        ### import leo
        import sys
        
        # Fix a hangnail: on Windows the drive letter returned by
        # __file__ is randomly upper or lower case!
        # The made for an ugly recent files list.
        path = g.__file__ # was leo.__file__
        if sys.platform=='win32':
            if len(path) > 2 and path[1]==':':
                # Convert the drive name to upper case.
                path = path[0].upper() + path[1:]
        encoding = g.startupEncoding()
        path = g.os_path_abspath(path,encoding)
        if path:
            loadDir = g.os_path_dirname(path,encoding)
        else: loadDir = None
            
        if (
            not loadDir or
            not g.os_path_exists(loadDir,encoding) or
            not g.os_path_isdir(loadDir,encoding)
        ):
            loadDir = os.getcwd()
            print "Using emergency loadDir:",repr(loadDir)
        
        loadDir = g.os_path_abspath(loadDir,encoding)
        # g.es("load dir: %s" % (loadDir),color="blue")
        return loadDir
    except:
        print "Exception getting load directory"
        import traceback ; traceback.print_exc()
        return None
#@-node:AGP.20250415230112.1412:computeLoadDir
#@+node:AGP.20250415230112.1413:computeStandardDirectories
def computeStandardDirectories():
    
    '''Set g.app.loadDir, g.app.homeDir and g.app.globalConfigDir.'''
    
    if 0:
        import sys
        for s in sys.path: g.trace(s)
    
    g.app.loadDir = g.computeLoadDir() #g.exe_dir 
        # Depends on g.app.tkEncoding: uses utf-8 for now.
    
    #g.app.leoDir = g.computeLeoDir()
    g.computeLeoDir()
    
    g.app.homeDir = g.computeHomeDir()
    
    g.app.extensionsDir = g.os_path_abspath(
        g.os_path_join(g.app.loadDir,'..','extensions'))
    
    g.app.globalConfigDir = g.computeGlobalConfigDir()
    
    g.app.testDir = g.os_path_abspath(
        g.os_path_join(g.app.loadDir,'..','test'))
        
    g.app.user_xresources_path = g.os_path_join(g.app.homeDir,'.leo_xresources')
#@-node:AGP.20250415230112.1413:computeStandardDirectories
#@+node:AGP.20250415230112.1414:startupEncoding
def startupEncoding ():
    
    import leoGlobals as g
    import sys
    
    if sys.platform=="win32": # "mbcs" exists only on Windows.
        encoding = "mbcs"
    elif sys.platform=="dawwin":
        encoding = "utf-8"
    else:
        encoding = g.app.tkEncoding
        
    return encoding
#@-node:AGP.20250415230112.1414:startupEncoding
#@-node:AGP.20250415230112.1408:Compute directories... (leoGlobals)
#@+node:AGP.20250415230112.1415:Directive utils...
#@+node:AGP.20250415230112.1416:g.comment_delims_from_extension
def comment_delims_from_extension(filename):
    
    """
    Return the comment delims corresponding to the filename's extension.

    >>> g.comment_delims_from_extension(".py")
    ('#', None, None)

    >>> g.comment_delims_from_extension(".c")
    ('//', '/*', '*/')
    
    >>> g.comment_delims_from_extension(".html")
    (None, '<!--', '-->')

    """

    root, ext = os.path.splitext(filename)
    if ext == '.tmp':
        root, ext = os.path.splitext(root)
        
    language = g.app.extension_dict.get(ext[1:])
    if ext:
        
        return g.set_delims_from_language(language)
    else:
        g.trace("unknown extension %s" % ext)
        return None,None,None
#@-node:AGP.20250415230112.1416:g.comment_delims_from_extension
#@+node:AGP.20250415230112.1417:@language and @comment directives (leoUtils)
#@+node:AGP.20250415230112.1418:set_delims_from_language
# Returns a tuple (single,start,end) of comment delims

def set_delims_from_language(language):
    
    # g.trace(g.callers())
    langs = leoLang.languages
    if language in langs.keys():
        langmod = langs[language]
        return langmod.COMMENT_START,langmod.BLOCK_COMMENT_START,langmod.BLOCK_COMMENT_END
    
        """val = app.language_delims_dict.get(language)
    if val:
        delim1,delim2,delim3 = g.set_delims_from_string(val)
        if delim2 and not delim3:
            return None,delim1,delim2
        else: # 0,1 or 3 params.
            return delim1,delim2,delim3"""
    else:
        return None, None, None # Indicate that no change should be made
#@-node:AGP.20250415230112.1418:set_delims_from_language
#@+node:AGP.20250415230112.1419:set_delims_from_string
def set_delims_from_string(s):

    """Returns (delim1, delim2, delim2), the delims following the @comment directive.
    
    This code can be called from @language logic, in which case s can point at @comment"""

    # Skip an optional @comment
    tag = "@comment"
    i = 0
    if g.match_word(s,i,tag):
        i += len(tag)
        
    count = 0 ; delims = [None, None, None]
    while count < 3 and i < len(s):
        i = j = g.skip_ws(s,i)
        while i < len(s) and not g.is_ws(s[i]) and not g.is_nl(s,i):
            i += 1
        if j == i: break
        delims[count] = s[j:i]
        count += 1
        
    # 'rr 09/25/02
    if count == 2: # delims[0] is always the single-line delim.
        delims[2] = delims[1]
        delims[1] = delims[0]
        delims[0] = None

    # 7/8/02: The "REM hack": replace underscores by blanks.
    # 9/25/02: The "perlpod hack": replace double underscores by newlines.
    for i in xrange(0,3):
        if delims[i]:
            delims[i] = string.replace(delims[i],"__",'\n') 
            delims[i] = string.replace(delims[i],'_',' ')

    return delims[0], delims[1], delims[2]
#@-node:AGP.20250415230112.1419:set_delims_from_string
#@+node:AGP.20250415230112.1420:set_language
def set_language(s,i,issue_errors_flag=False):
    
    """Scan the @language directive that appears at s[i:].

    Returns (language, delim1, delim2, delim3)
    """

    tag = "@language"
    # g.trace(g.get_line(s,i))
    assert(i != None)
    assert(g.match_word(s,i,tag))
    i += len(tag) ; i = g.skip_ws(s, i)
    # Get the argument.
    j = i ; i = g.skip_c_id(s,i)
    # Allow tcl/tk.
    arg = string.lower(s[j:i])
    
    """if app.language_delims_dict.get(arg):
        language = arg
        delim1, delim2, delim3 = g.set_delims_from_language(language)
        return language, delim1, delim2, delim3"""
    
    if arg in leoLang.languages.keys():
        language = arg
        delim1, delim2, delim3 = g.set_delims_from_language(language)
        return language, delim1, delim2, delim3
    
    if issue_errors_flag:
        g.es("ignoring: " + g.get_line(s,i))

    return None, None, None, None,
#@-node:AGP.20250415230112.1420:set_language
#@-node:AGP.20250415230112.1417:@language and @comment directives (leoUtils)
#@+node:AGP.20250415230112.1421:g.findReference
#@+at 
#@nonl
# We search the descendents of v looking for the definition node matching 
# name.
# There should be exactly one such node (descendents of other definition nodes 
# are not searched).
#@-at
#@@c

def findReference(c,name,root):

    for p in root.subtree_iter():
        assert(p!=root)
        if p.matchHeadline(name) and not p.isAtIgnoreNode():
            return p

    # g.trace("not found:",name,root)
    return c.nullPosition()
#@-node:AGP.20250415230112.1421:g.findReference
#@+node:AGP.20250415230112.1422:get_directives_dict & globalDirectiveList
# The caller passes [root_node] or None as the second arg.  This allows us to distinguish between None and [None].

def get_directives_dict(s,root=None):
    
    """Scans root for @directives found in globalDirectiveList.

    Returns a dict containing pointers to the start of each directive"""

    if root: root_node = root[0]
    theDict = {}
    i = 0 ; n = len(s)
    while i < n:
        if s[i] == '@' and i+1 < n:
            #@            << set theDict for @ directives >>
            #@+node:AGP.20250415230112.1423:<< set theDict for @ directives >>
            j = g.skip_c_id(s,i+1)
            word = s[i+1:j]
            
            global globalDirectiveList
            
            if word in globalDirectiveList:
                if theDict.has_key(word):
                    # Ignore second value.
                    pass
                    # g.es("Warning: conflicting values for %s" % (word), color="blue")
                else:
                    theDict [word] = i
            #@-node:AGP.20250415230112.1423:<< set theDict for @ directives >>
            #@nl
        elif root and g.match(s,i,"<<"):
            #@            << set theDict["root"] for noweb * chunks >>
            #@+node:AGP.20250415230112.1424:<< set theDict["root"] for noweb * chunks >>
            #@+at 
            #@nonl
            # The following looks for chunk definitions of the form < < * > > 
            # =. If found, we take this to be equivalent to @root filename if 
            # the headline has the form @root filename.
            #@-at
            #@@c
            
            i = g.skip_ws(s,i+2)
            if i < n and s[i] == '*' :
                i = g.skip_ws(s,i+1) # Skip the '*'
                if g.match(s,i,">>="):
                    # < < * > > = implies that @root should appear in the headline.
                    i += 3
                    if root_node:
                        theDict["root"]=0 # value not immportant
                    else:
                        g.es(g.angleBrackets("*") + "= requires @root in the headline")
            #@-node:AGP.20250415230112.1424:<< set theDict["root"] for noweb * chunks >>
            #@nl
        i = g.skip_line(s,i)
    return theDict
#@-node:AGP.20250415230112.1422:get_directives_dict & globalDirectiveList
#@+node:AGP.20250415230112.1425:getOutputNewline
def getOutputNewline (c=None,name=None):
    
    '''Convert the name of a line ending to the line ending itself.
    
    Priority:
    - Use name if name given
    - Use c.config.output_newline if c given,
    - Otherwise use g.app.config.output_newline.'''
    
    # g.trace(c,name,c.config.output_newline)
    if name: s = name
    elif c:  s = c.config.output_newline
    else:    s = app.config.output_newline

    if not s: s = ''
    s = s.lower()
    if s in ( "nl","lf"): s = '\n'
    elif s == "cr": s = '\r'
    elif s == "platform": s = os.linesep  # 12/2/03: emakital
    elif s == "crlf": s = "\r\n"
    else: s = '\n' # Default for erroneous values.
    return s
#@-node:AGP.20250415230112.1425:getOutputNewline
#@+node:AGP.20250415230112.1426:scanAtEncodingDirective
def scanAtEncodingDirective(s,theDict):
    
    """Scan the @encoding directive at s[theDict["encoding"]:].

    Returns the encoding name or None if the encoding name is invalid.
    """

    k = theDict["encoding"]
    i = g.skip_to_end_of_line(s,k)
    j = len("@encoding")
    encoding = s[k+j:i].strip()
    if g.isValidEncoding(encoding):
        # g.trace(encoding)
        return encoding
    else:
        g.es("invalid @encoding:"+encoding,color="red")
        return None
#@-node:AGP.20250415230112.1426:scanAtEncodingDirective
#@+node:AGP.20250415230112.1427:scanAtLineendingDirective
def scanAtLineendingDirective(s,theDict):
    
    """Scan the @lineending directive at s[theDict["lineending"]:].

    Returns the actual lineending or None if the name of the lineending is invalid.
    """

    k = theDict["lineending"]
    i = g.skip_to_end_of_line(s,k)
    j = len("@lineending")
    j = g.skip_ws(s,j)
    e = s[k+j:i].strip()

    if e in ("cr","crlf","lf","nl","platform"):
        lineending = g.getOutputNewline(name=e)
        # g.trace(e,lineending)
        return lineending
    else:
        # g.es("invalid @lineending directive:"+e,color="red")
        return None
#@-node:AGP.20250415230112.1427:scanAtLineendingDirective
#@+node:AGP.20250415230112.1428:scanAtPagewidthDirective
def scanAtPagewidthDirective(s,theDict,issue_error_flag=False):
    
    """Scan the @pagewidth directive at s[theDict["pagewidth"]:].

    Returns the value of the width or None if the width is invalid.
    """
    
    k = theDict["pagewidth"]
    j = i = k + len("@pagewidth")
    i, val = g.skip_long(s,i)
    if val != None and val > 0:
        # g.trace(val)
        return val
    else:
        if issue_error_flag:
            j = g.skip_to_end_of_line(s,k)
            g.es("ignoring " + s[k:j],color="red")
        return None
#@-node:AGP.20250415230112.1428:scanAtPagewidthDirective
#@+node:AGP.20250415230112.1429:scanAtTabwidthDirective
def scanAtTabwidthDirective(s,theDict,issue_error_flag=False):
    
    """Scan the @tabwidth directive at s[theDict["tabwidth"]:].

    Returns the value of the width or None if the width is invalid.
    """
    
    k = theDict["tabwidth"]
    i = k + len("@tabwidth")
    i, val = g.skip_long(s, i)
    if val != None and val != 0:
        # g.trace(val)
        return val
    else:
        if issue_error_flag:
            i = g.skip_to_end_of_line(s,k)
            g.es("Ignoring " + s[k:i],color="red")
        return None
#@-node:AGP.20250415230112.1429:scanAtTabwidthDirective
#@+node:AGP.20250415230112.1430:scanForAtIgnore
def scanForAtIgnore(c,p):
    
    """Scan position p and its ancestors looking for @ignore directives."""

    if g.app.unitTesting:
        return False # For unit tests.

    for p in p.self_and_parents_iter():
        s = p.bodyString()
        d = g.get_directives_dict(s)
        if d.has_key("ignore"):
            return True

    return False
#@-node:AGP.20250415230112.1430:scanForAtIgnore
#@+node:AGP.20250415230112.1431:g.scanForAtSettings
def scanForAtSettings(p):
    
    """Scan position p and its ancestors looking for @settings nodes."""
    
    for p in p.self_and_parents_iter():
        h = p.headString()
        h = g.app.config.canonicalizeSettingName(h)
        if h.startswith("@settings"):
            return True

    return False
#@-node:AGP.20250415230112.1431:g.scanForAtSettings
#@+node:AGP.20250415230112.1432:scanForAtLanguage
def scanForAtLanguage(c,p):
    
    """Scan position p and p's ancestors looking only for @language and @ignore directives.

    Returns the language found, or c.target_language."""
    
    # Unlike the code in x.scanAllDirectives, this code ignores @comment directives.

    if c and p:
        for p in p.self_and_parents_iter():
            s = p.bodyString()
            d = g.get_directives_dict(s)
            if d.has_key("language"):
                k = d["language"]
                language,delim1,delim2,delim3 = g.set_language(s,k)
                return language # Continue looking for @ignore

    return c.target_language
#@-node:AGP.20250415230112.1432:scanForAtLanguage
#@+node:AGP.20250415230112.1433:g.scanDirectives
#@+at 
#@nonl
# Perhaps this routine should be the basis of atFile.scanAllDirectives and 
# tangle.scanAllDirectives, but I am loath to make any further to these two 
# already-infamous routines.  Also, this code does not check for @color and 
# @nocolor directives: leoColor.useSyntaxColoring does that.
#@-at
#@@c

def scanDirectives(c,p=None):
    
    """Scan vnode v and v's ancestors looking for directives.

    Returns a dict containing the results, including defaults."""

    if p is None:
        p = c.currentPosition()

    #@    << Set local vars >>
    #@+node:AGP.20250415230112.1434:<< Set local vars >>
    page_width = c.page_width
    tab_width  = c.tab_width
    language = c.target_language
    if c.target_language:
        c.target_language = c.target_language.lower()
    delim1, delim2, delim3 = g.set_delims_from_language(c.target_language)
    path = None
    encoding = None # 2/25/03: This must be none so that the caller can set a proper default.
    lineending = g.getOutputNewline(c=c) # Init from config settings.
    wrap = c.config.getBool("body_pane_wraps")
    #@-node:AGP.20250415230112.1434:<< Set local vars >>
    #@nl
    old = {}
    pluginsList = [] # 5/17/03: a list of items for use by plugins.
    for p in p.self_and_parents_iter():
        s = p.v.t.bodyString
        theDict = g.get_directives_dict(s)
        #@        << Test for @comment and @language >>
        #@+node:AGP.20250415230112.1435:<< Test for @comment and @language >>
        # 1/23/05: Any previous @language or @comment prevents processing up the tree.
        # This code is now like the code in tangle.scanAlldirectives.
        
        if old.has_key("comment") or old.has_key("language"):
            pass
        
        elif theDict.has_key("comment"):
            k = theDict["comment"]
            delim1,delim2,delim3 = g.set_delims_from_string(s[k:])
        
        elif theDict.has_key("language"):
            k = theDict["language"]
            language,delim1,delim2,delim3 = g.set_language(s,k)
        #@-node:AGP.20250415230112.1435:<< Test for @comment and @language >>
        #@nl
        #@        << Test for @encoding >>
        #@+node:AGP.20250415230112.1436:<< Test for @encoding >>
        if not old.has_key("encoding") and theDict.has_key("encoding"):
            
            e = g.scanAtEncodingDirective(s,theDict)
            if e:
                encoding = e
        #@-node:AGP.20250415230112.1436:<< Test for @encoding >>
        #@nl
        #@        << Test for @lineending >>
        #@+node:AGP.20250415230112.1437:<< Test for @lineending >>
        if not old.has_key("lineending") and theDict.has_key("lineending"):
            
            e = g.scanAtLineendingDirective(s,theDict)
            if e:
                lineending = e
        #@-node:AGP.20250415230112.1437:<< Test for @lineending >>
        #@nl
        #@        << Test for @pagewidth >>
        #@+node:AGP.20250415230112.1438:<< Test for @pagewidth >>
        if theDict.has_key("pagewidth") and not old.has_key("pagewidth"):
            
            w = g.scanAtPagewidthDirective(s,theDict)
            if w and w > 0:
                page_width = w
        #@-node:AGP.20250415230112.1438:<< Test for @pagewidth >>
        #@nl
        #@        << Test for @path >>
        #@+node:AGP.20250415230112.1439:<< Test for @path >>
        if not path and not old.has_key("path") and theDict.has_key("path"):
        
            k = theDict["path"]
            #@    << compute relative path from s[k:] >>
            #@+node:AGP.20250415230112.1440:<< compute relative path from s[k:] >>
            j = i = k + len("@path")
            i = g.skip_to_end_of_line(s,i)
            path = string.strip(s[j:i])
            
            # Remove leading and trailing delims if they exist.
            if len(path) > 2 and (
                (path[0]=='<' and path[-1] == '>') or
                (path[0]=='"' and path[-1] == '"') ):
                path = path[1:-1]
            
            path = string.strip(path)
            if 0: # 11/14/02: we want a _relative_ path, not an absolute path.
                path = g.os_path_join(app.loadDir,path)
            #@-node:AGP.20250415230112.1440:<< compute relative path from s[k:] >>
            #@nl
            if path and len(path) > 0:
                base = g.getBaseDirectory(c=c) # returns "" on error.
                path = g.os_path_join(base,path)
        #@-node:AGP.20250415230112.1439:<< Test for @path >>
        #@nl
        #@        << Test for @tabwidth >>
        #@+node:AGP.20250415230112.1441:<< Test for @tabwidth >>
        if theDict.has_key("tabwidth") and not old.has_key("tabwidth"):
            
            w = g.scanAtTabwidthDirective(s,theDict)
            if w and w != 0:
                tab_width = w
        #@-node:AGP.20250415230112.1441:<< Test for @tabwidth >>
        #@nl
        #@        << Test for @wrap and @nowrap >>
        #@+node:AGP.20250415230112.1442:<< Test for @wrap and @nowrap >>
        if not old.has_key("wrap") and not old.has_key("nowrap"):
            
            if theDict.has_key("wrap"):
                wrap = True
            elif theDict.has_key("nowrap"):
                wrap = False
        #@-node:AGP.20250415230112.1442:<< Test for @wrap and @nowrap >>
        #@nl
        g.doHook("scan-directives",c=c,p=p,v=p,s=s,
            old_dict=old,dict=theDict,pluginsList=pluginsList)
        old.update(theDict)

    if path == None: path = g.getBaseDirectory(c=c)

    return {
        "delims"    : (delim1,delim2,delim3),
        "encoding"  : encoding,
        "language"  : language,
        "lineending": lineending,
        "pagewidth" : page_width,
        "path"      : path,
        "tabwidth"  : tab_width,
        "pluginsList": pluginsList,
        "wrap"      : wrap }
#@-node:AGP.20250415230112.1433:g.scanDirectives
#@-node:AGP.20250415230112.1415:Directive utils...
#@+node:AGP.20250415230112.1443:g.openWithFileName
def openWithFileName(fileName,old_c,enableLog=True,readAtFileNodesFlag=True):
    
    """Create a Leo Frame for the indicated fileName if the file exists."""

    if not fileName or len(fileName) == 0:
        return False, None
        
    def munge(name):
        name = name or ''
        return g.os_path_normpath(name).lower()

    # Create a full, normalized, Unicode path name, preserving case.
    fileName = g.os_path_normpath(g.os_path_abspath(fileName))

    # If the file is already open just bring its window to the front.
    theList = app.windowList
    for frame in theList:
        if munge(fileName) == munge(frame.c.mFileName):
            frame.bringToFront()
            frame.c.setLog()
            return True, frame
    try:
        if old_c:
            # New in 4.4: We must read the file *twice*.
            # The first time sets settings for the later call to c.finishCreate.
            # g.trace('***** prereading',fileName)
            
            #c2 = g.app.config.openSettingsFile(fileName)
            #if c2: g.app.config.updateSettings(c2,localFlag=True)
            pass
        # Open the file in binary mode to allow 0x1a in bodies & headlines.
        theFile = open(fileName,'rb')
        c,frame = app.newLeoCommanderAndFrame(fileName)
        
        frame.log.enable(enableLog)
        g.app.writeWaitingLog() # New in 4.3: write queued log first.
        c.beginUpdate()
        try:
            if not g.doHook("open1",old_c=old_c,c=c,new_c=c,fileName=fileName):
                c.setLog()
                app.lockLog()
                frame.c.fileCommands.open(theFile,fileName,
                                            readAtFileNodesFlag=readAtFileNodesFlag) # closes file.
                app.unlockLog()
                for frame in g.app.windowList:
                    # The recent files list has been updated by menu.updateRecentFiles.
                    frame.c.config.setRecentFiles(g.app.config.recentFiles)
            # Bug fix in 4.4.
            frame.openDirectory = g.os_path_abspath(g.os_path_dirname(fileName))
            g.doHook("open2",old_c=old_c,c=c,new_c=frame.c,fileName=fileName)
        
            c.frame.body.colorizer.scan_tree()
            c.frame.body.colorizer.colorize(c.currentPosition())
        
        finally:
            c.endUpdate()
            k = c.k
            #agpkeyk and k.setInputState(k.unboundKeyAction)
            if c.config.getBool('outline_pane_has_initial_focus'):
                c.treeWantsFocusNow()
            else:
                c.bodyWantsFocusNow()
        
        #g.color_gen_theme('#08090A','#e8e8FF',1.0) 
        
        frame.show()
        return True, frame
    except IOError:
        # Do not use string + here: it will fail for non-ascii strings!
        g.es("can not open: %s" % (fileName), color="blue")
        return False, None
    except Exception:
        g.es("exceptions opening: %s" % (fileName),color="red")
        g.es_exception()
        return False, None
#@nonl
#@-node:AGP.20250415230112.1443:g.openWithFileName
#@+node:AGP.20250415230112.1444:wrap_lines
#@+at 
#@nonl
# Important note: this routine need not deal with leading whitespace.  
# Instead, the caller should simply reduce pageWidth by the width of leading 
# whitespace wanted, then add that whitespace to the lines returned here.
# 
# The key to this code is the invarient that line never ends in whitespace.
#@-at
#@@c

def wrap_lines (lines,pageWidth,firstLineWidth=None):

    """Returns a list of lines, consisting of the input lines wrapped to the given pageWidth."""

    if pageWidth < 10:
        pageWidth = 10
        
    # DTHEIN 3-NOV-2002: First line is special
    if not firstLineWidth:
        firstLineWidth = pageWidth
    if firstLineWidth < 10:
        firstLineWidth = 10
    outputLineWidth = firstLineWidth

    # g.trace(lines)
    result = [] # The lines of the result.
    line = "" # The line being formed.  It never ends in whitespace.
    for s in lines:
        i = 0
        while i < len(s):
            assert(len(line) <= outputLineWidth) # DTHEIN 18-JAN-2004
            j = g.skip_ws(s,i)   # ;   ws = s[i:j]
            k = g.skip_non_ws(s,j) ; word = s[j:k]
            assert(k>i)
            i = k
            # DTHEIN 18-JAN-2004: wrap at exactly the text width, 
            # not one character less
            # 
            wordLen = len(word)
            if len(line) > 0 and wordLen > 0: wordLen += len(" ")
            if wordLen + len(line) <= outputLineWidth:
                if wordLen > 0:
                    #@                    << place blank and word on the present line >>
                    #@+node:AGP.20250415230112.1445:<< place blank and word on the present line >>
                    if len(line) == 0:
                        # Just add the word to the start of the line.
                        line = word
                    else:
                        # Add the word, preceeded by a blank.
                        line = " ".join([line,word]) # DTHEIN 18-JAN-2004: better syntax
                    #@-node:AGP.20250415230112.1445:<< place blank and word on the present line >>
                    #@nl
                else: pass # discard the trailing whitespace.
            else:
                #@                << place word on a new line >>
                #@+node:AGP.20250415230112.1446:<< place word on a new line >>
                # End the previous line.
                if len(line) > 0:
                    result.append(line)
                    outputLineWidth = pageWidth # DTHEIN 3-NOV-2002: width for remaining lines
                    
                # Discard the whitespace and put the word on a new line.
                line = word
                
                # Careful: the word may be longer than pageWidth.
                if len(line) > pageWidth: # DTHEIN 18-JAN-2004: line can equal pagewidth
                    result.append(line)
                    outputLineWidth = pageWidth # DTHEIN 3-NOV-2002: width for remaining lines
                    line = ""
                #@-node:AGP.20250415230112.1446:<< place word on a new line >>
                #@nl
    if len(line) > 0:
        result.append(line)
    # g.trace(result)
    return result
#@-node:AGP.20250415230112.1444:wrap_lines
#@-node:AGP.20250415230112.1407:Commands & Directives
#@+node:AGP.20250415230112.1447:Debugging, Dumping, Timing, Tracing & Sherlock
#@+node:AGP.20250415230112.1448:alert
def alert(message):

    g.es(message)

    import tkMessageBox
    tkMessageBox.showwarning("Alert", message)
#@-node:AGP.20250415230112.1448:alert
#@+node:AGP.20250415230112.1449:callers
def callers (n=8,excludeCaller=True,files=False):
    
    '''Return a list containing the callers of the function that called g.callerList.
    
    By default, the function that called g.callerList is not on the list,
    which is what is wanted when using g.trace.'''
    
    result = [] ; first = True
    while n > 0:
        s = g._callerName(n,files=files)
        if s.endswith('callers'):
            if excludeCaller and result:
                del result [-1]
            break
        elif s:
            if first and files:
                first = False ; s = '\n' + s
            result.append(s)
        n -= 1
        
    sep = g.choose(files,'\n',',')
    return sep.join(result)
#@-node:AGP.20250415230112.1449:callers
#@+node:AGP.20250415230112.1450:_callerName
def _callerName (n=1,files=False):

    try: # get the function name from the call stack.
        f1 = sys._getframe(n) # The stack frame, n levels up.
        code1 = f1.f_code # The code object
        if files:
            return '%s:%s' % (g.shortFilename(code1.co_filename),code1.co_name)
        else:
            return code1.co_name # The code name
    except ValueError:
        return '' # The stack is not deep enough.
    except:
        g.es_exception()
        return '' # "<no caller name>"
#@-node:AGP.20250415230112.1450:_callerName
#@+node:AGP.20250415230112.1451:g.pdb & test
def pdb ():
    
    """Fall into pdb."""

    import pdb # Required: we have just defined pdb as a function!

    pdb.set_trace()
#@+node:AGP.20250415230112.1452:test_g_pdb
def test_g_pdb():
    
    import sys
    
    # Not a good unit test; it probably will never fail.
    def aFunction(): pass
    assert type(g.pdb)==type(aFunction), 'wrong type for g.pdb: %s' % type(g.pdb)
    
    class myStdout:
        def write(self,s):
            pass # g.es('From pdb:',s)
        
    class myStdin:
        def readline (self):
            return 'c' # Return 'c' (continue) for all requests for input.
            
    def restore():
        sys.stdout,sys.stdin = sys.__stdout__,sys.__stdin__
     
    try:
        sys.stdin = myStdin() # Essential
        sys.stdout=myStdout() # Optional
        g.pdb()
        restore()
        # assert False,'test of reraising'
    except Exception:
        restore()
        raise
#@-node:AGP.20250415230112.1452:test_g_pdb
#@-node:AGP.20250415230112.1451:g.pdb & test
#@+node:AGP.20250415230112.1453:Dumps
#@+node:AGP.20250415230112.1454:dump
def dump(s):
    
    out = ""
    for i in s:
        out += str(ord(i)) + ","
    return out
        
def oldDump(s):

    out = ""
    for i in s:
        if i=='\n':
            out += "[" ; out += "n" ; out += "]"
        if i=='\t':
            out += "[" ; out += "t" ; out += "]"
        elif i==' ':
            out += "[" ; out += " " ; out += "]"
        else: out += i
    return out
#@-node:AGP.20250415230112.1454:dump
#@+node:AGP.20250415230112.1455:es_dump
def es_dump (s,n = 30,title=None):
    
    if title:
        g.es_print(title)

    i = 0
    while i < len(s):
        g.es_print(''.join(['%2x ' % (ord(ch)) for ch in s[i:i+n]]))
        i += n
#@nonl
#@-node:AGP.20250415230112.1455:es_dump
#@+node:AGP.20250415230112.1456:es_error
def es_error (s,color=None):

    if color is None and g.app.config: # May not exist during initialization.
        color = g.theme['error'] #g.app.config.getColor(None,"log_error_color")

    g.es(s,color=color)
#@-node:AGP.20250415230112.1456:es_error
#@+node:AGP.20250415230112.1457:es_event_exception
def es_event_exception (eventName,full=False):

    g.es("exception handling ", eventName, " event")
    typ,val,tb = sys.exc_info()

    if full:
        errList = traceback.format_exception(typ,val,tb)
    else:
        errList = traceback.format_exception_only(typ,val)

    for i in errList:
        g.es(i)
        
    if not g.stdErrIsRedirected(): # 2/16/04
        traceback.print_exc()
#@-node:AGP.20250415230112.1457:es_event_exception
#@+node:AGP.20250415230112.1458:es_exception & test
def es_exception (full=True,c=None,color="red"):
    
    typ,val,tb = sys.exc_info()

    # g.trace(full,typ,tb)
    
    fileName,n = g.getLastTracebackFileAndLineNumber()

    if full or g.app.debugSwitch > 0:
        lines = traceback.format_exception(typ,val,tb)
    else:
        lines = traceback.format_exception_only(typ,val)
        if 0: # We might as well print the entire SyntaxError message.
            lines = lines[-1:] # Usually only one line, but more for Syntax errors!

    for line in lines:
        g.es_error(line,color=color)
        if not g.stdErrIsRedirected():
            print line

    if g.app.debugSwitch > 1:
        import pdb # Be careful: g.pdb may or may not have been defined.
        pdb.set_trace()

    return fileName,n
#@+node:AGP.20250415230112.1459:test_g_es_exception
def test_g_es_exception():
    
    if c.config.redirect_execute_script_output_to_log_pane:
        return # Test doesn't work when redirection is on.

    try:
        import sys
        # Catch the output of g.es_exception.
        # We catch the AssertionError, so nothing gets written to stderr.
        sys.stdout = fo = g.fileLikeObject()
        try: # Create an exception to catch.
            assert False, 'Assert False in test_g_es_exception'
        except AssertionError:
            g.es_exception(color='suppress')
            result = fo.get()
            s1 = 'Traceback (most recent call last):'
            s2 = 'AssertionError: Assert False in test_g_es_exception'
            assert result.find(s1) > -1, 'No traceback line: %s' % repr(result)
            assert result.find(s2) > -1, 'No AssertionError line: %s' % repr(result)
    finally:
        # Not needed unless we execute this script as selected text.
        sys.stdout = sys.__stdout__
#@-node:AGP.20250415230112.1459:test_g_es_exception
#@-node:AGP.20250415230112.1458:es_exception & test
#@+node:AGP.20250415230112.1460:es_exception_type
def es_exception_type (c=None,color="red"):
    
    # exctype is a Exception class object; value is the error message.
    exctype, value = sys.exc_info()[:2]
    
    g.es_print('%s, %s' % (exctype.__name__, value),color=color)
#@-node:AGP.20250415230112.1460:es_exception_type
#@+node:AGP.20250415230112.1461:getLastTracebackFileAndLineNumber
def getLastTracebackFileAndLineNumber():
    
    typ,val,tb = sys.exc_info()
    
    if typ in (exceptions.SyntaxError,exceptions.IndentationError):
        # Syntax and indentation errors are a special case.
        # extract_tb does _not_ return the proper line number!
        # This code is similar to the code in format_exception_only(!!)
        try:
            # g.es_print(repr(val))
            msg,(filename, lineno, offset, line) = val
            return filename,lineno
        except:
            g.trace("bad line number")
            return None,0

    else:
        # The proper line number is the second element in the last tuple.
        data = traceback.extract_tb(tb)
        # g.es_print(repr(data))
        item = data[-1]
        filename = item[0]
        n = item[1]
        return filename,n
#@-node:AGP.20250415230112.1461:getLastTracebackFileAndLineNumber
#@+node:AGP.20250415230112.1462:printBindings
def print_bindings (name,window):

    bindings = window.bind()
    
    print "Bindings for", name
    for b in bindings:
        print b
#@-node:AGP.20250415230112.1462:printBindings
#@+node:AGP.20250415230112.1463:printGlobals
def printGlobals(message=None):
    
    # Get the list of globals.
    globs = list(globals())
    globs.sort()
    
    # Print the list.
    if message:
        leader = "-" * 10
        print leader, ' ', message, ' ', leader
    for glob in globs:
        print glob
#@-node:AGP.20250415230112.1463:printGlobals
#@+node:AGP.20250415230112.1464:printLeoModules
def printLeoModules(message=None):
    
    # Create the list.
    mods = []
    for name in sys.modules.keys():
        if name and name[0:3] == "leo":
            mods.append(name)

    # Print the list.
    if message:
        leader = "-" * 10
        print leader, ' ', message, ' ', leader
    mods.sort()
    for m in mods:
        print m,
    print
#@-node:AGP.20250415230112.1464:printLeoModules
#@-node:AGP.20250415230112.1453:Dumps
#@+node:AGP.20250415230112.1465:file/module/plugin_date
def module_date (mod,format=None):
    theFile = g.os_path_join(app.loadDir,mod.__file__)
    root,ext = g.os_path_splitext(theFile) 
    return g.file_date(root + ".py",format=format)

def plugin_date (plugin_mod,format=None):
    theFile = g.os_path_join(app.loadDir,"..","plugins",plugin_mod.__file__)
    root,ext = g.os_path_splitext(theFile) 
    return g.file_date(root + ".py",format=format)

def file_date (theFile,format=None):
    if theFile and len(theFile)and g.os_path_exists(theFile):
        try:
            n = g.os_path_getmtime(theFile)
            if format == None:
                format = "%m/%d/%y %H:%M:%S"
            return time.strftime(format,time.gmtime(n))
        except (ImportError,NameError):
            pass # Time module is platform dependent.
    return ""
#@-node:AGP.20250415230112.1465:file/module/plugin_date
#@+node:AGP.20250415230112.1466:redirecting stderr and stdout to Leo's log pane
class redirectClass:
    
    """A class to redirect stdout and stderr to Leo's log pane."""

    #@    << redirectClass methods >>
    #@+node:AGP.20250415230112.1467:<< redirectClass methods >>
    #@+others
    #@+node:AGP.20250415230112.1468:redirectClass.__init__
    def __init__ (self):
        
        self.old = None
    #@-node:AGP.20250415230112.1468:redirectClass.__init__
    #@+node:AGP.20250415230112.1469:isRedirected
    def isRedirected (self):
    
        return self.old != None
    #@-node:AGP.20250415230112.1469:isRedirected
    #@+node:AGP.20250415230112.1470:flush
    # For LeoN: just for compatibility.
    
    def flush(self, *args):
        return
    #@-node:AGP.20250415230112.1470:flush
    #@+node:AGP.20250415230112.1471:rawPrint
    def rawPrint (self,s):
    
        if self.old:
            self.old.write(s+'\n')
        else:
            print s
    #@-node:AGP.20250415230112.1471:rawPrint
    #@+node:AGP.20250415230112.1472:redirect
    def redirect (self,stdout=1):
    
        if g.app.batchMode:
            # Redirection is futile in batch mode.
            return
    
        if not self.old:
            if stdout:
                self.old,sys.stdout = sys.stdout,self
            else:
                self.old,sys.stderr = sys.stderr,self
    #@-node:AGP.20250415230112.1472:redirect
    #@+node:AGP.20250415230112.1473:undirect
    def undirect (self,stdout=1):
    
        if self.old:
            if stdout:
                sys.stdout,self.old = self.old,None
            else:
                sys.stderr,self.old = self.old,None
    #@-node:AGP.20250415230112.1473:undirect
    #@+node:AGP.20250415230112.1474:write
    def write(self,s):
    
        if self.old:
            if app.log:
                app.log.put(s)
            else:
                self.old.write(s+'\n')
        else:
            # Can happen when g.batchMode is True.
            print s
    #@-node:AGP.20250415230112.1474:write
    #@-others
    #@-node:AGP.20250415230112.1467:<< redirectClass methods >>
    #@nl

# Create two redirection objects, one for each stream.
redirectStdErrObj = redirectClass()
redirectStdOutObj = redirectClass()

#@<< define convenience methods for redirecting streams >>
#@+node:AGP.20250415230112.1475:<< define convenience methods for redirecting streams >>
#@+others
#@+node:AGP.20250415230112.1476:redirectStderr & redirectStdout
# Redirect streams to the current log window.
def redirectStderr():
    global redirectStdErrObj
    redirectStdErrObj.redirect(stdout=False)

def redirectStdout():
    global redirectStdOutObj
    redirectStdOutObj.redirect()
#@-node:AGP.20250415230112.1476:redirectStderr & redirectStdout
#@+node:AGP.20250415230112.1477:restoreStderr & restoreStdout
# Restore standard streams.
def restoreStderr():
    global redirectStdErrObj
    redirectStdErrObj.undirect(stdout=False)
    
def restoreStdout():
    global redirectStdOutObj
    redirectStdOutObj.undirect()
#@-node:AGP.20250415230112.1477:restoreStderr & restoreStdout
#@+node:AGP.20250415230112.1478:stdErrIsRedirected & stdOutIsRedirected
def stdErrIsRedirected():
    global redirectStdErrObj
    return redirectStdErrObj.isRedirected()
    
def stdOutIsRedirected():
    global redirectStdOutObj
    return redirectStdOutObj.isRedirected()
#@-node:AGP.20250415230112.1478:stdErrIsRedirected & stdOutIsRedirected
#@+node:AGP.20250415230112.1479:rawPrint
# Send output to original stdout.

def rawPrint(s):

    global redirectStdOutObj

    redirectStdOutObj.rawPrint(s)
#@-node:AGP.20250415230112.1479:rawPrint
#@-others
#@-node:AGP.20250415230112.1475:<< define convenience methods for redirecting streams >>
#@nl

if 0: # Test code: may be executed in the child node.
    #@    << test code >>
    #@+node:AGP.20250415230112.1480:<< test code >>
    import leoGlobals as g ; import sys
    print >> sys.stdout, "stdout isRedirected:", g.stdOutIsRedirected()
    print >> sys.stderr, "stderr isRedirected:", g.stdErrIsRedirected()
    
    # stderr
    import leoGlobals as g ; import sys
    g.redirectStderr()
    print >> sys.stdout, "stdout isRedirected:", g.stdOutIsRedirected()
    print >> sys.stderr, "stderr isRedirected:", g.stdErrIsRedirected()
    
    import leoGlobals as g ; import sys
    g.restoreStderr()
    print >> sys.stdout, "stdout isRedirected:", g.stdOutIsRedirected()
    print >> sys.stderr, "stderr isRedirected:", g.stdErrIsRedirected()
    
    # stdout
    import leoGlobals as g ; import sys
    g.restoreStdout()
    print >> sys.stdout, "stdout isRedirected:", g.stdOutIsRedirected()
    print >> sys.stderr, "stderr isRedirected:", g.stdErrIsRedirected()
    
    import leoGlobals as g ; import sys
    g.redirectStdout()
    print >> sys.stdout, "stdout isRedirected:", g.stdOutIsRedirected()
    print >> sys.stderr, "stderr isRedirected:", g.stdErrIsRedirected()
    #@-node:AGP.20250415230112.1480:<< test code >>
    #@nl
#@-node:AGP.20250415230112.1466:redirecting stderr and stdout to Leo's log pane
#@+node:AGP.20250415230112.1481:get_line & get_line_after
# Very useful for tracing.

def get_line (s,i):

    nl = ""
    if g.is_nl(s,i):
        i = g.skip_nl(s,i)
        nl = "[nl]"
    j = g.find_line_start(s,i)
    k = g.skip_to_end_of_line(s,i)
    return nl + s[j:k]
    
def get_line_after (s,i):
    
    nl = ""
    if g.is_nl(s,i):
        i = g.skip_nl(s,i)
        nl = "[nl]"
    k = g.skip_to_end_of_line(s,i)
    return nl + s[i:k]
#@-node:AGP.20250415230112.1481:get_line & get_line_after
#@+node:AGP.20250415230112.1482:pause
def pause (s):
    
    print s
    
    i = 0
    while i < 1000000L:
        i += 1
#@-node:AGP.20250415230112.1482:pause
#@+node:AGP.20250415230112.1483:print_obj & toString
def print_obj (obj,tag=None,sort=False,verbose=True,indent=''):
    
    if type(obj) in (type(()),type([])):
        g.print_list(obj,tag,sort,indent)
    elif type(obj) == type({}):
        g.print_dict(obj,tag,verbose,indent)
    else:
        print '%s%s' % (indent,repr(obj).strip())
        
def toString (obj,tag=None,sort=False,verbose=True,indent=''):

    if type(obj) in (type(()),type([])):
        return g.listToString(obj,tag,sort,indent)
    elif type(obj) == type({}):
        return g.dictToString(obj,tag,verbose,indent)
    else:
        return '%s%s' % (indent,repr(obj).strip())
#@-node:AGP.20250415230112.1483:print_obj & toString
#@+node:AGP.20250415230112.1484:print_dict & dictToString
def print_dict(d,tag='',verbose=True,indent=''):
    
    if not d:
        if tag: print '%s...{}' % tag
        else:   print '{}'
        return
    
    keys = d.keys() ; keys.sort()
    n = 6
    for key in keys:
        if type(key) == type(''):
            n = max(n,len(key))
    if tag: print '%s...{\n' % tag
    else:   print '{\n'
    for key in keys:
        print "%s%*s: %s" % (indent,n,key,repr(d.get(key)).strip())
    print '}'

printDict = print_dict

def dictToString(d,tag=None,verbose=True,indent=''):
    
    if not d:
        if tag: return '%s...{}' % tag
        else:   return '{}'
    keys = d.keys() ; keys.sort()
    n = 6
    for key in keys:
        if type(key) in (type(''),type(u'')):
            n = max(n,len(key))
    lines = ["%s%*s: %s" % (indent,n,key,repr(d.get(key)).strip()) for key in keys]
    s = '\n'.join(lines)
    if tag:
        return '%s...{\n%s}\n' % (tag,s)
    else:
        return '{\n%s}\n' % s
#@-node:AGP.20250415230112.1484:print_dict & dictToString
#@+node:AGP.20250415230112.1485:print_list & listToString
def print_list(aList,tag=None,sort=False,indent=''):
    
    if not aList:
        if tag: print '%s...[]' % tag
        else:   print '[]'
        return
    if sort:
        bList = aList[:] # Sort a copy!
        bList.sort()
    else:
        bList = aList
    if tag: print '%s...[' % tag
    else:   print '['
    for e in bList:
        print '%s%s' % (indent,repr(e).strip())
    print ']'

printList = print_list

def listToString(aList,tag=None,sort=False,indent=''):

    if not aList:
        if tag: return '%s...{}' % tag
        else:   return '[]'
    if sort:
        bList = aList[:] # Sort a copy!
        bList.sort()
    else:
        bList = aList
    lines = ["%s%s" % (indent,repr(e).strip()) for e in bList]
    s = '\n'.join(lines)
    if tag:
        return '[%s...\n%s\n]' % (tag,s)
    else:
        return '[%s]' % s
#@-node:AGP.20250415230112.1485:print_list & listToString
#@+node:AGP.20250415230112.1486:print_stack (printStack)
def print_stack():

    traceback.print_stack()
    
printStack = print_stack
#@-node:AGP.20250415230112.1486:print_stack (printStack)
#@+node:AGP.20250415230112.1487:Sherlock... (trace)
#@+at 
#@nonl
# Starting with this release, you will see trace statements throughout the 
# code.  The trace function is defined in leoGlobals.py; trace implements much 
# of the functionality of my Sherlock tracing package.  Traces are more 
# convenient than print statements for two reasons: 1) you don't need explicit 
# trace names and 2) you can disable them without recompiling.
# 
# In the following examples, suppose that the call to trace appears in 
# function f.
# 
# g.trace(string) prints string if tracing for f has been enabled.  For 
# example, the following statment prints from s[i] to the end of the line if 
# tracing for f has been enabled.
# 
#   j = g.skip_line(s,i) ; g.trace(s[i:j])
# 
# g.trace(function) exectutes the function if tracing for f has been enabled.  
# For example,
# 
#   g.trace(self.f2)
# 
# You enable and disable tracing by calling g.init_trace(args).  Examples:
# 
#   g.init_trace("+*")         # enable all traces
#   g.init_trace("+a","+b")    # enable traces for a and b
#   g.init_trace(("+a","+b"))  # enable traces for a and b
#   g.init_trace("-a")         # disable tracing for a
#   traces = g.init_trace("?") # return the list of enabled traces
# 
# If two arguments are supplied to trace, the first argument is the 
# "tracepoint name" and the second argument is the "tracepoint action" as 
# shown in the examples above.  If tracing for the tracepoint name is enabled, 
# the tracepoint action is printed (if it is a string) or exectuted (if it is 
# a function name).
# 
# "*" will not match an explicit tracepoint name that starts with a minus 
# sign.  For example,
# 
#   g.trace_tag("-nocolor", self.disable_color)
#@-at
#@+node:AGP.20250415230112.1489:get_Sherlock_args
#@+at 
#@nonl
# It no args are given we attempt to get them from the "SherlockArgs" file.  
# If there are still no arguments we trace everything.  This default makes 
# tracing much more useful in Python.
#@-at
#@@c

def get_Sherlock_args (args):

    if not args or len(args)==0:
        try:
            fn = g.os_path_join(app.loadDir,"SherlockArgs")
            f = open(fn)
            args = f.readlines()
            f.close()
        except: pass
    elif type(args[0]) == type(("1","2")):
        args = args[0] # strip away the outer tuple.

    # No args means trace everything.
    if not args or len(args)==0: args = ["+*"] 
    # print "get_Sherlock_args:", args
    return args
#@-node:AGP.20250415230112.1489:get_Sherlock_args
#@+node:AGP.20250415230112.1490:init_trace
def init_trace(args,echo=1):

    t = app.trace_list
    args = g.get_Sherlock_args(args)

    for arg in args:
        if arg[0] in string.ascii_letters: prefix = '+'
        else: prefix = arg[0] ; arg = arg[1:]
        
        if prefix == '?':
            print "trace list:", t
        elif prefix == '+' and not arg in t:
            t.append(string.lower(arg))
            if echo:
                print "enabling:", arg
        elif prefix == '-' and arg in t:
            t.remove(string.lower(arg))
            if echo:
                print "disabling:", arg
        else:
            print "ignoring:", prefix + arg
#@-node:AGP.20250415230112.1490:init_trace
#@+node:AGP.20250415230112.1491:trace
# Convert all args to strings.

def trace (*args,**keys):
    
    callers = keys.get("callers",False)
    newline = keys.get("newline",True)
    align =   keys.get("align",0)

    s = ""
    for arg in args:
        if type(arg) == type(u""):
            pass
            # try:    arg = str(arg) 
            # except: arg = repr(arg)
        elif type(arg) != type(""):
            arg = repr(arg)
        if len(s) > 0:
            s = s + " " + arg
        else:
            s = arg
    message = s
    try: # get the function name from the call stack.
        f1 = sys._getframe(1) # The stack frame, one level up.
        code1 = f1.f_code # The code object
        name = code1.co_name # The code name
    except: name = ""
    if name == "?":
        name = "<unknown>"

    if callers:
        traceback.print_stack()
        
    if align != 0 and len(name) < abs(align):
        pad = ' ' * (abs(align) - len(name))
        if align > 0: name = name + pad
        else:         name = pad + name

    if newline:
        print name + ": " + message
    else:
        print name + ": " + message,
#@nonl
#@-node:AGP.20250415230112.1491:trace
#@+node:AGP.20250415230112.1492:trace_tag
# Convert all args to strings.
# Print if tracing for name has been enabled.

def trace_tag (name, *args):
    
    s = ""
    for arg in args:
        if type(arg) != type(""):
            arg = repr(arg)
        if len(s) > 0:
            s = s + ", " + arg
        else:
            s = arg
    message = s

    t = app.trace_list
    # tracepoint names starting with '-' must match exactly.
    minus = len(name) > 0 and name[0] == '-'
    if minus: name = name[1:]
    if (not minus and '*' in t) or name.lower() in t:
        s = name + ": " + message
        print s # Traces _always_ get printed.
#@-node:AGP.20250415230112.1492:trace_tag
#@-node:AGP.20250415230112.1487:Sherlock... (trace)
#@+node:AGP.20250415230112.1493:Statistics
#@+node:AGP.20250415230112.1494:clear_stats
def clear_stats():
    
    g.trace()
    
    g.app.statsDict = {}

clearStats = clear_stats
#@-node:AGP.20250415230112.1494:clear_stats
#@+node:AGP.20250415230112.1495:print_stats
def print_stats (name=None):

    if name:
        if type(name) != type(""):
            name = repr(name)
    else:
        name = g._callerName(n=2) # Get caller name 2 levels back.

    g.printDict(g.app.statsDict,tag='statistics at %s' % name)

printStats = print_stats
#@-node:AGP.20250415230112.1495:print_stats
#@+node:AGP.20250415230112.1496:stat
def stat (name=None):

    """Increments the statistic for name in g.app.statsDict
    The caller's name is used by default.
    """
    
    d = g.app.statsDict
    
    if name:
        if type(name) != type(""):
            name = repr(name)
    else:
        name = g._callerName(n=2) # Get caller name 2 levels back.
        
    # g.trace(name)

    d [name] = 1 + d.get(name,0)
#@-node:AGP.20250415230112.1496:stat
#@-node:AGP.20250415230112.1493:Statistics
#@+node:AGP.20250415230112.1497:Timing
def getTime():
    return time.clock()
    
def esDiffTime(message, start):
    g.es("%s %6.3f" % (message,(time.clock()-start)))
    return time.clock()
    
def printDiffTime(message, start):
    print "%s %6.3f" % (message,(time.clock()-start))
    return time.clock()
#@-node:AGP.20250415230112.1497:Timing
#@-node:AGP.20250415230112.1447:Debugging, Dumping, Timing, Tracing & Sherlock
#@+node:AGP.20250415230112.1498:Files & Directories...
#@+node:AGP.20250415230112.1499:create_temp_file & test
def create_temp_file (textMode=False):
    '''Return a tuple (theFile,theFileName)

    theFile: a file object open for writing.
    theFileName: the name of the temporary file.'''
    
    # mktemp is deprecated, but we can't get rid of it
    # because mkstemp does not exist in Python 2.2.1.
    
    try:
        # fd is an handle to an open file as would be returned by os.open()
        fd,theFileName = tempfile.mkstemp(text=textMode)
        mode = g.choose(textMode,'w','wb')
        theFile = os.fdopen(fd,mode)
        # g.trace(fd,theFile)
    except AttributeError:
        # g.trace("mkstemp doesn't exist")
        theFileName = tempfile.mktemp()
        try:
            mode = g.choose(textMode,'w','wb')
            theFile = file(theFileName,mode)
        except IOError:
            theFile,theFileName = None,''
    except Exception:
        g.es('Unexpected exception in g.create_temp_file',color='red')
        g.es_exception()
        theFile,theFileName = None,''

    return theFile,theFileName
#@+node:AGP.20250415230112.1500:test_g_create_temp_file
def test_g_create_temp_file():
    
    import types

    theFile,theFileName = g.create_temp_file()

    assert type(theFile) == types.FileType, 'not file type'
    assert type(theFileName) in (types.StringType, types.UnicodeType), 'not string type'
#@-node:AGP.20250415230112.1500:test_g_create_temp_file
#@-node:AGP.20250415230112.1499:create_temp_file & test
#@+node:AGP.20250415230112.1501:ensure_extension
def ensure_extension (name, ext):

    theFile, old_ext = g.os_path_splitext(name)
    if not name:
        return name # don't add to an empty name.
    elif old_ext and old_ext == ext:
        return name
    else:
        return name + ext
#@-node:AGP.20250415230112.1501:ensure_extension
#@+node:AGP.20250415230112.1502:g.is_sentinel
def is_sentinel (line,delims):
    
    #@    << is_sentinel doc tests >>
    #@+node:AGP.20250415230112.1503:<< is_sentinel doc tests >>
    """
    
    Return True if line starts with a sentinel comment.
    
    >>> py_delims = comment_delims_from_extension('.py')
    >>> is_sentinel("#@+node",py_delims)
    True
    >>> is_sentinel("#comment",py_delims)
    False
    
    >>> c_delims = comment_delims_from_extension('.c')
    >>> is_sentinel("//@+node",c_delims)
    True
    >>> is_sentinel("//comment",c_delims)
    False
    
    >>> html_delims = comment_delims_from_extension('.html')
    >>> is_sentinel("<!--@+node-->",html_delims)
    True
    >>> is_sentinel("<!--comment-->",html_delims)
    False
    
    """
    #@-node:AGP.20250415230112.1503:<< is_sentinel doc tests >>
    #@nl
    
    delim1,delim2,delim3 = delims
    
    line = line.lstrip()

    if delim1:
        return line.startswith(delim1+'@')
    elif delim2 and delim3:
        i = line.find(delim2+'@')
        j = line.find(delim3)
        return 0 == i < j
    else:
        print repr(delims)
        g.es("Can't happen: is_sentinel",color="red")
        return False
#@-node:AGP.20250415230112.1502:g.is_sentinel
#@+node:AGP.20250415230112.1504:Used by tangle code & leoFileCommands
#@+node:AGP.20250415230112.1505:g.update_file_if_changed
# This is part of the tangle code.

def update_file_if_changed(file_name,temp_name):

    """Compares two files.
    
    If they are different, we replace file_name with temp_name.
    Otherwise, we just delete temp_name. Both files should be closed."""

    if g.os_path_exists(file_name):
        if filecmp.cmp(temp_name, file_name):
            kind = 'unchanged'
            ok = g.utils_remove(temp_name)
        else:
            kind = '***updating'
            mode = g.utils_stat(file_name)
            ok = g.utils_rename(temp_name,file_name,mode)
    else:
        kind = 'creating'
        ok = g.utils_rename(temp_name,file_name)
        
    if ok:
        g.es('%12s: %s' % (kind,file_name))
    else:
        g.es("rename failed: no file created!",color="red")
        g.es(file_name," may be read-only or in use")
#@-node:AGP.20250415230112.1505:g.update_file_if_changed
#@+node:AGP.20250415230112.1506:g.utils_remove & test
def utils_remove (fileName,verbose=True):

    try:
        os.remove(fileName)
        return True
    except:
        if verbose:
            g.es("exception removing:" + fileName)
            g.es_exception()
        return False
#@+node:AGP.20250415230112.1507:test_g_utils_remove
def test_g_utils_remove():

    import os
    exists = g.os_path_exists
    
    path = g.os_path_join(g.app.testDir,'xyzzy')
    if exists(path):
        os.remove(path)
        
    assert not exists(path)
    assert not g.utils_remove(path,verbose=False)
    
    f = file(path,'w')
    f.write('test')
    f.close()
    
    assert exists(path)
    assert g.utils_remove(path,verbose=True)
    assert not exists(path)
#@-node:AGP.20250415230112.1507:test_g_utils_remove
#@-node:AGP.20250415230112.1506:g.utils_remove & test
#@+node:AGP.20250415230112.1508:g.utils_rename & test
#@<< about os.rename >>
#@+node:AGP.20250415230112.1509:<< about os.rename >>
#@+at 
#@nonl
# Here is the Python 2.4 documentation for rename (same as Python 2.3)
# 
# Rename the file or directory src to dst.  If dst is a directory, OSError 
# will be raised.
# 
# On Unix, if dst exists and is a file, it will be removed silently if the 
# user
# has permission. The operation may fail on some Unix flavors if src and dst 
# are
# on different filesystems. If successful, the renaming will be an atomic
# operation (this is a POSIX requirement).
# 
# On Windows, if dst already exists, OSError will be raised even if it is a 
# file;
# there may be no way to implement an atomic rename when dst names an existing
# file.
#@-at
#@-node:AGP.20250415230112.1509:<< about os.rename >>
#@nl

def utils_rename (src,dst,mode=None,verbose=True):

    '''Platform independent rename.'''

    head, tail = g.os_path_split(dst)
    if head and len(head) > 0:
        g.makeAllNonExistentDirectories(head)

    if g.os_path_exists(dst):
        if not g.utils_remove(dst):
            return False
    try:
        # New in Leo 4.4b1: try using shutil first.
        try:
            import shutil # shutil is new in Python 2.3
            shutil.move(src,dst)
        except ImportError:
            if sys.platform == "win32":
                os.rename(src,dst)
            else:
                try:
                    # Alas, distutils.file_util may not exist.
                    from distutils.file_util import move_file
                    move_file(src,dst)
                except ImportError:
                    # Desperation: may give: 'Invalid cross-device link'
                    os.rename(src,dst)
        if mode:
            g.utils_chmod(dst,mode,verbose)
        return True
    except Exception:
        if verbose:
            g.es('Exception renaming %s to %s' % (src,dst),color='red')
            g.es_exception(full=False)
        return False
#@+node:AGP.20250415230112.1510:test_g_utils_rename
def test_g_utils_rename():

    import os
    exists = g.os_path_exists
    
    path = g.os_path_join(g.app.testDir,'xyzzy')
    if exists(path):
        os.remove(path)
        
    assert not exists(path)
    assert not g.utils_remove(path,verbose=False)
    
    f = file(path,'w')
    f.write('test')
    f.close()
    
    assert exists(path)
    assert g.utils_remove(path,verbose=True)
    assert not exists(path)
#@-node:AGP.20250415230112.1510:test_g_utils_rename
#@-node:AGP.20250415230112.1508:g.utils_rename & test
#@+node:AGP.20250415230112.1511:g.utils_chmod
def utils_chmod (fileName,mode,verbose=True):
    
    if mode is None:
        return

    try:
        os.chmod(fileName,mode)
    except:
        if verbose:
            g.es("exception in os.chmod(%s)" % (fileName))
            g.es_exception()
#@-node:AGP.20250415230112.1511:g.utils_chmod
#@+node:AGP.20250415230112.1512:g.utils_stat
def utils_stat (fileName):

    '''Return the access mode of named file, removing any setuid, setgid, and sticky bits.'''

    try:
        mode = (os.stat(fileName))[0] & 0777
    except:
        mode = None
        
    return mode
#@-node:AGP.20250415230112.1512:g.utils_stat
#@-node:AGP.20250415230112.1504:Used by tangle code & leoFileCommands
#@+node:AGP.20250415230112.1513:getBaseDirectory
# Handles the conventions applying to the "relative_path_base_directory" configuration option.

def getBaseDirectory(c=None):

    base = app.config.relative_path_base_directory

    if base and base == "!":
        base = app.loadDir
    elif base and base == ".":
        base = c.openDirectory

    # g.trace(base)
    if base and len(base) > 0 and g.os_path_isabs(base):
        return base # base need not exist yet.
    else:
        return "" # No relative base given.
#@-node:AGP.20250415230112.1513:getBaseDirectory
#@+node:AGP.20250415230112.1514:makeAllNonExistentDirectories
# This is a generalization of os.makedir.

def makeAllNonExistentDirectories (theDir):

    """Attempt to make all non-existent directories"""

    if not app.config.create_nonexistent_directories:
        return None

    dir1 = theDir = g.os_path_normpath(theDir)

    # Split theDir into all its component parts.
    paths = []
    while len(theDir) > 0:
        head,tail=g.os_path_split(theDir)
        if len(tail) == 0:
            paths.append(head)
            break
        else:
            paths.append(tail)
            theDir = head
    path = ""
    paths.reverse()
    for s in paths:
        path = g.os_path_join(path,s)
        if not g.os_path_exists(path):
            try:
                os.mkdir(path)
                g.es("created directory: "+path)
            except:
                g.es("exception creating directory: "+path)
                g.es_exception()
                return None
    return dir1 # All have been created.
#@-node:AGP.20250415230112.1514:makeAllNonExistentDirectories
#@+node:AGP.20250415230112.1515:readlineForceUnixNewline (Steven P. Schaefer)
#@+at 
#@nonl
# Stephen P. Schaefer 9/7/2002
# 
# The Unix readline() routine delivers "\r\n" line end strings verbatim, while 
# the windows versions force the string to use the Unix convention of using 
# only "\n".  This routine causes the Unix readline to do the same.
#@-at
#@@c

def readlineForceUnixNewline(f):

    s = f.readline()
    if len(s) >= 2 and s[-2] == "\r" and s[-1] == "\n":
        s = s[0:-2] + "\n"
    return s
#@-node:AGP.20250415230112.1515:readlineForceUnixNewline (Steven P. Schaefer)
#@+node:AGP.20250415230112.1516:sanitize_filename
def sanitize_filename(s):

    """Prepares string s to be a valid file name:
    
    - substitute '_' whitespace and characters used special path characters.
    - eliminate all other non-alphabetic characters.
    - strip leading and trailing whitespace.
    - return at most 128 characters."""

    result = ""
    for ch in s.strip():
        if ch in string.ascii_letters:
            result += ch
        elif ch in string.whitespace: # Translate whitespace.
            result += '_'
        elif ch in ('.','\\','/',':'): # Translate special path characters.
            result += '_'
    while 1:
        n = len(result)
        result = result.replace('__','_')
        if len(result) == n:
            break
    result = result.strip()
    return result [:128]
#@-node:AGP.20250415230112.1516:sanitize_filename
#@+node:AGP.20250415230112.1517:setGlobalOpenDir
def setGlobalOpenDir (fileName):
    
    if fileName:
        g.app.globalOpenDir = g.os_path_dirname(fileName)
        # g.es('current directory: %s' %  g.app.globalOpenDir)
#@-node:AGP.20250415230112.1517:setGlobalOpenDir
#@+node:AGP.20250415230112.1518:shortFileName & shortFilename
def shortFileName (fileName):
    
    return g.os_path_basename(fileName)
    
shortFilename = shortFileName
#@-node:AGP.20250415230112.1518:shortFileName & shortFilename
#@-node:AGP.20250415230112.1498:Files & Directories...
#@+node:AGP.20250415230112.1519:Garbage Collection
# debugGC = False # Must be true to enable traces below.

lastObjectCount = 0
lastObjectsDict = {}
lastTypesDict = {}
lastFunctionsDict = {}

#@+others
#@+node:AGP.20250415230112.1520:enable_gc_debug
def enable_gc_debug(event=None):
    
    if g.app.trace_gc_inited:
        return
    
    if gc:
        if g.app.trace_gc_verbose:
            gc.set_debug(
                gc.DEBUG_STATS | # prints statistics.
                gc.DEBUG_LEAK | # Same as all below.
                gc.DEBUG_COLLECTABLE |
                gc.DEBUG_UNCOLLECTABLE |
                gc.DEBUG_INSTANCES |
                gc.DEBUG_OBJECTS |
                gc.DEBUG_SAVEALL
            )
            g.es('enabled verbose gc stats',color='blue')
        else:
            gc.set_debug(gc.DEBUG_STATS)
            g.es('enabled brief gc stats',color='blue')
    else:
        g.es('Can not import gc module',color='blue')
#@-node:AGP.20250415230112.1520:enable_gc_debug
#@+node:AGP.20250415230112.1521:clearAllIvars
def clearAllIvars (o):
    
    """Clear all ivars of o, a member of some class."""
    
    o.__dict__.clear()
#@-node:AGP.20250415230112.1521:clearAllIvars
#@+node:AGP.20250415230112.1522:Called from commands
#@+node:AGP.20250415230112.1523:collectGarbage
def collectGarbage():

    try:
        if not g.app.trace_gc_inited and g.app.trace_gc_verbose:
            g.enable_gc_debug()

        if g.app.trace_gc_verbose or g.app.trace_gc_calls:
            g.es_print('Collecting garbage')

        gc.collect()
    except:
        pass
        
    # Only init once, regardless of what happens.
    g.app.trace_gc_inited = True
#@-node:AGP.20250415230112.1523:collectGarbage
#@+node:AGP.20250415230112.1524:printGcSummary
def printGcSummary (message='',trace=False):
    
    if not message:
        message = g._callerName(n=2)

    g.enable_gc_debug()

    try:
        n = len(gc.garbage)
        n2 = len(gc.get_objects())
        s = 'garbage: %d, objects: %d, %s' % (n,n2,message)
        if trace:
            print s
        else:
            g.es_print(s)
    except:
        traceback.print_exc()
#@-node:AGP.20250415230112.1524:printGcSummary
#@+node:AGP.20250415230112.1525:printGcAll
def printGcAll (message=''):
    
    if not message:
        message = g._callerName(n=2)
    
    d = {} ; objects = gc.get_objects()
    g.es_print('-' * 30)
    g.es_print('%d objects' % len(objects),message)

    for obj in objects:
        t = type(obj)
        if t == 'instance':
            try: t = obj.__class__
            except: pass
        d[t] = d.get(t,0) + 1
        
    if 1: # Sort by n
        items = d.items()
        try:
            # Support for keword args to sort function exists in Python 2.4.
            # Support for None as an alternative to omitting cmp exists in Python 2.3.
            items.sort(key=lambda x: x[1],reverse=True)
        except: pass
        for z in items:
            g.es_print('%40s %7d' % (z[0],z[1]))
    else: # Sort by type
        keys = d.keys() ; keys.sort()
        for t in keys:
            g.es_print('%40s %7d' % (t,d.get(t)))
#@-node:AGP.20250415230112.1525:printGcAll
#@+node:AGP.20250415230112.1526:printGcObjects
def printGcObjects(message=''):
    
    if not message:
        message = g._callerName(n=2)

    global lastObjectCount

    try:
        n = len(gc.garbage)
        n2 = len(gc.get_objects())
        delta = n2-lastObjectCount
        lastObjectCount = n2

        g.es_print('-' * 30)
        g.es_print("garbage: %d, objects: %d, delta: %d %s" % (n,n2,delta,message))
        
        #@        << print number of each type of object >>
        #@+node:AGP.20250415230112.1527:<< print number of each type of object >>
        global lastTypesDict
        typesDict = {}
        
        for obj in gc.get_objects():
            n = typesDict.get(type(obj),0)
            t = type(obj)
            if t == 'instance':
                try: t = obj.__class__
                except: pass
            typesDict[t] = n + 1
            
        # Create the union of all the keys.
        keys = typesDict.keys()
        for key in lastTypesDict.keys():
            if key not in keys:
                keys.append(key)
        
        keys.sort()
        for key in keys:
            n1 = lastTypesDict.get(key,0)
            n2 = typesDict.get(key,0)
            delta2 = n2-n1
            if delta2 != 0:
                g.es_print("%+6d =%7d %s" % (delta2,n2,key))
            
        lastTypesDict = typesDict
        typesDict = {}
        #@-node:AGP.20250415230112.1527:<< print number of each type of object >>
        #@nl
        if 0:
            #@            << print added functions >>
            #@+node:AGP.20250415230112.1528:<< print added functions >>
            import types
            import inspect
            
            global lastFunctionsDict
            
            funcDict = {}
            
            for obj in gc.get_objects():
                if type(obj) == types.FunctionType:
                    key = repr(obj) # Don't create a pointer to the object!
                    funcDict[key]=None 
                    if not lastFunctionsDict.has_key(key):
                        g.es_print(obj)
                        args, varargs, varkw,defaults  = inspect.getargspec(obj)
                        g.es_print("args", args)
                        if varargs: g.es_print("varargs",varargs)
                        if varkw: g.es_print("varkw",varkw)
                        if defaults:
                            g.es_print("defaults...")
                            for s in defaults: g.es_print(s)
            
            lastFunctionsDict = funcDict
            funcDict = {}
            #@-node:AGP.20250415230112.1528:<< print added functions >>
            #@nl

    except:
        traceback.print_exc()
#@-node:AGP.20250415230112.1526:printGcObjects
#@+node:AGP.20250415230112.1529:printGcVerbose
# WARNING: the id trick is not proper because newly allocated objects
#          can have the same address as old objets.

def printGcVerbose(message=''):
    
    if not message:
        message = g._callerName(n=2)

    global lastObjectsDict
    objects = gc.get_objects()
    
    newObjects = [o for o in objects if not lastObjectsDict.has_key(id(o))]
    
    lastObjectsDict = {}
    for o in objects:
        lastObjectsDict[id(o)]=o
        
    dicts = 0 ; seqs = 0
    
    i = 0 ; n = len(newObjects)
    while i < 100 and i < n:
        o = newObjects[i]
        if type(o) == type({}): dicts += 1
        elif type(o) in (type(()),type([])):
            seqs += 1
        else:
            g.es_print(o)
        i += 1
    g.es_print('-' * 40)
    g.es_print('dicts: %d, sequences: %d' % (dicts,seqs))
    g.es_print("%25s: %d new, %d total objects" % (message,len(newObjects),len(objects)))
#@-node:AGP.20250415230112.1529:printGcVerbose
#@-node:AGP.20250415230112.1522:Called from commands
#@+node:AGP.20250415230112.1530:Called from unit tests
#@+node:AGP.20250415230112.1531:printGc
def printGc(message=None):
    
    if not g.app.trace_gc: return None
    
    if not message:
        message = g._callerName(n=2)
        
    printGcObjects(message)
    printGcRefs(message)
    
    if g.app.trace_gc_verbose:
        printGcVerbose(message)
#@+node:AGP.20250415230112.1532:printGcRefs
def printGcRefs (message=''):

    refs = gc.get_referrers(app.windowList[0])
    g.es_print('-' * 30,message)

    if g.app.trace_gc_verbose:
        g.es_print("refs of", app.windowList[0])
        for ref in refs:
            g.es_print(type(ref))
    else:
        g.es_print("%d referers" % len(refs))
#@-node:AGP.20250415230112.1532:printGcRefs
#@-node:AGP.20250415230112.1531:printGc
#@-node:AGP.20250415230112.1530:Called from unit tests
#@-others
#@-node:AGP.20250415230112.1519:Garbage Collection
#@+node:AGP.20250415230112.1533:Hooks & plugins (leoGlobals)
#@+node:AGP.20250415230112.1534:idle time functions (leoGlobals)
#@+node:AGP.20250415230112.1535:enableIdleTimeHook
#@+at 
#@nonl
# Enables the "idle" hook.
# After enableIdleTimeHook is called, Leo will call the "idle" hook
# approximately every g.idleTimeDelay milliseconds.
#@-at
#@@c

def enableIdleTimeHook(idleTimeDelay=100):

    if not g.app.idleTimeHook:
        # g.trace('start idle-time hook: %d msec.' % idleTimeDelay)
        # Start idle-time processing only after the first idle-time event.
        g.app.gui.setIdleTimeHook(g.idleTimeHookHandler)
        g.app.afterHandler = g.idleTimeHookHandler
        
    # 1/4/05: Always update these.
    g.app.idleTimeHook = True
    g.app.idleTimeDelay = idleTimeDelay # Delay in msec.
#@-node:AGP.20250415230112.1535:enableIdleTimeHook
#@+node:AGP.20250415230112.1536:disableIdleTimeHook
# Disables the "idle" hook.
def disableIdleTimeHook():
    
    g.app.idleTimeHook = False
#@-node:AGP.20250415230112.1536:disableIdleTimeHook
#@+node:AGP.20250415230112.1537:idleTimeHookHandler
# An internal routine used to dispatch the "idle" hook.
trace_count = 0

def idleTimeHookHandler(*args,**keys):

    # New for Python 2.3: may be called during shutdown.
    if g.app.killed: return
    
    for w in g.app.windowList:
        c = w.c
        # Do NOT compute c.currentPosition.
        # This would be a MAJOR leak of positions.
        g.doHook("idle",c=c)

    # Requeue this routine after g.app.idleTimeDelay msec.
    # (This delay is set by g.enableIdleTimeHook.)
    # Faster requeues overload the system.
    if g.app.idleTimeHook:
        g.app.gui.setIdleTimeHookAfterDelay(g.idleTimeHookHandler)
        g.app.afterHandler = g.idleTimeHookHandler
    else:
        g.app.afterHandler = None
#@-node:AGP.20250415230112.1537:idleTimeHookHandler
#@-node:AGP.20250415230112.1534:idle time functions (leoGlobals)
#@+node:AGP.20250415230112.1538:g.doHook
#@+at 
#@nonl
# This global function calls a hook routine.  Hooks are identified by the tag 
# param.
# Returns the value returned by the hook routine, or None if the there is an 
# exception.
# 
# We look for a hook routine in three places:
# 1. c.hookFunction
# 2. app.hookFunction
# 3. leoPlugins.doPlugins()
# We set app.hookError on all exceptions.  Scripts may reset app.hookError to 
# try again.
#@-at
#@@c

def doHook(tag,*args,**keywords):
    #print "doHook1"
    if g.app.killed or g.app.hookError or (g.app.gui and g.app.gui.isNullGui):
        return None
        
    if args:
        # A minor error in Leo's core.
        print "***ignoring args param.  tag = %s" % tag

    if not g.app.config.use_plugins:
        if tag == "start1":
            s = "Plugins disabled: use_plugins is 0 in a leoSettings.leo file."
            g.es_print(s,color="blue")
        return None
         
    # Get the hook handler function.  Usually this is doPlugins.
    #print "doHook2",tag
    leo.do_hooks(tag,keywords)
    
    
    
    
    c = keywords.get("c")
    f = (c and c.hookFunction) or g.app.hookFunction
    if not f:
        import leoPlugins
        g.app.hookFunction = f = leoPlugins.doPlugins
        
    try:
        # Pass the hook to the hook handler.
        # print 'doHook',f.__name__,keywords.get('c')
        #print "g.doHook():",tag,f
        return f(tag,keywords)
    except Exception:
        g.es_exception()
        g.app.hookError = True # Supress this function.
        g.app.idleTimeHook = False # Supress idle-time hook
        return None # No return value
#@-node:AGP.20250415230112.1538:g.doHook
#@+node:AGP.20250415230112.1539:g.plugin_signon
def plugin_signon(module_name,verbose=False):
    
    # The things we do to keep pychecker happy... 
    m = g.Bunch(__name__='',__version__='')
    
    exec("import %s ; m = %s" % (module_name,module_name))
    
    if verbose: # or g.app.unitTesting:
        g.es("...%s.py v%s: %s" % (
            m.__name__, m.__version__, g.plugin_date(m)))

        print m.__name__, m.__version__
        
    app.loadedPlugins.append(module_name)
#@-node:AGP.20250415230112.1539:g.plugin_signon
#@-node:AGP.20250415230112.1533:Hooks & plugins (leoGlobals)
#@+node:AGP.20250415230112.1540:Most common functions...
# These are guaranteed always to exist for scripts.
#@+node:AGP.20250415230112.1541:app & leoProxy (no longer used)
if 0: # No longer needed with the new import scheme.

    class leoProxy:
    
        """A proxy for the gApp object that can be created before gApp itself.
        
        After gApp is created, both app.x and app().x refer to gApp.x."""
    
        def __getattr__(self,attr):
            return getattr(gApp,attr)
            
        def __setattr__(self,attr,val):
            setattr(gApp,attr,val)
    
        def __call__(self):
            return gApp
            
    # The code can use app.x and app().x to refer to ivars of the leoApp class.
    app = leoProxy()
#@-node:AGP.20250415230112.1541:app & leoProxy (no longer used)
#@+node:AGP.20250415230112.1542:choose
def choose(cond, a, b): # warning: evaluates all arguments

    if cond: return a
    else: return b
#@-node:AGP.20250415230112.1542:choose
#@+node:AGP.20250415230112.1543:es, enl, ecnl
def ecnl(tabName='Log'):
    g.ecnls(1,tabName)

def ecnls(n,tabName='Log'):
    log = app.log
    if log and not log.isNull:
        while log.newlines < n:
            g.enl(tabName)

def enl(tabName='Log'):
    log = app.log
    if log and not log.isNull:
        log.newlines += 1
        log.putnl(tabName)

def es(s,*args,**keys):
    if app.killed:
        return
    newline = keys.get("newline",True)
    color = keys.get('color')
    tabName = keys.get('tabName','Log')
        # Default goes to log pane *Not* the presently active pane.
    if color == 'suppress': return # New in 4.3.
    if type(s) != type("") and type(s) != type(u""): # 1/20/03
        s = repr(s)
    for arg in args:
        if type(arg) != type("") and type(arg) != type(u""): # 1/20/03
            arg = repr(arg)
        s = s + ", " + arg
    if app.batchMode:
        if app.log:
            app.log.put(s)
    else:
        log = app.log
        if log and not log.isNull:
            # print 'g.es',s
            log.put(s,color=color,tabName=tabName)
            for ch in s:
                if ch == '\n': log.newlines += 1
                else: log.newlines = 0
            if newline:
                g.ecnl(tabName=tabName) # only valid here
        elif newline:
            app.logWaiting.append((s+'\n',color),)
            # print s
        else:
            app.logWaiting.append((s,color),)
            # print s,
#@-node:AGP.20250415230112.1543:es, enl, ecnl
#@+node:AGP.20250415230112.1544:es_print & test
def es_print(s,*args,**keys):
    
    print g.toEncodedString(s,'ascii')
    g.es(s,*args,**keys)
    
def test_g_es_print():
    
    g.es_print('\ntest of es_print: Ă',color='red')
#@-node:AGP.20250415230112.1544:es_print & test
#@+node:AGP.20250415230112.1545:es_trace & test
def es_trace(s,*args,**keys):
    
    g.trace(g.toEncodedString(s,'ascii'))
    g.es(s,*args,**keys)
    
def test_g_es_trace():
    
    g.es_trace('\ntest of es_trace: Ă',color='red')
#@-node:AGP.20250415230112.1545:es_trace & test
#@+node:AGP.20250415230112.1546:et, et_* and _ (underscore)
if 1: # Do nothing
    et = es
    et_print = es_print
    es_trace = es_trace
    def _(s): return s
else: # Use the gettext module to translate arguments.
    def et (s):
        es(_(s))
        
    def et_trace(s):
        es_trace(_(s))

    def et_trace(s):
        es_trace(_(s))

    def _ (s):
        '''Return the translated text of s.'''
        return gettext.gettext(s)
#@-node:AGP.20250415230112.1546:et, et_* and _ (underscore)
#@+node:AGP.20250415230112.1547:top
if 0: # An extremely dangerous function.

    def top():
        
        """Return the commander of the topmost window"""
        
        # Warning: may be called during startup or shutdown when nothing exists.
        try:
            return app.log.c
        except:
            return None
#@-node:AGP.20250415230112.1547:top
#@+node:AGP.20250415230112.1548:trace is defined below
#@-node:AGP.20250415230112.1548:trace is defined below
#@+node:AGP.20250415230112.1549:windows
def windows():
    return app.windowList
#@-node:AGP.20250415230112.1549:windows
#@-node:AGP.20250415230112.1540:Most common functions...
#@+node:AGP.20250415230112.1550:os.path wrappers (leoGlobals.py)
#@+at 
#@nonl
# Note: all these methods return Unicode strings. It is up to the user to
# convert to an encoded string as needed, say when opening a file.
#@-at
#@+node:AGP.20250415230112.1551:os_path_abspath
def os_path_abspath(path,encoding=None):
    
    """Convert a path to an absolute path."""

    path = g.toUnicodeFileEncoding(path,encoding)

    path = os.path.abspath(path)
    
    path = g.toUnicodeFileEncoding(path,encoding)
    
    return path
#@-node:AGP.20250415230112.1551:os_path_abspath
#@+node:AGP.20250415230112.1552:os_path_basename
def os_path_basename(path,encoding=None):
    
    """Return the second half of the pair returned by split(path)."""

    path = g.toUnicodeFileEncoding(path,encoding)

    path = os.path.basename(path)
    
    path = g.toUnicodeFileEncoding(path,encoding)
    
    return path
#@-node:AGP.20250415230112.1552:os_path_basename
#@+node:AGP.20250415230112.1553:os_path_dirname
def os_path_dirname(path,encoding=None):
    
    """Return the first half of the pair returned by split(path)."""
    
    path = g.toUnicodeFileEncoding(path,encoding)
    
    path = os.path.dirname(path)
    
    path = g.toUnicodeFileEncoding(path,encoding)
    
    return path
#@-node:AGP.20250415230112.1553:os_path_dirname
#@+node:AGP.20250415230112.1554:os_path_exists
def os_path_exists(path,encoding=None):
    
    """Normalize the path and convert it to an absolute path."""

    path = g.toUnicodeFileEncoding(path,encoding)

    return os.path.exists(path)
#@-node:AGP.20250415230112.1554:os_path_exists
#@+node:AGP.20250415230112.1555:os_path_getmtime
def os_path_getmtime(path,encoding=None):
    
    """Normalize the path and convert it to an absolute path."""

    path = g.toUnicodeFileEncoding(path,encoding)

    return os.path.getmtime(path)
#@-node:AGP.20250415230112.1555:os_path_getmtime
#@+node:AGP.20250415230112.1556:os_path_isabs
def os_path_isabs(path,encoding=None):
    
    """Normalize the path and convert it to an absolute path."""

    path = g.toUnicodeFileEncoding(path,encoding)

    return os.path.isabs(path)
#@-node:AGP.20250415230112.1556:os_path_isabs
#@+node:AGP.20250415230112.1557:os_path_isdir
def os_path_isdir(path,encoding=None):
    
    """Normalize the path and convert it to an absolute path."""

    path = g.toUnicodeFileEncoding(path,encoding)

    return os.path.isdir(path)
#@-node:AGP.20250415230112.1557:os_path_isdir
#@+node:AGP.20250415230112.1558:os_path_isfile
def os_path_isfile(path,encoding=None):
    
    """Normalize the path and convert it to an absolute path."""

    path = g.toUnicodeFileEncoding(path,encoding)

    return os.path.isfile(path)
#@-node:AGP.20250415230112.1558:os_path_isfile
#@+node:AGP.20250415230112.1559:os_path_join
def os_path_join(*args,**keys):
    
    encoding = keys.get("encoding")

    uargs = [g.toUnicodeFileEncoding(arg,encoding) for arg in args]
    
    # Note:  This is exactly the same convention as used by getBaseDirectory.
    if uargs and uargs[0] == '!!':
        uargs[0] = g.app.loadDir
    elif uargs and uargs[0] == '.':
        c = keys.get('c')
        if c and c.openDirectory:
            uargs[0] = c.openDirectory
            # g.trace(c.openDirectory)

    path = os.path.join(*uargs)
    # May not be needed on some Pythons.
    path = g.toUnicodeFileEncoding(path,encoding)
    return path
#@-node:AGP.20250415230112.1559:os_path_join
#@+node:AGP.20250415230112.1560:os_path_norm NOT USED
if 0:  # A bad idea.
    
    def os_path_norm(path,encoding=None):
    
        """Normalize both the path and the case."""
    
        path = g.toUnicodeFileEncoding(path,encoding)
    
        path = os.path.normcase(path)
        path = os.path.normpath(path)
        
        path = g.toUnicodeFileEncoding(path,encoding)
        
        return path
#@-node:AGP.20250415230112.1560:os_path_norm NOT USED
#@+node:AGP.20250415230112.1561:os_path_normabs NOT USED
if 0: # A bad idea.

    def os_path_normabs (path,encoding=None):
    
        """Convert the file name to a fully normalized absolute path.
        
        There is no exact analog to this in os.path"""
        
        path = g.os_path_abspath(path,encoding = encoding)
        path = g.os_path_norm(path,encoding = encoding)
    
        return path
#@-node:AGP.20250415230112.1561:os_path_normabs NOT USED
#@+node:AGP.20250415230112.1562:os_path_normcase
def os_path_normcase(path,encoding=None):
    
    """Normalize the path's case."""

    path = g.toUnicodeFileEncoding(path,encoding)

    path = os.path.normcase(path)
    
    path = g.toUnicodeFileEncoding(path,encoding)
    
    return path
#@-node:AGP.20250415230112.1562:os_path_normcase
#@+node:AGP.20250415230112.1563:os_path_normpath
def os_path_normpath(path,encoding=None):
    
    """Normalize the path."""

    path = g.toUnicodeFileEncoding(path,encoding)

    path = os.path.normpath(path)
    
    path = g.toUnicodeFileEncoding(path,encoding)
    
    return path
#@-node:AGP.20250415230112.1563:os_path_normpath
#@+node:AGP.20250415230112.1564:os_path_split
def os_path_split(path,encoding=None):
    
    path = g.toUnicodeFileEncoding(path,encoding)

    head,tail = os.path.split(path)

    head = g.toUnicodeFileEncoding(head,encoding)
    tail = g.toUnicodeFileEncoding(tail,encoding)

    return head,tail
#@-node:AGP.20250415230112.1564:os_path_split
#@+node:AGP.20250415230112.1565:os_path_splitext
def os_path_splitext(path,encoding=None):

    path = g.toUnicodeFileEncoding(path,encoding)

    head,tail = os.path.splitext(path)

    head = g.toUnicodeFileEncoding(head,encoding)
    tail = g.toUnicodeFileEncoding(tail,encoding)

    return head,tail
#@-node:AGP.20250415230112.1565:os_path_splitext
#@+node:AGP.20250415230112.1566:toUnicodeFileEncoding
def toUnicodeFileEncoding(path,encoding):

    if not encoding:
        if sys.platform == "win32":
            # encoding = "mbcs" # Leo 4.2 and previous.
            encoding = 'utf-8' # New in Leo 4.3
        else:
            encoding = app.tkEncoding

    # Yes, this is correct.  All os_path_x functions return Unicode strings.
    return g.toUnicode(path,encoding)
#@-node:AGP.20250415230112.1566:toUnicodeFileEncoding
#@-node:AGP.20250415230112.1550:os.path wrappers (leoGlobals.py)
#@+node:AGP.20250415230112.1567:Scanning... (leoGlobals.py)
#@+node:AGP.20250415230112.1568:g.scanAtFileOptions (used in 3.x read code)
def scanAtFileOptions (h,err_flag=False):
    
    assert(g.match(h,0,"@file"))
    i = len("@file")
    atFileType = "@file"
    optionsList = []

    while g.match(h,i,'-'):
        #@        << scan another @file option >>
        #@+node:AGP.20250415230112.1569:<< scan another @file option >>
        i += 1 ; err = -1
        
        if g.match_word(h,i,"asis"):
            if atFileType == "@file":
                atFileType = "@silentfile"
            elif err_flag:
                g.es("using -asis option in:" + h)
        elif g.match(h,i,"noref"): # Just match the prefix.
            if atFileType == "@file":
                atFileType = "@rawfile"
            elif atFileType == "@nosentinelsfile":
                atFileType = "@silentfile"
            elif err_flag:
                g.es("ignoring redundant -noref in:" + h)
        elif g.match(h,i,"nosent"): # Just match the prefix.,"@write"
            if atFileType == "@file":
                atFileType = "@nosentinelsfile"
            elif atFileType == "@rawfile":
                atFileType = "@silentfile"
            elif err_flag:
                g.es("ignoring redundant -nosent in:" + h)
        elif g.match_word(h,i,"thin"):
            if atFileType == "@file":
                atFileType = "@thinfile"
            elif err_flag:
                g.es("using -thin option in:" + h)
        else:
            if 0: # doesn't work
                for option in ("fat","new","now","old","thin","wait"):
                    if g.match_word(h,i,option):
                        optionsList.append(option)
                if len(option) == 0:
                    err = i-1
        # Scan to the next minus sign.
        while i < len(h) and h[i] not in (' ','\t','-'):
            i += 1
        if err > -1:
            g.es("unknown option:" + h[err:i] + " in " + h)
        #@-node:AGP.20250415230112.1569:<< scan another @file option >>
        #@nl
        
    # Convert atFileType to a list of options.
    for fileType,option in (
        ("@silentfile","asis"),
        ("@nosentinelsfile","nosent"),
        ("@rawfile","noref"),
        ("@thinfile","thin")
    ):
        if atFileType == fileType and option not in optionsList:
            optionsList.append(option)
            
    # g.trace(atFileType,optionsList)

    return i,atFileType,optionsList
#@-node:AGP.20250415230112.1568:g.scanAtFileOptions (used in 3.x read code)
#@+node:AGP.20250415230112.1570:scanAtRootOptions
def scanAtRootOptions (s,i,err_flag=False):
    
    assert(g.match(s,i,"@root"))
    i += len("@root")
    mode = None 
    while g.match(s,i,'-'):
        #@        << scan another @root option >>
        #@+node:AGP.20250415230112.1571:<< scan another @root option >>
        i += 1 ; err = -1
        
        if g.match_word(s,i,"code"): # Just match the prefix.
            if not mode: mode = "code"
            elif err_flag: g.es("modes conflict in:" + g.get_line(s,i))
        elif g.match(s,i,"doc"): # Just match the prefix.
            if not mode: mode = "doc"
            elif err_flag: g.es("modes conflict in:" + g.get_line(s,i))
        else:
            err = i-1
            
        # Scan to the next minus sign.
        while i < len(s) and s[i] not in (' ','\t','-'):
            i += 1
        
        if err > -1 and err_flag:
            g.es("unknown option:" + s[err:i] + " in " + g.get_line(s,i))
        #@-node:AGP.20250415230112.1571:<< scan another @root option >>
        #@nl

    if mode == None:
        doc = app.config.at_root_bodies_start_in_doc_mode
        mode = g.choose(doc,"doc","code")
    return i,mode
#@-node:AGP.20250415230112.1570:scanAtRootOptions
#@+node:AGP.20250415230112.1572:scanError
# It is dubious to bump the Tangle error count here, but it really doesn't hurt.

def scanError(s):

    """Bump the error count in the tangle command."""
    
    # New in Leo 4.4b1: just set this global.
    g.app.scanErrors +=1
    g.es(s)
#@-node:AGP.20250415230112.1572:scanError
#@+node:AGP.20250415230112.1573:scanf
# A quick and dirty sscanf.  Understands only %s and %d.

def scanf (s,pat):
    count = pat.count("%s") + pat.count("%d")
    pat = pat.replace("%s","(\S+)")
    pat = pat.replace("%d","(\d+)")
    parts = re.split(pat,s)
    result = []
    for part in parts:
        if len(part) > 0 and len(result) < count:
            result.append(part)
    # g.trace("scanf returns:",result)
    return result
    
if 0: # testing
    g.scanf("1.0","%d.%d",)
#@-node:AGP.20250415230112.1573:scanf
#@+node:AGP.20250415230112.1574:Scanners: calling scanError
#@+at 
#@nonl
# These scanners all call g.scanError() directly or indirectly, so they will 
# call g.es() if they find an error.  g.scanError() also bumps 
# c.tangleCommands.errors, which is harmless if we aren't tangling, and useful 
# if we are.
# 
# These routines are called by the Import routines and the Tangle routines.
#@-at
#@+node:AGP.20250415230112.1575:skip_block_comment
# Scans past a block comment (an old_style C comment).

def skip_block_comment (s,i):

    assert(g.match(s,i,"/*"))
    j = i ; i += 2 ; n = len(s)
    
    k = string.find(s,"*/",i)
    if k == -1:
        g.scanError("Run on block comment: " + s[j:i])
        return n
    else: return k + 2
#@-node:AGP.20250415230112.1575:skip_block_comment
#@+node:AGP.20250415230112.1576:skip_braces
#@+at 
#@nonl
# This code is called only from the import logic, so we are allowed to try 
# some tricks.  In particular, we assume all braces are matched in #if blocks.
#@-at
#@@c

def skip_braces(s,i):

    """Skips from the opening to the matching brace.
    
    If no matching is found i is set to len(s)"""

    # start = g.get_line(s,i)
    assert(g.match(s,i,'{'))
    level = 0 ; n = len(s)
    while i < n:
        c = s[i]
        if c == '{':
            level += 1 ; i += 1
        elif c == '}':
            level -= 1
            if level <= 0: return i
            i += 1
        elif c == '\'' or c == '"': i = g.skip_string(s,i)
        elif g.match(s,i,'//'): i = g.skip_to_end_of_line(s,i)
        elif g.match(s,i,'/*'): i = g.skip_block_comment(s,i)
        # 7/29/02: be more careful handling conditional code.
        elif g.match_word(s,i,"#if") or g.match_word(s,i,"#ifdef") or g.match_word(s,i,"#ifndef"):
            i,delta = g.skip_pp_if(s,i)
            level += delta
        else: i += 1
    return i
#@-node:AGP.20250415230112.1576:skip_braces
#@+node:AGP.20250415230112.1577:skip_php_braces (Dave Hein)
#@+at 
#@nonl
# 08-SEP-2002 DTHEIN: Added for PHP import support
# Skips from the opening to the matching . If no matching is found i is set to 
# len(s).
# 
# This code is called only from the import logic, and only for PHP imports.
#@-at
#@@c

def skip_php_braces(s,i):

    # start = g.get_line(s,i)
    assert(g.match(s,i,'{'))
    level = 0 ; n = len(s)
    while i < n:
        c = s[i]
        if c == '{':
            level += 1 ; i += 1
        elif c == '}':
            level -= 1
            if level <= 0: return i + 1
            i += 1
        elif c == '\'' or c == '"': i = g.skip_string(s,i)
        elif g.match(s,i,"<<<"): i = g.skip_heredoc_string(s,i)
        elif g.match(s,i,'//') or g.match(s,i,'#'): i = g.skip_to_end_of_line(s,i)
        elif g.match(s,i,'/*'): i = g.skip_block_comment(s,i)
        else: i += 1
    return i
#@-node:AGP.20250415230112.1577:skip_php_braces (Dave Hein)
#@+node:AGP.20250415230112.1578:skip_parens
def skip_parens(s,i):

    """Skips from the opening ( to the matching ).
    
    If no matching is found i is set to len(s)"""

    level = 0 ; n = len(s)
    assert(g.match(s,i,'('))
    while i < n:
        c = s[i]
        if c == '(':
            level += 1 ; i += 1
        elif c == ')':
            level -= 1
            if level <= 0:  return i
            i += 1
        elif c == '\'' or c == '"': i = g.skip_string(s,i)
        elif g.match(s,i,"//"): i = g.skip_to_end_of_line(s,i)
        elif g.match(s,i,"/*"): i = g.skip_block_comment(s,i)
        else: i += 1
    return i
#@-node:AGP.20250415230112.1578:skip_parens
#@+node:AGP.20250415230112.1579:skip_pascal_begin_end
def skip_pascal_begin_end(s,i):

    """Skips from begin to matching end.
    If found, i points to the end. Otherwise, i >= len(s)
    The end keyword matches begin, case, class, record, and try."""

    assert(g.match_c_word(s,i,"begin"))
    level = 1 ; i = g.skip_c_id(s,i) # Skip the opening begin.
    while i < len(s):
        ch = s[i]
        if ch =='{' : i = g.skip_pascal_braces(s,i)
        elif ch =='"' or ch == '\'': i = g.skip_pascal_string(s,i)
        elif g.match(s,i,"//"): i = g.skip_line(s,i)
        elif g.match(s,i,"(*"): i = g.skip_pascal_block_comment(s,i)
        elif g.match_c_word(s,i,"end"):
            level -= 1 ;
            if level == 0:
                # lines = s[i1:i+3] ; g.trace('\n' + lines + '\n')
                return i
            else: i = g.skip_c_id(s,i)
        elif g.is_c_id(ch):
            j = i ; i = g.skip_c_id(s,i) ; name = s[j:i]
            if name in ["begin", "case", "class", "record", "try"]:
                level += 1
        else: i += 1
    return i
#@-node:AGP.20250415230112.1579:skip_pascal_begin_end
#@+node:AGP.20250415230112.1580:skip_pascal_block_comment
# Scans past a pascal comment delimited by (* and *).

def skip_pascal_block_comment(s,i):
    
    j = i
    assert(g.match(s,i,"(*"))
    i = string.find(s,"*)",i)
    if i > -1: return i + 2
    else:
        g.scanError("Run on comment" + s[j:i])
        return len(s)

#   n = len(s)
#   while i < n:
#       if g.match(s,i,"*)"): return i + 2
#       i += 1
#   g.scanError("Run on comment" + s[j:i])
#   return i
#@-node:AGP.20250415230112.1580:skip_pascal_block_comment
#@+node:AGP.20250415230112.1581:skip_pascal_string : called by tangle
def skip_pascal_string(s,i):

    j = i ; delim = s[i] ; i += 1
    assert(delim == '"' or delim == '\'')

    while i < len(s):
        if s[i] == delim:
            return i + 1
        else: i += 1

    g.scanError("Run on string: " + s[j:i])
    return i
#@-node:AGP.20250415230112.1581:skip_pascal_string : called by tangle
#@+node:AGP.20250415230112.1582:skip_heredoc_string : called by php import (Dave Hein)
#@+at 
#@nonl
# 08-SEP-2002 DTHEIN:  added function skip_heredoc_string
# A heredoc string in PHP looks like:
# 
#   <<<EOS
#   This is my string.
#   It is mine. I own it.
#   No one else has it.
#   EOS
# 
# It begins with <<< plus a token (naming same as PHP variable names).
# It ends with the token on a line by itself (must start in first position.
# 
#@-at
#@@c
def skip_heredoc_string(s,i):
    
    j = i
    assert(g.match(s,i,"<<<"))
    m = re.match("\<\<\<([a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*)", s[i:])
    if (None == m):
        i += 3
        return i

    # 14-SEP-2002 DTHEIN: needed to add \n to find word, not just string
    delim = m.group(1) + '\n' 
    
    i = g.skip_line(s,i) # 14-SEP-2002 DTHEIN: look after \n, not before
    n = len(s)
    while i < n and not g.match(s,i,delim):
        i = g.skip_line(s,i) # 14-SEP-2002 DTHEIN: move past \n
        
    if i >= n:
        g.scanError("Run on string: " + s[j:i])
    elif g.match(s,i,delim):
        i += len(delim)
    return i
#@-node:AGP.20250415230112.1582:skip_heredoc_string : called by php import (Dave Hein)
#@+node:AGP.20250415230112.1583:skip_pp_directive
# Now handles continuation lines and block comments.

def skip_pp_directive(s,i):

    while i < len(s):
        if g.is_nl(s,i):
            if g.escaped(s,i): i = g.skip_nl(s,i)
            else: break
        elif g.match(s,i,"//"): i = g.skip_to_end_of_line(s,i)
        elif g.match(s,i,"/*"): i = g.skip_block_comment(s,i)
        else: i += 1
    return i
#@-node:AGP.20250415230112.1583:skip_pp_directive
#@+node:AGP.20250415230112.1584:skip_pp_if
# Skips an entire if or if def statement, including any nested statements.

def skip_pp_if(s,i):
    
    start_line = g.get_line(s,i) # used for error messages.
    # g.trace(start_line)

    assert(
        g.match_word(s,i,"#if") or
        g.match_word(s,i,"#ifdef") or
        g.match_word(s,i,"#ifndef"))

    i = g.skip_line(s,i)
    i,delta1 = g.skip_pp_part(s,i)
    i = g.skip_ws(s,i)
    if g.match_word(s,i,"#else"):
        i = g.skip_line(s,i)
        i = g.skip_ws(s,i)
        i,delta2 = g.skip_pp_part(s,i)
        if delta1 != delta2:
            g.es("#if and #else parts have different braces: " + start_line)
    i = g.skip_ws(s,i)
    if g.match_word(s,i,"#endif"):
        i = g.skip_line(s,i)
    else:
        g.es("no matching #endif: " + start_line)

    # g.trace(delta1,start_line)
    return i,delta1
#@-node:AGP.20250415230112.1584:skip_pp_if
#@+node:AGP.20250415230112.1585:skip_pp_part
# Skip to an #else or #endif.  The caller has eaten the #if, #ifdef, #ifndef or #else

def skip_pp_part(s,i):

    # g.trace(g.get_line(s,i))

    delta = 0
    while i < len(s):
        c = s[i]
        if 0:
            if c == '\n':
                g.trace(delta,g.get_line(s,i))
        if g.match_word(s,i,"#if") or g.match_word(s,i,"#ifdef") or g.match_word(s,i,"#ifndef"):
            i,delta1 = g.skip_pp_if(s,i)
            delta += delta1
        elif g.match_word(s,i,"#else") or g.match_word(s,i,"#endif"):
            return i,delta
        elif c == '\'' or c == '"': i = g.skip_string(s,i)
        elif c == '{':
            delta += 1 ; i += 1
        elif c == '}':
            delta -= 1 ; i += 1
        elif g.match(s,i,"//"): i = g.skip_line(s,i)
        elif g.match(s,i,"/*"): i = g.skip_block_comment(s,i)
        else: i += 1
    return i,delta
#@-node:AGP.20250415230112.1585:skip_pp_part
#@+node:AGP.20250415230112.1586:skip_python_string
def skip_python_string(s,i):

    if g.match(s,i,"'''") or g.match(s,i,'"""'):
        j = i ; delim = s[i]*3 ; i += 3
        k = string.find(s,delim,i)
        if k > -1: return k+3
        g.scanError("Run on triple quoted string: " + s[j:i])
        return len(s)
    else:
        return g.skip_string(s,i)
#@-node:AGP.20250415230112.1586:skip_python_string
#@+node:AGP.20250415230112.1587:skip_string
def skip_string(s,i,verbose=True):
    
    '''Scan forward to the end of a string.
    New in Leo 4.4.2 final: give error only if verbose is True'''
    
    j = i ; delim = s[i] ; i += 1
    assert(delim == '"' or delim == '\'')
    
    n = len(s)
    while i < n and s[i] != delim:
        if s[i] == '\\' : i += 2
        else: i += 1

    if i >= n:
        if verbose:
            g.scanError("Run on string: " + s[j:i])
    elif s[i] == delim:
        i += 1

    # g.trace(s[j:i])
    return i
#@-node:AGP.20250415230112.1587:skip_string
#@+node:AGP.20250415230112.1588:skip_to_semicolon
# Skips to the next semicolon that is not in a comment or a string.

def skip_to_semicolon(s,i):

    n = len(s)
    while i < n:
        c = s[i]
        if c == ';': return i
        elif c == '\'' or c == '"' : i = g.skip_string(s,i)
        elif g.match(s,i,"//"): i = g.skip_to_end_of_line(s,i)
        elif g.match(s,i,"/*"): i = g.skip_block_comment(s,i)
        else: i += 1
    return i
#@-node:AGP.20250415230112.1588:skip_to_semicolon
#@+node:AGP.20250415230112.1589:skip_typedef
def skip_typedef(s,i):

    n = len(s)
    while i < n and g.is_c_id(s[i]):
        i = g.skip_c_id(s,i)
        i = g.skip_ws_and_nl(s,i)
    if g.match(s,i,'{'):
        i = g.skip_braces(s,i)
        i = g.skip_to_semicolon(s,i)
    return i
#@-node:AGP.20250415230112.1589:skip_typedef
#@-node:AGP.20250415230112.1574:Scanners: calling scanError
#@+node:AGP.20250415230112.1590:Scanners: no error messages
#@+node:AGP.20250415230112.1591:escaped
# Returns True if s[i] is preceded by an odd number of backslashes.

def escaped(s,i):

    count = 0
    while i-1 >= 0 and s[i-1] == '\\':
        count += 1
        i -= 1
    return (count%2) == 1
#@-node:AGP.20250415230112.1591:escaped
#@+node:AGP.20250415230112.1592:find_line_start
def find_line_start(s,i):

    # bug fix: 11/2/02: change i to i+1 in rfind
    i = string.rfind(s,'\n',0,i+1) # Finds the highest index in the range.
    if i == -1: return 0
    else: return i + 1
#@-node:AGP.20250415230112.1592:find_line_start
#@+node:AGP.20250415230112.1593:find_on_line
def find_on_line(s,i,pattern):

    # j = g.skip_line(s,i) ; g.trace(s[i:j])
    j = string.find(s,'\n',i)
    if j == -1: j = len(s)
    k = string.find(s,pattern,i,j)
    if k > -1: return k
    else: return None
#@-node:AGP.20250415230112.1593:find_on_line
#@+node:AGP.20250415230112.1594:is_c_id
def is_c_id(ch):

    return g.isWordChar(ch)

#@-node:AGP.20250415230112.1594:is_c_id
#@+node:AGP.20250415230112.1595:is_nl
def is_nl(s,i):

    return i < len(s) and (s[i] == '\n' or s[i] == '\r')
#@-node:AGP.20250415230112.1595:is_nl
#@+node:AGP.20250415230112.1596:is_special
# We no longer require that the directive appear befor any @c directive or section definition.

def is_special(s,i,directive):

    """Return True if the body text contains the @ directive."""

    # j = g.skip_line(s,i) ; g.trace(s[i:j],':',directive)
    assert (directive and directive [0] == '@' )

    # 10/23/02: all directives except @others must start the line.
    skip_flag = directive in ("@others","@all")
    while i < len(s):
        if g.match_word(s,i,directive):
            return True, i
        else:
            i = g.skip_line(s,i)
            if skip_flag:
                i = g.skip_ws(s,i)
    return False, -1
#@-node:AGP.20250415230112.1596:is_special
#@+node:AGP.20250415230112.1597:is_ws & is_ws_or_nl
def is_ws(c):

    return c == '\t' or c == ' '
    
def is_ws_or_nl(s,i):

    return g.is_nl(s,i) or (i < len(s) and g.is_ws(s[i]))
#@-node:AGP.20250415230112.1597:is_ws & is_ws_or_nl
#@+node:AGP.20250415230112.1598:match
# Warning: this code makes no assumptions about what follows pattern.

def match(s,i,pattern):

    return s and pattern and string.find(s,pattern,i,i+len(pattern)) == i
#@-node:AGP.20250415230112.1598:match
#@+node:AGP.20250415230112.1599:match_c_word
def match_c_word (s,i,name):

    if name == None: return False
    n = len(name)
    if n == 0: return False
    return name == s[i:i+n] and (i+n == len(s) or not g.is_c_id(s[i+n]))
#@-node:AGP.20250415230112.1599:match_c_word
#@+node:AGP.20250415230112.1600:match_ignoring_case
def match_ignoring_case(s1,s2):

    if s1 == None or s2 == None: return False
    return string.lower(s1) == string.lower(s2)
#@-node:AGP.20250415230112.1600:match_ignoring_case
#@+node:AGP.20250415230112.1601:match_word
def match_word(s,i,pattern):

    if pattern == None: return False
    j = len(pattern)
    if j == 0: return False
    if s.find(pattern,i,i+j) != i:
        return False
    if i+j >= len(s):
        return True
    ch = s[i+j]
    return not g.isWordChar(ch)
#@-node:AGP.20250415230112.1601:match_word
#@+node:AGP.20250415230112.1602:skip_blank_lines
def skip_blank_lines(s,i):

    while i < len(s):
        if g.is_nl(s,i) :
            i = g.skip_nl(s,i)
        elif g.is_ws(s[i]):
            j = g.skip_ws(s,i)
            if g.is_nl(s,j):
                i = j
            else: break
        else: break
    return i
#@-node:AGP.20250415230112.1602:skip_blank_lines
#@+node:AGP.20250415230112.1603:skip_c_id
def skip_c_id(s,i):

    n = len(s)
    while i < n and g.isWordChar(s[i]):
        i += 1
    return i
#@-node:AGP.20250415230112.1603:skip_c_id
#@+node:AGP.20250415230112.1604:skip_id
def skip_id(s,i,chars=None):

    chars = chars and g.toUnicode(chars,encoding='ascii') or ''
    n = len(s)
    while i < n and (g.isWordChar(s[i]) or s[i] in chars):
        i += 1
    return i
#@nonl
#@-node:AGP.20250415230112.1604:skip_id
#@+node:AGP.20250415230112.1605:skip_line, skip_to_end_of_line
#@+at 
#@nonl
# These methods skip to the next newline, regardless of whether the newline 
# may be preceeded by a backslash. Consequently, they should be used only when 
# we know that we are not in a preprocessor directive or string.
#@-at
#@@c

def skip_line (s,i):

    i = string.find(s,'\n',i)
    if i == -1: return len(s)
    else: return i + 1
        
def skip_to_end_of_line (s,i):

    i = string.find(s,'\n',i)
    if i == -1: return len(s)
    else: return i
#@-node:AGP.20250415230112.1605:skip_line, skip_to_end_of_line
#@+node:AGP.20250415230112.1606:skip_long
def skip_long(s,i):
    
    """Scan s[i:] for a valid int.
    Return (i, val) or (i, None) if s[i] does not point at a number.
    """

    val = 0
    i = g.skip_ws(s,i)
    n = len(s)
    if i >= n or (not s[i].isdigit() and s[i] not in u'+-'):
        return i, None
    j = i
    if s[i] in u'+-': # Allow sign before the first digit
        i +=1
    while i < n and s[i].isdigit():
        i += 1
    try: # There may be no digits.
        val = int(s[j:i])
        return i, val
    except:
        return i,None
#@-node:AGP.20250415230112.1606:skip_long
#@+node:AGP.20250415230112.1607:skip_matching_python_delims
def skip_matching_python_delims(s,i,delim1,delim2,reverse=False):
    
    '''Skip from the opening delim to the matching delim2.
    
    Return the index of the matching ')', or -1'''
    
    level = 0 ; n = len(s)
    assert(g.match(s,i,delim1))
    if reverse:
         while i >= 0:
            ch = s[i]
            if ch == delim1:
                level += 1 ; i -= 1
            elif ch == delim2:
                level -= 1
                if level <= 0:  return i
                i -= 1
            # Doesn't handle strings and comments properly...
            else: i -= 1
    else:
        while i < n:
            progress = i
            ch = s[i]
            if ch == delim1:
                level += 1 ; i += 1
            elif ch == delim2:
                level -= 1
                if level <= 0:  return i
                i += 1
            elif ch == '\'' or ch == '"': i = g.skip_string(s,i,verbose=False)
            elif g.match(s,i,'#'):  i = g.skip_to_end_of_line(s,i)
            else: i += 1
            if i == progress: return -1
    return -1
#@-node:AGP.20250415230112.1607:skip_matching_python_delims
#@+node:AGP.20250415230112.1608:skip_matching_python_parens
def skip_matching_python_parens(s,i):

    '''Skip from the opening ( to the matching ).
    
    Return the index of the matching ')', or -1'''
    
    return skip_matching_python_delims(s,i,'(',')')
#@-node:AGP.20250415230112.1608:skip_matching_python_parens
#@+node:AGP.20250415230112.1609:skip_nl
# We need this function because different systems have different end-of-line conventions.

def skip_nl (s,i):

    """Skips a single "logical" end-of-line character."""

    if g.match(s,i,"\r\n"): return i + 2
    elif g.match(s,i,'\n') or g.match(s,i,'\r'): return i + 1
    else: return i
#@-node:AGP.20250415230112.1609:skip_nl
#@+node:AGP.20250415230112.1610:skip_non_ws
def skip_non_ws (s,i):

    n = len(s)
    while i < n and not g.is_ws(s[i]):
        i += 1
    return i
#@-node:AGP.20250415230112.1610:skip_non_ws
#@+node:AGP.20250415230112.1611:skip_pascal_braces
# Skips from the opening { to the matching }.

def skip_pascal_braces(s,i):

    # No constructs are recognized inside Pascal block comments!
    k = string.find(s,'}',i)
    if i == -1: return len(s)
    else: return k
#@-node:AGP.20250415230112.1611:skip_pascal_braces
#@+node:AGP.20250415230112.1612:skip_to_char
def skip_to_char(s,i,ch):
    
    j = string.find(s,ch,i)
    if j == -1:
        return len(s),s[i:]
    else:
        return j,s[i:j]
#@-node:AGP.20250415230112.1612:skip_to_char
#@+node:AGP.20250415230112.1613:skip_ws, skip_ws_and_nl
def skip_ws(s,i):

    n = len(s)
    while i < n and g.is_ws(s[i]):
        i += 1
    return i
    
def skip_ws_and_nl(s,i):

    n = len(s)
    while i < n and (g.is_ws(s[i]) or g.is_nl(s,i)):
        i += 1
    return i
#@-node:AGP.20250415230112.1613:skip_ws, skip_ws_and_nl
#@-node:AGP.20250415230112.1590:Scanners: no error messages
#@+node:AGP.20250415230112.1614:splitLines & joinLines
def splitLines (s):
    
    """Split s into lines, preserving the number of lines and the ending of the last line."""

    # g.stat()
    
    if s:
        return s.splitlines(True) # This is a Python string function!
    else:
        return []

splitlines = splitLines

def joinLines (aList):
    
    return ''.join(aList)
    
joinlines = joinLines
#@-node:AGP.20250415230112.1614:splitLines & joinLines
#@-node:AGP.20250415230112.1567:Scanning... (leoGlobals.py)
#@+node:AGP.20250415230112.1615:Script Tools (leoGlobals.py)
#@+node:AGP.20250415230112.1616:g.initScriptFind (set up dialog)
def initScriptFind(c,findHeadline,changeHeadline=None,firstNode=None,
    script_search=True,script_change=True):
        
    import leoTest
    import leoGlobals as g

    # Find the scripts.
    p = c.currentPosition()
    u = leoTest.testUtils(c)
    find_p = u.findNodeInTree(p,findHeadline)
    if find_p:
        find_text = find_p.bodyString()
    else:
        g.es("no Find script node",color="red")
        return
    if changeHeadline:
        change_p = u.findNodeInTree(p,changeHeadline)
    else:
        change_p = None
    if change_p:
        change_text = change_p.bodyString()
    else:
        change_text = ""
    # print find_p,change_p
    
    # Initialize the find panel.
    c.script_search_flag = script_search
    c.script_change_flag = script_change and change_text
    if script_search:
        c.find_text = find_text.strip() + "\n"
    else:
        c.find_text = find_text
    if script_change:
        c.change_text = change_text.strip() + "\n"
    else:
        c.change_text = change_text
    c.frame.findPanel.init(c)
    c.showFindPanel()
#@-node:AGP.20250415230112.1616:g.initScriptFind (set up dialog)
#@+node:AGP.20250415230112.1617:g.findNodeInTree, findNodeAnywhere, findTopLevelNode
def findNodeInTree(c,p,headline):

    """Search for a node in v's tree matching the given headline."""
    
    for p in p.subtree_iter():
        if p.headString().strip() == headline.strip():
            return p.copy()
    return c.nullPosition()

def findNodeAnywhere(c,headline):
    
    for p in c.allNodes_iter():
        if p.headString().strip() == headline.strip():
            return p.copy()
    return c.nullPosition()
    
def findTopLevelNode(c,headline):
    
    for p in c.rootPosition().self_and_siblings_iter():
        if p.headString().strip() == headline.strip():
            return p.copy()
    return c.nullPosition()
#@-node:AGP.20250415230112.1617:g.findNodeInTree, findNodeAnywhere, findTopLevelNode
#@+node:AGP.20250415230112.1618:g.handleScriptException
def handleScriptException (c,p,script,script1):

    g.es("exception executing script",color='blue')

    fileName, n = g.es_exception(full=False)

    if p and not script1 and fileName == "<string>":
        c.goToScriptLineNumber(p,script,n)

    #@    << dump the lines near the error >>
    #@+node:AGP.20250415230112.1619:<< dump the lines near the error >>
    if g.os_path_exists(fileName):
        f = file(fileName)
        lines = f.readlines()
        f.close()
    else:
        lines = g.splitLines(script)
    
    s = '-' * 20
    g.es_print(s)
    
    # Print surrounding lines.
    i = max(0,n-2)
    j = min(n+2,len(lines))
    while i < j:
        ch = g.choose(i==n-1,'*',' ')
        s = "%s line %d: %s" % (ch,i+1,lines[i])
        g.es(s,newline=False)
        i += 1
    #@-node:AGP.20250415230112.1619:<< dump the lines near the error >>
    #@nl
#@-node:AGP.20250415230112.1618:g.handleScriptException
#@+node:AGP.20250415230112.1620:g.executeFile
def executeFile(filename, options= ''):

    if not os.access(filename, os.R_OK): return

    subprocess = g.importExtension('subprocess',None,verbose=False)

    cwd = os.getcwdu()
    fdir, fname = g.os_path_split(filename)
    
    if subprocess: # Only exists in Python 2.4.
        #@        << define subprocess_wrapper >>
        #@+node:AGP.20250415230112.1621:<< define subprocess_wrapper >>
        def subprocess_wrapper(cmdlst):
            
            # g.trace(cmdlst, fdir)
            # g.trace(subprocess.list2cmdline([cmdlst]))
        
            p = subprocess.Popen(cmdlst, cwd=fdir,
                universal_newlines=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
            stdo, stde = p.communicate()
            return p.wait(), stdo, stde
        #@-node:AGP.20250415230112.1621:<< define subprocess_wrapper >>
        #@nl
        rc, so, se = subprocess_wrapper('%s %s %s'%(sys.executable, fname, options))
        if rc:
             print 'return code', rc
        print so, se
    else:
        if fdir: os.chdir(fdir)
        d = {'__name__': '__main__'}
        execfile(fname, d)  #, globals()
        os.system('%s %s' % (sys.executable, fname))
        if fdir: os.chdir(cwd)
#@-node:AGP.20250415230112.1620:g.executeFile
#@+node:AGP.20250415230112.1622:g.makeScriptButton
def makeScriptButton (c,
    p=None, # A node containing the script.
    script=None, # The script itself.
    buttonText=None,
    balloonText=None,#'Script Button',
    shortcut=None,#bg='LightSteelBlue1',
    define_g=True,define_name='__main__',silent=False, # Passed on to c.executeScript.
):
    
    '''Create a script button for the script in node p.
    The button's text defaults to p.headString'''

    k = c.k
    if p and not buttonText: buttonText = p.headString().strip()
    if not buttonText: buttonText = 'Unnamed Script Button'
    #@    << create the button b >>
    #@+node:AGP.20250415230112.1623:<< create the button b >>
    iconBar = c.frame.getIconBarObject()
    b = iconBar.add(text=buttonText)
    
    if sys.platform == "win32":
        width = int(len(buttonText) * 0.9)
        b.configure(width=width,font=('verdana',7,'bold'))
    #@-node:AGP.20250415230112.1623:<< create the button b >>
    #@nl
    #@    << define the callbacks for b >>
    #@+node:AGP.20250415230112.1624:<< define the callbacks for b >>
    def deleteButtonCallback(event=None,b=b,c=c):
        if b: b.pack_forget()
        c.frame.bodyWantsFocus()
        
    def executeScriptCallback (event=None,
        b=b,c=c,buttonText=buttonText,p=p and p.copy(),script=script):
    
        if c.disableCommandsMessage:
            g.es(c.disableCommandsMessage,color='blue')
        else:
            g.app.scriptDict = {}
            c.executeScript(p=p,script=script,
            define_g= define_g,define_name=define_name,silent=silent)
            # Remove the button if the script asks to be removed.
            if g.app.scriptDict.get('removeMe'):
                g.es("Removing '%s' button at its request" % buttonText)
                b.pack_forget()
        # Do not assume the script will want to remain in this commander.
    #@-node:AGP.20250415230112.1624:<< define the callbacks for b >>
    #@nl
    b.configure(command=executeScriptCallback)
    b.bind('<3>',deleteButtonCallback)
    if shortcut:
        #@        << bind the shortcut to executeScriptCallback >>
        #@+node:AGP.20250415230112.1625:<< bind the shortcut to executeScriptCallback >>
        func = executeScriptCallback
        shortcut = k.canonicalizeShortcut(shortcut)
        ok = k.bindKey ('button', shortcut,func,buttonText)
        if ok:
            g.es_print('Bound @button %s to %s' % (buttonText,shortcut),color='blue')
        #@-node:AGP.20250415230112.1625:<< bind the shortcut to executeScriptCallback >>
        #@nl
    #@    << create press-buttonText-button command >>
    #@+node:AGP.20250415230112.1626:<< create press-buttonText-button command >>
    aList = [g.choose(ch.isalnum(),ch,'-') for ch in buttonText]
    
    buttonCommandName = ''.join(aList)
    buttonCommandName = buttonCommandName.replace('--','-')
    buttonCommandName = 'press-%s-button' % buttonCommandName.lower()
    
    # This will use any shortcut defined in an @shortcuts node.
    k.registerCommand(buttonCommandName,None,executeScriptCallback,pane='button',verbose=False)
    #@-node:AGP.20250415230112.1626:<< create press-buttonText-button command >>
    #@nl
#@-node:AGP.20250415230112.1622:g.makeScriptButton
#@-node:AGP.20250415230112.1615:Script Tools (leoGlobals.py)
#@+node:AGP.20250415230112.1627:Unicode utils...
#@+node:AGP.20250415230112.1628:g.isWordChar & g.isWordChar1
def isWordChar (ch):
    
    '''Return True if ch should be considered a letter.'''

    return ch and (ch.isalnum() or ch == u'_')
    
def isWordChar1 (ch):
    
    return ch and (ch.isalpha() or ch == u'_')
#@nonl
#@-node:AGP.20250415230112.1628:g.isWordChar & g.isWordChar1
#@+node:AGP.20250415230112.1629:g.safeStringCompare & test (Do not use)
#@+at 
#@nonl
# Important: Leo is supposed to convert all characters to unicode,
# so there should never be a need for safeStringCompare.
# 
# The proper way to avoid UnicodeError's is to call 
# g.toUnicode(s,g.app.tkEncoding)
# 
#@-at
#@@c

if 0:
    def safeStringCompare (s1,s2):

        s1 = g.toUnicode(s1,'utf-8')
        s2 = g.toUnicode(s2,'utf-8')
        return s1 == s2
    
    def xxx_test_g_safeStringCompare ():
        
        assert g.safeStringCompare('a','á') is False
        assert g.safeStringCompare('','á') is False
        assert g.safeStringCompare('',u'á') is False
        assert g.safeStringCompare('a','a') is True
        assert g.safeStringCompare('á','á') is True
        assert g.safeStringCompare(u'á',u'á') is True
#@-node:AGP.20250415230112.1629:g.safeStringCompare & test (Do not use)
#@+node:AGP.20250415230112.1633:isUnicode
def isUnicode(s):
    
    return s is None or type(s) == type(u' ')
#@-node:AGP.20250415230112.1633:isUnicode
#@+node:AGP.20250415230112.1634:isValidEncoding
def isValidEncoding (encoding):
    
    if not encoding:
        return False

    import codecs

    try:
        codecs.lookup(encoding)
        return True
    except LookupError:
        return False
#@nonl
#@-node:AGP.20250415230112.1634:isValidEncoding
#@+node:AGP.20250415230112.1635:reportBadChars
def reportBadChars (s,encoding):
    
    errors = 0
    if type(s) == type(u""):
        for ch in s:
            try: ch.encode(encoding,"strict")
            except UnicodeEncodeError:
                errors += 1
        if errors:
            g.es("%d errors converting %s to %s" % (
                errors, s.encode(encoding,'replace'),
                encoding.encode('ascii','replace')),
            color='red')
    elif type(s) == type(""):
        for ch in s:
            try: unicode(ch,encoding,"strict")
            except: errors += 1
        if errors:
            g.es("%d errors converting %s (%s encoding) to unicode" % (
                errors,
                unicode(s,encoding,'replace'),
                encoding.encode('ascii','replace')),
            color='red')
#@+node:AGP.20250415230112.1636:test_g_reportBadChars
def test_g_reportBadChars ():
    
    for s,encoding in (
        ('aĂbĂ',  'ascii'),
        (u'aĂbĂ', 'ascii'),
        ('炰',    'ascii'),
        (u'炰',   'ascii'),
        
        ('aĂbĂ',  'utf-8'),
        (u'aĂbĂ', 'utf-8'),
        ('炰',    'utf-8'),
        (u'炰',   'utf-8'),
    ):
    
        g.reportBadChars(s,encoding)
#@-node:AGP.20250415230112.1636:test_g_reportBadChars
#@-node:AGP.20250415230112.1635:reportBadChars
#@+node:AGP.20250415230112.1637:toUnicode & toEncodedString (and tests)
#@+node:AGP.20250415230112.1638:toEncodedString
def toEncodedString (s,encoding,reportErrors=False):

    if type(s) == type(u""):
        try:
            s = s.encode(encoding,"strict")
        except UnicodeError:
            if reportErrors:
                g.reportBadChars(s,encoding)
            s = s.encode(encoding,"replace")
    return s
#@-node:AGP.20250415230112.1638:toEncodedString
#@+node:AGP.20250415230112.1639:toEncodedStringWithErrorCode
def toEncodedStringWithErrorCode (s,encoding):
    
    ok = True

    if type(s) == type(u""):
        try:
            s = s.encode(encoding,"strict")
        except UnicodeError:
            s = s.encode(encoding,"replace")
            ok = False

    return s,ok
#@-node:AGP.20250415230112.1639:toEncodedStringWithErrorCode
#@+node:AGP.20250415230112.1640:toUnicode
def toUnicode (s,encoding,reportErrors=False):
    
    if s is None:
        s = u""
    if type(s) == type(""):
        try:
            s = unicode(s,encoding,"strict")
        except UnicodeError:
            if reportErrors:
                g.reportBadChars(s,encoding)
            s = unicode(s,encoding,"replace")
    return s
#@-node:AGP.20250415230112.1640:toUnicode
#@+node:AGP.20250415230112.1641:toUnicodeWithErrorCode
def toUnicodeWithErrorCode (s,encoding):
    
    ok = True
    
    if s is None:
        s = u""
    if type(s) == type(""):
        try:
            s = unicode(s,encoding,"strict")
        except UnicodeError:
            s = unicode(s,encoding,"replace")
            ok = False

    return s,ok
#@-node:AGP.20250415230112.1641:toUnicodeWithErrorCode
#@+node:AGP.20250415230112.1642:test_round_trip_toUnicode_toEncodedString
def test_round_trip_toUnicode_toEncodedString ():
   
    for s,encoding in (
        ('a',    'utf-8'),
        ('a',    'ascii'),
        ('äöü',  'utf-8'),
        ('äöü',  'mbcs'),
        ('炰',   'utf-8'),
        ('炰',   'mbcs'),
    ):
        if g.isValidEncoding(encoding):
            s2,ok = g.toUnicodeWithErrorCode(s,encoding)
            assert ok, 'toUnicodeWithErrorCode fails for %s' %s
            s3,ok = g.toEncodedStringWithErrorCode(s2,encoding)
            assert ok, 'toEncodedStringWithErrorCode fails for %s' % s2
            assert s3 == s, 'Round-trip one failed for %s' %s
            
            s2 = g.toUnicode(s,encoding)
            s3 = g.toEncodedString(s2,encoding)
            assert s3 == s, 'Round-trip two failed for %s' %s
#@-node:AGP.20250415230112.1642:test_round_trip_toUnicode_toEncodedString
#@+node:AGP.20250415230112.1643:test_failure_with_ascii_encodings
def test_failure_with_ascii_encodings():

    encoding = 'ascii'
    
    s = '炰'
    s2,ok = g.toUnicodeWithErrorCode(s,encoding)
    assert not ok, 'toUnicodeWithErrorCode returns True for %s with ascii encoding' % s
    
    s = u'炰'
    s3,ok = g.toEncodedStringWithErrorCode(s,encoding)
    assert not ok, 'toEncodedStringWithErrorCode returns True for %s with ascii encoding' % s
#@-node:AGP.20250415230112.1643:test_failure_with_ascii_encodings
#@-node:AGP.20250415230112.1637:toUnicode & toEncodedString (and tests)
#@-node:AGP.20250415230112.1627:Unicode utils...
#@+node:AGP.20250415230112.1644:Utility classes, functions & objects...
#@+node:AGP.20250415230112.1645: List utilities...
#@+node:AGP.20250415230112.1646:appendToList
def appendToList(out, s):

    for i in s:
        out.append(i)
#@-node:AGP.20250415230112.1646:appendToList
#@+node:AGP.20250415230112.1647:flattenList
def flattenList (theList):

    result = []
    for item in theList:
        if type(item) == types.ListType:
            result.extend(g.flattenList(item))
        else:
            result.append(item)
    return result
#@-node:AGP.20250415230112.1647:flattenList
#@+node:AGP.20250415230112.1648:maxStringListLength
def maxStringListLength(aList):
    
    '''Return the maximum string length in a list of strings.'''
    
    n = 0
    for z in aList:
        if type(z) in (type(''),type(u'')):
            n = max(n,len(z))

    return n
#@-node:AGP.20250415230112.1648:maxStringListLength
#@-node:AGP.20250415230112.1645: List utilities...
#@+node:AGP.20250415230112.1649: Index utilities...
#@+node:AGP.20250415230112.1650:g.convertPythonIndexToRowCol  & test
def convertPythonIndexToRowCol (s,i):
    
    '''Convert index i into string s into zero-based row/col indices.'''
    
    if not s or i == 0:
        return 0,0
    else:
        i = min(i,len(s)-1)
        # works regardless of what s[i] is
        row = s.count('\n',0,i) # Don't include i
        if row == 0:
            return row,i
        else:
            prevNl = s.rfind('\n',0,i) # Don't include i
            # assert prevNl > -1
            return row,i-prevNl-1
#@+node:AGP.20250415230112.1651:bruteForceConvertPythonIndexToRowCol
def bruteForceConvertPythonIndexToRowCol (s,i):
        
    lines = g.splitLines(s)
    row,total = 0,0
    for line in lines:
        n = len(line)
        if i < total + n:
            break
        else:
            total += n
            row += 1
    return row, i-total
#@-node:AGP.20250415230112.1651:bruteForceConvertPythonIndexToRowCol
#@+node:AGP.20250415230112.1652:test_g_convertPythonIndexToRowCol
def test_g_convertPythonIndexToRowCol ():
    
    s = '\nabc\n\npdq\nxy'

    for i in xrange(len(s)+1): # Test one-too-large case.
        try: ch = s[i]
        except IndexError: ch = '**'
        rowCol_1 = g.convertPythonIndexToRowCol(s,i)
        rowCol_2 = g.bruteForceConvertPythonIndexToRowCol(s,i)
        if g.app.unitTesting:
            assert i == len(s) or rowCol_1 == rowCol_2
        else:
            print '%2d %4s %5s' % (i,repr(ch),rowCol_1==rowCol_2),
            print rowCol_1,rowCol_2
#@-node:AGP.20250415230112.1652:test_g_convertPythonIndexToRowCol
#@-node:AGP.20250415230112.1650:g.convertPythonIndexToRowCol  & test
#@+node:AGP.20250415230112.1653:g.convertRowColToPythonIndex & test
def convertRowColToPythonIndex (s,row,col):
    
    lines = g.splitLines(s)

    if row >= len(lines):
        return len(s)
        
    col = min(col, len(lines[row]))

    prev = 0
    for line in lines[:row]:
        prev += len(line)
        
    return prev + col
#@+node:AGP.20250415230112.1654:test_g_convertPythonIndexToRowCol
def test_g_convertRowColToPythonIndex ():

    s = '\nabc\n\npdq\nxy'
    lines = g.splitLines(s)
    row = 0 ; prev = -1
    for line in lines:
        col = 0
        for ch in line:
            i = g.convertRowColToPythonIndex(s,row,col)
            assert i == prev + 1,'i %d prev %d' % (i,prev)
            if not g.app.unitTesting:
                print '%4s %2d %2d %2d' % (repr(ch),row,col,i)
            prev = i
            col += 1
        row += 1
#@-node:AGP.20250415230112.1654:test_g_convertPythonIndexToRowCol
#@-node:AGP.20250415230112.1653:g.convertRowColToPythonIndex & test
#@-node:AGP.20250415230112.1649: Index utilities...
#@+node:AGP.20250415230112.1655:angleBrackets & virtual_event_name
# Returns < < s > >

def angleBrackets(s):

    return ( "<<" + s +
        ">>") # must be on a separate line.

virtual_event_name = angleBrackets
#@-node:AGP.20250415230112.1655:angleBrackets & virtual_event_name
#@+node:AGP.20250415230112.1656:CheckVersion
#@+node:AGP.20250415230112.1657:checkVersion (EKR)
# Simplified version by EKR: stringCompare not used.

def CheckVersion (s1,s2,condition=">=",stringCompare=None,delimiter='.',trace=False):
    
    vals1 = [int(s) for s in s1.split(delimiter)] ; n1 = len(vals1)
    vals2 = [int(s) for s in s2.split(delimiter)] ; n2 = len(vals2)
    n = max(n1,n2)
    if n1 < n: vals1.extend([0 for i in xrange(n - n1)])
    if n2 < n: vals2.extend([0 for i in xrange(n - n2)])
    for cond,val in (
        ('==', vals1 == vals2), ('!=', vals1 != vals2),
        ('<',  vals1 <  vals2), ('<=', vals1 <= vals2),
        ('>',  vals1 >  vals2), ('>=', vals1 >= vals2),
    ):
        if condition == cond:
            result = val ; break
    else:
        raise EnvironmentError,"condition must be one of '>=', '>', '==', '!=', '<', or '<='."
    
    if trace:
        # print '%10s' % (repr(vals1)),'%2s' % (condition),'%10s' % (repr(vals2)),result
        print '%7s' % (s1),'%2s' % (condition),'%7s' % (s2),result
    return result
#@nonl
#@-node:AGP.20250415230112.1657:checkVersion (EKR)
#@+node:AGP.20250415230112.1658:oldCheckVersion (Dave Hein)
#@+at
# g.CheckVersion() is a generic version checker.  Assumes a
# version string of up to four parts, or tokens, with
# leftmost token being most significant and each token
# becoming less signficant in sequence to the right.
# 
# RETURN VALUE
# 
# 1 if comparison is True
# 0 if comparison is False
# 
# PARAMETERS
# 
# version: the version string to be tested
# againstVersion: the reference version string to be
#               compared against
# condition: can be any of "==", "!=", ">=", "<=", ">", or "<"
# stringCompare: whether to test a token using only the
#              leading integer of the token, or using the
#              entire token string.  For example, a value
#              of "0.0.1.0" means that we use the integer
#              value of the first, second, and fourth
#              tokens, but we use a string compare for the
#              third version token.
# delimiter: the character that separates the tokens in the
#          version strings.
# 
# The comparison uses the precision of the version string
# with the least number of tokens.  For example a test of
# "8.4" against "8.3.3" would just compare the first two
# tokens.
# 
# The version strings are limited to a maximum of 4 tokens.
#@-at
#@@c

def oldCheckVersion( version, againstVersion, condition=">=", stringCompare="0.0.0.0", delimiter='.' ):

    # g.pdb()

    # tokenize the stringCompare flags
    compareFlag = string.split( stringCompare, '.' )

    # tokenize the version strings
    testVersion = string.split( version, delimiter )
    testAgainst = string.split( againstVersion, delimiter )

    # find the 'precision' of the comparison
    tokenCount = 4
    if tokenCount > len(testAgainst):
        tokenCount = len(testAgainst)
    if tokenCount > len(testVersion):
        tokenCount = len(testVersion)

    # Apply the stringCompare flags
    justInteger = re.compile("^[0-9]+")
    for i in range(tokenCount):
        if "0" == compareFlag[i]:
            m = justInteger.match( testVersion[i] )
            testVersion[i] = m.group()
            m = justInteger.match( testAgainst[i] )
            testAgainst[i] = m.group()
        elif "1" != compareFlag[i]:
            errMsg = "stringCompare argument must be of " +\
                 "the form \"x.x.x.x\" where each " +\
                 "'x' is either '0' or '1'."
            raise EnvironmentError,errMsg

    # Compare the versions
    if condition == ">=":
        for i in range(tokenCount):
            if testVersion[i] < testAgainst[i]:
                return 0
            if testVersion[i] > testAgainst[i]:
                return 1 # it was greater than
        return 1 # it was equal
    if condition == ">":
        for i in range(tokenCount):
            if testVersion[i] < testAgainst[i]:
                return 0
            if testVersion[i] > testAgainst[i]:
                return 1 # it was greater than
        return 0 # it was equal
    if condition == "==":
        for i in range(tokenCount):
            if testVersion[i] != testAgainst[i]:
                return 0 # any token was not equal
        return 1 # every token was equal
    if condition == "!=":
        for i in range(tokenCount):
            if testVersion[i] != testAgainst[i]:
                return 1 # any token was not equal
        return 0 # every token was equal
    if condition == "<":
        for i in range(tokenCount):
            if testVersion[i] >= testAgainst[i]:
                return 0
            if testVersion[i] < testAgainst[i]:
                return 1 # it was less than
        return 0 # it was equal
    if condition == "<=":
        for i in range(tokenCount):
            if testVersion[i] > testAgainst[i]:
                return 0
            if testVersion[i] < testAgainst[i]:
                return 1 # it was less than
        return 1 # it was equal

    # didn't find a condition that we expected.
    raise EnvironmentError,"condition must be one of '>=', '>', '==', '!=', '<', or '<='."
#@nonl
#@-node:AGP.20250415230112.1658:oldCheckVersion (Dave Hein)
#@-node:AGP.20250415230112.1656:CheckVersion
#@+node:AGP.20250415230112.1659:class Bunch (object)
#@+at 
#@nonl
# From The Python Cookbook:  Often we want to just collect a bunch of stuff 
# together, naming each item of the bunch; a dictionary's OK for that, but a 
# small do-nothing class is even handier, and prettier to use.
# 
# Create a Bunch whenever you want to group a few variables:
# 
#     point = Bunch(datum=y, squared=y*y, coord=x)
# 
# You can read/write the named attributes you just created, add others, del 
# some of them, etc:
#     if point.squared > threshold:
#         point.isok = True
#@-at
#@@c

class Bunch (object):
    
    """A class that represents a colection of things.
    
    Especially useful for representing a collection of related variables."""
    
    def __init__(self,**keywords):
        self.__dict__.update (keywords)
        
    def __repr__(self):
        return self.toString()

    def ivars(self):
        return self.__dict__.keys()
        
    def keys(self):
        return self.__dict__.keys()
        
    def toString(self):
        tag = self.__dict__.get('tag')
        entries = ["%s: %s" % (key,str(self.__dict__.get(key)))
            for key in self.ivars() if key != 'tag']
        if tag:
            return "Bunch(tag=%s)...\n%s\n" % (tag,'\n'.join(entries))
        else:
            return "Bunch...\n%s\n" % '\n'.join(entries)

    # Used by new undo code.
    def __setitem__ (self,key,value):
        '''Support aBunch[key] = val'''
        return operator.setitem(self.__dict__,key,value)
        
    def __getitem__ (self,key):
        '''Support aBunch[key]'''
        return operator.getitem(self.__dict__,key)
        
    def get (self,key,theDefault=None):
        return self.__dict__.get(key,theDefault)
        
bunch = Bunch
#@-node:AGP.20250415230112.1659:class Bunch (object)
#@+node:AGP.20250415230112.1660:class mulderUpdateAlgorithm (leoGlobals)
import difflib,shutil

class mulderUpdateAlgorithm:
    
    """A class to update derived files using
    diffs in files without sentinels.
    """
    
    #@    @+others
    #@+node:AGP.20250415230112.1661:__init__
    def __init__ (self,testing=False,verbose=False):
        
        self.testing = testing
        self.verbose = verbose
        self.do_backups = False
    #@-node:AGP.20250415230112.1661:__init__
    #@+node:AGP.20250415230112.1662:copy_sentinels
    #@+at 
    #@nonl
    # This script retains _all_ sentinels.  If lines are replaced, or deleted,
    # we restore deleted sentinel lines by checking for gaps in the mapping.
    #@-at
    #@@c
    
    def copy_sentinels (self,write_lines,fat_lines,fat_pos,mapping,startline,endline):
        """
        
        Copy sentinel lines from fat_lines to write_lines.
    
        Copy all sentinels _after_ the current reader postion up to,
        but not including, mapping[endline].
    
        """
    
        j_last = mapping[startline]
        i = startline + 1
        while i <= endline:
            j = mapping[i]
            if j_last + 1 != j:
                fat_pos = j_last + 1
                # Copy the deleted sentinels that comprise the gap.
                while fat_pos < j:
                    line = fat_lines[fat_pos]
                    write_lines.append(line)
                    if self.testing and self.verbose: print "Copy sentinel:",fat_pos,line,
                    fat_pos += 1
            j_last = j ; i += 1
    
        fat_pos = mapping[endline]
        return fat_pos
    #@-node:AGP.20250415230112.1662:copy_sentinels
    #@+node:AGP.20250415230112.1663:copy_time
    def copy_time(self,sourcefilename,targetfilename):
        
        """
        Set the target file's modification time to
        that of the source file.
        """
    
        st = os.stat(sourcefilename)
    
        if hasattr(os, 'utime'):
            os.utime(targetfilename, (st.st_atime, st.st_mtime))
        elif hasattr(os, 'mtime'):
            os.mtime(targetfilename, st.st_mtime)
        else:
            g.trace("Can not set modification time")
    #@-node:AGP.20250415230112.1663:copy_time
    #@+node:AGP.20250415230112.1664:create_mapping
    def create_mapping (self,lines,delims):
        """
    
        'lines' is a list of lines of a file with sentinels.
     
        Returns:
    
        result: lines with all sentinels removed.
    
        mapping: a list such that result[mapping[i]] == lines[i]
        for all i in range(len(result))
    
        """
        
        if not lines:
            return [],[]
    
        # Create mapping and set i to the index of the last non-sentinel line.
        mapping = []
        for i in xrange(len(lines)):
            if not g.is_sentinel(lines[i],delims):
                mapping.append(i)
    
        # Create a last mapping entry for copy_sentinels.
        mapping.append(i)
        
        # Use removeSentinelsFromLines to handle @nonl properly.
        stripped_lines = self.removeSentinelsFromLines(lines,delims)
    
        return stripped_lines, mapping
    #@-node:AGP.20250415230112.1664:create_mapping
    #@+node:AGP.20250415230112.1665:Get or remove sentinel lines
    # These routines originally were part of push_filter & push_filter_lines.
    #@+node:AGP.20250415230112.1666:separateSentinelsFromFile/Lines
    def separateSentinelsFromFile (self,filename):
        
        """Separate the lines of the file into a tuple of two lists,
        containing the sentinel and non-sentinel lines of the file."""
        
        lines = file(filename).readlines()
        delims = g.comment_delims_from_extension(filename)
        
        return self.separateSentinelsFromLines(lines,delims)
        
    def separateSentinelsFromLines (self,lines,delims):
        
        """Separate lines (a list of lines) into a tuple of two lists,
        containing the sentinel and non-sentinel lines of the original list."""
        
        strippedLines = self.removeSentinelsFromLines(lines,delims)
        sentinelLines = self.getSentinelsFromLines(lines,delims)
        
        return strippedLines,sentinelLines
    #@-node:AGP.20250415230112.1666:separateSentinelsFromFile/Lines
    #@+node:AGP.20250415230112.1667:removeSentinelsFromFile/Lines
    def removeSentinelsFromFile (self,filename):
        
        """Return a copy of file with all sentinels removed."""
        
        lines = file(filename).readlines()
        delims = g.comment_delims_from_extension(filename)
        
        return self.removeSentinelsFromLines(lines,delims)
        
    def removeSentinelsFromLines (self,lines,delims):
    
        """Return a copy of lines with all sentinels removed."""
        
        delim1,delim2,delim3 = delims
        result = [] ; last_nosent_i = -1
        for i in xrange(len(lines)):
            if not g.is_sentinel(lines[i],delims):
                result.append(lines[i])
                last_nosent_i = i
        #@    << remove the newline from result[-1] if line[i] is followed by @nonl >>
        #@+node:AGP.20250415230112.1668:<< remove the newline from result[-1] if line[i] is followed by @nonl >>
        i = last_nosent_i
        
        if i + 1 < len(lines):
        
            line = lines[i+1]
            j = g.skip_ws(line,0)
        
            if match(line,j,delim1):
                j += len(delim1)
        
                if g.match(line,j,"@nonl"):
                    line = lines[i]
                    if line[-1] == '\n':
                        assert(result[-1] == line)
                        result[-1] = line[:-1]
        #@-node:AGP.20250415230112.1668:<< remove the newline from result[-1] if line[i] is followed by @nonl >>
        #@nl
        return result
    #@-node:AGP.20250415230112.1667:removeSentinelsFromFile/Lines
    #@+node:AGP.20250415230112.1669:getSentinelsFromFile/Lines
    def getSentinelsFromFile (self,filename,delims):
        
        """Returns all sentinels lines in a file."""
        
        lines = file(filename).readlines()
        delims = g.comment_delims_from_extension(filename)
    
        return self.getSentinelsFromLines(lines,delims)
        
    def getSentinelsFromLines (self,lines,delims):
        
        """Returns all sentinels lines in lines."""
        
        return [line for line in lines if g.is_sentinel(line,delims)]
    #@-node:AGP.20250415230112.1669:getSentinelsFromFile/Lines
    #@-node:AGP.20250415230112.1665:Get or remove sentinel lines
    #@+node:AGP.20250415230112.1670:propagateDiffsToSentinelsFile
    def propagateDiffsToSentinelsFile(self,sourcefilename,targetfilename):
        
        #@    << init propagateDiffsToSentinelsFile vars >>
        #@+node:AGP.20250415230112.1671:<< init propagateDiffsToSentinelsFile vars >>
        # Get the sentinel comment delims.
        delims = g.comment_delims_from_extension(sourcefilename)
        if not delims:
            return
        
        try:
            # Create the readers.
            sfile = file(sourcefilename)
            tfile = file(targetfilename)
            
            fat_lines = sfile.readlines() # Contains sentinels.
            j_lines   = tfile.readlines() # No sentinels.
            
            i_lines,mapping = self.create_mapping(fat_lines,delims)
            
            sfile.close()
            tfile.close()
        except:
            g.es_exception("can not open files")
            return
        #@-node:AGP.20250415230112.1671:<< init propagateDiffsToSentinelsFile vars >>
        #@nl
        
        write_lines = self.propagateDiffsToSentinelsLines(
            i_lines,j_lines,fat_lines,mapping)
            
        # Update _source_ file if it is not the same as write_lines.
        written = self.write_if_changed(write_lines,targetfilename,sourcefilename)
        if written:
            #@        << paranoia check>>
            #@+node:AGP.20250415230112.1672:<<paranoia check>>
            # Check that 'push' will re-create the changed file.
            strippedLines,sentinel_lines = self.separateSentinelsFromFile(sourcefilename)
            
            if strippedLines != j_lines:
                self.report_mismatch(strippedLines, j_lines,
                    "Propagating diffs did not work as expected",
                    "Content of sourcefile:",
                    "Content of modified file:")
            
            # Check that no sentinels got lost.
            fat_sentinel_lines = self.getSentinelsFromLines(fat_lines,delims)
            
            if sentinel_lines != fat_sentinel_lines:
                self.report_mismatch(sentinel_lines,fat_sentinel_lines,
                    "Propagating diffs modified sentinel lines:",
                    "Current sentinel lines:",
                    "Old sentinel lines:")
            #@-node:AGP.20250415230112.1672:<<paranoia check>>
            #@nl
    #@-node:AGP.20250415230112.1670:propagateDiffsToSentinelsFile
    #@+node:AGP.20250415230112.1673:propagateDiffsToSentinelsLines (called from perfect import)
    def propagateDiffsToSentinelsLines (self,
        i_lines,j_lines,fat_lines,mapping):
        
        """Compare the 'i_lines' with 'j_lines' and propagate the diffs back into
        'write_lines' making sure that all sentinels of 'fat_lines' are copied.
    
        i/j_lines have no sentinels.  fat_lines does."""
    
        #@    << init propagateDiffsToSentinelsLines vars >>
        #@+node:AGP.20250415230112.1674:<< init propagateDiffsToSentinelsLines vars >>
        # Indices into i_lines, j_lines & fat_lines.
        i_pos = j_pos = fat_pos = 0
        
        # These vars check that all ranges returned by get_opcodes() are contiguous.
        i2_old = j2_old = -1
        
        # Create the output lines.
        write_lines = []
        
        matcher = difflib.SequenceMatcher(None,i_lines,j_lines)
        
        testing = self.testing
        verbose = self.verbose
        #@-node:AGP.20250415230112.1674:<< init propagateDiffsToSentinelsLines vars >>
        #@nl
        #@    << copy the sentinels at the beginning of the file >>
        #@+node:AGP.20250415230112.1675:<< copy the sentinels at the beginning of the file >>
        while fat_pos < mapping[0]:
        
            line = fat_lines[fat_pos]
            write_lines.append(line)
            if testing:
                print "copy initial line",fat_pos,line,
            fat_pos += 1
        #@-node:AGP.20250415230112.1675:<< copy the sentinels at the beginning of the file >>
        #@nl
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if testing:
                if verbose: print
                print "Opcode %7s %3d %3d %3d %3d" % (tag,i1,i2,j1,j2)
                if verbose: print
            #@        << update and check the loop invariant >>
            #@+node:AGP.20250415230112.1676:<< update and check the loop invariant>>
            # We need the ranges returned by get_opcodes to completely cover the source lines being compared.
            # We also need the ranges not to overlap.
            
            assert(i2_old in (-1,i1))
            assert(j2_old in (-1,j1))
            
            i2_old = i2 ; j2_old = j2
            
            # Check the loop invariants.
            assert i_pos == i1
            assert j_pos == j1
            assert fat_pos == mapping[i1]
            
            if 0: # not yet.
                if testing: # A bit costly.
                    t_sourcelines,t_sentinel_lines = push_filter_lines(write_lines, delims)
                    # Check that we have all the modifications so far.
                    assert t_sourcelines == j_lines[:j1],"t_sourcelines == j_lines[:j1]"
                    # Check that we kept all sentinels so far.
                    assert t_sentinel_lines == push_filter_lines(fat_lines[:fat_pos], delims)[1]
            #@-node:AGP.20250415230112.1676:<< update and check the loop invariant>>
            #@nl
            if tag == 'equal':
                #@            << handle 'equal' tag >>
                #@+node:AGP.20250415230112.1677:<< handle 'equal' tag >>
                # Copy the lines, including sentinels.
                while fat_pos <= mapping[i2-1]:
                    line = fat_lines[fat_pos]
                    if 0: # too verbose.
                        if testing: print "Equal: copying ", line,
                    write_lines.append(line)
                    fat_pos += 1
                
                if testing and verbose:
                    print "Equal: synch i", i_pos,i2
                    print "Equal: synch j", j_pos,j2
                
                i_pos = i2
                j_pos = j2
                
                # Copy the sentinels which might follow the lines.       
                fat_pos = self.copy_sentinels(write_lines,fat_lines,fat_pos,mapping,i2-1,i2)
                #@-node:AGP.20250415230112.1677:<< handle 'equal' tag >>
                #@nl
            elif tag == 'replace':
                #@            << handle 'replace' tag >>
                #@+node:AGP.20250415230112.1678:<< handle 'replace' tag >>
                #@+at 
                #@nonl
                # Replace lines that may span sentinels.
                # 
                # For now, we put all the new contents after the first 
                # sentinel.
                # 
                # A more complex approach: run the difflib across the 
                # different lines and try to
                # construct a mapping changed line => orignal line.
                #@-at
                #@@c
                
                while j_pos < j2:
                    line = j_lines[j_pos]
                    if testing:
                        print "Replace i:",i_pos,repr(i_lines[i_pos])
                        print "Replace j:",j_pos,repr(line)
                        i_pos += 1
                
                    write_lines.append(line)
                    j_pos += 1
                
                i_pos = i2
                
                # Copy the sentinels which might be between the changed code.         
                fat_pos = self.copy_sentinels(write_lines,fat_lines,fat_pos,mapping,i1,i2)
                #@-node:AGP.20250415230112.1678:<< handle 'replace' tag >>
                #@nl
            elif tag == 'delete':
                #@            << handle 'delete' tag >>
                #@+node:AGP.20250415230112.1679:<< handle 'delete' tag >>
                if testing and verbose:
                    print "delete: i",i_pos,i1
                    print "delete: j",j_pos,j1
                
                j_pos = j2
                i_pos = i2
                
                # Restore any deleted sentinels.
                fat_pos = self.copy_sentinels(write_lines,fat_lines,fat_pos,mapping,i1,i2)
                #@-node:AGP.20250415230112.1679:<< handle 'delete' tag >>
                #@nl
            elif tag == 'insert':
                #@            << handle 'insert' tag >>
                #@+node:AGP.20250415230112.1680:<< handle 'insert' tag >>
                while j_pos < j2:
                    line = j_lines[j_pos]
                    if testing: print "Insert:", line,
                    write_lines.append(line)
                    j_pos += 1
                
                # The input streams are already in synch.
                #@-node:AGP.20250415230112.1680:<< handle 'insert' tag >>
                #@nl
            else: assert 0,"bad tag"
        #@    << copy the sentinels at the end of the file >>
        #@+node:AGP.20250415230112.1681:<< copy the sentinels at the end of the file >>
        while fat_pos < len(fat_lines):
        
            line = fat_lines[fat_pos]
            write_lines.append(line)
            if testing:
                print "Append last line",line
            fat_pos += 1
        #@-node:AGP.20250415230112.1681:<< copy the sentinels at the end of the file >>
        #@nl
        return write_lines
    #@-node:AGP.20250415230112.1673:propagateDiffsToSentinelsLines (called from perfect import)
    #@+node:AGP.20250415230112.1682:report_mismatch
    def report_mismatch (self,lines1,lines2,message,lines1_message,lines2_message):
    
        """
        Generate a report when something goes wrong.
        """
        
        print '='*20
        print message
        
        if 0:
            print lines1_message
            print '-'*20
            for line in lines1:
              print line,
             
            print '='*20
        
            print lines2_message
            print '-'*20
            for line in lines2:
                print line,
    #@-node:AGP.20250415230112.1682:report_mismatch
    #@+node:AGP.20250415230112.1683:stripWhitespaceFromBlankLines(before_lines)
    def stripWhitespaceFromBlankLines (self,lines):
        
        # All backslashes must be doubled.
    
        """Strip blanks and tabs from lines containing only blanks and tabs.
        
        >>> import leoGlobals as g
        >>> s = "a\\n \\t\\n\\t\\t \\t\\nb"
        >>> theLines = g.splitLines(s)
        >>> theLines
        ['a\\n', ' \\t\\n', '\\t\\t \\t\\n', 'b']
        >>> g.mulderUpdateAlgorithm().stripWhitespaceFromBlankLines(theLines)
        ['a\\n', '\\n', '\\n', 'b']
        """
    
        for i in xrange(len(lines)):
            # lstrip does not exist in python 2.2.1.
            stripped_line = lines[i]
            while stripped_line and stripped_line[0] in (' ','\t'):
                stripped_line = stripped_line [1:]
            if stripped_line in ('\n',''):
                lines[i] = stripped_line
                
        return lines
    #@-node:AGP.20250415230112.1683:stripWhitespaceFromBlankLines(before_lines)
    #@+node:AGP.20250415230112.1684:write_if_changed
    def write_if_changed(self,lines,sourcefilename,targetfilename):
        """
        
        Replaces target file if it is not the same as 'lines',
        and makes the modification date of target file the same as the source file.
        
        Optionally backs up the overwritten file.
    
        """
        
        copy = not os.path.exists(targetfilename) or lines != file(targetfilename).readlines()
            
        if self.testing:
            if copy:
                print "Writing",targetfilename,"without sentinals"
            else:
                print "Files are identical"
    
        if copy:
            if self.do_backups:
                #@            << make backup file >>
                #@+node:AGP.20250415230112.1685:<< make backup file >>
                if os.path.exists(targetfilename):
                    count = 0
                    backupname = "%s.~%s~" % (targetfilename,count)
                    while os.path.exists(backupname):
                        count += 1
                        backupname = "%s.~%s~" % (targetfilename,count)
                    os.rename(targetfilename, backupname)
                    if self.testing:
                        print "backup file in ", backupname
                #@-node:AGP.20250415230112.1685:<< make backup file >>
                #@nl
            outfile = open(targetfilename, "w")
            for line in lines:
                outfile.write(line)
            outfile.close()
            self.copy_time(sourcefilename,targetfilename)
        return copy
    #@-node:AGP.20250415230112.1684:write_if_changed
    #@-others
    
#def doMulderUpdateAlgorithm(sourcefilename,targetfilename):
#
#    mu = mulderUpdateAlgorithm()
#
#    mu.pull_source(sourcefilename,targetfilename)
#    mu.copy_time(targetfilename,sourcefilename)
#@-node:AGP.20250415230112.1660:class mulderUpdateAlgorithm (leoGlobals)
#@+node:AGP.20250415230112.1686:class nullObject
# From the Python cookbook, recipe 5.23

class nullObject:
    
    """An object that does nothing, and does it very well."""
    
    def __init__   (self,*args,**keys): pass
    def __call__   (self,*args,**keys): return self
    
    def __repr__   (self): return "nullObject"
    
    def __nonzero__ (self): return 0
    
    def __delattr__(self,attr):     return self
    def __getattr__(self,attr):     return self
    def __setattr__(self,attr,val): return self
#@-node:AGP.20250415230112.1686:class nullObject
#@+node:AGP.20250415230112.1687:g.makeDict
# From the Python cookbook.

def makeDict(**keys):
    
    """Returns a Python dictionary from using the optional keyword arguments."""

    return keys
#@-node:AGP.20250415230112.1687:g.makeDict
#@+node:AGP.20250415230112.1688:g.computeWindowTitle
def computeWindowTitle (fileName):

    if fileName == None:
        return "untitled"
    else:
        path,fn = g.os_path_split(fileName)
        if path:
            title = fn + " in " + path
        else:
            title = fn
        return title
#@-node:AGP.20250415230112.1688:g.computeWindowTitle
#@+node:AGP.20250415230112.1689:g.executeScript
def executeScript (name):
    
    """Execute a script whose short python file name is given"""
    
    mod_name,ext = g.os_path_splitext(name)
    theFile = None
    try:
        # This code is in effect an import or a reload.
        # This allows the user to modify scripts without leaving Leo.
        import imp
        theFile,filename,description = imp.find_module(mod_name)
        imp.load_module(mod_name,theFile,filename,description)
    except:
        g.es("Exception executing " + name,color="red")
        g.es_exception()

    if theFile:
        theFile.close()
#@-node:AGP.20250415230112.1689:g.executeScript
#@+node:AGP.20250415230112.1690:g.fileLikeObject
# Note: we could use StringIo for this.

class fileLikeObject:

    """Define a file-like object for redirecting writes to a string.
    
    The caller is responsible for handling newlines correctly."""
    
    #@    @+others
    #@+node:AGP.20250415230112.1691: ctor
    def __init__(self,fromString=None):
    
        # New in 4.2.1: allow the file to be inited from string s.
        if fromString:
            self.list = g.splitLines(fromString) # Must preserve newlines!
        else:
            self.list = []
    
        self.ptr = 0
        
    # In CStringIO the buffer is read-only if the initial value (fromString) is non-empty.
    #@-node:AGP.20250415230112.1691: ctor
    #@+node:AGP.20250415230112.1692:clear
    def clear (self):
        
        self.list = []
    #@-node:AGP.20250415230112.1692:clear
    #@+node:AGP.20250415230112.1693:close
    def close (self):
        
        pass
        
        # The StringIo version free's the memory buffer.
    #@-node:AGP.20250415230112.1693:close
    #@+node:AGP.20250415230112.1694:flush
    def flush (self):
        
        pass
    #@-node:AGP.20250415230112.1694:flush
    #@+node:AGP.20250415230112.1695:get & getvalue
    def get (self):
    
        return ''.join(self.list)
        
    getvalue = get # for compatibility with StringIo
    #@-node:AGP.20250415230112.1695:get & getvalue
    #@+node:AGP.20250415230112.1696:readline
    def readline(self): # New for read-from-string (readOpenFile).
    
        if self.ptr < len(self.list):
            line = self.list[self.ptr]
            # g.trace(repr(line))
            self.ptr += 1
            return line
        else:
            return ''
    #@-node:AGP.20250415230112.1696:readline
    #@+node:AGP.20250415230112.1697:write
    def write (self,s):
        
        if s:
            self.list.append(s)
    #@-node:AGP.20250415230112.1697:write
    #@-others
#@-node:AGP.20250415230112.1690:g.fileLikeObject
#@+node:AGP.20250415230112.1698:g.funcToMethod
#@+at 
#@nonl
# The following is taken from page 188 of the Python Cookbook.
# 
# The following method allows you to add a function as a method of any class.  
# That is, it converts the function to a method of the class.  The method just 
# added is available instantly to all existing instances of the class, and to 
# all instances created in the future.
# 
# The function's first argument should be self.
# 
# The newly created method has the same name as the function unless the 
# optional name argument is supplied, in which case that name is used as the 
# method name.
#@-at
#@@c

def funcToMethod(f,theClass,name=None):

    setattr(theClass,name or f.__name__,f)
    # g.trace(name)
#@-node:AGP.20250415230112.1698:g.funcToMethod
#@+node:AGP.20250415230112.1699:g.getScript & tests
def getScript (c,p,useSelectedText=True,forcePythonSentinels=True,useSentinels=True):
    
    '''Return the expansion of the selected text of node p.
    Return the expansion of all of node p's body text if there
    is p is not the current node or if there is no text selection.'''

    at = c.atFileCommands
    if not p:
        p = c.currentPosition()
    try:
        if g.app.batchMode:
            s = p.bodyString()
        elif p == c.currentPosition():
            if useSelectedText and c.frame.body.hasTextSelection():
                s = c.frame.body.getSelectedText()
            else:
                s = c.frame.body.getAllText()
        else:
            s = p.bodyString()
        # Remove extra leading whitespace so the user may execute indented code.
        s = g.removeExtraLws(s,c.tab_width)
        if s.strip():
            g.app.scriptDict["script1"]=s
            script = at.writeFromString(p.copy(),s,
                forcePythonSentinels=forcePythonSentinels,
                useSentinels=useSentinels)
            script = script.replace("\r\n","\n") # Use brute force.
            # Important, the script is an **encoded string**, not a unicode string.
            g.app.scriptDict["script2"]=script
        else: script = ''
    except Exception:
        s = "unexpected exception in g.getScript"
        g.es_print(s)
        g.es_exception()
        script = ''

    # g.trace(type(script),repr(script))
    return script
#@+node:AGP.20250415230112.1700:test_g_getScript_strips_crlf
def test_g_getScript_strips_crlf():

    script = g.getScript(c,p) # This will get the text of this node.
    assert script.find('\r\n') == -1, repr(script)
#@-node:AGP.20250415230112.1700:test_g_getScript_strips_crlf
#@-node:AGP.20250415230112.1699:g.getScript & tests
#@+node:AGP.20250415230112.1701:g.longestCommonPrefix & g.itemsMatchingPrefixInList
def longestCommonPrefix (s1,s2):
    
    '''Find the longest prefix common to strings s1 and s2.'''
    
    prefix = ''
    for ch in s1:
        if s2.startswith(prefix + ch):
            prefix = prefix + ch
        else:
            return prefix
    return prefix
        
def itemsMatchingPrefixInList (s,aList,matchEmptyPrefix=False):
    
    '''This method returns a sorted list items of aList whose prefix is s.
    
    It also returns the longest common prefix of all the matches.'''

    if s:
        pmatches = [a for a in aList if a.startswith(s)]
    elif matchEmptyPrefix:
        pmatches = aList[:]
    else: pmatches = []

    if pmatches:
        pmatches.sort()
        common_prefix = reduce(g.longestCommonPrefix,pmatches)
    else:
        common_prefix = ''

    # g.trace(repr(s),len(pmatches))
    return pmatches,common_prefix
#@-node:AGP.20250415230112.1701:g.longestCommonPrefix & g.itemsMatchingPrefixInList
#@+node:AGP.20250415230112.1702:import wrappers
#@+at 
#@nonl
# 1/6/05: The problem with Tkinter is that imp.load_module is equivalent to 
# reload.
# 
# The solutions is easy: simply return sys.modules.get(moduleName) if 
# moduleName is in sys.modules!
#@-at
#@+node:AGP.20250415230112.1703:g.cantImport
def cantImport (moduleName,pluginName=None,verbose=True):
    
    """Print a "Can't Import" message and return None."""

    # g.trace(verbose,moduleName,repr(pluginName))
    # if not pluginName: g.printStack()
    
    if verbose and not g.app.unitTesting:
        s = "Can not import %s" % moduleName
        if pluginName: s += " from plugin %s" % pluginName
        g.es_print(s,color="blue")

    return None
#@-node:AGP.20250415230112.1703:g.cantImport
#@+node:AGP.20250415230112.1704:g.importModule
def importModule (moduleName,pluginName=None,verbose=False):

    '''Try to import a module as Python's import command does.

    moduleName is the module's name, without file extension.'''
    
    module = sys.modules.get(moduleName)
    if not module:
        try:
            theFile = None
            import imp
            try:    #agp
                #print moduleName
                module =  __import__(moduleName, globals(), locals(), [], -1)

            except ImportError:
                g.cantImport(moduleName,pluginName=pluginName,verbose=verbose)
            
            #try:   #agp
            #    data = imp.find_module(moduleName) # This can open the file.
            #    theFile,pathname,description = data
            #    module = imp.load_module(moduleName,theFile,pathname,description)
            #except Exception: # Importing a module can throw exceptions other than ImportError.
            #    g.cantImport(moduleName,pluginName=pluginName,verbose=verbose)
        finally:
            if theFile: theFile.close()
    return module
#@-node:AGP.20250415230112.1704:g.importModule
#@+node:AGP.20250415230112.1705:g.importExtension & helpers
def importExtension (moduleName,pluginName=None,verbose=False,required=False):

    '''Try to import a module.  If that fails,
    try to import the module from Leo's extensions directory.

    moduleName is the module's name, without file extension.'''
    
    # g.trace(verbose,moduleName,pluginName)
    
    module = g.importModule(moduleName,pluginName=pluginName,verbose=False)

    if not module:
        #print g.app.extensionsDir
        module = g.importFromPath(moduleName,g.app.extensionsDir,
            pluginName=pluginName,verbose=verbose)
            
        if not module and required:
            g.cantImportDialog(pluginName,moduleName)
            try: # Avoid raising SystemExit if possible.
                import os ; os._exit(1) # May not be available on all platforms.
            except Exception:
                import sys ; sys.exit(1)

    return module
#@+node:AGP.20250415230112.1706:cantImportDialog & helpers
def cantImportDialog (pluginName,moduleName):
    
    message = '''
%s requires the %s module.
Official distributions contain this module in Leo's extensions folder,
but this module may be missing if you get Leo from cvs.
''' % (pluginName,moduleName)

    if 1: # Requires minimal further imports.
        try:
            import Tkinter as Tk
            root = g.app.root or Tk.Tk()
            title = 'Can not import %s' % moduleName
            top = createDialogFrame(Tk,root,title,message)
            root.wait_window(top)
        except ImportError:
            print 'Can not import %s' % moduleName
            print 'Can not import Tkinter'
            print 'Leo must now exit'
        
    else: # Can cause import problems during startup.
        import leoTkinterDialog
        
        d = leoTkinterDialog.tkinterAskOk(
            c=None,title='Can not import %s' %(moduleName),
            message=message)
        d.run(modal=True)
#@+node:AGP.20250415230112.1707:createDialogFrame
def createDialogFrame(Tk,root,title,message):
    
    """Create the Tk.Toplevel widget for a leoTkinterDialog."""

    top = Tk.Toplevel(root)
    top.title(title)

    def onKey(event,top=top):
        if event.char.lower() in ('\n','\r'):
            top.destroy()
    top.bind("<Key>",onKey)

    f = Tk.Frame(top)
    f.pack(side="top",expand=1,fill="both")
    
    label = Tk.Label(f,text=message)
    label.pack(pady=10)
    
    def okButton(top=top):
        top.destroy()
    
    buttons = {"text":'OK',"command":okButton,"default":True}, # Singleton tuple.
    createDialogButtons(Tk,top,buttons)
    
    center(top)
    top.lift()
    top.focus_force()
    
    # Attach the icon at idle time.
    def attachIconCallback(top=top):
        g.app.gui.attachLeoIcon(top)
    top.after_idle(attachIconCallback)

    return top
#@-node:AGP.20250415230112.1707:createDialogFrame
#@+node:AGP.20250415230112.1708:createDialogButtons
def createDialogButtons (Tk,top,buttons):
    
    """Create a row of buttons.
    
    buttons is a list of dictionaries containing the properties of each button."""
    
    f = Tk.Frame(top)
    f.pack(side="top",padx=30)

    for d in buttons:
        text = d.get("text","<missing button name>")
        isDefault = d.get("default",False)
        underline = d.get("underline",0)
        command = d.get("command",None)
        bd = g.choose(isDefault,4,2)

        b = Tk.Button(f,width=6,text=text,bd=bd,underline=underline,command=command)
        b.pack(side="left",padx=5,pady=10)
#@-node:AGP.20250415230112.1708:createDialogButtons
#@+node:AGP.20250415230112.1709:center
def center(top):

    """Center the dialog on the screen.

    WARNING: Call this routine _after_ creating a dialog.
    (This routine inhibits the grid and pack geometry managers.)"""

    sw = top.winfo_screenwidth()
    sh = top.winfo_screenheight()
    w,h,x,y = get_window_info(top)
    
    # Set the new window coordinates, leaving w and h unchanged.
    x = (sw - w)/2
    y = (sh - h)/2
    top.geometry("%dx%d%+d%+d" % (w,h,x,y))
    
    return w,h,x,y
#@-node:AGP.20250415230112.1709:center
#@+node:AGP.20250415230112.1710:get_window_info
# WARNING: Call this routine _after_ creating a dialog.
# (This routine inhibits the grid and pack geometry managers.)

def get_window_info (top):
    
    top.update_idletasks() # Required to get proper info.

    # Get the information about top and the screen.
    geom = top.geometry() # geom = "WidthxHeight+XOffset+YOffset"
    dim,x,y = string.split(geom,'+')
    w,h = string.split(dim,'x')
    w,h,x,y = int(w),int(h),int(x),int(y)
    
    return w,h,x,y
#@-node:AGP.20250415230112.1710:get_window_info
#@-node:AGP.20250415230112.1706:cantImportDialog & helpers
#@-node:AGP.20250415230112.1705:g.importExtension & helpers
#@+node:AGP.20250415230112.1711:g.importFromPath
def importFromPath (name,path,pluginName=None,verbose=False):
    
    fn = g.shortFileName(name)
    moduleName,ext = g.os_path_splitext(fn)
    path = g.os_path_normpath(path)
    path = g.toEncodedString(path,app.tkEncoding)
    
    # g.trace(verbose,name,pluginName)
    module = sys.modules.get(moduleName)
    if not module:
        try:
            theFile = None
            import imp
            try:
                data = imp.find_module(moduleName,[path]) # This can open the file.
                theFile,pathname,description = data
                module = imp.load_module(moduleName,theFile,pathname,description)
            except ImportError:
                g.es_exception()
                                
            except Exception:
                g.es_print("unexpected exception in g.importFromPath",color='blue')
                g.es_exception()
            
            
            
            
        # Put no return statements before here!
        finally: 
            if theFile: theFile.close()
        
    if not module:
        g.cantImport(moduleName,pluginName=pluginName,verbose=verbose)

    return module
#@-node:AGP.20250415230112.1711:g.importFromPath
#@-node:AGP.20250415230112.1702:import wrappers
#@+node:AGP.20250415230112.1712:g.prettyPrintType
def prettyPrintType (obj):

    if type(obj) in (
        types.MethodType,types.UnboundMethodType,types.BuiltinMethodType):
        return 'method'
    elif type(obj) in (types.BuiltinFunctionType,types.FunctionType):
        return 'function'
    elif type(obj) == types.ModuleType:
        return 'module'
    elif type(obj) == types.InstanceType:
        return 'object'
    elif type(obj) in (types.UnicodeType,types.StringType):
        return 'string'
    else:
        theType = str(type(obj))
        if theType.startswith("<type '"): theType = theType[7:]
        if theType.endswith("'>"): theType = theType[:-2]
        return theType
#@-node:AGP.20250415230112.1712:g.prettyPrintType
#@+node:AGP.20250415230112.1713:g.stripBrackets
def stripBrackets (s):
    
    '''Same as s.lstrip('<').rstrip('>') except it works for Python 2.2.1.'''
    
    if s.startswith('<'):
        s = s[1:]
    if s.endswith('>'):
        s = s[:-1]
    return s
#@-node:AGP.20250415230112.1713:g.stripBrackets
#@+node:AGP.20250415230112.1714:readLines class and generator
#@+node:AGP.20250415230112.1715:g.readLinesGenerator
def readLinesGenerator(s):

    for line in g.splitLines(s):
        # g.trace(repr(line))
        yield line
    yield ''
#@-node:AGP.20250415230112.1715:g.readLinesGenerator
#@+node:AGP.20250415230112.1716:class readLinesClass
class readLinesClass:
    
    """A class whose next method provides a readline method for Python's tokenize module."""

    def __init__ (self,s):
        self.lines = g.splitLines(s)
        self.i = 0

    def next(self):
        if self.i < len(self.lines):
            line = self.lines[self.i]
            self.i += 1
        else:
            line = ''
        # g.trace(repr(line))
        return line
#@-node:AGP.20250415230112.1716:class readLinesClass
#@-node:AGP.20250415230112.1714:readLines class and generator
#@-node:AGP.20250415230112.1644:Utility classes, functions & objects...
#@+node:AGP.20250415230112.1717:Whitespace...
#@+node:AGP.20250415230112.1718:g.adjustTripleString (same as removeExtraLws)
def adjustTripleString (s,tab_width):
    
    '''Remove leading indentation from a triple-quoted string.
    
    This works around the fact that Leo nodes can't represent underindented strings.
    '''
    
    # Compute the minimum leading whitespace of all non-blank lines.
    lines = g.splitLines(s)
    w = -1
    for s in lines:
       if s.strip():
            lws = g.get_leading_ws(s)
            w2 = g.computeWidth(lws,tab_width)
            if w < 0: w = w2
            else:     w = min(w,w2)
            # g.trace('w',w)
    if w <= 0: return s

    # Remove the leading whitespace.
    result = [g.removeLeadingWhitespace(line,w,tab_width) for line in lines]
    result = ''.join(result)

    return result
#@-node:AGP.20250415230112.1718:g.adjustTripleString (same as removeExtraLws)
#@+node:AGP.20250415230112.1719:computeLeadingWhitespace
# Returns optimized whitespace corresponding to width with the indicated tab_width.

def computeLeadingWhitespace (width, tab_width):

    if width <= 0:
        return ""
    if tab_width > 1:
        tabs   = width / tab_width
        blanks = width % tab_width
        return ('\t' * tabs) + (' ' * blanks)
    else: # 7/3/02: negative tab width always gets converted to blanks.
        return (' ' * width)
#@-node:AGP.20250415230112.1719:computeLeadingWhitespace
#@+node:AGP.20250415230112.1720:computeWidth
# Returns the width of s, assuming s starts a line, with indicated tab_width.

def computeWidth (s, tab_width):
        
    w = 0
    for ch in s:
        if ch == '\t':
            w += (abs(tab_width) - (w % abs(tab_width)))
        else:
            w += 1
    return w
#@-node:AGP.20250415230112.1720:computeWidth
#@+node:AGP.20250415230112.1721:get_leading_ws
def get_leading_ws(s):
    
    """Returns the leading whitespace of 's'."""

    i = 0 ; n = len(s)
    while i < n and s[i] in (' ','\t'):
        i += 1
    return s[0:i]
#@-node:AGP.20250415230112.1721:get_leading_ws
#@+node:AGP.20250415230112.1722:optimizeLeadingWhitespace
# Optimize leading whitespace in s with the given tab_width.

def optimizeLeadingWhitespace (line,tab_width):

    i, width = g.skip_leading_ws_with_indent(line,0,tab_width)
    s = g.computeLeadingWhitespace(width,tab_width) + line[i:]
    return s
#@-node:AGP.20250415230112.1722:optimizeLeadingWhitespace
#@+node:AGP.20250415230112.1723:regularizeTrailingNewlines
#@+at
# 
# The caller should call g.stripBlankLines before calling this routine if 
# desired.
# 
# This routine does _not_ simply call rstrip(): that would delete all trailing 
# whitespace-only lines, and in some cases that would change the meaning of 
# program or data.
# 
#@-at
#@@c

def regularizeTrailingNewlines(s,kind):
    
    """Kind is 'asis', 'zero' or 'one'."""
    
    pass
#@-node:AGP.20250415230112.1723:regularizeTrailingNewlines
#@+node:AGP.20250415230112.1724:removeLeadingWhitespace
# Remove whitespace up to first_ws wide in s, given tab_width, the width of a tab.

def removeLeadingWhitespace (s,first_ws,tab_width):

    j = 0 ; ws = 0
    for ch in s:
        if ws >= first_ws:
            break
        elif ch == ' ':
            j += 1 ; ws += 1
        elif ch == '\t':
            j += 1 ; ws += (abs(tab_width) - (ws % abs(tab_width)))
        else: break
    if j > 0:
        s = s[j:]
    return s
#@-node:AGP.20250415230112.1724:removeLeadingWhitespace
#@+node:AGP.20250415230112.1725:g.removeExtraLws & tests
def removeExtraLws (s,tab_width):
    
    '''Remove extra indentation from one or more lines.
    
    Warning: used by getScript.  This is *not* the same as g.adjustTripleString.'''
    
    lines = g.splitLines(s)

    # Find the first non-blank line and compute w, the width of its leading whitespace.
    for s in lines:
       if s.strip():
            lws = g.get_leading_ws(s)
            w = g.computeWidth(lws,tab_width)
            # g.trace('w',w)
            break
    else: return s
    
    # Remove the leading whitespace.
    result = [g.removeLeadingWhitespace(line,w,tab_width) for line in lines]
    result = ''.join(result)
    
    if 0:
        g.trace('lines...')
        for line in g.splitLines(result):
            print repr(line)

    return result
#@+node:AGP.20250415230112.1726:test_g_removeExtraLws
def test_g_removeExtraLws():
    
    for s,expected in (
        (' a\n b\n c', 'a\nb\nc'),
        (' \n  A\n    B\n  C\n', '\nA\n  B\nC\n'),
    ):
        result = g.removeExtraLws(s,c.tab_width)
        assert result == expected, '\ns: %s\nexpected: %s\nresult:   %s' % (
            repr(s),repr(expected),repr(result))
#@-node:AGP.20250415230112.1726:test_g_removeExtraLws
#@-node:AGP.20250415230112.1725:g.removeExtraLws & tests
#@+node:AGP.20250415230112.1727:removeTrailingWs
# Warning: string.rstrip also removes newlines!

def removeTrailingWs(s):

    j = len(s)-1
    while j >= 0 and (s[j] == ' ' or s[j] == '\t'):
        j -= 1
    return s[:j+1]
#@-node:AGP.20250415230112.1727:removeTrailingWs
#@+node:AGP.20250415230112.1728:skip_leading_ws
# Skips leading up to width leading whitespace.

def skip_leading_ws(s,i,ws,tab_width):

    count = 0
    while count < ws and i < len(s):
        ch = s[i]
        if ch == ' ':
            count += 1
            i += 1
        elif ch == '\t':
            count += (abs(tab_width) - (count % abs(tab_width)))
            i += 1
        else: break

    return i
#@-node:AGP.20250415230112.1728:skip_leading_ws
#@+node:AGP.20250415230112.1729:skip_leading_ws_with_indent
def skip_leading_ws_with_indent(s,i,tab_width):

    """Skips leading whitespace and returns (i, indent), 
    
    - i points after the whitespace
    - indent is the width of the whitespace, assuming tab_width wide tabs."""

    count = 0 ; n = len(s)
    while i < n:
        ch = s[i]
        if ch == ' ':
            count += 1
            i += 1
        elif ch == '\t':
            count += (abs(tab_width) - (count % abs(tab_width)))
            i += 1
        else: break

    return i, count
#@-node:AGP.20250415230112.1729:skip_leading_ws_with_indent
#@+node:AGP.20250415230112.1730:stripBlankLines
def stripBlankLines(s):
    
    lines = g.splitLines(s)

    for i in xrange(len(lines)):

        line = lines[i]
        j = g.skip_ws(line,0)
        if j >= len(line):
            lines[i] = ''
            # g.trace("%4d %s" % (i,repr(lines[i])))
        elif line[j] == '\n':
            lines[i] = '\n'
            # g.trace("%4d %s" % (i,repr(lines[i])))
            
    return ''.join(lines)
#@-node:AGP.20250415230112.1730:stripBlankLines
#@-node:AGP.20250415230112.1717:Whitespace...
#@+node:AGP.20250415230112.1731:ZODB support
#@+node:AGP.20250415230112.1732:g.init_zodb
init_zodb_import_failed = False
init_zodb_failed = {} # Keys are paths, values are True.
init_zodb_db = {} # Keys are paths, values are ZODB.DB instances.

def init_zodb (pathToZodbStorage,verbose=True):
    
    '''Return an ZODB.DB instance from ZODB.FileStorage.FileStorage(pathToZodbStorage)
    return None on any error.'''
    
    global init_zodb_db, init_zodb_failed, init_zodb_import_failed
    
    db = init_zodb_db.get(pathToZodbStorage)
    if db: return db
    
    if init_zodb_import_failed: return None

    failed = init_zodb_failed.get(pathToZodbStorage)
    if failed: return None

    try:
        import ZODB
    except ImportError:
        if verbose:
            g.es('g.init_zodb: can not import ZODB')
            g.es_exception()
        init_zodb_import_failed = True
        return None
    
    try:
        storage = ZODB.FileStorage.FileStorage(pathToZodbStorage)
        init_zodb_db [pathToZodbStorage] = db = ZODB.DB(storage)
        return db
    except Exception:
        if verbose:
            g.es('g.init_zodb: exception creating ZODB.DB instance')
            g.es_exception()
        init_zodb_failed [pathToZodbStorage] = True
        return None
#@nonl
#@-node:AGP.20250415230112.1732:g.init_zodb
#@-node:AGP.20250415230112.1731:ZODB support
#@-others


#import leoApp
#print "leoglobals import",app
#@nonl
#@-node:AGP.20250415230112.1384:@thin leoGlobals.py
#@-leo
