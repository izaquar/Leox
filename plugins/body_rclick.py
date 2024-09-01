#@+leo-ver=4-thin
#@+node:AGP.20230208000543:@thin body_rclick.py
"""Create a context menu when right-clicking in the body pane."""

#@<< version history >>
#@+node:AGP.20230208000543.1:<< version history >>
#@+at
# 0.1, 0.2: Created by 'e'.
# 0.3 EKR:
#     - Converted to 4.2 code style. Use @file node.
#     - Simplified rClickBinder, rClicker, rc_help.  Disabled signon.
#     - Removed calls to registerHandler, "by" ivar, rClickNew, and shutdown 
# code.
#     - Added select all item for the log pane.
# 0.4 Maxim Krikun:
#     - added context-dependent commands:
#        open url, jump to reference, pydoc help
#     - replaced rc_help with context-dependent pydoc help;
#     - rc_help was not working for me :(
# 0.5 EKR:
#     - Style changes.
#     - Help sends output to console as well as log pane.
#     - Used code similar to rc_help code in getdoc.
#       Both kinds of code work for me (using 4.2 code base)
#     - Simplified crop method.
# 0.6 EKR:
#     - Use g.importExtension to import Tk.
# 0.7 EKR:
#     - Use e.widget._name.startswith('body') to test for the body pane.
# 0.8 EKR:
# - Added init function.
# - Eliminated g.top.
# 0.9 EKR:
# - Define callbacks so that all are accessible.
# 0.10 EKR:
# - Removed call to str that was causing a unicode error.
# 
# 
# 0.10exe AGP:
#     -changed stuff and renamed
#@-at
#@nonl
#@-node:AGP.20230208000543.1:<< version history >>
#@nl
#@<< imports >>
#@+node:AGP.20230208000543.2:<< imports >>
import leoGlobals as g
import leoPlugins

Tk = g.importExtension('Tkinter')

import re
import sys


#@-node:AGP.20230208000543.2:<< imports >>
#@nl
__version__ = "0.10"

#@+others
#@+node:AGP.20230216112815:notes
#@+at
# c.frame.body.colorizer.c_keywords = []
#@-at
#@nonl
#@-node:AGP.20230216112815:notes
#@+node:AGP.20230208000543.4:init
def init ():
    
    if Tk: # OK for unit tests.
    
        if g.app.gui is None:
            g.app.createTkGui(__file__)
    
        if g.app.gui.guiName() == "tkinter":
            leoPlugins.registerHandler("after-create-leo-frame",rClickbinder)
            leoPlugins.registerHandler("bodyrclick1",on_right_click)
            g.plugin_signon(__name__)
            
    return Tk is not None
#@nonl
#@-node:AGP.20230208000543.4:init
#@+node:AGP.20230208000543.5:rClickbinder
def rClickbinder(tag,keywords):

    c = keywords.get('c')
    
    if c and c.exists:
        c.frame.log.logCtrl.bind  ('<Button-3>',c.frame.OnBodyRClick)
        # c.frame.body.bodyCtrl.bind('<Button-3>',c.frame.OnBodyRClick)
#@nonl
#@-node:AGP.20230208000543.5:rClickbinder
#@+node:AGP.20230208000543.6:on_right_click()
# EKR: it is not necessary to catch exceptions or to return "break".

