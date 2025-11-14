import tork

#from gl import glNewList,glEndList,glBegin,glEnd,glEnable,glDisable,glPushMatrix,glPopMatrix
#from gl import glTranslatef,glBlendFunc
#from gl import glTexRecti,draw_border,glCallString,glColor3f,glColor3ub,glRecti,glRectf
#from gl import control

tork.auto_import(tork,tork.gl)

import __main__,sys


_md_ = __main__.__dict__


LEFT = 0x40
HCENTER = 0x20
RIGHT = 0x10

TOP = 0x04
VCENTER = 0x02
BOTTOM = 0x01

LEFT_TOP = 0x44
LEFT_CENTER = 0x42
LEFT_BOTTOM = 0x41

CENTER_BOTTOM = 0x21
CENTER = 0x22
CENTER_TOP = 0x24

RIGHT_TOP = 0x14
RIGHT_CENTER = 0x12
RIGHT_BOTTOM = 0x11

last_anchor = LEFT_TOP
last_pos = vertex()

font_color = vertex()

def glRecti(x1,y1,x2,y2):
    glBegin(GL_QUADS)
    glVertex2i(x1,y1)
    glVertex2i(x2,y1)
    glVertex2i(x2,y2)
    glVertex2i(x1,y2)
    glEnd()
def glRectf(x1,y1,x2,y2):
    glBegin(GL_QUADS)
    glVertex2f(x1,y1)
    glVertex2f(x2,y1)
    glVertex2f(x2,y2)
    glVertex2f(x1,y2)
    glEnd()
def set_var(vardict,varname,value):
    attribs = varname.split(".")
    
    #var = __main__
    if len(attribs) == 1:
        vardict[attribs[0]] = value
    else:
        var = vardict[attribs.pop(0)]
        while len(attribs) > 1:
            var = getattr(var, attribs.pop(0))
    
        setattr(var, attribs[0], value)
def get_var(vardict,varname):    
    attribs = varname.split(".")
    
    var = vardict[attribs.pop(0)]
    
    for a in attribs:
        var = getattr(var, a)
    
    return var

class LABEL(pycontrol):
    def __init__( self, x, y, anchor, label, var=None,proc=None ,load=str,save=str ):
        pycontrol.__init__(self,x,y,anchor)
        
        self.font = _md_["default_font"]
        
        self.var = var
        self.name = self.label = label
        
        if proc != None:
            self.proc = proc
        else:
            self.proc = None
        
        if var != None:
            if not hasattr(_md_,var):
                _md_[var] = save("1")
        
        
        self.load = load
    
        #self.on_setup()
    def on_draw(self):
        f = self.font
        font_height = f.height
        label = self.label
        
        
        minx,miny,minz,minw = self.minimum()
        
        sh = font_height + 2
        sw = f.strlen(label)
        
        self.maximum(minx+sw,miny+sh,0,0)
        
        glPushMatrix()
        
        glTranslatef(minx,miny,0.0)
        
        back_color.color3()
        #glRecti(0,0,sw,sh)
        
        f.enable()
        glTranslatef(0,font_height,0)
        glColor3f(0.0,0.0,0.0)
        
        glCallString(label)
        if self.proc != None:
            glCallString(self.load(self.proc()))
        else:
            if self.var != None:
                glCallString(": "+self.load(_md_[self.var]))
        
        f.disable()
        
        glPopMatrix()
    def to_code(self):
        return self.var+" = "+str(_md_[self.var])
class BUTTON(pycontrol):
    def __init__(self,x,y,anchor=LEFT_TOP,label="",proc=None,dcproc=None,arg=None,w=None,h=None):
        pycontrol.__init__(self,x,y,anchor)
        
        f = self.font = _md_["default_font"]
        
        if type(label) == str:
            self.name = label
        elif proc != None:
            self.name = proc.__name__
        elif dcproc != None:
            self.name = dcproc.__name__
        
        self.label = label
        self.focus = False
        self.pressed = False
        self.enabled = True
        
        self.pressed_color = back_color    
        self.proc = proc
        self.dcproc = dcproc
        self.arg=arg
        
        self.width = w
        self.height= h
        
        
        self.setup()
    
    def on_mouse_out(self):
        
        if self.pressed == True:        
            self.pressed = False
            self.setup()
            
            self.front_draw()
    
    def on_setup(self):    
        minx,miny,minz,minw = self.minimum()
        label = self.label
        
        w = self.width
        h = self.height
        
        if type(label) == texture:
            label.bind()
            if w == None:
                w = label.get_int_level_param(0,GL_TEXTURE_WIDTH)       #cant be used inside GL_COMPILE
            if h == None:
                h = label.get_int_level_param(0,GL_TEXTURE_HEIGHT)
        
        glNewList(self.drawlist,GL_COMPILE)
        glPushMatrix()    
        
        glTranslatef(minx,miny,0.0)
        
        if type(label) == texture:  
            
            if self.enabled:
                if self.pressed:
                    self.pressed_color.color3()
                else:
                    glColor4f(1.0,1.0,1.0,1.0)
            else:
                glColor4f(1.0,1.0,1.0,0.1)
            
            label.enable()
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
            
            glTexRecti(w,h)
            
            label.disable()
            glDisable(GL_BLEND)
            
            draw_border(0,0,w,h,not self.pressed)
            
        elif type(label) == str:
            
            
            f = self.font
            label_len = f.strlen(label)
            
            if w == None:
                w = label_len + 20
                xtrans = 10
            else:
                xtrans = w/2 - label_len/2
            
            if h == None:
                h = f.height + 15
            
            
            
            back_color.color3()
            glRecti(0,0,w,h)
            draw_border(0,0,w,h,not self.pressed)
            f.enable()
            glTranslatef(xtrans,f.height+((h-f.height)/2)-3,0)        
            
            fr,fg,fb,fa = font_color()
            
            if self.enabled:
                fa = 1.0
            else:
                fa = 1.0
            glColor4f(fr,fg,fb,fa)
            
            glCallString(label)   
            f.disable()
        
        glPopMatrix()   
        glEndList()
        self.maximum(minx+w,miny+h,0,0)
        #--------------------------------------------------
        glNewList(self.selectlist,GL_COMPILE)
        glPushMatrix()
        glTranslatef(minx,miny,0.0)
        glRecti(0,0,w,h)
        glPopMatrix()
        glEndList()
        
        
    
    def on_mouse_down(self,x,y,button):
        if not self.enabled or self.proc==None:
            return
        
        self.pressed = True
        self.setup()
        
        self.front_draw()
    def on_mouse_up(self,x,y,button):
        if not self.enabled or self.proc == None:
            return
        
        if self.pressed == True:        
            self.pressed = False
            self.setup()
            self.front_draw()
            if self.proc != None:
                if self.arg != None:
                    self.proc(self.arg)
                else:
                    self.proc()
        
    def on_mouse_double_click(self,x,y,button):
        if not self.enabled or self.dcproc == None:
            return
        
        if self.arg != None:
            self.dcproc(self.arg)
        else:
            self.dcproc()
    

