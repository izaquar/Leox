#@+leo-ver=4-thin
#@+node:AGP.20250415230112.1893:@thin leoKeys.py
"""Gui-independent keystroke handling for Leo.""" 

#@@language python
#@@tabwidth -4
#@@pagewidth 80

#@<< imports >>
#@+node:AGP.20250415230112.1894:<< imports >>
import leoGlobals as g
import leoEditCommands #agp cmd
import leo

import Tkinter as Tk


import glob
import inspect
import os
import re
import string
import sys
import types

# The following imports _are_ used.
import compiler
import parser
#@-node:AGP.20250415230112.1894:<< imports >>
#@nl
#@<< about 'internal' bindings >>
#@+node:AGP.20250415230112.1895:<< about 'internal' bindings >>
#@@nocolor
#@+at
# 
# Here are the rules for translating key bindings (in leoSettings.leo) into 
# keys for k.bindingsDict:
# 
# 1.  The case of plain letters is significant:  a is not A.
# 
# 2.  The Shift- prefix can be applied *only* to letters.  Leo will ignore 
# (with a warning) the shift prefix applied to any other binding, e.g., 
# Ctrl-Shift-(
# 
# 3.  The case of letters prefixed by Ctrl-, Alt-, Key- or Shift- is *not* 
# significant.  Thus, the Shift- prefix is required if you want an upper-case 
# letter (with the exception of 'bare' uppercase letters.)
# 
# The following table illustrates these rules.  In each row, the first entry 
# is the key (for k.bindingsDict) and the other entries are equivalents that 
# the user may specify in leoSettings.leo:
# 
# a, Key-a, Key-A
# A, Shift-A
# Alt-a, Alt-A
# Alt-A, Alt-Shift-a, Alt-Shift-A
# Ctrl-a, Ctrl-A
# Ctrl-A, Ctrl-Shift-a, Ctrl-Shift-A
# !, Key-!,Key-exclam,exclam
# 
# This table is consistent with how Leo already works (because it is 
# consistent with Tk's key-event specifiers).  It is also, I think, the least 
# confusing set of rules.
#@-at
#@-node:AGP.20250415230112.1895:<< about 'internal' bindings >>
#@nl
#@<< about key dicts >>
#@+node:AGP.20250415230112.1896:<< about key dicts >>
#@@nocolor
#@+at
# 
# ivars:
# 
# c.commandsDict:
#     Keys are emacs command names; values are functions f.
# 
# k.inverseCommandsDict:
#     Keys are f.__name__; values are emacs command names.
# 
# k.bindingsDict:
#     Keys are shortcuts; values are *lists* of 
# g.bunch(func,name,warningGiven)
# 
# k.masterBindingsDict:
#     Keys are scope names: 'all','text',etc. or mode names.
#     Values are dicts:  keys are strokes, values are 
# g.Bunch(commandName,func,pane,stroke)
# 
# k.masterGuiBindingsDict:
#     Keys are strokes; value is a list of widgets for which stroke is bound.
# 
# k.settingsNameDict:
#     Keys are lowercase settings; values are 'real' Tk key specifiers.
#     Important: this table has no inverse.
# 
# not an ivar (computed by k.computeInverseBindingDict):
# 
# inverseBindingDict
#     Keys are emacs command names; values are *lists* of shortcuts.
#@-at
#@-node:AGP.20250415230112.1896:<< about key dicts >>
#@nl

