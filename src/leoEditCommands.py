# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:AGP.20250415230112.813:@thin leoEditCommands.py
#@@first

'''Basic editor commands for Leo.

Modelled after Emacs and Vim commands.'''

from __future__ import generators # To make Leo work with Python 2.2

#@<< imports >>
#@+node:AGP.20250415230112.814:<< imports >>
import leoGlobals as g

import leoFind
import leoKeys
import leoTest

import cPickle
import difflib
import os
import re
import string
import sys
import Tkinter as Tk

subprocess     = g.importExtension('subprocess',    pluginName=None,verbose=False)
tkColorChooser = g.importExtension('tkColorChooser',pluginName=None,verbose=False)
tkFileDialog   = g.importExtension('tkFileDialog',  pluginName=None,verbose=False)
tkFont         = g.importExtension('tkFont',        pluginName=None,verbose=False)

# The following imports is sometimes used.
import threading
#@-node:AGP.20250415230112.814:<< imports >>
#@nl

#@<< define class baseEditCommandsClass >>
#@+node:AGP.20250415230112.815:<< define class baseEditCommandsClass >>
class baseEditCommandsClass:

    '''The base class for all edit command classes'''

    #@    @+others
    #@+node:AGP.20250415230112.816: ctor, finishCreate, init (baseEditCommandsClass)
    def __init__ (self,c):
    
        self.c = c
        self.k = self.k = None
        self.registers = {}
        self.undoData = None
        
    def finishCreate(self):
    
        # Class delegators.
        self.k = self.k = self.c.k
        try:
            self.w = self.c.frame.body.bodyCtrl # New in 4.4a4.
        except AttributeError:
            self.w = None
        
    def init (self):
        
        '''Called from k.keyboardQuit to init all classes.'''
        
        pass
    #@nonl
    #@-node:AGP.20250415230112.816: ctor, finishCreate, init (baseEditCommandsClass)
    #@+node:AGP.20250415230112.817:begin/endCommand
    #@+node:AGP.20250415230112.818:beginCommand  & beginCommandWithEvent
    def beginCommand (self,undoType='Typing'):
        
        '''Do the common processing at the start of each command.'''
    
        return self.beginCommandHelper(ch='',undoType=undoType,w=self.w)
    
    def beginCommandWithEvent (self,event,undoType='Typing'):
        
        '''Do the common processing at the start of each command.'''
        
        return self.beginCommandHelper(ch=event.char,undoType=undoType,w=event.widget)
    #@+node:AGP.20250415230112.819:beingCommandHelper
    # New in Leo 4.4b4: calling beginCommand is valid for all widgets,
    # but does nothing unless we are in the body pane.
    
    def beginCommandHelper (self,ch,undoType,w):
    
        c = self.c ; p = c.currentPosition()
        name = c.widget_name(w)
    
        if name.startswith('body'):
            oldSel =  g.app.gui.getTextSelection(w)
            oldText = p.bodyString()
            self.undoData = g.Bunch(
                ch=ch,name=name,oldSel=oldSel,oldText=oldText,w=w,undoType=undoType)
        else:
            self.undoData = None
    
        return w
    #@-node:AGP.20250415230112.819:beingCommandHelper
    #@-node:AGP.20250415230112.818:beginCommand  & beginCommandWithEvent
    #@+node:AGP.20250415230112.820:endCommand
    # New in Leo 4.4b4: calling endCommand is valid for all widgets,
    # but handles undo only if we are in body pane.
    
    def endCommand(self,label=None,changed=True,setLabel=True):
        
        '''Do the common processing at the end of each command.'''
        
        c = self.c ; b = self.undoData ; k = self.k
    
        if b and b.name.startswith('body') and changed:
            c.frame.body.onBodyChanged(undoType=b.undoType,
                oldSel=b.oldSel,oldText=b.oldText,oldYview=None)
            
        self.undoData = None # Bug fix: 1/6/06 (after a5 released).
    
        k.clearState()
        
        # Warning: basic editing commands **must not** set the label.
        if setLabel:
            if label:
                k.setLabelGrey(label)
            else:
                k.resetLabel()
    #@-node:AGP.20250415230112.820:endCommand
    #@-node:AGP.20250415230112.817:begin/endCommand
    #@+node:AGP.20250415230112.821:editWidget
    def editWidget (self,event):
        
        c = self.c ; w = event and event.widget
        
        if w and g.app.gui.isTextWidget(w):
            self.w = w
        else:
            self.w = self.c.frame.body and self.c.frame.body.bodyCtrl
    
        if self.w:
            c.widgetWantsFocusNow(self.w)
            
        return self.w
    #@nonl
    #@-node:AGP.20250415230112.821:editWidget
    #@+node:AGP.20250415230112.822:getPublicCommands & getStateCommands
    def getPublicCommands (self):
    
        '''Return a dict describing public commands implemented in the subclass.
        Keys are untranslated command names.  Values are methods of the subclass.'''
    
        return {}
    #@-node:AGP.20250415230112.822:getPublicCommands & getStateCommands
    #@+node:AGP.20250415230112.823:getWSString
    def getWSString (self,txt):
    
        if 1:
            ntxt = [g.choose(ch=='\t',ch,' ') for ch in txt]
        else:
            ntxt = []
            for z in txt:
                if z == '\t':
                    ntxt.append(z)
                else:
                    ntxt.append(' ')
    
        return ''.join(ntxt)
    #@-node:AGP.20250415230112.823:getWSString
    #@+node:AGP.20250415230112.824:oops
    def oops (self):
    
        print("baseEditCommandsClass oops:",
            g.callers(),
            "must be overridden in subclass")
    #@-node:AGP.20250415230112.824:oops
    #@+node:AGP.20250415230112.825:Helpers
    #@+node:AGP.20250415230112.826:_chckSel
    def _chckSel (self,event,warning='no selection'):
    
        c = self.c ; k = self.k
        
        w = self.editWidget(event)
    
        val = w and 'sel' in w.tag_names() and w.tag_ranges('sel')
        
        if warning and not val:
            k.setLabelGrey(warning)
        
        return val
    #@-node:AGP.20250415230112.826:_chckSel
    #@+node:AGP.20250415230112.827:_checkIfRectangle
    def _checkIfRectangle (self,event):
    
        k = self.k ; key = event.keysym.lower()
        
        val = self.registers.get(key)
    
        if val and type(val) == type([]):
            k.clearState()
            k.setLabelGrey("Register contains Rectangle, not text")
            return True
    
        return False
    #@-node:AGP.20250415230112.827:_checkIfRectangle
    #@+node:AGP.20250415230112.828:contRanges
    def contRanges (self,w,range):
    
        ranges = w.tag_ranges(range)
        t1 = w.get(ranges[0],ranges[-1])
        t2 = []
        for z in xrange(0,len(ranges),2):
            z1 = z + 1
            t2.append(w.get(ranges[z],ranges[z1]))
        t2 = '\n'.join(t2)
        return t1 == t2
    #@-node:AGP.20250415230112.828:contRanges
    #@+node:AGP.20250415230112.829:getRectanglePoints
    def getRectanglePoints (self,w):
    
        c = self.c
        c.widgetWantsFocusNow(w)
    
        i  = w.index('sel.first')
        i2 = w.index('sel.last')
        r1, r2 = i.split('.')
        r3, r4 = i2.split('.')
    
        return int(r1), int(r2), int(r3), int(r4)
    #@-node:AGP.20250415230112.829:getRectanglePoints
    #@+node:AGP.20250415230112.830:inRange
    def inRange (self,w,range,l='',r=''):
    
        ranges = w.tag_ranges(range)
        for z in xrange(0,len(ranges),2):
            z1 = z + 1
            l1 = 'insert%s' % l
            r1 = 'insert%s' % r
            if w.compare(l1,'>=',ranges[z]) and w.compare(r1,'<=',ranges[z1]):
                return True
        return False
    #@-node:AGP.20250415230112.830:inRange
    #@+node:AGP.20250415230112.831:keyboardQuit
    def keyboardQuit (self,event):
        
        '''Clear the state and the minibuffer label.'''
        
        return self.k.keyboardQuit(event)
    #@-node:AGP.20250415230112.831:keyboardQuit
    #@+node:AGP.20250415230112.832:testinrange
    def testinrange (self,w):
    
        if not self.inRange(w,'sel') or not self.contRanges(w,'sel'):
            # self.removeRKeys(w)
            return False
        else:
            return True
    #@-node:AGP.20250415230112.832:testinrange
    #@-node:AGP.20250415230112.825:Helpers
    #@-others
#@-node:AGP.20250415230112.815:<< define class baseEditCommandsClass >>
#@nl

#@+others
#@+node:AGP.20250415230112.833: Module level...
#@+node:AGP.20250415230112.834:createEditCommanders (leoEditCommands module)
def createEditCommanders (c):
    
    '''Create edit classes in the commander.'''
    
    global classesList

    for name, theClass in classesList:
        theInstance = theClass(c)# Create the class.
        setattr(c,name,theInstance)
        # g.trace(name,theInstance)
#@-node:AGP.20250415230112.834:createEditCommanders (leoEditCommands module)
#@+node:AGP.20250415230112.835:finishCreateEditCommanders (leoEditCommands module)
def finishCreateEditCommanders (c):
    
    '''Finish creating edit classes in the commander.
    
    Return the commands dictionary for all the classes.'''
    
    global classesList
    
    d = {}

    for name, theClass in classesList:
        theInstance = getattr(c,name)
        theInstance.finishCreate()
        theInstance.init()
        d2 = theInstance.getPublicCommands()
        if d2:
            d.update(d2)
            if 0:
                keys = d2.keys()
                keys.sort()
                print '----- %s' % name
                for key in keys: print
                
    return d
#@-node:AGP.20250415230112.835:finishCreateEditCommanders (leoEditCommands module)
#@+node:AGP.20250415230112.836:initAllEditCommanders
def initAllEditCommanders (c):
    
    '''Re-init classes in the commander.'''
    
    global classesList

    for name, theClass in classesList:
        theInstance = getattr(c,name)
        theInstance.init()
#@-node:AGP.20250415230112.836:initAllEditCommanders
#@-node:AGP.20250415230112.833: Module level...
#@+node:AGP.20250415230112.837:class Tracker (an iterator)
class Tracker:

    '''An iterator class to allow the user to cycle through and change a list.'''

    #@    @+others
    #@+node:AGP.20250415230112.838:init
    def __init__ (self):
        
        self.tablist = []
        self.prefix = None 
        self.ng = self._next()
    #@-node:AGP.20250415230112.838:init
    #@+node:AGP.20250415230112.839:setTabList
    def setTabList (self,prefix,tlist):
        
        self.prefix = prefix 
        self.tablist = tlist
    #@-node:AGP.20250415230112.839:setTabList
    #@+node:AGP.20250415230112.840:_next
    def _next (self):
        
        while 1:
            tlist = self.tablist 
            if not tlist:yield ''
            for z in self.tablist:
                if tlist!=self.tablist:
                    break 
                yield z
    #@-node:AGP.20250415230112.840:_next
    #@+node:AGP.20250415230112.841:next
    def next (self):
        
        return self.ng.next()
    #@-node:AGP.20250415230112.841:next
    #@+node:AGP.20250415230112.842:clear
    def clear (self):
    
        self.tablist = []
        self.prefix = None
    #@-node:AGP.20250415230112.842:clear
    #@-others
#@-node:AGP.20250415230112.837:class Tracker (an iterator)
#@+node:AGP.20250415230112.843:abbrevCommandsClass (test)
#@+at
# 
# type some text, set its abbreviation with Control-x a i g, type the text for 
# abbreviation expansion
# type Control-x a e ( or Alt-x expand-abbrev ) to expand abbreviation
# type Alt-x abbrev-on to turn on automatic abbreviation expansion
# Alt-x abbrev-on to turn it off
# 
# an example:
# type:
# frogs
# after typing 's' type Control-x a i g.  This will turn the miniBuffer blue, 
# type in your definition. For example: turtles.
# 
# Now in the buffer type:
# frogs
# after typing 's' type Control-x a e.  This will turn the 'frogs' into:
# turtles
#@-at
#@@c

class abbrevCommandsClass (baseEditCommandsClass):

    #@    @+others
    #@+node:AGP.20250415230112.844: ctor & finishCreate
    def __init__ (self,c):
        
        baseEditCommandsClass.__init__(self,c) # init the base class.
        
        # Set local ivars.
        self.abbrevs ={}
        
    def finishCreate(self):
        
        baseEditCommandsClass.finishCreate(self)
    #@-node:AGP.20250415230112.844: ctor & finishCreate
    #@+node:AGP.20250415230112.845: getPublicCommands & getStateCommands
    def getPublicCommands (self):
        
        return {
            'abbrev-mode':                  self.toggleAbbrevMode,
            'add-global-abbrev':            self.addAbbreviation,
            # 'expand-abbrev':              self.expandAbbrev, # Not a command.
            'expand-region-abbrevs':        self.regionalExpandAbbrev,
            'inverse-add-global-abbrev':    self.addInverseAbbreviation,
            'kill-all-abbrevs':             self.killAllAbbrevs,
            'list-abbrevs':                 self.listAbbrevs,
            'read-abbrev-file':             self.readAbbreviations,
            'write-abbrev-file':            self.writeAbbreviations,
        }
    #@-node:AGP.20250415230112.845: getPublicCommands & getStateCommands
    #@+node:AGP.20250415230112.846:addAbbreviation
    def addAbbreviation (self,event):
        
        '''Add an abbreviation:
        The selected text is the abbreviation;
        the minibuffer prompts you for the name of the abbreviation.
        Also sets abbreviations on.'''
                
        k = self.k ; state = k.getState('add-abbr')
    
        if state == 0:
            w = self.editWidget(event) # Sets self.w
            if not w: return
            k.setLabelBlue('Add Abbreviation: ',protect=True)
            k.getArg(event,'add-abbr',1,self.addAbbreviation)
        else:
            w = self.w
            k.clearState()
            k.resetLabel()
            word = w.get('insert -1c wordstart','insert -1c wordend')
            if k.arg.strip():
                self.abbrevs [k.arg] = word
                k.abbrevOn = True
                k.setLabelGrey(
                    "Abbreviations are on.\nAbbreviation: '%s' = '%s'" % (
                    k.arg,word))
    #@-node:AGP.20250415230112.846:addAbbreviation
    #@+node:AGP.20250415230112.847:addInverseAbbreviation
    def addInverseAbbreviation (self,event):
        
        '''Add an inverse abbreviation:
        The selected text is the abbreviation name;
        the minibuffer prompts you for the value of the abbreviation.'''
        
        k = self.k ; state = k.getState('add-inverse-abbr')
    
        if state == 0:
            w = self.editWidget(event) # Sets self.w
            if not w: return
            k.setLabelBlue('Add Inverse Abbreviation: ',protect=True)
            k.getArg(event,'add-inverse-abbr',1,self.addInverseAbbreviation)
        else:
            w = self.w
            k.clearState()
            k.resetLabel()
            word = w.get('insert -1c wordstart','insert -1c wordend').strip()
            if word:
                self.abbrevs [word] = k.arg
    #@-node:AGP.20250415230112.847:addInverseAbbreviation
    #@+node:AGP.20250415230112.848:expandAbbrev
    def expandAbbrev (self,event):
        
        '''Not a command.  Called from k.masterCommand to expand
        abbreviations in event.widget.'''
    
        k = self.k ; ch = event.char.strip()
        w = self.editWidget(event)
        if not w: return
    
        word = w.get('insert -1c wordstart','insert -1c wordend')
        g.trace('ch',repr(ch),'word',repr(word))
        if ch:
            # We must do this: expandAbbrev is called from Alt-x and Control-x,
            # we get two differnt types of data and w states.
            word = '%s%s'% (word,ch)
            
        val = self.abbrevs.get(word)
        if val is not None:
            w.delete('insert -1c wordstart','insert -1c wordend')
            w.insert('insert',val)
            
        return val is not None
    #@-node:AGP.20250415230112.848:expandAbbrev
    #@+node:AGP.20250415230112.849:killAllAbbrevs
    def killAllAbbrevs (self,event):
        
        '''Delete all abbreviations.'''
    
        self.abbrevs = {}
    #@-node:AGP.20250415230112.849:killAllAbbrevs
    #@+node:AGP.20250415230112.850:listAbbrevs
    def listAbbrevs (self,event):
        
        '''List all abbreviations.'''
    
        k = self.k
        
        if self.abbrevs:
            for z in self.abbrevs:
                g.es('%s=%s' % (z,self.abbrevs[z]))
    #@-node:AGP.20250415230112.850:listAbbrevs
    #@+node:AGP.20250415230112.851:readAbbreviations
    def readAbbreviations (self,event):
        
        '''Read abbreviations from a file.'''
    
        f = tkFileDialog and tkFileDialog.askopenfile()
        if not f: return
    
        for x in f:
            a, b = x.split('=')
            b = b [:-1]
            self.abbrevs [a] = b
        f.close()
    #@-node:AGP.20250415230112.851:readAbbreviations
    #@+node:AGP.20250415230112.852:regionalExpandAbbrev
    def regionalExpandAbbrev (self,event):
        
        '''Exapand abbreviations throughout a region.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w or not self._chckSel(event): return
    
        i1 = w.index('sel.first')
        i2 = w.index('sel.last')
        ins = w.index('insert')
        #@    << define a new generator searchXR >>
        #@+node:AGP.20250415230112.853:<< define a new generator searchXR >>
        #@+at 
        #@nonl
        # This is a generator (it contains a yield).
        # To make this work we must define a new generator for each call to 
        # regionalExpandAbbrev.
        #@-at
        #@@c
        def searchXR (i1,i2,ins,event):
            k = self.k
            w = self.editWidget(event)
            if not w: return
        
            w.tag_add('sXR',i1,i2)
            while i1:
                tr = w.tag_ranges('sXR')
                if not tr: break
                i1 = w.search(r'\w',i1,stopindex=tr[1],regexp=True)
                if i1:
                    word = w.get('%s wordstart' % i1,'%s wordend' % i1)
                    w.tag_delete('found')
                    w.tag_add('found','%s wordstart' % i1,'%s wordend' % i1)
                    w.tag_config('found',background='yellow')
                    if self.abbrevs.has_key(word):
                        k.setLabel('Replace %s with %s? y/n' % (word,self.abbrevs[word]))
                        yield None
                        if k.regXKey == 'y':
                            ind = w.index('%s wordstart' % i1)
                            w.delete('%s wordstart' % i1,'%s wordend' % i1)
                            w.insert(ind,self.abbrevs[word])
                    i1 = '%s wordend' % i1
            w.mark_set('insert',ins)
            w.selection_clear()
            w.tag_delete('sXR')
            w.tag_delete('found')
            k.setLabelGrey('')
            self.k.regx = g.bunch(iter=None,key=None)
        #@-node:AGP.20250415230112.853:<< define a new generator searchXR >>
        #@nl
    
        # EKR: the 'result' of calling searchXR is a generator object.
        k.regx.iter = searchXR(i1,i2,ins,event)
        k.regx.iter.next() # Call it the first time.
    #@-node:AGP.20250415230112.852:regionalExpandAbbrev
    #@+node:AGP.20250415230112.854:toggleAbbrevMode
    def toggleAbbrevMode (self,event):
        
        '''Toggle abbreviation mode.'''
     
        k = self.k
        k.abbrevOn = not k.abbrevOn
        k.keyboardQuit(event)
        k.setLabel('Abbreviations are ' + g.choose(k.abbrevOn,'On','Off'))
    #@-node:AGP.20250415230112.854:toggleAbbrevMode
    #@+node:AGP.20250415230112.855:writeAbbreviations
    def writeAbbreviations (self,event):
        
        '''Write abbreviations to a file.'''
    
        f = tkFileDialog and tkFileDialog.asksaveasfile()
        if not f: return
    
        for x in self.abbrevs:
            f.write('%s=%s\n' % (x,self.abbrevs[x]))
        f.close()
    #@-node:AGP.20250415230112.855:writeAbbreviations
    #@-others
#@-node:AGP.20250415230112.843:abbrevCommandsClass (test)
#@+node:AGP.20250415230112.856:bufferCommandsClass
#@+at 
#@nonl
# An Emacs instance does not have knowledge of what is considered a buffer in 
# the environment.
# 
# The call to setBufferInteractionMethods calls the buffer configuration 
# methods.
#@-at
#@@c

class bufferCommandsClass (baseEditCommandsClass):

    #@    @+others
    #@+node:AGP.20250415230112.857: ctor (bufferCommandsClass)
    def __init__ (self,c):
        
        baseEditCommandsClass.__init__(self,c) # init the base class.
        
        self.fromName = '' # Saved name from getBufferName.
        self.nameList = [] # [n: <headline>]
        self.names = {}
        self.tnodes = {} # Keys are n: <headline>, values are tnodes.
        
        try:
            self.w = c.frame.body.bodyCtrl
        except AttributeError:
            self.w = None
    #@-node:AGP.20250415230112.857: ctor (bufferCommandsClass)
    #@+node:AGP.20250415230112.858: getPublicCommands
    def getPublicCommands (self):
    
        return {
        
            # These do not seem useful.
                # 'copy-to-buffer':               self.copyToBuffer,
                # 'insert-to-buffer':             self.insertToBuffer,
           
            'append-to-buffer':             self.appendToBuffer,
            'kill-buffer' :                 self.killBuffer,
            'list-buffers' :                self.listBuffers,
            'list-buffers-alphabetically':  self.listBuffersAlphabetically,
            'prepend-to-buffer':            self.prependToBuffer,
            'rename-buffer':                self.renameBuffer,
            'switch-to-buffer':             self.switchToBuffer,
        }
    #@-node:AGP.20250415230112.858: getPublicCommands
    #@+node:AGP.20250415230112.859:Entry points
    #@+node:AGP.20250415230112.860:appendToBuffer
    def appendToBuffer (self,event):
        
        '''Add the selected body text to the end of the body text of a named buffer (node).'''
        
        w = self.editWidget(event) # Sets self.w
        if not w: return
    
        self.k.setLabelBlue('Append to buffer: ')
        self.getBufferName(self.appendToBufferFinisher)
    
    def appendToBufferFinisher (self,name):
    
        c = self.c ; k = self.k ; w = self.w
        s = g.app.gui.getSelectedText(w)
        p = self.findBuffer(name)
        if s and p:
            c.beginUpdate()
            try:
                w = self.w
                c.selectPosition(p)
                self.beginCommand('append-to-buffer: %s' % p.headString())
                w.insert('end',s)
                w.mark_set('insert','end')
                w.see('end')
                self.endCommand()
            finally:
                c.endUpdate()
                c.recolor_now()
    #@-node:AGP.20250415230112.860:appendToBuffer
    #@+node:AGP.20250415230112.861:copyToBuffer
    def copyToBuffer (self,event):
        
        '''Add the selected body text to the end of the body text of a named buffer (node).'''
        
        w = self.editWidget(event) # Sets self.w
        if not w: return
    
        self.k.setLabelBlue('Copy to buffer: ')
        self.getBufferName(self.copyToBufferFinisher)
    
    def copyToBufferFinisher (self,event,name):
    
        c = self.c ; k = self.k ; w = self.w
        s = g.app.gui.getSelectedText(w)
        p = self.findBuffer(name)
        if s and p:
            c.beginUpdate()
            try:
                w = self.w
                c.selectPosition(p)
                self.beginCommand('copy-to-buffer: %s' % p.headString())
                w.insert('end',s)
                w.mark_set('insert','end')
                w.see('end')
                self.endCommand()
            finally:
                c.endUpdate()
                c.recolor_now()
    #@-node:AGP.20250415230112.861:copyToBuffer
    #@+node:AGP.20250415230112.862:insertToBuffer
    def insertToBuffer (self,event):
        
        '''Add the selected body text at the insert point of the body text of a named buffer (node).'''
        
        w = self.editWidget(event) # Sets self.w
        if not w: return
    
        self.k.setLabelBlue('Insert to buffer: ')
        self.getBufferName(self.insertToBufferFinisher)
    
    def insertToBufferFinisher (self,event,name):
        
        c = self.c ; k = self.k ; w = self.w
        s = g.app.gui.getSelectedText(w)
        p = self.findBuffer(name)
        if s and p:
            c.beginUpdate()
            try:
                w = self.w
                c.selectPosition(p)
                self.beginCommand('insert-to-buffer: %s' % p.headString())
                w.insert('insert',s)
                w.see('insert')
                self.endCommand()
            finally:
                c.endUpdate()
    #@-node:AGP.20250415230112.862:insertToBuffer
    #@+node:AGP.20250415230112.863:killBuffer
    def killBuffer (self,event):
        
        '''Delete a buffer (node) and all its descendants.'''
        
        w = self.editWidget(event) # Sets self.w
        if not w: return
    
        self.k.setLabelBlue('Kill buffer: ')
        self.getBufferName(self.killBufferFinisher)
    
    def killBufferFinisher (self,name):
    
        c = self.c ; p = self.findBuffer(name)
        if p:
            h = p.headString()
            current = c.currentPosition()
            c.selectPosition(p)
            c.deleteOutline (op_name='kill-buffer: %s' % h)
            c.selectPosition(current)
            self.k.setLabelBlue('Killed buffer: %s' % h)
    #@-node:AGP.20250415230112.863:killBuffer
    #@+node:AGP.20250415230112.864:listBuffers & listBuffersAlphabetically
    def listBuffers (self,event):
        
        '''List all buffers (node headlines), in outline order.
        Nodes with the same headline are disambiguated by giving their parent or child index.
        '''
        
        self.computeData()
        g.es('Buffers...')
        for name in self.nameList:
            g.es(name)
            
    def listBuffersAlphabetically (self,event):
        
        '''List all buffers (node headlines), in alphabetical order.
        Nodes with the same headline are disambiguated by giving their parent or child index.'''
        
        self.computeData()
        names = self.nameList[:] ; names.sort()
        
        g.es('Buffers...')
        for name in names:
            g.es(name)
    #@-node:AGP.20250415230112.864:listBuffers & listBuffersAlphabetically
    #@+node:AGP.20250415230112.865:prependToBuffer
    def prependToBuffer (self,event):
        
        '''Add the selected body text to the start of the body text of a named buffer (node).'''
        
        w = self.editWidget(event) # Sets self.w
        if not w: return
    
        self.k.setLabelBlue('Prepend to buffer: ')
        self.getBufferName(self.prependToBufferFinisher)
        
    def prependToBufferFinisher (self,event,name):
        
        c = self.c ; k = self.k ; w = self.w
        s = g.app.gui.getSelectedText(w)
        p = self.findBuffer(name)
        if s and p:
            c.beginUpdate()
            try:
                w = self.w
                c.selectPosition(p)
                self.beginCommand('prepend-to-buffer: %s' % p.headString())
                w.insert('1.0',s)
                w.mark_set('insert','1.0')
                w.see('1.0')
                self.endCommand()
            finally:
                c.endUpdate()
                c.recolor_now()
    
    #@-node:AGP.20250415230112.865:prependToBuffer
    #@+node:AGP.20250415230112.866:renameBuffer
    def renameBuffer (self,event):
        
        '''Rename a buffer, i.e., change a node's headline.'''
        
        self.k.setLabelBlue('Rename buffer from: ')
        self.getBufferName(self.renameBufferFinisher1)
        
    def renameBufferFinisher1 (self,name):
        
        self.fromName = name
        self.k.setLabelBlue('Rename buffer from: %s to: ' % (name))
        self.getBufferName(self.renameBufferFinisher2)
        
    def renameBufferFinisher2 (self,name):
        
        c = self.c ; p = self.findBuffer(self.fromName)
        if p:
            c.endEditing()
            c.beginUpdate()
            c.setHeadString(p,name)
            c.endUpdate()
    #@-node:AGP.20250415230112.866:renameBuffer
    #@+node:AGP.20250415230112.867:switchToBuffer
    def switchToBuffer (self,event):
        
        '''Select a buffer (node) by its name (headline).'''
    
        self.k.setLabelBlue('Switch to buffer: ')
        self.getBufferName(self.switchToBufferFinisher)
        
    def switchToBufferFinisher (self,name):
        
        c = self.c ; p = self.findBuffer(name)
        if p:
            c.beginUpdate()
            try:
                c.selectPosition(p)
            finally:
                c.endUpdate()
    #@-node:AGP.20250415230112.867:switchToBuffer
    #@-node:AGP.20250415230112.859:Entry points
    #@+node:AGP.20250415230112.868:Utils
    #@+node:AGP.20250415230112.869:computeData
    def computeData (self):
        
        counts = {} ; self.nameList = []
        self.names = {} ; self.tnodes = {}
       
        for p in self.c.allNodes_iter():
            h = p.headString().strip()
            t = p.v.t
            n = counts.get(t,0) + 1
            counts[t] = n
            if n == 1: # Only make one entry per set of clones.
                nameList = self.names.get(h,[])
                if nameList:
                    if p.parent():
                        key = '%s, parent: %s' % (h,p.parent().headString())
                    else:
                        key = '%s, child index: %d' % (h,p.childIndex())
                else:
                    key = h
                self.nameList.append(key)
                self.tnodes[key] = t
                nameList.append(key)
                self.names[h] = nameList
    #@-node:AGP.20250415230112.869:computeData
    #@+node:AGP.20250415230112.870:findBuffer
    def findBuffer (self,name):
        
        t = self.tnodes.get(name)
    
        for p in self.c.allNodes_iter():
            if p.v.t == t:
                return p
               
        g.trace("Can't happen",name)
        return None
    #@-node:AGP.20250415230112.870:findBuffer
    #@+node:AGP.20250415230112.871:getBufferName
    def getBufferName (self,finisher):
        
        '''Get a buffer name into k.arg and call k.setState(kind,n,handler).'''
        
        k = self.k ; c = k.c ; state = k.getState('getBufferName')
        
        if state == 0:
            self.computeData()
            self.getBufferNameFinisher = finisher
            prefix = k.getLabel() ; event = None
            k.getArg(event,'getBufferName',1,self.getBufferName,
                prefix=prefix,tabList=self.nameList)
        else:
            k.resetLabel()
            k.clearState()
            finisher = self.getBufferNameFinisher
            self.getBufferNameFinisher = None
            finisher(k.arg)
    #@-node:AGP.20250415230112.871:getBufferName
    #@-node:AGP.20250415230112.868:Utils
    #@-others
#@-node:AGP.20250415230112.856:bufferCommandsClass
#@+node:AGP.20250415230112.872:controlCommandsClass
class controlCommandsClass (baseEditCommandsClass):
    
    #@    @+others
    #@+node:AGP.20250415230112.873: ctor
    def __init__ (self,c):
    
        baseEditCommandsClass.__init__(self,c) # init the base class.
        
        self.payload = None
    #@-node:AGP.20250415230112.873: ctor
    #@+node:AGP.20250415230112.874: getPublicCommands
    def getPublicCommands (self):
        
        k = self.c.k
    
        return {
            'advertised-undo':              self.advertizedUndo,
            'iconify-frame':                self.iconifyFrame, # Same as suspend.
            'keyboard-quit':                k.keyboardQuit,
            'save-buffers-kill-leo':        self.saveBuffersKillLeo,
            'set-silent-mode':              self.setSilentMode,
            'shell-command':                self.shellCommand,
            'shell-command-on-region':      self.shellCommandOnRegion,
            'suspend':                      self.suspend,
        }
    #@-node:AGP.20250415230112.874: getPublicCommands
    #@+node:AGP.20250415230112.875:advertizedUndo
    def advertizedUndo (self,event):
        
        '''Undo the previous command.'''
    
        self.c.undoer.undo()
    #@-node:AGP.20250415230112.875:advertizedUndo
    #@+node:AGP.20250415230112.876:executeSubprocess
    def executeSubprocess (self,event,command,input):
        
        '''Execute a command in a separate process.'''
        
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        k.setLabelBlue('started  shell-command: %s' % command)
        try:
            ofile = os.tmpfile()
            efile = os.tmpfile()
            process = subprocess.Popen(command,bufsize=-1,
                stdout = ofile.fileno(), stderr = ofile.fileno(),
                stdin = subprocess.PIPE, shell = True)
            if input: process.communicate(input)
            process.wait()
            efile.seek(0)
            errinfo = efile.read()
            if errinfo: w.insert('insert',errinfo)
            ofile.seek(0)
            okout = ofile.read()
            if okout: w.insert('insert',okout)
        except Exception, x:
            w.insert('insert',x)
            
        k.setLabelGrey('finished shell-command: %s' % command)
    #@-node:AGP.20250415230112.876:executeSubprocess
    #@+node:AGP.20250415230112.877:setSilentMode
    def setSilentMode (self,event=None):
        
        '''Set the mode to be run silently, without the minibuffer.
        The only use for this command is to put the following in an @mode node::
            
            --> set-silent-mode'''
        
        self.c.k.silentMode = True
    #@-node:AGP.20250415230112.877:setSilentMode
    #@+node:AGP.20250415230112.878:shellCommand
    def shellCommand (self,event):
        
        '''Execute a shell command.'''
    
        if subprocess:
            k = self.k ; state = k.getState('shell-command')
        
            if state == 0:
                k.setLabelBlue('shell-command: ',protect=True)
                k.getArg(event,'shell-command',1,self.shellCommand)
            else:
                command = k.arg
                k.commandName = 'shell-command: %s' % command
                k.clearState()
                self.executeSubprocess(event,command,input=None)
        else:
            k.setLabelGrey('can not execute shell-command: can not import subprocess')
    #@-node:AGP.20250415230112.878:shellCommand
    #@+node:AGP.20250415230112.879:shellCommandOnRegion
    def shellCommandOnRegion (self,event):
        
        '''Execute a command taken from the selected text in a separate process.'''
        
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        if subprocess:
            is1,is2 = None,None
            try:
                is1 = w.index('sel.first')
                is2 = w.index('sel.last')
            finally:
                if is1:
                    command = w.get(is1,is2)
                    k.commandName = 'shell-command: %s' % command
                    self.executeSubprocess(event,command,input=None)
                else:
                    k.clearState()
                    k.resetLabel()
        else:
            k.setLabelGrey('can not execute shell-command: can not import subprocess')
    #@-node:AGP.20250415230112.879:shellCommandOnRegion
    #@+node:AGP.20250415230112.880:shutdown, saveBuffersKillEmacs & setShutdownHook
    def shutdown (self,event):
        
        '''Quit Leo, prompting to save any unsaved files first.'''
        
        g.app.onQuit()
            
    saveBuffersKillLeo = shutdown
    #@-node:AGP.20250415230112.880:shutdown, saveBuffersKillEmacs & setShutdownHook
    #@+node:AGP.20250415230112.881:suspend & iconifyFrame
    def suspend (self,event):
        
        '''Minimize the present Leo window.'''
    
        w = self.editWidget(event)
        if not w: return
        w.winfo_toplevel().iconify()
        
    # Must be a separate function so that k.inverseCommandsDict will be a true inverse.
        
    def iconifyFrame (self,event):
        
        '''Minimize the present Leo window.'''
    
        self.suspend(event)
    #@-node:AGP.20250415230112.881:suspend & iconifyFrame
    #@-others
