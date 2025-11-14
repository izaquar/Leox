#@+leo-ver=4-thin
#@+node:AGP.20250415230112.3125:@thin leoTkinterDialog.py
#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
import string

import Tkinter as Tk

#@+others
#@+node:AGP.20250415230112.3126: class leoTkinterDialog
class leoTkinterDialog:
    """The base class for all Leo Tkinter dialogs"""
    #@    @+others
    #@+node:AGP.20250415230112.3127:__init__ (tkDialog)
    def __init__(self,c,title="",resizeable=True,canClose=True,show=True):
        
        """Constructor for the leoTkinterDialog class."""
        
        self.answer = None # Value returned from run()
        self.c = c # For use by delayed focus methods in c.frame.
        self.resizeable = resizeable
        self.title = title
        self.modal = None
        
        self.buttonsFrame = None # Frame to hold typical dialog buttons.
        self.defaultButtonCommand = None  # Command to call when user closes the window by clicking the close box.
        self.frame = None # The outermost frame.
        self.root = None # g.app.root
        self.showFlag = show
        self.top = None # The toplevel Tk widget.
        self.focus_widget = None # The widget to get the first focus.
        self.canClose = canClose
    #@-node:AGP.20250415230112.3127:__init__ (tkDialog)
    #@+node:AGP.20250415230112.3128:cancelButton, noButton, okButton, yesButton
    def cancelButton(self):
        
        """Do default click action in cancel button."""
        
        self.answer="cancel"
        self.top.destroy()
        
    def noButton(self):
        
        """Do default click action in no button."""
        
        self.answer="no"
        self.top.destroy()
        
    def okButton(self):
        
        """Do default click action in ok button."""
        
        self.answer="ok"
        self.top.destroy()
    
    def yesButton(self):
        
        """Do default click action in yes button."""
    
        self.answer="yes"
        self.top.destroy()
    #@-node:AGP.20250415230112.3128:cancelButton, noButton, okButton, yesButton
    #@+node:AGP.20250415230112.3129:center
    def center(self):
        
        """Center any leoTkinterDialog."""
        
        g.app.gui.center_dialog(self.top)
    #@-node:AGP.20250415230112.3129:center
    #@+node:AGP.20250415230112.3130:createButtons
    def createButtons (self,buttons):
        
        """Create a row of buttons.
        
        buttons is a list of dictionaries containing the properties of each button."""
        
        assert(self.frame)
        self.buttonsFrame = f = Tk.Frame(self.top)
        f.pack(side="top",padx=30)
    
        # Buttons is a list of dictionaries, with an empty dictionary at the end if there is only one entry.
        buttonList = []
        for d in buttons:
            text = d.get("text","<missing button name>")
            isDefault = d.get("default",False)
            underline = d.get("underline",0)
            command = d.get("command",None)
            bd = g.choose(isDefault,4,2)
    
            b = Tk.Button(f,width=6,text=text,bd=bd,underline=underline,command=command)
            b.pack(side="left",padx=5,pady=10)
            buttonList.append(b)
            
            if isDefault and command:
                self.defaultButtonCommand = command
            
        return buttonList
    #@-node:AGP.20250415230112.3130:createButtons
    #@+node:AGP.20250415230112.3131:createMessageFrame
    def createMessageFrame (self,message):
        
        """Create a frame containing a Tk.Label widget."""
    
        label = Tk.Label(self.frame,text=message)
        label.pack(pady=10)
    #@-node:AGP.20250415230112.3131:createMessageFrame
    #@+node:AGP.20250415230112.3132:createTopFrame
    def createTopFrame(self):
        
        """Create the Tk.Toplevel widget for a leoTkinterDialog."""
    
        if g.app.unitTesting: return
        
        self.root = g.app.root
        # g.trace("leoTkinterDialog",'root',self.root)
    
        self.top = Tk.Toplevel(self.root)
        self.top.title(self.title)
    
        if not self.resizeable:
            self.top.resizable(0,0) # neither height or width is resizable.
    
        self.frame = Tk.Frame(self.top)
        self.frame.pack(side="top",expand=1,fill="both")
        
        if not self.canClose:
            self.top.protocol("WM_DELETE_WINDOW", self.onClose)
        
        # Do this at idle time.
        def attachIconCallback(top=self.top):
            g.app.gui.attachLeoIcon(top)
        
        self.top.after_idle(attachIconCallback)
    #@-node:AGP.20250415230112.3132:createTopFrame
    #@+node:AGP.20250415230112.3133:onClose
    def onClose (self):
        
        """Disable all attempts to close this frame with the close box."""
        
        pass
    #@-node:AGP.20250415230112.3133:onClose
    #@+node:AGP.20250415230112.3134:run (tkDialog)
    def run (self,modal):
        
        """Run a leoTkinterDialog."""
        
        if g.app.unitTesting: return None
    
        c = self.c ; self.modal = modal
    
        self.center() # Do this after all packing complete.
        if self.showFlag:
            self.top.lift()
        else:
            self.top.withdraw()
    
        # Get all keystrokes.
        if self.modal:
            self.top.grab_set() # Make the dialog a modal dialog.
            
        if self.focus_widget == None:
            self.focus_widget = self.top
            
        c and c.widgetWantsFocusNow(self.focus_widget)
           
        self.root.wait_window(self.top)
        
        if self.modal:
            return self.answer
        else:
            return None
    #@-node:AGP.20250415230112.3134:run (tkDialog)
    #@-others