class TBUTTON(pycontrol):
    def __init__(self,x,y,anchor=LEFT_TOP,label="",toggle_on=None,toggle_off=None,w=None,h=None):
        
        pycontrol.__init__(self,x,y,anchor)
        f = self.font = _md_["default_font"]
        
        
        
        self.label = label
        self.pressed = False
        self.enabled = True
        self.pressed_color = back_color    
        
        
        if toggle_on !=None:
            self.toggle_on = toggle_on
        
        if toggle_off !=None:
            self.toggle_off = toggle_off
        
        
        self.width = w
        self.height= h
        
    
        #self.setup()
    def toggle_on(self):
        return True
    def toggle_off(self):
        return True
    def on_setup(self):    
        minx,miny,minz,minw = self.minimum()
        label = self.label
        
        w = self.width
        h = self.height
        
        if type(label) == texture:
            label.bind()
            if w == None:
                w = label.get_int_level_param(0,GL_TEXTURE_WIDTH)       #cant be used inside GL_COMPILE
            if h == None:
                h = label.get_int_level_param(0,GL_TEXTURE_HEIGHT)
        
        glNewList(self.drawlist,GL_COMPILE)
        glPushMatrix()    
        
        glTranslatef(minx,miny,0.0)
        
        if type(label) == texture:  
            
            if self.enabled:
                if self.pressed:
                    self.pressed_color.color3()
                else:
                    glColor4f(1.0,1.0,1.0,1.0)
            else:
                glColor4f(1.0,1.0,1.0,0.1)
            
            label.enable()
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
            
            glTexRecti(w,h)
            
            label.disable()
            glDisable(GL_BLEND)
            
            draw_border(0,0,w,h,not self.pressed)
            
        elif type(label) == str:
            
            
            f = self.font
            label_len = f.strlen(label)
            
            if w == None:
                w = label_len + 20
                xtrans = 10
            else:
                xtrans = w/2 - label_len/2
            
            if h == None:
                h = f.height + 15
            
            
            
            back_color.color3()
            glRecti(0,0,w,h)
            draw_border(0,0,w,h,not self.pressed)
            f.enable()
            glTranslatef(xtrans,f.height+((h-f.height)/2)-3,0)        
            
            fr,fg,fb,fa = font_color()
            
            if self.enabled:
                fa = 1.0
            else:
                fa = 1.0
            glColor4f(fr,fg,fb,fa)
            
            glCallString(label)   
            f.disable()
        
        glPopMatrix()   
        glEndList()
        self.maximum(minx+w,miny+h,0,0)
        #--------------------------------------------------
        glNewList(self.selectlist,GL_COMPILE)
        glPushMatrix()
        glTranslatef(minx,miny,0.0)
        glRecti(0,0,w,h)
        glPopMatrix()
        glEndList()
        
        
    
    def on_mouse_down(self,x,y,button):
        if not self.enabled:
            return
        
        if self.pressed:
            self.pressed = not self.toggle_off()
        else:
            self.pressed = self.toggle_on()
            
        self.setup()
        #self.front_draw()
        current_warp().paint()
Checkboxes = []
class CHECKBOX(pycontrol):
    def __init__(self,x,y,anchor=LEFT_TOP,var="",gid=0):
        pycontrol.__init__(self,x,y,anchor)
        
        self.font = _md_["default_font"]
        self.vardict = _md_
        
        Checkboxes.append(self)
        
        self.pressed = False
        self.enabled = True
        self.GroupeID = gid
        self.allow_empty_groupe = True
        
        
        #self.load = bool 
        
        
        
        self.var = var
        self.label = var.replace("_"," ").title()
        self.name = var.replace(".","_")
        
        #if not hasattr(_md_,var):
        #    _md_[var] = True
        
        
        self.focus = False
        
        
        #self.setup()
    def set_value(self,value,force=False):
        vd,var = self.vardict,self.var
        
        old_value = get_var(vd,var)
           
        if value == True:
            if self.GroupeID != 0:
                for c in Checkboxes:
                    if c != self and c.GroupeID == self.GroupeID:
                        c.set_value(False,True)
            
            set_var(vd,var,True)
        
        else:
            if self.GroupeID == 0 or force:
                set_var(vd,var,False)
                
        if old_value != get_var(vd,var):   
            self.on_change() 
            self.setup()
    
    
    def on_setup(self):  
        minx,miny,minz,minw = self.minimum.get()
        
        glNewList(self.drawlist,GL_COMPILE)
        glPushMatrix()
        glTranslatef(minx,miny,0.0)
        
        f = self.font
        fh = f.height
        label = self.label
        label_len = f.strlen(label)
        
        sw = label_len+fh+5
        sh = fh + 10
        
        maxx = minx+sw
        maxy = miny+sh
        
        back_color.color3()
        glRecti(0,0,sw,sh)
        
        glColor3f(1.0,1.0,1.0)
        glRecti(2,3,fh-3,fh-3)
        
        
        if self.enabled:
            glColor3f(0.0,0.0,0.0)
        else:
            glColor3f(0.4,0.4,0.4)
        
        if get_var(self.vardict,self.var) == True:
            glRecti(4,5,fh-5,fh-5)    
        
        f.enable()
        glTranslatef(fh+4,fh-2,0)
        glCallString(self.label)   
        f.disable()
        
        draw_border(0,2,fh-2,fh-1,0)
        
        glPopMatrix()
        
        glEndList()    
        #--------------------------------------------------
        glNewList(self.selectlist,GL_COMPILE)
        glRectf(minx,miny,maxx,maxy)
        glEndList()
        
        self.maximum(maxx,maxy,0,0)
    
    def on_mouse_up(self,x,y,button):
        
        if not self.enabled:
            return
            
        if not self.pressed:
            return
        
        
        if get_var(self.vardict,self.var) == True:
            print "mugv"
            if self.GroupeID == 0:        
                self.set_value(False)    
        else:
            print get_var(self.vardict,self.var),"mungv",self.GroupeID
            #self.set_value(True)
            self.set_value(True,True)
        
        self.pressed = False
        
        self.front_draw()
    
    def on_mouse_down(self,x,y,button):
        self.pressed = True
    def xon_mouse_move(self,x,y):
        self.pressed = False
    
    def on_mouse_out(self):
        self.pressed = False
    
    
    def on_change(self):
        pass