#@-node:AGP.20250415230112.872:controlCommandsClass
#@+node:AGP.20250415230112.882:debugCommandsClass
class debugCommandsClass (baseEditCommandsClass):
    
    #@    @+others
    #@+node:AGP.20250415230112.883: ctor
    def __init__ (self,c):
    
        baseEditCommandsClass.__init__(self,c) # init the base class.
    #@-node:AGP.20250415230112.883: ctor
    #@+node:AGP.20250415230112.884: getPublicCommands
    def getPublicCommands (self):
        
        k = self
    
        return {
            'collect-garbage':      self.collectGarbage,
            'debug':                self.debug,
            'disable-gc-trace':     self.disableGcTrace,
            'dump-all-objects':     self.dumpAllObjects,
            'dump-new-objects':     self.dumpNewObjects,
            'enable-gc-trace':      self.enableGcTrace,
            'free-tree-widgets':    self.freeTreeWidgets,
            'print-focus':          self.printFocus,
            'print-stats':          self.printStats,
            'print-gc-summary':     self.printGcSummary,
            'run-unit-tests':       self.runUnitTests,
            'verbose-dump-objects': self.verboseDumpObjects,
        }
    #@-node:AGP.20250415230112.884: getPublicCommands
    #@+node:AGP.20250415230112.885:collectGarbage
    def collectGarbage (self,event=None):
        
        """Run Python's Gargabe Collector."""
        
        g.collectGarbage()
    #@-node:AGP.20250415230112.885:collectGarbage
    #@+node:AGP.20250415230112.886:debug
    def debug (self,event=None,target = None):
        
        '''Start an external debugger in another process.'''
    
        c = self.c ; p = c.currentPosition()
        pythonDir = g.os_path_dirname(sys.executable)
        
        #@    << find a debugger or return >>
        #@+node:AGP.20250415230112.887:<< find a debugger or return >>
        debuggers = (
            c.config.getString('debugger_path'),
            g.os_path_join(pythonDir,'scripts','_winpdb.py'),
        )
        
        for debugger in debuggers:
            if debugger:
                debugger = g.os_path_abspath(debugger)
                if g.os_path_exists(debugger):
                    break
                else:
                    g.es('Debugger does not exist: %s' % (debugger),color='blue')
        else:
            g.es('No debugger found.')
            return
        #@-node:AGP.20250415230112.887:<< find a debugger or return >>
        #@nl
        #@    << find the target file >>
        #@+node:AGP.20250415230112.888:<< find the target file >>
        targets = (
            target,
            c.config.getString('debugger_force_taget'),
            p.copy().anyAtFileNodeName(),
            c.config.getString('debugger_default_target'),
        )
        
        for target in targets:
            if target:
                target = g.os_path_abspath(target)
                if g.os_path_exists(target):
                    break
                else:
                    g.es('Debug target does not exist: %s' % (target),color='blue')
        #@-node:AGP.20250415230112.888:<< find the target file >>
        #@nl
        
        if target:
            args = [sys.executable, debugger, '-t', target]
        else:
            args = [sys.executable, debugger, '-t']
        
        if 1: # Use present environment.
            os.spawnv(os.P_NOWAIT, sys.executable, args)
        else: # Use a pristine environment.
            os.spawnve(os.P_NOWAIT, sys.executable, args, os.environ)
    #@-node:AGP.20250415230112.886:debug
    #@+node:AGP.20250415230112.889:dumpAll/New/VerboseObjects
    def dumpAllObjects (self,event=None):
        
        '''Print a summary of all existing Python objects.'''
        
        old = g.app.trace_gc
        g.app.trace_gc = True
        g.printGcAll()
        g.app.trace_gc = old
        
    def dumpNewObjects (self,event=None):
        
        '''Print a summary of all Python objects created
        since the last time Python's Garbage collector was run.'''
    
        old = g.app.trace_gc
        g.app.trace_gc = True
        g.printGcObjects()
        g.app.trace_gc = old
        
    def verboseDumpObjects (self,event=None):
        
        '''Print a more verbose listing of all existing Python objects.'''
        
        old = g.app.trace_gc
        g.app.trace_gc = True
        g.printGcVerbose()
        g.app.trace_gc = old
    #@-node:AGP.20250415230112.889:dumpAll/New/VerboseObjects
    #@+node:AGP.20250415230112.890:enable/disableGcTrace
    def disableGcTrace (self,event=None):
        
        '''Enable tracing of Python's Garbage Collector.'''
        
        g.app.trace_gc = False
        
    def enableGcTrace (self,event=None):
        
        '''Disable tracing of Python's Garbage Collector.'''
        
        g.app.trace_gc = True
        g.app.trace_gc_inited = False
        g.enable_gc_debug()
    #@-node:AGP.20250415230112.890:enable/disableGcTrace
    #@+node:AGP.20250415230112.891:freeTreeWidgets
    def freeTreeWidgets (self,event=None):
        
        '''Free all widgets used in Leo's outline pane.'''
        
        c = self.c
        
        c.frame.tree.destroyWidgets()
        c.redraw_now()
    #@-node:AGP.20250415230112.891:freeTreeWidgets
    #@+node:AGP.20250415230112.892:printFocus
    # Doesn't work if the focus isn't in a pane with bindings!
    
    def printFocus (self,event=None):
        
        '''Print information about the requested focus (for debugging).'''
        
        c = self.c
        
        g.es_print('      hasFocusWidget: %s' % c.widget_name(c.hasFocusWidget))
        g.es_print('requestedFocusWidget: %s' % c.widget_name(c.requestedFocusWidget))
        g.es_print('           get_focus: %s' % c.widget_name(c.get_focus()))
    #@-node:AGP.20250415230112.892:printFocus
    #@+node:AGP.20250415230112.893:printGcSummary
    def printGcSummary (self,event=None):
        
        
        '''Print a brief summary of all Python objects.'''
    
        g.printGcSummary()
    #@-node:AGP.20250415230112.893:printGcSummary
    #@+node:AGP.20250415230112.894:printStats
    def printStats (self,event=None):
        
        '''Print statistics about the objects that Leo is using.'''
        
        c = self.c
        c.frame.tree.showStats()
        self.dumpAllObjects()
    #@-node:AGP.20250415230112.894:printStats
    #@+node:AGP.20250415230112.895:runUnitTest
    def runUnitTests (self,event=None):
        
        '''Run all unit tests contained in the presently selected outline.'''
        
        c = self.c
    
        leoTest.doTests(c,all=False)
    #@-node:AGP.20250415230112.895:runUnitTest
    #@-others