#@-node:AGP.20250415230112.3126: class leoTkinterDialog
#@+node:AGP.20250415230112.3135:class tkinterAboutLeo
class tkinterAboutLeo (leoTkinterDialog):
    
    """A class that creates the Tkinter About Leo dialog."""

    #@    @+others
    #@+node:AGP.20250415230112.3136:tkinterAboutLeo.__init__
    def __init__ (self,c,version,theCopyright,url,email):
        
        """Create a Tkinter About Leo dialog."""
    
        leoTkinterDialog.__init__(self,c,"About Leox",resizeable=True) # Initialize the base class.
        
        if g.app.unitTesting: return
        
        self.copyright = theCopyright
        self.email = email
        self.url = url
        self.version = version
        
        c.inCommand = False # Allow the app to close immediately.
    
        self.createTopFrame()
        self.createFrame()
    #@-node:AGP.20250415230112.3136:tkinterAboutLeo.__init__
    #@+node:AGP.20250415230112.3137:tkinterAboutLeo.createFrame
    def createFrame (self):
        
        """Create the frame for an About Leo dialog."""
        
        if g.app.unitTesting: return
        
        frame = self.frame
        theCopyright = self.copyright ; email = self.email
        url = self.url ; version = self.version
        
        print g.app.leoDir
        version = "Leox "+open(g.app.leoDir+"/VERSION").read()+"\n\n"
        # Calculate the approximate height & width. (There are bugs in Tk here.)
        lines = string.split(theCopyright,'\n')
        height = len(lines) + 8 # Add lines for version,url,email,spacing.
        width = 0
        for line in lines:
            width = max(width,len(line))
        width = max(width,len(url))
        width += 10 # 9/9/02
    
        frame.pack(padx=6,pady=4)
        
        self.text = text = Tk.Text(frame,height=height,width=width,bd=0,bg=frame.cget("background"))
        text.pack(pady=10)
        
        
        
        text.insert("end",'\n\n')
        text.insert("end",version,"version")
        text.insert("end",theCopyright,"copyright")
        #text.insert("end",'\n')
        text.insert("end",url,"url") # Add "url" tag.
        text.insert("end",'\n')
        #text.insert("end",email,"email") # Add "email" tag.
        
        text.tag_config("version",justify="center")
        text.tag_config("copyright",justify="center",spacing1="3")
        
        text.tag_config("url",underline=1,justify="center",spacing1="10")
        text.tag_bind("url","<Button-1>",self.onAboutLeoUrl)
        text.tag_bind("url","<Enter>",self.setArrowCursor)
        text.tag_bind("url","<Leave>",self.setDefaultCursor)
    
        text.tag_config("email",underline=1,justify="center",spacing1="10")
        #text.tag_bind("email","<Button-1>",self.onAboutLeoEmail)
        text.tag_bind("email","<Enter>",self.setArrowCursor)
        text.tag_bind("email","<Leave>",self.setDefaultCursor)
    
        text.configure(state="disabled")
    #@-node:AGP.20250415230112.3137:tkinterAboutLeo.createFrame
    #@+node:AGP.20250415230112.3138:tkinterAboutLeo.onAboutLeoEmail
    def onAboutLeoEmail(self,event=None):
        
        """Handle clicks in the email link in an About Leo dialog."""
        
        try:
            import webbrowser
            webbrowser.open("mailto:" + self.email)
        except:
            g.es("not found: " + self.email)
    #@-node:AGP.20250415230112.3138:tkinterAboutLeo.onAboutLeoEmail
    #@+node:AGP.20250415230112.3139:tkinterAboutLeo.onAboutLeoUrl
    def onAboutLeoUrl(self,event=None):
        
        """Handle clicks in the url link in an About Leo dialog."""
        
        try:
            import webbrowser
            webbrowser.open(self.url)
        except:
            g.es("not found: " + self.url)
    #@-node:AGP.20250415230112.3139:tkinterAboutLeo.onAboutLeoUrl
    #@+node:AGP.20250415230112.3140:tkinterAboutLeo: setArrowCursor, setDefaultCursor
    def setArrowCursor (self,event=None):
        
        """Set the cursor to an arrow in an About Leo dialog."""
        
        self.text.configure(cursor="arrow")
        
    def setDefaultCursor (self,event=None):
        
        """Set the cursor to the default cursor in an About Leo dialog."""
        
        self.text.configure(cursor="xterm")
    #@-node:AGP.20250415230112.3140:tkinterAboutLeo: setArrowCursor, setDefaultCursor
    #@-others