#creating a static member create a reference loop and entry wont be deleted at termination,
#also entry wont be deleted at runtime unless they are removed from the list!
Entries = [] 


class ENTRY(pycontrol):
    def __init__(self,x,y,anchor,var,w=200,save=str,load=str,label=None,add=None):
        pycontrol.__init__(self,x,y,anchor)    
        self.font = _md_["default_font"]
        self.vardict = _md_
            
        self.enabled = True
        self.pressed = False
        self.back_color = vertex(1.0,1.0,1.0,1.0)
        self.focus_color = vertex(0.7,0.7,0.9,1.0)
        
        self.focus = False
        self.modified = False    
        
        Entries.append(self)
        
        self.width = w
        
        #if code == None:
        #    self.code = load
        #else:
        #    self.code = code
        
        self.var = var
        self.name = var.replace(".","_") + "_entry"
        
        self.load = load
        self.save = save
        if label == None:
            self.label = var.replace("_"," ").replace("."," ").title()+": "
        else:
            self.label = label
        
        #self.get_var()
        
        #self.on_setup()
    def set_value(self,v=None):
        if v != None:
            self.text = v
        
        set_var(self.vardict,self.var,self.save(self.text))
    def get_value(self):    
        self.text = self.load(get_var(self.vardict,self.var))
        return self.text
    def on_setup(self):
        f = self.font    
        minx,miny,minz,minw = self.minimum()
        
        sw = self.width
        sh = f.height + 6
        
        label_len = f.strlen(self.label)
        self.box_width = sw - label_len
        
        
        if self.modified != True:
            self.get_value()
        
        text_len = f.strlen(self.text)
        self.maximum(minx+sw,miny+sh,0,0)
        
        
        #----------------------------------
        glNewList(self.drawlist,GL_COMPILE)
        glPushMatrix()
        
        glTranslatef(minx,miny,0.0)
        
        
        
        if self.focus:
            mid_color.color3()
        else:            
            back_color.color3()
        
        
        
        glRecti(label_len+1,1,sw-1,sh-1)
        draw_border(label_len,0,sw,sh,0)    
        
        f.enable()
        glTranslatef(0,f.height,0)
        
        if self.enabled:
            font_color.color3()
            #glColor3f(0.0,0.0,0.0)
        else:
            mid_color.color3()
            #glColor3f(0.4,0.4,0.4)
        
        glCallString(self.label)   
        
        glTranslatef(self.box_width-text_len-4,0,0)
        
        glCallString(self.text)
        f.disable()
        
        glPopMatrix()
        glEndList()    
        
        #--------------------------------------------------
        glNewList(self.selectlist,GL_COMPILE)
        glPushMatrix()
        glTranslatef(minx,miny,0.0)
        glRecti(0,0,sw,sh)
        glPopMatrix()
        glEndList()
    def on_mouse_down(self,x,y,button):
        if not self.enabled:
            return
            
        self.pressed = True
            
        current_warp().key_target = self
    def on_mouse_double_click(self,x,y,button):
        if not self.enabled:
            return
            
        current_warp().key_target = self
        self.keypad()
    def on_mouse_up(self,x,y,button):
        if not self.enabled:
            return
        
        if self.pressed == True:        
            self.pressed = False
            
        
    def on_char(self,char):
        if not self.enabled:
            return
            
        co = ord(char)
        
        if not self.accept_char(char):
            return
        
        if 31 < co and co < 255 and co != 127:
            text = self.text
            if self.font.strlen(text) < (self.box_width-6):
                #print char
                self.text = text + char
                self.modified = True
                self.setup()
                current_warp().redraw()
    def on_key_down(self,key):
        if not self.enabled:
            return
        text = self.text
        if key == TK_BACK:
            if len(text) > 0:
                self.text = text[:-1]
                self.modified = True
                self.setup()
                current_warp().redraw()
                
        if key == TK_DELETE:
            if len(text) > 0:
                self.text = ""
                self.modified = True
                self.setup()
                current_warp().redraw()
                
        if key == TK_RETURN:
            self.set_value()
            #self.get_value()
            
            
            #current_warp().key_target = None
            self.modified = False
            #self.setup()
            self.on_change()
            
            current_warp().redraw()
    def on_key_in(self):
        self.focus = True
        self.on_setup()
        current_warp().redraw()
    def on_key_out(self):
        if self.modified:
            self.set_value()
            self.get_value()
            self.modified = False
        self.focus = False
        self.on_setup()
        
        current_warp().redraw()
    def on_change(self):
        pass
        #self.setup()
        #self.front_draw()
        #print "on_change"
    def keypad(self):
        pass
        #self.setup()
        #self.front_draw()
        #print "on_change"
    def accept_char(self,char):
        return True