#@-node:AGP.20250415230112.882:debugCommandsClass
#@+node:AGP.20250415230112.896:editCommandsClass
class editCommandsClass (baseEditCommandsClass):
    
    '''Contains editing commands with little or no state.'''

    #@    @+others
    #@+node:AGP.20250415230112.897: birth
    #@+node:AGP.20250415230112.898: ctor (editCommandsClass)
    def __init__ (self,c):
    
        baseEditCommandsClass.__init__(self,c) # init the base class.
        
        self.ccolumn = '0'   # For comment column functions.
        self.dynaregex = re.compile(r'[%s%s\-_]+'%(string.ascii_letters,string.digits))
            # Not a unicode problem.
            # For dynamic abbreviations
        self.extendMode = False # True: all cursor move commands extend the selection.
        self.fillPrefix = '' # For fill prefix functions.
        self.fillColumn = 70 # For line centering.
        self.moveSpotNode = None # A tnode.
        self.moveSpot = None # For retaining preferred column when moving up or down.
        self.moveCol = None # For retaining preferred column when moving up or down.
        self.store ={'rlist':[], 'stext':''} # For dynamic expansion.
        self.sampleWidget = None # Created later.
        self.swapSpots = []
        self._useRegex = False # For replace-string
        self.w = None # For use by state handlers.
        
        # Settings...
        self.autocompleteBrackets   = c.config.getBool('autocomplete-brackets')
        self.bracketsFlashBg        = c.config.getColor('flash-brackets-background-color')
        self.bracketsFlashCount     = c.config.getInt('flash-brackets-count')
        self.bracketsFlashDelay     = c.config.getInt('flash-brackets-delay')
        self.bracketsFlashFg        = c.config.getColor('flash-brackets-foreground-color')
        self.flashMatchingBrackets  = c.config.getBool('flash-matching-brackets')
        self.smartAutoIndent        = c.config.getBool('smart_auto_indent')
        
        self.initBracketMatcher(c)
    #@-node:AGP.20250415230112.898: ctor (editCommandsClass)
    #@+node:AGP.20250415230112.899: getPublicCommands (editCommandsClass)
    def getPublicCommands (self):        
    
        c = self.c ; k = self.k 
    
        return {
            'activate-cmds-menu':                   self.activateCmdsMenu,
            'activate-edit-menu':                   self.activateEditMenu,
            'activate-file-menu':                   self.activateFileMenu,
            'activate-help-menu':                   self.activateHelpMenu,
            'activate-outline-menu':                self.activateOutlineMenu,
            'activate-plugins-menu':                self.activatePluginsMenu,
            'activate-window-menu':                 self.activateWindowMenu,
            'add-editor':                           c.frame.body.addEditor,
            'add-space-to-lines':                   self.addSpaceToLines,
            'add-tab-to-lines':                     self.addTabToLines, 
            'back-to-indentation':                  self.backToIndentation,
            'back-char':                            self.backCharacter,
            'back-char-extend-selection':           self.backCharacterExtendSelection,
            'back-paragraph':                       self.backwardParagraph,
            'back-paragraph-extend-selection':      self.backwardParagraphExtendSelection,
            'back-sentence':                        self.backSentence,
            'back-sentence-extend-selection':       self.backSentenceExtendSelection,
            'back-word':                            self.backwardWord,
            'back-word-extend-selection':           self.backwardWordExtendSelection,
            'backward-delete-char':                 self.backwardDeleteCharacter,
            'backward-kill-paragraph':              self.backwardKillParagraph,
            'backward-find-character':              self.backwardFindCharacter,
            'backward-find-character-extend-selection': self.backwardFindCharacterExtendSelection,
            'beginning-of-buffer':                  self.beginningOfBuffer,
            'beginning-of-buffer-extend-selection': self.beginningOfBufferExtendSelection,
            'beginning-of-line':                    self.beginningOfLine,
            'beginning-of-line-extend-selection':   self.beginningOfLineExtendSelection,
            'capitalize-word':                      self.capitalizeWord,
            'center-line':                          self.centerLine,
            'center-region':                        self.centerRegion,
            'clean-lines':                          self.cleanLines,
            'clear-extend-mode':                    self.clearExtendMode,
            'clear-selected-text':                  self.clearSelectedText,
            'click-click-box':                      self.clickClickBox,
            'click-headline':                       self.clickHeadline,
            'click-icon-box':                       self.clickIconBox,
            'contract-body-pane':                   c.frame.contractBodyPane,
            'contract-log-pane':                    c.frame.contractLogPane,
            'contract-outline-pane':                c.frame.contractOutlinePane,
            'contract-pane':                        c.frame.contractPane,
            'count-region':                         self.countRegion,
            'cycle-focus':                          self.cycleFocus,
            'cycle-all-focus':                      self.cycleAllFocus,
            'cycle-editor-focus':                   c.frame.body.cycleEditorFocus,
            'dabbrev-completion':                   self.dynamicExpansion2,
            'dabbrev-expands':                      self.dynamicExpansion,
            'delete-char':                          self.deleteNextChar,
            'delete-editor':                        c.frame.body.deleteEditor,
            'delete-indentation':                   self.deleteIndentation,
            'delete-spaces':                        self.deleteSpaces,
            'do-nothing':                           self.doNothing,
            'downcase-region':                      self.downCaseRegion,
            'downcase-word':                        self.downCaseWord,
            'double-click-headline':                self.doubleClickHeadline,
            'double-click-icon-box':                self.doubleClickIconBox,
            'end-of-buffer':                        self.endOfBuffer,
            'end-of-buffer-extend-selection':       self.endOfBufferExtendSelection,
            'end-of-line':                          self.endOfLine,
            'end-of-line-extend-selection':         self.endOfLineExtendSelection,
            'escape':                               self.watchEscape,
            'eval-expression':                      self.evalExpression,
            'exchange-point-mark':                  self.exchangePointMark,
            'expand-body-pane':                     c.frame.expandBodyPane,
            'expand-log-pane':                      c.frame.expandLogPane,
            'expand-outline-pane':                  c.frame.expandOutlinePane,
            'expand-pane':                          c.frame.expandPane,
            'extend-to-line':                       self.extendToLine,
            'extend-to-paragraph':                  self.extendToParagraph,
            'extend-to-sentence':                   self.extendToSentence,
            'extend-to-word':                       self.extendToWord,
            'fill-paragraph':                       self.fillParagraph,
            'fill-region':                          self.fillRegion,
            'fill-region-as-paragraph':             self.fillRegionAsParagraph,
            'find-character':                       self.findCharacter,
            'find-character-extend-selection':      self.findCharacterExtendSelection,
            'find-word':                            self.findWord,
            'flush-lines':                          self.flushLines,
            'focus-to-body':                        self.focusToBody,
            'focus-to-log':                         self.focusToLog,
            'focus-to-minibuffer':                  self.focusToMinibuffer,
            'focus-to-tree':                        self.focusToTree,
            'forward-char':                         self.forwardCharacter,
            'forward-char-extend-selection':        self.forwardCharacterExtendSelection,
            'forward-paragraph':                    self.forwardParagraph,
            'forward-paragraph-extend-selection':   self.forwardParagraphExtendSelection,
            'forward-sentence':                     self.forwardSentence,
            'forward-sentence-extend-selection':    self.forwardSentenceExtendSelection,
            'forward-end-word':                     self.forwardEndWord, # New in Leo 4.4.2.
            'forward-end-word-extend-selection':    self.forwardEndWordExtendSelection, # New in Leo 4.4.2.
            'forward-word':                         self.forwardWord,
            'forward-word-extend-selection':        self.forwardWordExtendSelection,
            'fully-expand-body-pane':               c.frame.fullyExpandBodyPane,
            'fully-expand-log-pane':                c.frame.fullyExpandLogPane,
            'fully-expand-pane':                    c.frame.fullyExpandPane,
            'fully-expand-outline-pane':            c.frame.fullyExpandOutlinePane,
            'goto-char':                            self.gotoCharacter,
            'goto-global-line':                     self.gotoGlobalLine,
            'goto-line':                            self.gotoLine,
            'hide-body-pane':                       c.frame.hideBodyPane,
            'hide-log-pane':                        c.frame.hideLogPane,
            'hide-pane':                            c.frame.hidePane,
            'hide-outline-pane':                    c.frame.hideOutlinePane,
            'how-many':                             self.howMany,
            # Use indentBody in leoCommands.py
            'indent-relative':                      self.indentRelative,
            'indent-rigidly':                       self.tabIndentRegion,
            'indent-to-comment-column':             self.indentToCommentColumn,
            'insert-newline':                       self.insertNewline,
            'insert-parentheses':                   self.insertParentheses,
            'keep-lines':                           self.keepLines,
            'kill-paragraph':                       self.killParagraph,
            'line-number':                          self.lineNumber,
            'move-lines-down':                      self.moveLinesDown,
            'move-lines-up':                        self.moveLinesUp,
            'move-past-close':                      self.movePastClose,
            'move-past-close-extend-selection':     self.movePastCloseExtendSelection,
            'newline-and-indent':                   self.insertNewLineAndTab,
            'next-line':                            self.nextLine,
            'next-line-extend-selection':           self.nextLineExtendSelection,
            'previous-line':                        self.prevLine,
            'previous-line-extend-selection':       self.prevLineExtendSelection,
            'remove-blank-lines':                   self.removeBlankLines,
            'remove-space-from-lines':              self.removeSpaceFromLines,
            'remove-tab-from-lines':                self.removeTabFromLines,
            'reverse-region':                       self.reverseRegion,
            'scroll-down':                          self.scrollDown,
            'scroll-down-extend-selection':         self.scrollDownExtendSelection,
            'scroll-outline-down-line':             self.scrollOutlineDownLine,
            'scroll-outline-down-page':             self.scrollOutlineDownPage,
            'scroll-outline-left':                  self.scrollOutlineLeft,
            'scroll-outline-right':                 self.scrollOutlineRight,
            'scroll-outline-up-line':               self.scrollOutlineUpLine,
            'scroll-outline-up-page':               self.scrollOutlineUpPage,
            'scroll-up':                            self.scrollUp,
            'scroll-up-extend-selection':           self.scrollUpExtendSelection,
            # Exists, but can not be executed via the minibuffer.
            # 'self-insert-command':                self.selfInsertCommand,
            'set-comment-column':                   self.setCommentColumn,
            'set-extend-mode':                      self.setExtendMode,
            'set-fill-column':                      self.setFillColumn,
            'set-fill-prefix':                      self.setFillPrefix,
            #'set-mark-command':                    self.setRegion,
            #'show-colors':                          self.showColors,
            #'show-fonts':                           self.showFonts,
            'simulate-begin-drag':                  self.simulateBeginDrag,
            'simulate-end-drag':                    self.simulateEndDrag,
            'sort-columns':                         self.sortColumns,
            'sort-fields':                          self.sortFields,
            'sort-lines':                           self.sortLines,
            'split-line':                           self.splitLine,
            'tabify':                               self.tabify,
            'toggle-extend-mode':                   self.toggleExtendMode,
            'transpose-chars':                      self.transposeCharacters,
            'transpose-lines':                      self.transposeLines,
            'transpose-words':                      self.transposeWords,
            'untabify':                             self.untabify,
            'upcase-region':                        self.upCaseRegion,
            'upcase-word':                          self.upCaseWord,
            'view-lossage':                         self.viewLossage,
            'what-line':                            self.whatLine,
        }
    #@-node:AGP.20250415230112.899: getPublicCommands (editCommandsClass)
    #@+node:AGP.20250415230112.900:doNothing
    def doNothing (self,event):
        
        '''A placeholder command, useful for testing bindings.'''
    
        g.trace()
    #@nonl
    #@-node:AGP.20250415230112.900:doNothing
    #@-node:AGP.20250415230112.897: birth
    #@+node:AGP.20250415230112.901:capitalization & case
    #@+node:AGP.20250415230112.902:capitalizeWord & up/downCaseWord
    def capitalizeWord (self,event):
        '''Capitalize the word at the cursor.'''
        self.capitalizeHelper(event,'cap','capitalize-word')
    
    def downCaseWord (self,event):
        '''Convert all characters of the word at the cursor to lower case.'''
        self.capitalizeHelper(event,'low','downcase-word')
    
    def upCaseWord (self,event):
        '''Convert all characters of the word at the cursor to UPPER CASE.'''
        self.capitalizeHelper(event,'up','upcase-word')
    #@-node:AGP.20250415230112.902:capitalizeWord & up/downCaseWord
    #@+node:AGP.20250415230112.903:changePreviousWord (not used)
    def changePreviousWord (self,event):
    
        k = self.k ; stroke = k.stroke
        w = self.editWidget(event)
        if not w: return
    
        i = w.index('insert')
        self.beginCommand(undoType='change-previous-word')
        self.moveWordHelper(event,extend=False,forward=False)
    
        if stroke == '<Alt-c>':
            self.capitalizeWord(event)
        elif stroke == '<Alt-u>':
             self.upCaseWord(event)
        elif stroke == '<Alt-l>':
            self.downCaseWord(event)
    
        w.mark_set('insert',i)
        
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.903:changePreviousWord (not used)
    #@+node:AGP.20250415230112.904:capitalizeHelper
    def capitalizeHelper (self,event,which,undoType):
    
        w = self.editWidget(event)
        if not w: return
    
        text = w.get('insert wordstart','insert wordend')
        i = w.index('insert')
        if text == ' ': return
        
        self.beginCommand(undoType=undoType)
        
        w.delete('insert wordstart','insert wordend')
        if which == 'cap':
            text = text.capitalize()
        if which == 'low':
            text = text.lower()
        if which == 'up':
            text = text.upper()
        w.insert('insert',text)
        w.mark_set('insert',i)
        
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.904:capitalizeHelper
    #@-node:AGP.20250415230112.901:capitalization & case
    #@+node:AGP.20250415230112.905:clicks and focus (editCommandsClass)
    #@+node:AGP.20250415230112.906:activate-x-menu & activateMenu (editCommandsClass)
    def activateCmdsMenu    (self,event=None):
        '''Activate Leo's Cmnds menu.'''
        self.activateMenu('Cmds')
    
    def activateEditMenu    (self,event=None):
        '''Activate Leo's Edit menu.'''
        self.activateMenu('Edit')
    
    def activateFileMenu    (self,event=None):
        '''Activate Leo's File menu.'''
        self.activateMenu('File')
    
    def activateHelpMenu    (self,event=None):
        '''Activate Leo's Help menu.'''
        self.activateMenu('Help')
    
    def activateOutlineMenu (self,event=None):
        '''Activate Leo's Outline menu.'''
        self.activateMenu('Outline')
    
    def activatePluginsMenu (self,event=None):
        '''Activate Leo's Plugins menu.'''
        self.activateMenu('Plugins')
    
    def activateWindowMenu  (self,event=None):
        '''Activate Leo's Window menu.'''
        self.activateMenu('Window')
    
    def activateMenu (self,menuName):
        c = self.c
        c.frame.menu.activateMenu(menuName)
    #@-node:AGP.20250415230112.906:activate-x-menu & activateMenu (editCommandsClass)
    #@+node:AGP.20250415230112.907:cycleFocus
    def cycleFocus (self,event):
        
        '''Cycle the keyboard focus between Leo's outline, body and log panes.'''
    
        c = self.c ;  w = event.widget
       
        
        body = c.frame.body.bodyCtrl
        log  = c.frame.log.logCtrl
        tree = c.frame.tree.canvas
        panes = [body,log,tree]
    
        if w in panes:
            i = panes.index(w) + 1
            if i >= len(panes): i = 0
            pane = panes[i]
        else:
            pane = body
        
        # Warning: traces mess up the focus
        # print g.app.gui.widget_name(w),g.app.gui.widget_name(pane)
        
        # This works from the minibuffer *only* if there is no typing completion.
        c.widgetWantsFocusNow(pane)
        c.k.newMinibufferWidget = pane
    #@nonl
    #@-node:AGP.20250415230112.907:cycleFocus
    #@+node:AGP.20250415230112.908:cycleAllFocus
    editWidgetCount = 0
    logWidgetCount = 0
    
    def cycleAllFocus (self,event):
        
        '''Cycle the keyboard focus between Leo's outline,
        all body editors and all tabs in the log pane.'''
    
        c = self.c ; k = c.k
        w = event and event.widget # Does **not** require a text widget.
    
        pane = None ; w_name = g.app.gui.widget_name
        trace = False
        if trace: print (
            '---- w',w_name(w),id(w),
            '#tabs',c.frame.log.numberOfVisibleTabs(),
            'bodyCtrl',w_name(c.frame.body.bodyCtrl),id(c.frame.body.bodyCtrl))
    
        # w may not be the present body widget, so test its name, not its id.
        if w_name(w).startswith('body'):
            n = c.frame.body.numberOfEditors
            # g.trace(self.editWidgetCount,n)
            if n > 1:
                self.editWidgetCount += 1
                if self.editWidgetCount == 1:
                    pane = c.frame.body.bodyCtrl
                elif self.editWidgetCount > n:
                    self.editWidgetCount = 0 ; self.logWidgetCount = 1
                    c.frame.log.selectTab('Log')
                    pane = c.frame.log.logCtrl
                else:
                    c.frame.body.cycleEditorFocus(event) ; pane = None
            else:
                self.editWidgetCount = 0 ; self.logWidgetCount = 1
                c.frame.log.selectTab('Log')
                pane = c.frame.log.logCtrl
        elif w_name(w).startswith('log'):
            n = c.frame.log.numberOfVisibleTabs()
            if n > 1:
                self.logWidgetCount += 1
                if self.logWidgetCount == 1:
                    c.frame.log.selectTab('Log')
                    pane = c.frame.log.logCtrl
                elif self.logWidgetCount > n:
                    self.logWidgetCount = 0
                    pane = c.frame.tree.canvas
                else:
                    c.frame.log.cycleTabFocus()
                    pane = c.frame.log.logCtrl
            else:
                self.logWidgetCount = 0
                pane = c.frame.tree.canvas
        else:
            pane = c.frame.body.bodyCtrl
            self.editWidgetCount = 1 ; self.logWidgetCount = 0
            
        if trace: print 'old: %10s new: %10s' % (w_name(w),w_name(pane))
    
        if pane:
            k.newMinibufferWidget = pane
            c.widgetWantsFocusNow(pane)
    #@nonl
    #@-node:AGP.20250415230112.908:cycleAllFocus
    #@+node:AGP.20250415230112.909:focusTo...
    def focusToBody (self,event):
        '''Put the keyboard focus in Leo's body pane.'''
        self.c.bodyWantsFocusNow()
    
    def focusToLog (self,event):
        '''Put the keyboard focus in Leo's log pane.'''
        self.c.logWantsFocusNow()
        
    def focusToMinibuffer (self,event):
        '''Put the keyboard focus in Leo's minibuffer.'''
        self.c.minibufferWantsFocusNow()
    
    def focusToTree (self,event):
        '''Put the keyboard focus in Leo's outline pane.'''
        self.c.treeWantsFocusNow()
    #@-node:AGP.20250415230112.909:focusTo...
    #@+node:AGP.20250415230112.910:clicks in the headline
    # These call the actual event handlers so as to trigger hooks.
    
    def clickHeadline (self,event=None):
        '''Simulate a click in the headline of the presently selected node.'''
        c = self.c ; p = c.currentPosition()
        c.frame.tree.onHeadlineClick(event,p=p)
        
    def doubleClickHeadline (self,event=None):
        '''Simulate a double click in headline of the presently selected node.'''
        return self.clickHeadline(event)
    
    def rightClickHeadline (self,event=None):
        '''Simulate a right click in the headline of the presently selected node.'''
        c = self.c ; p = c.currentPosition()
        c.frame.tree.onHeadlineRightClick(event,p=p)
    #@-node:AGP.20250415230112.910:clicks in the headline
    #@+node:AGP.20250415230112.911:clicks in the icon box
    # These call the actual event handlers so as to trigger hooks.
    
    def clickIconBox (self,event=None):
        '''Simulate a click in the icon box of the presently selected node.'''
        c = self.c ; p = c.currentPosition()
        c.frame.tree.onIconBoxClick(event,p=p)
    
    def doubleClickIconBox (self,event=None):
        '''Simulate a double-click in the icon box of the presently selected node.'''
        c = self.c ; p = c.currentPosition()
        c.frame.tree.onIconBoxDoubleClick(event,p=p)
    
    def rightClickIconBox (self,event=None):
    
        '''Simulate a right click in the icon box of the presently selected node.'''
        c = self.c ; p = c.currentPosition()
        c.frame.tree.onIconBoxRightClick(event,p=p)
    #@-node:AGP.20250415230112.911:clicks in the icon box
    #@+node:AGP.20250415230112.912:clickClickBox
    # Call the actual event handlers so as to trigger hooks.
    
    def clickClickBox (self,event=None):
    
        '''Simulate a click in the click box (+- box) of the presently selected node.'''
    
        c = self.c ; p = c.currentPosition()
        c.frame.tree.onClickBoxClick(event,p=p)
    #@-node:AGP.20250415230112.912:clickClickBox
    #@+node:AGP.20250415230112.913:simulate...Drag
    # These call the drag setup methods which in turn trigger hooks.
    
    def simulateBeginDrag (self,event=None):
    
        '''Simulate the start of a drag in the presently selected node.'''
        c = self.c ; p = c.currentPosition()
        c.frame.tree.startDrag(event,p=p)
    
    def simulateEndDrag (self,event=None):
    
        '''Simulate the end of a drag in the presently selected node.'''
        c = self.c
        
        # Note: this assumes that tree.startDrag has already been called.
        c.frame.tree.endDrag(event)
    #@-node:AGP.20250415230112.913:simulate...Drag
    #@-node:AGP.20250415230112.905:clicks and focus (editCommandsClass)
    #@+node:AGP.20250415230112.914:color & font
    #@+node:AGP.20250415230112.915:show-colors
    def showColors (self,event):
        
        '''Open a tab in the log pane showing various color pickers.'''
        
        c = self.c ; log = c.frame.log ; tabName = 'Colors'
        
        #@    << define colors >>
        #@+node:AGP.20250415230112.916:<< define colors >>
        colors = (
            "gray60", "gray70", "gray80", "gray85", "gray90", "gray95",
            "snow1", "snow2", "snow3", "snow4", "seashell1", "seashell2",
            "seashell3", "seashell4", "AntiqueWhite1", "AntiqueWhite2", "AntiqueWhite3",
            "AntiqueWhite4", "bisque1", "bisque2", "bisque3", "bisque4", "PeachPuff1",
            "PeachPuff2", "PeachPuff3", "PeachPuff4", "NavajoWhite1", "NavajoWhite2",
            "NavajoWhite3", "NavajoWhite4", "LemonChiffon1", "LemonChiffon2",
            "LemonChiffon3", "LemonChiffon4", "cornsilk1", "cornsilk2", "cornsilk3",
            "cornsilk4", "ivory1", "ivory2", "ivory3", "ivory4", "honeydew1", "honeydew2",
            "honeydew3", "honeydew4", "LavenderBlush1", "LavenderBlush2",
            "LavenderBlush3", "LavenderBlush4", "MistyRose1", "MistyRose2",
            "MistyRose3", "MistyRose4", "azure1", "azure2", "azure3", "azure4",
            "SlateBlue1", "SlateBlue2", "SlateBlue3", "SlateBlue4", "RoyalBlue1",
            "RoyalBlue2", "RoyalBlue3", "RoyalBlue4", "blue1", "blue2", "blue3", "blue4",
            "DodgerBlue1", "DodgerBlue2", "DodgerBlue3", "DodgerBlue4", "SteelBlue1",
            "SteelBlue2", "SteelBlue3", "SteelBlue4", "DeepSkyBlue1", "DeepSkyBlue2",
            "DeepSkyBlue3", "DeepSkyBlue4", "SkyBlue1", "SkyBlue2", "SkyBlue3",
            "SkyBlue4", "LightSkyBlue1", "LightSkyBlue2", "LightSkyBlue3",
            "LightSkyBlue4", "SlateGray1", "SlateGray2", "SlateGray3", "SlateGray4",
            "LightSteelBlue1", "LightSteelBlue2", "LightSteelBlue3",
            "LightSteelBlue4", "LightBlue1", "LightBlue2", "LightBlue3",
            "LightBlue4", "LightCyan1", "LightCyan2", "LightCyan3", "LightCyan4",
            "PaleTurquoise1", "PaleTurquoise2", "PaleTurquoise3", "PaleTurquoise4",
            "CadetBlue1", "CadetBlue2", "CadetBlue3", "CadetBlue4", "turquoise1",
            "turquoise2", "turquoise3", "turquoise4", "cyan1", "cyan2", "cyan3", "cyan4",
            "DarkSlateGray1", "DarkSlateGray2", "DarkSlateGray3",
            "DarkSlateGray4", "aquamarine1", "aquamarine2", "aquamarine3",
            "aquamarine4", "DarkSeaGreen1", "DarkSeaGreen2", "DarkSeaGreen3",
            "DarkSeaGreen4", "SeaGreen1", "SeaGreen2", "SeaGreen3", "SeaGreen4",
            "PaleGreen1", "PaleGreen2", "PaleGreen3", "PaleGreen4", "SpringGreen1",
            "SpringGreen2", "SpringGreen3", "SpringGreen4", "green1", "green2",
            "green3", "green4", "chartreuse1", "chartreuse2", "chartreuse3",
            "chartreuse4", "OliveDrab1", "OliveDrab2", "OliveDrab3", "OliveDrab4",
            "DarkOliveGreen1", "DarkOliveGreen2", "DarkOliveGreen3",
            "DarkOliveGreen4", "khaki1", "khaki2", "khaki3", "khaki4",
            "LightGoldenrod1", "LightGoldenrod2", "LightGoldenrod3",
            "LightGoldenrod4", "LightYellow1", "LightYellow2", "LightYellow3",
            "LightYellow4", "yellow1", "yellow2", "yellow3", "yellow4", "gold1", "gold2",
            "gold3", "gold4", "goldenrod1", "goldenrod2", "goldenrod3", "goldenrod4",
            "DarkGoldenrod1", "DarkGoldenrod2", "DarkGoldenrod3", "DarkGoldenrod4",
            "RosyBrown1", "RosyBrown2", "RosyBrown3", "RosyBrown4", "IndianRed1",
            "IndianRed2", "IndianRed3", "IndianRed4", "sienna1", "sienna2", "sienna3",
            "sienna4", "burlywood1", "burlywood2", "burlywood3", "burlywood4", "wheat1",
            "wheat2", "wheat3", "wheat4", "tan1", "tan2", "tan3", "tan4", "chocolate1",
            "chocolate2", "chocolate3", "chocolate4", "firebrick1", "firebrick2",
            "firebrick3", "firebrick4", "brown1", "brown2", "brown3", "brown4", "salmon1",
            "salmon2", "salmon3", "salmon4", "LightSalmon1", "LightSalmon2",
            "LightSalmon3", "LightSalmon4", "orange1", "orange2", "orange3", "orange4",
            "DarkOrange1", "DarkOrange2", "DarkOrange3", "DarkOrange4", "coral1",
            "coral2", "coral3", "coral4", "tomato1", "tomato2", "tomato3", "tomato4",
            "OrangeRed1", "OrangeRed2", "OrangeRed3", "OrangeRed4", "red1", "red2", "red3",
            "red4", "DeepPink1", "DeepPink2", "DeepPink3", "DeepPink4", "HotPink1",
            "HotPink2", "HotPink3", "HotPink4", "pink1", "pink2", "pink3", "pink4",
            "LightPink1", "LightPink2", "LightPink3", "LightPink4", "PaleVioletRed1",
            "PaleVioletRed2", "PaleVioletRed3", "PaleVioletRed4", "maroon1",
            "maroon2", "maroon3", "maroon4", "VioletRed1", "VioletRed2", "VioletRed3",
            "VioletRed4", "magenta1", "magenta2", "magenta3", "magenta4", "orchid1",
            "orchid2", "orchid3", "orchid4", "plum1", "plum2", "plum3", "plum4",
            "MediumOrchid1", "MediumOrchid2", "MediumOrchid3", "MediumOrchid4",
            "DarkOrchid1", "DarkOrchid2", "DarkOrchid3", "DarkOrchid4", "purple1",
            "purple2", "purple3", "purple4", "MediumPurple1", "MediumPurple2",
            "MediumPurple3", "MediumPurple4", "thistle1", "thistle2", "thistle3",
            "thistle4" )
        #@-node:AGP.20250415230112.916:<< define colors >>
        #@nl
        
        if log.frameDict.get(tabName):
            log.selectTab(tabName)
        else:
            log.selectTab(tabName)
            t = log.textDict.get(tabName)
            t.pack_forget()
            f = log.frameDict.get(tabName)
            self.createColorPicker(f,colors)
    #@+node:AGP.20250415230112.917:createColorPicker
    def createColorPicker (self,parent,colors):
        
        colors = list(colors)
        bg = parent.cget('background')
        
        outer = Tk.Frame(parent,background=bg)
        outer.pack(side='top',fill='both',expand=1,pady=10)
        
        f = Tk.Frame(outer)
        f.pack(side='top',expand=0,fill='x')
        f1 = Tk.Frame(f) ; f1.pack(side='top',expand=0,fill='x')
        f2 = Tk.Frame(f) ; f2.pack(side='top',expand=1,fill='x')
        f3 = Tk.Frame(f) ; f3.pack(side='top',expand=1,fill='x')
        
        label = Tk.Text(f1,height=1,width=20)
        label.insert('1.0','Color name or value...')
        label.pack(side='left',pady=6)
    
        #@    << create optionMenu and callback >>
        #@+node:AGP.20250415230112.918:<< create optionMenu and callback >>
        colorBox = Pmw.ComboBox(f2,scrolledlist_items=colors)
        colorBox.pack(side='left',pady=4)
        
        def colorCallback (newName): 
            label.delete('1.0','end')
            label.insert('1.0',newName)
            try:
                for theFrame in (parent,outer,f,f1,f2,f3):
                    theFrame.configure(background=newName)
            except: pass # Ignore invalid names.
        
        colorBox.configure(selectioncommand=colorCallback)
        #@-node:AGP.20250415230112.918:<< create optionMenu and callback >>
        #@nl
        #@    << create picker button and callback >>
        #@+node:AGP.20250415230112.919:<< create picker button and callback >>
        def pickerCallback ():
            rgb,val = tkColorChooser.askcolor(parent=parent,initialcolor=f.cget('background'))
            if rgb or val:
                # label.configure(text=val)
                label.delete('1.0','end')
                label.insert('1.0',val)
                for theFrame in (parent,outer,f,f1,f2,f3):
                    theFrame.configure(background=val)
        
        b = Tk.Button(f3,text="Color Picker...",
            command=pickerCallback,background=bg)
        b.pack(side='left',pady=4)
        #@-node:AGP.20250415230112.919:<< create picker button and callback >>
        #@nl
    #@-node:AGP.20250415230112.917:createColorPicker
    #@-node:AGP.20250415230112.915:show-colors
    #@+node:AGP.20250415230112.920:show-fonts & helpers
    def showFonts (self,event):
        
        '''Open a tab in the log pane showing a font picker.'''
    
        c = self.c ; log = c.frame.log ; tabName = 'Fonts'
    
        if log.frameDict.get(tabName):
            log.selectTab(tabName)
        else:
            log.selectTab(tabName)
            f = log.frameDict.get(tabName)
            t = log.textDict.get(tabName)
            t.pack_forget()
            self.createFontPicker(f)
    #@+node:AGP.20250415230112.921:createFontPicker
    def createFontPicker (self,parent):
    
        bg = parent.cget('background')
        font = self.getFont()
        #@    << create the frames >>
        #@+node:AGP.20250415230112.922:<< create the frames >>
        f = Tk.Frame(parent,background=bg) ; f.pack (side='top',expand=0,fill='both')
        f1 = Tk.Frame(f,background=bg)     ; f1.pack(side='top',expand=1,fill='x')
        f2 = Tk.Frame(f,background=bg)     ; f2.pack(side='top',expand=1,fill='x')
        f3 = Tk.Frame(f,background=bg)     ; f3.pack(side='top',expand=1,fill='x')
        f4 = Tk.Frame(f,background=bg)     ; f4.pack(side='top',expand=1,fill='x')
        #@-node:AGP.20250415230112.922:<< create the frames >>
        #@nl
        #@    << create the family combo box >>
        #@+node:AGP.20250415230112.923:<< create the family combo box >>
        names = tkFont.families()
        names = list(names)
        names.sort()
        names.insert(0,'<None>')
        
        self.familyBox = familyBox = Pmw.ComboBox(f1,
            labelpos="we",label_text='Family:',label_width=10,
            label_background=bg,
            arrowbutton_background=bg,
            scrolledlist_items=names)
        
        familyBox.selectitem(0)
        familyBox.pack(side="left",padx=2,pady=2)
        #@-node:AGP.20250415230112.923:<< create the family combo box >>
        #@nl
        #@    << create the size entry >>
        #@+node:AGP.20250415230112.924:<< create the size entry >>
        Tk.Label(f2,text="Size:",width=10,background=bg).pack(side="left")
        
        sizeEntry = Tk.Entry(f2,width=4)
        sizeEntry.insert(0,'12')
        sizeEntry.pack(side="left",padx=2,pady=2)
        #@-node:AGP.20250415230112.924:<< create the size entry >>
        #@nl
        #@    << create the weight combo box >>
        #@+node:AGP.20250415230112.925:<< create the weight combo box >>
        weightBox = Pmw.ComboBox(f3,
            labelpos="we",label_text="Weight:",label_width=10,
            label_background=bg,
            arrowbutton_background=bg,
            scrolledlist_items=['normal','bold'])
        
        weightBox.selectitem(0)
        weightBox.pack(side="left",padx=2,pady=2)
        #@-node:AGP.20250415230112.925:<< create the weight combo box >>
        #@nl
        #@    << create the slant combo box >>
        #@+node:AGP.20250415230112.926:<< create the slant combo box>>
        slantBox = Pmw.ComboBox(f4,
            labelpos="we",label_text="Slant:",label_width=10,
            label_background=bg,
            arrowbutton_background=bg,
            scrolledlist_items=['roman','italic'])
        
        slantBox.selectitem(0)
        slantBox.pack(side="left",padx=2,pady=2)
        #@-node:AGP.20250415230112.926:<< create the slant combo box>>
        #@nl
        #@    << create the sample text widget >>
        #@+node:AGP.20250415230112.927:<< create the sample text widget >>
        self.sampleWidget = sample = Tk.Text(f,height=20,width=80,font=font)
        sample.pack(side='left')
        
        s = 'The quick brown fox\njumped over the lazy dog.\n0123456789'
        sample.insert('1.0',s)
        #@-node:AGP.20250415230112.927:<< create the sample text widget >>
        #@nl
        #@    << create and bind the callbacks >>
        #@+node:AGP.20250415230112.928:<< create and bind the callbacks >>
        def fontCallback(event=None):
            self.setFont(familyBox,sizeEntry,slantBox,weightBox,sample)
        
        for w in (familyBox,slantBox,weightBox):
            w.configure(selectioncommand=fontCallback)
        
        sizeEntry.bind('<Return>',fontCallback)
        #@-node:AGP.20250415230112.928:<< create and bind the callbacks >>
        #@nl
        self.createBindings()
    #@-node:AGP.20250415230112.921:createFontPicker
    #@+node:AGP.20250415230112.929:createBindings (fontPicker)
    def createBindings (self):
        
        c = self.c ; k = c.k
        
        table = (
            ('<Button-1>',  k.masterClickHandler),
            ('<Double-1>',  k.masterClickHandler),
            ('<Button-3>',  k.masterClickHandler),
            ('<Double-3>',  k.masterClickHandler),
            ('<Key>',       k.masterKeyHandler),
            ("<Escape>",    self.hideTab),
        )
    
        w = self.sampleWidget
        for event, callback in table:
            w.bind(event,callback)
            
        k.completeAllBindingsForWidget(w)
    #@-node:AGP.20250415230112.929:createBindings (fontPicker)
    #@+node:AGP.20250415230112.930:getFont
    def getFont(self,family=None,size=12,slant='roman',weight='normal'):
        
        try:
            return tkFont.Font(family=family,size=size,slant=slant,weight=weight)
        except Exception:
            g.es("exception setting font")
            g.es("family,size,slant,weight:",family,size,slant,weight)
            # g.es_exception() # This just confuses people.
            return g.app.config.defaultFont
    #@-node:AGP.20250415230112.930:getFont
    #@+node:AGP.20250415230112.931:setFont
    def setFont(self,familyBox,sizeEntry,slantBox,weightBox,label):
        
        d = {}
        for box,key in (
            (familyBox, 'family'),
            (None,      'size'),
            (slantBox,  'slant'),
            (weightBox, 'weight'),
        ):
            if box: val = box.get()
            else:
                val = sizeEntry.get().strip() or ''
                try: int(val)
                except ValueError: val = None
            if val and val.lower() not in ('none','<none>',):
                d[key] = val
    
        family=d.get('family',None)
        size=d.get('size',12)
        weight=d.get('weight','normal')
        slant=d.get('slant','roman')
        font = self.getFont(family,size,slant,weight)
        label.configure(font=font)
    #@-node:AGP.20250415230112.931:setFont
    #@+node:AGP.20250415230112.932:hideTab
    def hideTab (self,event=None):
        
        c = self.c
        c.frame.log.selectTab('Log')
        c.bodyWantsFocus()
    #@-node:AGP.20250415230112.932:hideTab
    #@-node:AGP.20250415230112.920:show-fonts & helpers
    #@-node:AGP.20250415230112.914:color & font
    #@+node:AGP.20250415230112.933:comment column...
    #@+node:AGP.20250415230112.934:setCommentColumn
    def setCommentColumn (self,event):
        
        '''Set the comment column for the indent-to-comment-column command.'''
    
        w = self.editWidget(event)
        if not w: return
    
        cc = w.index('insert')
        cc1, cc2 = cc.split('.')
        self.ccolumn = cc2
    #@-node:AGP.20250415230112.934:setCommentColumn
    #@+node:AGP.20250415230112.935:indentToCommentColumn
    def indentToCommentColumn (self,event):
    
        '''Insert whitespace to indent to the comment column.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
        
        self.beginCommand(undoType='indent-to-comment-column')
    
        i = w.index('insert lineend')
        i1, i2 = i.split('.')
        i2 = int(i2)
        c1 = int(self.ccolumn)
    
        if i2 < c1:
            wsn = c1- i2
            w.insert('insert lineend',' '*wsn)
        if i2 >= c1:
            w.insert('insert lineend',' ')
        w.mark_set('insert','insert lineend')
        
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.935:indentToCommentColumn
    #@-node:AGP.20250415230112.933:comment column...
    #@+node:AGP.20250415230112.936:dynamic abbreviation...
    #@+node:AGP.20250415230112.937:dynamicExpansion
    def dynamicExpansion (self,event): #, store = {'rlist': [], 'stext': ''} ):
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        rlist = self.store ['rlist']
        stext = self.store ['stext']
        i = w.index('insert -1c wordstart')
        i2 = w.index('insert -1c wordend')
        txt = w.get(i,i2)
        dA = w.tag_ranges('dA')
        w.tag_delete('dA')
        def doDa (txt,from_='insert -1c wordstart',to_='insert -1c wordend'):
            w.delete(from_,to_)
            w.insert('insert',txt,'dA')
    
        if dA:
            dA1, dA2 = dA
            dtext = w.get(dA1,dA2)
            if dtext.startswith(stext) and i2 == dA2:
                #This seems reasonable, since we cant get a whole word that has the '-' char in it, we do a good guess
                if rlist:
                    txt = rlist.pop()
                else:
                    txt = stext
                    w.delete(dA1,dA2)
                    dA2 = dA1 # since the text is going to be reread, we dont want to include the last dynamic abbreviation
                    self.getDynamicList(w,txt,rlist)
                doDa(txt,dA1,dA2) ; return
            else: dA = None
    
        if not dA:
            self.store ['stext'] = txt
            self.store ['rlist'] = rlist = []
            self.getDynamicList(w,txt,rlist)
            if not rlist: return
            txt = rlist.pop()
            doDa(txt)
    #@-node:AGP.20250415230112.937:dynamicExpansion
    #@+node:AGP.20250415230112.938:dynamicExpansion2
    def dynamicExpansion2 (self,event):
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        i = w.index('insert -1c wordstart')
        i2 = w.index('insert -1c wordend')
        txt = w.get(i,i2)
        rlist = []
        self.getDynamicList(w,txt,rlist)
        dEstring = reduce(g.longestCommonPrefix,rlist)
        if dEstring:
            w.delete(i,i2)
            w.insert(i,dEstring)
    #@-node:AGP.20250415230112.938:dynamicExpansion2
    #@+node:AGP.20250415230112.939:getDynamicList (helper)
    def getDynamicList (self,w,txt,rlist):
    
         ttext = w.get('1.0','end')
         items = self.dynaregex.findall(ttext) #make a big list of what we are considering a 'word'
         if items:
             for word in items:
                 if not word.startswith(txt) or word == txt: continue #dont need words that dont match or == the pattern
                 if word not in rlist:
                     rlist.append(word)
                 else:
                     rlist.remove(word)
                     rlist.append(word)
    #@-node:AGP.20250415230112.939:getDynamicList (helper)
    #@-node:AGP.20250415230112.936:dynamic abbreviation...
    #@+node:AGP.20250415230112.940:esc methods for Python evaluation
    #@+node:AGP.20250415230112.941:watchEscape (Revise)
    def watchEscape (self,event):
    
        k = self.k
    
        if not k.inState():
            k.setState('escape','start',handler=self.watchEscape)
            k.setLabelBlue('Esc ')
        elif k.getStateKind() == 'escape':
            state = k.getState('escape')
            # hi1 = k.keysymHistory [0]
            # hi2 = k.keysymHistory [1]
            data1 = leoKeys.keyHandlerClass.lossage[0]
            data2 = leoKeys.keyHandlerClass.lossage[1]
            ch1, stroke1 = data1
            ch2, stroke2 = data2
            
            if state == 'esc esc' and event.keysym == 'colon':
                self.evalExpression(event)
            elif state == 'evaluate':
                self.escEvaluate(event)
            # elif hi1 == hi2 == 'Escape':
            elif stroke1 == 'Escape' and stroke2 == 'Escape':
                k.setState('escape','esc esc')
                k.setLabel('Esc Esc -')
            elif event.keysym not in ('Shift_L','Shift_R'):
                k.keyboardQuit(event)
    #@-node:AGP.20250415230112.941:watchEscape (Revise)
    #@+node:AGP.20250415230112.942:escEvaluate (Revise)
    def escEvaluate (self,event):
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        if k.getLabel() == 'Eval:':
            k.setLabel('')
    
        if event.keysym == 'Return':
            expression = k.getLabel()
            try:
                ok = False
                result = eval(expression,{},{})
                result = str(result)
                w.insert('insert',result)
                ok = True
            finally:
                k.keyboardQuit(event)
                if not ok:
                    k.setLabel('Error: Invalid Expression')
        else:
            k.updateLabel(event)
    #@-node:AGP.20250415230112.942:escEvaluate (Revise)
    #@-node:AGP.20250415230112.940:esc methods for Python evaluation
    #@+node:AGP.20250415230112.943:evalExpression
    def evalExpression (self,event):
        
        '''Evaluate a Python Expression entered in the minibuffer.'''
    
        k = self.k ; state = k.getState('eval-expression')
        
        if state == 0:
            k.setLabelBlue('Eval: ',protect=True)
            k.getArg(event,'eval-expression',1,self.evalExpression)
        else:
            k.clearState()
            try:
                e = k.arg
                result = str(eval(e,{},{}))
                k.setLabelGrey('Eval: %s -> %s' % (e,result))
            except Exception:
                k.setLabelGrey('Invalid Expression: %s' % e)
    #@-node:AGP.20250415230112.943:evalExpression
    #@+node:AGP.20250415230112.944:fill column and centering
    #@+at
    # These methods are currently just used in tandem to center the line or 
    # region within the fill column.
    # for example, dependent upon the fill column, this text:
    # 
    # cats
    # raaaaaaaaaaaats
    # mats
    # zaaaaaaaaap
    # 
    # may look like
    # 
    #                                  cats
    #                            raaaaaaaaaaaats
    #                                  mats
    #                              zaaaaaaaaap
    # 
    # after an center-region command via Alt-x.
    #@-at
    #@@c
    
    #@+others
    #@+node:AGP.20250415230112.945:centerLine
    def centerLine (self,event):
    
        '''Centers line within current fill column'''
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        ind = w.index('insert linestart')
        txt = w.get('insert linestart','insert lineend')
        txt = txt.strip()
        if len(txt) >= self.fillColumn: return
        
        self.beginCommand(undoType='center-line')
    
        amount = (self.fillColumn-len(txt)) / 2
        ws = ' ' * amount
        col, nind = ind.split('.')
        ind = w.search('\w','insert linestart',regexp=True,stopindex='insert lineend')
        if ind:
            w.delete('insert linestart','%s' % ind)
            w.insert('insert linestart',ws)
            
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.945:centerLine
    #@+node:AGP.20250415230112.946:setFillColumn
    def setFillColumn (self,event):
        
        '''Set the fill column used by the center-line and center-region commands.'''
    
        k = self.k ; state = k.getState('set-fill-column')
        
        if state == 0:
            k.setLabelBlue('Set Fill Column: ')
            k.getArg(event,'set-fill-column',1,self.setFillColumn)
        else:
            k.clearState()
            try:
                n = int(k.arg)
                k.setLabelGrey('fill column is: %d' % n)
                k.commandName = 'set-fill-column %d' % n
            except ValueError:
                k.resetLabel()
    #@-node:AGP.20250415230112.946:setFillColumn
    #@+node:AGP.20250415230112.947:centerRegion
    def centerRegion( self, event ):
    
        '''Centers the selected text within the fill column'''
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        start = w.index( 'sel.first linestart' )
        sindex , x = start.split( '.' )
        sindex = int( sindex )
        end = w.index( 'sel.last linestart' )
        eindex , x = end.split( '.' )
        eindex = int( eindex )
        
        self.beginCommand(undoType='center-region')
    
        while sindex <= eindex:
            txt = w.get( '%s.0 linestart' % sindex , '%s.0 lineend' % sindex )
            txt = txt.strip()
            if len( txt ) >= self.fillColumn:
                sindex = sindex + 1
                continue
            amount = ( self.fillColumn - len( txt ) ) / 2
            ws = ' ' * amount
            ind = w.search( '\w', '%s.0' % sindex, regexp = True, stopindex = '%s.0 lineend' % sindex )
            if not ind: 
                sindex = sindex + 1
                continue
            w.delete( '%s.0' % sindex , '%s' % ind )
            w.insert( '%s.0' % sindex , ws )
            sindex = sindex + 1
            
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.947:centerRegion
    #@+node:AGP.20250415230112.948:setFillPrefix
    def setFillPrefix( self, event ):
        
        '''Make the selected text the fill prefix.'''
    
        w = self.editWidget(event)
        if not w: return
    
        txt = w.get( 'insert linestart', 'insert' )
        self.fillPrefix = txt
    #@-node:AGP.20250415230112.948:setFillPrefix
    #@+node:AGP.20250415230112.949:_addPrefix
    def _addPrefix (self,ntxt):
    
        ntxt = ntxt.split('.')
        ntxt = map(lambda a: self.fillPrefix+a,ntxt)
        ntxt = '.'.join(ntxt)
        return ntxt
    #@-node:AGP.20250415230112.949:_addPrefix
    #@-others
    #@-node:AGP.20250415230112.944:fill column and centering
    #@+node:AGP.20250415230112.950:find (quick)
    #@+node:AGP.20250415230112.951:backward/findCharacter & helper
    def backwardFindCharacter (self,event):
        return self.findCharacterHelper(event,backward=True,extend=False)
        
    def backwardFindCharacterExtendSelection (self,event):
        return self.findCharacterHelper(event,backward=True,extend=True)
        
    def findCharacter (self,event):
        return self.findCharacterHelper(event,backward=False,extend=False)
        
    def findCharacterExtendSelection (self,event):
        return self.findCharacterHelper(event,backward=False,extend=True)
    #@nonl
    #@+node:AGP.20250415230112.952:findCharacterHelper
    def findCharacterHelper (self,event,backward,extend):
    
        '''Put the cursor at the next occurance of a character on a line.'''
    
        c = self.c ; k = c.k ; tag = 'find-char' ; state = k.getState(tag)
    
        if state == 0:
            w = self.editWidget(event) # Sets self.w
            if not w: return
            self.event = event
            self.backward = backward ; self.extend = extend ;
            self.insert = w.index('insert')
            s = '%s character %s' % (
                g.choose(backward,'Backward find','Find'),
                g.choose(extend,' & extend',''))
            c.frame.clearStatusLine()
            c.frame.putStatusLine(s,color='blue')
            # Get the arg without touching the focus.
            k.getArg(event,tag,1,self.findCharacter,oneCharacter=True,useMinibuffer=False)
        else:
            event = self.event ; w = self.w
            backward = self.backward ; extend = self.extend
            ch = k.arg ; s = g.app.gui.getAllText(w)
            def toGui (i): return g.app.gui.toGuiIndex(s,w,i)
            def toPython (i): return g.app.gui.toPythonIndex(s,w,i)
            ins = toPython(self.insert)
            i = ins + g.choose(backward,-1,+1) # skip the present character.
            if backward:
                start = s.rfind('\n',0,i)
                if start == -1: start = 0
                j = s.rfind(ch,start,max(start,i)) # Skip the character at the cursor.
                if j > -1:
                    spot = toGui(j)
                    self.moveToHelper(event,spot,extend)
            else:
                end = s.find('\n',i)
                if end == -1: end = len(s)
                j = s.find(ch,min(i,end),end) # Skip the character at the cursor.
                if j > -1:
                    spot = toGui(j)
                    self.moveToHelper(event,spot,extend)
            c.frame.clearStatusLine()
            k.clearState()
    #@nonl
    #@-node:AGP.20250415230112.952:findCharacterHelper
    #@-node:AGP.20250415230112.951:backward/findCharacter & helper
    #@+node:AGP.20250415230112.953:findWord
    def findWord (self,event):
        
        '''Put the cursor at the next word (on a line) that starts with a character.'''
    
        k = self.k ; tag = 'find-word-on-line' ; state = k.getState(tag)
        
        if state == 0:
            w = self.editWidget(event) # Sets self.w
            if not w: return
            k.setLabelBlue('Find word: ')
            k.getArg(event,tag,1,self.findWord)
        else:        
            word = k.arg ; w = self.w ; c = k.c
            if word:
                i = w.index('insert')
                s = g.app.gui.getAllText(w)
                i = g.app.gui.toPythonIndex(s,w,i)
                j = s.find('\n',i) # Limit to this line.
                s = s[:j]
                while i < len(s):
                    if i == -1: break
                    ok = g.match_word(s,i,word) and (i == 0 or not g.isWordChar(s[i-1]))
                    # g.trace(ok,repr(word),i,repr(s))
                    if ok:
                        i1 = g.app.gui.toGuiIndex(s,w,i)
                        i2 = g.app.gui.toGuiIndex(s,w,i+len(word))
                        g.app.gui.setSelectionRange(w,i1,i2)
                        break
                    else:
                        i += 1
            k.resetLabel()
            k.clearState()
    
    #@-node:AGP.20250415230112.953:findWord
    #@-node:AGP.20250415230112.950:find (quick)
    #@+node:AGP.20250415230112.954:goto...
    #@+node:AGP.20250415230112.955:gotoCharacter
    def gotoCharacter (self,event):
        
        '''Put the cursor at the n'th character of the buffer.'''
    
        k = self.k ; state = k.getState('goto-char')
    
        if state == 0:
            w = self.editWidget(event) # Sets self.w
            if not w: return
            k.setLabelBlue('Goto character: ')
            k.getArg(event,'goto-char',1,self.gotoCharacter)
        else:
            n = k.arg ; w = self.w
            if n.isdigit():
                w.mark_set('insert','1.0 +%sc' % n)
                w.see('insert')
            k.resetLabel()
            k.clearState()
    #@-node:AGP.20250415230112.955:gotoCharacter
    #@+node:AGP.20250415230112.956:gotoGlobalLine
    def gotoGlobalLine (self,event):
        
        '''Put the cursor at the n'th line of a file or script.
        This is a minibuffer interface to Leo's legacy Go To Line number command.'''
    
        k = self.k ; tag = 'goto-global-line' ; state = k.getState(tag)
        
        if state == 0:
            w = self.editWidget(event) # Sets self.w
            if not w: return
            k.setLabelBlue('Goto global line: ')
            k.getArg(event,tag,1,self.gotoGlobalLine)
        else:
            n = k.arg
            k.resetLabel()
            k.clearState()
            if n.isdigit():
                self.c.goToLineNumber (n=int(n))
    #@-node:AGP.20250415230112.956:gotoGlobalLine
    #@+node:AGP.20250415230112.957:gotoLine
    def gotoLine (self,event):
        
        '''Put the cursor at the n'th line of the buffer.'''
    
        k = self.k ; state = k.getState('goto-line')
        
        if state == 0:
            w = self.editWidget(event) # Sets self.w
            if not w: return
            k.setLabelBlue('Goto line: ')
            k.getArg(event,'goto-line',1,self.gotoLine)
        else:
            n = k.arg ;  w = self.w
            if n.isdigit():
                w.mark_set('insert','%s.0' % n)
                w.see('insert')
            k.resetLabel()
            k.clearState()
    #@-node:AGP.20250415230112.957:gotoLine
    #@-node:AGP.20250415230112.954:goto...
    #@+node:AGP.20250415230112.958:indent...
    #@+node:AGP.20250415230112.959:backToIndentation
    def backToIndentation (self,event):
        
        '''Position the point at the first non-blank character on the line.'''
        
        w = self.editWidget(event)
        if not w: return
    
        self.beginCommand(undoType='back-to-indentation')
    
        i = w.index('insert linestart')
        i2 = w.search(r'\w',i,stopindex='%s lineend' % i,regexp=True)
        w.mark_set('insert',i2)
    
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.959:backToIndentation
    #@+node:AGP.20250415230112.960:deleteIndentation
    def deleteIndentation (self,event):
        
        '''Delete indentation in the presently line.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
        
        self.beginCommand(undoType='delete-indentation')
    
        txt = w.get('insert linestart','insert lineend')
        txt = ' %s' % txt.lstrip()
        w.delete('insert linestart','insert lineend +1c')
        i = w.index('insert - 1c')
        w.insert('insert -1c',txt)
        w.mark_set('insert',i)
    
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.960:deleteIndentation
    #@+node:AGP.20250415230112.961:indentRelative
    def indentRelative (self,event):
        
        '''The indent-relative command indents at the point based on the previous
        line (actually, the last non-empty line.) It inserts whitespace at the
        point, moving point, until it is underneath an indentation point in the
        previous line.
        
        An indentation point is the end of a sequence of whitespace or the end of
        the line. If the point is farther right than any indentation point in the
        previous line, the whitespace before point is deleted and the first
        indentation point then applicable is used. If no indentation point is
        applicable even then whitespace equivalent to a single tab is inserted.'''
        
        c = self.c ; undoType = 'indent-relative'
        
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        self.beginCommand(undoType=undoType)
        i = w.index('insert')
        oldSel = (i,i)
        line, col = i.split('.')
        c2 = int(col)
        l2 = int(line) -1
        if l2 < 1: return
        txt = w.get('%s.%s' % (l2,c2),'%s.0 lineend' % l2)
        if len(txt) <= len(w.get('insert','insert lineend')):
            w.insert('insert','\t')
        else:
            reg = re.compile('(\s+)')
            ntxt = reg.split(txt)
            replace_word = re.compile('\w')
            for z in ntxt:
                if z.isspace():
                    w.insert('insert',z)
                    break
                else:
                    z = replace_word.subn(' ',z)
                    w.insert('insert',z[0])
                    
        i = w.index('insert')
        result = w.get('1.0','end')
        head = tail = oldYview = None
        c.updateBodyPane(head,result,tail,undoType,oldSel,oldYview)
        w.mark_set('insert',i)
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.961:indentRelative
    #@-node:AGP.20250415230112.958:indent...
    #@+node:AGP.20250415230112.962:insert & delete...
    #@+node:AGP.20250415230112.963:addSpace/TabToLines & removeSpace/TabFromLines & helper
    def addSpaceToLines (self,event):
        '''Add a space to start of all lines, or all selected lines.'''
        self.addRemoveHelper(event,ch=' ',add=True,undoType='add-space-to-lines')
        
    def addTabToLines (self,event):
        '''Add a tab to start of all lines, or all selected lines.'''
        self.addRemoveHelper(event,ch='\t',add=True,undoType='add-tab-to-lines')
        
    def removeSpaceFromLines (self,event):
        '''Remove a space from start of all lines, or all selected lines.'''
        self.addRemoveHelper(event,ch=' ',add=False,undoType='remove-space-from-lines')
        
    def removeTabFromLines (self,event):
        '''Remove a tab from start of all lines, or all selected lines.'''
        self.addRemoveHelper(event,ch='\t',add=False,undoType='remove-tab-from-lines')
    #@+node:AGP.20250415230112.964:addRemoveHelper
    def addRemoveHelper(self,event,ch,add,undoType):
    
        c = self.c ; k = self.k
        w = self.editWidget(event)
        if not w: return
    
        if g.app.gui.hasSelection(w):
            s = g.app.gui.getSelectedText(w)
        else:
            s = g.app.gui.getAllText(w)
        if not s: return
        
        # Insert or delete spaces instead of tabs when negative tab width is in effect.
        d = g.scanDirectives(c) ; width = d.get('tabwidth')
        if ch == '\t' and width < 0: ch = ' ' * abs(width)
        self.beginCommand(undoType=undoType)
        if add:
            result = [ch + line for line in g.splitLines(s)]
        else:
            result = [g.choose(line.startswith(ch),line[len(ch):],line) for line in g.splitLines(s)]
        result = ''.join(result)
        
        # g.trace(g.app.gui.getSelectionRange(w),'len(result)',len(result))
        if g.app.gui.hasSelection(w):
            i,j = g.app.gui.getSelectionRange(w)
            w.delete(i,j)
            w.insert(i,result)
            g.app.gui.setSelectionRange(w, i, j + '+%dc' %(len(result)))
        else:
            w.delete('1.0','end')
            w.insert('1.0',result)
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.964:addRemoveHelper
    #@-node:AGP.20250415230112.963:addSpace/TabToLines & removeSpace/TabFromLines & helper
    #@+node:AGP.20250415230112.965:backwardDeleteCharacter
    def backwardDeleteCharacter (self,event=None):
        
        '''Delete the character to the left of the cursor.'''
        
        c = self.c ; p = c.currentPosition()
        w = self.editWidget(event)
        if not w: return
        
        wname = c.widget_name(w)
        i,j = g.app.gui.getTextSelection(w)
        # g.trace(wname,i,j)
    
        if wname.startswith('body'):
            self.beginCommand()
            d = g.scanDirectives(c,p)
            tab_width = d.get("tabwidth",c.tab_width)
            changed = True
            if i != j:
                w.delete(i,j)
            elif i == '1.0':
                changed = False # Bug fix: 1/6/06 (after a5 released).
            elif tab_width > 0:
                w.delete('insert-1c')
            else:
                #@            << backspace with negative tab_width >>
                #@+node:AGP.20250415230112.966:<< backspace with negative tab_width >>
                s = prev = w.get("insert linestart","insert")
                n = len(prev)
                abs_width = abs(tab_width)
                
                # Delete up to this many spaces.
                n2 = (n % abs_width) or abs_width
                n2 = min(n,n2) ; count = 0
                
                while n2 > 0:
                    n2 -= 1
                    ch = prev[n-count-1]
                    if ch != ' ': break
                    else: count += 1
                
                # Make sure we actually delete something.
                w.delete("insert -%dc" % (max(1,count)),"insert")
                #@-node:AGP.20250415230112.966:<< backspace with negative tab_width >>
                #@nl
            self.endCommand(changed=True,setLabel=False) # Necessary to make text changes stick.
        else:
            # No undo in this widget.
            if i != j:
                w.delete(i,j)
            elif i != '1.0':
                # Bug fix: 1/6/06 (after a5 released).
                # Do nothing at the start of the headline.
                w.delete('insert-1c')
    #@-node:AGP.20250415230112.965:backwardDeleteCharacter
    #@+node:AGP.20250415230112.967:clean-lines
    def cleanLines (self,event):
        
        '''Removes leading whitespace from otherwise blanks lines.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
        
        if g.app.gui.hasSelection(w):
            s = g.app.gui.getSelectedText(w)
        else:
            s = g.app.gui.getAllText(w)
    
        lines = [] ; changed = False
        for line in g.splitlines(s):
            if line.strip():
                lines.append(line)
            else:
                if line.endswith('\n'):
                    lines.append('\n')
                changed = '\n' != line
    
        if changed:
            self.beginCommand(undoType='clean-lines')
            result = ''.join(lines)
            if g.app.gui.hasSelection(w):
                i,j = g.app.gui.getSelectionRange(w)
                w.delete(i,j)
                w.insert(i,result)
                g.app.gui.setSelectionRange(w, i, j + '%dc' %(len(result)))
            else:
                w.delete('1.0','end')
                w.insert('1.0',result)
            self.endCommand(changed=changed,setLabel=True)
    #@-node:AGP.20250415230112.967:clean-lines
    #@+node:AGP.20250415230112.968:clearSelectedText
    def clearSelectedText (self,event):
        
        '''Delete the selected text.'''
        
        c = self.c
        w = self.editWidget(event)
        if not w: return
    
        i,j = g.app.gui.getTextSelection(w)
        if i == j: return
    
        self.beginCommand(undoType='clear-selected-text')
        g.app.gui.replaceSelectionRangeWithText (w,i,j,'')
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.968:clearSelectedText
    #@+node:AGP.20250415230112.969:deleteNextChar
    def deleteNextChar (self,event):
        
        '''Delete the character to the right of the cursor.'''
    
        c = self.c
        w = self.editWidget(event)
        if not w: return
    
        i,j = g.app.gui.getTextSelection(w)
        end = w.index('end-1c')
        
        self.beginCommand(undoType='delete-char')
    
        changed = True
        if i != j:
            w.delete(i,j)
        elif j != end:
            w.delete(i)
        else:
            changed = False
            
        self.endCommand(changed=changed,setLabel=False)
    #@-node:AGP.20250415230112.969:deleteNextChar
    #@+node:AGP.20250415230112.970:deleteSpaces
    def deleteSpaces (self,event,insertspace=False):
        
        '''Delete all whitespace surrounding the cursor.'''
    
        c = self.c
        w = self.editWidget(event)
        if not w: return
    
        char = w.get('insert','insert + 1c ')
        if not char.isspace(): return
        
        undoType = g.choose(insertspace,'insert-space','delete-spaces')
        self.beginCommand(undoType=undoType)
        
        i = w.index('insert')
        wf = w.search(r'\w',i,stopindex='%s lineend' % i,regexp=True)
        wb = w.search(r'\w',i,stopindex='%s linestart' % i,regexp=True,backwards=True)
        if '' not in (wf,wb):
            w.delete('%s +1c' % wb,wf)
            if insertspace: w.insert('insert',' ')
    
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.970:deleteSpaces
    #@+node:AGP.20250415230112.971:insertNewLine
    def insertNewLine (self,event):
        
        '''Insert a newline at the cursor.'''
    
        w = self.editWidget(event)
        if not w: return
    
        wname = g.app.gui.widget_name(w)
        
        if not wname.startswith('head'):
            self.beginCommand(undoType='insert-newline')
            w.insert('insert','\n')
            self.endCommand(changed=True,setLabel=False)
    
    insertNewline = insertNewLine
    #@-node:AGP.20250415230112.971:insertNewLine
    #@+node:AGP.20250415230112.972:insertNewLineAndTab
    def insertNewLineAndTab (self,event):
    
        '''Insert a newline and tab at the cursor.'''
    
        w = self.editWidget(event)
        if not w: return
    
        wname = g.app.gui.widget_name(w)
        
        if not wname.startswith('head'):
            self.beginCommand(undoType='insert-newline-and-indent')
            w.insert('insert','\n\t')
            self.endCommand(changed=True,setLabel=False)
    #@-node:AGP.20250415230112.972:insertNewLineAndTab
    #@+node:AGP.20250415230112.973:insertParentheses
    def insertParentheses (self,event):
        
        '''Insert () at the cursor.'''
    
        w = self.editWidget(event)
        if not w: return
    
        self.beginCommand(undoType='insert-parenthesis')
        w.insert('insert','()')
        w.mark_set('insert','insert -1c')
        self.endCommand(changed=True,setLabel=False)
    #@-node:AGP.20250415230112.973:insertParentheses
    #@+node:AGP.20250415230112.974:removeBlankLines
    def removeBlankLines (self,event):
        
        '''The remove-blank-lines command removes lines containing nothing but
        whitespace. If there is a text selection, only lines within the selected
        text are affected; otherwise all blank lines in the selected node are
        affected.'''
        
        c = self.c ; undoType = 'remove-blank-lines' ; p = c.currentPosition()
        result = []
        body = p.bodyString()
        hasSelection = c.frame.body.hasTextSelection()
        
        if hasSelection:
            head,lines,tail,oldSel,oldYview = c.getBodyLines()
            joinChar = '\n'
        else:
            head = tail = oldYview = None
            lines = g.splitLines(body)
            oldSel = ('1.0','1.0')
            joinChar = ''
    
        for line in lines:
            if line.strip():
                result.append(line)
    
        result = joinChar.join(result)
        
        if result != body:
            c.updateBodyPane(head,result,tail,undoType,oldSel,oldYview)
    #@-node:AGP.20250415230112.974:removeBlankLines
    #@+node:AGP.20250415230112.975:selfInsertCommand & helpers
    def selfInsertCommand(self,event,action='insert'):
        
        '''Insert a character in the body pane.
        This is the default binding for all keys in the body pane.'''
        
        c = self.c ; p = c.currentPosition()
        ch = event and event.char or ''
        if event and event.keysym == 'Return': ch = '\n' # This fixes the MacOS return bug.
        w = self.editWidget(event)
        if not w: return 'break'
    
        name = c.widget_name(w)
        oldSel =  name.startswith('body') and g.app.gui.getTextSelection(w) or (None,None)
        oldText = name.startswith('body') and p.bodyString() or ''
        undoType = 'Typing'
        trace = c.config.getBool('trace_masterCommand')
        brackets = self.openBracketsList + self.closeBracketsList
        inBrackets = g.toUnicode(ch,g.app.tkEncoding) in brackets
        
        if trace: g.trace(name,repr(ch),ch in brackets)
        
        if g.doHook("bodykey1",c=c,p=p,v=p,ch=ch,oldSel=oldSel,undoType=undoType):
            return "break" # The hook claims to have handled the event.
            
        if ch == '\t':
            self.updateTab(p,w)
        elif ch == '\b':
            # This is correct: we only come here if there no bindngs for this key. 
            self.backwardDeleteCharacter(event)
        elif ch in ('\r','\n'):
            ch = '\n'
            #@        << handle newline >>
            #@+node:AGP.20250415230112.976:<< handle newline >>
            i,j = oldSel
            
            if i != j:
                # No auto-indent if there is selected text.
                w.delete(i,j)
                w.insert(i,ch)
            else:
                w.insert(i,ch)
                allow_in_nocolor = c.config.getBool('autoindent_in_nocolor_mode')
                if (
                    (allow_in_nocolor or c.frame.body.colorizer.useSyntaxColoring(p)) and
                    undoType != "Change"
                ):
                    # No auto-indent if in @nocolor mode or after a Change command.
                    self.updateAutoIndent(p,w)
            #@-node:AGP.20250415230112.976:<< handle newline >>
            #@nl
        elif inBrackets and self.autocompleteBrackets:
            self.updateAutomatchBracket(p,w,ch,oldSel)
        elif ch: # Null chars must not delete the selection.
            i,j = oldSel
            if i != j:                  w.delete(i,j)
            elif action == 'overwrite': w.delete(i,'%s+1c' % i)
            w.insert(i,ch)
            if inBrackets and self.flashMatchingBrackets: # New in 4.4.1.
               self.flashMatchingBracketsHelper(w,i,ch)               
        else:
            return 'break' # New in 4.4a5: this method *always* returns 'break'
            
        # New in 4.4.1: Set the column for up and down keys.
        spot = w.index('insert')
        c.editCommands.setMoveCol(spot)
    
        # Update the text and handle undo.
        newText = g.app.gui.getAllText(w) # New in 4.4b3: converts to unicode.
        # g.trace(repr(newText))
        w.see(w.index('insert'))
        if newText != oldText:
            c.frame.body.onBodyChanged(undoType=undoType,
                oldSel=oldSel,oldText=oldText,oldYview=None)
                
        g.doHook("bodykey2",c=c,p=p,v=p,ch=ch,oldSel=oldSel,undoType=undoType)
        return 'break'
    #@nonl
    #@+node:AGP.20250415230112.977:test_selfInsertCommand
    def test_selfInsertCommand(self):
        
        self = c.editCommands
        event = g.Bunch(char='É',keysym=None,widget=c.frame.body.bodyCtrl)
        self.selfInsertCommand(event)
    #@nonl
    #@-node:AGP.20250415230112.977:test_selfInsertCommand
    #@+node:AGP.20250415230112.978:initBracketMatcher
    def initBracketMatcher (self,c):
    
        self.openBracketsList  = c.config.getString('open_flash_brackets')  or '([{'
        self.closeBracketsList = c.config.getString('close_flash_brackets') or ')]}'
        
        if len(self.openBracketsList) != len(self.closeBracketsList):
            g.es_print('bad open/close_flash_brackets setting: using defaults')
            self.openBracketsList  = '([{'
            self.closeBracketsList = ')]}'
    
        # g.trace('self.openBrackets',openBrackets)
        # g.trace('self.closeBrackets',closeBrackets)
    #@-node:AGP.20250415230112.978:initBracketMatcher
    #@+node:AGP.20250415230112.979:flashMatchingBracketsHelper
    def flashMatchingBracketsHelper (self,w,index,ch):
    
        s = g.app.gui.getAllText(w)
        i = g.app.gui.toPythonIndex(s,w,index)
        
        d = {}
        if ch in self.openBracketsList:
            for z in xrange(len(self.openBracketsList)):
                d [self.openBracketsList[z]] = self.closeBracketsList[z]
            reverse = False # Search forward
        else:
            for z in xrange(len(self.openBracketsList)):
                d [self.closeBracketsList[z]] = self.openBracketsList[z]
            reverse = True # Search backward
    
        delim2 = d.get(ch)
        j = g.skip_matching_python_delims(s,i,ch,delim2,reverse=reverse)
        if j != -1:
            j = g.app.gui.toGuiIndex(s,w,j)
            self.flashCharacter(w,j)
    #@-node:AGP.20250415230112.979:flashMatchingBracketsHelper
    #@+node:AGP.20250415230112.980:flashCharacter
    def flashCharacter(self,w,i):
        
        bg      = self.bracketsFlashBg or 'DodgerBlue1'
        fg      = self.bracketsFlashFg or 'white'
        flashes = self.bracketsFlashCount or 2
        delay   = self.bracketsFlashDelay or 75
    
        def addFlashCallback(w,count,index):
            w.tag_add('flash',index,'%s+1c' % (index))
            w.after(delay,removeFlashCallback,w,count-1,index)
        
        def removeFlashCallback(w,count,index):
            w.tag_remove('flash','1.0','end')
            if count > 0:
                w.after(delay,addFlashCallback,w,count,index)
    
        try:
            w.tag_configure('flash',foreground=fg,background=bg)
            addFlashCallback(w,flashes,i)
        except Exception:
            pass
    #@-node:AGP.20250415230112.980:flashCharacter
    #@+node:AGP.20250415230112.981:updateAutomatchBracket
    def updateAutomatchBracket (self,p,w,ch,oldSel):
    
        # assert ch in ('(',')','[',']','{','}')
        
        c = self.c ; d = g.scanDirectives(c,p) ; i,j = oldSel
        language = d.get('language')
        
        if ch in ('(','[','{',):
            automatch = language not in ('plain',)
            if automatch:
                ch = ch + {'(':')','[':']','{':'}'}.get(ch)
            if i != j:
                w.delete(i,j)
            w.insert(i,ch)
            if automatch:
                w.mark_set('insert','insert-1c')
        else:
            ch2 = w.get('insert')
            if ch2 in (')',']','}'):
                w.mark_set('insert','insert+1c')
            else:
                if i != j:
                    w.delete(i,j)
                w.insert(i,ch)
    #@-node:AGP.20250415230112.981:updateAutomatchBracket
    #@+node:AGP.20250415230112.982:udpateAutoIndent
    # By David McNab:
    def updateAutoIndent (self,p,w):
    
        c = self.c ; d = g.scanDirectives(c,p)
        tab_width = d.get("tabwidth",c.tab_width) # Get the previous line.
        s = w.get("insert linestart - 1 lines","insert linestart -1c")
        # Add the leading whitespace to the present line.
        junk, width = g.skip_leading_ws_with_indent(s,0,tab_width)
        if s and len(s) > 0 and s [ -1] == ':':
            # For Python: increase auto-indent after colons.
            if c.frame.body.colorizer.scanColorDirectives(p) == "python":
                width += abs(tab_width)
        if self.smartAutoIndent:
            # Determine if prev line has unclosed parens/brackets/braces
            bracketWidths = [width] ; tabex = 0
            for i in range(0,len(s)):
                if s [i] == '\t':
                    tabex += tab_width-1
                if s [i] in '([{':
                    bracketWidths.append(i+tabex+1)
                elif s [i] in '}])' and len(bracketWidths) > 1:
                    bracketWidths.pop()
            width = bracketWidths.pop()
        ws = g.computeLeadingWhitespace(width,tab_width)
        if ws:
            w.insert("insert",ws)
    #@-node:AGP.20250415230112.982:udpateAutoIndent
    #@+node:AGP.20250415230112.983:updateTab
    def updateTab (self,p,w):
    
        c = self.c ; d = g.scanDirectives(c,p)
        tab_width = d.get("tabwidth",c.tab_width)
        
        i,j = g.app.gui.getTextSelection(w)
        if i != j:
            w.delete(i,j)
        if tab_width > 0:
            w.insert("insert",'\t')
        else:
            # Get the preceeding characters.
            s = w.get("insert linestart","insert")
        
            # Compute n, the number of spaces to insert.
            width = g.computeWidth(s,tab_width)
            n = abs(tab_width) - (width % abs(tab_width))
            w.insert("insert",' ' * n)
    #@-node:AGP.20250415230112.983:updateTab
    #@-node:AGP.20250415230112.975:selfInsertCommand & helpers
    #@-node:AGP.20250415230112.962:insert & delete...
    #@+node:AGP.20250415230112.984:info...
    #@+node:AGP.20250415230112.985:howMany
    def howMany (self,event):
        
        '''Print how many occurances of a regular expression are found
        in the body text of the presently selected node.'''
        
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        state = k.getState('how-many')
        if state == 0:
            k.setLabelBlue('How many: ',protect = True)
            k.getArg(event,'how-many',1,self.howMany)
        else:
            k.clearState()
            s = w.get('1.0','end')
            reg = re.compile(k.arg)
            i = reg.findall(s)
            k.setLabelGrey('%s occurances of %s' % (len(i),k.arg))
    #@-node:AGP.20250415230112.985:howMany
    #@+node:AGP.20250415230112.986:lineNumber
    def lineNumber (self,event):
        
        '''Print the line and column number and percentage of insert point.'''
    
        k = self.k
        w = self.editWidget(event)
    
        i = w.index('insert')
        i1, i2 = i.split('.')
        c = w.get('insert','insert + 1c')
        txt = w.get('1.0','end')
        txt2 = w.get('1.0','insert')
        perc = len(txt) * .01
        perc = int(len(txt2)/perc)
    
        k.setLabelGrey('Char: %s point %s of %s(%s%s)  Column %s' % (c,len(txt2),len(txt),perc,'%',i1))
    #@-node:AGP.20250415230112.986:lineNumber
    #@+node:AGP.20250415230112.987:viewLossage
    def viewLossage (self,event):
        
        '''Put the Emacs-lossage in the minibuffer label.'''
    
        k = self.k
        
        g.es('Lossage...')
        aList = leoKeys.keyHandlerClass.lossage
        aList.reverse()
        for data in aList:
            ch,stroke = data
            d = {' ':'Space','\t':'Tab','\b':'Backspace','\n':'Newline','\r':'Return'}
            g.es(stroke or d.get(ch) or ch or 'None')
    #@-node:AGP.20250415230112.987:viewLossage
    #@+node:AGP.20250415230112.988:whatLine
    def whatLine (self,event):
        
        '''Print the line number of the line containing the cursor.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        i = w.index('insert')
        i1, i2 = i.split('.')
        k.keyboardQuit(event)
    
        k.setLabel("Line %s" % i1)
    #@-node:AGP.20250415230112.988:whatLine
    #@-node:AGP.20250415230112.984:info...
    #@+node:AGP.20250415230112.989:line...
    #@+node:AGP.20250415230112.990:flushLines
    def flushLines (self,event):
    
        '''Delete each line that contains a match for regexp, operating on the text after point.
    
        In Transient Mark mode, if the region is active, the command operates on the region instead.'''
    
        k = self.k ; state = k.getState('flush-lines')
        
        if state == 0:
            k.setLabelBlue('Flush lines regexp: ',protect=True)
            k.getArg(event,'flush-lines',1,self.flushLines)
        else:
            k.clearState()
            k.resetLabel()
            self.linesHelper(event,k.arg,'flush')
            k.commandName = 'flush-lines %s' % k.arg
    #@-node:AGP.20250415230112.990:flushLines
    #@+node:AGP.20250415230112.991:keepLines
    def keepLines (self,event):
    
        '''Delete each line that does not contain a match for regexp, operating on the text after point.
    
        In Transient Mark mode, if the region is active, the command operates on the region instead.'''
    
        k = self.k ; state = k.getState('keep-lines')
        
        if state == 0:
            k.setLabelBlue('Keep lines regexp: ',protect=True)
            k.getArg(event,'keep-lines',1,self.keepLines)
        else:
            k.clearState()
            k.resetLabel()
            self.linesHelper(event,k.arg,'keep')
            k.commandName = 'keep-lines %s' % k.arg
    #@-node:AGP.20250415230112.991:keepLines
    #@+node:AGP.20250415230112.992:linesHelper
    def linesHelper (self,event,pattern,which):
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
       
        self.beginCommand(undoType=which+'-lines')
        if w.tag_ranges('sel'):
            i = w.index('sel.first') ; end = w.index('sel.last')
        else:
             i = w.index('insert') ; end = 'end'
        txt = w.get(i,end)
        tlines = txt.splitlines(True)
        if which == 'flush':    keeplines = list(tlines)
        else:                   keeplines = []
    
        try:
            regex = re.compile(pattern)
            for n, z in enumerate(tlines):
                f = regex.findall(z)
                if which == 'flush' and f:
                    keeplines [n] = None
                elif f:
                    keeplines.append(z)
        except Exception, x:
            return
        if which == 'flush':
            keeplines = [x for x in keeplines if x != None]
        w.delete(i,end)
        w.insert(i,''.join(keeplines))
        w.mark_set('insert',i)
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.992:linesHelper
    #@+node:AGP.20250415230112.993:splitLine
    def splitLine (self,event):
        
        '''Split a line at the cursor position.'''
    
        w = self.editWidget(event)
        if not w: return
    
        s = w.get('insert linestart','insert lineend')
        
        self.beginCommand(undoType='split-line')
        s = self.getWSString(s)
        i = w.index('insert')
        w.insert(i,s + '\n')
        # w.mark_set('insert',i)
        # w.insert('insert','\n')
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.993:splitLine
    #@-node:AGP.20250415230112.989:line...
    #@+node:AGP.20250415230112.994:move cursor... (leoEditCommands)
    #@+node:AGP.20250415230112.995: helpers
    #@+node:AGP.20250415230112.996:extendHelper
    def extendHelper (self,w,extend,ins1,spot,setSpot=True):
    
        '''Handle the details of extending the selection.
        This method is called for all cursor moves.
        
        extend: Clear the selection unless this is True.
        ins1:   The *previous* insert point.
        spot:   The *new* insert point.
        '''
        c = self.c ; p = c.currentPosition()
        moveSpot = self.moveSpot
        extend = extend or self.extendMode
        if extend:
            i, j = g.app.gui.getTextSelection(w)
            # Reset the move spot if needed.
            if (
                not moveSpot or p.v.t != self.moveSpotNode or
                (
                    i == j or # A cute trick
                    (not w.compare(moveSpot,'==',i) and
                    not w.compare(moveSpot,'==',j))
                )
            ):
                self.moveSpotNode = p.v.t
                self.moveSpot = w.index(ins1)
                self.setMoveCol(ins1)
            moveSpot = self.moveSpot
            if w.compare(spot,'<',moveSpot):
                g.app.gui.setTextSelection(w,spot,moveSpot,insert=None)
            else:
                g.app.gui.setTextSelection(w,moveSpot,spot,insert=None)
        else:
            if setSpot or not moveSpot:
                self.setMoveCol(spot)
            g.app.gui.setTextSelection(w,spot,spot,insert=None)
            
        c.frame.updateStatusLine()
    #@nonl
    #@-node:AGP.20250415230112.996:extendHelper
    #@+node:AGP.20250415230112.997:moveUpOrDownHelper
    def moveUpOrDownHelper (self,event,direction,extend):
    
        c = self.c
        w = self.editWidget(event)
        if not w: return
    
        # Make the insertion cursor visible so bbox won't return an empty list.
        w.see('insert')
        # Remember the original insert point.  This may become the moveSpot.
        ins1 = w.index('insert')
        # Compute the new spot.
        row1,col1 = ins1.split('.')
        row1 = int(row1) ; col1 = int(col1)
        # Find the coordinates of the cursor and set the new height.
        # There may be roundoff errors because character postions may not match exactly.
        x, y, junk, textH = w.bbox('insert')
        bodyW, bodyH = w.winfo_width(), w.winfo_height()
        junk, maxy, junk, junk = w.bbox("@%d,%d" % (bodyW,bodyH))
        # Make sure y is within text boundaries.
        if direction == "up":
            if y <= textH:  w.yview("scroll",-1,"units")
            else:           y = max(y-textH,0)
        else:
            if y >= maxy:   w.yview("scroll",1,"units")
            else:           y = min(y+textH,maxy)
        # Position the cursor on the proper side of the characters.
        newx, newy, width, junk = w.bbox("@%d,%d" % (x,y))
        if x > newx + width / 2: x = newx + width + 1
        # Move to the new row.
        spot = w.index("@%d,%d" % (x,y))
        row,col = spot.split('.')
        row = int(row) ; col = int(col)
        w.mark_set('insert',spot)
        # Adjust the column in the *new* row, but only if we have actually gone to a new row.
        if self.moveSpot:
            if col != self.moveCol and row != row1:
                s = w.get('insert linestart','insert lineend')
                col = min(len(s),self.moveCol)
                if col >= 0:
                    w.mark_set('insert','%d.%d' % (row,col))
                    spot = w.index('insert')
                    w.see('insert')
        # Handle the extension.
        self.extendHelper(w,extend,ins1,spot,setSpot=False)
    #@-node:AGP.20250415230112.997:moveUpOrDownHelper
    #@+node:AGP.20250415230112.998:moveToHelper
    def moveToHelper (self,event,spot,extend):
    
        '''Common helper method for commands the move the cursor
        in a way that can be described by a Tk Text expression.'''
    
        c = self.c ; k = c.k
        w = self.editWidget(event)
        if not w: return
    
        c.widgetWantsFocusNow(w)
        wname = c.widget_name(w)
        if wname.startswith('mini'):
            # Put the request in the proper range.
            i, j = k.getEditableTextRange()
            ins1 = w.index('insert')
            spot = w.index(spot)
            if w.compare(spot,'<',i):
                spot = i
            elif w.compare(spot,'>',j):
                spot = j
            w.mark_set('insert',spot)
            self.extendHelper(w,extend,ins1,spot,setSpot=False)
            w.see(spot)
        else:
            # Remember the original insert point.  This may become the moveSpot.
            ins1 = w.index('insert')
    
            # Move to the spot.
            w.mark_set('insert',spot)
            spot = w.index('insert')
    
            # Handle the selection.
            self.extendHelper(w,extend,ins1,spot,setSpot=True)
            w.see(spot)
    #@-node:AGP.20250415230112.998:moveToHelper
    #@+node:AGP.20250415230112.999:movePastCloseHelper
    def movePastCloseHelper (self,event,extend):
    
        c = self.c
        w = self.editWidget(event)
        if not w: return
    
        c.widgetWantsFocusNow(w)
        i = w.search('(','insert',backwards=True,stopindex='1.0')
        if '' == i: return
    
        icheck = w.search(')','insert',backwards=True,stopindex='1.0')
        if icheck:
            ic = w.compare(i,'<',icheck)
            if ic: return
    
        i2 = w.search(')','insert',stopindex='end')
        if '' == i2: return
    
        i2check = w.search('(','insert',stopindex='end')
        if i2check:
            ic2 = w.compare(i2,'>',i2check)
            if ic2: return
        
        ins = '%s+1c' % i2
        self.moveToHelper(event,ins,extend)
    #@-node:AGP.20250415230112.999:movePastCloseHelper
    #@+node:AGP.20250415230112.1000:moveWordHelper
    def moveWordHelper (self,event,extend,forward,end=False):
    
        '''Move the cursor to the next word.
        The cursor is placed at the start of the word unless end=True'''
    
        c = self.c
        w = self.editWidget(event)
        if not w: return
        
        c.widgetWantsFocusNow(w)
        s = w.get('1.0','end') ; n = len(s)
    
        def toGui (i): return g.app.gui.toGuiIndex(s,w,i)
        def toPython (i): return g.app.gui.toPythonIndex(s,w,i)
    
        i = toPython(w.index('insert'))
        
        if forward:
            # Unlike backward-word moves, there are two options...
            if end:
                while 0 <= i < n and not g.isWordChar(s[i]):
                    i += 1
                while 0 <= i < n and g.isWordChar(s[i]):
                    i += 1
            else:
                while 0 <= i < n and g.isWordChar(s[i]):
                    i += 1
                while 0 <= i < n and not g.isWordChar(s[i]):
                    i += 1
        else:
            i -= 1
            while 0 <= i < n and not g.isWordChar(s[i]):
                i -= 1
            while 0 <= i < n and g.isWordChar(s[i]):
                i -= 1
            i += 1
        
        self.moveToHelper(event,toGui(i),extend)
    #@nonl
    #@-node:AGP.20250415230112.1000:moveWordHelper
    #@+node:AGP.20250415230112.1001:backSentenceHelper
    def backSentenceHelper (self,event,extend):
    
        c = self.c
        w = self.editWidget(event)
        if not w: return
    
        c.widgetWantsFocusNow(w)
        i = w.search('.','insert',backwards=True,stopindex='1.0')
        if i:
            i2 = w.search('.',i,backwards=True,stopindex='1.0')
            if i2:
                ins = w.search('\w',i2,stopindex=i,regexp=True) or i2
            else:
                ins = '1.0'
        else:
            ins = '1.0'
        if ins:
            self.moveToHelper(event,ins,extend)
    #@-node:AGP.20250415230112.1001:backSentenceHelper
    #@+node:AGP.20250415230112.1002:forwardSentenceHelper
    def forwardSentenceHelper (self,event,extend):
    
        c = self.c
        w = self.editWidget(event)
        if not w: return
    
        c.widgetWantsFocusNow(w)
        ins = w.index('insert')
        # sel_i,sel_j = g.app.gui.getTextSelection(w)
        i = w.search('.','insert',stopindex='end')
        ins = i and '%s +1c' % i or 'end'
        self.moveToHelper(event,ins,extend)
    #@-node:AGP.20250415230112.1002:forwardSentenceHelper
    #@+node:AGP.20250415230112.1003:forwardParagraphHelper
    def forwardParagraphHelper (self,event,extend):
        
        c = self.c
        w = self.editWidget(event)
        if not w: return
    
        c.widgetWantsFocusNow(w)
        i = w.index('insert')
        while 1:
            txt = w.get('%s linestart' % i,'%s lineend' % i).strip()
            if txt:
                i = w.index('%s + 1 lines' % i)
                if w.index('%s linestart' % i) == w.index('end'):
                    i = w.search(r'\w','end',backwards=True,regexp=True,stopindex='1.0')
                    i = '%s + 1c' % i
                    break
            else:
                i = w.search(r'\w',i,regexp=True,stopindex='end')
                i = '%s' % i
                break
        if i:
            self.moveToHelper(event,i,extend)
    #@-node:AGP.20250415230112.1003:forwardParagraphHelper
    #@+node:AGP.20250415230112.1004:backwardParagraphHelper
    def backwardParagraphHelper (self,event,extend):
        
        c = self.c
        w = self.editWidget(event)
        if not w: return
    
        c.widgetWantsFocusNow(w)
        i = w.index('insert')
        while 1:
            s = w.get('%s linestart' % i,'%s lineend' % i).strip()
            if s:
                i = w.index('%s - 1 lines' % i)
                if w.index('%s linestart' % i) == '1.0':
                    i = w.search(r'\w','1.0',regexp=True,stopindex='end')
                    break
            else:
                i = w.search(r'\w',i,backwards=True,regexp=True,stopindex='1.0')
                i = '%s +1c' % i
                break
        if i:
            self.moveToHelper(event,i,extend)
    #@-node:AGP.20250415230112.1004:backwardParagraphHelper
    #@+node:AGP.20250415230112.1005:setMoveCol
    def setMoveCol (self,spot):
        
        self.moveSpot = spot
        self.moveCol = int(spot.split('.')[1])
    
        if 0:
            g.trace(
                # 'spot',self.moveSpot,
                'col',self.moveCol)
    #@-node:AGP.20250415230112.1005:setMoveCol
    #@-node:AGP.20250415230112.995: helpers
    #@+node:AGP.20250415230112.1006:buffers
    def beginningOfBuffer (self,event):
        '''Move the cursor to the start of the body text.'''
        self.moveToHelper(event,'1.0',extend=False)
        
    def beginningOfBufferExtendSelection (self,event):
        '''Extend the text selection by moving the cursor to the start of the body text.'''
        self.moveToHelper(event,'1.0',extend=True)
    
    def endOfBuffer (self,event):
        '''Move the cursor to the end of the body text.'''
        self.moveToHelper(event,'end',extend=False)
        
    def endOfBufferExtendSelection (self,event):
        '''Extend the text selection by moving the cursor to the end of the body text.'''
        self.moveToHelper(event,'end',extend=True)
    #@-node:AGP.20250415230112.1006:buffers
    #@+node:AGP.20250415230112.1007:characters
    def backCharacter (self,event):
        '''Move the cursor back one character, extending the selection if in extend mode.'''
        self.moveToHelper(event,'insert-1c',extend=False)
        
    def backCharacterExtendSelection (self,event):
        '''Extend the selection by moving the cursor back one character.'''
        self.moveToHelper(event,'insert-1c',extend=True)
        
    def forwardCharacter (self,event):
        '''Move the cursor forward one character, extending the selection if in extend mode.'''
        self.moveToHelper (event,'insert+1c',extend=False)
        
    def forwardCharacterExtendSelection (self,event):
        '''Extend the selection by moving the cursor forward one character.'''
        self.moveToHelper (event,'insert+1c',extend=True)
    #@-node:AGP.20250415230112.1007:characters
    #@+node:AGP.20250415230112.1008:clear/set/ToggleExtendMode
    def clearExtendMode (self,event):
        '''Turn off extend mode: cursor movement commands do not extend the selection.'''
        self.extendModeHelper(event,False)
    
    def setExtendMode (self,event):
        '''Turn on extend mode: cursor movement commands do extend the selection.'''
        self.extendModeHelper(event,True)
    
    def toggleExtendMode (self,event):
        '''Toggle extend mode, i.e., toggle whether cursor movement commands extend the selections.'''
        self.extendModeHelper(event,not self.extendMode)
    
    def extendModeHelper (self,event,val):
    
        c = self.c
        w = self.editWidget(event)
        if not w: return
    
        self.extendMode = val
        g.es('Extend mode %s' % (g.choose(val,'on','off')), color='red')
        c.widgetWantsFocusNow(w)
    #@-node:AGP.20250415230112.1008:clear/set/ToggleExtendMode
    #@+node:AGP.20250415230112.1009:exchangePointMark
    def exchangePointMark (self,event):
        
        '''Exchange the point (insert point) with the mark (the other end of the selected text).'''
        
        c = self.c
        w = self.editWidget(event)
        if not w: return
    
        c.widgetWantsFocusNow(w)
        i,j = g.app.gui.getTextSelection(w,sort=False)
        if i != j:
            ins = w.index('insert')
            ins = g.choose(ins==i,j,i)
            g.app.gui.setInsertPoint(w,ins)
            g.app.gui.setTextSelection(w,i,j,insert=None)
    #@-node:AGP.20250415230112.1009:exchangePointMark
    #@+node:AGP.20250415230112.1010:extend-to-line
    def extendToLine (self,event):
        
        '''Select the line at the cursor.'''
        
        c = self.c
        w = self.editWidget(event)
        if not w: return
        
        def toGui(i): return g.app.gui.toGuiIndex(s,w,i)
        def toPython(i): return g.app.gui.toPythonIndex(s,w,i)
        
        s = w.get('1.0','end') ; n = len(s)
        i = toPython(w.index('insert'))
        while 0 <= i < n and not s[i] == '\n':
            i -= 1
        i += 1 ; i1 = i
        while 0 <= i < n and not s[i] == '\n':
            i += 1
    
        g.app.gui.setSelectionRange(w,toGui(i1),toGui(i))
    #@-node:AGP.20250415230112.1010:extend-to-line
    #@+node:AGP.20250415230112.1011:extend-to-sentence
    def extendToSentence (self,event):
        
        '''Select the line at the cursor.'''
        
        c = self.c
        w = self.editWidget(event)
        if not w: return
        
        def toGui(i): return g.app.gui.toGuiIndex(s,w,i)
        def toPython(i): return g.app.gui.toPythonIndex(s,w,i)
        
        s = w.get('1.0','end') ; n = len(s)
        i = toPython(w.index('insert'))
        i2 = 1 + s.find('.',i)
        if i2 == -1: i2 = n
        i1 = 1 + s.rfind('.',0,i2-1)
    
        g.app.gui.setSelectionRange(w,toGui(i1),toGui(i2))
    #@nonl
    #@-node:AGP.20250415230112.1011:extend-to-sentence
    #@+node:AGP.20250415230112.1012:extend-to-word
    def extendToWord (self,event):
        
        '''Select the word at the cursor.'''
        
        c = self.c
        w = self.editWidget(event)
        if not w: return
    
        def toGui (i): return g.app.gui.toGuiIndex(s,w,i)
        def toPython (i): return g.app.gui.toPythonIndex(s,w,i)
    
        s = w.get('1.0','end') ; n = len(s)
        i = toPython(w.index('insert'))
        while 0 <= i < n and not g.isWordChar(s[i]):
            i -= 1
        while 0 <= i < n and g.isWordChar(s[i]):
            i -= 1
        i += 1
        # Move to the end of the word.
        i1 = i
        while 0 <= i < n and g.isWordChar(s[i]):
            i += 1
        g.app.gui.setSelectionRange(w,toGui(i1),toGui(i))
    #@nonl
    #@-node:AGP.20250415230112.1012:extend-to-word
    #@+node:AGP.20250415230112.1013:lines
    def beginningOfLine (self,event):
        '''Move the cursor to the start of the line, extending the selection if in extend mode.'''
        self.moveToHelper(event,'insert linestart',extend=False)
        
    def beginningOfLineExtendSelection (self,event):
        '''Extend the selection by moving the cursor to the start of the line.'''
        self.moveToHelper(event,'insert linestart',extend=True)
        
    def endOfLine (self,event):
        '''Move the cursor to the end of the line, extending the selection if in extend mode.'''
        self.moveToHelper(event,'insert lineend',extend=False)
        
    def endOfLineExtendSelection (self,event):
        '''Extend the selection by moving the cursor to the end of the line.'''
        self.moveToHelper(event,'insert lineend',extend=True)
    
    def nextLine (self,event):
        '''Move the cursor down, extending the selection if in extend mode.'''
        self.moveUpOrDownHelper(event,'down',extend=False)
        
    def nextLineExtendSelection (self,event):
        '''Extend the selection by moving the cursor down.'''
        self.moveUpOrDownHelper(event,'down',extend=True)
        
    def prevLine (self,event):
        '''Move the cursor up, extending the selection if in extend mode.'''
        self.moveUpOrDownHelper(event,'up',extend=False)
        
    def prevLineExtendSelection (self,event):
        '''Extend the selection by moving the cursor up.'''
        self.moveUpOrDownHelper(event,'up',extend=True)
    #@-node:AGP.20250415230112.1013:lines
    #@+node:AGP.20250415230112.1014:movePastClose (test)
    def movePastClose (self,event):
        '''Move the cursor past the closing parenthesis.'''
        self.movePastCloseHelper(event,extend=False)
        
    def movePastCloseExtendSelection (self,event):
        '''Extend the selection by moving the cursor past the closing parenthesis.'''
        self.movePastCloseHelper(event,extend=True)
    #@-node:AGP.20250415230112.1014:movePastClose (test)
    #@+node:AGP.20250415230112.1015:paragraphs
    def backwardParagraph (self,event):
        '''Move the cursor to the previous paragraph.'''
        self.backwardParagraphHelper (event,extend=False)
        
    def backwardParagraphExtendSelection (self,event):
        '''Extend the selection by moving the cursor to the previous paragraph.'''
        self.backwardParagraphHelper (event,extend=True)
        
    def forwardParagraph (self,event):
        '''Move the cursor to the next paragraph.'''
        self.forwardParagraphHelper(event,extend=False)
        
    def forwardParagraphExtendSelection (self,event):
        '''Extend the selection by moving the cursor to the next paragraph.'''
        self.forwardParagraphHelper(event,extend=True)
    #@-node:AGP.20250415230112.1015:paragraphs
    #@+node:AGP.20250415230112.1016:sentences
    def backSentence (self,event):
        '''Move the cursor to the previous sentence.'''
        self.backSentenceHelper(event,extend=False)
        
    def backSentenceExtendSelection (self,event):
        '''Extend the selection by moving the cursor to the previous sentence.'''
        self.backSentenceHelper(event,extend=True)
        
    def forwardSentence (self,event):
        '''Move the cursor to the next sentence.'''
        self.forwardSentenceHelper(event,extend=False)
        
    def forwardSentenceExtendSelection (self,event):
        '''Extend the selection by moving the cursor to the next sentence.'''
        self.forwardSentenceHelper(event,extend=True)
    #@-node:AGP.20250415230112.1016:sentences
    #@+node:AGP.20250415230112.1017:words
    def backwardWord (self,event):
        '''Move the cursor to the previous word.'''
        self.moveWordHelper(event,extend=False,forward=False)
        
    def backwardWordExtendSelection (self,event):
        '''Extend the selection by moving the cursor to the next word.'''
        self.moveWordHelper(event,extend=True,forward=False)
        
    def forwardEndWord (self,event): # New in Leo 4.4.2
        '''Move the cursor to the next word.'''
        self.moveWordHelper(event,extend=False,forward=True,end=True)
            
    def forwardEndWordExtendSelection (self,event): # New in Leo 4.4.2
        '''Extend the selection by moving the cursor to the previous word.'''
        self.moveWordHelper(event,extend=True,forward=True,end=True)
    
    def forwardWord (self,event):
        '''Move the cursor to the next word.'''
        self.moveWordHelper(event,extend=False,forward=True)
        
    def forwardWordExtendSelection (self,event):
        '''Extend the selection by moving the cursor to the previous word.'''
        self.moveWordHelper(event,extend=True,forward=True)
    #@-node:AGP.20250415230112.1017:words
    #@-node:AGP.20250415230112.994:move cursor... (leoEditCommands)
    #@+node:AGP.20250415230112.1018:paragraph...
    #@+others
    #@+node:AGP.20250415230112.1019:backwardKillParagraph
    def backwardKillParagraph (self,event):
        
        '''Kill the previous paragraph.'''
    
        k = self.k ; c = k.c
        w = self.editWidget(event)
        if not w: return
    
        i = w.index('insert')
        i2 = i
        txt = w.get('insert linestart','insert lineend')
        undoType='backward-kill-paragraph'
        self.beginCommand(undoType=undoType)
    
        if not txt.rstrip().lstrip():
            self.backwardParagraph(event)
            i2 = w.index('insert')
        self.extendToParagraph(event)
        i3 = w.index('sel.first')
        c.killBufferCommands.kill(event,i3,i2,undoType=undoType)
        w.mark_set('insert',i)
        w.selection_clear()
    
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1019:backwardKillParagraph
    #@+node:AGP.20250415230112.1020:fillParagraph
    def fillParagraph( self, event ):
        
        '''Fill the selected paragraph'''
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        txt = w.get( 'insert linestart', 'insert lineend' )
        txt = txt.strip()
        if txt:
            self.beginCommand(undoType='fill-paragraph')
            i = w.index( 'insert' )
            i2 = i
            txt2 = txt
            while txt2:
                pi2 = w.index( '%s - 1 lines' % i2)
                txt2 = w.get( '%s linestart' % pi2, '%s lineend' % pi2 )
                if w.index( '%s linestart' % pi2 ) == '1.0':
                    i2 = w.search( '\w', '1.0', regexp = True, stopindex = 'end' )
                    break
                if txt2.strip() == '': break
                i2 = pi2
            i3 = i
            txt3 = txt
            while txt3:
                pi3 = w.index( '%s + 1 lines' %i3 )
                txt3 = w.get( '%s linestart' % pi3, '%s lineend' % pi3 )
                if w.index( '%s lineend' % pi3 ) == w.index( 'end' ):
                    i3 = w.search( '\w', 'end', backwards = True, regexp = True, stopindex = '1.0' )
                    break
                if txt3.strip() == '': break
                i3 = pi3
            ntxt = w.get( '%s linestart' %i2, '%s lineend' %i3 )
            ntxt = self._addPrefix( ntxt )
            w.delete( '%s linestart' %i2, '%s lineend' % i3 )
            w.insert( i2, ntxt )
            w.mark_set( 'insert', i )
            self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1020:fillParagraph
    #@+node:AGP.20250415230112.1021:fillRegion
    def fillRegion (self,event):
    
        '''Fill all paragraphs in the selected text.'''
        k = self.k
        w = self.editWidget(event)
        if not w or not self._chckSel(event): return
        
        self.beginCommand(undoType='fill-region')
    
        s1 = w.index('sel.first')
        s2 = w.index('sel.last')
        w.mark_set('insert',s1)
        self.backwardParagraph(event)
        if w.index('insert linestart') == '1.0':
            self.fillParagraph(event)
        while 1:
            self.forwardParagraph(event)
            if w.compare('insert','>',s2):
                break
            self.fillParagraph(event)
    
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1021:fillRegion
    #@+node:AGP.20250415230112.1022:fillRegionAsParagraph
    def fillRegionAsParagraph (self,event):
        
        '''Fill the selected text.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w or not self._chckSel(event): return
        
        self.beginCommand(undoType='fill-region-as-paragraph')
    
        i1 = w.index('sel.first linestart')
        i2 = w.index('sel.last lineend')
        txt = w.get(i1,i2)
        txt = self._addPrefix(txt)
        w.delete(i1,i2)
        w.insert(i1,txt)
    
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1022:fillRegionAsParagraph
    #@+node:AGP.20250415230112.1023:killParagraph (Test)
    def killParagraph (self,event):
        
        '''Kill the present paragraph.'''
    
        k = self.k ; c = k.c
        w = self.editWidget(event)
        if not w: return
    
        i = w.index('insert')
        txt = w.get('insert linestart','insert lineend')
        
        self.beginCommand(undoType='kill-paragraph')
    
        if not txt.strip():
            i = w.search(r'\w',i,regexp=True,stopindex='end')
        self.selectParagraphHelper(w,i)
        i2 = w.index('insert')
        c.killBufferCommands.kill(event,i,i2)
        w.mark_set('insert',i)
        w.selection_clear()
    
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1023:killParagraph (Test)
    #@+node:AGP.20250415230112.1024:extend-to-paragraph & helper
    def extendToParagraph (self,event):
        
        '''Select the paragraph surrounding the cursor.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        txt = w.get('insert linestart','insert lineend')
        txt = txt.strip()
        i = w.index('insert')
    
        if not txt:
            while 1:
                i = w.index('%s + 1 lines' % i)
                txt = w.get('%s linestart' % i,'%s lineend' % i).strip()
                if txt:
                    self.selectParagraphHelper(w,i) ; break
                if w.index('%s lineend' % i) == w.index('end'):
                    return
    
        if txt:
            while 1:
                i = w.index('%s - 1 lines' % i)
                txt = w.get('%s linestart' % i,'%s lineend' % i).strip()
                if not txt or w.index('%s linestart' % i) == w.index('1.0'):
                    if not txt: i = w.index('%s + 1 lines' % i)
                    self.selectParagraphHelper(w,i)
                    break
    #@+node:AGP.20250415230112.1025:selectParagraphHelper
    def selectParagraphHelper (self,w,start):
    
        i2 = start
        while 1:
            txt = w.get('%s linestart' % i2,'%s lineend' % i2)
            if w.index('%s lineend' % i2) == w.index('end'):
                break
            txt = txt.strip()
            if not txt: break
            else:
                i2 = w.index('%s + 1 lines' % i2)
    
        w.tag_add('sel','%s linestart' % start,'%s lineend' % i2)
        w.mark_set('insert','%s lineend' % i2)
    #@-node:AGP.20250415230112.1025:selectParagraphHelper
    #@-node:AGP.20250415230112.1024:extend-to-paragraph & helper
    #@-others
    #@-node:AGP.20250415230112.1018:paragraph...
    #@+node:AGP.20250415230112.1026:region...
    #@+others
    #@+node:AGP.20250415230112.1027:indentRegion (not used: use c.indentBody instead)
    def indentRegion (self,event):
        w = self.editWidget(event)
        if not w: return
    
        mrk = 'sel'
        trange = w.tag_ranges(mrk)
        if len(trange) != 0:
            ind = w.search('\w','%s linestart' % trange[0],stopindex='end',regexp=True)
            if not ind: return
            text = w.get('%s linestart' % ind,'%s lineend' % ind)
            sstring = text.lstrip()
            sstring = sstring [0]
            ws = text.split(sstring)
            if len(ws) > 1:
                ws = ws [0]
            else:
                ws = ''
            s, s1 = trange [0].split('.')
            e, e1 = trange [ -1].split('.')
            s = int(s)
            s = s + 1
            e = int(e) + 1
            for z in xrange(s,e):
                t2 = w.get('%s.0' % z,'%s.0 lineend' % z)
                t2 = t2.lstrip()
                t2 = ws + t2
                w.delete('%s.0' % z,'%s.0 lineend' % z)
                w.insert('%s.0' % z,t2)
        # self.removeRKeys(w)
    #@-node:AGP.20250415230112.1027:indentRegion (not used: use c.indentBody instead)
    #@+node:AGP.20250415230112.1028:tabIndentRegion (indent-rigidly)
    def tabIndentRegion (self,event):
        
        '''Insert a hard tab at the start of each line of the selected text.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w or not self._chckSel(event): return
        
        self.beginCommand(undoType='indent-rigidly')
    
        i = w.index('sel.first')
        i2 = w.index('sel.last')
        i = w.index('%s linestart' % i)
        i2 = w.index('%s linestart' % i2)
        while 1:
            w.insert(i,'\t')
            if i == i2: break
            i = w.index('%s + 1 lines' % i)
    #@-node:AGP.20250415230112.1028:tabIndentRegion (indent-rigidly)
    #@+node:AGP.20250415230112.1029:countRegion
    def countRegion (self,event):
        
        '''Print the number of lines and characters in the selected text.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        txt = w.get('sel.first','sel.last')
        lines = 1 ; chars = 0
        for z in txt:
            if z == '\n': lines += 1
            else:         chars += 1
    
        k.setLabelGrey('Region has %s lines, %s character%s' % (
            lines,chars,g.choose(chars==1,'','s')))
    #@-node:AGP.20250415230112.1029:countRegion
    #@+node:AGP.20250415230112.1030:moveLinesDown (works)
    def moveLinesDown (self,event):
        
        '''Move all lines containing any selected text down one line,
        moving to the next node if the lines are the last lines of the body.'''
    
        c = self.c
        w = self.editWidget(event)
        if not w or not self._chckSel(event): return
    
        self.beginCommand(undoType='move-lines-down')
    
        i,j = g.app.gui.getSelectionRange(w)
        i = w.index(i+' linestart')
        j = w.index(j+' lineend+1c')
        j2 = w.index(j+ ' lineend+1c')
        selected = w.get(i,j) # g.trace('selected',repr(selected))
        moved = w.get(j,j2)  # g.trace('moved',repr(moved))
        if moved:
            if not moved.endswith('\n'): moved = moved + '\n'
            w.mark_set('i',i)
            w.mark_set('j',j)
            w.delete(j,j2)
            w.insert(i,moved)
            w.mark_set('sel.start','i')
            w.mark_set('sel.end','j')
            w.mark_unset('i')
            w.mark_unset('j')
        elif g.app.gui.widget_name(w).startswith('body'):
            # Move the text to the top of the next node.
            p = c.currentPosition()
            if not p.hasThreadNext(): return
            if not moved.endswith('\n'): moved = moved + '\n'
            w.delete(i,j) # Deleted the old selection.
            c.setBodyString(p,w.get('1.0','end')) # Doesn't really work: undo doesn't work.
            p = p.threadNext()
            c.beginUpdate()
            c.selectPosition(p)
            c.endUpdate()
            w.focus_force()
            w.insert('1.0',selected)
            g.app.gui.setSelectionRangeWithLength(w,'1.0',len(selected)-1)
    
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1030:moveLinesDown (works)
    #@+node:AGP.20250415230112.1031:moveLinesUp (works, except for selection point when last line selected)
    def moveLinesUp (self,event):
        
        '''Move all lines containing any selected text up one line,
        moving to the previous node as needed.'''
    
        c = self.c
        w = self.editWidget(event)
        if not w: return
    
        if not g.app.gui.hasSelection(w): return
        
        self.beginCommand(undoType='move-lines-up')
        
        i,j = g.app.gui.getSelectionRange(w)
        i = w.index(i+' linestart')
        j = w.index(j+' lineend+1c')
        i2 = w.index(i+'-1c linestart')
        selected = w.get(i,j) # ; g.trace('selected',repr(selected))
        moved = w.get(i2,i)   # ; g.trace('moved',repr(moved))
    
        if moved:
            w.mark_set('i',i)
            w.mark_set('j',j)
            w.delete(i2,i)
            if w.compare('j','==','end'):
                if moved.endswith('\n'): moved = moved[:-1]
                w.insert('j','\n' + moved)
            else:
                w.insert('j',moved)
            w.mark_unset('sel')
            w.mark_set('sel.start','i')
            w.mark_set('sel.end','j')
            w.mark_unset('i')
            w.mark_unset('j')
        elif g.app.gui.widget_name(w).startswith('body'):
            p = c.currentPosition()
            if not p.hasThreadBack(): return
            w.delete(i,j+'+1c')
            c.setBodyString(p,w.get('1.0','end'))
            p = p.threadBack()
            c.beginUpdate()
            c.selectPosition(p)
            c.endUpdate()
            w.focus_force()
            s = g.app.gui.getAllText(w)
            if s.endswith('\n'):
                w.insert('end',selected)
            else:
                if selected.endswith('\n'): selected = selected[:-1]
                w.insert('end','\n'+selected)
            g.app.gui.setSelectionRange(w,'end-%dc' % (len(selected)+1),'end-1c') # works
    
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1031:moveLinesUp (works, except for selection point when last line selected)
    #@+node:AGP.20250415230112.1032:reverseRegion
    def reverseRegion (self,event):
        
        '''Reverse the order of lines in the selected text.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w or not self._chckSel(event): return
    
        self.beginCommand(undoType='reverse-region')
    
        ins = w.index('insert')
        is1 = w.index('sel.first')
        is2 = w.index('sel.last')
        txt = w.get('%s linestart' % is1,'%s lineend' % is2)
        w.delete('%s linestart' % is1,'%s lineend' % is2)
        txt = txt.split('\n')
        txt.reverse()
        istart = is1.split('.')
        istart = int(istart[0])
        for z in txt:
            w.insert('%s.0' % istart,'%s\n' % z)
            istart = istart + 1
        w.mark_set('insert',ins)
        k.clearState()
        k.resetLabel()
        
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1032:reverseRegion
    #@+node:AGP.20250415230112.1033:up/downCaseRegion & helper
    def downCaseRegion (self,event):
        '''Convert all characters in the selected text to lower case.'''
        self.caseHelper(event,'low','downcase-region')
        
    def upCaseRegion (self,event):
        '''Convert all characters in the selected text to UPPER CASE.'''
        self.caseHelper(event,'up','upcase-region')
        
    def caseHelper (self,event,way,undoType):
    
        w = self.editWidget(event)
        if not w: return
    
        trange = w.tag_ranges('sel')
        if len(trange) != 0:
            self.beginCommand(undoType=undoType)
            text = w.get(trange[0],trange[-1])
            i = w.index('insert')
            if text == ' ': return
            w.delete(trange[0],trange[-1])
            if way == 'low': text = text.lower()
            if way == 'up':  text = text.upper()
            w.insert('insert',text)
            w.mark_set('insert',i)
            self.endCommand(changed=True,setLabel=True)
    
        # self.removeRKeys(w)
    #@-node:AGP.20250415230112.1033:up/downCaseRegion & helper
    #@-others
    #@-node:AGP.20250415230112.1026:region...
    #@+node:AGP.20250415230112.1034:scrolling...
    #@+node:AGP.20250415230112.1035:scrollUp/Down/extendSelection
    def scrollDown (self,event):
        '''Scroll the presently selected pane down one page.'''
        self.scrollHelper(event,'down',extend=False)
    
    def scrollDownExtendSelection (self,event):
        '''Extend the text selection by scrolling the body text down one page.'''
        self.scrollHelper(event,'down',extend=True)
    
    def scrollUp (self,event):
        '''Scroll the presently selected pane up one page.'''
        self.scrollHelper(event,'up',extend=False)
    
    def scrollUpExtendSelection (self,event):
        '''Extend the text selection by scrolling the body text up one page.'''
        self.scrollHelper(event,'up',extend=True)
    #@+node:AGP.20250415230112.1036:scrollHelper
    def scrollHelper (self,event,direction,extend):
    
        k = self.k ; c = k.c
        w = event and event.widget
        if not w: return #  This does **not** require a text widget.
    
        if g.app.gui.isTextWidget(w):
    
            c.widgetWantsFocusNow(w)
        
            # Remember the original insert point.  This may become the moveSpot.
            ins1 = w.index('insert')
            row, col = ins1.split('.') ; row = int(row) ; col = int(col)
        
            # Compute the spot.
            chng = self.measure(w) ; delta = chng [0]
            row1 = g.choose(direction=='down',row+delta,row-delta)
            spot = w.index('%d.%d' % (row1,col))
            w.mark_set('insert',spot)
        
            # Handle the extension.
            self.extendHelper(w,extend,ins1,spot,setSpot=False)
            w.see('insert')
        elif g.app.gui.widget_name(w).startswith('canvas'):
            if direction=='down':
                self.scrollOutlineDownPage()
            else:
                self.scrollOutlineUpPage()
    #@-node:AGP.20250415230112.1036:scrollHelper
    #@+node:AGP.20250415230112.1037:measure
    def measure (self,w):
        i = w.index('insert')
        i1, i2 = i.split('.')
        start = int(i1)
        watch = 0
        ustart = start
        pone = 1
        top = i
        bottom = i
        while pone:
            ustart = ustart-1
            if ustart < 0:
                break
            ds = '%s.0' % ustart
            pone = w.dlineinfo(ds)
            if pone:
                top = ds
                watch = watch + 1
        pone = 1
        ustart = start
        while pone:
            ustart = ustart + 1
            ds = '%s.0' % ustart
            pone = w.dlineinfo(ds)
            if pone:
                bottom = ds
                watch = watch + 1
    
        return watch, top, bottom
    #@-node:AGP.20250415230112.1037:measure
    #@-node:AGP.20250415230112.1035:scrollUp/Down/extendSelection
    #@+node:AGP.20250415230112.1038:scrollOutlineUp/Down/Line/Page
    def scrollOutlineDownLine (self,event=None):
        '''Scroll the outline pane down one line.'''
        a,b = self.c.frame.treeBar.get()
        if b < 1.0:
            self.c.frame.tree.canvas.yview_scroll(1,"unit")
        
    def scrollOutlineDownPage (self,event=None):
        '''Scroll the outline pane down one page.'''
        a,b = self.c.frame.treeBar.get()
        if b < 1.0:
            self.c.frame.tree.canvas.yview_scroll(1,"page")
    
    def scrollOutlineUpLine (self,event=None):
        '''Scroll the outline pane up one line.'''
        a,b = self.c.frame.treeBar.get()
        if a > 0.0:
            self.c.frame.tree.canvas.yview_scroll(-1,"unit")
    
    def scrollOutlineUpPage (self,event=None):
        '''Scroll the outline pane up one page.'''
        a,b = self.c.frame.treeBar.get()
        if a > 0.0:
            self.c.frame.tree.canvas.yview_scroll(-1,"page")
    #@-node:AGP.20250415230112.1038:scrollOutlineUp/Down/Line/Page
    #@+node:AGP.20250415230112.1039:scrollOutlineLeftRight
    def scrollOutlineLeft (self,event=None):
        '''Scroll the outline left.'''
        self.c.frame.tree.canvas.xview_scroll(1,"unit")
        
    def scrollOutlineRight (self,event=None):
        '''Scroll the outline left.'''
        self.c.frame.tree.canvas.xview_scroll(-1,"unit")
    #@-node:AGP.20250415230112.1039:scrollOutlineLeftRight
    #@-node:AGP.20250415230112.1034:scrolling...
    #@+node:AGP.20250415230112.1040:sort...
    '''XEmacs provides several commands for sorting text in a buffer.  All
    operate on the contents of the region (the text between point and the
    mark).  They divide the text of the region into many "sort records",
    identify a "sort key" for each record, and then reorder the records
    using the order determined by the sort keys.  The records are ordered so
    that their keys are in alphabetical order, or, for numerical sorting, in
    numerical order.  In alphabetical sorting, all upper-case letters `A'
    through `Z' come before lower-case `a', in accordance with the ASCII
    character sequence.
    
       The sort commands differ in how they divide the text into sort
    records and in which part of each record they use as the sort key.
    Most of the commands make each line a separate sort record, but some
    commands use paragraphs or pages as sort records.  Most of the sort
    commands use each entire sort record as its own sort key, but some use
    only a portion of the record as the sort key.
    
    `M-x sort-lines'
         Divide the region into lines and sort by comparing the entire text
         of a line.  A prefix argument means sort in descending order.
    
    `M-x sort-paragraphs'
         Divide the region into paragraphs and sort by comparing the entire
         text of a paragraph (except for leading blank lines).  A prefix
         argument means sort in descending order.
    
    `M-x sort-pages'
         Divide the region into pages and sort by comparing the entire text
         of a page (except for leading blank lines).  A prefix argument
         means sort in descending order.
    
    `M-x sort-fields'
         Divide the region into lines and sort by comparing the contents of
         one field in each line.  Fields are defined as separated by
         whitespace, so the first run of consecutive non-whitespace
         characters in a line constitutes field 1, the second such run
         constitutes field 2, etc.
    
         You specify which field to sort by with a numeric argument: 1 to
         sort by field 1, etc.  A negative argument means sort in descending
         order.  Thus, minus 2 means sort by field 2 in reverse-alphabetical
         order.
    
    `M-x sort-numeric-fields'
         Like `M-x sort-fields', except the specified field is converted to
         a number for each line and the numbers are compared.  `10' comes
         before `2' when considered as text, but after it when considered
         as a number.
    
    `M-x sort-columns'
         Like `M-x sort-fields', except that the text within each line used
         for comparison comes from a fixed range of columns.  An explanation
         is given below.
    
       For example, if the buffer contains:
    
         On systems where clash detection (locking of files being edited) is
         implemented, XEmacs also checks the first time you modify a buffer
         whether the file has changed on disk since it was last visited or
         saved.  If it has, you are asked to confirm that you want to change
         the buffer.
    
    then if you apply `M-x sort-lines' to the entire buffer you get:
    
         On systems where clash detection (locking of files being edited) is
         implemented, XEmacs also checks the first time you modify a buffer
         saved.  If it has, you are asked to confirm that you want to change
         the buffer.
         whether the file has changed on disk since it was last visited or
    
    where the upper case `O' comes before all lower case letters.  If you
    apply instead `C-u 2 M-x sort-fields' you get:
    
         saved.  If it has, you are asked to confirm that you want to change
         implemented, XEmacs also checks the first time you modify a buffer
         the buffer.
         On systems where clash detection (locking of files being edited) is
         whether the file has changed on disk since it was last visited or
    
    where the sort keys were `If', `XEmacs', `buffer', `systems', and `the'.
    
       `M-x sort-columns' requires more explanation.  You specify the
    columns by putting point at one of the columns and the mark at the other
    column.  Because this means you cannot put point or the mark at the
    beginning of the first line to sort, this command uses an unusual
    definition of `region': all of the line point is in is considered part
    of the region, and so is all of the line the mark is in.
    
       For example, to sort a table by information found in columns 10 to
    15, you could put the mark on column 10 in the first line of the table,
    and point on column 15 in the last line of the table, and then use this
    command.  Or you could put the mark on column 15 in the first line and
    point on column 10 in the last line.
    
       This can be thought of as sorting the rectangle specified by point
    and the mark, except that the text on each line to the left or right of
    the rectangle moves along with the text inside the rectangle.  *Note
    Rectangles::.
    
    '''
    #@+node:AGP.20250415230112.1041:sortLines
    def sortLines (self,event,which=None):
        
        '''Sort lines of the selected text by comparing the entire text of a line.
        A prefix argument means sort in descending order.'''
    
        c = self.c ; k = c.k
        w = self.editWidget(event)
        if not w or not self._chckSel(event): return
    
        self.beginCommand(undoType='sort-lines')
        i = w.index('sel.first')
        i2 = w.index('sel.last')
        is1 = i.split('.')
        is2 = i2.split('.')
        txt = w.get('%s.0' % is1[0],'%s.0 lineend' % is2[0])
        ins = w.index('insert')
        txt = txt.split('\n')
        w.delete('%s.0' % is1[0],'%s.0 lineend' % is2[0])
        txt.sort()
        if which:
            txt.reverse()
        inum = int(is1[0])
        for z in txt:
            w.insert('%s.0' % inum,'%s\n' % z)
            inum = inum + 1
        w.mark_set('insert',ins)
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1041:sortLines
    #@+node:AGP.20250415230112.1042:sortColumns
    def sortColumns (self,event):
        
        '''Sort lines of selected text using only lines in the given columns to do the comparison.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w or not self._chckSel(event): return
    
        self.beginCommand(undoType='sort-columns')
        ins = w.index('insert')
        is1 = w.index('sel.first')
        is2 = w.index('sel.last')
        sint1, sint2 = is1.split('.')
        sint2 = int(sint2)
        sint3, sint4 = is2.split('.')
        sint4 = int(sint4)
        txt = w.get('%s.0' % sint1,'%s.0 lineend' % sint3)
        w.delete('%s.0' % sint1,'%s.0 lineend' % sint3)
        columns = []
        i = int(sint1)
        i2 = int(sint3)
        while i <= i2:
            t = w.get('%s.%s' % (i,sint2),'%s.%s' % (i,sint4))
            columns.append(t)
            i = i + 1
        txt = txt.split('\n')
        zlist = zip(columns,txt)
        zlist.sort()
        i = int(sint1)
        for z in xrange(len(zlist)):
             w.insert('%s.0' % i,'%s\n' % zlist[z][1])
             i = i + 1
        w.mark_set('insert',ins)
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1042:sortColumns
    #@+node:AGP.20250415230112.1043:sortFields
    def sortFields (self,event,which=None):
        
        '''Divide the selected text into lines and sort by comparing the contents of
         one field in each line. Fields are defined as separated by whitespace, so
         the first run of consecutive non-whitespace characters in a line
         constitutes field 1, the second such run constitutes field 2, etc.
    
         You specify which field to sort by with a numeric argument: 1 to sort by
         field 1, etc. A negative argument means sort in descending order. Thus,
         minus 2 means sort by field 2 in reverse-alphabetical order.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w or not self._chckSel(event): return
    
        self.beginCommand(undoType='sort-fields')
        ins = w.index('insert')
        is1 = w.index('sel.first')
        is2 = w.index('sel.last')
        txt = w.get('%s linestart' % is1,'%s lineend' % is2)
        txt = txt.split('\n')
        fields = []
        fn = r'\w+'
        frx = re.compile(fn)
        for z in txt:
            f = frx.findall(z)
            if not which:
                fields.append(f[0])
            else:
                i = int(which)
                if len(f) < i: return
                i = i-1
                fields.append(f[i])
        nz = zip(fields,txt)
        nz.sort()
        w.delete('%s linestart' % is1,'%s lineend' % is2)
        i = is1.split('.')
        int1 = int(i[0])
        for z in nz:
            w.insert('%s.0' % int1,'%s\n' % z[1])
            int1 = int1 + 1
        w.mark_set('insert',ins)
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1043:sortFields
    #@-node:AGP.20250415230112.1040:sort...
    #@+node:AGP.20250415230112.1044:swap/transpose...
    #@+node:AGP.20250415230112.1045:swapHelper
    def swapHelper (self,w,find,ftext,lind,ltext):
    
        w.delete(find,'%s wordend' % find)
        w.insert(find,ltext)
        w.delete(lind,'%s wordend' % lind)
        w.insert(lind,ftext)
        self.swapSpots.pop()
        self.swapSpots.pop()
    #@-node:AGP.20250415230112.1045:swapHelper
    #@+node:AGP.20250415230112.1046:transposeLines
    def transposeLines (self,event):
        
        '''Transpose the line containing the cursor with the preceding line.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        i = w.index('insert')
        i1, i2 = i.split('.')
        i1 = str(int(i1)-1)
    
        self.beginCommand(undoType='transpose-lines')
    
        if i1 != '0':
            l2 = w.get('insert linestart','insert lineend')
            w.delete('insert linestart-1c','insert lineend')
            w.insert(i1+'.0',l2+'\n')
        else:
            l2 = w.get('2.0','2.0 lineend')
            w.delete('2.0','2.0 lineend')
            w.insert('1.0',l2+'\n')
    
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1046:transposeLines
    #@+node:AGP.20250415230112.1047:swapWords
    def swapWords (self,event,swapspots):
        
        '''Transpose the word at the cursor with the preceding word.'''
    
        w = self.editWidget(event)
        if not w: return
    
        txt = w.get('insert wordstart','insert wordend')
        if not txt: return
        
        i = w.index('insert wordstart')
        
        self.beginCommand(undoType='swap-words')
    
        if len(swapspots) != 0:
            if w.compare(i,'>',swapspots[1]):
                self.swapHelper(w,i,txt,swapspots[1],swapspots[0])
            elif w.compare(i,'<',swapspots[1]):
                self.swapHelper(w,swapspots[1],swapspots[0],i,txt)
        else:
            swapspots.append(txt)
            swapspots.append(i)
    
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1047:swapWords
    #@+node:AGP.20250415230112.1048:transposeWords (doesn't work)
    def transposeWords (self,event):
        
        '''Transpose the word at the cursor with the preceding word.'''
        
        w = self.editWidget(event)
        if not w: return
        
        self.beginCommand(undoType='transpose-words')
        self.swapWords(event,self.swapSpots)
        self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1048:transposeWords (doesn't work)
    #@+node:AGP.20250415230112.1049:swapCharacters & transeposeCharacters
    def swapCharacters (self,event):
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        i = w.index('insert')
        c1 = w.get('insert','insert +1c')
        c2 = w.get('insert -1c','insert')
        
        self.beginCommand(undoType='swap-characters')
        w.delete('insert -1c','insert')
        w.insert('insert',c1)
        w.delete('insert','insert +1c')
        w.insert('insert',c2)
        w.mark_set('insert',i)
        self.endCommand(changed=True,setLabel=True)
    
    transposeCharacters = swapCharacters
    #@-node:AGP.20250415230112.1049:swapCharacters & transeposeCharacters
    #@-node:AGP.20250415230112.1044:swap/transpose...
    #@+node:AGP.20250415230112.1050:tabify & untabify
    def tabify (self,event):
        '''Convert 4 spaces to tabs in the selected text.'''
        self.tabifyHelper (event,which='tabify')
        
    def untabify (self,event):
        '''Convert tabs to 4 spaces in the selected text.'''
        self.tabifyHelper (event,which='untabify')
    
    def tabifyHelper (self,event,which):
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        if w.tag_ranges('sel'):
            self.beginCommand(undoType=which)
            i = w.index('sel.first')
            end = w.index('sel.last')
            txt = w.get(i,end)
            if which == 'tabify':
                pattern = re.compile(' {4,4}') # Huh?
                ntxt = pattern.sub('\t',txt)
            else:
                pattern = re.compile('\t')
                ntxt = pattern.sub('    ',txt)
            w.delete(i,end)
            w.insert(i,ntxt)
            self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1050:tabify & untabify
    #@-others
#@-node:AGP.20250415230112.896:editCommandsClass
#@+node:AGP.20250415230112.1051:editFileCommandsClass
class editFileCommandsClass (baseEditCommandsClass):
    
    '''A class to load files into buffers and save buffers to files.'''
    
    #@    @+others
    #@+node:AGP.20250415230112.1052: ctor
    def __init__ (self,c):
    
        baseEditCommandsClass.__init__(self,c) # init the base class.
    #@-node:AGP.20250415230112.1052: ctor
    #@+node:AGP.20250415230112.1053: getPublicCommands (editFileCommandsClass)
    def getPublicCommands (self):
        
        k = self.k
    
        return {
            'delete-file':          self.deleteFile,
            'diff':                 self.diff, 
            'insert-file':          self.insertFile,
            'make-directory':       self.makeDirectory,
            'open-outline-by-name': self.openOutlineByName,
            'remove-directory':     self.removeDirectory,
            'save-file':            self.saveFile
        }
    #@-node:AGP.20250415230112.1053: getPublicCommands (editFileCommandsClass)
    #@+node:AGP.20250415230112.1054:deleteFile
    def deleteFile (self,event):
        
        '''Prompt for the name of a file and delete it.'''
    
        k = self.k ; state = k.getState('delete_file')
    
        if state == 0:
            prefix = 'Delete File: '
            k.setLabelBlue('%s%s%s' % (prefix,os.getcwd(),os.sep))
            k.getArg(event,'delete_file',1,self.deleteFile,prefix=prefix)
        else:
            k.keyboardQuit(event)
            k.clearState()
            try:
                os.remove(k.arg)
                k.setLabel('Deleted: %s' % k.arg)
            except:
                k.setLabel('Not Deleted: %s' % k.arg)
    #@-node:AGP.20250415230112.1054:deleteFile
    #@+node:AGP.20250415230112.1055:diff (revise)
    def diff (self,event):
    
        '''Creates a node and puts the diff between 2 files into it.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        try:
            f, name = self.getReadableTextFile()
            txt1 = f.read() ; f.close()
            f2, name2 = self.getReadableTextFile()
            txt2 = f2.read() ; f2.close()
        except IOError: return
    
        ### self.switchToBuffer(event,"*diff* of ( %s , %s )" % (name,name2))
        data = difflib.ndiff(txt1,txt2)
        idata = []
        for z in data:
            idata.append(z)
        w.delete('1.0','end')
        w.insert('1.0',''.join(idata))
    #@-node:AGP.20250415230112.1055:diff (revise)
    #@+node:AGP.20250415230112.1056:getReadableTextFile
    def getReadableTextFile (self):
    
        fname = tkFileDialog and tkFileDialog.askopenfilename()
        if fname == None:
            return None, None
        else:
            f = open(fname,'rt')
            return f, fname
    #@-node:AGP.20250415230112.1056:getReadableTextFile
    #@+node:AGP.20250415230112.1057:insertFile
    def insertFile (self,event):
        
        '''Prompt for the name of a file and put the selected text into it.'''
    
        k = self.k ; c = k.c
        w = self.editWidget(event)
        if not w: return
    
        f, name = self.getReadableTextFile()
        if f:
            txt = f.read()
            f.close()
            w.insert('insert',txt)
            w.see('1.0')
    #@-node:AGP.20250415230112.1057:insertFile
    #@+node:AGP.20250415230112.1058:makeDirectory
    def makeDirectory (self,event):
        
        '''Prompt for the name of a directory and create it.'''
    
        k = self.k ; state = k.getState('make_directory')
    
        if state == 0:
            prefix = 'Make Directory: '
            k.setLabelBlue('%s%s%s' % (prefix,os.getcwd(),os.sep))
            k.getArg(event,'make_directory',1,self.makeDirectory,prefix=prefix)
        else:
            k.keyboardQuit(event)
            k.clearState()
            try:
                os.mkdir(k.arg)
                k.setLabel("Created: %s" % k.arg)
            except:
                k.setLabel("Not Create: %s" % k.arg)
    #@-node:AGP.20250415230112.1058:makeDirectory
    #@+node:AGP.20250415230112.1059:open-outline-by-name
    def openOutlineByName (self,event):
        
        '''Prompt for the name of a Leo outline and open it.'''
    
        k = self.k
        k.setLabelBlue('Open Leo Outline: ',protect=True)
        k.getFileName(event,handler=self.openOutlineByNameFinisher)
    
    def openOutlineByNameFinisher (self,event):
    
        c = self.c ; k = self.k ; fileName = k.arg
        
        k.resetLabel()
        if fileName and g.os_path_exists(fileName) and not g.os_path_isdir(fileName):
            g.openWithFileName(fileName,c)
    #@-node:AGP.20250415230112.1059:open-outline-by-name
    #@+node:AGP.20250415230112.1060:removeDirectory
    def removeDirectory (self,event):
        
        '''Prompt for the name of a directory and delete it.'''
    
        k = self.k ; state = k.getState('remove_directory')
    
        if state == 0:
            prefix = 'Remove Directory: '
            k.setLabelBlue('%s%s%s' % (prefix,os.getcwd(),os.sep))
            k.getArg(event,'remove_directory',1,self.removeDirectory,prefix=prefix)
        else:
            k.keyboardQuit(event)
            k.clearState()
            try:
                os.rmdir(k.arg)
                k.setLabel('Removed: %s' % k.arg)
            except:
                k.setLabel('Not Remove: %s' % k.arg)
    #@-node:AGP.20250415230112.1060:removeDirectory
    #@+node:AGP.20250415230112.1061:saveFile
    def saveFile (self,event):
        
        '''Prompt for the name of a file and put the body text of the selected node into it..'''
    
        w = self.editWidget(event)
        if not w: return
    
        txt = w.get('1.0','end')
        f = tkFileDialog and tkFileDialog.asksaveasfile()
        if f:
            f.write(txt)
            f.close()
    #@-node:AGP.20250415230112.1061:saveFile
    #@-others