def on_right_click(tag,keywords):
    
    c = keywords.get("c")
    e = keywords.get("event")
    if not c or not c.exists or not e: return

    e.widget.focus()
    
    
    
    
    if e.widget._name.startswith('body'):
        #@        << define commandList for body >>
        #@+node:AGP.20230208000543.8:<< define commandList for body >>
        commandList = [
            #('-||-|-||-',None),   #
            #('U',c.undoer.undo),  #no c.undoer
            #('R',undoer.redo),
            # ('-',None),
            #('Cut', c.frame.OnCutFromMenu),
            ('Cut', lambda e=e:c.frame.cutText(e)),
            ('Copy', lambda e=e:c.frame.copyText(e)),
            ('Paste',lambda e=e:c.frame.pasteText(e)),
            ('Swap',lambda e=e:c.frame.swapText(e)),
            ('Delete',lambda c=c:brc_delete(c)),
            ('-',None),
            ('SelectAll',c.frame.body.selectAllText),
            ('-',None),
            ('Indent',c.indentBody),
            ('Unindent',c.dedentBody)
            #('-',None),
            #('Find Bracket',c.findMatchingBracket),
            #('Insert newline', rc_nlCallback),
            
            # this option seems not working, at least in win32
            # replaced with context-sensitive "pydoc help"  --Maxim Krikun
            # ('Help(txt)',rc_helpCallback),   #how to highlight 'txt' in the menu?
            
            #('Execute Script',c.executeScript)
            # ('-||-|-||-',None),   # 1st & last needed because of freaky sticky finger
            ]
        #@nonl
        #@-node:AGP.20230208000543.8:<< define commandList for body >>
        #@nl
        if g.scanDirectives(c)["language"] == "python":
            commandList.append(('-',None))
            commandList.append(('Execute Script',c.executeScript))
        #@        << add entries for context sensitive commands in body >>
        #@+node:AGP.20230208000543.9:<< add entries for context sensitive commands in body >>
        #@+at 
        #@nonl
        # Context-sensitive rclick commands.
        # 
        # On right-click get the selected text, or the whole line containing 
        # cursor if no selection.
        # Scan this text for certain regexp pattern. For each occurrence of a 
        # pattern add a command,
        # which name and action depend on the text matched.
        # 
        # Example below extracts URL's from the text and puts "Open URL:..." 
        # th menu.
        # 
        #@-at
        #@@c
        
        #@<< get text and word from the body text >>
        #@+node:AGP.20230208000543.10:<< get text and word from the body text >>
        text = c.frame.body.getSelectedText()
        if text:
            word = text.strip()
        else:
            ind0,ind1=c.frame.body.getTextSelection()
            n0,p0=ind0.split('.',2)
            n1,p1=ind1.split('.',2)
            assert n0==n1
            assert p0==p1
            text=c.frame.body.getTextRange(n0+".0",n1+".end")
            word=getword(text,int(p0))
        #@nonl
        #@-node:AGP.20230208000543.10:<< get text and word from the body text >>
        #@nl
        
        if 0:
            g.es("selected text: "+text)
            g.es("selected word: "+repr(word))
        
        contextCommands=[]
        
        #@<< add entry for jump to section >>
        #@+node:AGP.20230208000543.12:<< add entry for jump to section >>
        scan_jump_re="<"+"<[^<>]+>"+">"
        
        p=c.currentPosition()
        for match in re.finditer(scan_jump_re,text):
            name=match.group()
            ref=g.findReference(c,name,p)
            if ref:
                # Bug fix 1/8/06: bind c here.
                # This is safe because we only get called from the proper commander.
                def jump_command(c=c,*k,**kk):
                    c.beginUpdate()
                    c.selectPosition(ref)
                    c.endUpdate()
                menu_item=( 'Jump to: '+crop(name,30), jump_command)
                contextCommands.append( menu_item )
            else:
                # could add "create section" here?
                pass
        #@nonl
        #@-node:AGP.20230208000543.12:<< add entry for jump to section >>
        #@nl
        
        
        if contextCommands:
            commandList.append(("-",None))
            commandList.extend(contextCommands)
        #@nonl
        #@-node:AGP.20230208000543.9:<< add entries for context sensitive commands in body >>
        #@nl
    else:
        #@        << define commandList for log pane >>
        #@+node:AGP.20230208000543.14:<< define commandList for log pane >>
        commandList=[
            #('Cut', c.frame.OnCutFromMenu), 
            ('Copy',c.frame.OnCopyFromMenu),
            #('Paste', c.frame.OnPasteFromMenu),
            #('Select All', rc_selectAllCallback)
            ]
        #@nonl
        #@-node:AGP.20230208000543.14:<< define commandList for log pane >>
        #@nl
                
    rmenu = Tk.Menu(None,tearoff=0,takefocus=0)
    for (txt,cmd) in commandList:
        if txt == '-':
            rmenu.add_separator()
        else:
            rmenu.add_command(label=txt,command=cmd)

    #rmenu.tk_popup(e.x_root-23,e.y_root+13)
    rmenu.tk_popup(e.x_root+1,e.y_root-10)
    #rmenu.post(e.x_root+1,e.y_root-10)
    
    return False
#@nonl
#@-node:AGP.20230208000543.6:on_right_click()
#@+node:AGP.20230208000543.16:brc_delete()
def brc_delete(c):

    if c.frame.body.hasTextSelection():
        c.frame.body.deleteTextSelection()
        c.frame.body.onBodyChanged("Delete")
#@nonl
#@-node:AGP.20230208000543.16:brc_delete()
#@+node:AGP.20230208000543.19:Utils for context sensitive commands
#@+node:AGP.20230208000543.20:crop
def crop(s,n=20,end="..."):

    """return a part of string s, no more than n characters; optionally add ... at the end"""
    
    if len(s)<=n:
        return s
    else:
        return s[:n]+end # EKR
#@nonl
#@-node:AGP.20230208000543.20:crop
#@+node:AGP.20230208000543.21:getword
def getword(s,pos):

    """returns a word in string s around position pos"""

    for m in re.finditer("\w+",s):
        if m.start()<=pos and m.end()>=pos:
            return m.group()
    return None			
#@-node:AGP.20230208000543.21:getword
#@+node:AGP.20230208000543.22:getdoc
def getdoc(thing, title='Help on %s', forceload=0):
    
    #g.trace(thing)

    if 1: # Both seem to work.

        # Redirect stdout to a "file like object".
        old_stdout = sys.stdout
        sys.stdout = fo = g.fileLikeObject()
        # Python's builtin help function writes to stdout.
        help(str(thing))
        # Restore original stdout.
        sys.stdout = old_stdout
        # Return what was written to fo.
        return fo.get()

    else:
        # Similar to doc function from pydoc module.
        from pydoc import resolve, describe, inspect, text, plain
        object, name = resolve(thing, forceload)
        desc = describe(object)
        module = inspect.getmodule(object)
        if name and '.' in name:
            desc += ' in ' + name[:name.rfind('.')]
        elif module and module is not object:
            desc += ' in module ' + module.__name__
        doc = title % desc + '\n\n' + text.document(object, name)
        return plain(doc)
#@nonl
#@-node:AGP.20230208000543.22:getdoc
#@-node:AGP.20230208000543.19:Utils for context sensitive commands
#@-others
#@nonl
#@-node:AGP.20230208000543:@thin body_rclick.py
#@-leo