#@-node:AGP.20250415230112.3135:class tkinterAboutLeo
#@+node:AGP.20250415230112.3141:class tkinterAskLeoID
class tkinterAskLeoID (leoTkinterDialog):
    
    """A class that creates the Tkinter About Leo dialog."""

    #@    @+others
    #@+node:AGP.20250415230112.3142:tkinterAskLeoID.__init__
    def __init__(self,c=None):
        
        """Create the Leo Id dialog."""
    
        # Initialize the base class: prevent clicks in the close box from closing.
        leoTkinterDialog.__init__(self,c,"Enter unique id",resizeable=False,canClose=False)
        
        if g.app.unitTesting: return
            
        self.id_entry = None
        self.answer = None
    
        self.createTopFrame()
        self.top.bind("<Key>", self.onKey)
        
        message = (
            "Please enter an id that identifies you uniquely.\n\n" +
            
            "Your id must contain only letters and numbers\n" +
            "and must be at least 3 characters in length.")
        self.createFrame(message)
        self.focus_widget = self.id_entry
    
        buttons = {"text":"OK","command":self.onButton,"default":True}, # Singleton tuple.
        buttonList = self.createButtons(buttons)
        self.ok_button = buttonList[0]
        self.ok_button.configure(state="disabled")
    #@-node:AGP.20250415230112.3142:tkinterAskLeoID.__init__
    #@+node:AGP.20250415230112.3143:tkinterAskLeoID.createFrame
    def createFrame(self,message):
        
        """Create the frame for the Leo Id dialog."""
        
        if g.app.unitTesting: return
        
        f = self.frame
    
        label = Tk.Label(f,text=message)
        label.pack(pady=10)
    
        self.id_entry = text = Tk.Entry(f,width=20)
        text.pack()
    #@-node:AGP.20250415230112.3143:tkinterAskLeoID.createFrame
    #@+node:AGP.20250415230112.3144:tkinterAskLeoID.onButton
    def onButton(self):
        
        """Handle clicks in the Leo Id close button."""
    
        s = self.id_entry.get().strip()
        if len(s) < 3:  # Require at least 3 characters in an id.
            return
    
        self.answer = g.app.leoID = s
        
        self.top.destroy() # terminates wait_window
        self.top = None
    #@-node:AGP.20250415230112.3144:tkinterAskLeoID.onButton
    #@+node:AGP.20250415230112.3145:tkinterAskLeoID.onKey
    def onKey(self,event):
        
        """Handle keystrokes in the Leo Id dialog."""
        
        #@    << eliminate invalid characters >>
        #@+node:AGP.20250415230112.3146:<< eliminate invalid characters >>
        e = self.id_entry
        s = e.get().strip()
        i = 0 ; ok = True
        while i < len(s):
            ch = s[i]
            if not ch.isalnum():
                e.delete(str(i))
                s = e.get()
                ok = False
            else:
                i += 1
        if not ok: return
        #@-node:AGP.20250415230112.3146:<< eliminate invalid characters >>
        #@nl
        #@    << enable the ok button if there are 3 or more valid characters >>
        #@+node:AGP.20250415230112.3147:<< enable the ok button if there are 3 or more valid characters >>
        e = self.id_entry
        b = self.ok_button
        
        if len(e.get().strip()) >= 3:
            b.configure(state="normal")
        else:
            b.configure(state="disabled")
        #@-node:AGP.20250415230112.3147:<< enable the ok button if there are 3 or more valid characters >>
        #@nl
        
        ch = event.char.lower()
        if ch in ('\n','\r'):
            self.onButton()
        return "break"
    #@-node:AGP.20250415230112.3145:tkinterAskLeoID.onKey
    #@-others