class EDIT(pycontrol):
    def __init__(self,lines,left=0,top=0):
        pycontrol.__init__(self)
        #self.classname = "EDIT"    
        self.font = _md_["default_font"]
        
        self.text_list = glGenLists(1)
        self.sel_list = glGenLists(1)
        self.lines_sel_list = glGenLists(1)
        self.left = left
        self.top = top
        self.minimum(left,top,0,0)
        
        self.lines = lines
        
        self.focus = False
        self.text_color = vertex(0.0,0.0,0.0,0.0)
        
        self.caret_row = 0
        self.caret_col = 0
        self.sel_row = -1
        self.sel_col = -1
        self.row = -1
        self.col = -1
        
        self.sel_offset = 2
        self.caret_width = 2
        
        self.selecting = False
        self.show_caret = True
        
        #self.selection = selection()
        
        self.setup()
    
    def sel_range(self):    
        start_row = caret_row = self.caret_row
        start_col = caret_col = self.caret_col
        end_row = sel_row = self.sel_row
        end_col = sel_col = self.sel_col
        
        if sel_row > -1 and caret_row > sel_row:
    	    start_row = sel_row;
            start_col = sel_col;
    	    end_row = caret_row;
            end_col = caret_col;
    
    
        if sel_col > -1 and caret_col > sel_col and caret_row == sel_row:
            start_col = sel_col;
            end_col = caret_col;
            
        return (start_row, start_col, end_row, end_col)
    def list_text(self):
        f = self.font
        nl = f.listbase+10
        lh = f.height + f.line_spacing
        ls = f.line_spacing
        self.minimum(self.left,self.top,0.0,0.0)
        self.maximum.zero()
        
    
        glNewList(self.text_list,GL_COMPILE)
        #----------------------------------
        f.enable()
        #glCallList(nl)
        glPopMatrix()
        glTranslatef(0.0,f.height,0.0)
        glPushMatrix()
        
        self.text_color.color3()
        xborder = self.left
        yborder = self.top+lh/2
        i = 1
        
        for line in self.lines:
            tv = vertex(xborder+f.strlen(line),yborder+i*lh,0,0)
            self.eval_minmax(tv)
            glCallString(line)
            glCallList(nl)
            i += 1
        
        f.disable()
        #----------------------------------
        glEndList()
    def list_sel(self):
        start_row, start_col, end_row, end_col = self.sel_range()
    
        
        rownum = end_row - start_row
        colnum = end_col - start_col
    
        f = self.font
        lh = f.height + f.line_spacing
        lines = self.lines
        glNewList(self.sel_list,GL_COMPILE)
        #------------------------
        #glTranslatef(0,self.sel_offset,0)
        f.enable_geometry();
    
        nl = f.listbase + 10
        slen = 0
    
        glEnable(GL_BLEND)
        glBlendFunc(GL_ONE_MINUS_DST_COLOR,GL_ZERO)
    
        #glCallList(nl)
        glColor3f(0.7,0.7,0.7)
        if end_col > -1:
            #--preselection    
            i = 0;
            while i < start_row:
                glCallList(nl)
                i += 1
        
            if start_col > 0:
                slen = f.strlen(lines[i][:start_col-1])
                glTranslatef(slen,0,0)
        
            #----selection
            sx = 0;
            ec = end_col;
            tlen = len(lines[end_row])
            if end_col > tlen:
                end_col = tlen
        
            if self.caret_col == start_col and start_row == self.caret_row:
                sx = self.caret_width
                self.draw_caret()
                glColor3f(0.7,0.7,0.7)
        
            if start_row != end_row:
                glRecti(sx,0,f.strlen(self.lines[i][:start_col]),lh)
                glCallList(nl)
                i+=1
            
                while i < end_row:
                    glRecti(0,0,f.strlen(self.lines[i]),lh)
                    glCallList(nl)
                    i+=1
            
                if end_col > 0:
                    slen = f.strlen(lines[i][:end_col-1])
                    glRecti(0,0,slen,lh)
                    glTranslatef(slen,0,0)           
    
                if self.caret_col == end_col:
                    self.draw_caret()
            else:
                if end_col > 0:
                    slen = f.strlen(lines[i][start_col:end_col-1])
                    glRecti(sx,0,slen,lh)
                    glTranslatef(slen,0,0)
    
                if self.caret_col == end_col:
                    self.draw_caret()
    
        else:
            #print "endcol == -1"
            i = 0
            while i < self.caret_row:
                glCallList(nl)
                i+=1
            
            if self.caret_col > 0:
                slen = f.strlen(lines[i][0:self.caret_col])
                glTranslatef(slen,0,0)
            #print "draw_caret"
            self.draw_caret()
    
        glDisable(GL_BLEND)
        f.disable_geometry()
        #------------------------
        glEndList()
    def draw_caret(self):
        if self.show_caret:
            #glBlendFunc(GL_ONE_MINUS_DST_COLOR,GL_ONE)
            glColor3f(1.0,0.0,0.0)
            glRecti(0,0,self.caret_width, self.font.height)
            #glBlendFunc(GL_ONE_MINUS_DST_COLOR,GL_ZERO)
    def on_setup(self):
        self.list_text()
        self.list_sel()
        
        xborder = 2
        yborder = 2
        
        f = self.font
        fh = f.line_spacing + f.height
        nl = f.listbase+10
        
        #--------------------------------------------
        min = self.minimum
        max = self.maximum
        
        glNewList(self.drawlist,GL_COMPILE)
        
        glPushMatrix()
        glColor3ub(255,255,255)
        glRectf(0,0,10000,10000)#max.x,max.y)
        glTranslatef(self.left,self.top,0)
        glCallList(self.text_list)
        glCallList(self.sel_list)       	
        glPopMatrix()
        glEndList()
    
        #---------------------------------------------
        glNewList(self.selectlist,GL_COMPILE)
        glRecti(0,0,100000,100000)
        glEndList()
    
        #---------------------------------------------
        
        glNewList(self.lines_sel_list,GL_COMPILE)
        #glPushMatrix()
        #glTranslatef(0,self.sel_offset,0)
        f.enable_geometry()
    
        #glCallList(nl)
        glPopMatrix()
        glTranslatef(0.0,f.height,0.0)
        glPushMatrix()
        
        for i in range(len(self.lines)):
            #glLoadName(i)
            glRecti(0,0,10000,-fh)
            glCallList(nl)
    
        f.disable_geometry()
        #glPopMatrix()
        glEndList()
        
    def xon_select_target(self,x,y):    
        
        port = self.parent.as_viewport()
        glClear(GL_COLOR_BUFFER_BIT)
        
        port.push()
        
        
        glTranslatef(self.left,self.top,0)    
        
        f = self.font
        f.enable_geometry()
        #f.enable()
        #glListBase(f.listbase)
        #glPopMatrix()
        
        #glLoadIdentity()
        glPushMatrix()
        #glScalef(1.0,-1.0,1.0)
        glTranslatef(0.0,f.height+f.line_spacing,0.0)
        glTranslatef(self.left,self.top,0)    
        
        glPushMatrix()
        
        
        glColor4ub(255,255,0,0)
        glRecti(10,100,1000,100)
        
        lines = self.lines
        for i in range(len(lines)):
            line = lines[i]
            glColor4ub(i,255,0,0)
            glRecti(0,0,10000,-f.height)
            for j in range(len(line)):
                glColor4ub(i,j,255,0)
                glCallString(line[j])
                #glRecti(i,j,10,-10)
            #glCallString("\n")
            glCallList(f.listbase+10)
        f.disable_geometry()
        #f.disable()
        glPopMatrix()
        glPopMatrix()
        port.pop()
        sel = glReadPixel(x,y)
        
        self.row = sel & 0xFF
        self.col = (sel & 0xFF00) >> 8
        #print f.listbase
        print self.row,self.col
        return self
    def sub_select(self,x,y):
        port = self.parent.as_viewport()
        glClear(GL_COLOR_BUFFER_BIT)
        
        port.push()
        
        
        glTranslatef(self.left,self.top,0)    
        
        f = self.font
        f.enable_geometry()
        
        glPushMatrix()
        glTranslatef(0.0,f.height+f.line_spacing,0.0)
        glTranslatef(self.left,self.top,0)    
        glPushMatrix()
        
        
        glColor4ub(255,255,0,0)
        glRecti(10,100,1000,100)
        
        lines = self.lines
        
        
        for i in range(len(lines)):
            line = lines[i]
            glColor4ub(i,255,0,0)
            glRecti(0,0,10000,-f.height)
            glCallList(f.listbase+10)
        
        sel = glReadPixel(x,y)
        self.row = sel & 0xFF
        
        ################################
        
        
        for i in range(len(lines)):
            line = lines[i]
            glColor4ub(i,255,0,0)
            glRecti(0,0,10000,-f.height)
            for j in range(len(line)):
                glColor4ub(i,j,255,0)
                glCallString(line[j])
                #glRecti(i,j,10,-10)
            #glCallString("\n")
            glCallList(f.listbase+10)
        f.disable_geometry()
        #f.disable()
        glPopMatrix()
        glPopMatrix()
        port.pop()
        
        
        self.row = sel & 0xFF
        self.col = (sel & 0xFF00) >> 8
        #print f.listbase
        print self.row,self.col
        return self
    def select_chars(self):
        selection = self.selection
        #print self.sel_row
        if self.row > -1 and len(self.lines) > 0:
            f = self.font   
            fh = f.line_spacing + f.height
            nl = f.listbase + 10
        
            selection.begin()
            
            glTranslatef(-2,0,0)
            f.enable_geometry()
            glCallList(nl)
            
            for i in range(self.row):
                glCallList(nl)
            
            s = self.lines[self.row]
            #print s
            slen = len(s)
            
            glLoadName(0);
            glRecti(-10,0,0,fh)
            for i in range(slen):
                glLoadName(i)
                glCallString(s[i])
    	        
            f.disable_geometry()
            glTranslatef(2,0,0);
    
    
            hits = selection.end()
            #print "hits",hits
            if hits != None:
                self.col = hits[0][2][0]
                #print self.col
            else:
                self.col = slen
    def select_lines(self):
        nl = self.font.listbase + 10
        self.selection = selection = self.parent.as_viewport().selection
        
        selection.begin()
        glCallList(self.lines_sel_list)    
        hits = selection.end()
        #print "line_hits",hits
        if hits != None:
            self.row = hits[0][2][0]
        else:
            self.row = -1
    def on_mouse_in(self):
        current_warp().cursor = TC_BEAM
    def on_mouse_out(self):
        current_warp().cursor = TC_ARROW;
    def xon_mouse_down(self,x,y,button):
        w = current_warp()
        w.capture_mouse(self)
        w.key_target = self
    
        self.selecting = True
    
        self.sub_select(x,y)
    
        self.caret_row = self.row
        #print "col",self.col
        self.caret_col = self.col
        self.sel_row = self.sel_col = -1
    
        self.list_sel()
        w.redraw()
    def xon_mouse_up(self,x,y,button):
        w = current_warp()
        w.release_mouse()
        self.selecting = False
    def xon_mouse_move(self,x,y):
        #print "mousemove"
        #print self.selecting
        if self.selecting == True:
    	    self.sub_select(x,y)
        
            if self.sel_row == self.caret_row and self.col == self.caret_col:
                if self.sel_col == 0:
                    pass
                #SelCol = SelRow = -1;
            else:
                if self.col == -1 and self.row == -1:
                    self.sel_col = self.caret_col
                    self.sel_row = self.caret_row
              
        
            if self.row == self.sel_row and self.col == self.sel_col:
                self.col = self.row = -1
        
            self.caret_row = self.sel_row
            self.caret_col = self.sel_col
        
            self.list_sel()
            current_warp().redraw()
    def load(self,text):
        self.lines = text.splitlines()
        self.caret_col = self.caret_row = 0
        self.sel_col = self.sel_row = -1
        self.on_setup()
        self.on_change()
    def delete_sel(self):
        start_row, start_col, end_row, end_col = self.sel_range()
        rownum = end_row - start_row;
        
        lines = self.lines
    
        if rownum == 0:
            if start_col == 0:
                if end_col == len(lines[start_row]):
                    del lines[start_row]
                else:
                    lines[start_row] = lines[start_row][:endcol]
            else:   
                lines[start_row] = lines[start_row][:start_col-1] + lines[start_row][end_row:]
        else:
            if start_col == 0:
                del lines[start_row+1]
            else:
                lines[start_row] = lines[start_row][:start_col-1]
    
            del lines[start_row+1:start_row+rownum]
        
            if end_col < len(lines[start_row+1]):
                lines[start_row] = lines[start_row][end_col:]
            
            del lines[start_row+1]
    
        self.caret_col = start_col
        self.caret_row = start_row
        self.sel_col = -1
        self.sel_row = -1
    
        self.on_setup()
        self.on_change()
    def delete(self):
        lines = self.lines
        if self.sel_row > -1:
            self.delete_sel()
        else:
            if self.caret_col == len(lines[caret_row]):
                if self.caret_row+1 < len(lines):
                    lines[self.caret_row] += lines[self.caret_row+1]
                    del lines[self.caret_row+1]
            elif self.caret_col == 0:
                lines[self.caret_row] = lines[self.caret_row][1:]
            else:
                lines[self.caret_row] = lines[self.caret_row][1:self.caret_col-1] + lines[self.caret_row][self.caret_col+1:]
        
        self.on_setup()
        self.on_change()
    def backspace(self):
        lines = self.lines
        if self.sel_col > -1:
            self.delete_sel()
        else:
            if self.caret_col == 0:
                if self.caret_row > 0:
                    self.caret_col = len(lines[self.caret_row-1]);
                    lines[self.caret_row-1] = lines[self.caret_row-1] + lines[self.caret_row]
                    del lines[caret_row]
                    self.caret_row -= 1
    
            elif self.caret_col == len(lines[self.caret_row]):
                if self.caret_col == 1:
                    lines[self.caret_row] = ""
                else:
                    lines[self.caret_row] = lines[self.caret_row][:-2]
                self.caret_col -= 1
            else:
                if self.caret_col > 1:
                    lines[self.caret_row] = lines[self.caret_row][:self.caret_col-2] + lines[self.caret_row][self.caret_col:]
                else:
                    lines[self.caret_row] = lines[self.caret_row][self.caret_col:]
                self.caret_col -= 1
    
        self.on_setup()
        self.on_change()
    def newline(self):
        if self.sel_row > -1:
            self.delete_sel()
        
        lines = self.lines
        if len(lines) ==0:
            lines.append("")
            lines.append("")
        elif self.caret_col == 0:
            lines.insert(self.caret_row, "")
            self.caret_row += 1
        elif self.caret_col == len(lines[self.caret_row]):
            lines.insert(self.caret_row+1, "")
            self.caret_row += 1
            self.caret_col = 0;
        else:        
            ts = lines[self.caret_row][:self.caret_col]
            lines.insert(self.caret_row+1,lines[self.caret_row][self.caret_col:])
            lines[self.caret_row] = lines[self.caret_row][:self.caret_col-1]
            self.caret_col = 0
            self.caret_row += 1
            
        self.on_setup()
        self.on_change()
    def insert(self,text):
        if self.sel_row > -1:
            self.delete_sel()
        
        lines = self.lines
        
        if len(lines == 0):
            lines.append("")
        
        tlines = text.splitlines()
    
        if len(tlines) > 0:
            if self.caret_col == 0: #prepend
                i = 0
                while i < len(tlines)-1:
                    lines.insert(self.caret_row,tlines[i])
                    i += 1
                    self.caret_row += 1
    
                if i < len(tlines):
                    self.caret_col = len(tlines[i])
                    s = tlines[i]
                    if len(lines[self.caret_row]) > 0:
                        s += lines[self.caret_row]
                    lines[self.caret_row] = s
            elif self.caret_col == len(lines[self.caret_row]):
                i = 0
                lines[self.caret_row] += tlines[i];#append
                i += 1
                self.caret_col = len(lines[self.caret_row])
            
                while i < len(tlines):
                    self.caret_row += 1
                    self.caret_col = len(tlines[i])
                    lines.insert(self.caret_row,tlines[i])
                    i += 1
            else:
                ts = lines[self.caret_row]
                lines[self.caret_row] = lines[self.caret_row][:self.caret_col-1]        
            
                lines[self.caret_row] += tlines[0]
                slen = len(lines[self.caret_row])
            
                for i in range(len(tkines)):
                    lines.insert(self.caret_row+1,tlines[i])         
                    self.caret_row += 1
                    slen = len(lines[self.caret_row])
            
                lines[self.caret_row] += ts[:self.caret_col]
                self.caret_col = slen;
        
    
        self.on_setup()
        self.on_change()
    def copy(self):
        if self.sel_col > -1:
            current_warp().clipboard = self.get_selection()
    def cut(self):
        if self.sel_col > -1:
            current_warp().clipboard = self.get_selection()
            self.delete_sel()
    def paste(self):
        self.insert(current_warp().clipboard)
    max_x = 0
    max_y = 0