#@-node:AGP.20250415230112.1051:editFileCommandsClass
#@+node:AGP.20250415230112.1062:helpCommandsClass
class helpCommandsClass (baseEditCommandsClass):
    
    '''A class to load files into buffers and save buffers to files.'''
    
    #@    @+others
    #@+node:AGP.20250415230112.1063:getPublicCommands (helpCommands)
    def getPublicCommands (self):
        
        return {
            'help-for-minibuffer':      self.helpForMinibuffer,
            'help-for-command':         self.helpForCommand,
            'apropos-autocompletion':   self.aproposAutocompletion,
            'apropos-bindings':         self.aproposBindings,
            'apropos-find-commands':    self.aproposFindCommands,
            'python-help':              self.pythonHelp,
        }
    #@-node:AGP.20250415230112.1063:getPublicCommands (helpCommands)
    #@+node:AGP.20250415230112.1064:helpForMinibuffer
    def helpForMinibuffer (self,event=None):
        
        '''Print a messages telling you how to get started with Leo.'''
    
        # A bug in Leo: triple quotes puts indentation before each line.
        c = self.c
        s = '''
    The mini-buffer is intended to be like the Emacs buffer:
    
    full-command: (default shortcut: Alt-x) Puts the focus in the minibuffer. Type a
    full command name, then hit <Return> to execute the command. Tab completion
    works, but not yet for file names.
    
    quick-command-mode (default shortcut: Alt-x). Like Emacs Control-C. This mode is
    defined in leoSettings.leo. It is useful for commonly-used commands.
    
    universal-argument (default shortcut: Alt-u). Like Emacs Ctrl-u. Adds a repeat
    count for later command. Ctrl-u 999 a adds 999 a's. Many features remain
    unfinished.
    
    keyboard-quit (default shortcut: Ctrl-g) Exits any minibuffer mode and puts
    the focus in the body pane.
    
    Use the help-for-command command to see documentation for a particular command.
    '''
    
        s = g.adjustTripleString(s,c.tab_width)
            # Remove indentation from indentation of this function.
        # s = s % (shortcuts[0],shortcuts[1],shortcuts[2],shortcuts[3])
        
        if not g.app.unitTesting:
            g.es_print(s)
    #@+node:AGP.20250415230112.1065:test_helpForMinibuffer
    def test_help(self):
        
        c.helpCommands.helpForMinibuffer()
    #@-node:AGP.20250415230112.1065:test_helpForMinibuffer
    #@-node:AGP.20250415230112.1064:helpForMinibuffer
    #@+node:AGP.20250415230112.1066:helpForCommand
    def helpForCommand (self,event):
        
        '''Prompts for a command name and prints the help message for that command.'''
        
        k = self.k
        k.fullCommand(event,help=True,helpHandler=self.helpForCommandFinisher)
        
    def helpForCommandFinisher (self,commandName):
    
        c = self.c
        bindings = self.getBindingsForCommand(commandName)
        func = c.commandsDict.get(commandName)
        if func and func.__doc__:
            s = ''.join([
                g.choose(line.strip(),line.lstrip(),'\n')
                    for line in g.splitLines(func.__doc__)])
        else:
            s = 'no docstring'
        g.es('%s:%s\n%s\n' % (commandName,bindings,s),color='blue')
    
    def getBindingsForCommand(self,commandName):
    
        c = self.c ; k = c.k ; d = k.bindingsDict
        keys = d.keys() ; keys.sort()
    
        data = [] ; n1 = 4 ; n2 = 20
        for key in keys:
            bunchList = d.get(key,[])
            for b in bunchList:
                if b.commandName == commandName:
                    pane = g.choose(b.pane=='all','',' %s:' % (b.pane))
                    s1 = pane
                    s2 = k.prettyPrintKey(key,brief=True)
                    s3 = b.commandName
                    n1 = max(n1,len(s1))
                    n2 = max(n2,len(s2))
                    data.append((s1,s2,s3),)
    
        data.sort(lambda x,y: cmp(x[1],y[1]))
            
        return ','.join(['%s %s' % (s1,s2) for s1,s2,s3 in data])
            # g.es('%*s %*s %s' % (-n1,s1,-(min(12,n2)),s2,s3))
    #@nonl
    #@-node:AGP.20250415230112.1066:helpForCommand
    #@+node:AGP.20250415230112.1067:aproposAutocompletion
    def aproposAutocompletion (self,event=None):
        
        '''Prints a discussion of autocompletion.'''
        
        c = self.c ; s = '''
    This documentation describes both autocompletion and calltips.
    
    Typing a period when @language python is in effect starts autocompletion. Typing
    '(' during autocompletion shows the calltip. Typing Return or Control-g
    (keyboard-quit) exits autocompletion or calltips.
    
    Autocompletion
        
    Autocompletion shows what may follow a period in code. For example, after typing
    g. Leo will show a list of all the global functions in leoGlobals.py.
    Autocompletion works much like tab completion in the minibuffer. Unlike the
    minibuffer, the presently selected completion appears directly in the body
    pane.
    
    A leading period brings up 'Autocomplete Modules'. (The period goes away.) You
    can also get any module by typing its name. If more than 25 items would appear
    in the Autocompleter tab, Leo shows only the valid starting characters. At this
    point, typing an exclamation mark shows the complete list. Thereafter, typing
    further exclamation marks toggles between full and abbreviated modes.
    
    If x is a list 'x.!' shows all its elements, and if x is a Python dictionary,
    'x.!' shows x.keys(). For example, 'sys.modules.!' Again, further exclamation
    marks toggles between full and abbreviated modes.
    
    During autocompletion, typing a question mark shows the docstring for the
    object. For example: 'g.app?' shows the docstring for g.app. This doesn't work
    (yet) directly for Python globals, but '__builtin__.f?' does. Example:
    '__builtin__.pow?' shows the docstring for pow.
    
    Autocompletion works in the Find tab; you can use <Tab> to cycle through the
    choices. The 'Completion' tab appears while you are doing this; the Find tab
    reappears once the completion is finished.
    
    Calltips
    
    Calltips appear after you type an open parenthesis in code. Calltips shows the
    expected arguments to a function or method. Calltips work for any Python
    function or method, including Python's global function. Examples:
    
    a)  'g.toUnicode('  gives 'g.toUnicode(s, encoding, reportErrors=False'
    b) 'c.widgetWantsFocusNow' gives 'c.widgetWantsFocusNow(w'
    c) 'reduce(' gives 'reduce(function, sequence[, initial]) -> value'
    
    The calltips appear directly in the text and the argument list is highlighted so
    you can just type to replace it. The calltips appear also in the status line for
    reference after you have started to replace the args.
    
    Options
    
    Both autocompletion and calltips are initially enabled or disabled by the
    enable_autocompleter_initially and enable_calltips_initially settings in
    leoSettings.leo. You may enable or disable these features at any time with these
    commands: enable-autocompleter, enable-calltips, disable-autocompleter and
    disable-calltips.
    '''
    
        if not g.app.unitTesting:
            # Remove indentation from indentation of this function.
            s = g.adjustTripleString(s,c.tab_width)
            g.es_print(s)
    #@+node:AGP.20250415230112.1068:test_aproposAutocompletion
    def test_aproposAutocompletion (self):
    
        c.helpCommands.aproposAutocompletion()
    #@-node:AGP.20250415230112.1068:test_aproposAutocompletion
    #@-node:AGP.20250415230112.1067:aproposAutocompletion
    #@+node:AGP.20250415230112.1069:aproposBindings
    def aproposBindings (self,event=None):
        
        '''Prints a discussion of keyboard bindings.'''
        
        c = self.c
        s = '''
    A shortcut specification has the form:
        
    command-name = shortcutSpecifier
    
    or
    
    command-name ! pane = shortcutSpecifier
    
    The first form creates a binding for all panes except the minibuffer. The second
    form creates a binding for one or more panes. The possible values for 'pane'
    are:
    
    pane    bound panes
    ----    -----------
    all     body,log,tree
    body    body
    log     log
    mini    minibuffer
    text    body,log
    tree    tree
        
    You may use None as the specifier. Otherwise, a shortcut specifier consists of a
    head followed by a tail. The head may be empty, or may be a concatenation of the
    following: (All entries in each row are equivalent).
        
    Shift+ Shift-
    Alt+ or Alt-
    Control+, Control-, Ctrl+ or Ctrl-
    
    Notes:
    
    1. The case of plain letters is significant:  a is not A.
    
    2. The Shift- (or Shift+) prefix can be applied *only* to letters or
    multi-letter tails. Leo will ignore (with a warning) the shift prefix applied to
    other single letters, e.g., Ctrl-Shift-(
    
    3. The case of letters prefixed by Ctrl-, Alt-, Key- or Shift- is *not*
    significant.
    
    The following table illustrates these rules.  In each row, the first entry is the key (for k.bindingsDict) and the other entries are equivalents that the user may specify in leoSettings.leo:
    
    a, Key-a, Key-A
    A, Shift-A
    Alt-a, Alt-A
    Alt-A, Alt-Shift-a, Alt-Shift-A
    Ctrl-a, Ctrl-A
    Ctrl-A, Ctrl-Shift-a, Ctrl-Shift-A
    !, Key-!,Key-exclam,exclam
    '''
    
        s = g.adjustTripleString(s,c.tab_width)
            # Remove indentation from indentation of this function.
            
        if not g.app.unitTesting:
            g.es_print(s)
    #@+node:AGP.20250415230112.1070:test_apropos_bindings
    def test_apropos_bindings (self):
    
        c.helpCommands.aproposBindings()
    #@-node:AGP.20250415230112.1070:test_apropos_bindings
    #@-node:AGP.20250415230112.1069:aproposBindings
    #@+node:AGP.20250415230112.1071:aproposFindCommands
    def aproposFindCommands (self, event=None):
        
        '''Prints a discussion of of Leo's find commands.'''
        
        c = self.c
        
        #@    << define s >>
        #@+node:AGP.20250415230112.1072:<< define s >>
        s = '''
        Important: all minibuffer search commands, with the exception of the isearch (incremental) commands, simply provide a minibuffer interface to Leo's legacy find commands.  This means that all the powerful features of Leo's legacy commands are available to the minibuffer search commands.
        
        Note: all bindings shown are the default bindings for these commands.  You may change any of these bindings using @shortcut nodes in leoSettings.leo.
        
        Settings
        
        leoSettings.leo now contains several settings related to the Find tab:
        
        - @bool show_only_find_tab_options = True
        
        When True (recommended), the Find tab does not show the 'Find', 'Change', 'Change, Then Find', 'Find All' and 'Change All' buttons.
        
        - @bool minibufferSearchesShowFindTab = True
        
        When True, Leo shows the Find tab when executing most of the commands discussed below.  It's not necessary for it to be visible, but I think it provides good feedback about what search-with-present-options does.  YMMY.  When True, the sequence Control-F, Control-G is one way to show the Find Tab.
        
        Basic find commands
        
        - The open-find-tab command makes the Find tab visible.  The Find tab does **not** need to be visible to execute any search command discussed below.
        
        - The hide-find-tab commands hides the Find tab, but retains all the present settings.
        
        - The search-with-present-options command (Control-F) prompts for a search string.  Typing the <Return> key puts the search string in the Find tab and executes a search based on all the settings in the Find tab. This is a recommended default (Control-F) search command.
        
        - The show-search-options command shows the present search options in the status line.  At present, this command also makes the Find tab visible.
        
        Search again commands
        
        - The find-tab-find-next command (F3) is the same as the search-with-present-options command, except that it uses the search string in the find-tab.  Recommended as the default 'search again' command.
        
        - Similarly, the find-tab-find-previous command (F2) repeats the command specified by the Find tab,
          but in reverse.
        
        - The find-again is the same as the find-tab-find-next command if a search pattern is not '<find pattern here>'.
          Otherwise, the find-again is the same as the search-with-present-options command.
        
        Setting find options
        
        - Several minibuffer commands toggle the checkboxes and radio buttons in the Find tab, and thus affect the operation of the search-with-present-options command. Some may want to bind these commands to keys. Others, will prefer to toggle options in a mode.
        
        Here are the commands that toggle checkboxes: toggle-find-ignore-case-option, toggle-find-in-body-option, toggle-find-in-headline-option, toggle-find-mark-changes-option, toggle-find-mark-finds-option, toggle-find-regex-option, toggle-find-reverse-option, toggle-find-word-option, and toggle-find-wrap-around-option.
        
        Here are the commands that set radio buttons: set-find-everywhere, set-find-node-only, and set-find-suboutline-only.
        
        - The enter-find-options-mode (Ctrl-Shift-F) enters a mode in which you may change all checkboxes and radio buttons in the Find tab with plain keys.  As always, you can use the mode-help (Tab) command to see a list of key bindings in effect for the mode.
        
        Search commands that set options as a side effect
        
        The following commands set an option in the Find tab, then work exactly like the search-with-present-options command.
        
        - The search-backward and search-forward commands set the 'Whole Word' checkbox to False.
        
        - The word-search-backward and word-search-forward set the 'Whole Word' checkbox to True.
        
        - The re-search-forward and re-search-backward set the 'Regexp' checkbox to True.
        
        Find all commands
        
        - The find-all command prints all matches in the log pane.
        
        - The clone-find-all command replaces the previous 'Clone Find' checkbox.  It prints all matches in the log pane, and creates a node at the beginning of the outline containing clones of all nodes containing the 'find' string.  Only one clone is made of each node, regardless of how many clones the node has, or of how many matches are found in each node.
        
        Note: the radio buttons in the Find tab (Entire Outline, Suboutline Only and Node only) control how much of the outline is affected by the find-all and clone-find-all commands.
        
        Search and replace commands
        
        The replace-string prompts for a search string.  Type <Return> to end the search string.  The command will then prompt for the replacement string.  Typing a second <Return> key will place both strings in the Find tab and executes a **find** command, that is, the search-with-present-options command.
        
        So the only difference between the replace-string and search-with-present-options commands is that the replace-string command has the side effect of setting 'change' string in the Find tab.  However, this is an extremely useful side effect, because of the following commands...
        
        - The find-tab-change command (Ctrl-=) replaces the selected text with the 'change' text in the Find tab.
        
        - The find-tab-change-then-find (Ctrl--) replaces the selected text with the 'change' text in the Find tab, then executes the find command again.
        
        The find-tab-find-next, find-tab-change and find-tab-change-then-find commands can simulate any kind of query-replace command.  **Important**: Leo presently has separate query-replace and query-replace-regex commands, but they are buggy and 'under-powered'.  Fixing these commands has low priority.
        
        - The find-tab-change-all command changes all occurrences of the 'find' text with the 'change' text.  Important: the radio buttons in the Find tab (Entire Outline, Suboutline Only and Node only) control how much of the outline is affected by this command.
        
        Incremental search commands
        
        Leo's incremental search commands are completely separate from Leo's legacy search commands.  At present, incremental search commands do not cross node boundaries: they work only in the body text of single node.
        
        Coming in Leo 4.4b3: the incremental commands will maintain a list of previous matches.  This allows for
        
        a) support for backspace and
        b) an incremental-search-again command.
        
        Furthermore, this list makes it easy to detect the end of a wrapped incremental search.
        
        Here is the list of incremental find commands: isearch-backward, isearch-backward-regexp, isearch-forward and
        isearch-forward-regexp.'''
        #@-node:AGP.20250415230112.1072:<< define s >>
        #@nl
    
        # Remove indentation from s: a workaround of a Leo bug.
        s = g.adjustTripleString(s,c.tab_width)
    
        if not g.app.unitTesting:
            g.es_print(s)
    #@+node:AGP.20250415230112.1073:test_apropos_find_commands
    def test_apropos_find_commands (self):
    
        c.helpCommands.aproposFindCommands()
    #@-node:AGP.20250415230112.1073:test_apropos_find_commands
    #@-node:AGP.20250415230112.1071:aproposFindCommands
    #@+node:AGP.20250415230112.1074:pythonHelp
    def pythonHelp (self,event=None):
        
        '''Prompt for a arg for Python's help function, and put it to the log pane.'''
                
        c = self.c ; k = c.k ; tag = 'python-help' ; state = k.getState(tag)
    
        if state == 0:
            c.frame.minibufferWantsFocus()
            k.setLabelBlue('Python help: ',protect=True)
            k.getArg(event,tag,1,self.pythonHelp)
        else:
            k.clearState()
            k.resetLabel()
            s = k.arg.strip()
            if s:
                g.redirectStderr()
                g.redirectStdout()
                try: help(str(s))
                except Exception: pass
                g.restoreStderr()
                g.restoreStdout()
    #@-node:AGP.20250415230112.1074:pythonHelp
    #@-others