#@-node:AGP.20250415230112.3141:class tkinterAskLeoID
#@+node:AGP.20250415230112.3148:class tkinterAskOk
class tkinterAskOk(leoTkinterDialog):
    
    """A class that creates a Tkinter dialog with a single OK button."""

    #@    @+others
    #@+node:AGP.20250415230112.3149:class tkinterAskOk.__init__
    def __init__ (self,c,title,message=None,text="Ok",resizeable=False):
    
        """Create a dialog with one button"""
    
        leoTkinterDialog.__init__(self,c,title,resizeable) # Initialize the base class.
        
        if g.app.unitTesting: return
    
        self.text = text
        self.createTopFrame()
        self.top.bind("<Key>", self.onKey)
    
        if message:
            self.createMessageFrame(message)
    
        buttons = {"text":text,"command":self.okButton,"default":True}, # Singleton tuple.
        self.createButtons(buttons)
    #@-node:AGP.20250415230112.3149:class tkinterAskOk.__init__
    #@+node:AGP.20250415230112.3150:class tkinterAskOk.onKey
    def onKey(self,event):
        
        """Handle Key events in askOk dialogs."""
    
        ch = event.char.lower()
    
        if ch in (self.text[0].lower(),'\n','\r'):
            self.okButton()
    
        return "break"
    #@-node:AGP.20250415230112.3150:class tkinterAskOk.onKey
    #@-others
#@-node:AGP.20250415230112.3148:class tkinterAskOk
#@+node:AGP.20250415230112.3151:class tkinterAskOkCancelNumber
class  tkinterAskOkCancelNumber (leoTkinterDialog):
    
    """Create and run a modal Tkinter dialog to get a number."""
    
    #@    @+others
    #@+node:AGP.20250415230112.3152:tkinterAskOKCancelNumber.__init__
    def __init__ (self,c,title,message):
        
        """Create a number dialog"""
    
        leoTkinterDialog.__init__(self,c,title,resizeable=False) # Initialize the base class.
        
        if g.app.unitTesting: return
    
        self.answer = -1
        self.number_entry = None
    
        self.createTopFrame()
        self.top.bind("<Key>", self.onKey)
    
        self.createFrame(message)
        self.focus_widget = self.number_entry
    
        buttons = (
                {"text":"Ok",    "command":self.okButton,     "default":True},
                {"text":"Cancel","command":self.cancelButton} )
        buttonList = self.createButtons(buttons)
        self.ok_button = buttonList[0] # Override the default kind of Ok button.
    #@-node:AGP.20250415230112.3152:tkinterAskOKCancelNumber.__init__
    #@+node:AGP.20250415230112.3153:tkinterAskOKCancelNumber.createFrame
    def createFrame (self,message):
        
        """Create the frame for a number dialog."""
        
        if g.app.unitTesting: return
        
        c = self.c
        
        lab = Tk.Label(self.frame,text=message)
        lab.pack(pady=10,side="left")
        
        self.number_entry = t = Tk.Entry(self.frame,width=20)
        t.pack(side="left")
        
        c.set_focus(t)
    #@-node:AGP.20250415230112.3153:tkinterAskOKCancelNumber.createFrame
    #@+node:AGP.20250415230112.3154:tkinterAskOKCancelNumber.okButton, cancelButton
    def okButton(self):
        
        """Handle clicks in the ok button of a number dialog."""
    
        s = self.number_entry.get().strip()
    
        try:
            self.answer=int(s)
        except:
            self.answer=-1 # Cancel the operation.
    
        self.top.destroy()
        
    def cancelButton(self):
        
        """Handle clicks in the cancel button of a number dialog."""
    
        self.answer=-1
        self.top.destroy()
    #@-node:AGP.20250415230112.3154:tkinterAskOKCancelNumber.okButton, cancelButton
    #@+node:AGP.20250415230112.3155:tkinterAskOKCancelNumber.onKey
    def onKey (self,event):
        
        #@    << eliminate non-numbers >>
        #@+node:AGP.20250415230112.3156:<< eliminate non-numbers >>
        e = self.number_entry
        s = e.get().strip()
        
        i = 0
        while i < len(s):
            ch = s[i]
            if not ch.isdigit():
                e.delete(str(i))
                s = e.get()
            else:
                i += 1
        #@-node:AGP.20250415230112.3156:<< eliminate non-numbers >>
        #@nl
    
        ch = event.char.lower()
    
        if ch in ('o','\n','\r'):
            self.okButton()
        elif ch == 'c':
            self.cancelButton()
    
        return "break"
    #@-node:AGP.20250415230112.3155:tkinterAskOKCancelNumber.onKey
    #@-others
