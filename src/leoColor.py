#@+leo-ver=4-thin
#@+node:AGP.20250415230112.301:@thin leoColor.py
"""Syntax coloring routines for Leo."""

#@@language python
#@@tabwidth -4
#@@pagewidth 80

import leoGlobals as g
from leoLang import languages

import re
import string,time



#@+others
#@+node:AGP.20250415230112.302:leoKeywords
# leoKeywords is used by directivesKind, so it should be a module-level symbol.

# leoKeywords must be a list so that plugins may alter it.

leoKeywords = [
    "@","@all","@c","@code","@color","@comment",
    "@delims","@doc","@encoding","@end_raw",
    "@first","@header","@ignore",
    "@killcolor",
    "@language","@last","@lineending",
    "@nocolor","@noheader","@nowrap","@others",
    "@pagewidth","@path","@quiet","@raw","@root","@root-code","@root-doc",
    "@silent","@tabwidth","@terse",
    "@unit","@verbose","@wrap",
    "@keywords","@nosent","@xcc"]
#@-node:AGP.20250415230112.302:leoKeywords
#@+node:AGP.20250415230112.303:class colorizer
class colorizer:
    """Leo's syntax colorer class"""
    #@    @+others
    #@+node:AGP.20250415230112.304:__init__()
    def __init__(self,c,widget=None):
    
        self.c = c
        self.frame = c.frame
        self.body = c.frame.body
        
        if str(self.__class__) == "leoColor.nullColorizer":
            return self
        
        #self.import_languages()
        self.body_text_widget = self.text_widget = widget
        
        
        theme = g.theme
    
        self.tag_dict = {
            "directive"         :{'foreground':theme['directive']},
            "docPart"           :{'foreground':"red"},
            "keyword"           :{'foreground':theme['keyword']},
            "leoKeyword"        :{'foreground':theme['accent']},
            "link"              :{'foreground':theme['accent']},
            "nameBrackets"      :{'foreground':theme['string']},
            "string"            :{'foreground':theme['string']},
            "name"              :{'foreground':"red",'underline':1},
            "comment"           :{'foreground':theme['comment']},
        }
        
        if widget:
            self.configure_tags(widget)
        
        self.enabled = True # True: syntax coloring enabled
        self.showInvisibles = False # True: show "invisible" characters.
        self.comment_string = None # Set by scanColorDirectives on @comment
        
        self.names = []
        
        # Copies of arguments.
        self.p = None
        self.language = None
        self.langmod = None
        self.flag = None
        self.killFlag = False
        self.langswitch = False
        self.colorize_head = None
    #@-node:AGP.20250415230112.304:__init__()
    #@+node:AGP.20250415230112.305:remove_tags()
    def remove_tags (self):
        tw = self.text_widget
        for tag in tw.tag_names():
            tw.tag_remove(tag,"1.0","end")
            
            
    #@-node:AGP.20250415230112.305:remove_tags()
    #@+node:AGP.20250415230112.306:delete_tags()
    def delete_tags (self):
        tw = self.text_widget
        tw.tag_delete(*tw.tag_names())
            
            
    #@-node:AGP.20250415230112.306:delete_tags()
    #@+node:AGP.20250415230112.307:configure_tags()
    def configure_tags(self,w=None):
        
        if w:
            tw = w
        else:
            tw = self.text_widget
        
        for tag,td in self.tag_dict.items():
            tw.tag_config(tag,**td)
    #@-node:AGP.20250415230112.307:configure_tags()
    #@+node:AGP.20250422142943:sync_tags()
    def sync_tags(self,t):
        td = self.tag_dict
        td_keys = td.keys()
        for tn in t.tag_names():
            if tn in td_keys:
                t.tag_config(tn,**td[tn])
                if tn == "comment":
                    t.tag_raise(tn)
                if tn == "leoKeyword":
                    t.tag_raise(tn)
    #@nonl
    #@-node:AGP.20250422142943:sync_tags()
    #@+node:AGP.20250415230112.308:AGP self COLORIZER
    # todo:
    # whitespace
    # docpart and nocolor
    #plain language -> color only: leoKeywords and section
    # case insensitive lang
    #@nonl
    #@+node:AGP.20250415230112.309:colorize_lang()
    def colorize_lang(self,txt):
        
        #do some localisation
        pKeyword = self.pKeyword
        pDirective = self.pDirective
        pBlockString = self.pBlockString
        pString = self.pString
        pComment = self.pComment
        pBlockComment = self.pBlockComment
        pSection = self.pSection
        
        lang = self.langmod
        
        USE_BLOCKSTRING = lang.USE_BLOCKSTRING
        LINE_ESCAPE = lang.LINE_ESCAPE
        DIRECTIVE_START = lang.DIRECTIVE_START
        STRING_DELIMS = lang.STRING_DELIMS
        COMMENT_START = lang.COMMENT_START
        BLOCK_COMMENT_START = lang.BLOCK_COMMENT_START
        BLOCK_COMMENT_END = lang.BLOCK_COMMENT_END
        VALID_NAME_CHARS = lang.VALID_NAME_CHARS
        VALID_NAME_START_CHARS = lang.VALID_NAME_START_CHARS
        
        #self.widget
        
        lines = txt.splitlines()
        line_index = 1
        line = lines.pop(0)
        index = 0
        
        len_line = len(line)
        self.len_lines = len_lines = len(lines)
        
        parsers = self.parsers = []
        
        
        
        while 1:
            while index < len_line:            
                
                EOL = index == (len_line-1)
                self.EOF = EOL and (len_lines == 0)
                
                if len(parsers) > 0:
                    for p in reversed(parsers):
                        index = p( line,index,line_index )
                    
                else:
                    
                    ch = line[index]
                    substring = line[index:]
                    
                    if ch in VALID_NAME_START_CHARS:
                        index = pKeyword( line,index,line_index,True )
        
                    elif DIRECTIVE_START and substring.startswith(DIRECTIVE_START):
                        index = pDirective( line,index,line_index,True )
        
                    elif ch in STRING_DELIMS:
                        if USE_BLOCKSTRING and substring.startswith(ch*3):
                            index = pBlockString( line,index,line_index,True )
                        else:
                            index = pString( line,index,line_index,True )
                            
                    elif substring.startswith(COMMENT_START):
                        index = pComment( line,index,line_index,True )
                    
                    elif BLOCK_COMMENT_START and substring.startswith(BLOCK_COMMENT_START):
                        index = pBlockComment( line,index,line_index,True )
        
                    elif ch == "@":
                        index = pKeyword( line,index,line_index,True )
                        
                    elif substring.startswith("<<"):
                        index = pSection( line,index,line_index,True )
                        
                    else:
                        index += 1
                    
    
            if len_lines > 0:
                line_index += 1
                line = lines.pop(0)
                index = 0
                
                len_line = len(line)
                self.len_lines = len_lines = len(lines)
            else:
                break
        
    #@-node:AGP.20250415230112.309:colorize_lang()
    #@+node:AGP.20250415230112.310:colorize_none()
    def colorize_none(self,txt):
        
        #do some localisation
        pleoKeyword = self.pleoKeyword
        pSection = self.pSection
        
        
        #self.widget
        
        lines = txt.splitlines()
        line_index = 1
        line = lines.pop(0)
        index = 0
        
        len_line = len(line)
        self.len_lines = len_lines = len(lines)
        
        parsers = self.parsers = []
        
        
        
        while 1:
            while index < len_line:            
                
                EOL = index == (len_line-1)
                self.EOF = EOL and (len_lines == 0)
                
                if len(parsers) > 0:
                    for p in reversed(parsers):
                        index = p( line,index,line_index )
                    
                else:
                    
                    ch = line[index]
                    substring = line[index:]
                    
                    if ch == "@":
                        index = pleoKeyword( line,index,line_index,True )
                        
                    elif substring.startswith("<<"):
                        index = pSection( line,index,line_index,True )
                        
                    else:
                        index += 1
                    
    
            if len_lines > 0:
                line_index += 1
                line = lines.pop(0)
                index = 0
                
                len_line = len(line)
                self.len_lines = len_lines = len(lines)
            else:
                break
        
    #@-node:AGP.20250415230112.310:colorize_none()
    #@+node:AGP.20250415230112.311:pDirective()
    def pDirective(self,line,index,line_index,start=False):
        tw=self.text_widget
        #pp directives are multi-lined with \ , support for some form of comment
        if start:
            start = self.pDirective_start = (line_index,index)
            self.parsers.append(self.pDirective)
        else:
            start = self.pDirective_start
        
        
        
        lang = self.langmod
        len_line = len(line)
    
        substring = line[index:]
        
        #if substring.startswith("#"):#define "):
        words = substring.split()
        #print words,substring
        directive = words[0]
            
        #if directive in ["#define","#undef","#if","#ifdef","#ifndef","#endif","#else","#elif"]:
            
        """s = e = index+len(directive)+1#8
            while e < len_line-1 and not line[e].isspace():
                e += 1
            
            if e == len_line-1:
                e+=1
            """
        
        s = e = index+len(directive)+1
        if tw:
            tw.tag_add( "directive", "%i.%i" % start, "%i.%i" % (line_index,s) )
            #print "tag add1"
        
        if directive in ["#define","#ifdef","#ifndef","#undef"]:#next word is a definition
            index = s
            if len(words) > 1:
                name = words[1]
                #print "dirname",name
                index = s+len(name)
                if name not in self.names:
                    self.names.append(name)
                    #print name
                if tw: tw.tag_add( "leoKeyword", "%i.%i" % (line_index,s), "%i.%i" % (line_index,index) )
        else:
            index = s#+len(words[1])
        #elif directive in ["#if","#elif","#pragma","#error"]:#what follow is an expression
            
        #    index = len_line
            
        #elif directive in ["#endif"]:#what must be a comment
        
        
        self.parsers.remove(self.pDirective)
        
        line_escape = lang.LINE_ESCAPE
        
        """
        fd = {substring.find(lang.COMMENT_START): 1}
        if lang.BLOCK_COMMENT_START:
            fd[substring.find(lang.BLOCK_COMMENT_START)] = 2
        fd.pop(-1,None)
        
        
        if len(fd) > 0:
            pi = min(fd)     #minimum index found
            p = fd[pi]   #associated parser
        
            if p == 1:
                self.text_widget.tag_add("comment", "%i.%i" % (line_index,pi), "%i.%i" % (line_index,len_line) )
                index = len_line
                line_escape = False #void line escaping
        
            elif p == 2:
                index = self.pBlockComment(line,pi,line_index,True)
        """
        #else:
        #    index = len_line
            
        #if index == len_line:
        #    if line[index-1] != line_escape or self.len_lines==0:  #do not continue on next line
        #        self.parsers.remove(self.pDirective)
        #        self.text_widget.tag_add( "directive", "%i.%i" % start, "%i.%i" % (line_index,index) )
        #    #index += 1
                
        
        return index
    #@nonl
    #@-node:AGP.20250415230112.311:pDirective()
    #@+node:AGP.20250415230112.312:pComment()
    def pComment(self,line,index,line_index,start=False):
        
        tw=self.text_widget
        
        start =  (line_index,index)
        index = len(line)
        if tw: tw.tag_add("comment", "%i.%i" % start, "%i.%i" % (line_index,index) )
        
        return index
    
    #@-node:AGP.20250415230112.312:pComment()
    #@+node:AGP.20250415230112.313:pBlockComment()
    def pBlockComment(self,line,index,line_index,start=False):
        tw=self.text_widget
        
        if start:
            start = self.pBlockComment_start = (line_index,index)
            self.parsers.append(self.pBlockComment)
        else:
            start = self.pBlockComment_start
        
        BCE = self.langmod.BLOCK_COMMENT_END
        len_line = len(line)
        
        substring = line[index:]
        
        bcs = substring.find(BCE)
        
        
        if bcs > -1:
            index += bcs + len(BCE)
            stop = index + 1
        else:
            stop = None
            index = len_line
        
        
    
        if stop or self.len_lines==0:#EOF
            self.parsers.remove(self.pBlockComment)
            if tw: tw.tag_add("comment", "%i.%i" % start, "%i.%i" % (line_index,index) )
            
            if len(self.parsers)>0:
                index -= 1  #so that the parent parser can close
        
        return index
    #@nonl
    #@-node:AGP.20250415230112.313:pBlockComment()
    #@+node:AGP.20250415230112.314:pString()
    def pString(self,line,index,line_index,start=False):
        tw=self.text_widget
            
        if start:
            start = self.pString_start = (line_index,index)
            self.pString_delim = line[index]
            self.parsers.append(self.pString)
        else:
            start = self.pString_start
        
        len_line = len(line)
        
        index += 1
        
        substring = line[index:]
        
        ss = substring.find(self.pString_delim)   
        
        if ss > -1:
            index += ss+1
            self.parsers.remove(self.pString)        
            if tw: tw.tag_add( "string", "%i.%i" % start, "%i.%i" % (line_index,index) )
        else:
            index = len_line
            line_escape = self.langmod.LINE_ESCAPE
            
            if  (line_escape and not substring.endswith(line_escape)) or self.len_lines==0 :#EOF
                self.parsers.remove(self.pString)
                if tw: tw.tag_add( "string", "%i.%i" % start, "%i.%i" % (line_index,index) )
        
        
        return index
    #@nonl
    #@-node:AGP.20250415230112.314:pString()
    #@+node:AGP.20250415230112.315:pBlockString()
    def pBlockString(self,line,index,line_index,start=False):
        tw=self.text_widget
            
        if start:
            start = self.pBlockString_start = (line_index,index)
            self.pBlockString_delim = line[index]*3
            self.parsers.append(self.pBlockString)
        else:
            start = self.pBlockString_start
        
        lang = self.langmod
        len_line = len(line)
        
        bss = line[index:].find(self.pBlockString_delim)
        
        if bss > -1:
            index = index + bss + len(self.pBlockString_delim)
            self.parsers.remove(self.pBlockString)
            if tw: tw.tag_add( "string", "%i.%i" % start, "%i.%i" % (line_index,index+1) )
        
        else:
            index = len_line -1
            if self.len_lines==0:
                self.parsers.remove(self.pBlockString)
                if tw: tw.tag_add( "string", "%i.%i" % start, "%i.%i" % (line_index,index+1) )
        
        
        
        return index
    #@nonl
    #@-node:AGP.20250415230112.315:pBlockString()
    #@+node:AGP.20250415230112.316:pKeyword()
    def pKeyword(self,line,index,line_index,start=False):
        
        tw=self.text_widget
        
        if start:
            start = self.pKeyword_start = (line_index,index)
            self.parsers.append(self.pKeyword)
            if line[index] == "@":
                index += 1
        else:
            start = self.pKeyword_start
        
        
        
        lang = self.langmod
        len_line = len(line)
        
        if index == len_line:
            return index
        
        VNC = lang.VALID_NAME_CHARS
        
        valid = line[index] in VNC
        while valid and index < len_line-1:
            index += 1
            valid = line[index] in VNC
        
        
        EOL = index == (len(line)-1)
        
        if EOL and valid:
            index +=1
            
        name = line[start[1]:index]
            
        
        self.parsers.remove(self.pKeyword)
        
        if name.startswith("@"):
            if start[1] != 0 and name not in ("@others","@all"):
                return index
                
            if name in leoKeywords:
                if tw: tw.tag_add( "leoKeyword", "%i.%i" % start, "%i.%i" % (line_index,index) )
                    
        elif name in lang.keywords:
            if tw: tw.tag_add( "keyword", "%i.%i" % start, "%i.%i" % (line_index,index) )
        elif name in self.names:
            if tw: tw.tag_add( "leoKeyword", "%i.%i" % start, "%i.%i" % (line_index,index) )
        
        return index
        
    #@nonl
    #@-node:AGP.20250415230112.316:pKeyword()
    #@+node:AGP.20250415230112.317:pleoKeyword()
    def pleoKeyword(self,line,index,line_index,start=False):
        
        tw=self.text_widget
        
        start = (line_index,index)
        if line[index] == "@":
            index += 1
        
        
        len_line = len(line)
    
        valid = not line[index].isspace()
        
        while valid and index < len_line-1:
            index += 1
            valid = not line[index].isspace()
        
        
        EOL = index == (len(line)-1)
        
        if EOL and valid:
            index +=1
            
        name = line[start[1]:index]
        
        
        if name.startswith("@"):
            if start[1] != 0 and name not in ("@others","@all"):#only those are not required to be a line start
                return index
                
            if name in leoKeywords:
                if tw: tw.tag_add( "leoKeyword", "%i.%i" % start, "%i.%i" % (line_index,index) )
                
                #if name == "@language" and self.langswitch:
                #    print self,self.langswitch
                #    print "swith lang",line[start[1]:]
                    
                    
                
        return index
        
    #@nonl
    #@-node:AGP.20250415230112.317:pleoKeyword()
    #@+node:AGP.20250415230112.318:pSection()
    def pSection(self,line,index,line_index,start=False):
        
        tw=self.text_widget
            
        start = (line_index,index)
        
        len_line = len(line)
        
        #index += 1
        
        substring = line[index:]
        
        ss = substring.find(">>")   
        
        if ss > -1 and tw:
            #index += ss+1     
            if tw: tw.tag_add( "nameBrackets", "%i.%i" % start, "%i.%i" % (line_index,index+2) )
            
            #print line[index:index+ss+3]
            searchName = self.text_widget.get("%i.%i" % start,"%i.%i" % (line_index,index+ss+3)) # includes brackets
            ref = g.findReference(self.c,searchName,self.p)
            if ref:
                tn = "link"
            else:
                tn = "name"
                
            if tw: tw.tag_add( tn, "%i.%i" % (line_index,index+2), "%i.%i" % (line_index,index+ss) )
            if tw: tw.tag_add( "nameBrackets", "%i.%i" % (line_index,index+ss), "%i.%i" % (line_index,index+ss+3) )
        
        
            index = len_line
        else:
            index += 1
        
        
        return index
    #@nonl
    #@-node:AGP.20250415230112.318:pSection()
    #@-node:AGP.20250415230112.308:AGP self COLORIZER
    #@+node:AGP.20250415230112.319:disable() & enable()
    def disable (self):
    
        # print "disabling all syntax coloring"
        self.enabled=False
        
    def enable (self):
    
        self.enabled=True
    #@-node:AGP.20250415230112.319:disable() & enable()
    #@+node:AGP.20250415230112.320:colorize()
    def colorize(self,p,leading=None,trailing=None,incremental=False):
        
        """Color the body pane either incrementally or non-incrementally"""
        
        #import traceback; traceback.print_stack()
        
        if not self.enabled:
            return
            
        self.text_widget = self.body_text_widget
            
        self.scanColorDirectives(p)
        
        if self.killFlag:
            self.delete_tags()
            return
        
        self.remove_tags()
        
        
        if not self.flag:
            return
        
        clock = time.clock()
        
        c = self.c
        self.p=p
        
        # Add any newly-added user keywords.
        for d in g.globalDirectiveList:
            name = '@' + d
            if name not in leoKeywords:
                leoKeywords.append(name)
    
        if self.language:
            self.language = self.language.lower() # 6/20/05
        
        lang = self.language
        #print lang
        #if self.showInvisibles:
        
        #self.configure_tags()
        
        self.text_widget.tag_raise("comment")
        
        try:
            
            g.doHook("init-color-markup",colorer=self,p=self.p,v=self.p)
                
            s = self.body.getAllText()
            if s == "":
                return "ok"
            
            if lang in languages.keys():
                self.langmod = languages[lang]
                self.colorize_head = getattr(self.langmod,"colorize_head",None)
                
                self.colorize_lang(s)
                #print time.clock() - clock
            
            else:
                
                self.colorize_none(s)
                
            return "ok"
            
        
        except:
            
            
            if self.c:
                g.es_exception()
            else:
                import traceback ; traceback.print_exc()
            return "error" # for unit testing.
    #@-node:AGP.20250415230112.320:colorize()
    #@+node:AGP.20250416182201:colorize_headline()
    def colorize_headline(self,t):
        #print 'clorize'
        self.text_widget = t
        
        self.langswitch = True
        
        
        s = t.get(1.0,'end')
        
        #self.delete_tags();
        
        if s == "":
            return
            
        self.colorize_none(s)
        td = self.tag_dict
        t.tag_config("leoKeyword",**td["leoKeyword"])
            
    #@-node:AGP.20250416182201:colorize_headline()
    #@+node:AGP.20250417084753:colorize_headlineN()
    def colorize_headlineN(self,p,t):
        
        #check the langauge
        bs = p.v.bodyString()
        body_directives = self.scan_directives(bs,dir_list=["@language"])
        if body_directives:
            #print body_directives
            new_lang = body_directives[-1][1] # take last one
            if new_lang in languages:
                self.language = new_lang
                self.langmod = languages[new_lang]
                self.colorize_head = getattr(self.langmod,"colorize_head",None)
        
        lang,colorize_head = self.langmod , self.colorize_head
        
        
        
        self.langswitch = True
        
        tw = self.text_widget = t
        t.tag_delete(t.tag_names())
        
        txt = tw.get(1.0,'end')
        
        if lang:
            colorize_head = self.colorize_head#getattr(lang,"colorize_head",None) #custom language colorizer
        
            if colorize_head:
                res = colorize_head(txt)
                if res:
                    #print res
                    spec,ret,name,params,pure,dest,ctors = res
                    
                    off = 0# len(txt)
            
                    v,s,e = spec
                    if v != "":
                        tw.tag_add("keyword","1."+str(s+off),"1."+str(e+off))
            
                    v,s,e = ret
                    if s != -1 and e != -1:
                        tw.tag_add("keyword","1."+str(s+off),"1."+str(e+off))		
            
                    params,s,e = params
                    if params != "()":
                        s += 1
                        params = params.strip("()").split(",")
                        
                        for p in params:
                            """words = p.split()
                            
                            ptype = "".join(words[:-1])
                            #print "tags",s,len(ptype)
                            tw.tag_add("keyword","1."+str(s),"1."+str(s+len(ptype)) )
                            s += len(ptype)+1
                            
                            if len(words) > 1:
                                pname = words[-1]
                                tw.tag_add("string","1."+str(s+off),"1."+str(s+off+len(pname)))
                                s += len(pname)+1
                                
                            """
                            pmo = re.search("(?P<TYPE>.+[ |*])(?P<NAME>.*)",p)
                            if pmo != None:
                                #print pmo.groupdict(),p
                                s2,e2 = pmo.span("TYPE")
                                tw.tag_add("keyword","1."+str(s+off+s2),"1."+str(s+off+(e2-s2)))
                                s2,e2 = pmo.span("NAME")
                                tw.tag_add("string","1."+str(s+off+s2),"1."+str(s+off+e2))
                                
                                off += len(p)+1
                                
                    
                    
                    self.sync_tags(tw)
    
                    return
            #print "colorizing using colorizer"
        else:
            self.colorize_none(txt)
            td = self.tag_dict
            t.tag_config("leoKeyword",**td["leoKeyword"])
            return
        
        #print "colorizing using colorizer"
        #do some localisation
        pKeyword = self.pKeyword
        pDirective = self.pDirective
        pBlockString = self.pBlockString
        pString = self.pString
        pComment = self.pComment
        pBlockComment = self.pBlockComment
        pSection = self.pSection
        
        
        
        USE_BLOCKSTRING = lang.USE_BLOCKSTRING
        LINE_ESCAPE = lang.LINE_ESCAPE
        DIRECTIVE_START = lang.DIRECTIVE_START
        STRING_DELIMS = lang.STRING_DELIMS
        COMMENT_START = lang.COMMENT_START
        BLOCK_COMMENT_START = lang.BLOCK_COMMENT_START
        BLOCK_COMMENT_END = lang.BLOCK_COMMENT_END
        VALID_NAME_CHARS = lang.VALID_NAME_CHARS
        VALID_NAME_START_CHARS = lang.VALID_NAME_START_CHARS
        
        #self.widget
        
        lines = txt.splitlines()
        line_index = 1
        line = lines.pop(0)
        index = 0
        
        len_line = len(line)
        self.len_lines = len_lines = len(lines)
        
        parsers = self.parsers = []
        
        
        
        while 1:
            while index < len_line:            
                
                if lang != self.langmod: #because it may change while colorizing
                    lang = self.langmod
                    USE_BLOCKSTRING = lang.USE_BLOCKSTRING
                    LINE_ESCAPE = lang.LINE_ESCAPE
                    DIRECTIVE_START = lang.DIRECTIVE_START
                    STRING_DELIMS = lang.STRING_DELIMS
                    COMMENT_START = lang.COMMENT_START
                    BLOCK_COMMENT_START = lang.BLOCK_COMMENT_START
                    BLOCK_COMMENT_END = lang.BLOCK_COMMENT_END
                    VALID_NAME_CHARS = lang.VALID_NAME_CHARS
                    VALID_NAME_START_CHARS = lang.VALID_NAME_START_CHARS
    
                
                EOL = index == (len_line-1)
                self.EOF = EOL and (len_lines == 0)
                
                if len(parsers) > 0:
                    for p in reversed(parsers):
                        index = p( line,index,line_index )
                    
                else:
                    
                    ch = line[index]
                    substring = line[index:]
                    
                    if ch in VALID_NAME_START_CHARS:
                        index = pKeyword( line,index,line_index,True )
        
                    elif DIRECTIVE_START and substring.startswith(DIRECTIVE_START):
                        index = pDirective( line,index,line_index,True )
        
                    elif ch in STRING_DELIMS:
                        if USE_BLOCKSTRING and substring.startswith(ch*3):
                            index = pBlockString( line,index,line_index,True )
                        else:
                            index = pString( line,index,line_index,True )
                            
                    elif substring.startswith(COMMENT_START):
                        index = pComment( line,index,line_index,True )
                    
                    elif BLOCK_COMMENT_START and substring.startswith(BLOCK_COMMENT_START):
                        index = pBlockComment( line,index,line_index,True )
        
                    elif ch == "@":
                        index = pKeyword( line,index,line_index,True )
                        
                    elif substring.startswith("<<"):
                        index = pSection( line,index,line_index,True )
                        
                    else:
                        index += 1
                    
    
            if len_lines > 0:
                line_index += 1
                line = lines.pop(0)
                index = 0
                
                len_line = len(line)
                self.len_lines = len_lines = len(lines)
            else:
                break
        
        #configure used tags
        
        self.sync_tags(tw)
        #td = self.tag_dict
        #td_keys = td.keys()
        #for tn in t.tag_names():
        #    if tn in td_keys:
        #        t.tag_config(tn,**td[tn])
        #        if tn == "comment":
        #            t.tag_raise(tn)
        #        if tn == "leoKeyword":
        #            t.tag_raise(tn)
        #self.text_widget.tag_raise("comment")
        
        
        
    #@nonl
    #@-node:AGP.20250417084753:colorize_headlineN()
    #@+node:AGP.20250417133159:scan_directives()
    def scan_directives(self,s,dir_list=None):
        lines = s.splitlines()
        res = []
        
        for l in lines:
            ls = l.strip()
                
            if ls.startswith("@"):
                words = ls.split()
                if dir_list and words[0] in dir_list or not dir_list:
                    if len(words) > 1:
                        res.append(words[:2])
                    else:
                        res.append( (words[0],None) )
                    
                    
        if len(res) == 0:
            return None
            
        return res
    #@-node:AGP.20250417133159:scan_directives()
    #@+node:AGP.20250421213738:scan_tree()
    def scan_tree(self,p=None):
        #print "scan_tree"
        if p == None:
            p = self.c.rootPosition()
        
        while p:
            self.scan_node(p)
            for cn in p.subtree_iter():
                self.scan_node(cn)
            p = p.next()
        
    #@-node:AGP.20250421213738:scan_tree()
    #@+node:AGP.20250421214239:scan_node()
    def scan_node(self,p):
        #print p
        #check the langauge
        bs = p.v.bodyString()
        body_directives = self.scan_directives(bs,dir_list=["@language"])
        if body_directives:
            #print body_directives
            new_lang = body_directives[-1][1] # take last one
            if new_lang in languages:
                self.language = new_lang
                self.langmod = languages[new_lang]
        
        lang = self.langmod
        
        if not lang: return
        
        self.langswitch = True
        
        self.text_widget = None
        
        txt = bs
        
        
        
        #t.tag_delete(t.tag_names())
        
        #if not lang:
        #    self.colorize_none(txt)
        #    td = self.tag_dict
        #   t.tag_config("leoKeyword",**td["leoKeyword"])
        #    return
        
        
        #do some localisation
        #pKeyword = self.pKeyword
        pDirective = self.pDirective
        #pBlockString = self.pBlockString
        #pString = self.pString
        #pComment = self.pComment
        #pBlockComment = self.pBlockComment
        #pSection = self.pSection
        
        
        
        #USE_BLOCKSTRING = lang.USE_BLOCKSTRING
        LINE_ESCAPE = lang.LINE_ESCAPE
        DIRECTIVE_START = lang.DIRECTIVE_START
        #STRING_DELIMS = lang.STRING_DELIMS
        #COMMENT_START = lang.COMMENT_START
        #BLOCK_COMMENT_START = lang.BLOCK_COMMENT_START
        #BLOCK_COMMENT_END = lang.BLOCK_COMMENT_END
        #VALID_NAME_CHARS = lang.VALID_NAME_CHARS
        #VALID_NAME_START_CHARS = lang.VALID_NAME_START_CHARS
        
        #self.widget
        
        lines = txt.splitlines()
        
        if len(lines)==0:
            return
        
        line_index = 1
        line = lines.pop(0)
        index = 0
        
        len_line = len(line)
        self.len_lines = len_lines = len(lines)
        
        parsers = self.parsers = []
        
        
        
        while 1:
            while index < len_line:            
                
                if lang != self.langmod: #because it may change while colorizing
                    lang = self.langmod
                    #USE_BLOCKSTRING = lang.USE_BLOCKSTRING
                    LINE_ESCAPE = lang.LINE_ESCAPE
                    DIRECTIVE_START = lang.DIRECTIVE_START
                    #STRING_DELIMS = lang.STRING_DELIMS
                    #COMMENT_START = lang.COMMENT_START
                    #BLOCK_COMMENT_START = lang.BLOCK_COMMENT_START
                    #BLOCK_COMMENT_END = lang.BLOCK_COMMENT_END
                    #VALID_NAME_CHARS = lang.VALID_NAME_CHARS
                    #VALID_NAME_START_CHARS = lang.VALID_NAME_START_CHARS
    
                
                EOL = index == (len_line-1)
                self.EOF = EOL and (len_lines == 0)
                
                if len(parsers) > 0:
                    for p in reversed(parsers):
                        index = p( line,index,line_index )
                    
                else:
                    
                    ch = line[index]
                    substring = line[index:]
                    
                    #if ch in VALID_NAME_START_CHARS:
                    #    index = pKeyword( line,index,line_index,True )
        
                    if DIRECTIVE_START and substring.startswith(DIRECTIVE_START):
                        index = pDirective( line,index,line_index,True )
        
                    #elif ch in STRING_DELIMS:
                    #    if USE_BLOCKSTRING and substring.startswith(ch*3):
                    #        index = pBlockString( line,index,line_index,True )
                    #    else:
                    #        index = pString( line,index,line_index,True )
                            
                    #elif substring.startswith(COMMENT_START):
                    #    index = pComment( line,index,line_index,True )
                    
                    #elif BLOCK_COMMENT_START and substring.startswith(BLOCK_COMMENT_START):
                    #    index = pBlockComment( line,index,line_index,True )
        
                    #elif ch == "@":
                    #    index = pKeyword( line,index,line_index,True )
                        
                    #elif substring.startswith("<<"):
                    #    index = pSection( line,index,line_index,True )
                        
                    else:
                        index += 1
                    
    
            if len_lines > 0:
                line_index += 1
                line = lines.pop(0)
                index = 0
                
                len_line = len(line)
                self.len_lines = len_lines = len(lines)
            else:
                break
        
        
        
        
        
    #@nonl
    #@-node:AGP.20250421214239:scan_node()
    #@+node:AGP.20250415230112.321:scanColorDirectives
    def scanColorDirectives(self,p):
        
        """Scan position p and p's ancestors looking for @comment, @language and @root directives,
        setting corresponding colorizer ivars.
        """
        
        p = p.copy() ; c = self.c
        if c == None: return # self.c may be None for testing.
    
        if c.target_language:
            c.target_language = c.target_language.lower()
        
        self.language = language = c.target_language
        self.comment_string = None
        self.rootMode = None # None, "code" or "doc"
        
        self.flag = True
        self.killFlag = False
        
        comment_done = lang_done = color_done = False
        
        for p in p.self_and_parents_iter():
            # g.trace(p)
            s = p.v.t.bodyString
            theDict = g.get_directives_dict(s)
            
            #@        @+others
            #@+node:AGP.20250415230112.322:Test for @comment or @language
            # 10/17/02: @comment and @language may coexist in the same node.
            
            if not comment_done and theDict.has_key("comment"):
                    k = theDict["comment"]
                    self.comment_string = s[k:]
                    comment_done = True
            
            if not lang_done and theDict.has_key("language"):
                    i = theDict["language"]
                    language,junk,junk,junk = g.set_language(s,i)
                    self.language = language
                    lang_done = True
            
            #@-node:AGP.20250415230112.322:Test for @comment or @language
            #@+node:AGP.20250415230112.323:Test for @root, @root-doc or @root-code
            if theDict.has_key("root") and not self.rootMode:
            
                k = theDict["root"]
                if g.match_word(s,k,"@root-code"):
                    self.rootMode = "code"
                elif g.match_word(s,k,"@root-doc"):
                    self.rootMode = "doc"
                else:
                    doc = c.config.at_root_bodies_start_in_doc_mode
                    self.rootMode = g.choose(doc,"doc","code")
            #@-node:AGP.20250415230112.323:Test for @root, @root-doc or @root-code
            #@+node:AGP.20250415230112.324:Test for @nocolor @killcolor @color
            no_color = theDict.has_key("nocolor")
            color = theDict.has_key("color")
            kill_color = theDict.has_key("killcolor")
            
            
            # A killcolor anywhere disables coloring.
            if not color_done:
                if kill_color:
                    self.flag = False ; self.killFlag = True ; color_done = True
                # A color anywhere in the target enables coloring.
                if color and p == first:
                    self.flag = True ;  color_done = True
                # Otherwise, the @nocolor specification must be unambiguous.
                elif no_color and not color:
                    self.flag = False ;  color_done = True
                elif color and not no_color:
                    self.flag = True ;  color_done = True
            #@nonl
            #@-node:AGP.20250415230112.324:Test for @nocolor @killcolor @color
            #@-others
            
            if (comment_done or lang_done) and color_done:
                break
    
        #print self.flag,self.language
        
        return self.language # For use by external routines.
    #@-node:AGP.20250415230112.321:scanColorDirectives
    #@+node:AGP.20250415230112.325:color.schedule & idle_colorize (not used)
    def idle_colorize(self):
    
        # New in 4.3b1: make sure the colorizer still exists!
        if hasattr(self,'enabled') and self.enabled:
            p = self.c.currentPosition()
            if p:
                self.colorize(p,self.incremental)
    #@-node:AGP.20250415230112.325:color.schedule & idle_colorize (not used)
    #@+node:AGP.20250501081227:updateSyntaxColorer()
    def updateSyntaxColorer (self,p): pass
    #@nonl
    #@-node:AGP.20250501081227:updateSyntaxColorer()
    #@-others
#@-node:AGP.20250415230112.303:class colorizer
#@+node:AGP.20250415230112.326:class nullColorizer
class nullColorizer (colorizer):
    
    """A do-nothing colorer class"""
    
    #@    @+others
    #@+node:AGP.20250415230112.327:__init__
    def __init__ (self,c):
        
        colorizer.__init__(self,c,None) # init the base class.
    
        self.c = c
        self.enabled = False
    #@-node:AGP.20250415230112.327:__init__
    #@+node:AGP.20250415230112.328:entry points
    def colorize(self,p,incremental=False,interruptable=True): pass
    
    def disable(self): pass
        
    def enable(self): pass
    
    def scanColorDirectives(self,p): pass
    
    def updateSyntaxColorer (self,p): pass
    #@-node:AGP.20250415230112.328:entry points
    #@-others
#@-node:AGP.20250415230112.326:class nullColorizer
#@-others
#@-node:AGP.20250415230112.301:@thin leoColor.py
#@-leo
