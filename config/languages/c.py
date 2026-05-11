#@+leo-ver=4
#@+node:@file languages/c.py
import string,re

alias = ("cpp","c++")

from string import whitespace,ascii_letters,digits

USE_BLOCKSTRING = False
LINE_ESCAPE = "\\"

DIRECTIVE_START = "#"

STRING_DELIMS = "\""

COMMENT_START = "//"

BLOCK_COMMENT_START = "/*"
BLOCK_COMMENT_END = "*/"

VALID_NAME_CHARS = ascii_letters + digits + "_"
VALID_NAME_START_CHARS = ascii_letters + "_"


keywords = [
    # C keywords
    "auto","break","case","continue",
    "default","do","double","else","enum","extern",
    "float","for","goto","if","int","long","register","return",
    "short","signed","sizeof","static","struct","switch",
    "typedef","union","unsigned","void","volatile","while",
    # C++ keywords
    "asm","bool","catch","class","const","const_cast",
    "delete","dynamic_cast","explicit","false","friend",
    "inline","mutable","namespace","new","operator",
    "private","protected","public","reinterpret_cast","static_cast",
    "template","this","throw","true","try",
    "typeid","typename","using","virtual",
    # types
    "uint8_t","uint16_t","uint32_t","size_t","char","wchar_t",
    
    #misc
    "NULL",
    ]
    
symbols = {
    "USE_BLOCKSTRING":False,
    "LINE_ESCAPE" : "\\",
    "DIRECTIVE_START" : "#",
    "STRING_DELIMS" : "\"",
    "COMMENT_START" : "//",
    "BLOCK_COMMENT_START" : "/*",
    "BLOCK_COMMENT_END" : "*/",
    "VALID_NAME_CHARS" : ascii_letters + digits + "_",
    "VALID_NAME_START_CHARS" : ascii_letters + "_",
    "keywords" : keywords,
}

#@+others
#@+node:colorize_head()
def colorize_head(head,tw,line=1,hoff=0):
    params_e = head.rfind(")")
    
    linestr = str(line)+"."
    lineend = str(line)+".end"
    headstart = str(line)+"."+str(hoff)
    
    
    if head[0] not in VALID_NAME_START_CHARS:
        return None
    
    
    
    if params_e > -1:
        params_s = head.find("(",0,params_e)
        if params_s == -1:
            return None
        
        #process possible base class constructor initialisation
        head = head.replace("::",";;")
        
        head = " ".join(head.split())
        
        tctors = head.split(":")
        head = tctors.pop(0)#put actual funct in head
        #ctors = ""
        #for c in tctors:
        #    ctors += ":"+c		
        ctors = ":".join(tctors)
        
        #extract dest from ctors and append to head
        if ctors != "":
            p_e = ctors.rfind(")")
            head += ctors[p_e+1:]
            ctors = ctors[:p_e+1]
            #Error("xcc :","dest found:"+head)
        
        head = head.replace(";;","::")
        
        #remove the double space and so on
        #head = head.split()
        #head = string.join(head)
        head = string.join(head.split())
        
        
        
        #find "()" position
        params_e = head.rfind(")")
        params_s = head.rfind("(",0,params_e)
        
        if params_s > -1:
            # pure & dest ----------------------
            pure_s = head.find("=0",params_e)
            if pure_s > -1:				
                pure = (head[pure_s:pure_s+2],pure_s,pure_s+2)
                dest = (head[pure_s+2:],pure_s+2,len(head))
            else:
                pure = ("",-1,-1)
                dest = (head[params_e+1:],params_e+1,len(head))                    
            
            # params ------------------------			
            #params = (head[params_s:params_e+1],params_s,params_e+1)
            params = head[params_s:params_e+1]
            if params != "()":
                params = params.strip("()").split(",")
                off = 1
                for p in params:
                    pmo = re.search("(?P<TYPE>.+[ |*])(?P<NAME>.*)",p)
                    if pmo != None:
                        #print pmo.groupdict(),p
                        s2,e2 = pmo.span("TYPE")
                        tw.tag_add("keyword",linestr+str(params_s+s2+off+hoff),linestr+str(params_s+e2+off+hoff))
                        s2,e2 = pmo.span("NAME")
                        tw.tag_add("string",linestr+str(params_s+s2+off+hoff),linestr+str(params_s+e2+off+hoff))
                        
                        off += len(p)+1
            
            # name ---------------------------
            name_s = head.find("operator")
            if name_s == -1:
                name_s = head.rfind(" ",0,params_s)
                if name_s > -1:
                    name_s += 1
            
            if name_s > 0:
                name = (head[name_s:params_s],name_s,params_s)
                
                if name[0].startswith("~"): #ctors have no return value, all preceding name is specifier
                    #ret = ("",-1,-1)
                    #spec = (head[:name_s],0,name_s)
                    tw.tag_add("keyword",headstart,linestr+str(name_s+hoff))
                else:
                    ret_s = head.rfind(" ",0,name_s-1)
                
                    if ret_s > -1:
                        #ret = (head[ret_s+1:name_s-1],ret_s+1,name_s-1)
                        tw.tag_add("keyword",linestr+str(ret_s+1+hoff),"1."+str(name_s-1+hoff))
                        #spec = (head[:ret_s],0,ret_s)
                        tw.tag_add("keyword",headstart,linestr+str(ret_s+hoff))
                    else:
                        #ret = (head[:name_s],0,name_s)
                        tw.tag_add("keyword",headstart,linestr+str(name_s+hoff))
                        #spec = ("",-1,-1)
                    
            else:
                pass#name = (head[:params_s],0,params_s)
                #ret = ("",-1,-1)
                #spec = ("",-1,-1)
            
            #r = (spec,ret,name,params,pure,dest,ctors)
            return True
    return False
#@-node:colorize_head()
#@-others

#@-node:@file languages/c.py
#@-leo