class POPMENU(pycontrol):
    PopMenu = None
    def __init__(self,left,top,w):
        pycontrol.__init__(self)
        #self.classname = "POPMENU"
        self.font = _md_["default_font"]
        self.left = left
        self.top = top
        
        self.width = w
        
        self.items = []
        
        self.target = self.old_target = -1
        
        self.x_margin = 6
        self.y_margin = 6
        
        self.minimum(0,0,0,0)
        self.maximum(20,20,0,0)
        
        self.on_destroy = None
        self.destroy_data = None
        
        w = current_warp()
        v = w.viewport
        i = 0
        c = v.controls(i)
        while c != None:
            if c.classname == "POPMENU":
                w.remove(c)
                break
            c = v.controls(i)
            i += 1
        
        w.add(self)
        self.PopMenu = self 
    
        current_warp().swap_target(self)
        #current_warp().paint()
    def add_item(self,label,proc=None,data=None,enabled=True):
        self.items.append((label,proc,data,enabled))
        self.eval_minmax(vertex(self.font.strlen(label)+self.x_margin*2, len(self.items)*(self.font.height+self.y_margin)+2*self.y_margin ,0,0))
    def destroy(self):
        try:
            w = current_warp()
            w.remove(self)
            self.PopMenu = None
            if self.on_destroy != None:
                self.on_destroy(self.destroy_data)
            
            w.redraw()
        except Exception, e:
            print "destroy()",e
    def on_draw(self):
        glPushMatrix();
        
        minx,miny,minz,minw = self.minimum.get()
        maxx,maxy,maxz,maxw = self.maximum.get()
        font = self.font
        fh = font.height
        items = self.items
        xmarg = self.x_margin
        ymarg = self.y_margin
        
        glTranslatef(self.left,self.top,0)
        back_color.color3()
        glRectf(0.0,0.0,maxx,maxy)    
        draw_border(0,0,int(maxx),int(maxy),1)
        #print self.minimum,self.maximum
        glTranslatef(xmarg,ymarg,0)
        for i in range(len(items)):
            
            label,proc,data,enabled = items[i]
            if self.target == i:
                mid_color.color3()
                glRectf(0,2,maxx-2*xmarg,fh+2)
                if enabled == True:
                    back_color.color3()
                else:
                    glColor3ub(0,0,0)
            else:
                if enabled == True:
                    glColor3ub(0,0,0)
                else:
                    mid_color.color3()
            glTranslatef(0,fh,0)
            font.enable()
            glCallString(label)  
            font.disable()
            glTranslatef(0,ymarg,0)
    
        glPopMatrix();
    
    
    
    def on_select(self):
        
        
        #minx,miny,minz,minw = self.minimum.get()
        maxx,maxy,maxz,maxw = self.maximum.get()
        
        
        glRectf(self.left,self.top,self.left+maxx,self.top+maxy)
        
    def on_select_target(self,x,y):
        
        glPushMatrix();
        
        minx,miny,minz,minw = self.minimum.get()
        maxx,maxy,maxz,maxw = self.maximum.get()
        font = self.font
        fh = font.height
        items = self.items
        xmarg = self.x_margin
        ymarg = self.y_margin
        
        glTranslatef(self.left+xmarg,self.top+ymarg,0)
        for i in range(len(self.items)):
            glColor4ub(i,255,0,0)
            #glRectf(-2,0,maxx-xmarg-1,fh+ymarg*2)
            glRectf(0,2,maxx-2*xmarg,fh+2)
            glTranslatef(0,fh+ymarg,0)
    
        glPopMatrix();
        
        self.target = glReadPixel(x,y) & 0xFF    
        
        
        
        return self
    def on_mouse_out(self):
        self.destroy()
    def on_mouse_down(self,x,y,button):
        t = self.target
        if t > -1:
            label,proc,data,enabled = self.items[t]
            if enabled == True:
                if proc != None:
                    proc(data)
            else:
                return
        current_warp().swap_target(None)
        #self.destroy()
    def on_mouse_move(self,x,y):
        if self.target != self.old_target:
            current_warp().redraw()
            self.old_target = self.target