#@-node:AGP.20250415230112.1062:helpCommandsClass
#@+node:AGP.20250415230112.1075:keyHandlerCommandsClass (add docstrings)
class keyHandlerCommandsClass (baseEditCommandsClass):
    
    '''User commands to access the keyHandler class.'''
    
    #@    @+others
    #@+node:AGP.20250415230112.1076: ctor
    def __init__ (self,c):
    
        baseEditCommandsClass.__init__(self,c) # init the base class.
    #@-node:AGP.20250415230112.1076: ctor
    #@+node:AGP.20250415230112.1077:getPublicCommands (keyHandler)
    def getPublicCommands (self):
        
        k = self.k
        
        return {
            'auto-complete':            k.autoCompleter.autoComplete,
            'auto-complete-force':      k.autoCompleter.autoCompleteForce,
            'digit-argument':           k.digitArgument,
            'disable-autocompleter':    k.autoCompleter.disableAutocompleter,
            'disable-calltips':         k.autoCompleter.disableCalltips,
            'enable-autocompleter':     k.autoCompleter.enableAutocompleter,
            'enable-calltips':          k.autoCompleter.enableCalltips,
            'exit-named-mode':          k.exitNamedMode,
            'full-command':             k.fullCommand, # For menu.
            'hide-mini-buffer':         k.hideMinibuffer,
            'mode-help':                k.modeHelp,
            'negative-argument':        k.negativeArgument,
            'number-command':           k.numberCommand,
            'number-command-0':         k.numberCommand0,
            'number-command-1':         k.numberCommand1,
            'number-command-2':         k.numberCommand2,
            'number-command-3':         k.numberCommand3,
            'number-command-4':         k.numberCommand4,
            'number-command-5':         k.numberCommand5,
            'number-command-6':         k.numberCommand6,
            'number-command-7':         k.numberCommand7,
            'number-command-8':         k.numberCommand8,
            'number-command-9':         k.numberCommand9,
            'print-bindings':           k.printBindings,
            'print-commands':           k.printCommands,
            'repeat-complex-command':   k.repeatComplexCommand,
            # 'scan-for-autocompleter':   k.autoCompleter.scan,
            'set-command-state':        k.setCommandState,
            'set-insert-state':         k.setInsertState,
            'set-overwrite-state':      k.setOverwriteState,
            'show-calltips':            k.autoCompleter.showCalltips,
            'show-calltips-force':      k.autoCompleter.showCalltipsForce,
            'show-mini-buffer':         k.showMinibuffer,
            'toggle-autocompleter':     k.autoCompleter.toggleAutocompleter,
            'toggle-calltips':          k.autoCompleter.toggleCalltips,
            'toggle-mini-buffer':       k.toggleMinibuffer,
            'toggle-input-state':       k.toggleInputState,
            'universal-argument':       k.universalArgument,
        }
    #@-node:AGP.20250415230112.1077:getPublicCommands (keyHandler)
    #@-others