#@+others
#@+node:AGP.20250415230112.1897:class autoCompleterClass
class autoCompleterClass:
    
    '''A class that inserts autocompleted and calltip text in text widgets.
    This class shows alternatives in the tabbed log pane.
    
    The keyHandler class contains hooks to support these characters:
    invoke-autocompleter-character (default binding is '.')
    invoke-calltips-character (default binding is '(')
    '''

    #@    @+others
    #@+node:AGP.20250415230112.1898: ctor (autocompleter)
    def __init__ (self,k):
        
        self.c = c = k.c
        self.k = k
        self.allClassesDict = {} # Will be completed after more classes exist.
        self.attrDictDict = {}  # Keys are languages (strings); values are anonymous attrDicts.
            # attrDicts: keys are strings; values are list of strings (attributes).
        self.calltips = {} # Keys are language, values are dicts: keys are ids, values are signatures.
        self.classScanner = self.classScannerClass(c)
        self.forgivingParser = self.forgivingParserClass(c)
        self.globalPythonFunctionsDict = {}
        self.language = None
        self.leadinWord = None
        self.membersList = None
        self.objectDict = {} # Created on first use of the autocompleter.
        self.selection = None # The selection range on entry to autocompleter or calltips.
        self.selectedText = None # The selected text on entry to autocompleter or calltips.
        self.selfClassName = None
        self.selfObjectsDict = {} # Keys are classNames, values are real proxy objects.
        self.selfTnodesDict = {} # Keys are tnodes, values are real proxy objects.
        self.prefix = None
        self.prevObjects = []
        self.tabList = []
        self.tabListIndex = -1
        self.tabName = None # The name of the main completion tab.
        self.object = None # The previously found object, for . chaining.
        self.trace = c.config.getBool('trace_autocompleter')
        self.verbose = False # True: print all members.
        self.watchwords = {} # Keys are ids, values are lists of ids that can follow a id dot.
        self.widget = None # The widget that should get focus after autocomplete is done.
    #@+node:AGP.20250415230112.1899:defineClassesDict
    def defineClassesDict (self):
        
        self.allClassesDict = {}
        
        # gc may not exist.
        try: import gc
        except ImportError: return
    
        for z in gc.get_objects():
            t = type(z)
            if t == types.ClassType:
                name = z.__name__
            elif t == types.InstanceType:
                name = z.__class__.__name__
            elif repr(t).startswith('<class'): # A wretched kludge.
                name = z.__class__.__name__
            elif t == types.TypeType:
                name = z.__name__
            else:
                name = None
            if name:
                # if name == 'position': g.trace(t,z)
                self.allClassesDict [name] = z
            
        # g.printList(self.allClassesDict.keys(),tag='Classes',sort=True)
        # g.trace(len(self.allClassesDict.keys()))
        # g.trace('position:',self.allClassesDict.get('position'))
    #@-node:AGP.20250415230112.1899:defineClassesDict
    #@+node:AGP.20250415230112.1900:defineObjectDict
    def defineObjectDict (self):
        
        c = self.c ; k = c.k ; p = c.currentPosition()
    
        table = [
            # Python globals...
            (['aList','bList'],     'python','list'),
            (['aString'],           'object','aString'),    # An actual string object.
            (['c','old_c','new_c'], 'object',c),            # 'leoCommands','Commands'),
            (['d','d1','d2'],       'python','dict'),
            (['f'],                 'object',c.frame), # 'leoTkinterFrame','leoTkinterFrame'),
            (['g'],                 'object',g),       # 'leoGlobals',None),
            (['p','p1','p2'],       'object',p),       # 'leoNodes','position'),         
            (['s','s1','s2','ch'],  'object','aString'),
            (['string'],            'object',string),     # Python's string module.
            (['t','t1','t2'],       'object',p.v.t),   # 'leoNodes','tnode'),  
            (['v','v1','v2'],       'object',p.v),     # 'leoNodes','vnode'),
            (['w','widget'],        'Tkinter','Text'),
        ]
        
        if 0: # Not useful at this point.
            for key in __builtins__.keys():
                obj = __builtins__.get(key)
                if obj in (True,False,None): continue
                data = [key],'object',obj
                table.append(data)
        
        d = {'dict':{},'int':1,'list':[],'string':''}
    
        for idList,kind,nameOrObject in table:
            if kind == 'object':
                # Works, but hard to generalize for settings.
                obj = nameOrObject
            elif kind == 'python':
                className = nameOrObject
                o = d.get(className)
                obj = o is not None and o.__class__
            else:
                module = g.importModule (kind,verbose=True)
                if not module:
                    g.trace('Can not import ',nameOrObject)
                    continue
                self.appendToKnownObjects(module)
                if nameOrObject:
                    className = nameOrObject
                    obj = hasattr(module,className) and getattr(module,className) or None
                    if not obj:
                        g.trace('%s module has no class %s' % (kind,nameOrObject))
                    else:
                        self.appendToKnownObjects(getattr(module,className))
                else:
                    obj = module
            if not obj:
                g.trace('bad object',obj)
                continue
            for z in idList:
                self.objectDict[z]=obj
                # g.trace(obj)
    #@-node:AGP.20250415230112.1900:defineObjectDict
    #@-node:AGP.20250415230112.1898: ctor (autocompleter)
    #@+node:AGP.20250415230112.1901:Top level
    #@+node:AGP.20250415230112.1902:autoComplete
    def autoComplete (self,event=None,force=False):
        
        '''An event handler called from k.masterKeyHanderlerHelper.'''
    
        c = self.c ; k = self.k
        w = event and event.widget or c.get_focus()
    
        # First, handle the invocation character as usual.
        k.masterCommand(event,func=None,stroke=None,commandName=None)
        
        # Don't allow autocompletion in headlines.
        if not c.widget_name(w).startswith('head'):
            self.language = g.scanForAtLanguage(c,c.currentPosition())
            if w and self.language == 'python' and (k.enable_autocompleter or force):
                self.start(event=event,w=w)
    
        return 'break'
    #@-node:AGP.20250415230112.1902:autoComplete
    #@+node:AGP.20250415230112.1903:autoCompleteForce
    def autoCompleteForce (self,event=None):
        
        '''Show autocompletion, even if autocompletion is not presently enabled.'''
        
        return self.autoComplete(event,force=True)
    #@-node:AGP.20250415230112.1903:autoCompleteForce
    #@+node:AGP.20250415230112.1904:autoCompleterStateHandler
    def autoCompleterStateHandler (self,event):
        
        c = self.c ; k = self.k
        tag = 'auto-complete' ; state = k.getState(tag)
        keysym = event and event.keysym
        ch = event and event.char or ''
        trace = self.trace and not g.app.unitTesting
        if trace: g.trace(repr(ch),repr(keysym),state)
    
        if state == 0:
            c.frame.log.clearTab(self.tabName)
            self.computeCompletionList()
            k.setState(tag,1,handler=self.autoCompleterStateHandler) 
        elif keysym in ('space','Return'):
            self.finish()
        elif keysym == 'Escape':
            self.abort()
        elif keysym == 'Tab':
            self.doTabCompletion()
        elif keysym == 'BackSpace':
            self.doBackSpace()
        elif keysym == 'period':
            self.chain()
        elif keysym == 'question':
            self.info()
        elif keysym == 'exclam':
            # Toggle between verbose and brief listing.
            self.verbose = not self.verbose
            if type(self.object) == types.DictType:
                self.membersList = self.object.keys()
            elif type(self.object) in (types.ListType,types.TupleType):
                self.membersList = self.object
            self.computeCompletionList(verbose=self.verbose)
        elif ch and ch in string.printable:
            self.insertNormalChar(ch,keysym)
        else:
            if trace: g.trace('ignore',repr(ch))
            return 'do-standard-keys'
    #@-node:AGP.20250415230112.1904:autoCompleterStateHandler
    #@+node:AGP.20250415230112.1905:enable/disable/toggleAutocompleter/Calltips
    def disableAutocompleter (self,event=None):
        '''Disable the autocompleter.'''
        self.k.enable_autocompleter = False
        self.showAutocompleterStatus()
        
    def disableCalltips (self,event=None):
        '''Disable calltips.'''
        self.k.enable_calltips = False
        self.showCalltipsStatus()
        
    def enableAutocompleter (self,event=None):
        '''Enable the autocompleter.'''
        self.k.enable_autocompleter = True
        self.showAutocompleterStatus()
        
    def enableCalltips (self,event=None):
        '''Enable calltips.'''
        self.k.enable_calltips = True
        self.showCalltipsStatus()
        
    def toggleAutocompleter (self,event=None):
        '''Toggle whether the autocompleter is enabled.'''
        self.k.enable_autocompleter = not self.k.enable_autocompleter
        self.showAutocompleterStatus()
        
    def toggleCalltips (self,event=None):
        '''Toggle whether calltips are enabled.'''
        self.k.enable_calltips = not self.k.enable_calltips
        self.showCalltipsStatus()
    #@-node:AGP.20250415230112.1905:enable/disable/toggleAutocompleter/Calltips
    #@+node:AGP.20250415230112.1906:showCalltips
    def showCalltips (self,event=None,force=False):
        
        '''Show the calltips at the cursor.'''
        
        c = self.c ; k = c.k
        
        w = event and event.widget or c.get_focus()
        
        # Insert the calltip if possible, but not in headlines.
        if (k.enable_calltips or force) and not c.widget_name(w).startswith('head'):
            self.widget = w
            self.prefix = ''
            self.selection = g.app.gui.getTextSelection(w)
            self.selectedText = g.app.gui.getSelectedText(w)
            self.leadinWord = self.findCalltipWord(w)
            self.object = None
            self.membersList = None
            self.calltip()
        else:
            # Just insert the invocation character as usual.
            k.masterCommand(event,func=None,stroke=None,commandName=None)
            
        return 'break'
    #@-node:AGP.20250415230112.1906:showCalltips
    #@+node:AGP.20250415230112.1907:showCalltipsForce
    def showCalltipsForce (self,event=None):
        
        '''Show the calltips at the cursor, even if calltips are not presently enabled.'''
        
        return self.showCalltips(event,force=True)
    #@-node:AGP.20250415230112.1907:showCalltipsForce
    #@+node:AGP.20250415230112.1908:showAutocompleter/CalltipsStatus
    def showAutocompleterStatus (self):
        '''Show the autocompleter status on the status line.'''
        
        k = self.k
        
        if 1:
            g.es('Autocompleter %s' % (g.choose(k.enable_autocompleter,'On','Off')),color='red')
        else:
            frame = k.c.frame
            frame.clearStatusLine()
            frame.putStatusLine('Autocompleter ',color='blue')
            frame.putStatusLine(g.choose(k.enable_autocompleter,'On','Off'))
        
    def showCalltipsStatus (self):
        '''Show the autocompleter status on the status line.'''
        k = self.k
        if 1:
            g.es('Calltips %s' % (g.choose(k.enable_calltips,'On','Off')),color='red')
        else:
            frame = k.c.frame
            frame.clearStatusLine()
            frame.putStatusLine('Calltips ',color='blue')
            frame.putStatusLine(g.choose(k.enable_calltips,'On','Off'))
    #@nonl
    #@-node:AGP.20250415230112.1908:showAutocompleter/CalltipsStatus
    #@-node:AGP.20250415230112.1901:Top level
    #@+node:AGP.20250415230112.1909:Helpers
    #@+node:AGP.20250415230112.1910:abort & exit
    def abort (self):
        
        k = self.k
        k.keyboardQuit(event=None)
        self.exit(restore=True)
    
    def exit (self,restore=False): # Called from keyboard-quit.
        
        c = self.c ; w = self.widget
        for name in (self.tabName,'Modules','Info'):
            c.frame.log.deleteTab(name)
        c.widgetWantsFocusNow(w)
        i,j = g.app.gui.getTextSelection(w)
        if restore:
            w.delete(i,j)
            w.insert(i,self.selectedText)
        g.app.gui.setTextSelection(w,j,j,insert=j)
        
        self.clear()
        self.object = None
    #@-node:AGP.20250415230112.1910:abort & exit
    #@+node:AGP.20250415230112.1911:append/begin/popTabName
    def appendTabName (self,word):
        
        self.setTabName(self.tabName + word + '.')
    
    def beginTabName (self,word):
    
        # g.trace(word,g.callers())
        if word == 'self' and self.selfClassName:
            word = '%s (%s)' % (word,self.selfClassName)
        self.setTabName('AutoComplete ' + word + '.')
        
    def clearTabName (self):
        
        self.setTabName('AutoComplete ')
        
    def popTabName (self):
        
        s = self.tabName
        i = s.rfind('.',0,-1)
        if i > -1:
            self.setTabName(s[0:i])
        
    # Underscores are not valid in Pmw tab names!
    def setTabName (self,s):
    
        c = self.c
        if self.tabName:
            c.frame.log.deleteTab(self.tabName)
        self.tabName = s.replace('_','') or ''
        c.frame.log.clearTab(self.tabName)
    #@-node:AGP.20250415230112.1911:append/begin/popTabName
    #@+node:AGP.20250415230112.1912:appendToKnownObjects
    def appendToKnownObjects (self,obj):
        
        if 0:
            if type(obj) in (types.InstanceType,types.ModuleType,types):
                if hasattr(obj,'__name__'):
                    self.knownObjects[obj.__name__] = obj
                    # g.trace('adding',obj.__name__)
    #@-node:AGP.20250415230112.1912:appendToKnownObjects
    #@+node:AGP.20250415230112.1913:calltip
    def calltip (self,obj=None):
        
        c = self.c ; w = self.widget
        isStringMethod = False ; s = None
        # g.trace(self.leadinWord,obj)
    
        if self.leadinWord and (not obj or type(obj) == types.BuiltinFunctionType):
            #@        << try to set s from a Python global function >>
            #@+node:AGP.20250415230112.1914:<< try to set s from a Python global function >>
            # The first line of the docstring is good enough, except for classes.
            f = __builtins__.get(self.leadinWord)
            doc = f and type(f) != types.ClassType and f.__doc__
            if doc:
                # g.trace(doc)
                s = g.splitLines(doc)
                s = args = s and s [0] or ''
                i = s.find('(')
                if i > -1: s = s [i:]
                else: s = '(' + s
                s = s and s.strip() or ''
            #@-node:AGP.20250415230112.1914:<< try to set s from a Python global function >>
            #@nl
    
        if not s:
            #@        << get s using inspect >>
            #@+node:AGP.20250415230112.1915:<< get s using inspect >>
            isStringMethod = self.prevObjects and type(self.prevObjects[-1]) == types.StringType
            
            # g.trace(self.prevObjects)
            
            if isStringMethod and hasattr(string,obj.__name__):
                # A hack. String functions are builtins, and getargspec doesn't handle them.
                # Get the corresponding string function instead, and remove the s arg later.
                obj = getattr(string,obj.__name__)
            
            try:
                s1,s2,s3,s4 = inspect.getargspec(obj)
            except:
                # g.es('inspect failed:',repr(obj))
                self.extendSelection('(')
                self.finish()
                return # Not a function.  Just '('.
            
            s = args = inspect.formatargspec(s1,s2,s3,s4)
            #@-node:AGP.20250415230112.1915:<< get s using inspect >>
            #@nl
            
        #@    << remove 'self' from s, but not from args >>
        #@+node:AGP.20250415230112.1916:<< remove 'self' from s, but not from args >>
        if g.match(s,1,'self,'):
            s = s[0] + s[6:].strip()
        elif g.match_word(s,1,'self'):
            s = s[0] + s[5:].strip()
        #@-node:AGP.20250415230112.1916:<< remove 'self' from s, but not from args >>
        #@nl
        if isStringMethod:
            #@        << remove 's' from s *and* args >>
            #@+node:AGP.20250415230112.1917:<< remove 's' from s *and* args >>
            if g.match(s,1,'s,'):
                s = s[0] + s[3:]
                args = args[0] + args[3:]
            elif g.match_word(s,1,'s'):
                s = s[0] + s[2:]
                args = args[0] + args[2:]
            #@-node:AGP.20250415230112.1917:<< remove 's' from s *and* args >>
            #@nl
    
        s = s.rstrip(')') # Convenient.
        #@    << insert the text and set j1 and j2 >>
        #@+node:AGP.20250415230112.1918:<< insert the text and set j1 and j2 >>
        if g.app.gui.hasSelection(w):
            i,j = g.app.gui.getSelectionRange(w)
        else:
            i = j = g.app.gui.getInsertPoint(w)
        w.insert(j,s)
        c.frame.body.onBodyChanged('Typing')
        
        if 1:
            j1 = w.index('%s + 1c' % j)
            j2 = w.index('%s + %sc' % (j,len(s)))
        else:
            j1 = j2 = w.index('%s + 2c' % j)
        #@-node:AGP.20250415230112.1918:<< insert the text and set j1 and j2 >>
        #@nl
    
        # End autocompletion mode, restoring the selection.
        self.finish()
        c.widgetWantsFocusNow(w)
        g.app.gui.setSelectionRange(w,j1,j2,insert=j2)
        #@    << put the status line >>
        #@+node:AGP.20250415230112.1919:<< put the status line >>
        c.frame.clearStatusLine()
        if obj:
            name = hasattr(obj,'__name__') and obj.__name__ or repr(obj)
        else:
            name = self.leadinWord
        c.frame.putStatusLine('%s %s' % (name,args))
        #@-node:AGP.20250415230112.1919:<< put the status line >>
        #@nl
    #@-node:AGP.20250415230112.1913:calltip
    #@+node:AGP.20250415230112.1920:chain
    def chain (self):
        
        c = self.c ; w = self.widget
        word = g.app.gui.getSelectedText(w)
        old_obj = self.object
    
        if word and old_obj and type(old_obj) == type([]) and old_obj == sys.modules:
            obj = old_obj.get(word)
            if obj:
                self.object = obj
                self.clearTabName()
        elif word and old_obj and self.hasAttr(old_obj,word):
            self.push(old_obj)
            self.object = obj = self.getAttr(old_obj,word)
        else: obj = None
    
        if obj:
            self.appendToKnownObjects(obj)
            self.leadinWord = word
            self.membersList = self.getMembersList(obj)
            self.appendTabName(word)
            self.extendSelection('.')
            i = g.app.gui.getInsertPoint(w)
            g.app.gui.setTextSelection(w,i,i,insert=i)
            # g.trace('chaining to',word,self.object)
            # Similar to start logic.
            self.prefix = ''
            self.selection = g.app.gui.getTextSelection(w)
            self.selectedText = g.app.gui.getSelectedText(w)
            if self.membersList:
                # self.autoCompleterStateHandler(event=None)
                self.computeCompletionList()
                return
        self.extendSelection('.')
        self.finish()
    #@-node:AGP.20250415230112.1920:chain
    #@+node:AGP.20250415230112.1921:computeCompletionList
    def computeCompletionList (self,verbose=False):
        
        c = self.c ; gui = g.app.gui ; w = self.widget
        c.widgetWantsFocus(w)
        s = gui.getSelectedText(w)
        self.tabList,common_prefix = g.itemsMatchingPrefixInList(
            s,self.membersList,matchEmptyPrefix=True)
    
        if not common_prefix:
            if verbose or len(self.tabList) < 25:
                self.tabList,common_prefix = g.itemsMatchingPrefixInList(
                    s,self.membersList,matchEmptyPrefix=True)
            else: # Show the possible starting letters.
                d = {}
                for z in self.tabList:
                    ch = z and z[0] or ''
                    if ch:
                        n = d.get(ch,0)
                        d[ch] = n + 1
                aList = [ch+'...%d' % (d.get(ch)) for ch in d.keys()] ; aList.sort()
                self.tabList = aList
           
        c.frame.log.clearTab(self.tabName) # Creates the tab if necessary.
        if self.tabList:
            self.tabListIndex = -1 # The next item will be item 0.
            self.setSelection(common_prefix)
        for name in self.tabList:
            g.es('%s' % (name),tabName=self.tabName)
    #@-node:AGP.20250415230112.1921:computeCompletionList
    #@+node:AGP.20250415230112.1922:doBackSpace (autocompleter)
    def doBackSpace (self):
    
        '''Cut back to previous prefix.'''
        
        # g.trace(self.prefix,self.object,self.prevObjects)
        
        if self.prefix:
            self.prefix = self.prefix[:-1]
            self.setSelection(self.prefix)
            self.computeCompletionList()
        elif self.object:
            if self.prevObjects:
                obj = self.pop()
            else:
                obj = self.object
            # g.trace(self.object,obj)
            w = self.widget
            i,j = g.app.gui.getTextSelection(w)
            ch = w.get(i+'-1c')
            # g.trace(ch)
            if ch == '.':
                self.object = obj
                w.delete(i+'-1c')
                i = w.index(i+'-1c wordstart')
                j = w.index(i+' wordend')
                word = w.get(i,j)
                g.app.gui.setSelectionRange(w,i,j,insert=j)
                self.prefix = word
                self.popTabName()
                self.membersList = self.getMembersList(obj)
                # g.trace(len(self.membersList))
                if self.membersList:
                    self.computeCompletionList()
                else:
                    self.abort()
            else:
                self.abort() # should not happen.
        else:
            self.abort()
    #@-node:AGP.20250415230112.1922:doBackSpace (autocompleter)
    #@+node:AGP.20250415230112.1923:doTabCompletion
    def doTabCompletion (self):
        
        '''Handle tab completion when the user hits a tab.'''
        
        c = self.c ; gui = g.app.gui ; w = self.widget
        s = gui.getSelectedText(w)
    
        if s.startswith(self.prefix) and self.tabList:
            # g.trace('cycle','prefix',repr(self.prefix),len(self.tabList),repr(s))
            # Set the label to the next item on the tab list.
            self.tabListIndex +=1
            if self.tabListIndex >= len(self.tabList):
               self.tabListIndex = 0
            self.setSelection(self.tabList[self.tabListIndex])
        else:
            self.computeCompletionList()
    
        c.widgetWantsFocusNow(w)
    #@-node:AGP.20250415230112.1923:doTabCompletion
    #@+node:AGP.20250415230112.1924:extendSelection
    def extendSelection (self,s):
        
        c = self.c ; w = self.widget
        c.widgetWantsFocusNow(w)
        
        if g.app.gui.hasSelection(w):
            i,j = g.app.gui.getSelectionRange(w)
        else:
            i = j = g.app.gui.getInsertPoint(w)
        
        w.insert(j,s)
        j = w.index('%s + 1c' % (j))
        g.app.gui.setSelectionRange(w,i,j,insert=j)
        c.frame.body.onBodyChanged('Typing')
    #@-node:AGP.20250415230112.1924:extendSelection
    #@+node:AGP.20250415230112.1925:findAnchor
    def findAnchor (self,w):
        
        i = g.app.gui.getInsertPoint(w)
        
        while w.get(i + '-1c') == '.' and w.compare(i,'>','1.0'):
            i = w.index(i + '-2c wordstart')
    
        j = w.index(i+' wordend')
        word = w.get(i,j)
        
        if word == '.': word = None
        
        # g.trace(i,j,repr(word),w.get(j))
        return j,word
    #@-node:AGP.20250415230112.1925:findAnchor
    #@+node:AGP.20250415230112.1926:findCalltipWord
    def findCalltipWord (self,w):
        
        i = g.app.gui.getInsertPoint(w)
        
        if w.compare(i,'>','1.0'):
            return w.get(i+'-1c wordstart',i+'-1c wordstart wordend')
        else:
            return ''
    #@-node:AGP.20250415230112.1926:findCalltipWord
    #@+node:AGP.20250415230112.1927:finish
    def finish (self):
        
        c = self.c ; k = self.k
        
        k.keyboardQuit(event=None)
        
        for name in (self.tabName,'Modules','Info'):
            c.frame.log.deleteTab(name)
            
        c.frame.body.onBodyChanged('Typing')
        self.clear()
        self.object = None
    #@-node:AGP.20250415230112.1927:finish
    #@+node:AGP.20250415230112.1928:getAttr and hasAttr
    # The values of self.attrDictDic are anonymous attrDict's.
    # attrDicts: keys are strings, values are lists of strings.
    
    def getAttr (self,obj,attr):
        
        '''Simulate getattr function, regardless of langauge.'''
        
        if self.language == 'python':
            return getattr(obj,attr)
        else:
            d = self.attrDictDict.get(self.language)
            aList = d.get(obj,[])
            return attr in aList and attr
    
    def hasAttr (self,obj,attr):
        
        '''Simulate hasattr function, regardless of langauge.'''
    
        if self.language == 'python':
            return hasattr(obj,attr)
        else:
            d = self.attrDictDict.get(self.language)
            aList = d.get(obj,[])
            return attr in aList
    #@-node:AGP.20250415230112.1928:getAttr and hasAttr
    #@+node:AGP.20250415230112.1929:getLeadinWord
    def getLeadinWord (self,w):
        
        self.verbose = False # User must explicitly ask for verbose.
        self.leadinWord = None
        start = g.app.gui.getInsertPoint(w)
        start = w.index(start+'-1c')
        i,word = self.findAnchor(w)
    
        if word and word.isdigit():
            self.membersList = []
            return False
    
        self.setObjectAndMembersList(word)
        
        # g.trace(word,self.object,len(self.membersList))
    
        if not word:
            self.membersList = []
            return False
        elif not self.object:
            self.membersList = []
            return False
        else:
            self.beginTabName(word)
            while w.compare(i,'<',start):
                if w.get(i) != '.':
                    g.trace('oops: %s' % (repr(w.get(i))))
                    return False
                i = w.index(i+'+1c')
                j = w.index(i+' wordend')
                word = w.get(i,j)
                # g.trace(word,i,j,start)
                self.setObjectAndMembersList(word)
                if not self.object:
                    # g.trace('unknown',word)
                    return False
                self.appendTabName(word)
                i = j
            self.leadinWord = word
            return True
    #@-node:AGP.20250415230112.1929:getLeadinWord
    #@+node:AGP.20250415230112.1930:getMembersList
    def getMembersList (self,obj):
        
        '''Return a list of possible autocompletions for self.leadinWord.'''
    
        if obj:
            aList = inspect.getmembers(obj)
            members = ['%s:%s' % (a,g.prettyPrintType(b))
                for a,b in aList if not a.startswith('__')]
            members.sort()
            return members
        else:
            return []
    #@-node:AGP.20250415230112.1930:getMembersList
    #@+node:AGP.20250415230112.1931:info
    def info (self):
        
        c = self.c ; doc = None ; obj = self.object ; w = self.widget
    
        word = g.app.gui.getSelectedText(w)
        
        if not word:
            # Never gets called, but __builtin__.f will work.
            word = self.findCalltipWord(w)
            if word:
                # Try to get the docstring for the Python global.
                f = __builtins__.get(self.leadinWord)
                doc = f and f.__doc__
    
        if not doc:
            if not self.hasAttr(obj,word): return
            obj = self.getAttr(obj,word)
            doc = inspect.getdoc(obj)
    
        if doc:
            c.frame.log.clearTab('Info',wrap='word')
            g.es(doc,tabName='Info')
    #@-node:AGP.20250415230112.1931:info
    #@+node:AGP.20250415230112.1932:insertNormalChar
    def insertNormalChar (self,ch,keysym):
        
        k = self.k ; w = self.widget
    
        if g.isWordChar(ch):
            # Look ahead to see if the character completes any item.
            s = g.app.gui.getSelectedText(w) + ch
            tabList,common_prefix = g.itemsMatchingPrefixInList(
                s,self.membersList,matchEmptyPrefix=True)
            if tabList:
                # Add the character.
                self.tabList = tabList
                self.extendSelection(ch)
                s = g.app.gui.getSelectedText(w)
                if s.startswith(self.prefix):
                    self.prefix = self.prefix + ch
                self.computeCompletionList()
        else:
            word = g.app.gui.getSelectedText(w)
            if keysym == 'parenleft':
                # Similar to chain logic.
                obj = self.object
                # g.trace(obj,word,self.hasAttr(obj,word))
                if self.hasAttr(obj,word):
                    obj = self.getAttr(obj,word)
                    self.push(self.object)
                    self.object = obj
                    self.leadinWord = word
                    self.membersList = self.getMembersList(obj)
                    if k.enable_calltips:
                        # This calls self.finish if the '(' is valid.
                        self.calltip(obj)
                        return
            self.extendSelection(ch)
            self.finish()
    #@-node:AGP.20250415230112.1932:insertNormalChar
    #@+node:AGP.20250415230112.1933:push, pop, clear, stackNames
    def push (self,obj):
        
        if obj is not None:
            self.prevObjects.append(obj)
            # g.trace(self.stackNames())
            
    def pop (self):
        
        obj = self.prevObjects.pop()
        # g.trace(obj)
        return obj
        
    def clear (self):
        
        self.prevObjects = []
        # g.trace(g.callers())
        
    def stackNames (self):
        
        aList = []
        for z in self.prevObjects:
            if hasattr(z,'__name__'):
                aList.append(z.__name__)
            elif hasattr(z,'__class__'):
                aList.append(z.__class__.__name__)
            else:
                aList.append(str(z))
        return aList
    #@-node:AGP.20250415230112.1933:push, pop, clear, stackNames
    #@+node:AGP.20250415230112.1934:setObjectAndMembersList & helpers
    def setObjectAndMembersList (self,word):
        
        c = self.c
        
        if not word:
            # Leading dot shows all classes.
            self.leadinWord = None
            self.object = sys.modules
            self.membersList = sys.modules.keys()
            self.beginTabName('Modules')
        elif word in ( "'",'"'):
            word = 'aString' # This is in the objectsDict.
            self.clear()
            self.push(self.object)
            self.object = 'aString'
            self.membersList = self.getMembersList(self.object)
        elif self.object:
            self.getObjectFromAttribute(word)
        # elif word == 'self':
            # self.completeSelf()
        else:
            obj = self.objectDict.get(word) or sys.modules.get(word)
            self.completeFromObject(obj)
    
        # g.trace(word,self.object,len(self.membersList))
    #@+node:AGP.20250415230112.1935:getObjectFromAttribute
    def getObjectFromAttribute (self,word):
        
        obj = self.object
    
        if obj and self.hasAttr(obj,word):
            self.push(self.object)
            self.object = self.getAttr(obj,word)
            self.appendToKnownObjects(self.object)
            self.membersList = self.getMembersList(self.object)
        else:
            # No special support for 'self' here.
            # Don't clear the stack here!
            self.membersList = []
            self.object = None
    #@-node:AGP.20250415230112.1935:getObjectFromAttribute
    #@+node:AGP.20250415230112.1936:completeSelf
    def completeSelf (self):
        
        # This scan will be fast if an instant object already exists.
        className,obj,p,s = self.classScanner.scan()
        # g.trace(className,obj,p,s and len(s))
    
        # First, look up the className.
        if not obj and className:
            obj = self.allClassesDict.get(className)
            # if obj: g.trace('found in allClassesDict: %s = %s' % (className,obj))
    
        # Second, create the object from class definition.
        if not obj and s:
            theClass = self.computeClassObjectFromString(className,s)
            if theClass:
                obj = self.createProxyObjectFromClass(className,theClass)
                if obj:
                    self.selfObjectsDict [className] = obj
                    # This prevents future rescanning, even if the node moves.
                    self.selfTnodesDict [p.v.t] = obj
        if obj:
            self.selfClassName = className
            self.push(self.object)
            self.object = obj
            self.membersList = self.getMembersList(obj=obj)
        else:
            # No further action possible or desirable.
            self.selfClassName = None
            self.object = None
            self.clear()
            self.membersList = []
    #@-node:AGP.20250415230112.1936:completeSelf
    #@+node:AGP.20250415230112.1937:completeFromObject
    def completeFromObject (self,obj):
    
        if obj:
            self.appendToKnownObjects(obj)
            self.push(self.object)
            self.object = obj
            self.membersList = self.getMembersList(obj=obj)
        else:
            self.object = None
            self.clear()
            self.membersList = []
    #@-node:AGP.20250415230112.1937:completeFromObject
    #@-node:AGP.20250415230112.1934:setObjectAndMembersList & helpers
    #@+node:AGP.20250415230112.1938:setSelection
    def setSelection (self,s):
        
        c = self.c ; w = self.widget
        c.widgetWantsFocusNow(w)
        
        if g.app.gui.hasSelection(w):
            i,j = g.app.gui.getSelectionRange(w)
            w.delete(i,j)
        else:
            i = g.app.gui.getInsertPoint(w)
            
        # Don't go past the ':' that separates the completion from the type.
        n = s.find(':')
        if n > -1: s = s[:n]
        
        w.insert(i,s)
        j = w.index('%s + %dc' % (i,len(s)))
        # g.trace(i,j)
        g.app.gui.setSelectionRange(w,i,j,insert=j)
        # New in Leo 4.4.2: recolor immediately to preserve the new selection in the new colorizer.
        c.frame.body.recolor_now(c.currentPosition(),incremental=True)
        # Usually this call will have no effect because the body text has not changed.
        c.frame.body.onBodyChanged('Typing')
    #@-node:AGP.20250415230112.1938:setSelection
    #@+node:AGP.20250415230112.1939:start
    def start (self,event=None,w=None):
        
        if w: self.widget = w
        else: w = self.widget
        
        # We wait until now to define these dicts so that more classes and objects will exist.
        if not self.objectDict:
            self.defineClassesDict()
            self.defineObjectDict()
    
        self.prefix = ''
        self.selection = g.app.gui.getTextSelection(w)
        self.selectedText = g.app.gui.getSelectedText(w)
        flag = self.getLeadinWord(w)
        if self.membersList:
            if not flag:
                # Remove the (leading) invocation character.
                i = g.app.gui.getInsertPoint(w)
                if w.get(i+'-1c') == '.':
                    w.delete(i+'-1c')
                    
            self.autoCompleterStateHandler(event)
        else:
            self.abort()
    #@-node:AGP.20250415230112.1939:start
    #@-node:AGP.20250415230112.1909:Helpers
    #@+node:AGP.20250415230112.1940:Scanning
    # Not used at present, but soon.
    #@+node:AGP.20250415230112.1941:initialScan
    # Don't call this finishCreate: the startup logic would call it too soon.
    
    def initialScan (self):
        
        g.trace(g.callers())
        
        self.scan(thread=True)
    #@-node:AGP.20250415230112.1941:initialScan
    #@+node:AGP.20250415230112.1942:scan
    def scan (self,event=None,verbose=True,thread=True):
        
        c = self.c
        if not c or not c.exists or c.frame.isNullFrame: return
        if g.app.unitTesting: return
        
        # g.trace('autocompleter')
        
        if 0: ## thread:
            # Use a thread to do the initial scan so as not to interfere with the user.            
            def scan ():
                #g.es( "This is for testing if g.es blocks in a thread", color = 'pink' )
                # During unit testing c gets destroyed before the scan finishes.
                if not g.app.unitTesting:
                    self.scanOutline(verbose=True)
        
            t = threading.Thread(target=scan)
            t.setDaemon(True)
            t.start()
        else:
            self.scanOutline(verbose=verbose)
    #@-node:AGP.20250415230112.1942:scan
    #@+node:AGP.20250415230112.1943:definePatterns
    def definePatterns (self):
        
        self.space = r'[ \t\r\f\v ]+' # one or more whitespace characters.
        self.end = r'\w+\s*\([^)]*\)' # word (\w) ws ( any ) (can cross lines)
    
        # Define re patterns for various languages.
        # These patterns match method/function definitions.
        self.pats = {}
        self.pats ['python'] = re.compile(r'def\s+%s' % self.end)  # def ws word ( any ) # Can cross line boundaries.
        self.pats ['java'] = re.compile(
            r'((public\s+|private\s+|protected\s+)?(static%s|\w+%s){1,2}%s)' % (
                self.space,self.space,self.end))
        self.pats ['perl'] = re.compile(r'sub\s+%s' % self.end)
        self.pats ['c++'] = re.compile(r'((virtual\s+)?\w+%s%s)' % (self.space,self.end))
        self.pats ['c'] = re.compile(r'\w+%s%s' % (self.space,self.end))
        
        # Define self.okchars for getCleaString.
        okchars = {}
        for z in string.ascii_letters:
            okchars [z] = z
        okchars ['_'] = '_'
        self.okchars = okchars 
    #@nonl
    #@-node:AGP.20250415230112.1943:definePatterns
    #@+node:AGP.20250415230112.1944:scanOutline
    def scanOutline (self,verbose=True):
    
        '''Traverse an outline and build the autocommander database.'''
        
        if verbose: g.es_print('Scanning for auto-completer...')
    
        c = self.c ; k = self.k ; count = 0
        for p in c.allNodes_iter():
            if verbose:
                count += 1 ;
                if (count % 200) == 0: g.es('.',newline=False)
            language = g.scanForAtLanguage(c,p)
            # g.trace('language',language,p.headString())
            s = p.bodyString()
            if k.enable_autocompleter:
                self.scanForAutoCompleter(s)
            if k.enable_calltips:
                self.scanForCallTip(s,language)
    
        if 0:
            g.trace('watchwords...\n\n')
            keys = self.watchwords.keys() ; keys.sort()
            for key in keys:
                aList = self.watchwords.get(key)
                g.trace('%s:\n\n' % (key), g.listToString(aList))
        if 0:
            g.trace('calltips...\n\n')
            keys = self.calltips.keys() ; keys.sort()
            for key in keys:
                d = self.calltips.get(key)
                if d:
                    g.trace('%s:\n\n' % (key), g.dictToString(d))
            
        if verbose:        
            g.es_print('\nauto-completer scan complete',color='blue')
    #@-node:AGP.20250415230112.1944:scanOutline
    #@+node:AGP.20250415230112.1945:scanForCallTip
    def scanForCallTip (self,s,language):
    
        '''this function scans text for calltip info'''
    
        d = self.calltips.get(language,{})
        pat = self.pats.get(language or 'python')
        
        # Set results to a list of all the function/method defintions in s.
        results = pat and pat.findall(s) or []
    
        for z in results:
            if isinstance(z,tuple): z = z [0]
            pieces2 = z.split('(')
            # g.trace(pieces2)
            pieces2 [0] = pieces2 [0].split() [-1]
            a, b = pieces2 [0], pieces2 [1]
            aList = d.get(a,[])
            if str(z) not in aList:
                aList.append(str(z))
                d [a] = aList
        
        self.calltips [language] = d
    #@-node:AGP.20250415230112.1945:scanForCallTip
    #@+node:AGP.20250415230112.1946:scanForAutoCompleter
    def scanForAutoCompleter (self,s):
    
        '''This function scans text for the autocompleter database.'''
    
        aList = [] ; t1 = s.split('.')
        
        if 1: # Slightly faster.
            t1 = s.split('.') ; 
            i = 0 ; n = len(t1)-1
            while i < n:
                self.makeAutocompletionList(t1[i],t1[i+1],aList)
                i += 1
        else:
            reduce(lambda a,b: self.makeAutocompletionList(a,b,aList),t1)
    
        if aList:
            for a, b in aList:
                z = self.watchwords.get(a,[])
                if str(b) not in z:
                    z.append(str(b))
                    self.watchwords [a] = z
    #@+node:AGP.20250415230112.1947:makeAutocompletionList
    def makeAutocompletionList (self,a,b,glist):
        
        '''We have seen a.b, where a and b are arbitrary strings.
        Append (a1.b1) to glist.
        To compute a1, scan backwards in a until finding whitespace.
        To compute b1, scan forwards in b until finding a char not in okchars.
        '''
        
        if 1: # Do everything inline.  It's a few percent faster.
    
            # Compute reverseFindWhitespace inline.
            i = len(a) -1
            while i >= 0:
                if a[i].isspace() or a [i] == '.':
                    a1 = a [i+1:] ; break
                i -= 1
            else:
                a1 = a
                
            # Compute getCleanString inline.
            i = 0
            for ch in b:
                if ch not in self.okchars:
                    b1 = b[:i] ; break
                i += 1
            else:
                b1 = b
    
            if b1:
                glist.append((a1,b1),)
                
            return b # Not needed unless we are using reduce.
        else:
            a1 = self.reverseFindWhitespace(a)
            if a1:
                b1 = self.getCleanString(b)
                if b1:
                    glist.append((a1,b1))
            return b
    #@+node:AGP.20250415230112.1948:reverseFindWhitespace
    def reverseFindWhitespace (self,s):
    
        '''Return the longest tail of s containing no whitespace or period.'''
    
        i = len(s) -1
        while i >= 0:
            if s[i].isspace() or s [i] == '.': return s [i+1:]
            i -= 1
    
        return s
    #@-node:AGP.20250415230112.1948:reverseFindWhitespace
    #@+node:AGP.20250415230112.1949:getCleanString
    def getCleanString (self,s):
        
        '''Return the prefix of s containing only chars in okchars.'''
        
        i = 0
        for ch in s:
            if ch not in self.okchars:
                return s[:i]
            i += 1
    
        return s
    #@-node:AGP.20250415230112.1949:getCleanString
    #@-node:AGP.20250415230112.1947:makeAutocompletionList
    #@-node:AGP.20250415230112.1946:scanForAutoCompleter
    #@-node:AGP.20250415230112.1940:Scanning
    #@+node:AGP.20250415230112.1950:Proxy classes and objects
    #@+node:AGP.20250415230112.1951:createProxyObjectFromClass
    def createProxyObjectFromClass (self,className,theClass):
        
        '''Create a dummy instance object by instantiating theClass with a dummy ctor.'''
    
        if 0: # Calling the real ctor is way too dangerous.
            # Set args to the list of required arguments.
            args = inspect.getargs(theClass.__init__.im_func.func_code)
            args = args[0] ; n = len(args)-1
            args = [None for z in xrange(n)]
            
        def dummyCtor (self):
            pass
            
        try:
            obj = None
            old_init = hasattr(theClass,'__init__') and theClass.__init__
            theClass.__init__ = dummyCtor
            obj = theClass()
        finally:
            if old_init:
                theClass.__init__ = old_init
            else:
                delattr(theClass,'__init__')
            
        g.trace(type(theClass),obj)
    
        # Verify that it has all the proper attributes.
        # g.trace(g.listToString(dir(obj)))
        return obj
    #@-node:AGP.20250415230112.1951:createProxyObjectFromClass
    #@+node:AGP.20250415230112.1952:createClassObjectFromString
    def computeClassObjectFromString (self,className,s):
    
        try:
            # Add the the class definition to the present environment.
            exec s
    
            # Get the newly created object from the locals dict.
            theClass = locals().get(className)
            return theClass
    
        except Exception:
            if 1: # Could be a weird kind of user error.
                g.es_print('unexpected exception in computeProxyObject')
                g.es_exception()
            return None
    #@-node:AGP.20250415230112.1952:createClassObjectFromString
    #@-node:AGP.20250415230112.1950:Proxy classes and objects
    #@+node:AGP.20250415230112.1953:class forgivingParserClass
    class forgivingParserClass:
        
        '''A class to create a valid class instances from
        a class definition that may contain syntax errors.'''
        
        #@    @+others
        #@+node:AGP.20250415230112.1954:ctor (forgivingParserClass)
        def __init__ (self,c):
            
            self.c = c
            self.excludedTnodesList = []
            self.old_putBody = None # Set in parse for communication with newPutBody.
        #@-node:AGP.20250415230112.1954:ctor (forgivingParserClass)
        #@+node:AGP.20250415230112.1955:parse
        def parse (self,p):
            
            '''The top-level parser method.
            
            It patches c.atFileCommands.putBody, calls the forgiving parser and finally
            restores c.atFileCommands.putBody.'''
            
            c = self.c
            
            # Create an ivar for communication with newPutBody.
            self.old_putBody = c.atFileCommands.putBody
            
            # Override atFile.putBody.
            c.atFileCommands.putBody = self.newPutBody
            
            try:
                s = None
                s = self.forgivingParser(p)
            finally:
                c.atFileCommands.putBody = self.old_putBody
                return s
        #@-node:AGP.20250415230112.1955:parse
        #@+node:AGP.20250415230112.1956:forgivingParser
        def forgivingParser (self,p):
        
            c = self.c ; root = p.copy()
            self.excludedTnodesList = []
            s = g.getScript(c,root,useSelectedText=False)
            while s:
                try:
                    val = compiler.parse(s+'\n')
                    break
                except (parser.ParserError,SyntaxError):
                    fileName, n = g.getLastTracebackFileAndLineNumber()
                    p = self.computeErrorNode(c,root,n,lines=g.splitLines(s))
                    if not p or p == root:
                        g.es_print('Syntax error in class node: can not continue')
                        s = None ; break
                    else:
                        # g.es_print('Syntax error: deleting %s' % p.headString())
                        self.excludedTnodesList.append(p.v.t)
                        s = g.getScript(c,root,useSelectedText=False)
            return s or ''
        #@-node:AGP.20250415230112.1956:forgivingParser
        #@+node:AGP.20250415230112.1957:computeErrorNode
        def computeErrorNode (self,c,root,n,lines):
        
            '''The from c.goToLineNumber that applies to scripts.
            Unlike c.gotoLineNumberOpen, this function returns a position.'''
        
            if n == 1 or n >= len(lines):
                return root
        
            vnodeName, junk, junk, junk, junk = c.convertLineToVnodeNameIndexLine(
                lines, n, root, scriptFind = True)
        
            if vnodeName:
                for p in root.self_and_subtree_iter():
                    if p.matchHeadline(vnodeName):
                        return p
        
            return None
        #@-node:AGP.20250415230112.1957:computeErrorNode
        #@+node:AGP.20250415230112.1958:newPutBody
        def newPutBody (self,p,oneNodeOnly=False,fromString=''):
        
            if p.v.t in self.excludedTnodesList:
                pass
                # g.trace('ignoring',p.headString())
            else:
                self.old_putBody(p,oneNodeOnly,fromString)
        #@-node:AGP.20250415230112.1958:newPutBody
        #@-others
    #@-node:AGP.20250415230112.1953:class forgivingParserClass
    #@+node:AGP.20250415230112.1959:class classScannerClass
    class classScannerClass:
        
        '''A class to find class definitions in a node or its parents.'''
        
        #@    @+others
        #@+node:AGP.20250415230112.1960:ctor
        def __init__ (self,c):
            
            self.c = c
            
            # Ignore @root for now:
            # self.start_in_doc = c.config.getBool('at_root_bodies_start_in_doc_mode')
        
            self.start_in_doc = False
        #@-node:AGP.20250415230112.1960:ctor
        #@+node:AGP.20250415230112.1961:scan
        def scan (self):
            
            c = self.c
        
            className,obj,p = self.findParentClass(c.currentPosition())
            # g.trace(className,obj,p)
        
            if p and not obj:
                parser = c.k.autoCompleter.forgivingParser
                s = parser.parse(p)
            else:
                s = None
                
            return className,obj,p,s
        #@-node:AGP.20250415230112.1961:scan
        #@+node:AGP.20250415230112.1962:findParentClass
        def findParentClass (self,root):
            
            autoCompleter = self.c.k.autoCompleter
            
            # First, see if any parent has already been scanned.
            for p in root.self_and_parents_iter():
                obj = autoCompleter.selfTnodesDict.get(p.v.t)
                if obj:
                    # g.trace('found',obj,'in',p.headString())
                    return None,obj,p
            
            # Next, do a much slower scan.
            # g.trace('slow scanning...')
            for p in root.self_and_parents_iter():
                className = self.findClass(p)
                if className:
                    # g.trace('found',className,'in',p.headString())
                    return className,None,p
            
            return None,None,None
        #@-node:AGP.20250415230112.1962:findParentClass
        #@+node:AGP.20250415230112.1963:findClass & helpers
        def findClass (self,p):
        
            lines = g.splitLines(p.bodyString())
            inDoc = self.start_in_doc
            # g.trace(p.headString())
            for s in lines:
                if inDoc:
                    if self.endsDoc(s):
                        inDoc = False
                else:
                    if self.startsDoc(s):
                        inDoc = True
                    else:
                        # Not a perfect scan: a triple-string could start with 'class',
                        # but perfection is not important.
                        className = self.startsClass(s)
                        if className: return className
            else:
                return None
        #@+node:AGP.20250415230112.1964:endsDoc
        def endsDoc (self,s):
            
            return s.startswith('@c')
        #@-node:AGP.20250415230112.1964:endsDoc
        #@+node:AGP.20250415230112.1965:startsClass
        def startsClass (self,s):
            
            if s.startswith('class'):
                i = 5
                i = g.skip_ws(s,i)
                j = g.skip_id(s,i)
                word = s[i:j]
                # g.trace(word)
                return word
            else:
                return None
        #@-node:AGP.20250415230112.1965:startsClass
        #@+node:AGP.20250415230112.1966:startsDoc
        def startsDoc (self,s):
        
            for s2 in ('@doc','@ ','@\n', '@r', '@\t'):
                if s.startswith(s2):
                    return True
            else:
                return False
        #@-node:AGP.20250415230112.1966:startsDoc
        #@-node:AGP.20250415230112.1963:findClass & helpers
        #@-others
    #@-node:AGP.20250415230112.1959:class classScannerClass
    #@-others
#@-node:AGP.20250415230112.1897:class autoCompleterClass
#@-others
#@-node:AGP.20250415230112.1893:@thin leoKeys.py
#@-leo