class PANTOOL(pycontrol):
    def __init__(self,vport):
        pycontrol.__init__(self)
        
        #self.vport = vport
        
        self.trans = vertex()
        self.mintrans = vertex()
        self.maxtrans = vertex()
        
        
        self.start = vertex()
        self.panning = False
    
    def on_setup(self):
        #self.parent.tool = self
        self.scan_port()
    def scan_port(self):
        #print "scan1",self.trans_y
        self.minimum(0,0,0,0)
        self.maximum(0,0,0,0)
        
        
        vport = self.parent
        for obj in vport.objects:
            if(obj != self):
                #print obj.minimum,obj.maximum
                self.eval_minmax(obj.minimum)
                self.eval_minmax(obj.maximum)
        
        #self.minimum -= vertex(10,10,0,0)
        #self.maximum += vertex(10,10,0,0)
        
        pl,pt,pw,ph = vport.rect
        ph -= 4
        pw -= 4
        
        port_min = vertex()
        port_max = vertex(pw,ph,0.0,0.0)
        
        zv = vertex()
        
        mt = zv - self.minimum
        self.maxtrans = mt & (mt.gt(zv))
        mt = port_max - self.maximum
        mt.y -= 45
        self.mintrans = mt & (mt.lt(zv))
        
        #print self.minimum
        #print self.maximum
        #print self.mintrans
        #print self.maxtrans
        
    
    def apply(self):
        vport = self.parent
        
        self.trans.max(self.mintrans)
        self.trans.min(self.maxtrans)
        
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        glScalef(1,-1,1)
        glTranslatef(self.trans.x,self.trans.y,0)
        vport.modelview.get_modelview()
        glPopMatrix()
        
        vport.setup()
    
    def pan_up(self):
        self.scan_port()
        self.trans.y = 0
        self.apply()
        #current_warp().redraw()
    
    def pan_down(self):
        self.scan_port()
        self.trans_y = self.maxtrans_y
        self.apply()
        #current_warp().redraw()
    
    def on_resize(self,w,h):
        self.scan_port()
        self.apply()
    def on_mouse_down(self,x,y,button):
        #print "scroll mouse down"
        if button == TM_LBUTTON:
            current_warp().capture_mouse(self);
            self.panning = True;
            self.start(x,y,0,0)
    def on_mouse_move(self,x,y):
        
        if self.panning:
            self.trans += vertex(x,y) - self.start
            self.start(x,y)
            self.apply()
            self.parent.front_draw()
    def on_mouse_up(self,x,y,button):
        self.panning=False
        current_warp().release_mouse()