#@-node:AGP.20250415230112.1075:keyHandlerCommandsClass (add docstrings)
#@+node:AGP.20250415230112.1078:killBufferCommandsClass (add docstrings)
class killBufferCommandsClass (baseEditCommandsClass):
    
    '''A class to manage the kill buffer.'''

    #@    @+others
    #@+node:AGP.20250415230112.1079: ctor & finishCreate
    def __init__ (self,c):
    
        baseEditCommandsClass.__init__(self,c) # init the base class.
    
        self.killBuffer = [] # May be changed in finishCreate.
        self.kbiterator = self.iterateKillBuffer()
        self.last_clipboard = None # For interacting with system clipboard.
        self.reset = False
    
    def finishCreate (self):
        
        baseEditCommandsClass.finishCreate(self)
            # Call the base finishCreate.
            # This sets self.k
        
        if self.k.useGlobalKillbuffer:
            self.killBuffer = leoKeys.keyHandlerClass.global_killbuffer
    #@-node:AGP.20250415230112.1079: ctor & finishCreate
    #@+node:AGP.20250415230112.1080: getPublicCommands
    def getPublicCommands (self):
        
        return {
            'backward-kill-sentence':   self.backwardKillSentence,
            'backward-kill-word':       self.backwardKillWord,
            'clear-kill-ring':          self.clearKillRing,
            'kill-line':                self.killLine,
            'kill-word':                self.killWord,
            'kill-sentence':            self.killSentence,
            'kill-region':              self.killRegion,
            'kill-region-save':         self.killRegionSave,
            'yank':                     self.yank,
            'yank-pop':                 self.yankPop,
            'zap-to-character':         self.zapToCharacter,
        }
    #@-node:AGP.20250415230112.1080: getPublicCommands
    #@+node:AGP.20250415230112.1081:addToKillBuffer
    def addToKillBuffer (self,text):
        
        killKeys =(
            '<Control-k>', '<Control-w>',
            '<Alt-d>', '<Alt-Delete', '<Alt-z>', '<Delete>',
            '<Control-Alt-w>')
    
        k = self.k
        self.reset = True
    
        # g.trace(repr(text))
    
        if self.killBuffer and k.stroke in killKeys:
            self.killBuffer [0] = self.killBuffer [0] + text
        else:
            self.killBuffer.insert(0,text)
    #@-node:AGP.20250415230112.1081:addToKillBuffer
    #@+node:AGP.20250415230112.1082:backwardKillSentence
    def backwardKillSentence (self,event):
        
        '''Kill the previous sentence.'''
        
        w = self.editWidget(event)
        if not w: return
    
        i = w.search('.','insert',backwards=True,stopindex='1.0')
    
        if i:
            i2 = w.search('.',i,backwards=True,stopindex='1.0')
            i2 = g.choose(i2=='','1.0',i2+'+1c ')
            self.kill(event,i2,'%s + 1c' % i,undoType='backward-kill-sentence')
    #@-node:AGP.20250415230112.1082:backwardKillSentence
    #@+node:AGP.20250415230112.1083:backwardKillWord & killWord
    def backwardKillWord (self,event):
        '''Kill the previous word.'''
        c = self.c
        self.beginCommand(undoType='backward-kill-word')
        c.editCommands.backwardWord(event)
        self.killWs(event)
        self.kill(event,'insert wordstart','insert wordend',undoType=None)
        c.frame.body.forceFullRecolor()
        self.endCommand(changed=True,setLabel=True)
    
    def killWord (self,event):
        '''Kill the word containing the cursor.'''
        c = self.c
        self.beginCommand(undoType='kill-word')
        self.kill(event,'insert wordstart','insert wordend',undoType=None)
        self.killWs(event)
        c.frame.body.forceFullRecolor()
        self.endCommand(changed=True,setLabel=True)
    
    #@-node:AGP.20250415230112.1083:backwardKillWord & killWord
    #@+node:AGP.20250415230112.1084:clearKillRing
    def clearKillRing (self,event=None):
        
        '''Clear the kill ring.'''
        
        self.killBuffer = []
    #@-node:AGP.20250415230112.1084:clearKillRing
    #@+node:AGP.20250415230112.1085:getClipboard
    def getClipboard (self,w):
    
        try:
            ctxt = w.selection_get(selection='CLIPBOARD')
            if not self.killBuffer or ctxt != self.last_clipboard:
                self.last_clipboard = ctxt
                if not self.killBuffer or self.killBuffer [0] != ctxt:
                    return ctxt
        except: pass
    
        return None
    #@-node:AGP.20250415230112.1085:getClipboard
    #@+node:AGP.20250415230112.1086:iterateKillBuffer
    def iterateKillBuffer (self):
    
        while 1:
            if self.killBuffer:
                self.last_clipboard = None
                for z in self.killBuffer:
                    if self.reset:
                        self.reset = False
                        break
                    yield z
    #@-node:AGP.20250415230112.1086:iterateKillBuffer
    #@+node:AGP.20250415230112.1087:kill, killLine
    def kill (self,event,frm,to,undoType=None):
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        s = w.get(frm,to)
        if undoType: self.beginCommand(undoType=undoType)
        self.addToKillBuffer(s)
        w.clipboard_clear()
        w.clipboard_append(s)
        w.delete(frm,to)
        if undoType:
            self.c.frame.body.forceFullRecolor()
            self.endCommand(changed=True,setLabel=True)
    
    def killLine (self,event):
        '''Kill the line containing the cursor.'''
        self.kill(event,'insert linestart','insert lineend+1c',undoType='kill-line')
    #@nonl
    #@-node:AGP.20250415230112.1087:kill, killLine
    #@+node:AGP.20250415230112.1088:killRegion & killRegionSave & helper
    def killRegion (self,event):
        '''Kill the text selection.'''
        self.killRegionHelper(event,deleteFlag=True)
        
    def killRegionSave (self,event):
        '''Add the selected text to the kill ring, but do not delete it.'''
        self.killRegionHelper(event,deleteFlag=False)
    
    def killRegionHelper (self,event,deleteFlag):
    
        w = self.editWidget(event)
        if not w: return
        theRange = w.tag_ranges('sel')
        if not theRange: return
        
        s = w.get(theRange[0],theRange[-1])
        if deleteFlag:
            self.beginCommand(undoType='kill-region')
            w.delete(theRange[0],theRange[-1])
            self.c.frame.body.forceFullRecolor()
            self.endCommand(changed=True,setLabel=True)
        self.addToKillBuffer(s)
        w.clipboard_clear()
        w.clipboard_append(s)
        # self.removeRKeys(w)
    #@-node:AGP.20250415230112.1088:killRegion & killRegionSave & helper
    #@+node:AGP.20250415230112.1089:killSentence
    def killSentence (self,event):
        
        '''Kill the sentence containing the cursor.'''
    
        w = self.editWidget(event)
        if not w: return
    
        i  = w.search('.','insert',stopindex='end')
        if i:
            self.beginCommand(undoType='kill-sentence')
            i2 = w.search('.','insert',backwards=True,stopindex='1.0')
            i2 = g.choose(i2=='','1.0',i2+'+1c ')
            self.kill(event,i2,'%s + 1c' % i,undoType='kill-sentence')
            self.c.frame.body.forceFullRecolor()
            self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1089:killSentence
    #@+node:AGP.20250415230112.1090:killWs
    def killWs (self,event,undoType=None):
        
        ws = ''
        w = self.editWidget(event)
        if not w: return
    
        while 1:
            s = w.get('insert')
            if s in (' ','\t'):
                w.delete('insert')
                ws = ws + s
            else:
                break
       
        if ws:
            if undoType: self.beginCommand(undoType=undoType)
            self.addToKillBuffer(ws)
            if undoType: self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1090:killWs
    #@+node:AGP.20250415230112.1091:yank
    def yank (self,event):
        
        '''Insert the next entry in the kill ring at the insert point.'''
    
        c = self.c ; k = self.k
        w = self.editWidget(event)
        if not w: return
    
        i = w.index('insert')
        clip_text = self.getClipboard(w)
    
        if self.killBuffer or clip_text:
            self.beginCommand(undoType='yank')
            self.reset = True
            s = clip_text or self.kbiterator.next()
            w.tag_delete('kb')
            w.insert('insert',s,('kb'))
            w.mark_set('insert',i)
            c.frame.body.forceFullRecolor()
            self.endCommand(changed=True,setLabel=True)
    #@-node:AGP.20250415230112.1091:yank
    #@+node:AGP.20250415230112.1092:yankPop
    def yankPop (self,event):
        
        '''Replaces the just-yanked kill buffer with the contents of the previous kill buffer.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        i = w.index('insert') ; t, t1 = i.split('.')
        clip_text = self.getClipboard(w)
    
        if self.killBuffer or clip_text:
            if clip_text: s = clip_text
            else:         s = self.kbiterator.next()
            t1 = str(int(t1)+len(s))
            r = w.tag_ranges('kb')
            if r and r [0] == i:
                w.delete(r[0],r[-1])
            w.tag_delete('kb')
            w.insert('insert',s,('kb'))
            w.mark_set('insert',i)
    #@-node:AGP.20250415230112.1092:yankPop
    #@+node:AGP.20250415230112.1093:zapToCharacter
    def zapToCharacter (self,event):
        
        '''Kill characters from the insertion point to a given character.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
        
        state = k.getState('zap-to-char')
        if state == 0:
            k.setLabelBlue('Zap To Character: ',protect=True)
            k.setState('zap-to-char',1,handler=self.zapToCharacter)
        else:
            c = k.c
            ch = event and event.char
            k.resetLabel()
            k.clearState()
            if len(event.char) != 0 and not ch.isspace():
                i = w.search(ch,'insert',stopindex='end')
                if i != -1:
                    s = w.get('insert','%s' % i)
                    self.addToKillBuffer(s)
                    w.delete('insert','%s' % i)
    #@-node:AGP.20250415230112.1093:zapToCharacter
    #@-others
#@-node:AGP.20250415230112.1078:killBufferCommandsClass (add docstrings)
#@+node:AGP.20250415230112.1094:leoCommandsClass (add docstrings)
class leoCommandsClass (baseEditCommandsClass):
    
    #@    @+others
    #@+node:AGP.20250415230112.1095: ctor
    def __init__ (self,c):
    
        baseEditCommandsClass.__init__(self,c) # init the base class.
    #@-node:AGP.20250415230112.1095: ctor
    #@+node:AGP.20250415230112.1096:leoCommands.getPublicCommands
    def getPublicCommands (self):
        
        '''(leoCommands) Return a dict of the 'legacy' Leo commands.'''
        
        k = self.k ; d2 = {}
        
        #@    << define dictionary d of names and Leo commands >>
        #@+node:AGP.20250415230112.1097:<< define dictionary d of names and Leo commands >>
        c = self.c ; f = c.frame
        
        d = {
            'abort-edit-headline':          f.abortEditLabelCommand,
            'about-leo':                    c.about,
            'add-comments':                 c.addComments,     
            'beautify-all':                 c.beautifyAllPythonCode,
            'beautify':                     c.beautifyPythonCode,
            'cascade-windows':              f.cascade,
            'clear-recent-files':           c.clearRecentFiles,
            'close-window':                 c.close,
            'contract-or-go-left':          c.contractNodeOrGoToParent,
            'check-python-code':            c.checkPythonCode,
            'check-all-python-code':        c.checkAllPythonCode,
            'check-outline':                c.checkOutline,
            'clear-recent-files':           c.clearRecentFiles,
            'clone-node':                   c.clone,
            'contract-node':                c.contractNode,
            'contract-all':                 c.contractAllHeadlines,
            'contract-parent':              c.contractParent,
            'convert-all-blanks':           c.convertAllBlanks,
            'convert-all-tabs':             c.convertAllTabs,
            'convert-blanks':               c.convertBlanks,
            'convert-tabs':                 c.convertTabs,
            'copy-node':                    c.copyOutline,
            'copy-text':                    f.copyText,
            'cut-node':                     c.cutOutline,
            'cut-text':                     f.cutText,
            'de-hoist':                     c.dehoist,
            'delete-comments':              c.deleteComments,
            'delete-node':                  c.deleteOutline,
            'demote':                       c.demote,
            'dump-outline':                 c.dumpOutline,
            'edit-headline':                c.editHeadline,
            'end-edit-headline':            f.endEditLabelCommand,
            'equal-sized-panes':            f.equalSizedPanes,
            'execute-script':               c.executeScript,
            'exit-leo':                     g.app.onQuit,
            'expand-all':                   c.expandAllHeadlines,
            'expand-next-level':            c.expandNextLevel,
            'expand-node':                  c.expandNode,
            'expand-and-go-right':          c.expandNodeAndGoToFirstChild,
            'expand-ancestors-only':        c.expandOnlyAncestorsOfNode,
            'expand-or-go-right':           c.expandNodeOrGoToFirstChild,
            'expand-prev-level':            c.expandPrevLevel,
            'expand-to-level-1':            c.expandLevel1,
            'expand-to-level-2':            c.expandLevel2,
            'expand-to-level-3':            c.expandLevel3,
            'expand-to-level-4':            c.expandLevel4,
            'expand-to-level-5':            c.expandLevel5,
            'expand-to-level-6':            c.expandLevel6,
            'expand-to-level-7':            c.expandLevel7,
            'expand-to-level-8':            c.expandLevel8,
            'expand-to-level-9':            c.expandLevel9,
            'export-headlines':             c.exportHeadlines,
            'extract':                      c.extract,
            'extract-names':                c.extractSectionNames,
            'extract-section':              c.extractSection,
            'flatten-outline':              c.flattenOutline,
            'go-back':                      c.goPrevVisitedNode,
            'go-forward':                   c.goNextVisitedNode,
            'goto-first-node':              c.goToFirstNode,
            'goto-first-sibling':           c.goToFirstSibling,
            'goto-last-node':               c.goToLastNode,
            'goto-last-sibling':            c.goToLastSibling,
            'goto-last-visible':            c.goToLastVisibleNode,
            'goto-line-number':             c.goToLineNumber,
            'goto-next-changed':            c.goToNextDirtyHeadline,
            'goto-next-clone':              c.goToNextClone,
            'goto-next-marked':             c.goToNextMarkedHeadline,
            'goto-next-node':               c.selectThreadNext,
            'goto-next-sibling':            c.goToNextSibling,
            'goto-next-visible':            c.selectVisNext,
            'goto-parent':                  c.goToParent,
            'goto-prev-node':               c.selectThreadBack,
            'goto-prev-sibling':            c.goToPrevSibling,
            'goto-prev-visible':            c.selectVisBack,
            'hide-invisibles':              c.hideInvisibles,
            'hoist':                        c.hoist,
            'import-at-file':               c.importAtFile,
            'import-at-root':               c.importAtRoot,
            'import-cweb-files':            c.importCWEBFiles,
            'import-derived-file':          c.importDerivedFile,
            'import-flattened-outline':     c.importFlattenedOutline,
            'import-noweb-files':           c.importNowebFiles,
            'indent-region':                c.indentBody,
            'insert-node':                  c.insertHeadline,
            'insert-body-time':             c.insertBodyTime,
            'insert-headline-time':         f.insertHeadlineTime,
            'mark':                         c.markHeadline,
            'mark-changed-items':           c.markChangedHeadlines,
            'mark-changed-roots':           c.markChangedRoots,
            'mark-clones':                  c.markClones,
            'mark-subheads':                c.markSubheads,
            'match-brackets':               c.findMatchingBracket,
            'minimize-all':                 f.minimizeAll,
            'move-outline-down':            c.moveOutlineDown,
            'move-outline-left':            c.moveOutlineLeft,
            'move-outline-right':           c.moveOutlineRight,
            'move-outline-up':              c.moveOutlineUp,
            'new':                          c.new,
            #'open-compare-window':          c.openCompareWindow,
            'open-find-dialog':             c.showFindPanel, # Deprecated.
            'open-leoDocs-leo':             c.leoDocumentation,
            'open-leoPlugins-leo':          c.openLeoPlugins,
            'open-leoSettings-leo':         c.openLeoSettings,
            'open-scripts-leo':             c.openLeoScripts,
            'open-myLeoSettings-leo':       c.openMyLeoSettings,
            'open-online-home':             c.leoHome,
            'open-online-tutorial':         c.leoTutorial,
            'open-offline-tutorial':        f.leoHelp,
            'open-outline':                 c.open,
            'open-python-window':           c.openPythonWindow,
            'open-users-guide':             c.leoUsersGuide,
            #'open-with':                    c.openWith,
            'outline-to-cweb':              c.outlineToCWEB,
            'outline-to-noweb':             c.outlineToNoweb,
            'paste-node':                   c.pasteOutline,
            'paste-retaining-clones':       c.pasteOutlineRetainingClones,
            'paste-text':                   f.pasteText,
            'pretty-print-all-python-code': c.prettyPrintAllPythonCode,
            'pretty-print-python-code':     c.prettyPrintPythonCode,
            'promote':                      c.promote,
            'read-at-file-nodes':           c.readAtFileNodes,
            'read-outline-only':            c.readOutlineOnly,
            'redo':                         c.undoer.redo,
            'reformat-paragraph':           c.reformatParagraph,
            'remove-sentinels':             c.removeSentinels,
            'resize-to-screen':             f.resizeToScreen,
            'revert':                       c.revert,
            'save-file':                    c.save,
            'save-file-as':                 c.saveAs,
            'save-file-to':                 c.saveTo,
            'select-all':                   f.body.selectAllText,
            'settings':                     c.preferences,
            'set-colors':                   c.colorPanel,
            'set-font':                     c.fontPanel,
            'set-leo-id':                   g.app.askLeoID,
            'show-invisibles':              c.showInvisibles,
            'sort-children':                c.sortChildren,
            'sort-siblings':                c.sortSiblings,
            'tangle':                       c.tangle,
            'tangle-all':                   c.tangleAll,
            'tangle-marked':                c.tangleMarked,
            'toggle-active-pane':           f.toggleActivePane,
            'toggle-angle-brackets':        c.toggleAngleBrackets,
            'toggle-invisibles':            c.toggleShowInvisibles,
            'toggle-split-direction':       f.toggleSplitDirection,
            'undo':                         c.undoer.undo,
            'unindent-region':              c.dedentBody,
            'unmark-all':                   c.unmarkAll,
            'untangle':                     c.untangle,
            'untangle-all':                 c.untangleAll,
            'untangle-marked':              c.untangleMarked,
            'weave':                        c.weave,
            'write-at-file-nodes':          c.fileCommands.writeAtFileNodes,
            'write-dirty-at-file-nodes':    c.fileCommands.writeDirtyAtFileNodes,
            'write-missing-at-file-nodes':  c.fileCommands.writeMissingAtFileNodes,
            'write-outline-only':           c.fileCommands.writeOutlineOnly,
        }
        #@-node:AGP.20250415230112.1097:<< define dictionary d of names and Leo commands >>
        #@nl
        
        # Create a callback for each item in d.
        keys = d.keys() ; keys.sort()
        for name in keys:
            f = d.get(name)
            d2 [name] = f
            k.inverseCommandsDict [f.__name__] = name
            # g.trace('leoCommands %24s = %s' % (f.__name__,name))
            
        return d2
    #@-node:AGP.20250415230112.1096:leoCommands.getPublicCommands
    #@-others