#@-node:AGP.20250415230112.3151:class tkinterAskOkCancelNumber
#@+node:AGP.20250415230112.3157:class tkinterAskYesNo
class tkinterAskYesNo (leoTkinterDialog):

    """A class that creates a Tkinter dialog with two buttons: Yes and No."""

    #@    @+others
    #@+node:AGP.20250415230112.3158:tkinterAskYesNo.__init__
    def __init__ (self,c,title,message=None,resizeable=False):
        
        """Create a dialog having yes and no buttons."""
    
        leoTkinterDialog.__init__(self,c,title,resizeable) # Initialize the base class.
        
        if g.app.unitTesting: return
    
        self.createTopFrame()
        self.top.bind("<Key>",self.onKey)
    
        if message:
            self.createMessageFrame(message)
            
        buttons = (
            {"text":"Yes","command":self.yesButton,  "default":True},
            {"text":"No", "command":self.noButton} )
        self.createButtons(buttons)
    #@-node:AGP.20250415230112.3158:tkinterAskYesNo.__init__
    #@+node:AGP.20250415230112.3159:tkinterAskYesNo.onKey
    def onKey(self,event):
        
        """Handle keystroke events in dialogs having yes and no buttons."""
    
        ch = event.char.lower()
    
        if ch in ('y','\n','\r'):
            self.yesButton()
        elif ch == 'n':
            self.noButton()
    
        return "break"
    #@-node:AGP.20250415230112.3159:tkinterAskYesNo.onKey
    #@-others
#@-node:AGP.20250415230112.3157:class tkinterAskYesNo
#@+node:AGP.20250415230112.3160:class tkinterAskYesNoCancel
class tkinterAskYesNoCancel(leoTkinterDialog):
    
    """A class to create and run Tkinter dialogs having three buttons.
    
    By default, these buttons are labeled Yes, No and Cancel."""
    
    #@    @+others
    #@+node:AGP.20250415230112.3161:askYesNoCancel.__init__
    def __init__ (self,c,title,
        message=None,
        yesMessage="Yes",
        noMessage="No",
        defaultButton="Yes",
        resizeable=False):
            
        """Create a dialog having three buttons."""
    
        leoTkinterDialog.__init__(self,c,title,resizeable,canClose=False) # Initialize the base class.
        
        if g.app.unitTesting: return
    
        self.yesMessage,self.noMessage = yesMessage,noMessage
        self.defaultButton = defaultButton
    
        self.createTopFrame()
        self.top.bind("<Key>",self.onKey)
    
        if message:
            self.createMessageFrame(message)
            
        buttons = (
            {"text":yesMessage,"command":self.yesButton,   "default":yesMessage==defaultButton},
            {"text":noMessage, "command":self.noButton,    "default":noMessage==defaultButton},
            {"text":"Cancel",  "command":self.cancelButton,"default":"Cancel"==defaultButton} )
        self.createButtons(buttons)
    #@-node:AGP.20250415230112.3161:askYesNoCancel.__init__
    #@+node:AGP.20250415230112.3162:askYesNoCancel.onKey
    def onKey(self,event):
        
        """Handle keystrokes in dialogs with three buttons."""
    
        ch = event.char.lower()
        
        if ch in ('\n','\r'):
            ch = self.defaultButton[0].lower()
    
        if ch == self.yesMessage[0].lower():
            self.yesButton()
        elif ch == self.noMessage[0].lower():
            self.noButton()
        elif ch == 'c':
            self.cancelButton()
    
        return "break"
    #@-node:AGP.20250415230112.3162:askYesNoCancel.onKey
    #@+node:AGP.20250415230112.3163:askYesNoCancel.noButton & yesButton
    def noButton(self):
        
        """Handle clicks in the 'no' (second) button in a dialog with three buttons."""
        
        self.answer=self.noMessage.lower()
        self.top.destroy()
        
    def yesButton(self):
        
        """Handle clicks in the 'yes' (first) button in a dialog with three buttons."""
        
        self.answer=self.yesMessage.lower()
        self.top.destroy()
    #@-node:AGP.20250415230112.3163:askYesNoCancel.noButton & yesButton
    #@-others