class SPLITTER(pycontrol):
    def __init__(self,parent,dir=True,p1=None,p2=None,offset=100,lm=0,tm=0,rm=0,bm=0,width=5):
        
        pycontrol.__init__(self)
        #self.classname = "SPLITTER"
        if p1 == None:
            self.port1 = viewport(0,0,10,10)
        else:
            self.port1 = p1
            
        if p2 == None:
            self.port2 = viewport(0,0,10,10)
        else:
            self.port2 = p2
        
        self.port1.parent = self.port2.parent = self.parent = parent
        self.parent_port = self.parent
        
        self.offset = offset
        self.direction = dir
        self.dragging = False
        self.draggable = True
        
        self.start_x = 0
        self.start_y = 0
        self.lm = lm
        self.rm = rm
        self.bm = bm
        self.tm = tm
        self.width = width
        
        self.setup()
    def on_draw(self):
        self.port1.draw() 
        glCallList(self.drawlist)   
        self.port2.draw()
    def on_select(self):
        glCallList(self.selectlist)
        self.port1.select()
        self.port2.select()
    def on_select_target(self,x,y):
        #glClear(GL_COLOR_BUFFER_BIT)
        
        pLeft,pTop,pWidth,pHeight = self.parent_port.rect
        glRecti(self.lm,self.tm,pWidth-self.rm,pHeight-self.bm)
        
        glColor4ub(1,255,0,0)
        glCallList(self.selectlist)
        glColor4ub(2,255,255,0)
        self.port1.select()
        glColor4ub(3,0,255,0)
        self.port2.select()    
        
        sel = glReadPixel(x,y) & 0xFF
        
        if sel == 1:
            return self
        if sel == 2:
            return self.port1.select_target(x,y)
        if sel == 3:
            return self.port2.select_target(x,y)
        
        return None
    def on_setup(self):
        #print self.parent_port.get()
        pLeft,pTop,pWidth,pHeight = self.parent_port.rect
    
        if pHeight < 1 or pWidth < 1:
            return
        
        tm = self.tm
        lm = self.lm
        rm = self.rm
        bm = self.bm
        w = self.width
        
        off = self.offset
        
        cw = current_warp()
        wl,wt,ww,wh = cw.rect
        if self.direction: #vertical
        
            if off > pWidth - 10:
                off = pWidth - 10        
        
            sx = pLeft+off+lm
            sy = pTop+tm
            sw = sx+w
            sh = pHeight-bm
            
            self.port1.set(pLeft+lm,tm,pLeft+off-w/2,pHeight-tm-bm)
            self.port2.set(pLeft+off+w+lm+w/2,pTop+tm,pWidth-(off+w)-lm-rm-w/2,pHeight-tm-bm)
        
            
        else: #horizontal
    
            if off > pHeight - 10 - bm:
                off = pHeight - 10 - bm
                
            sx = pLeft+lm
            sy = off+tm
            sw = sx + pWidth-rm
            sh = sy + w 
            
            self.port1.set(pLeft+lm,pTop+tm,pWidth-rm,off-w/2)
            self.port2.set(pLeft+lm,pTop+off+tm+w+w/2,pWidth-rm,pHeight-(off+w)-bm-w/2)
            
        
        self.port1.identity()
        self.port1.resize(ww,wh)
        self.port2.identity()
        self.port2.resize(ww,wh)   
        
        glNewList(self.drawlist,GL_COMPILE)
        #glColor3f(0.0,0.0,0.0)
        #mid_color.color3()
        draw_border(sx,sy-1,sw,sh,1)
        #glRectf(minx,miny+self.top_margin,maxx,maxy+self.top_margin)
        glEndList()
        
        
        glNewList(self.selectlist,GL_COMPILE)
        glRectf(sx,sy,sw,sh)
        glEndList()
    def on_mouse_in(self):
        #print "mouse in"
        if self.direction:
            current_warp().cursor = TC_HSIZE
        else:
            current_warp().cursor = TC_VSIZE
    def on_mouse_out(self):
        #print "mouse out"
        self.dragging = False
        current_warp().cursor = TC_ARROW
    def on_mouse_down(self,x,y,button):
        current_warp().capture_mouse(self)
        self.dragging = True
        self.start_x = x
        self.start_y = y
    def on_mouse_up(self,x,y,button):
        self.dragging = False
        current_warp().release_mouse()
    def on_mouse_move(self,x,y):
        
        if self.dragging:
            #minx,miny,minz,minw = self.minimum.get()
            pl,pt,pw,ph = self.parent_port.rect
            
            offset = self.offset
            
            if self.direction:
                offset += x-self.start_x            
                if offset < 3:
                    offset = 3
                if offset > pw - 10:
                    offset = pw - 10
            else:
                offset += y-self.start_y
                if offset < 3:
                    offset =3
                if offset > ph - 10 - self.bm:
                    offset = ph - 10 - self.bm   
    
            #self.minimum(minx,miny,0,0)
            self.offset = offset
            
            self.setup();
            self.start_x = x
            self.start_y = y
            current_warp().redraw()
    def on_resize(self,w,h):
        self.setup()