#@-node:AGP.20250415230112.1094:leoCommandsClass (add docstrings)
#@+node:AGP.20250415230112.1098:macroCommandsClass
class macroCommandsClass (baseEditCommandsClass):

    #@    @+others
    #@+node:AGP.20250415230112.1099: ctor
    def __init__ (self,c):
    
        baseEditCommandsClass.__init__(self,c) # init the base class.
    
        self.lastMacro = None
        self.macs = []
        self.macro = []
        self.namedMacros = {}
        
        # Important: we must not interfere with k.state in startKbdMacro!
        self.recordingMacro = False
    #@-node:AGP.20250415230112.1099: ctor
    #@+node:AGP.20250415230112.1100: getPublicCommands
    def getPublicCommands (self):
    
        return {
            'call-last-keyboard-macro': self.callLastKeyboardMacro,
            'end-kbd-macro':            self.endKbdMacro,
            'name-last-kbd-macro':      self.nameLastKbdMacro,
            'load-file':                self.loadFile,
            'insert-keyboard-macro' :   self.insertKeyboardMacro,
            'start-kbd-macro':          self.startKbdMacro,
        }
    #@-node:AGP.20250415230112.1100: getPublicCommands
    #@+node:AGP.20250415230112.1101:Entry points
    #@+node:AGP.20250415230112.1102:insertKeyboardMacro
    def insertKeyboardMacro (self,event):
    
        '''Save all macros to a file.'''
    
        k = self.k ; state = k.getState('macro-name')
        prompt = 'Macro name: '
    
        if state == 0:
            k.setLabelBlue(prompt,protect=True)
            k.getArg(event,'macro-name',1,self.insertKeyboardMacro)
        else:
            ch = event.keysym ; s = s = k.getLabel(ignorePrompt=True)
            g.trace(repr(ch),repr(s))
            if ch == 'Return':
                k.clearState()
                self.saveMacros(event,s)
            elif ch == 'Tab':
                k.setLabel('%s%s' % (
                    prompt,self.findFirstMatchFromList(s,self.namedMacros)),
                    prompt=prompt,protect=True)
            else:
                k.updateLabel(event)
    #@+node:AGP.20250415230112.1103:findFirstMatchFromList
    def findFirstMatchFromList (self,s,aList=None):
    
        '''This method finds the first match it can find in a sorted list'''
    
        k = self.k ; c = k.c
    
        if aList is not None:
            aList = c.commandsDict.keys()
    
        pmatches = [item for item in aList if item.startswith(s)]
        pmatches.sort()
        if pmatches:
            mstring = reduce(g.longestCommonPrefix,pmatches)
            return mstring
    
        return s
    #@-node:AGP.20250415230112.1103:findFirstMatchFromList
    #@-node:AGP.20250415230112.1102:insertKeyboardMacro
    #@+node:AGP.20250415230112.1104:loadFile & helpers
    def loadFile (self,event):
    
        '''Asks for a macro file name to load.'''
    
        f = tkFileDialog and tkFileDialog.askopenfile()
        if f:
            self._loadMacros(f)
    #@+node:AGP.20250415230112.1105:_loadMacros
    def _loadMacros (self,f):
    
        '''Loads a macro file into the macros dictionary.'''
    
        k = self.k
        macros = cPickle.load(f)
        for z in macros:
            k.addToDoAltX(z,macros[z])
    #@-node:AGP.20250415230112.1105:_loadMacros
    #@-node:AGP.20250415230112.1104:loadFile & helpers
    #@+node:AGP.20250415230112.1106:nameLastKbdMacro
    def nameLastKbdMacro (self,event):
    
        '''Prompt for the name to be given to the last recorded macro.'''
    
        k = self.k ; state = k.getState('name-macro')
        
        if state == 0:
            k.setLabelBlue('Name of macro: ',protect=True)
            k.getArg(event,'name-macro',1,self.nameLastKbdMacro)
        else:
            k.clearState()
            name = k.arg
            k.addToDoAltX(name,self.lastMacro)
            k.setLabelGrey('Macro defined: %s' % name)
    #@-node:AGP.20250415230112.1106:nameLastKbdMacro
    #@+node:AGP.20250415230112.1107:saveMacros & helper
    def saveMacros (self,event,macname):
    
        '''Asks for a file name and saves it.'''
    
        name = tkFileDialog and tkFileDialog.asksaveasfilename()
        if name:
            f = file(name,'a+')
            f.seek(0)
            if f:
                self._saveMacros(f,macname)
    #@+node:AGP.20250415230112.1108:_saveMacros
    def _saveMacros( self, f , name ):
        '''Saves the macros as a pickled dictionary'''
        import cPickle
        fname = f.name
        try:
            macs = cPickle.load( f )
        except:
            macs = {}
        f.close()
        if self.namedMacros.has_key( name ):
            macs[ name ] = self.namedMacros[ name ]
            f = file( fname, 'w' )
            cPickle.dump( macs, f )
            f.close()
    #@-node:AGP.20250415230112.1108:_saveMacros
    #@-node:AGP.20250415230112.1107:saveMacros & helper
    #@+node:AGP.20250415230112.1109:startKbdMacro
    def startKbdMacro (self,event):
        
        '''Start recording a keyboard macro.'''
    
        k = self.k
        
        if not self.recordingMacro:
            self.recordingMacro = True
            k.setLabelBlue('Recording keyboard macro...',protect=True)
        else:
            stroke = k.stroke ; keysym = event.keysym
            if stroke == '<Key>' and keysym in ('Control_L','Alt_L','Shift_L'):
                return False
            g.trace('stroke',stroke,'keysym',keysym)
            if stroke == '<Key>' and keysym =='parenright':
                self.endKbdMacro(event)
                return True
            elif stroke == '<Key>':
                self.macro.append((event.keycode,event.keysym))
                return True
            else:
                self.macro.append((stroke,event.keycode,event.keysym,event.char))
                return True
    #@-node:AGP.20250415230112.1109:startKbdMacro
    #@+node:AGP.20250415230112.1110:endKbdMacro
    def endKbdMacro (self,event):
        
        '''Stop recording a keyboard macro.'''
    
        k = self.k ; self.recordingMacro = False
    
        if self.macro:
            self.macro = self.macro [: -4]
            self.macs.insert(0,self.macro)
            self.lastMacro = self.macro[:]
            self.macro = []
            k.setLabelGrey('Keyboard macro defined, not named')
        else:
            k.setLabelGrey('Empty keyboard macro')
    #@-node:AGP.20250415230112.1110:endKbdMacro
    #@+node:AGP.20250415230112.1111:callLastKeyboardMacro & helper (called from universal command)
    def callLastKeyboardMacro (self,event):
        
        '''Call the last recorded keyboard macro.'''
        
        w = event and event.widget
        # This does **not** require a text widget.
    
        if self.lastMacro:
            self._executeMacro(self.lastMacro,w)
    #@+node:AGP.20250415230112.1112:_executeMacro (revise)
    def _executeMacro (self,macro,w):
    
        k = self.k
    
        for z in macro:
            if len(z) == 2:
                w.event_generate('<Key>',keycode=z[0],keysym=z[1])
            else:
                meth = g.stripBrackets(z [0])
                bunchList = k.bindingsDict.get(meth,[])  ### Probably should not strip < and >
                if bunchList:
                    b = bunchList[0]
                    ev = Tk.Event()
                    ev.widget = w
                    ev.keycode = z [1]
                    ev.keysym = z [2]
                    ev.char = z [3]
                    k.masterCommand(ev,b.f,'<%s>' % meth)
    #@-node:AGP.20250415230112.1112:_executeMacro (revise)
    #@-node:AGP.20250415230112.1111:callLastKeyboardMacro & helper (called from universal command)
    #@-node:AGP.20250415230112.1101:Entry points
    #@+node:AGP.20250415230112.1113:Common Helpers
    #@+node:AGP.20250415230112.1114:addToDoAltX
    # Called from loadFile and nameLastKbdMacro.
    
    def addToDoAltX (self,name,macro):
    
        '''Adds macro to Alt-X commands.'''
        
        k= self ; c = k.c
    
        if c.commandsDict.has_key(name):
            return False
    
        def func (event,macro=macro):
            w = event and event.widget
            # This does **not** require a text widget.
            return self._executeMacro(macro,w)
    
        c.commandsDict [name] = func
        self.namedMacros [name] = macro
        return True
    #@-node:AGP.20250415230112.1114:addToDoAltX
    #@-node:AGP.20250415230112.1113:Common Helpers
    #@-others
#@-node:AGP.20250415230112.1098:macroCommandsClass
#@+node:AGP.20250415230112.1115:queryReplaceCommandsClass (limited to single node)
class queryReplaceCommandsClass (baseEditCommandsClass):
    
    '''A class to handle query replace commands.'''

    #@    @+others
    #@+node:AGP.20250415230112.1116: ctor & init
    def __init__ (self,c):
        
        baseEditCommandsClass.__init__(self,c) # init the base class.
        self.regexp = False # True: do query-replace-regexp.  Set in stateHandler.
        
    def init (self):
        
        self.qQ = None
        self.qR = None
        self.replaced = 0 # The number of replacements.
    #@-node:AGP.20250415230112.1116: ctor & init
    #@+node:AGP.20250415230112.1117: getPublicCommands
    def getPublicCommands (self):
    
        return {
            'query-replace':        self.queryReplace,
            'query-replace-regex':  self.queryReplaceRegex,
        }
    #@-node:AGP.20250415230112.1117: getPublicCommands
    #@+node:AGP.20250415230112.1118:Entry points
    def queryReplace (self,event):
    
        '''Interactively find and replace text.
        This is not recommended: Leo's other find and change commands are more capable.'''
        self.regexp = False
        self.stateHandler(event)
    
    def queryReplaceRegex (self,event):
        '''Interactively find and replace text using regular expressions.
        This is not recommended: Leo's other find and change commands are more capable.'''
        self.regexp = True
        self.stateHandler(event)
    #@-node:AGP.20250415230112.1118:Entry points
    #@+node:AGP.20250415230112.1119:Helpers
    #@+node:AGP.20250415230112.1120:doOneReplace
    def doOneReplace (self,event):
    
        w = self.editWidget(event)
        if not w: return
        
        i = w.tag_ranges('qR')
        w.delete(i[0],i[1])
        w.insert('insert',self.qR)
        self.replaced += 1
    #@-node:AGP.20250415230112.1120:doOneReplace
    #@+node:AGP.20250415230112.1121:findNextMatch
    def findNextMatch (self,event):
        
        '''Find the next match and select it.
        Return True if a match was found.
        Otherwise, call quitSearch and return False.'''
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
        
        w.tag_delete('qR')
        if self.regexp:
            #@        << handle regexp >>
            #@+node:AGP.20250415230112.1122:<< handle regexp >>
            try:
                regex = re.compile(self.qQ)
            except:
                self.quitSearch(event,'Illegal regular expression')
                return False
            
            txt = w.get('insert','end')
            match = regex.search(txt)
            
            if match:
                start = match.start()
                end = match.end()
                length = end - start
                w.mark_set('insert','insert +%sc' % start)
                ### w.update_idletasks()
                w.tag_add('qR','insert','insert +%sc' % length)
                w.tag_config('qR',background='lightblue')
                txt = w.get('insert','insert +%sc' % length)
                return True
            else:
                self.quitSearch(event)
                return False
            #@-node:AGP.20250415230112.1122:<< handle regexp >>
            #@nl
        else:
            #@        << handle plain search >>
            #@+node:AGP.20250415230112.1123:<< handle plain search >>
            i = w.search(self.qQ,'insert',stopindex='end')
            if i:
                w.mark_set('insert',i)
                ###w.update_idletasks()
                w.tag_add('qR','insert','insert +%sc' % len(self.qQ))
                w.tag_config('qR',background='lightblue')
                return True
            else:
                self.quitSearch(event)
                return False
            #@-node:AGP.20250415230112.1123:<< handle plain search >>
            #@nl
    #@-node:AGP.20250415230112.1121:findNextMatch
    #@+node:AGP.20250415230112.1124:getUserResponse
    def getUserResponse (self,event):
        
        w = self.editWidget(event)
        if not w or not hasattr(event,'keysym'): return
        
        # g.trace(event.keysym)
        if event.keysym == 'y':
            self.doOneReplace(event)
            if not self.findNextMatch(event):
                self.quitSearch(event)
        elif event.keysym in ('q','Return'):
            self.quitSearch(event)
        elif event.keysym == 'exclam':
            while self.findNextMatch(event):
                self.doOneReplace(event)
        elif event.keysym in ('n','Delete'):
            # Skip over the present match.
            w.mark_set('insert','insert +%sc' % len(self.qQ))
            if not self.findNextMatch(event):
                self.quitSearch(event)
    
        w.see('insert')
    #@-node:AGP.20250415230112.1124:getUserResponse
    #@+node:AGP.20250415230112.1125:quitSearch
    def quitSearch (self,event,message=None):
    
        k = self.k
        w = self.editWidget(event)
        if not w: return
    
        w.tag_delete('qR')
        k.clearState()
        if message is None:
            message = 'Replaced %d occurences' % self.replaced
        k.setLabelGrey(message)
    #@-node:AGP.20250415230112.1125:quitSearch
    #@+node:AGP.20250415230112.1126:stateHandler
    def stateHandler (self,event):
        
        k = self.k ; state = k.getState('query-replace')
        
        prompt = g.choose(self.regexp,'Query replace regexp','Query replace')
        
        if state == 0: # Get the first arg.
            self.init()
            k.setLabelBlue(prompt + ': ',protect=True)
            k.getArg(event,'query-replace',1,self.stateHandler)
        elif state == 1: # Get the second arg.
            self.qQ = k.arg
            if len(k.arg) > 0:
                prompt = '%s %s with: ' % (prompt,k.arg)
                k.setLabelBlue(prompt)
                k.getArg(event,'query-replace',2,self.stateHandler)
            else:
                k.resetLabel()
                k.clearState()
        elif state == 2: # Set the prompt and find the first match.
            self.qR = k.arg # Null replacement arg is ok.
            k.setLabelBlue('Query replacing %s with %s\n' % (self.qQ,self.qR) +
                'y: replace, (n or Delete): skip, !: replace all, (q or Return): quit',
                protect=True)
            k.setState('query-replace',3,self.stateHandler)
            self.findNextMatch(event)
        elif state == 3:
            self.getUserResponse(event)
    #@-node:AGP.20250415230112.1126:stateHandler
    #@-node:AGP.20250415230112.1119:Helpers
    #@-others
#@-node:AGP.20250415230112.1115:queryReplaceCommandsClass (limited to single node)
#@+node:AGP.20250415230112.1127:rectangleCommandsClass
class rectangleCommandsClass (baseEditCommandsClass):

    #@    @+others
    #@+node:AGP.20250415230112.1128: ctor & finishCreate
    def __init__ (self,c):
    
        baseEditCommandsClass.__init__(self,c) # init the base class.
        
        self.theKillRectangle = [] # Do not re-init this!
        self.stringRect = None
        
    def finishCreate(self):
        
        baseEditCommandsClass.finishCreate(self)
        
        self.commandsDict = {
            'c': ('clear-rectangle',    self.clearRectangle),
            'd': ('delete-rectangle',   self.deleteRectangle),
            'k': ('kill-rectangle',     self.killRectangle),
            'o': ('open-rectangle',     self.openRectangle),
            'r': ('copy-rectangle-to-register',
                self.c.registerCommands.copyRectangleToRegister),
            't': ('string-rectangle',   self.stringRectangle),
            'y': ('yank-rectangle',     self.yankRectangle),
        }
    #@-node:AGP.20250415230112.1128: ctor & finishCreate
    #@+node:AGP.20250415230112.1129:check
    def check (self,event,warning='No rectangle selected'):
        
        '''Return True if there is a selection.
        Otherwise, return False and issue a warning.'''
    
        return self._chckSel(event,warning)
    #@-node:AGP.20250415230112.1129:check
    #@+node:AGP.20250415230112.1130:getPublicCommands
    def getPublicCommands (self):
    
        return {
            'clear-rectangle':  self.clearRectangle,
            'close-rectangle':  self.closeRectangle,
            'delete-rectangle': self.deleteRectangle,
            'kill-rectangle':   self.killRectangle,
            'open-rectangle':   self.openRectangle,
            'string-rectangle': self.stringRectangle,
            'yank-rectangle':   self.yankRectangle,
        }
    #@-node:AGP.20250415230112.1130:getPublicCommands
    #@+node:AGP.20250415230112.1131:beginCommand & beginCommandWithEvent (rectangle)
    def beginCommand (self,undoType='Typing'):
    
        w = baseEditCommandsClass.beginCommand(self,undoType)
    
        r1, r2, r3, r4 = self.getRectanglePoints(w)
    
        return w, r1, r2, r3, r4
        
    def beginCommandWithEvent (self,event,undoType='Typing'):
        
        '''Do the common processing at the start of each command.'''
        
        w = baseEditCommandsClass.beginCommandWithEvent(self,event,undoType)
        
        r1, r2, r3, r4 = self.getRectanglePoints(w)
    
        return w, r1, r2, r3, r4
    #@-node:AGP.20250415230112.1131:beginCommand & beginCommandWithEvent (rectangle)
    #@+node:AGP.20250415230112.1132:Entries
    #@+node:AGP.20250415230112.1133:clearRectangle
    def clearRectangle (self,event):
        
        '''Clear the rectangle defined by the start and end of selected text.'''
        
        w = self.editWidget(event)
        if not w or not self.check(event): return
        
        w,r1,r2,r3,r4 = self.beginCommand('clear-rectangle')
    
        # Change the text.
        
        s = ' ' * (r4-r2)
        for r in xrange(r1,r3+1):
            w.delete('%s.%s' % (r,r2),'%s.%s' % (r,r4))
            w.insert('%s.%s' % (r,r2),s)
            
        self.endCommand()
    #@-node:AGP.20250415230112.1133:clearRectangle
    #@+node:AGP.20250415230112.1134:closeRectangle
    def closeRectangle (self,event):
        
        '''Delete the rectangle if it contains nothing but whitespace..'''
    
        w = self.editWidget(event)
        if not w or not self.check(event): return
    
        w,r1,r2,r3,r4 = self.beginCommand('close-rectangle')
      
        # Return if any part of the selection contains something other than whitespace.
        for r in xrange(r1,r3+1):
            s = w.get('%s.%s' % (r,r2),'%s.%s' % (r,r4))
            if s.strip(): return
    
        # Change the text.
        for r in xrange(r1,r3+1):
            w.delete('%s.%s' % (r,r2),'%s.%s' % (r,r4))
            
        self.endCommand()
    #@-node:AGP.20250415230112.1134:closeRectangle
    #@+node:AGP.20250415230112.1135:deleteRectangle
    def deleteRectangle (self,event):
        
        '''Delete the rectangle defined by the start and end of selected text.'''
    
        w = self.editWidget(event)
        if not w or not self.check(event): return
        
        w,r1,r2,r3,r4 = self.beginCommand('delete-rectangle')
    
        for r in xrange(r1,r3+1):
            w.delete('%s.%s' % (r,r2),'%s.%s' % (r,r4))
            
        self.endCommand()
    #@-node:AGP.20250415230112.1135:deleteRectangle
    #@+node:AGP.20250415230112.1136:killRectangle
    def killRectangle (self,event):
        
        '''Kill the rectangle defined by the start and end of selected text.'''
    
        w = self.editWidget(event)
        if not w or not self.check(event): return
        
        w,r1,r2,r3,r4 = self.beginCommand('kill-rectangle')
    
        self.theKillRectangle = []
        for r in xrange(r1,r3+1):
            s = w.get('%s.%s' % (r,r2),'%s.%s' % (r,r4))
            self.theKillRectangle.append(s)
            w.delete('%s.%s' % (r,r2),'%s.%s' % (r,r4))
    
        if self.theKillRectangle:
            w.mark_set('sel.start','insert')
            w.mark_set('sel.end','insert')
            
        self.endCommand()
    #@-node:AGP.20250415230112.1136:killRectangle
    #@+node:AGP.20250415230112.1137:openRectangle
    def openRectangle (self,event):
        
        '''Insert blanks in the rectangle defined by the start and end of selected text.
        This pushes the previous contents of the rectangle rightward.'''
    
        w = self.editWidget(event)
        if not w or not self.check(event): return
        
        w,r1,r2,r3,r4 = self.beginCommand('open-rectangle')
        
        s = ' ' * (r4-r2)
        for r in xrange(r1,r3+1):
            w.insert('%s.%s' % (r,r2),s)
            
        self.endCommand()
    #@-node:AGP.20250415230112.1137:openRectangle
    #@+node:AGP.20250415230112.1138:yankRectangle
    def yankRectangle (self,event,killRect=None):
        
        '''Yank into the rectangle defined by the start and end of selected text.'''
        
        c = self.c ; k = self.k
        w = self.editWidget(event)
        if not w: return
    
        killRect = killRect or self.theKillRectangle
        if not killRect:
            k.setLabelGrey('No kill rect')
            return
            
        w,r1,r2,r3,r4 = self.beginCommand('yank-rectangle')
        
        # Change the text.
        txt = w.get('insert linestart','insert')
        txt = self.getWSString(txt)
        i = w.index('insert')
        i1, i2 = i.split('.')
        i1 = int(i1)
        for z in killRect:
            txt2 = w.get('%s.0 linestart' % i1,'%s.%s' % (i1,i2))
            if len(txt2) != len(txt):
                amount = len(txt) - len(txt2)
                z = txt [-amount:] + z
            w.insert('%s.%s' % (i1,i2),z)
            if w.index('%s.0 lineend +1c' % i1) == w.index('end'):
                w.insert('%s.0 lineend' % i1,'\n')
            i1 += 1
    
        self.endCommand()
    #@-node:AGP.20250415230112.1138:yankRectangle
    #@+node:AGP.20250415230112.1139:stringRectangle
    def stringRectangle (self,event):
        
        '''Prompt for a string, then replace the contents of a rectangle with a string on each line.'''
    
        c = self.c ; k = self.k ; state = k.getState('string-rect')
        if state == 0:
            w = self.editWidget(event) # sets self.w
            if not w or not self.check(event): return
            self.stringRect = self.getRectanglePoints(w)
            k.setLabelBlue('String rectangle: ',protect=True)
            k.getArg(event,'string-rect',1,self.stringRectangle)
        else:
            k.clearState()
            k.resetLabel()
            w = self.w
            self.beginCommand('string-rectangle')
            r1, r2, r3, r4 = self.stringRect
            w.mark_set('sel.start','%d.%d' % (r1,r2))
            w.mark_set('sel.end',  '%d.%d' % (r3,r4))
            c.bodyWantsFocus()
            for r in xrange(r1,r3+1):
                w.delete('%s.%s' % (r,r2),'%s.%s' % (r,r4))
                w.insert('%s.%s' % (r,r2),k.arg)
            self.endCommand()
    #@nonl
    #@-node:AGP.20250415230112.1139:stringRectangle
    #@-node:AGP.20250415230112.1132:Entries
    #@-others
#@-node:AGP.20250415230112.1127:rectangleCommandsClass
#@+node:AGP.20250415230112.1140:registerCommandsClass
class registerCommandsClass (baseEditCommandsClass):

    '''A class to represent registers a-z and the corresponding Emacs commands.'''

    #@    @+others
    #@+node:AGP.20250415230112.1141:Birth
    #@+node:AGP.20250415230112.1142: ctor, finishCreate & init
    def __init__ (self,c):
        
        baseEditCommandsClass.__init__(self,c) # init the base class.
    
        self.methodDict, self.helpDict = self.addRegisterItems()
        self.init()
        
    def finishCreate (self):
        
        baseEditCommandsClass.finishCreate(self) # finish the base class.
        
        if self.k.useGlobalRegisters:
            self.registers = leoKeys.keyHandlerClass.global_registers
        else:
            self.registers = {}
            
    def init (self):
    
        self.method = None 
        self.registerMode = 0 # Must be an int.
    #@-node:AGP.20250415230112.1142: ctor, finishCreate & init
    #@+node:AGP.20250415230112.1143: getPublicCommands
    def getPublicCommands (self):
        
        return {
            'append-to-register':           self.appendToRegister,
            'copy-rectangle-to-register':   self.copyRectangleToRegister,
            'copy-to-register':             self.copyToRegister,
            'increment-register':           self.incrementRegister,
            'insert-register':              self.insertRegister,
            'jump-to-register':             self.jumpToRegister,
            # 'number-to-register':           self.numberToRegister,
            'point-to-register':            self.pointToRegister,
            'prepend-to-register':          self.prependToRegister,
            'view-register':                self.viewRegister,
        }
    #@-node:AGP.20250415230112.1143: getPublicCommands
    #@+node:AGP.20250415230112.1144:addRegisterItems (Not used!)
    def addRegisterItems( self ):
        
        methodDict = {
            'plus':     self.incrementRegister,
            'space':    self.pointToRegister,
            'a':        self.appendToRegister,
            'i':        self.insertRegister,
            'j':        self.jumpToRegister,
            # 'n':        self.numberToRegister,
            'p':        self.prependToRegister,
            'r':        self.copyRectangleToRegister,
            's':        self.copyToRegister,
            'v' :       self.viewRegister,
        }    
        
        helpDict = {
            's':    'copy to register',
            'i':    'insert from register',
            'plus': 'increment register',
            'n':    'number to register',
            'p':    'prepend to register',
            'a':    'append to register',
            'space':'point to register',
            'j':    'jump to register',
            'r':    'rectangle to register',
            'v': 'view register',
        }
    
        return methodDict, helpDict
    #@-node:AGP.20250415230112.1144:addRegisterItems (Not used!)
    #@-node:AGP.20250415230112.1141:Birth
    #@+node:AGP.20250415230112.1145:checkBodySelection
    def checkBodySelection (self,warning='No text selected'):
        
        return self._chckSel(event=None,warning=warning)
    #@-node:AGP.20250415230112.1145:checkBodySelection
    #@+node:AGP.20250415230112.1146:Entries...
    #@+node:AGP.20250415230112.1147:appendToRegister
    def appendToRegister (self,event):
        
        '''Prompt for a register name and append the selected text to the register's contents.'''
    
        c = self.c ; k = self.k ; state = k.getState('append-to-reg')
        
        if state == 0:
            k.setLabelBlue('Append to register: ',protect=True)
            k.setState('append-to-reg',1,self.appendToRegister)
        else:
            k.clearState()
            if self.checkBodySelection():
                if event.keysym.isalpha():
                    w = c.frame.body.bodyCtrl
                    c.bodyWantsFocus()
                    key = event.keysym.lower()
                    val = self.registers.get(key,'')
                    try:
                        val = val + w.get('sel.first','sel.last')
                    except Exception:
                        pass
                    self.registers[key] = val
                    k.setLabelGrey('Register %s = %s' % (key,repr(val)))
                else:
                    k.setLabelGrey('Register must be a letter')
        c.bodyWantsFocus()
    #@-node:AGP.20250415230112.1147:appendToRegister
    #@+node:AGP.20250415230112.1148:prependToRegister
    def prependToRegister (self,event):
        
        '''Prompt for a register name and prepend the selected text to the register's contents.'''
        
        c = self.c ; k = self.k ; state = k.getState('prepend-to-reg')
        
        if state == 0:
            k.setLabelBlue('Prepend to register: ',protect=True)
            k.setState('prepend-to-reg',1,self.prependToRegister)
        else:
            k.clearState()
            if self.checkBodySelection():
                if event.keysym.isalpha():
                    w = c.frame.body.bodyCtrl
                    c.bodyWantsFocus()
                    key = event.keysym.lower()
                    val = self.registers.get(key,'')
                    try:
                        val = w.get('sel.first','sel.last') + val
                    except Exception:
                        pass
                    self.registers[key] = val
                    k.setLabelGrey('Register %s = %s' % (key,repr(val)))
                else:
                    k.setLabelGrey('Register must be a letter')
        c.bodyWantsFocus()
    #@-node:AGP.20250415230112.1148:prependToRegister
    #@+node:AGP.20250415230112.1149:copyRectangleToRegister
    def copyRectangleToRegister (self,event):
        
        '''Prompt for a register name and append the rectangle defined by selected
        text to the register's contents.'''
    
        c = self.c ; k = self.k ; state = k.getState('copy-rect-to-reg')
    
        if state == 0:
            w = self.editWidget(event) # sets self.w
            if not w: return
            k.commandName = 'copy-rectangle-to-register'
            k.setLabelBlue('Copy Rectangle To Register: ',protect=True)
            k.setState('copy-rect-to-reg',1,self.copyRectangleToRegister)
        elif self.checkBodySelection('No rectangle selected'):
            k.clearState()
            if event.keysym.isalpha():
                key = event.keysym.lower()
                w = self.w
                c.widgetWantsFocusNow(w)
                r1, r2, r3, r4 = self.getRectanglePoints(w)
                rect = []
                while r1 <= r3:
                    txt = w.get('%s.%s' % (r1,r2),'%s.%s' % (r1,r4))
                    rect.append(txt)
                    r1 = r1 + 1
                self.registers [key] = rect
                k.setLabelGrey('Register %s = %s' % (key,repr(rect)))
            else:
                k.setLabelGrey('Register must be a letter')
        c.bodyWantsFocus()
    #@-node:AGP.20250415230112.1149:copyRectangleToRegister
    #@+node:AGP.20250415230112.1150:copyToRegister
    def copyToRegister (self,event):
        
        '''Prompt for a register name and append the selected text to the register's contents.'''
        
        c = self.c ; k = self.k ; state = k.getState('copy-to-reg')
        
        if state == 0:
            k.commandName = 'copy-to-register'
            k.setLabelBlue('Copy to register: ',protect=True)
            k.setState('copy-to-reg',1,self.copyToRegister)
        else:
            k.clearState()
            if self.checkBodySelection():
                if event.keysym.isalpha():
                    key = event.keysym.lower()
                    w = c.frame.body.bodyCtrl
                    c.bodyWantsFocus()
                    try:
                        val = w.get('sel.first','sel.last')
                    except Exception:
                        g.es_exception()
                        val = ''
                    self.registers[key] = val
                    k.setLabelGrey('Register %s = %s' % (key,repr(val)))
                else:
                    k.setLabelGrey('Register must be a letter')
        c.bodyWantsFocus()
    #@-node:AGP.20250415230112.1150:copyToRegister
    #@+node:AGP.20250415230112.1151:incrementRegister
    def incrementRegister (self,event):
        
        '''Prompt for a register name and increment its value if it has a numeric value.'''
        
        c = self.c ; k = self.k ; state = k.getState('increment-reg')
        
        if state == 0:
            k.setLabelBlue('Increment register: ',protect=True)
            k.setState('increment-reg',1,self.incrementRegister)
        else:
            k.clearState()
            if self._checkIfRectangle(event):
                pass # Error message is in the label.
            elif event.keysym.isalpha():
                key = event.keysym.lower()
                val = self.registers.get(key,0)
                try:
                    val = str(int(val)+1)
                    self.registers[key] = val
                    k.setLabelGrey('Register %s = %s' % (key,repr(val)))
                except ValueError:
                    k.setLabelGrey("Can't increment register %s = %s" % (key,val))
            else:
                k.setLabelGrey('Register must be a letter')
        c.bodyWantsFocus()
    #@-node:AGP.20250415230112.1151:incrementRegister
    #@+node:AGP.20250415230112.1152:insertRegister
    def insertRegister (self,event):
        
        '''Prompt for a register name and and insert the value of another register into its contents.'''
        
        c = self.c ; k = self.k ; state = k.getState('insert-reg')
        
        if state == 0:
            k.commandName = 'insert-register'
            k.setLabelBlue('Insert register: ',protect=True)
            k.setState('insert-reg',1,self.insertRegister)
        else:
            k.clearState()
            if event.keysym.isalpha():
                w = c.frame.body.bodyCtrl
                c.bodyWantsFocus()
                key = event.keysym.lower()
                val = self.registers.get(key)
                if val:
                    if type(val)==type([]):
                        c.rectangleCommands.yankRectangle(val)
                    else:
                        w.insert('insert',val)
                    k.setLabelGrey('Inserted register %s' % key)
                else:
                    k.setLabelGrey('Register %s is empty' % key)
            else:
                k.setLabelGrey('Register must be a letter')
        c.bodyWantsFocus()
    #@-node:AGP.20250415230112.1152:insertRegister
    #@+node:AGP.20250415230112.1153:jumpToRegister
    def jumpToRegister (self,event):
        
        '''Prompt for a register name and set the insert point to the value in its register.'''
    
        c = self.c ; k = self.k ; state = k.getState('jump-to-reg')
    
        if state == 0:
            k.setLabelBlue('Jump to register: ',protect=True)
            k.setState('jump-to-reg',1,self.jumpToRegister)
        else:
            k.clearState()
            if event.keysym.isalpha():
                if self._checkIfRectangle(event): return
                key = event.keysym.lower()
                val = self.registers.get(key)
                w = c.frame.body.bodyCtrl
                c.bodyWantsFocus()
                if val:
                    try:
                        w.mark_set('insert',val)
                        k.setLabelGrey('At %s' % repr(val))
                    except Exception:
                        k.setLabelGrey('Register %s is not a valid location' % key)
                else:
                    k.setLabelGrey('Register %s is empty' % key)
        c.bodyWantsFocus()
    #@-node:AGP.20250415230112.1153:jumpToRegister
    #@+node:AGP.20250415230112.1154:numberToRegister (not used)
    #@+at
    # C-u number C-x r n reg
    #     Store number into register reg (number-to-register).
    # C-u number C-x r + reg
    #     Increment the number in register reg by number (increment-register).
    # C-x r g reg
    #     Insert the number from register reg into the buffer.
    #@-at
    #@@c
    
    def numberToRegister (self,event):
        
        k = self.k ; state = k.getState('number-to-reg')
        
        if state == 0:
            k.commandName = 'number-to-register'
            k.setLabelBlue('Number to register: ',protect=True)
            k.setState('number-to-reg',1,self.numberToRegister)
        else:
            k.clearState()
            if event.keysym.isalpha():
                # self.registers[event.keysym.lower()] = str(0)
                k.setLabelGrey('number-to-register not ready yet.')
            else:
                k.setLabelGrey('Register must be a letter')
    #@-node:AGP.20250415230112.1154:numberToRegister (not used)
    #@+node:AGP.20250415230112.1155:pointToRegister
    def pointToRegister (self,event):
        
        '''Prompt for a register name and put a value indicating the insert point in the register.'''
        
        c = self.c ; k = self.k ; state = k.getState('point-to-reg')
        
        if state == 0:
            k.commandName = 'point-to-register'
            k.setLabelBlue('Point to register: ',protect=True)
            k.setState('point-to-reg',1,self.pointToRegister)
        else:
            k.clearState()
            if event.keysym.isalpha():
                w = c.frame.body.bodyCtrl
                c.bodyWantsFocus()
                key = event.keysym.lower()
                val = w.index('insert')
                self.registers[key] = val
                k.setLabelGrey('Register %s = %s' % (key,repr(val)))
            else:
                k.setLabelGrey('Register must be a letter')
        c.bodyWantsFocus()
    #@-node:AGP.20250415230112.1155:pointToRegister
    #@+node:AGP.20250415230112.1156:viewRegister
    def viewRegister (self,event):
        
        '''Prompt for a register name and print its contents.'''
    
        c = self.c ; k = self.k ; state = k.getState('view-reg')
        
        if state == 0:
            k.commandName = 'view-register'
            k.setLabelBlue('View register: ',protect=True)
            k.setState('view-reg',1,self.viewRegister)
        else:
            k.clearState()
            if event.keysym.isalpha():
                key = event.keysym.lower()
                val = self.registers.get(key)
                k.setLabelGrey('Register %s = %s' % (key,repr(val)))
            else:
                k.setLabelGrey('Register must be a letter')
        c.bodyWantsFocus()
    #@-node:AGP.20250415230112.1156:viewRegister
    #@-node:AGP.20250415230112.1146:Entries...
    #@-others