#@-node:AGP.20250415230112.3160:class tkinterAskYesNoCancel
#@+node:AGP.20250415230112.3164:class tkinterListboxDialog
class tkinterListBoxDialog (leoTkinterDialog):

    """A base class for Tkinter dialogs containing a Tk Listbox"""

    #@    @+others
    #@+node:AGP.20250415230112.3165:tkinterListboxDialog.__init__
    def __init__ (self,c,title,label):
        
        """Constructor for the base listboxDialog class."""
        
        leoTkinterDialog.__init__(self,c,title,resizeable=True) # Initialize the base class.
        
        if g.app.unitTesting: return
    
        self.createTopFrame()
        self.top.protocol("WM_DELETE_WINDOW", self.destroy)
    
        # Initialize common ivars.
        self.label = label
        self.positionList = []
        self.buttonFrame = None
        
        # Fill in the frame.
        self.createFrame()
        self.fillbox()
        
        # Make the common bindings after creating self.box.
        
        self.box.bind("<Double-Button-1>",self.go)
    #@-node:AGP.20250415230112.3165:tkinterListboxDialog.__init__
    #@+node:AGP.20250415230112.3166:addStdButtons
    def addStdButtons (self,frame):
        
        """Add stanadard buttons to a listBox dialog."""
        
        # Create the ok and cancel buttons.
        self.ok = ok = Tk.Button(frame,text="Go",width=6,command=self.go)
        self.hide = hide = Tk.Button(frame,text="Hide",width=6,command=self.hide)
    
        ok.pack(side="left",pady=2,padx=5)
        hide.pack(side="left",pady=2,padx=5)
    #@-node:AGP.20250415230112.3166:addStdButtons
    #@+node:AGP.20250415230112.3167:createFrame
    def createFrame(self):
        
        """Create the essentials of a listBoxDialog frame
        
        Subclasses will add buttons to self.buttonFrame"""
        
        if g.app.unitTesting: return
        
        self.outerFrame = f = Tk.Frame(self.frame)
        f.pack(expand=1,fill="both")
        
        if self.label:
            labf = Tk.Frame(f)
            labf.pack(pady=2)
            lab = Tk.Label(labf,text=self.label)
            lab.pack()
        
        f2 = Tk.Frame(f)
        f2.pack(expand=1,fill="both")
        
        self.box = box = Tk.Listbox(f2,height=20,width=30)
        box.pack(side="left",expand=1,fill="both")
        
        bar = Tk.Scrollbar(f2)
        bar.pack(side="left", fill="y")
        
        bar.config(command=box.yview)
        box.config(yscrollcommand=bar.set)
    #@-node:AGP.20250415230112.3167:createFrame
    #@+node:AGP.20250415230112.3168:destroy
    def destroy (self,event=None):
        
        """Hide, do not destroy, a listboxDialog window
        
        subclasses may override to really destroy the window"""
        
        self.top.withdraw() # Don't allow this window to be destroyed.
    #@-node:AGP.20250415230112.3168:destroy
    #@+node:AGP.20250415230112.3169:hide
    def hide (self):
        
        """Hide a list box dialog."""
        
        self.top.withdraw()
    #@-node:AGP.20250415230112.3169:hide
    #@+node:AGP.20250415230112.3170:fillbox
    def fillbox(self,event=None):
        
        """Fill a listbox from information.
        
        Overridden by subclasses"""
        
        pass
    #@-node:AGP.20250415230112.3170:fillbox
    #@+node:AGP.20250415230112.3171:go
    def go(self,event=None):
        
        """Handle clicks in the "go" button in a list box dialog."""
        
        c = self.c ; box = self.box
        
        # Work around an old Python bug.  Convert strings to ints.
        items = box.curselection()
        try:
            items = map(int, items)
        except ValueError: pass
    
        if items:
            n = items[0]
            p = self.positionList[n]
            c.beginUpdate()
            try:
                c.frame.tree.expandAllAncestors(p)
                c.selectPosition(p,updateBeadList=True)
                    # A case could be made for updateBeadList=False
            finally:
                c.endUpdate()
    #@-node:AGP.20250415230112.3171:go
    #@-others
#@-node:AGP.20250415230112.3164:class tkinterListboxDialog
#@-others
#@-node:AGP.20250415230112.3125:@thin leoTkinterDialog.py
#@-leo