#@-node:AGP.20250415230112.1140:registerCommandsClass
#@+node:AGP.20250415230112.1157:Search classes
#@+node:AGP.20250415230112.1158:class minibufferFind( (the findHandler)
class minibufferFind (baseEditCommandsClass):

    '''An adapter class that implements minibuffer find commands using the (hidden) Find Tab.'''

    #@    @+others
    #@+node:AGP.20250415230112.1159: ctor (minibufferFind)
    def __init__(self,c,finder):
        
        baseEditCommandsClass.__init__(self,c) # init the base class.
    
        self.c = c
        self.k = k = c.k
        self.w = None
        self.finder = finder
        self.findTextList = []
        self.changeTextList = []
        
        commandName = 'replace-string'
        s = k.getShortcutForCommandName(commandName)
        s = k.prettyPrintKey(s)
        s = k.shortcutFromSetting(s)
        self.replaceStringShortcut = s
    #@-node:AGP.20250415230112.1159: ctor (minibufferFind)
    #@+node:AGP.20250415230112.1160: Options
    #@+node:AGP.20250415230112.1161:setFindScope
    def setFindScope(self,where):
        
        '''Set the find-scope radio buttons.
        
        `where` must be in ('node-only','entire-outline','suboutline-only'). '''
        
        h = self.finder
        
        if where in ('node-only','entire-outline','suboutline-only'):
            var = h.dict['radio-search-scope'].get()
            if var:
                h.dict["radio-search-scope"].set(where)
        else:
            g.trace('oops: bad `where` value: %s' % where)
    #@-node:AGP.20250415230112.1161:setFindScope
    #@+node:AGP.20250415230112.1162:setOption
    def setOption (self, ivar, val):
        
        h = self.finder
    
        if ivar in h.intKeys:
            if val is not None:
                var = h.dict.get(ivar)
                var.set(val)
                # g.trace('%s = %s' % (ivar,val))
    
        elif not g.app.unitTesting:
            g.trace('oops: bad find ivar %s' % ivar)
    #@-node:AGP.20250415230112.1162:setOption
    #@+node:AGP.20250415230112.1163:getOption
    def getOption (self,ivar,verbose=False):
        
        h = self.finder
        
        var = h.dict.get(ivar)
        if var:
            val = var.get()
            verbose and g.trace('%s = %s' % (ivar,val))
            return val
        else:
            g.trace('bad ivar name: %s' % ivar)
            return None
    #@-node:AGP.20250415230112.1163:getOption
    #@+node:AGP.20250415230112.1164:showFindOptions
    def showFindOptions (self):
        
        '''Show the present find options in the status line.'''
        
        frame = self.c.frame ; z = []
        # Set the scope field.
        head  = self.getOption('search_headline')
        body  = self.getOption('search_body')
        scope = self.getOption('radio-search-scope')
        d = {'entire-outline':'all','suboutline-only':'tree','node-only':'node'}
        scope = d.get(scope) or ''
        head = g.choose(head,'head','')
        body = g.choose(body,'body','')
        sep = g.choose(head and body,'+','')
    
        frame.clearStatusLine()
        s = '%s%s%s %s  ' % (head,sep,body,scope)
        frame.putStatusLine(s,color='blue')
    
        # Set the type field.
        script = self.getOption('script_search')
        regex  = self.getOption('pattern_match')
        change = self.getOption('script_change')
        if script:
            s1 = '*Script-find'
            s2 = g.choose(change,'-change*','*')
            z.append(s1+s2)
        elif regex: z.append('regex')
        
        table = (
            ('reverse',         'reverse'),
            ('ignore_case',     'noCase'),
            ('whole_word',      'word'),
            ('wrap',            'wrap'),
            ('mark_changes',    'markChg'),
            ('mark_finds',      'markFnd'),
        )
            
        for ivar,s in table:
            val = self.getOption(ivar)
            if val: z.append(s)
    
        frame.putStatusLine(' '.join(z))
    #@-node:AGP.20250415230112.1164:showFindOptions
    #@+node:AGP.20250415230112.1165:toggleOption
    def toggleOption (self, ivar):
        
        h = self.finder
    
        if ivar in h.intKeys:
            var = h.dict.get(ivar)
            val = not var.get()
            var.set(val)
            # g.trace('%s = %s' % (ivar,val),var)
        else:
            g.trace('oops: bad find ivar %s' % ivar)
    #@-node:AGP.20250415230112.1165:toggleOption
    #@+node:AGP.20250415230112.1166:setupChangePattern
    def setupChangePattern (self,pattern):
        
        h = self.finder ; t = h.change_ctrl
        
        s = g.toUnicode(pattern,g.app.tkEncoding)
        
        t.delete('1.0','end')
        t.insert('1.0',s)
        
        h.update_ivars()
    #@-node:AGP.20250415230112.1166:setupChangePattern
    #@+node:AGP.20250415230112.1167:setupSearchPattern
    def setupSearchPattern (self,pattern):
        
        h = self.finder ; t = h.find_ctrl
        
        s = g.toUnicode(pattern,g.app.tkEncoding)
        
        t.delete('1.0','end')
        t.insert('1.0',s)
        
        h.update_ivars()
    #@-node:AGP.20250415230112.1167:setupSearchPattern
    #@-node:AGP.20250415230112.1160: Options
    #@+node:AGP.20250415230112.1168:addChangeStringToLabel
    def addChangeStringToLabel (self,protect=True):
        
        c = self.c ; k = c.k ; h = self.finder ; t = h.change_ctrl
        
        c.frame.log.selectTab('Find')
        c.minibufferWantsFocusNow()
        
        s = t.get('1.0','end')
    
        while s.endswith('\n') or s.endswith('\r'):
            s = s[:-1]
    
        k.extendLabel(s,select=True,protect=protect)
    #@-node:AGP.20250415230112.1168:addChangeStringToLabel
    #@+node:AGP.20250415230112.1169:addFindStringToLabel
    def addFindStringToLabel (self,protect=True):
        
        c = self.c ; k = c.k ; h = self.finder ; t = h.find_ctrl
        
        c.frame.log.selectTab('Find')
        c.minibufferWantsFocusNow()
    
        s = t.get('1.0','end')
        while s.endswith('\n') or s.endswith('\r'):
            s = s[:-1]
    
        k.extendLabel(s,select=True,protect=protect)
    #@-node:AGP.20250415230112.1169:addFindStringToLabel
    #@+node:AGP.20250415230112.1170:cloneFindAll
    def cloneFindAll (self,event):
    
        c = self.c ; k = self.k ; tag = 'clone-find-all'
        state = k.getState(tag)
    
        if state == 0:
            w = self.editWidget(event) # sets self.w
            if not w: return
            self.setupArgs(forward=None,regexp=None,word=None)
            k.setLabelBlue('Clone Find All: ',protect=True)
            k.getArg(event,tag,1,self.cloneFindAll)
        else:
            k.clearState()
            k.resetLabel()
            k.showStateAndMode()
            self.generalSearchHelper(k.arg,cloneFindAll=True)
    #@-node:AGP.20250415230112.1170:cloneFindAll
    #@+node:AGP.20250415230112.1171:findAgain
    def findAgain (self,event):
    
        f = self.finder
        
        f.p = self.c.currentPosition()
        f.v = self.finder.p.v
    
        # This handles the reverse option.
        return f.findAgainCommand()
    #@-node:AGP.20250415230112.1171:findAgain
    #@+node:AGP.20250415230112.1172:findAll
    def findAll (self,event):
    
        k = self.k ; state = k.getState('find-all')
        if state == 0:
            w = self.editWidget(event) # sets self.w
            if not w: return
            self.setupArgs(forward=True,regexp=False,word=True)
            k.setLabelBlue('Find All: ',protect=True)
            k.getArg(event,'find-all',1,self.findAll)
        else:
            k.clearState()
            k.resetLabel()
            k.showStateAndMode()
            self.generalSearchHelper(k.arg,findAll=True)
    #@-node:AGP.20250415230112.1172:findAll
    #@+node:AGP.20250415230112.1173:generalChangeHelper
    def generalChangeHelper (self,find_pattern,change_pattern):
        
        # g.trace(repr(change_pattern))
        
        c = self.c
    
        self.setupSearchPattern(find_pattern)
        self.setupChangePattern(change_pattern)
        c.widgetWantsFocusNow(self.w)
    
        self.finder.p = self.c.currentPosition()
        self.finder.v = self.finder.p.v
    
        # This handles the reverse option.
        self.finder.findNextCommand()
    #@-node:AGP.20250415230112.1173:generalChangeHelper
    #@+node:AGP.20250415230112.1174:generalSearchHelper
    def generalSearchHelper (self,pattern,cloneFindAll=False,findAll=False):
        
        c = self.c
        
        self.setupSearchPattern(pattern)
        c.widgetWantsFocusNow(self.w)
    
        self.finder.p = self.c.currentPosition()
        self.finder.v = self.finder.p.v
    
        if findAll:
             self.finder.findAllCommand()
        elif cloneFindAll:
             self.finder.cloneFindAllCommand()
        else:
            # This handles the reverse option.
            self.finder.findNextCommand()
    #@-node:AGP.20250415230112.1174:generalSearchHelper
    #@+node:AGP.20250415230112.1175:lastStateHelper
    def lastStateHelper (self):
        
        k = self.k
        k.clearState()
        k.resetLabel()
        k.showStateAndMode()
    #@-node:AGP.20250415230112.1175:lastStateHelper
    #@+node:AGP.20250415230112.1176:replaceString
    def replaceString (self,event):
    
        k = self.k ; tag = 'replace-string' ; state = k.getState(tag)
        pattern_match = self.getOption ('pattern_match')
        prompt = 'Replace ' + g.choose(pattern_match,'Regex','String')
        if state == 0:
            self.setupArgs(forward=None,regexp=None,word=None)
            prefix = '%s: ' % prompt
            self.stateZeroHelper(event,tag,prefix,self.replaceString)
        elif state == 1:
            self._sString = k.arg
            self.updateFindList(k.arg)
            s = '%s: %s With: ' % (prompt,self._sString)
            k.setLabelBlue(s,protect=True)
            self.addChangeStringToLabel()
            k.getArg(event,'replace-string',2,self.replaceString,completion=False,prefix=s)
        elif state == 2:
            self.updateChangeList(k.arg)
            self.lastStateHelper()
            self.generalChangeHelper(self._sString,k.arg)
    #@-node:AGP.20250415230112.1176:replaceString
    #@+node:AGP.20250415230112.1177:reSearchBackward/Forward
    def reSearchBackward (self,event):
    
        k = self.k ; tag = 're-search-backward' ; state = k.getState(tag)
        
        if state == 0:
            self.setupArgs(forward=False,regexp=True,word=None)
            self.stateZeroHelper(
                event,tag,'Regexp Search Backward:',self.reSearchBackward,
                escapes=[self.replaceStringShortcut])
        elif k.getArgEscape:
            # Switch to the replace command.
            k.setState('replace-string',1,self.replaceString)
            self.replaceString(event=None)
        else:
            self.updateFindList(k.arg)
            self.lastStateHelper()
            self.generalSearchHelper(k.arg)
    
    def reSearchForward (self,event):
    
        k = self.k ; tag = 're-search-forward' ; state = k.getState(tag)
        if state == 0:
            self.setupArgs(forward=True,regexp=True,word=None)
            self.stateZeroHelper(
                event,tag,'Regexp Search:',self.reSearchForward,
                escapes=[self.replaceStringShortcut])
        elif k.getArgEscape:
            # Switch to the replace command.
            k.setState('replace-string',1,self.replaceString)
            self.replaceString(event=None)
        else:
            self.updateFindList(k.arg)
            self.lastStateHelper()
            self.generalSearchHelper(k.arg)
    #@-node:AGP.20250415230112.1177:reSearchBackward/Forward
    #@+node:AGP.20250415230112.1178:seachForward/Backward
    def searchBackward (self,event):
    
        k = self.k ; tag = 'search-backward' ; state = k.getState(tag)
    
        if state == 0:
            self.setupArgs(forward=False,regexp=False,word=False)
            self.stateZeroHelper(
                event,tag,'Search Backward: ',self.searchBackward,
                escapes=[self.replaceStringShortcut])
        elif k.getArgEscape:
            # Switch to the replace command.
            k.setState('replace-string',1,self.replaceString)
            self.replaceString(event=None)
        else:
            self.updateFindList(k.arg)
            self.lastStateHelper()
            self.generalSearchHelper(k.arg)
    
    def searchForward (self,event):
    
        k = self.k ; tag = 'search-forward' ; state = k.getState(tag)
    
        if state == 0:
            self.setupArgs(forward=True,regexp=False,word=False)
            self.stateZeroHelper(
                event,tag,'Search: ',self.searchForward,
                escapes=[self.replaceStringShortcut])
        elif k.getArgEscape:
            # Switch to the replace command.
            k.setState('replace-string',1,self.replaceString)
            self.replaceString(event=None)
        else:
            self.updateFindList(k.arg)
            self.lastStateHelper()
            self.generalSearchHelper(k.arg)
    #@-node:AGP.20250415230112.1178:seachForward/Backward
    #@+node:AGP.20250415230112.1179:searchWithPresentOptions
    def searchWithPresentOptions (self,event):
    
        k = self.k ; tag = 'search-with-present-options'
        state = k.getState(tag)
    
        if state == 0:
            self.setupArgs(forward=None,regexp=None,word=None)
            self.stateZeroHelper(
                event,tag,'Search: ',self.searchWithPresentOptions,
                escapes=[self.replaceStringShortcut])
        elif k.getArgEscape:
            # Switch to the replace command.
            k.setState('replace-string',1,self.replaceString)
            self.replaceString(event=None)
        else:
            self.updateFindList(k.arg)
            k.clearState()
            k.resetLabel()
            k.showStateAndMode()
            self.generalSearchHelper(k.arg)
    #@-node:AGP.20250415230112.1179:searchWithPresentOptions
    #@+node:AGP.20250415230112.1180:setupArgs
    def setupArgs (self,forward=False,regexp=False,word=False):
        
        h = self.finder ; k = self.k
        
        if forward is None:
            reverse = None
        else:
            reverse = not forward
    
        for ivar,val,in (
            ('reverse', reverse),
            ('pattern_match',regexp),
            ('whole_word',word),
        ):
            if val is not None:
                self.setOption(ivar,val)
                
        h.p = p = self.c.currentPosition()
        h.v = p.v
        h.update_ivars()
        self.showFindOptions()
    #@-node:AGP.20250415230112.1180:setupArgs
    #@+node:AGP.20250415230112.1181:stateZeroHelper
    def stateZeroHelper (self,event,tag,prefix,handler,escapes=[]):
    
        k = self.k
        self.w = self.editWidget(event)
        if not self.w: return
    
        k.setLabelBlue(prefix,protect=True)
        self.addFindStringToLabel(protect=False)
        
        # g.trace(escapes,g.callers())
        k.getArgEscapes = escapes
        k.getArgEscape = None # k.getArg may set this.
        k.getArg(event,tag,1,handler, # enter state 1
            tabList=self.findTextList,completion=True,prefix=prefix)
    #@-node:AGP.20250415230112.1181:stateZeroHelper
    #@+node:AGP.20250415230112.1182:updateChange/FindList
    def updateChangeList (self,s):
    
        if s not in self.changeTextList:
            self.changeTextList.append(s)
            
    def updateFindList (self,s):
    
        if s not in self.findTextList:
            self.findTextList.append(s)
    #@-node:AGP.20250415230112.1182:updateChange/FindList
    #@+node:AGP.20250415230112.1183:wordSearchBackward/Forward
    def wordSearchBackward (self,event):
    
        k = self.k ; tag = 'word-search-backward' ; state = k.getState(tag)
    
        if state == 0:
            self.setupArgs(forward=False,regexp=False,word=True)
            self.stateZeroHelper(event,tag,'Word Search Backward: ',self.wordSearchBackward)
        else:
            self.lastStateHelper()
            self.generalSearchHelper(k.arg)
    
    def wordSearchForward (self,event):
    
        k = self.k ; tag = 'word-search-forward' ; state = k.getState(tag)
        
        if state == 0:
            self.setupArgs(forward=True,regexp=False,word=True)
            self.stateZeroHelper(event,tag,'Word Search: ',self.wordSearchForward)
        else:
            self.lastStateHelper()
            self.generalSearchHelper(k.arg)
    #@-node:AGP.20250415230112.1183:wordSearchBackward/Forward
    #@-others
#@-node:AGP.20250415230112.1158:class minibufferFind( (the findHandler)
#@+node:AGP.20250415230112.1184:class searchCommandsClass
class searchCommandsClass (baseEditCommandsClass):
    
    '''Implements many kinds of searches.'''

    #@    @+others
    #@+node:AGP.20250415230112.1185: ctor (searchCommandsClass)
    def __init__ (self,c):
        
        # g.trace('searchCommandsClass')
    
        baseEditCommandsClass.__init__(self,c) # init the base class.
        
        self.finder = None
        
        #self.findTabHandler = None
        #self.minibufferFindHandler = None
        
        try:
            self.w = c.frame.body.bodyCtrl
        except AttributeError:
            self.w = None
            
        # For isearch commands.
        #self.ifinder = leoFind.leoFind(c,title='ifinder')
        #self.isearch_v = None # vnode of last isearch.
        #self.isearch_stack = [] # A stack of previous matches: entries are: (sel,insert)
        
        self.ignoreCase = None
        self.forward = None
        self.regexp = None
    #@-node:AGP.20250415230112.1185: ctor (searchCommandsClass)
    #@+node:AGP.20250415230112.1186:init()
    def init (self):    #agp
        
        #if self.finder == None:
            #self.finder = g.app.gui.frame.searchbox#SearchBox(self.c)
        
        
        
        pass
    #@nonl
    #@-node:AGP.20250415230112.1186:init()
    #@+node:AGP.20250415230112.1187:getPublicCommands (searchCommandsClass)
    def getPublicCommands (self):
        
        return {
            'clone-find-all':                       self.findTabCloneFindAll,#agp
            'find-all':                    self.findTabFindAll,#agp
            
            # Thin wrappers on Find tab
            'find-next':                    self.findTabFindNext,
            'find-prev':                    self.findTabFindPrev,
            'change-all':                   self.findTabChangeAll,
            'find-tab-change-then-find':            self.findTabChangeThenFind,
                        
            #'hide-find-tab':                        self.hideFindTab,
                
            #'isearch-forward':                      self.isearchForward,
            #'isearch-backward':                     self.isearchBackward,
            #'isearch-forward-regexp':               self.isearchForwardRegexp,
            #'isearch-backward-regexp':              self.isearchBackwardRegexp,
            #'isearch-with-present-options':         self.isearchWithPresentOptions,
                        
            'open-find-tab':                        self.openFindTab,
        
            #'replace-string':                       self.replaceString,
                        
            #'re-search-forward':                    self.reSearchForward,
            #'re-search-backward':                   self.reSearchBackward,
    
            #'search-again':                         self.findAgain,
            # Uses existing search pattern.
            
            'search-forward':                       self.searchForward,
            'search-backward':                      self.searchBackward,
            'search-with-present-options':          self.searchWithPresentOptions,
            # Prompts for search pattern.
    
            'set-find-everywhere':                  self.setFindScopeEveryWhere,
            'set-find-node-only':                   self.setFindScopeNodeOnly,
            'set-find-suboutline-only':             self.setFindScopeSuboutlineOnly,
            
            'show-find-options':                    self.showFindOptions,
    
            'toggle-find-ignore-case-option':       self.toggleIgnoreCaseOption,
            'toggle-find-in-body-option':           self.toggleSearchBodyOption,
            'toggle-find-in-headline-option':       self.toggleSearchHeadlineOption,
            'toggle-find-mark-changes-option':      self.toggleMarkChangesOption,
            'toggle-find-mark-finds-option':        self.toggleMarkFindsOption,
            'toggle-find-regex-option':             self.toggleRegexOption,
            'toggle-find-reverse-option':           self.toggleReverseOption,
            'toggle-find-word-option':              self.toggleWholeWordOption,
            'toggle-find-wrap-around-option':       self.toggleWrapSearchOption,
            
            'word-search-forward':                  self.wordSearchForward,
            'word-search-backward':                 self.wordSearchBackward,
        }
    #@-node:AGP.20250415230112.1187:getPublicCommands (searchCommandsClass)
    #@+node:AGP.20250415230112.1188:Top-level methods
    #@+node:AGP.20250415230112.1189:Find Tab commands
    # Just open the Find tab if it has never been opened.
    # For minibuffer commands, it would be good to force the Find tab to be visible.
    # However, this leads to unfortunate confusion when executed from a shortcut.
    
    def openFindTab(self,arg):
        self.finder.SetFocus()
    
    def findTabFindNext(self,event=None): #agp
        self.finder.findNextCommand()
    
    def findTabFindPrev(self,event=None): #agp
        self.finder.findPrevCommand()
    
    def findTabFindAll(self,event=None):
        '''Execute the 'Find All' command with the settings shown in the Find tab.'''
        self.finder.findAllCommand()
        
    def findTabCloneFindAll (self,event=None):
        '''Execute the 'Find Previous' command with the settings shown in the Find tab.'''
        self.finder.CloneFindAllCommand()
        
    
    def findTabChange(self,event=None):
        '''Execute the 'Change' command with the settings shown in the Find tab.'''
        self.finder.changeCommand()
        
    def findTabChangeAll(self,event=None):
        '''Execute the 'Change All' command with the settings shown in the Find tab.'''
        self.finder.changeAllCommand()
        
    
    def findTabChangeThenFind(self,event=None):
        '''Execute the 'Replace, Find' command with the settings shown in the Find tab.'''
        self.finder.changeThenFindCommand()
            
    #@-node:AGP.20250415230112.1189:Find Tab commands
    #@+node:AGP.20250415230112.1190:getHandler
    def getHandler(self,show=False):
        
        '''Return the minibuffer handler, creating it if necessary.'''
        
        c = self.c
        
        self.openFindTab(show=show)
            # sets self.findTabHandler,
            # but *not* minibufferFindHandler.
        
        if not self.minibufferFindHandler:
            self.minibufferFindHandler = minibufferFind(c,self.findTabHandler)
    
        return self.minibufferFindHandler
    #@-node:AGP.20250415230112.1190:getHandler
    #@+node:AGP.20250415230112.1191:Find options wrappers
    def setFindScopeEveryWhere (self, event):
        '''Set the 'Entire Outline' radio button in the Find tab.'''
        return self.setFindScope('entire-outline')
    
    def setFindScopeNodeOnly  (self, event):
        '''Set the 'Node Only' radio button in the Find tab.'''
        return self.setFindScope('node-only')
    
    def setFindScopeSuboutlineOnly (self, event):
        '''Set the 'Suboutline Only' radio button in the Find tab.'''
        return self.setFindScope('suboutline-only')
        
    def showFindOptions (self,event):
        '''Show all Find options in the minibuffer label area.'''
        self.getHandler().showFindOptions()
    
    def toggleIgnoreCaseOption     (self, event):
        '''Toggle the 'Ignore Case' checkbox in the Find tab.'''
        return self.toggleOption('ignore_case')
    
    def toggleMarkChangesOption (self, event):
        '''Toggle the 'Mark Changes' checkbox in the Find tab.'''
        return self.toggleOption('mark_changes')
    def toggleMarkFindsOption (self, event):
        '''Toggle the 'Mark Finds' checkbox in the Find tab.'''
        return self.toggleOption('mark_finds')
    def toggleRegexOption (self, event):
        '''Toggle the 'Regexp' checkbox in the Find tab.'''
        return self.toggleOption('pattern_match')
    def toggleReverseOption        (self, event):
        '''Toggle the 'Reverse' checkbox in the Find tab.'''
        return self.toggleOption('reverse')
    
    def toggleSearchBodyOption (self, event):
        '''Set the 'Search Body' checkbox in the Find tab.'''
        return self.toggleOption('search_body')
    
    def toggleSearchHeadlineOption (self, event):
        '''Toggle the 'Search Headline' checkbox in the Find tab.'''
        return self.toggleOption('search_headline')
    
    def toggleWholeWordOption (self, event):
        '''Toggle the 'Whole Word' checkbox in the Find tab.'''
        return self.toggleOption('whole_word')
    
    def toggleWrapSearchOption (self, event):
        '''Toggle the 'Wrap Around' checkbox in the Find tab.'''
        return self.toggleOption('wrap')
        
    def setFindScope (self, where):  self.getHandler().setFindScope(where)
    def toggleOption (self, ivar):   self.getHandler().toggleOption(ivar)
    #@-node:AGP.20250415230112.1191:Find options wrappers
    #@+node:AGP.20250415230112.1192:Find wrappers
    def cloneFindAll (self,event):
        '''Do search-with-present-options and print all matches in the log pane. It
        also creates a node at the beginning of the outline containing clones of all
        nodes containing the 'find' string. Only one clone is made of each node,
        regardless of how many clones the node has, or of how many matches are found
        in each node.'''
        self.getHandler().cloneFindAll(event)
    
    def findAll            (self,event):
        '''Do search-with-present-options and print all matches in the log pane.'''
        self.getHandler().findAll(event)
    
    def replaceString      (self,event):
        '''Prompts for a search string. Type <Return> to end the search string. The
        command will then prompt for the replacement string. Typing a second
        <Return> key will place both strings in the Find tab and executes a **find**
        command, that is, the search-with-present-options command.'''
        self.getHandler().replaceString(event)
    
    def reSearchBackward   (self,event):
        '''Set the 'Regexp' checkbox to True and the 'Reverse' checkbox to True,
        then do search-with-present-options.'''
        self.getHandler().reSearchBackward(event)
    
    def reSearchForward    (self,event):
        '''Set the 'Regexp' checkbox to True, then do search-with-present-options.'''
        self.getHandler().reSearchForward(event)
    
    def searchBackward     (self,event):
        '''Set the 'Word Search' checkbox to False and the 'Reverse' checkbox to True,
        then do search-with-present-options.'''
        self.getHandler().searchBackward(event)
    
    def searchForward      (self,event):
        '''Set the 'Word Search' checkbox to False, then do search-with-present-options.'''
        self.getHandler().searchForward(event)
    
    def wordSearchBackward (self,event):
        '''Set the 'Word Search' checkbox to True, then do search-with-present-options.'''
        self.getHandler().wordSearchBackward(event)
    
    def wordSearchForward  (self,event):
        '''Set the Word Search' checkbox to True and the 'Reverse' checkbox to True,
        then do search-with-present-options.'''
        self.getHandler().wordSearchForward(event)
    
    def searchWithPresentOptions (self,event):
        '''Prompts for a search string. Typing the <Return> key puts the search
        string in the Find tab and executes a search based on all the settings in
        the Find tab. Recommended as the default search command.'''
        self.getHandler().searchWithPresentOptions(event)
    #@-node:AGP.20250415230112.1192:Find wrappers
    #@+node:AGP.20250415230112.1193:findAgain
    def findAgain (self,event):
    
        '''The find-again command is the same as the find-tab-find-next command
        if the search pattern in the Find tab is not '<find pattern here>'
        Otherwise, the find-again is the same as the search-with-present-options command.'''
        
        h = self.getHandler()
        
        # h.findAgain returns False if there is no search pattern.
        # In that case, we revert to search-with-present-options.
        if not h.findAgain(event):
            h.searchWithPresentOptions(event)
    #@-node:AGP.20250415230112.1193:findAgain
    #@-node:AGP.20250415230112.1188:Top-level methods
    #@-others
#@-node:AGP.20250415230112.1184:class searchCommandsClass
#@-node:AGP.20250415230112.1157:Search classes
#@+node:AGP.20250415230112.1194:Spell classes
#@+others
#@+node:AGP.20250415230112.1195:class spellCommandsClass
class spellCommandsClass (baseEditCommandsClass):
    
    '''Commands to support the Spell Tab.'''

    #@    @+others
    #@+node:AGP.20250415230112.1196:ctor
    def __init__ (self,c):
    
        baseEditCommandsClass.__init__(self,c) # init the base class.
        
        self.handler = None
        
        # All the work happens when we first open the frame.
    #@-node:AGP.20250415230112.1196:ctor
    #@+node:AGP.20250415230112.1197:getPublicCommands (searchCommandsClass)
    def getPublicCommands (self):
        
        return {
            'open-spell-tab':           self.openSpellTab,
            'spell-find':               self.find,
            'spell-change':             self.change,
            'spell-change-then-find':   self.changeThenFind,
            'spell-ignore':             self.ignore,
            'hide-spell-tab':           self.hide,
        }
    #@-node:AGP.20250415230112.1197:getPublicCommands (searchCommandsClass)
    #@+node:AGP.20250415230112.1198:openSpellTab
    def openSpellTab (self,event=None):
        
        '''Open the Spell Checker tab in the log pane.'''
    
        c = self.c ; log = c.frame.log ; tabName = 'Spell'
    
        if log.frameDict.get(tabName):
            log.selectTab(tabName)
        elif self.handler:
            if self.handler.loaded:
                self.handler.bringToFront()
        else:
            log.selectTab(tabName)
            f = log.frameDict.get(tabName)
            t = log.textDict.get(tabName)
            t.pack_forget()
            self.handler = spellTab(c,f)
            
        self.handler.bringToFront()
    #@-node:AGP.20250415230112.1198:openSpellTab
    #@+node:AGP.20250415230112.1199:commands...
    # Just open the Spell tab if it has never been opened.
    # For minibuffer commands, we must also force the Spell tab to be visible.
    
    def find (self,event=None):
        '''Simulate pressing the 'Find' button in the Spell tab.'''
        if self.handler:
            self.openSpellTab()
            self.handler.find()
        else:
            self.openSpellTab()
    
    def change(self,event=None):
        '''Simulate pressing the 'Change' button in the Spell tab.'''
        if self.handler:
            self.openSpellTab()
            self.handler.change()
        else:
            self.openSpellTab()
            
    def changeAll(self,event=None):
    
        if self.handler:
            self.openSpellTab()
            self.handler.changeAll()
        else:
            self.openSpellTab()
    
    def changeThenFind (self,event=None):
        '''Simulate pressing the 'Change, Find' button in the Spell tab.'''
        if self.handler:
            self.openSpellTab()
            self.handler.changeThenFind()
        else:
            self.openSpellTab()
            
    def hide (self,event=None):
        '''Hide the Spell tab.'''
        if self.handler:
            self.c.frame.log.selectTab('Log')
            self.c.bodyWantsFocus()
    
    def ignore (self,event=None):
        '''Simulate pressing the 'Ignore' button in the Spell tab.'''
        if self.handler:
            self.openSpellTab()
            self.handler.ignore()
        else:
            self.openSpellTab()
    #@-node:AGP.20250415230112.1199:commands...
    #@-others
#@-node:AGP.20250415230112.1195:class spellCommandsClass
#@+node:AGP.20250415230112.1200:class AspellClass
class AspellClass:
    
    """A wrapper class for Aspell spell checker"""
    
    #@    @+others
    #@+node:AGP.20250415230112.1201:Birth & death
    #@+node:AGP.20250415230112.1202:__init__
    def __init__ (self,c,local_dictionary_file,local_language_code):
    
        """Ctor for the Aspell class."""
    
        self.c = c
    
        self.aspell_dir = g.os_path_abspath(c.config.getString('aspell_dir'))
        self.aspell_bin_dir = g.os_path_abspath(c.config.getString('aspell_bin_dir'))
        
        self.local_language_code = local_language_code or 'en'
        self.local_dictionary_file = g.os_path_abspath(local_dictionary_file)
        self.local_dictionary = "%s.wl" % os.path.splitext(self.local_dictionary_file) [0]
        
        # g.trace('code',self.local_language_code,'dict',self.local_dictionary_file)
        # g.trace('dir',self.aspell_dir,'bin_dir',self.aspell_bin_dir)
        
        version = '.'.join([str(sys.version_info[i]) for i in (0,1)])
        self.use_ctypes = g.CheckVersion(version,'2.5')
        self.aspell = self.sc = None
        
        if self.use_ctypes:
            self.getAspellWithCtypes()
        else:
            self.getAspell()
    #@-node:AGP.20250415230112.1202:__init__
    #@+node:AGP.20250415230112.1203:getAspell
    def getAspell (self):
    
        try:
            import aspell
        except ImportError:
            # Specify the path to the top-level Aspell directory.
            theDir = g.choose(sys.platform=='darwin',self.aspell_dir,self.aspell_bin_dir)
            aspell = g.importFromPath('aspell',theDir,pluginName=__name__,verbose=True)
    
        self.aspell = aspell
        self.sc = aspell and aspell.spell_checker(prefix=self.aspell_dir,lang=self.local_language_code)
    #@nonl
    #@-node:AGP.20250415230112.1203:getAspell
    #@+node:AGP.20250415230112.1204:getAspellWithCtypes
    def getAspellWithCtypes (self):
        
        import ctypes
        c_int, c_char_p = ctypes.c_int, ctypes.c_char_p
    
        aspell = ctypes.CDLL(g.os_path_join(self.aspell_bin_dir, "aspell-15.dll"))
    
        #@    << define and configure aspell entry points >>
        #@+node:AGP.20250415230112.1205:<< define and configure aspell entry points >>
        # new_aspell_config
        new_aspell_config = aspell.new_aspell_config 
        new_aspell_config.restype = c_int
        
        # aspell_config_replace
        aspell_config_replace = aspell.aspell_config_replace 
        aspell_config_replace.argtypes = [c_int, c_char_p, c_char_p] 
        
        # aspell_config_retrieve
        aspell_config_retrieve = aspell.aspell_config_retrieve 
        aspell_config_retrieve.restype = c_char_p  
        aspell_config_retrieve.argtypes = [c_int, c_char_p] 
        
        # aspell_error_message
        aspell_error_message = aspell.aspell_error_message 
        aspell_error_message.restype = c_char_p  
        
        sc = new_aspell_config()
        if 0:
            print sc 
            print aspell_config_replace(sc, "prefix", aspell_dir) #1/0 
            print 'prefix', aspell_dir, `aspell_config_retrieve(sc, "prefix")`
            print aspell_config_retrieve(sc, "lang")
            print aspell_config_replace(sc, "lang",self.local_language_code)
            print aspell_config_retrieve(sc, "lang")
        
        possible_err = aspell.new_aspell_speller(sc)
        aspell.delete_aspell_config(c_int(sc))
        
        # Rudimentary error checking, needs more.  
        if aspell.aspell_error_number(possible_err) != 0:
            print 'err', aspell_error_message(possible_err)
            spell_checker = None
        else: 
            spell_checker = aspell.to_aspell_speller(possible_err)
        
        if not spell_checker:
            raise Exception('aspell checker not enabled')
        
        word_list_size = aspell.aspell_word_list_size
        word_list_size.restype = c_int
        word_list_size.argtypes = [c_int,]
        
        # word_list_elements
        word_list_elements = aspell.aspell_word_list_elements
        word_list_elements.restype = c_int
        word_list_elements.argtypes = [c_int,]
        
        # string_enumeration_next
        string_enumeration_next = aspell.aspell_string_enumeration_next
        string_enumeration_next.restype = c_char_p
        string_enumeration_next.argtypes = [c_int,]
        
        # check
        check = aspell.aspell_speller_check
        check.restype = c_int 
        check.argtypes = [c_int, c_char_p, c_int]
        
        # suggest
        suggest = aspell.aspell_speller_suggest
        suggest.restype = c_int 
        suggest.argtypes = [c_int, c_char_p, c_int]
        #@nonl
        #@-node:AGP.20250415230112.1205:<< define and configure aspell entry points >>
        #@nl
    
        # Remember these functions (bound methods).
        # No other ctypes data is known outside this method.
        self.check = check
        self.spell_checker = spell_checker
        self.string_enumeration_next = string_enumeration_next
        self.suggest = suggest
        self.word_list_elements = word_list_elements
        self.word_list_size = word_list_size
    #@-node:AGP.20250415230112.1204:getAspellWithCtypes
    #@-node:AGP.20250415230112.1201:Birth & death
    #@+node:AGP.20250415230112.1206:processWord
    def processWord(self, word):
        """Pass a word to aspell and return the list of alternatives.
        OK: 
        * 
        Suggestions: 
        & «original» «count» «offset»: «miss», «miss», ... 
        None: 
        # «original» «offset» 
        simplifyed to not create the string then make a list from it 
        """
        
        if self.use_ctypes:
            if self.check(self.spell_checker,word,len(word)):
                return None
            else:
                return self.suggestions(word)
        else:
            if self.sc.check(word):
                return None
            else:
                return self.sc.suggest(word)
    #@-node:AGP.20250415230112.1206:processWord
    #@+node:AGP.20250415230112.1207:suggestions
    def suggestions(self,word):
    
        "return list of words found"
        
        aList = []
        sw = self.suggest(self.spell_checker, word, len(word))
    
        if self.word_list_size(sw):
            ewords = self.word_list_elements(sw)
            while 1: 
                x = self.string_enumeration_next(ewords)
                if x is None: break
                aList.append(x)
        return aList
    #@nonl
    #@-node:AGP.20250415230112.1207:suggestions
    #@+node:AGP.20250415230112.1208:updateDictionary
    def updateDictionary(self):
    
        """Update the aspell dictionary from a list of words.
        
        Return True if the dictionary was updated correctly."""
    
        try:
            # Create master list
            basename = os.path.splitext(self.local_dictionary)[0]
            cmd = (
                "%s --lang=%s create master %s.wl < %s.txt" %
                (self.aspell_bin_dir, self.local_language_code, basename,basename))
            os.popen(cmd)
            return True
    
        except Exception, err:
            g.es_print("Unable to update local aspell dictionary: %s" % err)
            return False
    #@-node:AGP.20250415230112.1208:updateDictionary
    #@-others
#@-node:AGP.20250415230112.1200:class AspellClass
#@-others
#@-node:AGP.20250415230112.1194:Spell classes
#@-others

#@<< define classesList >>
#@+node:AGP.20250415230112.1209:<< define classesList >>
classesList = [
    ('abbrevCommands',      abbrevCommandsClass),
    ('bufferCommands',      bufferCommandsClass),
    ('editCommands',        editCommandsClass),
    ('controlCommands',     controlCommandsClass),
    ('debugCommands',       debugCommandsClass),
    ('editFileCommands',    editFileCommandsClass),
    ('helpCommands',        helpCommandsClass),
    ('keyHandlerCommands',  keyHandlerCommandsClass),
    ('killBufferCommands',  killBufferCommandsClass),
    ('leoCommands',         leoCommandsClass),
    ('macroCommands',       macroCommandsClass),
    ('queryReplaceCommands',queryReplaceCommandsClass),
    ('rectangleCommands',   rectangleCommandsClass),
    ('registerCommands',    registerCommandsClass),
    ('searchCommands',      searchCommandsClass),
    ('spellCommands',       spellCommandsClass),
]
#@-node:AGP.20250415230112.1209:<< define classesList >>
#@nl
#@-node:AGP.20250415230112.813:@thin leoEditCommands.py
#@-leo
