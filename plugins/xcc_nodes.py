#@+leo-ver=4-thin
#@+node:AGP.20230214111049:@thin xcc_nodes.py
"""Integrate C/C++ compiler and debugger in a node."""

#@<< About this plugin >>
#@+middle:AGP.20230214111049.1:Documentation
#@+node:AGP.20230214111049.2:<< About this plugin >>
#@@nocolor
#@+at 			
#@nonl
# X C++ Compiler nodes----
# PLEASE SEE http://xccnode.sourceforge.net/
#  The xcc_nodes.py plugins simplify c++ syntax and integrate compiling and 
# debuging tools.
# 
# To start debugging, create a node whose headline is::
# 
#     @xcc projectname
# 
# or::
# 
#     @xcc projectname.ext
# 
# The optional extension (*.ext) set the kind of project the node will build.
# An empty extension is equivalent to the '.exe' extension.
# 
# As soon as "@xcc" is written in the headline the plugin creates an empty 
# configuration.
# 
#     if ext == cpp,
#         inflate name.cpp
#         the node will attempt to build an executable
#     if ext == h,
#         inflate name.h
#         the node will attempt to check the syntax of the header
#     if ext == exe,
#         this is equivalent to no ext at all
#         inflate name.h and name.cpp
#         the node will attempt to build an executable
#     if ext == dll,
#         inflate name.h and name.cpp
#         the node will attempt to build a dynamic link library
#     if ext == lib,
#         inflate name.h and name.cpp
#  			the node will attempt to build a static link library
# 
# Creating programs
# 
# The "@xcc" node support Leo's @others syntax but **not**  section 
# references.
#  	The actual code is written in the children of the main node and the code 
# generation is
#  	affected by headlines.
# 
#  	Here are the rules: (see examples for good understanding)
# - The '@' rule: If a headline starts with "@", the node and its children are 
# ignored.
# 
# - The semicolon rule: If a headline ends with ";" and another compatible 
# rule is trigered in the
#  same headline, the rule will be written in the source if there is one.
# 
# **//**: If a headline start with "//", all its body and children are 
# commented out as follows::
#     /*headline
#         body text
#         and
#         childs
#         */
# 
# This rule is compatible with the ';' rule.
# 
# - The function rule: If a headline ends with ")", the headline is used as 
# funtion prototype.
#   The body and children are encased automatically in the opening and closing 
# curly brace.
# 
#   The class and function rules are disabled while in a function rule.
#   The function rule is compatible with the semicolon rule, except that if 
# there is a
#   header in the project the function will always be declared in the header 
# and
#   defined in the	source, appending "!" prevents declaration in header for 
# global functions.
# 
# - The class rule: If a headline starts with "class", a class is declared and 
# opening and
#   closing curly brace are automatically written, all the children of this 
# node are class members,
#   the functions are correctly dispatched between header and source (access 
# specifier is
#    appended if needed).
# 
# - The "Default" rule: If a headline doesn't match any of the preceeding 
# rules,
#   its headline is written as a comment and the body and childs written "as 
# is" as follows::
# 
#     //headline
#         body text
#         and all children.
# 
# This rule is compatible with the semicolon rule.
# 
# -> Config Panel reference:
# 	-> options : generally the most used options.
# 		-> Create files : Request that files should be inflated.
# 		-> Compile : Request that the project should be built using the configured 
# compiler.
# 			-> Seek first error : Attempt to locate the first error encountered.
# 		-> Execute : Request to run the built exe.
# 			-> Connect to pipe : Interface the built exe pipe to the node interface, 
# exe is simply spwned if unchecked.
# 		-> Debug : Request to run the built exe with the configured debugger 
# (overide the "Execute" option).
# 			-> Seek breapoints : Detect and "Goto" encountered breakpoints.
# 		-> Xcc verbose : Special verbose mode usefull to config the debugger and 
# widely used when coding the plugin
#  		-> Filter output : Filter compiler and debugger ouput, showing only error 
# and warning
# 		-> Colorize log : Colorize the output if checked, allowing easyer 
# browsing.
# 
# - by Alexis Gendron Paquette
#@-at
#@nonl
#@-node:AGP.20230214111049.2:<< About this plugin >>
#@-middle:AGP.20230214111049.1:Documentation
#@nl
#@<< version history >>
#@+middle:AGP.20230214111049.1:Documentation
#@+node:AGP.20230214111049.3:<< version history >>
#@@nocolor
#@+at
# 
# v 0.1: Alexis Gendron Paquette. - web & graphics: Felix Malboeuf
# 
# v 0.2 EKR:
# - Add per-node controller class.  This required many changes.
# - Many stylistic changes.  More are coming.
# 
# v 0.3 EKR:
# - Fixed a large number of crashers due to the reorganized code.
# - The major panels now appear to work.
# 
# v 0.4 EKR:
# - Added a ``what I did`` section.
# - Made UpdateProcess a cc method.
# - It appears that cc.OPTS is not set properly in PageClass.LoadObjects.
#   This prevents the compiler from working.
# v 0.5 AGP:
# - Asserted compatibility with leo 4.4.2.1 final
# - Many bug fix and improvement regarding line numbers and scroll system.
# - Added Language pane allowing to configure the node for almost any 
# language.
# - Added a tool launch sequencer in the option pane.
# - Added a Xcmd toggleable pane.
# - Began basic Linux testing, major problem reside in the use of "\" wich 
# worked in win32 wherea linux seem to require "/". Since window use both, the 
# solution is to always use "/".
# - Lot of other improvement.
#@-at
#@nonl
#@-node:AGP.20230214111049.3:<< version history >>
#@-middle:AGP.20230214111049.1:Documentation
#@nl
#@<< what I did >>
#@+middle:AGP.20230214111049.1:Documentation
#@+node:AGP.20230214111049.4:<< what I did >>
#@@nocolor
#@+at
# 
# **Important**: I have spent 8 or more hours making the following changes.
# Without doubt I have introduced some bugs while doing so. However, it was
# important to make these changes, for the following reasons:
# 
# 1. This is very important code, and deserves the best packaging.
# 
# 2. This code may form the basis of a Python-oriented debugger, so I wanted
#    to make the code base as solid as possible.
# 
# 3. Working and debugging code is the best way for me to really understand 
# it.
# 
# Here is what I have done in detail:
# 
# - Eliminated * imports:
#     ``* imports`` are bad style in complex code.
#     Replaced ``from leoPlugins import *`` by ``import leoPlugins``
#     Replaced ``from leoGlobals import *`` by ``import leoGlobals as g``
#     Replaced ``from Tkinter import *`` by import Tkinter as Tk.
#         Replaced Tk constants like END, FLAT, NW, etc. by 'end','flat','nw', 
# etc.
# 
# - Created the module-level init function that registers all hooks.
#   This is the recommended style: it shows in one place where all the hooks 
# are.
# 
# - Removed most try/except handling.
#     - Such handling is *usually* unnecessary, especially since Leo does a 
# good job
#       of recovering from crashes. However, try/except blocks might be 
# important
#       when executing user code, so perhaps it will be necessary to put some 
# back in.
#     - Replaced ``x = aDict[key]`` by ``x = aDict.get(key)`` to avoid 
# exceptions.
# 
# *** Eliminated *all* global variables (except commanders) as follows:
# 
# - Created per-commander controller class instances.
#     - The controllers dictionary is the only global variable.
#     - The new OnCreate event handler creates controller instances.
#     - Replaced all global variables by ivars of the controller class.
#     - Global constants still exist.
#     - Most former global functions now are methods of the controller class.
#     - By convention, cc refers to the proper controller, i.e., the 
# controller for the proper commander c.
#     - cc gets passed to the constructor of almost all classes.
#     - Replaced init logic (start2 hook) by logic in the ctor for the 
# controller class.
# 
# - Simplified module-level event handlers.
#     - They simply call the corresponding event handler in the proper 
# controller instance.
# 
# - Renamed most classes from XXX to XxxClass.
# 
# - Eliminated the Parser global.
#     - All Rule classes now get a Parser argument and define self.Parser.
# 
# - Disabled some weird code in OnIdle.  I'm not sure what this is supposed to 
# do.
# 
# - Create a new pause module-level function that calls winPause or linPause 
# as appropriate.
# 
# - Used more Pythonic or Leonic ideoms in many places:
#     - Replaced ``if x == True:`` by ``if x:``.
#     - Replaced ``if x == False:`` by ``if not x:``.
#     - Replaced ``if x != '':`` by ``if not x:``
#     etc.
#     *** Warning: these simplifications might cause problems.
#         For example, the re module uses None as a sentinal, and can also 
# return 0,
#         so tests like ``if result:`` are not correct in such cases.  I have 
# tried
#         not to simplify the code "too much" but I may have made mistakes.
#     *** if p is a node, ``if p == None:`` *must* be replaced by ``if not 
# p:``.
#     - cc.VERBOSE and cc.FILTER_OUTPUT now have values True/False instead of 
# 'true'/'false'.
#     - Defined TraceBack as g.es_exception.
#     - Changed ``Error(x) ; return`` to ``return Error(x)``, and similarly 
# for Warning, etc.
# 
# - Simplified the code wherever possible.
#     - Sometimes the change can be dramatic, as in cc.cGetDict.
# 
# * There does not seem to be any definition of ExtractLines.
#@-at
#@nonl
#@-node:AGP.20230214111049.4:<< what I did >>
#@-middle:AGP.20230214111049.1:Documentation
#@nl
#@<< what was redid/undid >>
#@+middle:AGP.20230214111049.1:Documentation
#@+node:AGP.20230214111049.5:<< what was redid/undid >>
#@@nocolor
#@+at
# 
# Ok, Edward made a great job on its own and has he expected somme bugs where 
# introduced but nothing too serious. I finished the code adaptation and 
# resolved the bug. I tried as much as possible to follow Ed's syntactic 
# rules. The major bugs introduced where caused by the replacement of code 
# like "if x == "True"" by "if x == True" or "if x". The config store those 
# value as the string, thats why they are compared against strings. I cant 
# explain why those tree form doesnt produce the same effect by i can tell 
# that they where causing trouble, so for now i use only comparition against 
# string.
# 
# Ther was also problems with the leo tracing system, see the "Tracing 
# Problems" node that follow.
# 
#@-at
#@-node:AGP.20230214111049.5:<< what was redid/undid >>
#@-middle:AGP.20230214111049.1:Documentation
#@nl
#@<< imports >>
#@+node:AGP.20230214111049.12:<< imports >>
# from leoPlugins import *
# from leoGlobals import *
import leoPlugins
import leoGlobals as g

# from Tkinter import *
import Tkinter as Tk
import traceback
import os,sys,thread,threading,time,string,re
import tkFileDialog,tkMessageBox,tkSimpleDialog
import pickle,base64,zlib

#import ttk
from PIL import Image,ImageTk,ImageOps
#@nonl
#@-node:AGP.20230214111049.12:<< imports >>
#@nl

controllers = {}

if 1: # To be replaced by ivars
    #@    << globals >>
    #@+node:AGP.20230214111049.13:<< globals >>
    #@+others
    #@+node:AGP.20230214111049.14:Icons
    #binary mapping: 00 0000 (6bit)MSB->LSB
    # b0:mark
    # b1:doc
    # b2:content
    # b3:clone
    # b4-5:type : class func or comment
    MARK_MARK = 1
    DOC_MARK = 2
    CONTENT_MARK = 4
    CLONE_MARK = 8
    
    FUNC_MARK = 0
    CLASS_MARK = 16
    #@+node:AGP.20230214111049.15:Go
    Go_e = "S\'x\\xdam\\x8e\\xcbn\\x830\\x14D\\xf7\\xfcLk \\xb2\\xbc\\xe8\\xe2\\xda@\\xc4\\xd32\\xe0\\x90.!J\\xa1\\x04\\x02\\x04K\\x80\\xbf\\xbeV\\xd6\\x1d\\xe9\\xe8\\x8cf5\\xf9\\xe7p\\xe6\\xde\\xd0\\xf9\\x00\\x02R\\x01\\xc0\\x9b\\xbb\\xa3\\xf0\\xfdd@\\nWH5\\x95\\xe9\\x956\\xd6+\\xe6\\x844\\xdcl|\\xbf]\\x03\\xfd\\xb2\\t\\xc16r\\x96j \\xa7\\xe3f\\xe9\\xb9\\x90\\xea\\xfbH\\xb1[\\xf8\\xfa\\xa90v2\\xadG\\xf5\\xc2v\\xd6\\x7f\\x18\\x88\\x01\\x8d\\xaa\\xef\\x83\\xb9v\\x1es\\xdc\\xc1?a\\xdb[\\xd6\\xfb\\x11@X\\t(\\x19\\xdd\\xc35\\xa6\\xd4\\x83)\\x8d\\x1fG\\xeb\\x8a\\x98uB\\xa2K\\xd2\\xb5\\xc0#\\xf8\\xcd\\xe5xI\\x8ap\\x95\\xb1\\xdf\\x8b\\x15_\\x9eT\\xf8\\xac\\xf4X\\\'\\xd7\\xf9,\\xc0\\x92u\\x11\\xc0\\x81\\xf2i\\xd8\\xdbtIR\\xdaJw\\x9aD\\xbb\\xf1(b%\"\\xf5\\x02b\\x8b\\x7f\\x80n\\xa2E]\\xe1f~\\x00\\xe0\\xad_\\xd6\\x1f\\x96\\x88[)\'\np0\n."
    #@nonl
    #@-node:AGP.20230214111049.15:Go
    #@+node:AGP.20230214111049.16:StepIn
    StepIn_e = "S\'x\\xda\\x95\\xd0Ms\\x820\\x10\\x06\\xe0;\\x7f\\xa5\\x17\\x15\\xa6\\x0e\\x87\\x1e6\\x100|\\x9a\\xa4\\x0c\\xda\\x9bP\\x0b\\x02\\x82\"\\x18\\xf0\\xd77\\xe1\\xdaS3\\xf3dg\\x92\\xec\\xbb3a\\xab\\xc6\\x8d\\xed\\xa6\\xc4\\x00\\x14\\xa2\\x04 \\xce\\xae\\xfa\\x98\\x9d\\xf5a{^\\x0f\\xdbTy\\r\\x99\\x12+S\\xbe\\x95R\\xf3)\\r\\xd9\\xc6|J\\xb2\\xae\\xe5\\x93\\xb5\\xa6\\xb6\\xfe\\xb4\\x19n\\xa7\\xb4QZo\\xce\\x95\\xc6\\xe3\\x89Ry<\\xac\\xc8\\xac\\xe0\\x92\\xf0\\xc52I\\xca\\xf5\\xe1\\x95\\xeb\\xd1\\xe2\\xa4G\\xbd&sTV\\x7f\\xdcD\\x95\\x92\\xaa\\x84\\xfa\\xe6\\xf3\\xfaf\\xd1\\xda\\xb3h\\x85\\xa7\\x90\\xab\\x03\\x99\\xc3\\xea/\\x97\\x01\\xc5P\\x10\\x0b\\xfe.\\r\\xfe\\xb3,\\xb1\\x94\\xe5K\\x00H\\x05\\xb0\\xb7\\xd0D\\x1e>\\x02{\\xee\\xb8v\\x7f \\x01\\xc4A\\x05\\x159\\x8f^\\xd4\\xe8\\xb8+\\xef\\xcfQ5O\\x06\\xd0\\x10\\x17yq\\xddU\\xc4H(B(\\x19-\\x87N\\x82\\xcb\\x8e\\x82\\xf8c\\x8f\\x8aU\\xe8\\x072\\x9b\\x89\\x1d\\x08m\\x15\\xbb\\xc8f\\xc2\\xb7\\xf6\\xcc\\xeb.\\x07\\x84\\xcb\\x90\\xec\\x03Q\\xd0\\xb1\\xa4\\x989\\xf7\\x9f\\x16\\xdek,\\x1b>\\x9b\\xef\\xc0\\xb6\\x8f\\x1d=\\xc4\\xed\\xe5M\\x0e\\xe1\\x8c^Z\\xe4|\\xd2 j\\x10\\x1a\\xf8.\\xd3J\\xd1\\xcd\\x1e\\xb2\\rJb\\xd4\\x82i:\\x85 `?>\\xb4_\\xa4j\\x9b\\xc9\'\np0\n."
    #@nonl
    #@-node:AGP.20230214111049.16:StepIn
    #@+node:AGP.20230214111049.17:StepOver
    StepOver_e = "S\'x\\xda\\x95\\xd0Mo\\x830\\x0c\\x06\\xe0;\\xbf\\xa6|hh\\x87\\x1e\\x9c\\x10h`@\\x03\\xed(\\xbbA\\x86\\xc2\\x97J\\x05l\\x01~\\xfdHw\\x9f\\xb4Wz\\xec\\x8b-YN\\x0e\\xbd\\x17;}M\\x00\\x18DW\\x80\\xc8\\xae\\xf4\\xd9\\xce\\x94m.\\x95XY\\xb8\\xad\\xb8\\xca7\\xbf\\xed\\xb2We.\\rE\\xdfGuM\\x95\\xb1\\xccf\\xe5Q\\x18\\xf3\\xb8{\\x14Y\\xaf\\xdc\\x83\\x8c\\xdf\\xfd\\x95\\xf7\\xfez\\xed\\xe9\\x1a\\xb6t%5M\\x9f*s\\xb6+3\\xda\\xf8\\xae0#\\xb56j\\xb9\\xfe\\xbbz\\xed\\xfdTI\\xbbG\\x90v>f\\xed\\xf0\\x12\\xb7d\\t\\x93\\xee\\xc3K\\x80\\x11\\x10\\x14\\xc3\\xdf\\xd1\\xe0?\\xc1\\xf2\\xd9\\x9e/\\x01\\xa0\\x8d\\x847\\x8c\\x16:\\x05\\x08\\xe1uJ\\xb5\\xb1\\xc3IN]$\\x98\\x90\\\'\\x1f\\xa4\\xcc\\xc3\\xc0\\x850\\x8c\\x9a\\xba\\xa6A\\xec\\x92U\\xcf\\xc0At\\x10\\x11r\\x93\\xeb\\x019\\xc8bS\\x02\\x08\\x1f\\x863\\x96\\xcc\\xea.\\x1e\\x08\\xbd8a4hy\\x00\\x143\\xdf\\xee\\xef\\xb5\\xe0\\xd4\\xa3h\\xab\\x9c\\xf2\\xaba\\xef\\x1e\\xc6\\x84I\\xcag!\\xac\\x98\\x9cH\\xcbo\\x13\\x069Y\\xa9?b\\x03\\xce\\xedV[\\xc5%\\xac\\x97O\\xc2\\xb1!)\\xb9]4Q\\x87\\xab\\xe77\\xc2\\xca\\xf4\\xb30\\xf9\\xdb~\"\\xc4\\xf2x\\xd4~\\x00\\\'\\xed\\x9a\\xd0\'\np0\n."
    #@nonl
    #@-node:AGP.20230214111049.17:StepOver
    #@+node:AGP.20230214111049.18:StepOut
    StepOut_e = "S\"x\\xda\\x95\\xd0\\xddn\\x820\\x14\\xc0\\xf1{\\x9eF\\xc5\\x8c\\xedb\\x17\\xa7\\xa5`a\\x80\\x05;\\xd4;As\\xca\\x87\\x9bQ\\x94\\x8f\\xa7_\\xcb\\x1b\\xac\\xc9/\'9i\\xfeM\\x9a.Z?q[\\xc5\\x00\\x04\\xc4\\x12 )\\xae\\xf6\\xb3\\xb8\\xd8\\x9dsYvNnL]a$\\xc6P:\\xda\\xde{\\x95\\xf9\\x87\\xd1\\x15\\xab\\x8f\\x97\\xa6\\xe7\\xd2\\xd2\\xf7\\x96\\xc6\\xbd\\xc8;\\xe3vZiy\\xab\\x95?\\xc18k\\x83L\\xd6A\\x16\\xd5|\\x8c\\x14\\x1f\\x99\\xe2\\xd9\\xec\\xb2N\\x9d\\xf9U\\xad\\xb4\\xbb\\xc9*\\xedx2Nv|\\xd7\\x9d\\xd9a\\x15\\xd7F~\\x8duV\\x97\\x9a[\\x985\\x01\\x15\\xf5\\xef[R\\xb3!\\xca\\xccB\\xf7\\xd2\\xe6\\xe8\\xa7 \\x18 \\xa7\\x00`\\xc1\\x7f\\x0e\\xed\\xe71\\x7f\\t\\x00o\\x01\\xb6\\x94\\x0c\\\\\\xfa\\xd4E\\xc4\\xad\\xa5\\xb7\\x04\\x9b\\xfc\\x8b\\x02\\xde7A\\x8f\\xb8\\x90\\xa17E\\xef\\x8ce=6\\x8c\\xd0\\x1d[\\xec<\\xa2\\xb8\\xdc\\x10w|\\x84\\x02\\xf0\\xb6\\xe0\\xd2S4F\\xeaUp8\\xd1\\xe8\\x8ar\\x98\\xa0\\xea\\xad\\xa6<\\xb9(\\x90\\x9d_J\\x08\\xdf\\x150\\x9e/\\xacI\\x15J\\x97\\xba4\\x0f\\xfdjI c>\\xfb\\xe6\\x9b\\xfd/\\x0e\\x870\\x8a\\x08*2$\\x10\\x9c\\xf91\\xc3*>$t\\xbf\\x86\\xeaL,2\\xae\\xc6M\\xa3{O\\x07H\\xfa\\x90\\x94\\xef\\xa0/]_\\xb1\\xf2\\x8b\\xa0\\x80\\xa4\\xff\\xfc\\xb4\\xfe\\x00\\xd4\\xc7\\xa1 \"\np0\n."
    #@nonl
    #@-node:AGP.20230214111049.18:StepOut
    #@+node:AGP.20230214111049.19:Pause
    Pause_e = "S\'x\\xda\\x95\\xceKn\\x830\\x18\\x04\\xe0=\\x97i\\xf3t\\xba\\xc8\\xe2\\xb7\\t\\xc6N\\xb0e\\x08\\x02\\x96\\x85\\x02\\x86:\\x84\\x14Wn9}Q{\\x82\\x8e\\xf4I\\xb3\\x19i\\xe2gC\\xa5o\\xf4\\t@A\\xa4\\x00\\x04\\xaa7\\x16e+[f\\xbb\\xc5f1\\xdbR.]\\xce\\x13Z\\xe4\\xc1\\xcb!\\x0f\\xd0>3\\x03OR\\xc3\\x92\\x93\\t-\\xeaC1{\\x9a\\x8a\\xfeim?\\xea\\xb5\\xedM\\xc0\\x93\\xda\\xc1\\xffC\\xfeF\\xde\\xef#\\x00V(\\x10\\x04\\x7f\\xb1\\xe9\\xec\\xe3\\xd6U\\xb9\\x0c}\\xd82B\\xb4\\xdaJ\\xca\\xaf\\xeeN\\x19&8m8\\xef\\x8aT\\xf9\\xb4\\xd3\\xd3%}\\xcc\\xf7(\\x13\\xac\\xed\\xa2\\xc6\\x80\\xday\\xef\\xcc\\x07\\x03\\xac\\xba\\xc9\\x98\\x1d\\x1e\\x82\\xde\\xba\\xd1\\x0e\\xda\\xb1\\xf4\\xbb\\x91\\xe6Z]\\xe2\\xcf\\xbe(h\\x89\\xc1\\x9d\\x13\\xdc\\xb7N\\x91\\x81\\x8c\\x8e\\xbf\\xd11~\\x8d\\x08\\x80t\\xc7\\xa3\\xf7\\x03\\xce\\xc7^\\x95\'\np0\n."
    #@nonl
    #@-node:AGP.20230214111049.19:Pause
    #@+node:AGP.20230214111049.20:Stop
    Stop_e = "S\'x\\xda-\\x8c\\xc1\\x8e\\x820\\x14E\\xf7\\xfc\\x8c\\xa2\\x18\\xdc\\xb8x\\x14h\\x0b%\\x0e4LSv`\\xb4O@t\\xa4\\x19\\x18\\xbe~&d\\xee\\xe2\\x9c\\xe4,n\\xb1\\xed\\xe99\\xec1\\x02\\xc8Ad\\x00\\xe7\\xe6\\xb1\\xb7\\xfe\\xd5\\xb5\\xbeZl\\xa3\\x96\\xaf\\x9d}\\xd5\\xaal\\xd9_\\xdc\\xdb\\xb7>\\x1eR~\\xf9$\\xb4q\\t\\xbdx3\\x88\\xed\\x0b\\xfe\\xe7\\xac$\\xd3\\xaa\\xf5\\x10\\x80\\xab\\x1c\\x18\\tf>\\xa6a`&\\x9d\\xb0\\xb8\\xe5\\x1d\\xa5\\x811Z\\x8b\\x04y\\xa78\\x18\\x8c\\xde\\xb5\\x91P\\xd6\\t\\xbd\\xe3\\xc4\\xaa\\xef\\xc9s\\xb2Z\\x02\\xc8l\\xb8\\xde\\x97\\xaa\\x93\\x85\\xe8\\xe4\\xb8A\\x94\\xba|T\\xa2_2\\x16\\xc5$\\x7f\\xa6\\xb7\\x8f\\xc1\\xe0\\x0f13X\\x8a\\x05F&\\x1eZ\\xe9Y\\x1a\\x00\\x84\\xe3\\xc9\\xf9\\x05\\x1a\\x01HO\'\np0\n."
    #@nonl
    #@-node:AGP.20230214111049.20:Stop
    #@+node:AGP.20230214111049.21:Doc
    DocData = "S\'x\\xda\\xcd\\x92\\xb9\\x92\\x9b@\\x00Ds~E\\x01\\x08\\x81\\x80\\xc0\\xc1\\x0c\\x83Y\\x0e\\x89C \\xa1\\xcd\\xc4\\xc2\\x0c \\x98\\x11\\xe2\\xe6\\xeb\\x17\\xdb\\xa1S\\x07~U/\\xe9\\xea\\xea\\xa8C\\xa16=T\\x17\\x06\\x00\\x01\\xf0\\xee\\x008^\\xf58\\xde\\xea\\xd4-\\x8f\\xd8\\x1d4\\xfc\\x165\\xac\"\\x987\\x19\\xdf=s\\xb0\\xa7\"\\x9boM+IMH\\xedGQ\\xbene%\\xe7u\\x9d\\xb6\\nG\\\\q\\xf7\\xcb\"=\\xee\\n\\xc7)\\x9f\\xeez\\xe9\\\\\\xff\\xb3\\xef\\x10(5\\x14T\\\'\\xecQ5\\r\\xeb\\xaf$l\\xd4*\\xa6*\\x7f\\xa5\\x19J\\x9a\\x8c&4[\\xcbFM\\x02\\xf65&L=|r\\xed\\x19E\\xac\\xe3\\x83\\xae\\xa7q\\x9f\\xe1`\\xec\\x15<\\xf6>a9\\xda\\xa4m?\\xbc\\xbb\\xa1K\\xbd\\xa5\\x1b\\xbd\\xe5\\x8c\\xfd\\xa9G\\xde\\xac\\xa5\\xde\\x9c\\\'\\xcd\\xb4\\x1b\\x87)\\x7f\\xb7\\x8b\\x8f\\xe6\\x15\\xa3\\x99[\\x87\\x8a\\x89y\\xc5\\x0e~z8\\x0c\\xca \\xe7\\xfc(\\xf3\\x95,c*\\xcb\\xe3&?*\\n\\x9f\\x8a*^Uu<h\\x1a\\xbf\\x817\\\'\\xf0\\x17\\x1c\\xf8\\x87\\xfc\\xa7c\\xfa\\xf4g\\xec\\xf7-\\x00\\xb0(\\x81X\\x87\\xb3\\xd59\\x10\\x92%\\x16\\r#\\x9a\\xeeq`\\x932\\x0c^\\x1e\\n\\xee\\xad\\x0e\\xcd\\xc86\\x12\\x9bLS|:Y\\x86eR\\x07\\x11\\x89\\xc5\\xd0\\xac\\xe4\\x85\\xdb\\xeb\\x15`V\\x1e\\xd4\\x936X&,\\x8c&\\xf6\\xcc\\t\\xdc\\xe0\\xc7\\xf3%\\x03\\xd3o\\xa2k$\\xf5\\x91-,8x\\n\\xf6\\xaa\\xb0H~.\\xe9\\xa5\\x11Z\\xf7L\\x04\\xa7\\xbeT\\x11[\\x1f\\x1f\\xee \\xca\\x9ct,\\x9d\\x97\\x11\\xf2W\\x8bL\\xda\\x1d\\x18\\xfa\\xbc\\\'\\xf0gI\\x80d!c\\xbb\\xd1X\\x97P\\xb2\\x80\\x0e\\x88`\\xdcO[\\x1e\\x07\\x16\\x03af\\x19%`.,\\xa0\\x1e\\xfb\\x0e\\xd9\\x1a\\xa8\\xfb\\xc1}\\x03\\xa7@\\xeb\\x92\'\np0\n."
    #@nonl
    #@-node:AGP.20230214111049.21:Doc
    #@+node:AGP.20230214111049.22:Watch
    WatchData = "S\"x\\xda\\x95\\x90\\xdbr\\x820\\x10@\\xdf\\xf9\\x1a\\xc1Z\\xea\\xe3&\\x86\\x8b\\x96\\x8bf\\x18\\x8coBk \\xa4B!\\x8a\\xc9\\xd77\\xfa\\x07\\xdd\\x99\\xb3g\\xf7ewg\\x0f\\x0b\\x19f\\x1b\\xd9\\x10\\x80=\\xa4\\x05@Z\\x95\\xae\\xaaJ\\xa3\\xaa\\xec\\xc9\\xa3\\xf633\\xf9\\xd6\\xc7\\xcc\\x9d\\xfc\\xc0:p\\xa7c`,\\xf7\\xca\\xd6\\xa3\\xb7\\xbeW\\xdeZ\\x9d\\xbd\\xb5\\xb3\\xfc-\\xd7\\x16w5h\\x0bu\\xfdwO\\x8d\'\\xad\\xcco)\\x07F\\xe5\\xaa\\xd7\\xd2\\xf4T.\\x07Z\\x8fL\\xd7\\x8a\\xd1\\xfa~\\xd2\\x85\\xdc\\xd2\\xe2j\\x11\\xb1NDL\\x9f\\x10\\xe7\\x99\\x9a\\xe8Fd\\x94\\x91\\xe1x#\\xc2\\xfaj\\xfb&R~\\x13\\xa5\\xbe\\xb0X\\x9b\\xefejjO\\x99&T\\xe3\\xd9\\x1d\\x04\\xf3\\xd2\\xb3]g\\xb1\\x13\\xbbaG9\\x80\\x03\\xff\\t<\\xbf\\xf4z\\t@\\xdc\\x00D\\x18=\\x18\\xdbm\\x10\\x9f\\x07\\xe2\\xf4\\xb8El\\xda\\xda\\xe6\\xab,\\x82\\x16b\\x12F\\x98\\x7f\\x04|\\x143#\\x04\\x03\\x97\\x19N\\xda>\\xee>\\xa3\\x96s\\x9d$-\\xdbw1A\\xb3j\\xcfR\\xac\\x12\\xa0!\\xc6\\xec\\x92#~p\\xdeB\\x84\\x10]L\\xb7X\\xf3\\xbe\\xc8s\\x01\\x8f\\xe2\\x07o\\x0eo\\xfdq#`\\x9f\\x07!\\x1cz\\x8d\\n>\\xbb\\xdd\\xe5\\xb3y\\xef\\x92,Ar\\xde\\xdez\\xd4\\xa4\\xa5)\\xc7\\x92\\x04\\xdfWx\\xd4\\x1d:9\\xdcey\\x84\\x16{{\\xba\\xef\\xfc\\x01\\xdb\\xb2\\x9a\\xfc\"\np0\n."
    #@nonl
    #@-node:AGP.20230214111049.22:Watch
    #@+node:AGP.20230214111049.23:Config
    ConfigData = "S\'x\\xdaU\\xce\\xc1r\\x820\\x14\\x85\\xe1=O\\x03\\xd6\\x11\\xbb\\xbc\\t\\x84\\x06\\x0c\\x99@-\\xda\\x1d\\xa4N\\x10(j\\xc9\\x10\\xe0\\xe9k\\xd8yg\\xbe\\xb9\\x9b\\x7fq2\\xb7\\x8bx\\xd0\\xd5!\\x80\\x00&\\x00R\\xff\\xe2i\\xbf\\xf0tU,\\xba\\xe2\\xd6$}\\x8b\\x8c\\xf2D\\xa6\\xa7Q\\x16\\xefc\\xb5\\xb1l\\xe6\\xfd\\x95\\x1bm9\\xf7\\xb2\\xe8\\xfa\\xa4\\x90}<\\xaf::\\xb3\\x86\\xcea\\xfd\\xa1\\xfd\\xcb[\\xba\\xc8\\xb5K\\x9b\\xb3g\\xcb8?\\xb6\\xf7$W\\xf0z\\xd8\\xac\\xcfY\\x17\\x01\\xd0\\n \\xc68S7\\x16\\x802\\x8a\\xd0\\x01\\x1b\\x8a\\tF\\x8aR\\xce@\\x18N\\x00+\\x97\\x8a\\x14\\xc0$1\\xa0\\xba\\x1d\\xcaC-\\xdc\\x9c#\\x04\\xfbG\\x19\\xd57\\xe7\\xf8\\x0b(@\\xed\\x105\\x0b=3\\x1ev\\x8a\\xf5\\x15\\xc1\\xd0\\xee\\xd1!\\x80t\\xc74R\\xe2Hq\\x8f\\x94\\xfb\\xc5\\xae`\"\\x81\\x82O\\xd3d\\xd1\\xf5[\\xe5\\x12=\\xa6\\xed\\xcf)\\x84m\\xbb\\x1b\\x03\\xe7\\xb9\\xd8w\\xfe\\x01*\\x83e%\'\np0\n."
    #@nonl
    #@-node:AGP.20230214111049.23:Config
    #@+node:AGP.20230214111049.24:Prompt
    Prompt_e = "S\'x\\xda\\xad\\x90\\xcdn\\xab0\\x14\\x84\\xf7\\xbcJ\\x16\\xb9I\\xdbp\\xbb\\xe8\\xe2p\\xb0\\x8d\\xe1\\xf2\\xe3:\\xb4%;\\x12r\\r\\x86\\x14Zh\\x0cy\\xfa\\x92\\xf6\\t*\\xf5\\x93F\\xa3\\x91F\\xb3\\x98\\xc7?\\r\\x8b\\xdd\\xa6d\\x02\\x04D)@\\xb2\\x9c\\xf9\\x7fs\\xbfX\\x9e\\xed\\xc5\\xfet7\\xd8\\xc7\\x9ba\\xff\\xbc\\x9au\\xe9\\xed\\xf8\\xd2\\xbf\\xd0\\xf1\\x1a\\xf3\\xe7\\xa6\\xdbM\\x87W\\x7f:4|\\n5\\x97\\xc4*\\xbdk;\\xba\\x1c\\xd6\\xc3{>+[\\x0f:[G:[us\\xdd\\x97i\\xdd\\x05\\xb2\\xf6Q\\xe8v\\x13W\\xd7@J.\\x00\\x96c\\xbdc\\x8f \\x08(\\x8e\\xf0\\x8d\\x05\\xbf\\xc8\\xcf\\xc6\\xd0|\\xd9\\xd7%\\x00\\xfcm>\\x86\\xc5\\x0e\\xf4\\x81\\xeb(\\xa3\\xa8\\x85\\xf5\\x96\\xf7\\x01E\\x18y%\\xbb\\x91\\xf7G\\xdfE\\tSq\\xaeD\\x9f\\\'\\x9e\\x1e\\xf9G\\xd1\\x18q\\x9b\\\'\\xbe\\xae\\xc8S\\xd6Om\\x9b\\xba\\x1e:w\\xf1\\xae6\\x1da\\xa1\\x87\\x08\\xe2%\\xacn-\\x11\"\\xbaXli\\x0b\\xdc\\xb4\\x1c\\xdc1\\x13E\"D{@\\x07+\\x88\\\\L\\x03\\xf5\\x11zP\\xf6\\x9b\\xfd+(Ch\\xdaH\\xf8k\\xc3vl\\x81q45\\x8bC\\xbd\\x19d\\xce-TNU\\x94\\xda@J\\xa8\\xae)U\\\'\\xf8\\x97)BOR\\xaf\\xa0\\xdb\\xf9\\xf5\\xe2]\\x9d\\x19$|\\xb4\\x03\\xc5\\x02R\\x95\\xfc\\xb8]\\x0b\\x15I\\x80\\xd8<<X\\x9fJ\\x0f\\xa2\\xed\'\np0\n."
    #@nonl
    #@-node:AGP.20230214111049.24:Prompt
    #@+node:AGP.20230214111049.25:Xcmd
    Xcmd_icon = "S\'x\\xda\\xcd\\x93\\xc1r\\xa30\\x0c\\x86\\xef\\xbcJ/\\x01\\x9a\\xd0\\x1cz\\xb0\\xc1\\x10C\\x81\\x05J\\x13\\xb8\\x81\\xc3\\xd8\\x0b\\x9e\\xe2\\x82\\x13\\xc0O_g{\\xd8\\x17\\xd8\\xc3j\\xe6\\x9b_\\xd6H\\xb2\\xc7#\\xe5;\\x1e\\xa4\\x1eg\\x08\\x80\\x0c\\xa4\\x15\\x00I{V\\xb2M\\x1f\\xac\\xd76\\xbd\\x13\\\'U\\xb3\\x93\\xae\\xe4\\xe2\\x9b\\xb3\\xe3\\xdf\\xb5\\xaa\\xf9p\\xbc\\xb7\\xfa<YG\\xd9\\x9c\\x8f\\xb6\\xd8\\xcc\\xbd(L\\xc39Xrj,)\\xeaM*QH\\xfb\\xcb\\xe2\\x9f\\xe1\\xc6e\\xb5q5\\x16\\xdc\\xfe:\\x13\\x1enD\\xd4\\x05\\x99\\xaa\\x8d\\xc8z+\\xfb\\xb0(9\\xde\\xe2\\xfet\\x8b\\xc5%\\x8du\\x1cu\\xf6\\r\\x19\\xfc\\x94\"q\\xb9\\xa1>\\xb8!Q\\xe5NgK\\x87\\x9d\\xa4Cl\\xa9\\x88\\x9d\\xa8NC,\\xa9X U\\xf7s\\xefT\\x99\\xe1\\xc4\\x83\\xa4\\xafL\\xd1w\\x1a\\xad\\xcd\\x03\\xe3\\xcc\\xc3\\xa6\\xd1N\\xc9\\xc3B\\xfbE9\\x88(\\x1b\\xc2H\\xab\\xabU\\x83\\x0fi?j\\xd0\\x1a\\x17\\x88aM\\x90\\x0fu\\x90\\x83\\xcc\\x05\\x14\\xbb\\xe0\\xaf\\x19\\xe0\\x1f\\xda\\x7f\\xda\\xcc]~\\x9a\\xfd\\x19\\x0b\\x00\\xf0\\xb4\\x00\\xdf\\x85+\\x9e#\\x08A&\\x9b\\x05RH_\\x12H3>\\xe6>\\xa4\\x00\\x07\\xa1G\\x8f\\xedG\\xe0R]\\x05\\xa1\\x07\"\\x0f\\xe4\\x85\\x88\\x8a\\x14\\xb2}e\\x88\\x18R\\x1c\\xc7\\x1e\\xed\\x8f\\x91\\xf9\\xa9\\x7f4\\xab|\\x98\\x8d\\xbb\\xbb\\x9bc\\x11\\xd3\\xc4\\xdd\\xb2\\\'\\x9d\\xd2d\\xbf\\xdf\\xa1W~\\x90\\xc3\\xa9\\xcf\\xc7h\\x08\\xd0\\xaef\\xfe\\xe8\\xaf\\xf8\\xb9\\xc1\\xfe;&A\\xbff\\x06\\x9a\\x0b\\xfd\\x8c\\xeb\\xf8\\xe21\\xbaC\\xf5/Lc\\xf6\\xe4\\xc3\\x9c\\xa0(wwQ\\xb4\\x87\\xacZ(AtH\\x0e\\xee\\t\\xb65~\\x03@1k\\x80eF\\x94\\x17\\xe2\\xf3\\xe7\\xc5e\\xac c\\x07\\x0c\\xa4\\xac7\\x0c\\xebg0_=\\xba\\x0c\\x11|,\\xc2\\xf2\\xfaj|\\x03\\x12!\\xf4\\x1d\'\np0\n."
    #@nonl
    #@-node:AGP.20230214111049.25:Xcmd
    #@-node:AGP.20230214111049.14:Icons
    #@+node:AGP.20230214111049.26:Colors
    ErrorColor = "#%02x%02x%02x" % (255,200,200)
    BreakColor = "#%02x%02x%02x" % (200,200,255)
    LineNumColor = "#%02x%02x%02x" % (200,200,255)
    RegExpFgColor = "#%02x%02x%02x" % (0,0,255)
    VarSupBgColor = "#%02x%02x%02x" % (255,230,230)
    #@nonl
    #@-node:AGP.20230214111049.26:Colors
    #@-others
    
    path_sym = "\\"
    #@nonl
    #@-node:AGP.20230214111049.13:<< globals >>
    #@nl

#@@language python
#@@tabwidth -4

__version__ = "0.5"

#@+others
#@+node:AGP.20230214111049.1:Documentation
#@+node:AGP.20230214111049.6:Known Flaws
#@@nocolor
#@+at 
# 
# *** Most flaw can be worked around by using "default" node(or rule) and 
# writing all	code inside it.
#  (default rule -> comment out headline & write body "as is")
# 
# - line number refresh isnt 100% accurate when editing text in the body.
# - Breakpoints can only be Added/deleted, Enabling/Disabling isnt supported 
# yet.
# - code auto dispath feature wont work as expected with template class and 
# function.
# - class is the only structural keyword supported in the tree to date, union, 
# struct and enum dont trigger any rule.
# - DLL debugging is untested to date, it surely dont work.
# - Untested on Linux, see linPause and aPause functions.
#@-at
#@nonl
#@-node:AGP.20230214111049.6:Known Flaws
#@+node:AGP.20230214111049.7:Future Features
#@@nocolor
#@+at
# 
# - C/C++ code/project importer/merger
# - Display external files if needed.(external error or similar)
# - "Browse Info" management allowing declaration/references to be searched 
# and displayed.
# - Automation of precompiled headers, possibly using a "#PCH" node.
# - in the debugger regular expression/task list:
#     reg exp:
#         if a group named "FOO" is returned by the regular
#         expression, then the "_FOO_" variable is supported
#         by the corresponding "Task" line.
#     Task:
#         Apart from those defined by the corresponding regular	expression,
#@-at
#@-node:AGP.20230214111049.7:Future Features
#@+node:AGP.20230214111049.8:Tracing Problems
#@+at
# -the g.trace func seem to randomly crash:
# ----------------------------------------------------------------------------------------
# Traceback (most recent call last):
#   File "C:\Documents and 
# Settings\gendroal\Programs\leo\plugins\xcc_nodes.py", line 884, in onIdle
#     cc.UpdateProcess()
#   File "C:\Documents and 
# Settings\gendroal\Programs\leo\plugins\xcc_nodes.py", line 979, in 
# UpdateProcess
#     g.trace()#ProcessClass.List
#   File "C:\Documents and Settings\gendroal\Programs\leo\src\leoGlobals.py", 
# line 1650, in trace
#     print name + ": " + message
# IOError: [Errno 9] Bad file descriptor
# ----------------------------------------------------------------------------------------
# 
#     This crash occur on idle time when opening leo with xcc_nodes enabled, 
# it show up randomly even if nothing is touched and no file operation is made 
# by the xcc plugin.
#     Seem that the only file descriptor present is the one used by the 
# "print" statement.
# 
# -try/except block were re-added to nearly all the plugin entry points, wich 
# are:
#     -All module level events handler
#     -The funcs called by the plugin buttons:
#         in ToolbarClass.Go & Refresh
#         in ControllerClass:
#             aPause
#             aStop
#             aStepIn
#             aStepOver
#             aStepOut
#         in ConfigClass.Show & Hide
#         in ConfigClass.CplPageClass.Browse & AddPath
#         in ConfigClass.DbgPageClass.Browse
#         in WatcherClass.Show & Hide
# - All g.trace occurence were commented out
#@-at
#@-node:AGP.20230214111049.8:Tracing Problems
#@+node:AGP.20230214111049.9:XCC Explanation
#@+at
# UNFINISHED
# 
# The xcc nodes idea emerge from a unpublished simple plugin called cpp_nodes 
# that i'v developed about 2 years ago. The aim of the cpp nodes plugin was to 
# reduce redondant c++ syntaxe. It then was obvious what the next step was 
# going to be, the breeding of the cpp nodes with the run nodes. The outcoming 
# xcc plugin result, with the aid of already present leo's feature, in a 
# powerfull code managing and building software. It work for any laguage and 
# tool we'v tried so far, from assembler to c++, from sdcc to windebug.
# 
# Special coding effort are made for this plugin to work in linux, but 
# unfortunately i have no report of any actual testing for that.
# 
# 
# Overall operation of the node is separated in three main actions.
# 
# Firstly the source and documentation files are generated by interfacing the 
# ParserClass, wich propose a generic parsing algorithm(tought it was 
# developed for c++), with opened files write methodes.
# 
# Secondly the build sequence is launched by running the configured tools with 
# a boosted version of the run_nodes plugin PROCESS class.
# 
# Thirdly, if configured for, the debugger will be launched for an interactive 
# debuging session.
# 
# 
#@-at
#@+node:AGP.20230214111049.10:The Three Distinctive Nodes
#@+at
# Amongst the members of the controllerclass, SELECTED_NODE, ACTIVE_NODE and 
# CHILD_NODE are some valuable and cherished companions. Hence they are great 
# clue of generale implement's stance. One who meddle with therein divine 
# matter is to make vigilant awareness of the nameless trinity.
#@-at
#@nonl
#@-node:AGP.20230214111049.10:The Three Distinctive Nodes
#@+node:AGP.20230214111049.11:The Parser
#@+at
# The ParserClass is one of the core component of the plugin, it run a set of 
# syntactic rules on the child nodes headlines. When a rule trigger, it 
# usually write the headline and the body(@others too) by using the 
# Declare(),Define() or Docum() function from ParserClass. These three 
# functions are the only outputs of the plugin(apart from config save), and in 
# fact they are not entirely output, the ParserClass must be configured to do 
# whatever suit one. Each of these increment a specific variable contained in 
# the parser. Define()\Declare() increment CURRENT_SRC_LINE\CURRENT_HDR_LINE 
# and Docum() incremnent CURRENT_DOC_LINE. Apart from the increment they call 
# functions contained in three separatelist, DEC_PROC_LIST, DEF_PROC_LIST and 
# DOC_PROC_LIST(now try to guess wich function call wich list). In the 
# ParserClass the lists are empty by default, so it produce nothing on its 
# own.
#@-at
#@nonl
#@-node:AGP.20230214111049.11:The Parser
#@-node:AGP.20230214111049.9:XCC Explanation
#@-node:AGP.20230214111049.1:Documentation
#@+node:AGP.20230214111049.27:Module level
#@+node:AGP.20230214111049.28:init
def init ():
    
    data = (
        (("new","open2"),   OnCreate),
        ("save1",           OnSave1),
        # ("start2",        OnStart2),
        (("select2","open2"),         OnSelect2),
        ("idle",            OnIdle),
        ("command2",        OnCommand2),
        ("bodydclick2",     OnBodyDoubleClick),
        ("bodykey2",        OnBodyKey2),
        ("headkey2",        OnHeadKey2),
        ("end1",            OnQuit),
    )
    
    for hook,f in data:
        leoPlugins.registerHandler(hook,f)

    g.plugin_signon(__name__)

    return True


#@-node:AGP.20230214111049.28:init
#@+node:AGP.20230214111049.29:Module-level event handlers
#@+node:AGP.20230214111049.30:OnCreate
def OnCreate(tag,keywords):
    try:
        c = keywords.get("c")
        if c:
            controllers [c] = controllerClass(c)
    except Exception:
        g.es_exception()
#@nonl
#@-node:AGP.20230214111049.30:OnCreate
#@+node:AGP.20230214111049.31:OnStart2 (No longer used)
if 0:
    def OnStart2(tag,keywords):
        try:
            if XCC_INITED == False:
                c = keywords.get("c")
                InitXcc(c)
                n = c.currentPosition()
                h = n.headString()	
                
        except Exception,e:
            TraceBack()
#@nonl
#@-node:AGP.20230214111049.31:OnStart2 (No longer used)
#@+node:AGP.20230214111049.32:OnSelect2
def OnSelect2(tag,keywords):
    try:
        global controllers
        c = keywords.get("c")
        cc = controllers.get(c)
        cc and cc.onSelect()
    except Exception:
        g.es_exception()
#@nonl
#@-node:AGP.20230214111049.32:OnSelect2
#@+node:AGP.20230214111049.33:OnIdle
def OnIdle(tag,keywords):
    try:
        global controllers
        c = keywords.get("c")
        cc = controllers.get(c)
        cc and cc.onIdle()
    except Exception:
        g.disableIdleTimeHook()
        g.es_exception()
#@nonl
#@-node:AGP.20230214111049.33:OnIdle
#@+node:AGP.20230214111049.34:OnCommand2
def OnCommand2(tag,keywords):
    try:
        global controllers
        c = keywords.get("c")
        cc = controllers.get(c)
        cc and cc.onCommand2(keywords)
    except Exception:
        g.es_exception()
#@nonl
#@-node:AGP.20230214111049.34:OnCommand2
#@+node:AGP.20230214111049.35:OnBodyDoubleClick
def OnBodyDoubleClick(tag,keywords):
    try:
        global controllers
        c = keywords.get("c")
        cc = controllers.get(c)
        cc and cc.onBodyDoubleClick()
    except Exception:
        g.es_exception()
#@nonl
#@-node:AGP.20230214111049.35:OnBodyDoubleClick
#@+node:AGP.20230214111049.36:OnBodyKey2
def OnBodyKey2(tag,keywords):
    try:
        global controllers
        c = keywords.get("c")
        cc = controllers.get(c)
        cc and cc.onBodyKey2(keywords)
    except Exception:
        g.es_exception()
#@nonl
#@-node:AGP.20230214111049.36:OnBodyKey2
#@+node:AGP.20230214111049.37:OnHeadKey2
def OnHeadKey2(tag,keywords):
    try:
        global controllers
        c = keywords.get("c")
        cc = controllers.get(c)
        cc and cc.onHeadKey2(keywords)
    except Exception:
        TraceBack()
#@nonl
#@-node:AGP.20230214111049.37:OnHeadKey2
#@+node:AGP.20230214111049.38:OnQuit
def OnQuit(tag,keywords):
    try:
        global controllers
        for key in controllers.keys():
            cc = controllers.get(key)
            cc.onQuit()
    except Exception:
        g.es_exception()
#@nonl
#@-node:AGP.20230214111049.38:OnQuit
#@+node:AGP.20230316112635:OnSave1
def OnSave1(tag,kw):
    try:
        global controllers
        c = kw.get("c")
        cc = controllers.get(c)
        cc and cc.CleanXccDicts()
    except Exception:
        g.es_exception()
#@nonl
#@-node:AGP.20230316112635:OnSave1
#@-node:AGP.20230214111049.29:Module-level event handlers
#@+node:AGP.20230214111049.39:pause & helpers
def pause (pid):
    
    if os.name == "nt":
        winPause(pid)
    else:
        linPause(pid)
#@nonl
#@+node:AGP.20230214111049.40:winPause
def winPause(pid):
    
	import ctypes

	hp = ctypes.windll.Kernel32.OpenProcess(0x1F0FFF,0,int(pid))
	if hp == 0:
		return Error("xcc: ","can't open process: "+str(long(ctypes.windll.Kernel32.GetLastError())))
	
	if ctypes.windll.Kernel32.DebugBreakProcess(hp) == 0:
		return Warning("xcc: ","Unable to break into the target!")
#@nonl
#@-node:AGP.20230214111049.40:winPause
#@+node:AGP.20230214111049.41:linPause
def linPause(pid):	# theorical way to do it, untested!

	import signal
	os.kill(pid,signal.SIGINT)
#@nonl
#@-node:AGP.20230214111049.41:linPause
#@-node:AGP.20230214111049.39:pause & helpers
#@+node:AGP.20230214111049.42:Helpers
#@+node:AGP.20230214111049.43:StrToBool
def StrToBool(str,value="True"):
    if str == value:
        return True
    return False
#@nonl
#@-node:AGP.20230214111049.43:StrToBool
#@+node:AGP.20230214111049.44:AddText
def AddText(text,node):

	node.setBodyString(node.bodyString()+text)
	l,c = LeoBody.index("end").split(".")
	LeoBody.see(l+".0")
#@nonl
#@-node:AGP.20230214111049.44:AddText
#@+node:AGP.20230214111049.45:CompressIcon
#@+at
# # Encode to base64, zip the data in a string and finally pickle it to be 
# free from illegal char
# #the inflated file is a literal(without the quote)
# #to be embeded in code and passed to DecompressIcon func before use.
# 
# #to use:
# 	# remove "@" at the top
# 	# ctrl+e (execute script)
# 	# choose the file to translate, press save
# 	# open choosedfile.lit in notepade, select all(ctrl+a), copy(ctrl+c), close 
# notepade
# 	# paste(ctrl+v) where you needed your literal (dont forget to add the 
# quote)
# 
# from leoGlobals import *
# import tkFileDialog
# from pickle import *
# from base64 import *
# from zlib import *
# import os
# 
# 
# try:
# 	ft = ('All Files', '.*'),
# 	s = tkFileDialog.askopenfilename(filetypes=ft,title="Select file to 
# convert...")
# 	if s:
# 		f = file(s,"rb")
# 		data = f.read()
# 		f.close()
# 		b64data = encodestring(data)
# 		zdata = compress(b64data,9)
# 		pdata = dumps(zdata)
# 		pdata = pdata.replace("\\","\\\\")
# 		pdata = pdata.replace("\'","\\\'")
# 		pdata = pdata.replace("\"","\\\"")
# 		pdata = pdata.replace("\n","\\n")
# 		name,ext = os.path.splitext(s)
# 		f = file(name+".lit","wb")
# 		f.write(pdata)
# 		f.close()
# except Exception,e:
# 	g.es(str(e))
#@-at
#@nonl
#@-node:AGP.20230214111049.45:CompressIcon
#@+node:AGP.20230214111049.46:DecompressIcon
def DecompressIcon(data):
	try:
		#unpickle
		zdata = pickle.loads(data)	
		#unzip
		return zlib.decompress(zdata)	#return a base64
	except Exception:
		Traceback()
#@-node:AGP.20230214111049.46:DecompressIcon
#@+node:AGP.20230214111049.47:Error
def Error(module,error):
	g.es(module,newline = False,color = "blue")
	g.es(error,color = "red")
#@-node:AGP.20230214111049.47:Error
#@+node:AGP.20230214111049.48:GetDictKey
def GetDictKey(dic,key,create=False,init=""):
        if key in dic:
            return dic[key]
        else:
            if create == True:
                dic[key] = init
                return dic[key]
            else:
                return None
#@nonl
#@-node:AGP.20230214111049.48:GetDictKey
#@+node:AGP.20230214111049.49:GetNodePath
def GetNodePath(node,_as="->"):

	path = []
	for p in node.parents_iter():
		path.insert(0,p.headString()+_as)

	path.append(node.headString())
	return ''.join(path)
#@nonl
#@-node:AGP.20230214111049.49:GetNodePath
#@+node:AGP.20230214111049.50:GetXccNode
def GetXccNode(node):

	for p in node.parents_iter():
		h = p.headString()
		if (h[0:5] == "@xcc "):
			return p
	
	return None
#@-node:AGP.20230214111049.50:GetXccNode
#@+node:AGP.20230214111049.51:ImportFiles
def ImportFiles():

	Warning("TODO: ","Add import code in ImportFiles function!")
#@nonl
#@-node:AGP.20230214111049.51:ImportFiles
#@+node:AGP.20230214111049.52:IsXcc
def IsXcc(node):

	if node.headString()[0:5] == "@xcc ":
		return True
	else:
		return False
#@-node:AGP.20230214111049.52:IsXcc
#@+node:AGP.20230214111049.53:HasXccDict
def HasXccDict(v):
    if hasattr(v,"unknownAttributes"):
        if "xcc_cfg" in v.unknownAttributes:
            return True
                
    return False
#@nonl
#@-node:AGP.20230214111049.53:HasXccDict
#@+node:AGP.20230214111049.54:Message
def Message(module,warning):

	g.es(module,newline = False,color = "blue")
	g.es(warning)
#@-node:AGP.20230214111049.54:Message
#@+node:AGP.20230214111049.55:TraceBack
def TraceBack():
        typ,val,tb = sys.exc_info()
        lines = traceback.format_exception(typ,val,tb)
        for line in lines:
            # g.es(line,color = "red")
            print line
            
TraceBack = g.es_exception
#@nonl
#@-node:AGP.20230214111049.55:TraceBack
#@+node:AGP.20230214111049.56:Warning
def Warning(module,warning):

	g.es(module,newline = False,color = "blue")
	g.es(warning,color = "orange")
#@nonl
#@-node:AGP.20230214111049.56:Warning
#@+node:AGP.20230317140108:GetAtOthersLayout()
def GetAtOthersLayout(node):
    cc = self.cc
    #if cc.CREATE_DOC == "True":
    #    doc = cc.cGet("DOC","",node)
    self.DocumNode(node)
        
    b = node.bodyString().strip("\n")
    o = b.find("@others")
    
    self.CURRENT_LOCATION = 1   #body
    
    
    
    cbt = self.CURRENT_BODY_TEXT = node.bodyString().split("@others")
    
    if len(cbt) > 0:
        
        for ti in range( len(cbt)-1 ):
            t = cbt[ti].splitlines(True)
            
            if not t[-1].endswith("\n"):    #there is a tabing for @others
                tab = t.pop(-1)
            
            self.TabWrite(t,w)
            
            self.Tab(tab)
            
            self.PushBodyLine()
            if self.ParseNode(node) == False:
                return False
            self.PopBodyLine()
            
            self.CURRENT_LOCATION = 1   #body
            
            self.UnTab(tab)
            
        
        self.TabWrite( cbt[-1].splitlines(True), w )    #write the final chunk
#@nonl
#@-node:AGP.20230317140108:GetAtOthersLayout()
#@+node:AGP.20230214111049.57:C++ parsing
#@+node:AGP.20230214111049.58:SplitFunc
def SplitFunc(head):
    params_e = head.rfind(")")
    if params_e > -1:
        
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
            params = (head[params_s:params_e+1],params_s,params_e+1)			
            
            # name ---------------------------
            name_s = head.find("operator")
            if name_s == -1:
                name_s = head.rfind(" ",0,params_s)
                if name_s > -1:
                    name_s += 1
            
            if name_s > 0:
                name = (head[name_s:params_s],name_s,params_s)
                
                if name[0].startswith("~"): #ctors have no return value, all preceding name is specifier
                    ret = ("",-1,-1)
                    spec = (head[:name_s],0,name_s)
                else:
                    ret_s = head.rfind(" ",0,name_s-1)
                
                    if ret_s > -1:
                        ret = (head[ret_s+1:name_s-1],ret_s+1,name_s-1)
                        spec = (head[:ret_s],0,ret_s)
                    else:
                        ret = (head[:name_s],0,name_s)
                        spec = ("",-1,-1)
                    
            else:
                name = (head[:params_s],0,params_s)
                ret = ("",-1,-1)
                spec = ("",-1,-1)
            
            r = (spec,ret,name,params,pure,dest,ctors)
            return r
    return None
#@nonl
#@-node:AGP.20230214111049.58:SplitFunc
#@+node:AGP.20230214111049.59:SplitParams
def SplitParams(params):
    params = params.strip("()")
    plist = params.split()
    params = string.join(plist)
    plist = params.split(",")
    
    for i in range(len(plist)):
        t=n=a=""
        prm = plist[i].strip()
        ac = prm.split("=")
        if len(ac) > 1:
            prm = ac[0]
            a = ac[1]
        else:
            a = None
        
        tns = prm.rfind(" ")#used rsplit but not avaible in py2.3
        
        if tns > -1:
            t = prm[:tns]
            n = prm[tns:]
        else:
            return None
        
        plist[i] = (t,n,a)
    
    
    return plist
            
#@nonl
#@-node:AGP.20230214111049.59:SplitParams
#@-node:AGP.20230214111049.57:C++ parsing
#@-node:AGP.20230214111049.42:Helpers
#@-node:AGP.20230214111049.27:Module level
#@+node:AGP.20230214111049.60:Classes
#@+node:AGP.20230214111049.61:class controllerClass
class controllerClass:

    #@    @+others
    #@+node:AGP.20230214111049.62:__init__
    def __init__ (self,c):
        
        self.c = c
        
        self.goingto = False
        
        #@    @+others
        #@+node:AGP.20230214111049.63:Xcc Core
        self.XCC_INITED = False
        
        self.ACTIVE_NODE = None
        self.ACTIVE_DICT = None
        self.ACTIVE_PROCESS = None
        
        self.SELECTED_NODE = None
        self.SELECTED_DICT = None
        
        self.LOCATE_CHILD = True
        self.CHILD_NODE = None
        self.CHILD_DICT = {}
        self.CHILD_LINE = None
        self.CHILD_EXT = None
        
        self.Parser = None
        #@nonl
        #@-node:AGP.20230214111049.63:Xcc Core
        #@+node:AGP.20230214111049.64:Browse Info
        self.NAME = ""
        self.EXT = ""
        self.HDR_EXT = ""
        self.SRC_EXT = ""
        self.BIN_EXT = ""
        self.ABS_PATH = ""
        self.REL_PATH = ""
        self.CWD = ""
        self.PARSE_ERROR = ""
        self.PARSE_ERROR_NODE = None
        self.CPPEXTS = ["h","cpp","c","dll","lib","exe"]
        #@nonl
        #@-node:AGP.20230214111049.64:Browse Info
        #@+node:AGP.20230214111049.65:Write Info
        self.CWD = os.getcwd().replace("\\",path_sym)
        self.CMT = "//"
        self.CREATE_DOC = "False"
        #@nonl
        #@-node:AGP.20230214111049.65:Write Info
        #@+node:AGP.20230214111049.66:Compile Info
        self.FIRST_ERROR = False
        self.CPL = {}
        self.COMPILE = False
        self.LINK = False
        self.OUTEXT = ""
        
        self.DEBUG = False
        self.EXECUTE = False
        self.CPL_ERR_REGEXP = None
        self.LKR_ERR_REGEXP = None
        self.SEEK_FIRST_ERROR = False
        
        self.EOL = ""
        #@nonl
        #@-node:AGP.20230214111049.66:Compile Info
        #@+node:AGP.20230214111049.67:Debug Info
        self.DBG = None
        
        self.DEBUGGER = ""
        self.TARGET_PID = ""
        
        self.DBG_RUNNING = False
        self.DBG_PROMPT = False
        self.DBG_PROMPT_REGEXP = None
        
        self.DBG_TASK = []
        self.DBG_SD = []
        self.DBG_RD = []
        self.PROMPT_RD = []
        
        self.DBG_STEPPING = False
        self.WATCH_TASK = None
        
        #	pipe char buffering
        self.OutBuff = ""
        self.ErrBuff = ""
        #@nonl
        #@-node:AGP.20230214111049.67:Debug Info
        #@+node:AGP.20230214111049.68:Execute Info
        self.EXE = None
        #@nonl
        #@-node:AGP.20230214111049.68:Execute Info
        #@+node:AGP.20230214111049.69:Options
        self.FILTER_OUTPUT = False
        self.VERBOSE = False
        self.OPTS = {}
        #@nonl
        #@-node:AGP.20230214111049.69:Options
        #@+node:AGP.20230214111049.70:Code Decorations
        self.CLASS_HDR = self.CMT+5*"------------------"+"\n"
        self.CLASS_OPN = "{\n"
        self.CLASS_END = "};\n"
            
        self.FUNC_HDR = self.CMT+5*"------------------"+"\n"
        self.FUNC_OPN = "{\n"
        self.FUNC_END = "}\n"
        #@nonl
        #@-node:AGP.20230214111049.70:Code Decorations
        #@+node:AGP.20230214111049.71:Leo's Controls shortcut
        
        self.LeoTop = c
        self.LeoFrame = c.frame	
        
        self.LeoBodyText = self.LeoFrame.body.bodyCtrl
        self.LeoBodyParent = self.LeoBodyText.nametowidget(self.LeoBodyText.winfo_parent())
        self.LeoYBodyBar = self.LeoFrame.body.bodyBar
        self.LeoXBodyBar = self.LeoFrame.body.bodyXBar
        
        self.LeoFont = self.LeoBodyText["font"]
        self.LeoWrap = self.LeoBodyText["wrap"]
        #@nonl
        #@-node:AGP.20230214111049.71:Leo's Controls shortcut
        #@+node:AGP.20230214111049.72:Widgets
        self.Config = ConfigClass(self)
        self.BreakBar = BreakbarClass(self)
        self.Dasm = DasmClass(self)
        self.Watcher = WatcherClass(self)
        self.DocEdit = DocEditClass(self)
        self.ToolBar = ToolbarClass(self) # must be created after BreakBar.
        #@-node:AGP.20230214111049.72:Widgets
        #@-others
        g.enableIdleTimeHook(idleTimeDelay=100)
    #@nonl
    #@-node:AGP.20230214111049.62:__init__
    #@+node:AGP.20230214111049.73:Event handlers
    #@+node:AGP.20230214111049.74:onSelect
    def onSelect(self):    
        cc = self
        p = cc.c.currentPosition()
        
        
        if IsXcc(p):
            cc.cSelect()
            cc.sSelect(p)        
        else:
            p2 = GetXccNode(p)
            if p2:
                if p2 != cc.SELECTED_NODE:
                    cc.sSelect(p2)
                cc.cSelect(p)
                
            else:
                cc.cSelect()
                cc.sSelect()
            
    #@nonl
    #@-node:AGP.20230214111049.74:onSelect
    #@+node:AGP.20230214111049.75:onIdle
    def onIdle(self):
    
        cc = self
        cc.UpdateProcess()
        cc.BreakBar.IdleUpdate()
    #@nonl
    #@-node:AGP.20230214111049.75:onIdle
    #@+node:AGP.20230214111049.76:onCommand2
    def onCommand2(self,keywords):
        cc = self
        label = keywords.get("label")
        #print "oncommand():"
        if label in ["undo","redo","backward-delete-char","delete-char","cut-text","paste-text"]:
            if cc.SELECTED_NODE:
                cc.BreakBar.bodychanged = True
    #@nonl
    #@-node:AGP.20230214111049.76:onCommand2
    #@+node:AGP.20230214111049.77:onBodyDoubleClick
    def onBodyDoubleClick(self):
    
        cc = self
    
        if cc.SELECTED_NODE == cc.c.currentPosition():
            cc.sGoToError()
    #@nonl
    #@-node:AGP.20230214111049.77:onBodyDoubleClick
    #@+node:AGP.20230214111049.78:onBodyKey2
    def onBodyKey2(self,keywords):   
        cc = self
        ch = keywords.get("ch")    
        
        cc.LeoBodyText.tag_delete("xcc_error")
            
        if cc.CHILD_NODE and ch == "\n":
            cc.BreakBar.BreaksFromTags()
    #@nonl
    #@-node:AGP.20230214111049.78:onBodyKey2
    #@+node:AGP.20230214111049.79:onHeadKey2
    def onHeadKey2(self,keywords):    
        cc = self
        p = cc.c.currentPosition()
        #print "onheadkey2"
        if IsXcc(p):
            
            if cc.c.openDirectory == None:
                p.setHeadString(p.headString()[1:])
                Error("xcc: ","Must save Leo file before using xcc node!")
                return
            
            
            if not cc.SELECTED_NODE:
                cc.sSelect(p)
            
            if cc.sGet("INITED","False") == "False":
                cc.sInitDict()
            
            cc.sGetBrowseInfo()
        else:
            p2 = GetXccNode(p)
            if p2:
                cc.sSelect(p2)
                cc.cSelect(p)
                
            #    try:
            #        cc.ParseTree()
            #        cc.c.redraw()
            #    except:
            #        TraceBack();
            #cc.sSelect(p2)
                #cc.cSelect(p)
    #@nonl
    #@-node:AGP.20230214111049.79:onHeadKey2
    #@+node:AGP.20230214111049.80:onQuit
    def onQuit(self):    
        cc = self
      
        if cc.ACTIVE_NODE:
            cc.GoToNode(cc.ACTIVE_NODE)
            cc.aStop()
            while cc.ACTIVE_NODE:
                cc.UpdateProcess()
    #@nonl
    #@-node:AGP.20230214111049.80:onQuit
    #@-node:AGP.20230214111049.73:Event handlers
    #@+node:AGP.20230214111049.81:Utility
    #@+node:AGP.20230214111049.82:GoToNode
    def GoToNode(self,node,index=None,tagcolor=None):
        
        if not node or self.goingto: return
        
        self.goingto = True # avoid recursion
        
        cc = self ; c = cc.c ; w = cc.LeoBodyText
        
        c.beginUpdate()
        if not node.isVisible():
            for p in node.parents_iter():
                p.expand()
        c.selectPosition(node)
        c.endUpdate()
    
        if index is None: return
        w.mark_set("insert",index)
        w.see(index)
    
        if tagcolor is None: return 
        l,c = w.index("insert").split(".")
        w.tag_add("xcc_error",l+".0",l+".end")
        w.tag_config("xcc_error",background=tagcolor)
        w.tag_raise("xcc_error")
        
        self.goingto = False
    #@nonl
    #@-node:AGP.20230214111049.82:GoToNode
    #@+node:AGP.20230214111049.83:UpdateProcess
    def UpdateProcess(self):
        
        #g.trace(ProcessClass.List)
        
        cc = self
        if len(ProcessClass.List) > 0:
            process = ProcessClass.List[0]
            if process.Update():
                #g.es("update")
                return
            if process.Close():
                ProcessClass.List = [] #reset
            else:
                ProcessClass.List.pop(0)
                if ProcessClass.List:
                    if not ProcessClass.List[0].Open():
                        ProcessClass.List = [] #reset
    #@nonl
    #@-node:AGP.20230214111049.83:UpdateProcess
    #@+node:AGP.20230214111049.84:ReplaceVars
    def ReplaceVars(self,exp):
    	exp = exp.replace("_NAME_",self.NAME)
    	exp = exp.replace("_EXT_",self.OUTEXT)
    	exp = exp.replace("_ABSPATH_",self.ABS_PATH)
    	exp = exp.replace("_RELPATH_",self.REL_PATH)
        
    	if self.EXT == self.HDR_EXT:
            exp = exp.replace("_SRCEXT_",self.HDR_EXT)
        else:
            exp = exp.replace("_SRCEXT_",self.SRC_EXT)
            
    	exp = exp.replace("\\",path_sym)
    	return exp
    	
    #@nonl
    #@-node:AGP.20230214111049.84:ReplaceVars
    #@+node:AGP.20230214111049.85:GetUnknownAttributes
    def GetUnknownAttributes(self,vnode,create = False):
    
    	if hasattr(vnode,"unknownAttributes") != True:
    		if create == True:
    			vnode.unknownAttributes = {}
    		else:
    			return None
    	return vnode.unknownAttributes
    #@nonl
    #@-node:AGP.20230214111049.85:GetUnknownAttributes
    #@+node:AGP.20230214111049.86:HideWidgets
    def HideWidgets(self):
        if self.Config.visible:
            self.Config.Hide()
                
        if self.DocEdit.visible:
            self.DocEdit.Hide()
            
        if self.Watcher.visible:
            self.Watcher.Hide()
            
        if self.Dasm.visible:
            self.Dasm.Hide()
    #@nonl
    #@-node:AGP.20230214111049.86:HideWidgets
    #@+node:AGP.20230316112635.1:CleanXccDicts
    def CleanXccDicts(self):
        cnt = 0
        for p in self.c.allNodes_iter(): 
            ua = self.GetUnknownAttributes(p.v)
            if ua:
                if hasattr(ua,"xcc_child_cfg"):
                    cfg = ua["xcc_child_cfg"]
        
        g.es("xcc: dropped %d empty dictionaries" % cnt)
    #@nonl
    #@-node:AGP.20230316112635.1:CleanXccDicts
    #@-node:AGP.20230214111049.81:Utility
    #@+node:AGP.20230214111049.87:Child Node Funcs
    #@+node:AGP.20230214111049.88:cIs
    def cIs(self,node):
    
        for p in node.parents_iter():
            if p.headString()[0:5] == "@xcc ":
                return True	
        return False
    #@nonl
    #@-node:AGP.20230214111049.88:cIs
    #@+node:AGP.20230214111049.89:cSet
    def cSet(self,name,value,node=None):    
        cc = self
        if node == None:
            if cc.CHILD_DICT != None:
                cc.CHILD_DICT[name] = value
        else:
            v = node.v    
            
            if not hasattr(v,"unknownAttributes"):
                v.unknownAttributes = ua = {}
            else:
                ua	=	v.unknownAttributes
        
            if "xcc_child_cfg" not in ua:
                ua["xcc_child_cfg"] = cfg = {}
            else:
                cfg = ua["xcc_child_cfg"]
                
            cfg[name] = value
            
    #@-node:AGP.20230214111049.89:cSet
    #@+node:AGP.20230214111049.90:cGet
    def cGet(self,name,init="",node=None):
        
        cc = self
        cfg = None
        
        if node == None:
            if cc.CHILD_DICT != None:
                cfg = cc.CHILD_DICT
            else:
                return init
        else:
            v = node.v
        
            if hasattr(v,"unknownAttributes"):
                ua	=	v.unknownAttributes
        
                if "xcc_child_cfg" in ua:
                    cfg = ua["xcc_child_cfg"]
    
        if cfg and name in cfg:
            return cfg[name]
                
        return init
    #@nonl
    #@-node:AGP.20230214111049.90:cGet
    #@+node:AGP.20230214111049.91:cSelect
    def cSelect(self,node=None):
        
        cc = self
    
        if node:
            cc.Config.Hide()
            cc.CHILD_NODE = node
            cc.CHILD_DICT = cc.cGetDict()
            #print cc.CHILD_DICT
            
            if cc.DocEdit.visible:
                cc.DocEdit.LoadFromNode()
            
            if cc.LOCATE_CHILD:
                #print "cSelect():"
                
                
                
                loc = LocatorClass(cc,cc.CHILD_NODE,1)
                cc.CHILD_EXT = loc.FOUND_FILE_EXT
                cc.CHILD_LINE = loc.FOUND_FILE_LINE								
                
                """print "loc",loc.CURRENT_LOCATION
                print "hdr src",loc.HEADER.CURRENT_LINE,loc.SOURCE.CURRENT_LINE
                print "head",loc.FOUND_HEAD_HDR_LINE,loc.FOUND_HEAD_SRC_LINE
                print "body",loc.FOUND_BODY_HDR_LINE,loc.FOUND_BODY_SRC_LINE,loc.CURRENT_BODY_LINE
                print "file",loc.FOUND_FILE_LINE,loc.FOUND_FILE_EXT
                print loc.FOUND_OTHERS"""
                
                #if loc.FOUND_FILE_EXT:
                cc.BreakBar.Show(loc)
                #cc.ToolBar.SyncDisplayToChild(loc)
                #else:
                #    cc.ToolBar.SyncDisplayToError()
                
                
                
        
        elif cc.CHILD_NODE:
            cc.BreakBar.Hide()
            cc.CHILD_NODE = None
            cc.CHILD_DICT = None
            cc.CHILD_LINE = None
            cc.CHILD_EXT = None
    #@nonl
    #@-node:AGP.20230214111049.91:cSelect
    #@+node:AGP.20230214111049.92:cGetDict
    def cGetDict(self,node=None,create=False):#Get xcc child dict alias "xcc_child_cfg" in ua	
        #the func must return the CHILD_NODE dict if node == None
        cc = self
    
        if node == None:
            node =	cc.CHILD_NODE
        
        v = node.v
        
        if not hasattr(v,"unknownAttributes"):
            if create != True:
                return None
            v.unknownAttributes = {}		
        
        if "xcc_child_cfg" not in v.unknownAttributes:
            if create != True:
                return None
            v.unknownAttributes["xcc_child_cfg"] = {}    
                
        return v.unknownAttributes.get("xcc_child_cfg")
    #@-node:AGP.20230214111049.92:cGetDict
    #@-node:AGP.20230214111049.87:Child Node Funcs
    #@+node:AGP.20230214111049.93:Selected Node Funcs
    #@+node:AGP.20230214111049.94:sGatherInfo NOT CALLED
    #@+node:AGP.20230214111049.95:Head
    #@-node:AGP.20230214111049.95:Head
    #@+node:AGP.20230214111049.96:Dicts
    #@-node:AGP.20230214111049.96:Dicts
    #@+node:AGP.20230214111049.97:File Creation
    #@-node:AGP.20230214111049.97:File Creation
    #@+node:AGP.20230214111049.98:Compilation
    #@-node:AGP.20230214111049.98:Compilation
    #@+node:AGP.20230214111049.99:Execution
    #@-node:AGP.20230214111049.99:Execution
    #@+node:AGP.20230214111049.100:Debugging
    #@-node:AGP.20230214111049.100:Debugging
    #@-node:AGP.20230214111049.94:sGatherInfo NOT CALLED
    #@+node:AGP.20230214111049.101:sExtractHeadInfo
    def sExtractHeadInfo (self):
        
        cc = self
    
        w = cc.SELECTED_NODE.headString() [5:]
        if w:
            path, name = os.path.split(w)
            name, ext = os.path.splitext(name)
            ext = ext.lower().replace(".","") or 'exe'
        else:
            path, name, ext = '', '', ''
    
        cc.sSet("REL_PATH",path)
        cc.sSet("NAME",name)
        cc.sSet("EXT",ext)
        theDir = g.choose(path,cc.CWD+"/"+path,cc.CWD)
        cc.sSet("ABS_PATH",theDir)
    #@nonl
    #@-node:AGP.20230214111049.101:sExtractHeadInfo
    #@+node:AGP.20230214111049.102:sGetBrowseInfo
    def sGetBrowseInfo (self):
        cc = self
        
        
        w = cc.SELECTED_NODE.headString() [5:]
        if w:
            cc.REL_PATH, cc.NAME = os.path.split(w)
            cc.NAME, EXT = os.path.splitext(cc.NAME)
            cc.EXT = EXT.lower().replace(".","")
        else:
            cc.REL_PATH, cc.NAME, cc.EXT = '', '', ''    
    
        cc.CWD = cc.ABS_PATH = cc.c.openDirectory#os.getcwd().replace("\\","/")
        
        if cc.REL_PATH and cc.REL_PATH[1] != ":": cc.ABS_PATH = cc.ABS_PATH + "/" + cc.REL_PATH
        
        cc.ABS_PATH = cc.ABS_PATH.replace("\\",path_sym)
        cc.REL_PATH = cc.REL_PATH.replace("\\",path_sym)
        
        cc.OPTS = cc.sGet("Options",{})
        cc.LANG = cc.sGet("Language",{})
        cc.HDR_EXT = GetDictKey(cc.LANG,"Header ext",create=True,init="h")
        cc.SRC_EXT = GetDictKey(cc.LANG,"Source ext",create=True,init="c")
        cc.BIN_EXT = GetDictKey(cc.LANG,"Binary ext",create=True,init="exe")
        
        
        co = GetDictKey(cc.LANG,"Class opening",create=True,init="")
        ce = GetDictKey(cc.LANG,"Class closing",create=True,init="")
        fo = GetDictKey(cc.LANG,"Fonction opening",create=True,init="")
        fe = GetDictKey(cc.LANG,"Fonction closing",create=True,init="")
        
        code = "self.CLASS_OPN = \""+co+"\"\n"
        code += "self.CLASS_END = \""+ce+"\"\n"
        code += "self.FUNC_OPN = \""+fo+"\"\n"
        code += "self.FUNC_END = \""+fe+"\""
        
        try:
            exec code
        
        except Exception as e:
            Error("xcc :sGetBrowseInfo()",e)
        
        
        
        
        if cc.EXT == "":
            cc.EXT = cc.BIN_EXT
    #@nonl
    #@-node:AGP.20230214111049.102:sGetBrowseInfo
    #@+node:AGP.20230214111049.103:sGetWriteInfo
    def sGetWriteInfo(self):
        
        cc = self
        
        if cc.NAME == "":
            return Error("xcc: ","Node have no name!")
            
        cc.CMT = GetDictKey(cc.LANG,"Comment symbol",create=True,init="//")
        if cc.CMT == "":
            cc.CMT = cc.LANG["Comment symbol"] = "//"
        
        
        if cc.REL_PATH != "" and os.access(cc.ABS_PATH,os.F_OK) != 1:
            os.makedirs(cc.ABS_PATH)
        
        if cc.OPTS.get("Create files") == "True":
            cc.CREATE_DOC = cc.OPTS.get("Doc files")
            cc.PYWRAP = cc.OPTS.get("Python wrapper")
        else:
            cc.CREATE_DOC = "False"
            cc.PYWRAP = "False"
        
        
            
        co = GetDictKey(cc.LANG,"Class opening",create=True,init="")
        ce = GetDictKey(cc.LANG,"Class closing",create=True,init="")
        fo = GetDictKey(cc.LANG,"Fonction opening",create=True,init="")
        fe = GetDictKey(cc.LANG,"Fonction closing",create=True,init="")
        
        code = "self.CLASS_OPN = \""+co+"\"\n"
        code += "self.CLASS_END = \""+ce+"\"\n"
        code += "self.FUNC_OPN = \""+fo+"\"\n"
        code += "self.FUNC_END = \""+fe+"\""
        
        try:
            exec code
        
        except Exception as e:
            Error("xcc :sGetWriteInfo()",e)
        
        self.CLASS_HDR = self.CMT+5*"------------------"+"\n"
        self.FUNC_HDR = self.CMT+5*"------------------"+"\n"
        
        return True
    #@nonl
    #@-node:AGP.20230214111049.103:sGetWriteInfo
    #@+node:AGP.20230214111049.104:sGetCompileInfo
    def sGetCompileInfo(self):
        
        cc = self
        cc.CPL = cc.sGet("Compiler")
        cc.LKR = cc.sGet("Linker")
    
        if not cc.CPL.get("Compiler"):
            return Error("xcc: ","No compiler defined!")
            
        cc.VERBOSE = StrToBool(cc.OPTS.get("Xcc verbose"))
        cc.DEBUG = StrToBool(cc.OPTS.get("Debug"))
        cc.EXECUTE = StrToBool(cc.OPTS.get("Execute"))
        cc.SEEK_FIRST_ERROR = StrToBool(cc.OPTS.get("Seek first error"))
        
        #compiling compiler & linker error detection regexp
        cc.CPL_ERR_REGEXP = re.compile(cc.CPL.get("Error detection"),re.IGNORECASE) 
        cc.LKR_ERR_REGEXP = re.compile(cc.LKR.get("Error detection"),re.IGNORECASE)
        
        return True
    
    
    #@-node:AGP.20230214111049.104:sGetCompileInfo
    #@+node:AGP.20230214111049.105:sGetDebugInfo
    def sGetDebugInfo(self):
        
        cc = self
       
        cc.DBG = cc.sGet("Debugger")
        if cc.DBG["Debugger"]:
            self.DBG_PROMPT_REGEXP = re.compile(cc.DBG.get("Prompt pattern"))
            return True
        else:
            return Error("xcc: ","No debugger defined!")
    #@nonl
    #@-node:AGP.20230214111049.105:sGetDebugInfo
    #@+node:AGP.20230214111049.106:sGetExecInfo
    def sGetExecInfo(self):
        
        cc = self
    
        cc.EXE = cc.sGet("Executable")		
        return True
    #@nonl
    #@-node:AGP.20230214111049.106:sGetExecInfo
    #@+node:AGP.20230214111049.107:sGoToError
    def sGoToError(self,e=None):#if e==None, retreive current body line
        
        cc = self
        
        mask = [" ",":","(",")"]
        if e == None:
            row,col = cc.LeoBodyText.index("insert").split(".")
            row = int(row)
            col = int(col)
            lines = cc.SELECTED_NODE.bodyString().splitlines()
            e = lines[row-1]
            #e=e.replace("/","\\")
        
        if cc.CPL_ERR_REGEXP:
            m = cc.CPL_ERR_REGEXP.search(e)
            if m != None:
                op = ""
                try:            
                    id = m.group("ID")
                    op += id
                except Exception:
                    pass
                try:
                    file = m.group("FILE")
                    op += " in "+file
                except Exception:
                    pass    
                try:
                    line = m.group("LINE")
                    op += " line "+line                
                except Exception:
                    pass            
                try:    
                    edef = m.group("DEF")
                    op += " : "+edef
                except Exception:
                    pass    
                
                path,name = os.path.split(cc.CPL["Compiler"])
                Error(name+" : ","Error: "+op)
            
                name,ext = os.path.splitext(file)
                if name == cc.NAME:
                    SeekErrorClass(cc,int(line),ext.replace(".",""),color=ErrorColor)
    #@nonl
    #@-node:AGP.20230214111049.107:sGoToError
    #@+node:AGP.20230214111049.108:sGo
    def sGo(self):	#this is where the selected node also become the active node
    
        cc = self
        
        cc.sGetBrowseInfo()
        
        if not cc.NAME:
            return Error("xcc: ","Node has no name!")
    
        if cc.LANG["Language"] == "":
            cc.LANG["Language"] == "c++"
            
            
        cc.sSetText("@language "+cc.LANG["Language"]+"\n")
        
        if not cc.sGetWriteInfo():
            return False
        if cc.OPTS.get("Create files") == "True":
            if cc.OPTS.get("Source files") == "True" or cc.OPTS.get("Doc files"):
                if not cc.CreateFiles():
                    return False
        
        cc.sGetExecInfo()
        if cc.OPTS.get("Build") == "True":        
            if not cc.sGetCompileInfo():
                return False
            
            
            bs = cc.OPTS.get("Build sequence").splitlines() 
            for s in bs:
                if s != "":
                    s = s.strip()
                    if s == "COMPILE":
                        cc.COMPILE = True           
                        if cc.Compile() == "False":
                            return False
                        else:
                            continue
                    if s == "LINK":
                        cc.LINK = True           
                        if cc.Link() == "False":
                            return False
                        else:
                            continue                
                    if cc.RunTool(cc,s) == "False":
                            return False
                
        if cc.EXECUTE and cc.EXT != cc.HDR_EXT:
            if cc.DEBUG:
                if not cc.Debug():
                    return False
            else:
                if not cc.Execute():
                    return False        
        
        return True
    
    
    #@-node:AGP.20230214111049.108:sGo
    #@+node:AGP.20230214111049.109:sSet
    def sSet (self,name,value):
        
        cc = self
    
        cc.SELECTED_DICT [name] = value
    #@-node:AGP.20230214111049.109:sSet
    #@+node:AGP.20230214111049.110:sGet
    def sGet(self,name,init=""):
        
        cc = self
        
        if name not in cc.SELECTED_DICT:
            cc.sSet(name,init)
    
        return cc.SELECTED_DICT[name]
    #@nonl
    #@-node:AGP.20230214111049.110:sGet
    #@+node:AGP.20230214111049.111:sIsDict
    def sIsDict(self):
        
        cc = self
    
        if not cc.SELECTED_NODE:
            return False
        
        v = cc.SELECTED_NODE.v	
        
        return hasattr(v,"unknownAttributes") and "xcc_cfg" in v.unknownAttributes
    #@nonl
    #@-node:AGP.20230214111049.111:sIsDict
    #@+node:AGP.20230214111049.112:sGetDict
    def sGetDict(self): # Get xcc parent dict alias "xcc_cfg" in ua
    
        cc = self
    
        if not cc.SELECTED_NODE:
            return None
        
        v = cc.SELECTED_NODE.v
    
        if not hasattr(v,"unknownAttributes"):
            v.unknownAttributes = {}
        
        if "xcc_cfg" in v.unknownAttributes:
            return v.unknownAttributes["xcc_cfg"]
        else:
            v.unknownAttributes["xcc_cfg"] = d = {}
            return d
    #@nonl
    #@-node:AGP.20230214111049.112:sGetDict
    #@+node:AGP.20230214111049.113:sInitDict
    def sInitDict(self):
        
        cc = self
        
        Warning("xcc: ","Writing blank configuration!")
        cc.sSetText("@language c++")
        cc.Config.ClearConfig()
        cc.Config.SaveToNode()
        cc.sSet("INITED","True")
    
    
    
    #@-node:AGP.20230214111049.113:sInitDict
    #@+node:AGP.20230214111049.114:sSelect
    def sSelect(self,node=None):
        
        cc = self ; c = cc.c
    
        if node:
            if cc.SELECTED_NODE:
                cc.Config.Hide()
            
            cc.SELECTED_NODE = node        
            cc.SELECTED_DICT = cc.sGetDict()
            
            if cc.SELECTED_NODE != cc.ACTIVE_NODE and cc.SELECTED_NODE.isMarked():
                cc.SELECTED_NODE.clearMarked()
                c.redraw()
            
            cc.sGetBrowseInfo()
            cc.sShow()
        elif cc.SELECTED_NODE:
            cc.Config.Hide()        
            cc.sHide()
            cc.SELECTED_NODE = None
            cc.SELECTED_DICT = None
    #@nonl
    #@-node:AGP.20230214111049.114:sSelect
    #@+node:AGP.20230214111049.115:sSync
    def sSync(self):
        
        cc = self
        
        cc.SELECTED_DICT = cc.sGetDict()
        if cc.SELECTED_DICT:
            cc.sExtractHeadInfo()
        
        cc.CHILD_DICT = cc.cGetDict()
    #@nonl
    #@-node:AGP.20230214111049.115:sSync
    #@+node:AGP.20230214111049.116:sShow
    def sShow(self):
        
        cc = self
        
        if cc.Config.visible:
            cc.Config.Hide()        
        if cc.BreakBar.visible:
            cc.BreakBar.Hide()        
        
        
        cc.LeoBodyText.pack_forget()
        cc.LeoYBodyBar.pack_forget()
        cc.LeoXBodyBar.pack_forget()
        
        #show the toolbar
        cc.ToolBar.pack(side="top",fill="x")
        
        if cc.DocEdit.visible:
            cc.DocEdit.LoadFromNode()
            
        #show the watch pane
        if cc.Watcher.visible:
            cc.Watcher.pack(side = "bottom",fill="x")        
            cc.ToolBar.WatchButton.config(command=cc.Watcher.Hide,relief='sunken')
            #sync data to selected node
            cc.Watcher.Sync()
            
            #update watch data if running
            if cc.ACTIVE_PROCESS and cc.DBG_PROMPT and cc.SELECTED_NODE == cc.ACTIVE_NODE:
                WatchTaskClass(cc)
                cc.DbgOut("")
            
        cc.LeoXBodyBar.pack(side="bottom",fill="x")
        cc.LeoYBodyBar.pack(side="right",fill="y")
        cc.LeoBodyText.pack(fill="both",expand=1)
        cc.LeoBodyText.config(wrap='none')
        
    #@-node:AGP.20230214111049.116:sShow
    #@+node:AGP.20230214111049.117:sHide
    def sHide(self):
        
        cc = self
    
        cc.LeoXBodyBar.pack_forget()
        cc.ToolBar.pack_forget()
        
        #set back the wrapping mode
        cc.LeoBodyText.config(wrap=cc.LeoWrap)
        
        if cc.Watcher.visible:
            cc.Watcher.Hide()
            
        if cc.DocEdit.visible:
            cc.DocEdit.Hide()
    #@nonl
    #@-node:AGP.20230214111049.117:sHide
    #@+node:AGP.20230214111049.118:sSetText
    def sSetText(self,text=""):
        
        cc = self
        cc.c.setBodyString(cc.SELECTED_NODE,text)
    #@-node:AGP.20230214111049.118:sSetText
    #@+node:AGP.20230214111049.119:sAddText
    def sAddText(self,text):
        
        cc = self
        
        cc.c.setBodyString(cc.SELECTED_NODE,cc.SELECTED_NODE.bodyString()+text)
    
        if cc.CHILD_NODE == None:
            l,c = cc.LeoBodyText.index("end").split(".")
            cc.LeoBodyText.see(l+".0")
    #@nonl
    #@-node:AGP.20230214111049.119:sAddText
    #@-node:AGP.20230214111049.93:Selected Node Funcs
    #@+node:AGP.20230214111049.120:Active Node Funcs
    #@+node:AGP.20230214111049.121:aSet
    def aSet(self,name,value):
        
        cc = self
        
        cc.ACTIVE_DICT[name] = value
    #@-node:AGP.20230214111049.121:aSet
    #@+node:AGP.20230214111049.122:aGet
    def aGet(self,name,init=""):
        
        cc = self
        
        if name not in cc.ACTIVE_DICT:
            cc.aSet(name,init)
    
        return cc.ACTIVE_DICT[name]
    #@-node:AGP.20230214111049.122:aGet
    #@+node:AGP.20230214111049.123:aGetDict
    def aGetDict(self):
        
        '''Get xcc parent dict alias "xcc_cfg" in uA.'''
        
        cc = self
    
        if not cc.ACTIVE_NODE:
            return None
        
        v = cc.ACTIVE_NODE.v	
        if not hasattr(v,"unknownAttributes"):
            v.unknownAttributes = {}
        
        if "xcc_cfg" not in v.unknownAttributes:
            v.unknownAttributes["xcc_cfg"] = {}
        
        return v.unknownAttributes.get("xcc_cfg")
    #@nonl
    #@-node:AGP.20230214111049.123:aGetDict
    #@+node:AGP.20230214111049.124:aGo
    def aGo(self):
        
        #g.trace()
        
        cc = self
        
        if cc.ACTIVE_NODE:
            s = cc.DBG.get("Continue")
            if s:
                cc.aWrite(s)
                cc.LeoBodyText.tag_delete("xcc_error")
                cc.ToolBar.DisableStep()
    #@nonl
    #@-node:AGP.20230214111049.124:aGo
    #@+node:AGP.20230214111049.125:aStop
    def aStop(self):
        try:
            cc = self
       
            if not cc.ACTIVE_NODE or not cc.ACTIVE_PROCESS:
                return Error("xcc: ","Current xcc node is not active!")
    
            if cc.ACTIVE_NODE == cc.SELECTED_NODE and cc.TARGET_PID:
                stop = cc.DBG.get("Stop")
                if cc.DBG_PROMPT:
                    if stop: cc.aWrite(stop)
                else:
                    pause(cc.TARGET_PID)
                    if stop: cc.DBG_TASK.append(DbgTaskClass(cc,stop))					
                
                cc.LeoBodyText.tag_delete("xcc_error")
                if cc.WATCH_TASK: cc.WATCH_TASK.Cancel()
        except Exception:
            g.es_exception()
    #@nonl
    #@-node:AGP.20230214111049.125:aStop
    #@+node:AGP.20230214111049.126:aStepIn
    def aStepIn(self):
        try:
            cc = self
       
            if (
                cc.ACTIVE_NODE and cc.ACTIVE_PROCESS and
                cc.ACTIVE_NODE == cc.SELECTED_NODE and
                cc.DBG["Step in"] != "" and cc.DBG_PROMPT
            ):
                cc.DBG_STEPPING = True
                cc.aWrite(cc.DBG["Step in"])
                cc.ToolBar.DisableStep()
                cc.LeoBodyText.tag_delete("xcc_error")
                cc.DBG_TASK.append(QueryGoTaskClass(cc))
        except Exception:
            g.es_exception()
    #@nonl
    #@-node:AGP.20230214111049.126:aStepIn
    #@+node:AGP.20230214111049.127:aStepOver
    def aStepOver(self):
        try:
            cc = self
        
            if (
                cc.ACTIVE_NODE and cc.ACTIVE_PROCESS and
                cc.ACTIVE_NODE == cc.SELECTED_NODE and
                cc.DBG.get("Step in") and cc.DBG_PROMPT
            ):
                cc.DBG_STEPPING = True			
                cc.aWrite(cc.DBG["Step over"])
                cc.ToolBar.DisableStep()
                cc.LeoBodyText.tag_delete("xcc_error")
                cc.DBG_TASK.append(QueryGoTaskClass(cc))
        except Exception:
            g.es_exception()
    #@-node:AGP.20230214111049.127:aStepOver
    #@+node:AGP.20230214111049.128:aStepOut
    def aStepOut(self):
        try:
            cc = self
    
            if (
                cc.ACTIVE_NODE and cc.ACTIVE_PROCESS and
                cc.ACTIVE_NODE == cc.SELECTED_NODE and
                cc.DBG.get("Step in") and cc.DBG_PROMPT
            ):
                cc.DBG_STEPPING = True
                cc.aWrite(cc.DBG["Step out"])
                cc.ToolBar.DisableStep()
                cc.LeoBodyText.tag_delete("xcc_error")
                cc.DBG_TASK.append(QueryGoTaskClass(cc))
        except Exception:
            g.es_exception()
    #@nonl
    #@-node:AGP.20230214111049.128:aStepOut
    #@+node:AGP.20230214111049.129:aPause
    def aPause(self):
        try:
            cc = self
        
            if not cc.ACTIVE_NODE or not cc.ACTIVE_PROCESS:
                Error("xcc: ","Current xcc node is not active!")
    
            elif cc.ACTIVE_NODE == cc.SELECTED_NODE and cc.TARGET_PID:
                pause(cc.TARGET_PID)
        except Exception:
            g.es_exception()
    #@nonl
    #@-node:AGP.20230214111049.129:aPause
    #@+node:AGP.20230214111049.130:aWrite
    def aWrite(self,text):
        
        cc = self
    
        if not cc.FILTER_OUTPUT:
            cc.aAddText(text+"\n")
        
        eol = ""   
        code = "eol = \""+cc.EOL+"\""    
        try:
            exec code
        except:
            TraceBack()
        
        if eol == "":
            eol = "\n"
        
        cc.ACTIVE_PROCESS.In.write(text+eol)
        cc.ACTIVE_PROCESS.In.flush()
        cc.DBG_PROMPT = False
        cc.ToolBar.PauseButton["state"] = 'normal'
        
        if cc.DEBUG and cc.EXECUTE:
            cc.ToolBar.HideInput()
    #@nonl
    #@-node:AGP.20230214111049.130:aWrite
    #@+node:AGP.20230214111049.131:aSelect
    def aSelect(self,node=None):
        
        cc = self
    
        cc.ACTIVE_NODE = node
        cc.ACTIVE_DICT = cc.aGetDict()
    #@nonl
    #@-node:AGP.20230214111049.131:aSelect
    #@+node:AGP.20230214111049.132:aSetText
    def aSetText(self,text=""):
        
        cc = self
        
        if cc.ACTIVE_NODE:
            cc.c.setBodyString(ACTIVE_NODE,text)
    #@nonl
    #@-node:AGP.20230214111049.132:aSetText
    #@+node:AGP.20230214111049.133:aAddText
    def aAddText(self,text):
        
        cc = self
        
        if cc.ACTIVE_NODE:
            cc.c.setBodyString(cc.ACTIVE_NODE,cc.ACTIVE_NODE.bodyString()+text)
        
            if cc.SELECTED_NODE == cc.ACTIVE_NODE and cc.CHILD_NODE==None:
                l,c = cc.LeoBodyText.index("end").split(".")
                cc.LeoBodyText.see(l+".0")
    #@nonl
    #@-node:AGP.20230214111049.133:aAddText
    #@-node:AGP.20230214111049.120:Active Node Funcs
    #@+node:AGP.20230214111049.134:Action Funcs
    #@+node:AGP.20230214111049.135:ParseTree
    def ParseTree(self):
        p = ParserClass(self)
        p.Parse()
    #@nonl
    #@-node:AGP.20230214111049.135:ParseTree
    #@+node:AGP.20230214111049.136:CreateFiles
    def CreateFiles(self):
    
        cc = self
        #g.trace(cc.OPTS)
        
        if cc.OPTS.get("Create files") == "True":
            return WriterClass(cc).Result
        else:
            return None
    #@nonl
    #@-node:AGP.20230214111049.136:CreateFiles
    #@+node:AGP.20230214111049.137:Compile
    def Compile(self):
        cc = self
        
        try:
            process = ProcessClass(cc,
                cc.SELECTED_NODE,
                cc.CPL.get("Compiler"),
                cc.CplCmd(),
                start=cc.CplStart,
                out=cc.CplOut,
                err=cc.CplErr,
                end=cc.CplEnd)
            
            return ProcessClass.QueueProcess(process)        
            
        except Exception:
            g.es_exception()
    #@nonl
    #@-node:AGP.20230214111049.137:Compile
    #@+node:AGP.20230214111049.138:CplCmd
    def CplCmd(self):
        
        cc = self
        cwd = os.getcwd()
    
        if cc.DEBUG:
            cmd = cc.CPL["Debug arguments"]
        else:
            cmd = cc.CPL["Arguments"]
        
        cmd = cc.ReplaceVars(cmd.replace("\n"," ").strip())
        
        #@    @+others
        #@+node:AGP.20230214111049.139:_INCPATHS_
        s = cc.CPL.get("Include path")
        if s:
            sym = s
            paths = cc.CPL.get("Include search paths",'').splitlines()
            cc.INCPATHS = ""
            for p in paths:
                if p != "":
                    cc.INCPATHS += " "+sym+"\""+p+"\""
            cmd = cmd.replace("_INCPATHS_",cc.INCPATHS.strip())
        #@nonl
        #@-node:AGP.20230214111049.139:_INCPATHS_
        #@+node:AGP.20230214111049.140:_LIBPATHS_
        s = cc.LKR.get("Library path")
        if s:
            sym = s
            paths = cc.LKR.get("Library search paths",'').splitlines()
            cc.LIBPATHS = ""
            for p in paths:
                if p != "":
                    cc.LIBPATHS += " "+sym+"\""+p+"\""
            cmd = cmd.replace("_LIBPATHS_",cc.LIBPATHS.strip())
        #@nonl
        #@-node:AGP.20230214111049.140:_LIBPATHS_
        #@+node:AGP.20230214111049.141:_LIBRARIES_
        s = cc.LKR.get("Use library")
        if s:
            sym = s
            libs = cc.LKR.get("Used libraries",'').split()
            cc.LIBRARIES = ""
            for l in libs:
                if l != "":
                    cc.LIBRARIES += " "+sym+"\""+l+"\""
            cmd = cmd.replace("_LIBRARIES_",cc.LIBRARIES.strip())
        #@nonl
        #@-node:AGP.20230214111049.141:_LIBRARIES_
        #@+node:AGP.20230214111049.142:_BUILD_
        if cc.OUTEXT == "dll":
            s = cc.LKR.get("Build dll")
        else:
            s = cc.LKR.get("Build exe")
            
        if s: cmd = cmd.replace("_BUILD_",s)
        #@nonl
        #@-node:AGP.20230214111049.142:_BUILD_
        #@-others
        
        return cmd
    
    
    #@-node:AGP.20230214111049.138:CplCmd
    #@+node:AGP.20230214111049.143:Link
    def Link(self):
        cc = self
        
        try:
            process = ProcessClass(cc,
                cc.SELECTED_NODE,
                cc.LKR.get("Linker"),
                cc.LkrCmd(),
                start=cc.LkrStart,
                out=cc.LkrOut,
                err=cc.LkrErr,
                end=cc.LkrEnd)
            
            return ProcessClass.QueueProcess(process)        
            
        except Exception:
            g.es_exception()
    #@nonl
    #@-node:AGP.20230214111049.143:Link
    #@+node:AGP.20230214111049.144:LkrCmd
    def LkrCmd(self):
        
        #g.trace()
        
        cc = self
        cwd = os.getcwd()
    
        if cc.DEBUG:
            cmd = cc.LKR["Debug arguments"]
        else:
            cmd = cc.LKR["Arguments"]
        
        cmd = cc.ReplaceVars(cmd.replace("\n"," ").strip())
        
        #@    @+others
        #@+node:AGP.20230214111049.145:_LIBPATHS_
        s = cc.LKR.get("Library path",'')
        if s:
            sym = s
            paths = cc.LKR.get("Library search paths",'').splitlines()
            cc.LIBPATHS = ""
            for p in paths:
                if p != "":
                    cc.LIBPATHS += " "+sym+"\""+p+"\""
            cmd = cmd.replace("_LIBPATHS_",cc.LIBPATHS.strip())
        #@nonl
        #@-node:AGP.20230214111049.145:_LIBPATHS_
        #@+node:AGP.20230214111049.146:_LIBRARIES_
        s = cc.LKR.get("Use library")
        if s:
            sym = s
            libs = cc.LKR.get("Used libraries",'').split()
            cc.LIBRARIES = ""
            for l in libs:
                if l != "":
                    cc.LIBRARIES += " "+sym+"\""+l+"\""
            cmd = cmd.replace("_LIBRARIES_",cc.LIBRARIES.strip())
        #@nonl
        #@-node:AGP.20230214111049.146:_LIBRARIES_
        #@+node:AGP.20230214111049.147:_BUILD_
        if cc.OUTEXT == "exe":
            s = cc.LKR.get("Build exe")
            if s: cmd = cmd.replace("_BUILD_",s)
        
        if cc.OUTEXT == "dll":
            s = cc.LKR.get("Build dll")
            if s: cmd = cmd.replace("_BUILD_",s)
        #@nonl
        #@-node:AGP.20230214111049.147:_BUILD_
        #@-others
    
        return cmd
    
    
    #@-node:AGP.20230214111049.144:LkrCmd
    #@+node:AGP.20230214111049.148:Debug
    def Debug(self):
        
        cc = self
        if cc.sGetDebugInfo() and cc.OUTEXT == cc.BIN_EXT:
            process = ProcessClass(cc,
                cc.SELECTED_NODE,
                cc.DBG.get("Debugger"),
                cc.DbgCmd(),
                start=cc.DbgStart,
                out=cc.DbgOut,
                err=cc.DbgErr,
                end=cc.DbgEnd)
                
            return ProcessClass.QueueProcess(process)
        return False
    #@nonl
    #@-node:AGP.20230214111049.148:Debug
    #@+node:AGP.20230214111049.149:DbgCmd
    def DbgCmd(self):
        
        cc = self
        
        cmd = cc.DBG.get("Arguments").replace("\n"," ").strip()
        cmd = cc.ReplaceVars(cmd)
        
        #g.trace(repr(cmd))
        return cmd
    #@nonl
    #@-node:AGP.20230214111049.149:DbgCmd
    #@+node:AGP.20230214111049.150:Execute
    def Execute(self):    
        #g.trace()
        
        cc = self
        
        cmd = cc.ABS_PATH+"/"+cc.NAME+"."+cc.OUTEXT
        args = cc.EXE.get("Execution arguments")
            
        if cc.OPTS.get("Connect to pipe") == "True":
            g.es("piping")
            process = ProcessClass(cc,
                cc.SELECTED_NODE,
                cmd,
                args,
                start=cc.ProgStart,
                out=cc.ProgOut,
                err=cc.ProgErr,
                end=cc.ProgEnd)
        else:
            process = ProcessClass(cc,cc.SELECTED_NODE,cmd,args,spawn=True)
    
        return ProcessClass.QueueProcess(process)
    #@-node:AGP.20230214111049.150:Execute
    #@+node:AGP.20230214111049.151:RunTool
    def RunTool(self,cc,cmdl):
        ca = cmdl.split("@",1)
        if len(ca) == 1: 
            cmd = ca[0]
            args =""
        if len(ca) == 2: 
            cmd = ca[0]
            args = ca[1]                
        
        process = ProcessClass(cc,
            cc.SELECTED_NODE,
            cc.ReplaceVars(cmd),
            cc.ReplaceVars(args),
            start=cc.ProgStart,
            out=cc.ProgOut,
            err=cc.ProgErr,
            end=cc.ProgEnd)
                
        return ProcessClass.QueueProcess(process)
    #@nonl
    #@-node:AGP.20230214111049.151:RunTool
    #@-node:AGP.20230214111049.134:Action Funcs
    #@+node:AGP.20230214111049.152:Compiler Events
    #@+node:AGP.20230214111049.153:CplStart
    def CplStart(self):
        cc = self
        cc.OutBuff = ""
        cc.ErrBuff = ""
        cc.FIRST_ERROR = False
        cc.aSelect(cc.SELECTED_NODE)
        process = ProcessClass.List[0]    
        
        text = ""	
        if cc.VERBOSE:
            if cc.LINK == True:
                pn = "Compiling"
            else:
                pn = "Building"       
            
            text += "\" "+pn+"...  Starting "+process.FileName+"...\n"
            text += "\" using arguments: "+process.Arguments+"\n"		
        text += "\""+("="*60)+"\n"
        
        cc.aAddText(text)
    #@-node:AGP.20230214111049.153:CplStart
    #@+node:AGP.20230214111049.154:CplOut
    def CplOut(self,text):
        cc = self
        cc.OutBuff += text
        lines = cc.OutBuff.splitlines(True)
        
        last_char = lines[-1][-1]
        if last_char != "\n" and last_char != "\r":
            cc.OutBuff = lines.pop()
        else:
            cc.OutBuff = ""
        
        text = ""	
        for l in lines:
            if l != "":
                if cc.CPL_ERR_REGEXP:
                    m = cc.CPL_ERR_REGEXP.search(l,re.IGNORECASE)
                    if m != None:
                        text += cc.CMT+" "+l
                        if cc.SEEK_FIRST_ERROR and not cc.FIRST_ERROR:
                            cc.FIRST_ERROR = True
                            cc.sGoToError(l)
                    else:
                        if cc.FILTER_OUTPUT != "True":
                            text += "\" "+l
                else:
                    text += l
                
        cc.aAddText(text)
    
    #@-node:AGP.20230214111049.154:CplOut
    #@+node:AGP.20230214111049.155:CplErr
    def CplErr(self,text):
        cc = self    
        cc.ErrBuff += text
        lines = cc.ErrBuff.splitlines(True)
        
        if lines[-1][-1] != "\n" and lines[-1][-1] != "\r":
            cc.ErrBuff = lines.pop()
        else:
            cc.ErrBuff = ""    
        
        text = ""	
        for l in lines:
            if l != "":
                text += cc.CMT+"err: "+l
                if cc.CPL_ERR_REGEXP:
                    m = cc.CPL_ERR_REGEXP.search(l,re.IGNORECASE)
                    if m != None:
                        if cc.SEEK_FIRST_ERROR and not cc.FIRST_ERROR:
                            cc.FIRST_ERROR = True
                            cc.sGoToError(l)
                
        cc.aAddText(text)
    #@nonl
    #@-node:AGP.20230214111049.155:CplErr
    #@+node:AGP.20230214111049.156:CplEnd
    def CplEnd(self,exitcode):
        
        cc = self
        text = "\""+("="*60)+"\n"
        
        if cc.LINK == True:
            pn = "Compilation"
        else:
            pn = "Build"
        
        
        if exitcode == None:
            text += "\" "+pn+" process successful!\n"
            Message("xcc : ",pn+" process successful!\n")
        else:
            text += "\" "+pn+" process aborted!\n"
            Error("xcc : ",pn+" process failed!")
        text += "\""+("-"*60)+"\n"
    
        cc.aAddText(text)
        cc.aSelect()
    #@nonl
    #@-node:AGP.20230214111049.156:CplEnd
    #@-node:AGP.20230214111049.152:Compiler Events
    #@+node:AGP.20230214111049.157:Linker Events
    #@+node:AGP.20230214111049.158:LkrStart
    def LkrStart(self):
        
        #g.trace()
    
        cc = self
        cc.OutBuff = ""
        cc.ErrBuff = ""
        cc.FIRST_ERROR = False
        cc.aSelect(cc.SELECTED_NODE)
        process = ProcessClass.List[0]
        
        text = ""	
        if cc.VERBOSE:
            text += "\" Linking...  Starting "+process.FileName+"...\n"
            text += "\" using arguments: "+process.Arguments+"\n"		
        text += "\""+("="*60)+"\n"
        
        cc.aAddText(text)
    
    #@-node:AGP.20230214111049.158:LkrStart
    #@+node:AGP.20230214111049.159:LkrOut
    def LkrOut(self,text):
        
        cc = self
        cc.OutBuff += text
        lines = cc.OutBuff.splitlines(True)
        if lines[-1][-1] != "\n" and lines[-1][-1] != "\r":
            cc.OutBuff = lines.pop()
        else:
            cc.OutBuff = ""
        
        text = ""	
        for l in lines:
            if l != "":
                if cc.LKR_ERR_REGEXP:
                    m = cc.LKR_ERR_REGEXP.search(l,re.IGNORECASE)
                    if m != None:
                        text += cc.CMT+" "+l
                    else:
                        if not cc.FILTER_OUTPUT:
                            text += "\" "+l
                else:
                    text += l
                
        cc.aAddText(text)
    
    #@-node:AGP.20230214111049.159:LkrOut
    #@+node:AGP.20230214111049.160:LkrErr
    def LkrErr(self,text):
        
        cc = self
        
        cc.ErrBuff += text
        lines = cc.ErrBuff.splitlines(True)
        if lines[-1][-1] != "\n" and lines[-1][-1] != "\r":
            cc.ErrBuff = lines.pop()
        else:
            cc.ErrBuff = ""
        
        text = ""	
        for l in lines:
            text += cc.CMT+"err: "+l+"\n"
                        
        cc.aAddText(text)
    #@nonl
    #@-node:AGP.20230214111049.160:LkrErr
    #@+node:AGP.20230214111049.161:LkrEnd
    def LkrEnd(self,exitcode):
        
        #g.trace(repr(exitcode))
        
        cc = self
        
        text = "\""+("="*60)+"\n"
        
        if exitcode == None:
            text += "\" Link process successful!\n"
            Message("xcc : ","Link process successful!")
        else:
            text += "// Link process aborted!\n"
            Error("xcc : ","Link process failed!")
        text += "\""+("-"*60)+"\n"
    
        cc.aAddText(text)
        cc.aSelect()
    #@nonl
    #@-node:AGP.20230214111049.161:LkrEnd
    #@-node:AGP.20230214111049.157:Linker Events
    #@+node:AGP.20230214111049.162:Debugger Events
    #@+node:AGP.20230214111049.163:DbgStart
    def DbgStart(self):
    
        #g.trace()
        cc = self
        cc.OutBuff = ""
        cc.ErrBuff = ""
        cc.ACTIVE_PROCESS = ProcessClass.List[0]
        cc.PROMPT_RD = []
        cc.DBG_STEPPING = False
        cc.DBG_PROMPT = False
        cc.TARGET_PID = ""
        cc.EOL = cc.DBG.get("Pipe eol")
        cc.aSelect(cc.SELECTED_NODE)
        # set buttons
        cc.ToolBar.PauseButton["state"] = 'normal'
        cc.ToolBar.StopButton["state"] = 'normal'
        # startup banner
        text = ""	
        if cc.VERBOSE:
            text += "\" Starting "+cc.ACTIVE_PROCESS.FileName+"...\n"
            text += "\" using arguments: "+cc.ACTIVE_PROCESS.Arguments+"\n"
        text += "\""+("="*60)+"\n"
        cc.aAddText(text)
        cc.DBG_TASK = []
        cc.DBG_SD = []
        cc.DBG_RD = []
        OutputTaskClass(cc)
        st = cc.ReplaceVars(cc.DBG["Startup task"]).splitlines()
        for t in st:
            DbgTaskClass(cc,t)
        TargetPidTaskClass(cc)
        RegExpTaskClass(cc)
        
        BreakTaskClass(cc)
        DbgTaskClass(cc,cc.DBG["Continue"])
    #@nonl
    #@-node:AGP.20230214111049.163:DbgStart
    #@+node:AGP.20230214111049.164:DbgOut
    def DbgOut(self,text):
        
        #g.trace(repr(text))
        
        cc = self
       
        #Extract output lines and prompt
        if text:
            cc.OutBuff += text
            lines = cc.OutBuff.splitlines(True)
            if lines[-1][-1] != "\n" and lines[-1][-1] != "\r":
                cc.OutBuff = lines.pop()
            else:
                cc.OutBuff = ""
    
            # sending output to SENT tasks
            for l in lines:
                for r in cc.DBG_RD:
                    r(l)
                if cc.DBG_PROMPT_REGEXP and cc.DBG_PROMPT_REGEXP.search(l):
                    cc.DBG_PROMPT = True            
                		
        
        if not cc.DBG_PROMPT:
            if cc.DBG_PROMPT_REGEXP and cc.DBG_PROMPT_REGEXP.search(cc.OutBuff):
                cc.DBG_PROMPT = True
        
        # detect the prompt
        if cc.DBG_PROMPT:
            cc.ToolBar.PauseButton["state"] = 'disabled'
            for prd in cc.PROMPT_RD:
                prd()
            if cc.DBG_STEPPING:
                cc.DBG_STEPPING = False
                cc.ToolBar.EnableStep()
            if not cc.FILTER_OUTPUT and cc.OutBuff != "":
                cc.aAddText("\" "+cc.OutBuff)
            cc.OutBuff = ""
    
        # send task to the debugger
        while cc.DBG_PROMPT and len(cc.DBG_SD) > 0:
            cc.DBG_SD[0]()
        
        if cc.DBG_PROMPT:
            cc.ToolBar.ShowInput()
    #@nonl
    #@-node:AGP.20230214111049.164:DbgOut
    #@+node:AGP.20230214111049.165:DbgErr
    def DbgErr(self,text):
        
        #g.trace(repr(text))
        
        cc = self
        cc.ErrBuff += text
        lines = cc.ErrBuff.splitlines(True)
        if lines[-1][-1] != "\n" and lines[-1][-1] != "\r":
            cc.ErrBuff = lines.pop()
        else:
            cc.ErrBuff = ""
        
        text = ""	
        for l in lines:
            text += "//err: "+l
                        
        cc.aAddText(text)
    #@nonl
    #@-node:AGP.20230214111049.165:DbgErr
    #@+node:AGP.20230214111049.166:DbgEnd
    def DbgEnd(self,exitcode):
    
        cc = self
        text = "\""+("="*60)+"\n"
        if exitcode == None:
            text += "\" Debug session ended successfully!\n"
        else:
            text += self.CMT+" Debug session aborted!\n"
        
        text += "\""+("-"*60)+"\n"
    
        cc.aAddText(text)
        cc.ToolBar.PauseButton["state"] = 'disabled'
        cc.ToolBar.StopButton["state"] = 'disabled'
        cc.ACTIVE_PROCESS = None
        cc.DBG_TASK = []
        cc.ToolBar.DisableStep()
        cc.LeoBodyText.tag_delete("xcc_error")	
        cc.TARGET_PID = ""
        cc.aSelect()
    #@-node:AGP.20230214111049.166:DbgEnd
    #@-node:AGP.20230214111049.162:Debugger Events
    #@+node:AGP.20230214111049.167:Program Events
    #@+node:AGP.20230214111049.168:ProgStart
    def ProgStart(self):
        
        #g.trace()
    
        cc = self
        cc.OutBuff = ""
        cc.ErrBuff = ""
        cc.aSelect(cc.SELECTED_NODE)
        cc.ACTIVE_PROCESS = ProcessClass.List[0]
        cc.EOL = cc.EXE.get("Pipe eol")
    
        text = ""	
        if cc.VERBOSE:
            text += "\" Starting "+cc.ACTIVE_PROCESS.FileName+"...\n"
            text += "\" using arguments: "+cc.ACTIVE_PROCESS.Arguments+"\n"		
        text += "\""+("="*60)+"\n"
        cc.aAddText(text)
        
        cc.ToolBar.ShowInput()
    #@nonl
    #@-node:AGP.20230214111049.168:ProgStart
    #@+node:AGP.20230214111049.169:ProgOut
    def ProgOut(self,text):
        
        #g.trace(repr(text))
        g.es(text)
        cc = self
        cc.OutBuff += text
        lines = cc.OutBuff.splitlines(True)
        if lines[-1][-1] != "\n" and lines[-1][-1] != "\r":
            cc.OutBuff = lines.pop()
        else:
            cc.OutBuff = ""
        
        text = ""	
        for l in lines:
            if l != "":
                text += "# "+l
        
        text += "# "+cc.OutBuff
        cc.OutBuff = ""
        cc.aAddText(text)
    #@nonl
    #@-node:AGP.20230214111049.169:ProgOut
    #@+node:AGP.20230214111049.170:ProgErr
    def ProgErr(self,text):
        
        #g.trace(repr(text))
        
        cc = self
        
        cc.ErrBuff += text
        lines = cc.ErrBuff.splitlines(True)
        if lines[-1][-1] != "\n" and lines[-1][-1] != "\r":
            cc.ErrBuff = lines.pop()
        else:
            cc.ErrBuff = ""
        
        text = ""	
        for l in lines:
            text += "// "+l+"\n"
        text += "# "+cc.ErrBuff
        cc.ErrBuff = ""
        cc.aAddText(text)
    #@nonl
    #@-node:AGP.20230214111049.170:ProgErr
    #@+node:AGP.20230214111049.171:ProgEnd
    def ProgEnd(self,exitcode):
        
        cc = self
        cc.ToolBar.HideInput()
        text = "\n\""+("="*60)+"\n"
        if exitcode == None:
            text += "\" "+cc.ACTIVE_PROCESS.FileName+" exited normally!\n"
        else:
            text += "// "+cc.ACTIVE_PROCESS.FileName+" exited with code: "+str(exitcode)+"\n"		
        text += "\""+("-"*60)+"\n"
    
        cc.aAddText(text)
        cc.ACTIVE_PROCESS = None
        cc.aSelect()
    #@nonl
    #@-node:AGP.20230214111049.171:ProgEnd
    #@-node:AGP.20230214111049.167:Program Events
    #@-others
#@nonl
#@-node:AGP.20230214111049.61:class controllerClass
#@+node:AGP.20230214111049.172:Debugger task classes
#@+node:AGP.20230214111049.173:DbgTaskClass
class DbgTaskClass:
    #@    @+others
    #@+node:AGP.20230214111049.174:__init__
    def __init__(self,cc,cmd,index=None):
        
        self.cc = cc
        self.Command = cmd
        
        if index:
            cc.DBG_SD.insert(index,self.Send)
        else:
            cc.DBG_SD.append(self.Send)
    #@nonl
    #@-node:AGP.20230214111049.174:__init__
    #@+node:AGP.20230214111049.175:Send
    def Send(self):
        
        cc = self.cc
    
        if self.Command:
            cc.aWrite(self.Command)
        cc.DBG_SD.remove(self.Send)
    #@nonl
    #@-node:AGP.20230214111049.175:Send
    #@-others
#@nonl
#@-node:AGP.20230214111049.173:DbgTaskClass
#@+node:AGP.20230214111049.176:OutputTaskClass
class OutputTaskClass(DbgTaskClass):
    #@    @+others
    #@+node:AGP.20230214111049.177:__init__
    def __init__(self,cc):
    
        self.cc = cc
        cc.DBG_RD.append(self.Receive)
    #@nonl
    #@-node:AGP.20230214111049.177:__init__
    #@+node:AGP.20230214111049.178:Send
    def Send(self):
        pass	#we just receive
    #@-node:AGP.20230214111049.178:Send
    #@+node:AGP.20230214111049.179:Receive
    def Receive(self,line):
        
        cc = self.cc
        
        if cc.DBG_PROMPT == False and line != "":
            lower = line.lower()
            if lower.find("error") > -1 or lower.find("warning") > -1:
                cc.aAddText(cc.CMT+line)
            else:
                if cc.OPTS["Filter output"] == "False":
                    cc.aAddText("\" "+line)
    #@nonl
    #@-node:AGP.20230214111049.179:Receive
    #@-others
    
#@nonl
#@-node:AGP.20230214111049.176:OutputTaskClass
#@+node:AGP.20230214111049.180:TargetPidTaskClass
class TargetPidTaskClass(DbgTaskClass):
    #@    @+others
    #@+node:AGP.20230214111049.181:__init__
    def __init__(self,cc):
        
        self.cc = cc
        cc.DBG_SD.append(self.Send)
        
        self.PidTask = cc.ReplaceVars(cc.DBG.get("Target pid task"))
        self.FindPid = cc.ReplaceVars(cc.DBG.get("Find pid"))
    #@nonl
    #@-node:AGP.20230214111049.181:__init__
    #@+node:AGP.20230214111049.182:Send
    def Send(self):
        cc = self.cc
        if self.PidTask != "":		
            cc.aWrite(cc.ReplaceVars(self.PidTask))
            cc.DBG_SD.remove(self.Send)
            cc.DBG_RD.append(self.Receive)
        else:
            cc.DBG_SD.remove(self.Send)
            Warning("xcc: ","Target pid task is undefined!")
    
    
    #@-node:AGP.20230214111049.182:Send
    #@+node:AGP.20230214111049.183:Receive
    def Receive(self,line):
       
        cc = self.cc
        if self.FindPid:
            if not cc.DBG_PROMPT:
                if line != "":
                    m = re.search(self.FindPid,line)
                    if m != None:
                        cc.TARGET_PID = int(m.group("PID"))		
                        if cc.VERBOSE:					
                            cc.aAddText("\" Target pid is: "+str(cc.TARGET_PID)+" \n")
                        cc.DBG_RD.remove(self.Receive)
                    
        else:
            cc.DBG_RD.remove(self.Receive)
    #@nonl
    #@-node:AGP.20230214111049.183:Receive
    #@-others
    
#@nonl
#@-node:AGP.20230214111049.180:TargetPidTaskClass
#@+node:AGP.20230214111049.184:BreakTaskClass
class BreakTaskClass(DbgTaskClass):
    #@    @+others
    #@+node:AGP.20230214111049.185:__init__
    def __init__(self,cc):
        
        self.cc = cc
        #gathering breaks
        self.Breaks = BreakFinderClass(cc).BREAKS
        if len(self.Breaks) != 0:
            self.bpsym = cc.DBG["Set break"]
            if self.bpsym == "":
                Waning("xcc: ","Set break symbol is undefined!")
            else:
                self.bpsym = cc.ReplaceVars(self.bpsym)
                cc.DBG_SD.append(self.Send)
        
        regexp = cc.DBG["Break detection"]
        if regexp != "":		
            regexp = regexp.splitlines()
            self.RegExp = []
            for e in regexp:
                self.RegExp.append(re.compile(e))		
        else:
            Warning("xcc: ","No break detection expression defined!")
    #@nonl
    #@-node:AGP.20230214111049.185:__init__
    #@+node:AGP.20230214111049.186:Send
    def Send(self):
        cc = self.cc
        if len(self.Breaks) > 0:
            extl,s = self.Breaks.popitem()
            ext,l = extl.split(":")
            bpat = self.bpsym
            bpat = bpat.replace("_FILE_",cc.NAME+"."+ext).replace("_LINE_",l)
            cc.aWrite(bpat)
        else:
            cc.DBG_SD.remove(self.Send)
            cc.DBG_RD.append(self.Receive)
    
    #@-node:AGP.20230214111049.186:Send
    #@+node:AGP.20230214111049.187:Receive
    def Receive(self,line):
        
        cc = self.cc
    
        for r in self.RegExp:
            if r.search(line) != None:
                if cc.OPTS.get("Seek breakpoints"):
                    QueryGoTaskClass(cc,0)
                if cc.VERBOSE:
                    cc.aAddText("\" Break detected!\n")
                
                if cc.ACTIVE_PROCESS and cc.SELECTED_NODE == cc.ACTIVE_NODE:
                    if cc.Watcher.visible:
                        WatchTaskClass(cc)               
                        if cc.DBG_PROMPT:
                            cc.DbgOut("")
                            
                    if cc.Dasm.visible:
                        DasmTaskClass(cc)               
                        if cc.DBG_PROMPT:
                            cc.DbgOut("")
                             
                cc.ToolBar.EnableStep()						
                return
    #@nonl
    #@-node:AGP.20230214111049.187:Receive
    #@-others
    
#@nonl
#@-node:AGP.20230214111049.184:BreakTaskClass
#@+node:AGP.20230214111049.188:RegExpTaskClass
class RegExpTaskClass(DbgTaskClass):
    #@    @+others
    #@+node:AGP.20230214111049.189:__init__
    def __init__(self,cc):
        
        self.cc = cc
        cc.DBG_RD.append(self.Receive)
        
        self.Exps = cc.ReplaceVars(cc.DBG.get("Regular expression",'')).splitlines()
        self.Task = cc.ReplaceVars(cc.DBG.get("Task",'')).splitlines()
        self.on = False	
    #@nonl
    #@-node:AGP.20230214111049.189:__init__
    #@+node:AGP.20230214111049.190:Send
    def Send(self):
        pass	#receive only
    
    
    
    #@-node:AGP.20230214111049.190:Send
    #@+node:AGP.20230214111049.191:Receive
    def Receive(self,line):
        
        cc = self.cc
    
        if not self.on:
            self.on = True ; return
        i=1
        for e in self.Exps:
            if e != "" and re.search(e,line) != None:
                if len(self.Task) >= i:
                    t = self.Task[i-1]
                else:
                    t = ""
                DbgTaskClass(cc,t,0)
                self.on = False
            i += 1
    #@nonl
    #@-node:AGP.20230214111049.191:Receive
    #@-others
    
#@nonl
#@-node:AGP.20230214111049.188:RegExpTaskClass
#@+node:AGP.20230214111049.192:WatchTaskClass
class WatchTaskClass(DbgTaskClass):
    #@    @+others
    #@+node:AGP.20230214111049.193:__init__
    def __init__(self,cc,index=0):
        
        self.cc = cc
        self.Index = index
        cc.WATCH_TASK = self
        self.Buffer = ""
        self.Count = 0
        
        cc.Watcher.OutBox.tag_delete("changed")
        self.Lines = cc.Watcher.InBox.get(1.0,'end').strip().splitlines()	
        
        if len(self.Lines) != 0:
            d=cc.DBG_SD.append(self.Send)
        
        for l in self.Lines:
            if l == "":
                del l
        
        self.nl = ""
        self.Inited = False
    #@-node:AGP.20230214111049.193:__init__
    #@+node:AGP.20230214111049.194:Cancel
    def Cancel(self):
        cc = self.cc
        if self.Send in cc.DBG_SD:
            cc.DBG_SD.remove(self.Send)
        if self.Receive in cc.DBG_RD:
            cc.DBG_RD.remove(self.Receive)
        if self.OnPrompt in cc.PROMPT_RD:
            cc.PROMPT_RD.remove(self.OnPrompt)
            
        cc.Watcher.Watching = False
        cc.WATCH_TASK = None
    
    #@-node:AGP.20230214111049.194:Cancel
    #@+node:AGP.20230214111049.195:Send
    def Send(self):
        cc = self.cc
        if len(self.Lines) > 0:
            cc.Watcher.Watching = True
            vari = self.Lines.pop(0)
            if vari.startswith("@"):
                vari = vari[1:]
            else:
                vari = vari = cc.DBG["Evaluate"]+vari
            cc.aWrite(vari)
            cc.DBG_SD.remove(self.Send)
            cc.DBG_RD.append(self.Receive)
            cc.PROMPT_RD.append(self.OnPrompt)
            self.Buffer = ""
            self.Count += 1
    #@nonl
    #@-node:AGP.20230214111049.195:Send
    #@+node:AGP.20230214111049.196:Receive
    def Receive(self,line):
        cc = self.cc
        if cc.DBG_PROMPT == False:		
            self.Buffer += line
    #@nonl
    #@-node:AGP.20230214111049.196:Receive
    #@+node:AGP.20230214111049.197:OnPrompt
    def OnPrompt(self):
        cc = self.cc
        
        cc.Watcher.OutBox["state"] = 'normal'
        s = str(self.Count)+".0"
        e = str(self.Count)+".end"
        
        self.Buffer = self.Buffer.replace("\n"," ")
        
        if self.Buffer != cc.Watcher.OutBox.get(s,e):
            changed = True
        else:
            changed = False
        
        cc.Watcher.OutBox.delete(s,e+"+1c")
        cc.Watcher.OutBox.insert(s,self.Buffer+"\n")	
        
        if changed == True:
            cc.Watcher.OutBox.tag_add("changed",s,e)
            cc.Watcher.OutBox.tag_config("changed",foreground ="red")
        
        cc.Watcher.OutBox["state"] = 'disabled'
            
        if len(self.Lines) != 0:
            cc.DBG_SD.append(self.Send)		
        else:
            cc.Watcher.Watching = False
            cc.WATCH_TASK = None
        
        cc.PROMPT_RD.remove(self.OnPrompt)	
        cc.DBG_RD.remove(self.Receive)
    
    #@-node:AGP.20230214111049.197:OnPrompt
    #@-others
    
#@nonl
#@-node:AGP.20230214111049.192:WatchTaskClass
#@+node:AGP.20230214111049.198:DasmTaskClass
class DasmTaskClass(DbgTaskClass):
    #@    @+others
    #@+node:AGP.20230214111049.199:__init__
    def __init__(self,cc,index=0):
        
        self.cc = cc
        self.Index = index
        cc.WATCH_TASK = self
        self.Buffer = ""
        
        cc.DBG_SD.append(self.Send)
        
        self.Inited = False
    #@-node:AGP.20230214111049.199:__init__
    #@+node:AGP.20230214111049.200:Cancel
    def Cancel(self):
        cc = self.cc
        if self.Send in cc.DBG_SD:
            cc.DBG_SD.remove(self.Send)
        if self.Receive in cc.DBG_RD:
            cc.DBG_RD.remove(self.Receive)
        if self.OnPrompt in cc.PROMPT_RD:
            cc.PROMPT_RD.remove(self.OnPrompt)
            
        self.Watching = False
        cc.WATCH_TASK = None
    
    #@-node:AGP.20230214111049.200:Cancel
    #@+node:AGP.20230214111049.201:Send
    def Send(self):
        cc = self.cc    
        cc.aWrite(cc.DBG["X cmd"])
        cc.DBG_SD.remove(self.Send)
        cc.DBG_RD.append(self.Receive)
        cc.PROMPT_RD.append(self.OnPrompt)
        self.Buffer = ""
    #@nonl
    #@-node:AGP.20230214111049.201:Send
    #@+node:AGP.20230214111049.202:Receive
    def Receive(self,line):
        cc = self.cc
        if cc.DBG_PROMPT == False:	
            self.Buffer += line
            
    #@nonl
    #@-node:AGP.20230214111049.202:Receive
    #@+node:AGP.20230214111049.203:OnPrompt
    def OnPrompt(self):
        cc = self.cc
        
        cc.DBG_RD.remove(self.Receive)
        cc.PROMPT_RD.remove(self.OnPrompt)
        t = cc.Dasm.DasmText
            
        t.config(state='normal')        
        t.delete(1.0,'end')
            
        t.insert("insert",self.Buffer)
        
        t.config(state='disabled')
        g.es("xcmd2")
    
    #@-node:AGP.20230214111049.203:OnPrompt
    #@-others
    
#@nonl
#@-node:AGP.20230214111049.198:DasmTaskClass
#@+node:AGP.20230214111049.204:QueryGoTaskClass
class QueryGoTaskClass(DbgTaskClass):

    #@    @+others
    #@+node:AGP.20230214111049.205:__init__
    def __init__(self,cc,index=None):
        
        self.cc = cc
        self.Query = cc.DBG.get("Query location")
        self.Find = cc.ReplaceVars(cc.DBG.get("Find location"))
        if not self.Query:
            cc.DBG_TASK.remove(self)
            Warning("xcc: ","Query location task is undefined!")
        elif index:
            cc.DBG_SD.insert(index,self.Send)
        else:
            cc.DBG_SD.append(self.Send)
    #@nonl
    #@-node:AGP.20230214111049.205:__init__
    #@+node:AGP.20230214111049.206:Send
    def Send(self):
        
        cc = self.cc
        cc.aWrite(self.Query)
        cc.DBG_SD.remove(self.Send)
        cc.DBG_RD.append(self.Receive)
    #@nonl
    #@-node:AGP.20230214111049.206:Send
    #@+node:AGP.20230214111049.207:Receive
    def Receive(self,line):
    
        cc = self.cc
        if cc.DBG_PROMPT == False:
            if line != "":
                m = re.search(self.Find,line,re.IGNORECASE)
                if m != None:
                    bline = m.group("LINE")
                    bext = m.group("EXT")
                        
                    if bline and bext:
                        if cc.VERBOSE:					
                            cc.aAddText("\" Current location is: "+bline+" in "+bext+" file!\n")
                        bline = int(bline)	
                        SeekErrorClass(self.cc,bline,bext,color=BreakColor)
                    
                    cc.DBG_RD.remove(self.Receive)
                    
                    if cc.Watcher.visible and cc.ACTIVE_PROCESS:
                        if cc.SELECTED_NODE == cc.ACTIVE_NODE:
                            WatchTaskClass(cc)
                        if cc.DBG_PROMPT:
                            cc.DbgOut("")
        else:
            cc.DBG_RD.remove(self.Receive)
                
    #@-node:AGP.20230214111049.207:Receive
    #@-others
    
#@nonl
#@-node:AGP.20230214111049.204:QueryGoTaskClass
#@+node:AGP.20230214111049.208:BreakIdTaskClass
class BreakIdTaskClass(DbgTaskClass):
    #@    @+others
    #@+node:AGP.20230214111049.209:__init__
    def __init__(self,cc,b,index=0):
        
        self.cc = cc
        
        if len(b) >0:
            self.Break = b
            self.ListBreaks = cc.DBG["List breaks"]
            self.IdentifyBreak = cc.ReplaceVars(cc.DBG["Identify break"])
            
            if self.ListBreaks and self.IdentifyBreak:
                if index:
                    cc.DBG_SD.insert(index,self.Send)
                else:
                    cc.DBG_SD.append(self.Send)
            else:
                Warning("xcc: ","Break Identification task is undefined!")
    #@nonl
    #@-node:AGP.20230214111049.209:__init__
    #@+node:AGP.20230214111049.210:Send
    def Send(self):
        cc = self.cc
        cc.aWrite(self.ListBreaks)
        cc.DBG_SD.remove(self.Send)
        cc.DBG_RD.append(self.Receive)
    
    #@-node:AGP.20230214111049.210:Send
    #@+node:AGP.20230214111049.211:Receive
    def Receive(self,line):
        
        cc = self.cc
        if not cc.DBG_PROMPT:
            if line:
                idb = cc.ReplaceVars(self.IdentifyBreak)
                            
                idb = idb.replace("_FILE_",self.Break[0]).replace("_LINE_",self.Break[1])
                m = re.search(idb,line,re.IGNORECASE)
                if m != None:
                    bid = m.group("ID")					
                    if bid != None:
                        if cc.VERBOSE:					
                            cc.aAddText("\" Break id at line "+self.Break[1]+" in "+self.Break[0]+" is "+bid+"\n")
                        DbgTaskClass(cc,cc.ReplaceVars(cc.DBG["Clear break"]).replace("_ID_",bid))
                        
        else:
            cc.DBG_RD.remove(self.Receive)
                
    #@nonl
    #@-node:AGP.20230214111049.211:Receive
    #@-others
    
#@nonl
#@-node:AGP.20230214111049.208:BreakIdTaskClass
#@-node:AGP.20230214111049.172:Debugger task classes
#@+node:AGP.20230214111049.212:class ProcessClass
class ProcessClass:
    List=[]
    if os.name == "dos" or os.name == "nt":
        Encoding = "mbcs"
    else:
        Encoding = "utf-8"
    #@    @+others
    #@+node:AGP.20230214111049.213:class ReadingThreadClass
    class ReadingThreadClass(threading.Thread):
    
        #@    @+others
        #@+node:AGP.20230214111049.214:__init__
        def __init__(self):
        
            threading.Thread.__init__(self)
            self.File = None
            self.Lock = thread.allocate_lock()
            self.Buffer = ""
        #@nonl
        #@-node:AGP.20230214111049.214:__init__
        #@+node:AGP.20230214111049.215:run
        def run(self):
            try:
                s=self.File.read(1)
                while s:
                    self.Lock.acquire()
                    self.Buffer = self.Buffer + s
                    self.Lock.release()
                    s=self.File.read(1)            
                    
            except IOError, ioerr:
                self.Buffer = self.Buffer +"\n"+ "[@run] ioerror :"+str(ioerr)
        #@nonl
        #@-node:AGP.20230214111049.215:run
        #@+node:AGP.20230214111049.216:Update
        def Update(self,func):
        
            ret = True
            if self.Lock.acquire(0) == 1:
                if self.Buffer and func:
                    func(unicode(self.Buffer, ProcessClass.Encoding))
                    self.Buffer=""
                else:
                    ret = self.isAlive()	
                self.Lock.release()
            else:
                	ret = self.isAlive()
            return ret
        
        
        #@-node:AGP.20230214111049.216:Update
        #@-others
    #@nonl
    #@-node:AGP.20230214111049.213:class ReadingThreadClass
    #@+node:AGP.20230214111049.217:__init__
    def __init__(self,cc,node,filename,args,start=None,out=None,err=None,end=None,spawn=False):
    
        self.cc = cc
        self.Node = node	
        self.Spawn = spawn	
        self.FileName = filename.replace("\\",path_sym)
        self.Arguments = args
        
        self.In = None
        self.OutThread = None
        self.ErrThread = None	
        
        self.OnStart = start
        self.Output = out
        self.Error = err
        self.OnEnd = end
        
        self.Kill = False
    #@-node:AGP.20230214111049.217:__init__
    #@+node:AGP.20230214111049.218:Open
    def Open(self):
        
        cc = self.cc
        if self.Spawn:
            os.spawnl(os.P_NOWAIT,self.FileName,self.Arguments)
            ProcessClass.List.remove(self)
            return True
    
        path,fname = os.path.split(self.FileName)
        
        if fname == "" or os.access(self.FileName,os.F_OK) != 1:		
            Warning("xcc: ","PROCESS: "+self.FileName+" is not a valid file!")
            #return #removed to allow std commands
    
        # Create the threads and open the pipe, saving and restoring the working directory.
        oldwdir= os.getcwd().replace("\\",path_sym)
        if path != "" and os.access(path,os.F_OK):        
            os.chdir(path)
        
        # added 14/11/07 : linux seem to have a different behaviour
        if os.name != "dos" and os.name != "nt":
            fname =  self.FileName
        
        self.OutThread = self.ReadingThreadClass()
        self.ErrThread = self.ReadingThreadClass()
        self.In,self.OutThread.File,self.ErrThread.File	= os.popen3(fname+" "+self.Arguments)
        os.chdir(oldwdir)
        
        if not self.In or not self.OutThread.File or not self.ErrThread.File:
            return Error("xcc: ","PROCESS: Can't open file!")
                                
        # Start the threads.
        self.OutThread.start()
        self.ErrThread.start()	
    
        self.Node.setMarked()	
        cc.LeoTop.redraw()
        return True
    #@nonl
    #@-node:AGP.20230214111049.218:Open
    #@+node:AGP.20230214111049.219:Close
    def Close(self):
        
        cc = self.cc
        
        self.In and self.In.close()
        
        self.OutThread.File and self.OutThread.File.close()
    
        exitcode = self.ErrThread.File and self.ErrThread.File.close()
        
        self.Node.clearMarked()
        self.Node = None	
            
        self.OnEnd and self.OnEnd(exitcode)	
    
        cc.LeoTop.redraw()
        
        return exitcode
    #@nonl
    #@-node:AGP.20230214111049.219:Close
    #@+node:AGP.20230214111049.220:Update
    def Update(self):
    
        if not self.OutThread or not self.ErrThread:
            return False
            
        # writing intro to console
        if self.OnStart:
            self.OnStart()
            self.OnStart = None
        
        return self.OutThread.Update(self.Output) or self.ErrThread.Update(self.Error)
    #@nonl
    #@-node:AGP.20230214111049.220:Update
    #@+node:AGP.20230214111049.221:QueueProcess
    def QueueProcess(p):
        if len(ProcessClass.List) == 0:
            ok = p.Open()
            if ok:
                ProcessClass.List.append(p)
            else:
                return False
        else:
            ProcessClass.List.append(p)
            return True
    #@nonl
    #@-node:AGP.20230214111049.221:QueueProcess
    #@-others
#@nonl
#@-node:AGP.20230214111049.212:class ProcessClass
#@+node:AGP.20230214111049.222:Widget classes
#@+node:AGP.20230214111049.223:class ConfigClass
class ConfigClass:
    #@    @+others
    #@+node:AGP.20230214111049.224:  __init__
    def __init__(self,cc):
        
        self.cc = cc
        self.Pages = []
        self.Buttons = []
        
        bg=g.theme['shade'](0.1)
        
        self.ActivePage = None
    
        #switch frame
        self.SwitchFrame = Tk.Frame(cc.LeoBodyParent,relief='groove',bd=2,height=40,width=100,bg=bg)
        
        #title
        self.Title = Tk.Entry(self.SwitchFrame,justify='center',bg=bg)
        self.Title.pack(side="top",fill="x",expand=1)	
        
        #self.AddPages()
        self.Pages.append(self.OptPageClass(cc,self))
        self.Pages.append(self.CplPageClass(cc))
        self.Pages.append(self.LkrPageClass(cc))
        self.Pages.append(self.DbgPageClass(cc))
        self.Pages.append(self.ExePageClass(cc))
        self.Pages.append(self.LangPageClass(cc))
        #self.Pages.append(self.CodePageClass(cc))
        
        #add pages switches
        for page in self.Pages:
            if page:
                b = Tk.Button(self.SwitchFrame,text=page.name,width=10,command=page.Show,relief='groove',bg=bg)
                self.Buttons.append(b)
                b.pack(side="left")
                if not self.ActivePage:
                    self.ActivePage = page
            
        if 0: #Cancel button
            # Not needed.
            b = Tk.Button(self.SwitchFrame,text="Cancel",command=lambda: self.Hide(False))
            b.pack(side="right")
    
       
        
        self.BreakTags = {}
        self.visible = False
    #@nonl
    #@-node:AGP.20230214111049.224:  __init__
    #@+node:AGP.20230214111049.225:  class PageClass
    class PageClass(Tk.Canvas):
        #@    @+others
        #@+node:AGP.20230214111049.226:class CHECK
        class CHECK:
            #@    @+others
            #@+node:AGP.20230214111049.227:__init__
            def __init__(self,master,n,x=0,y=0,dpd=[]):
                self.dpd = dpd
                self.Check = Tk.StringVar()
                self.Name = n
                c = self.c = Tk.Checkbutton(master,text=n,onvalue="True",offvalue="False",
                                            variable=self.Check,command=self.UpdDpd,bg=master["bg"])
                master.create_window(x,y,anchor='nw',window=c)
                c['selectcolor']=c['bg']
            #@nonl
            #@-node:AGP.20230214111049.227:__init__
            #@+node:AGP.20230214111049.228:Get
            def Get(self):
                return self.Check.get()
            #@-node:AGP.20230214111049.228:Get
            #@+node:AGP.20230214111049.229:Set
            def Set(self,value):
                self.Check.set(value)
                self.UpdDpd()
            #@-node:AGP.20230214111049.229:Set
            #@+node:AGP.20230214111049.230:UpdDpd
            def UpdDpd(self):
                if self.Check.get() == "True":
                    for d in self.dpd:
                        d.config(state="normal")
                else:
                    for d in self.dpd:
                        d.config(state="disabled")
            #@nonl
            #@-node:AGP.20230214111049.230:UpdDpd
            #@-others
        #@-node:AGP.20230214111049.226:class CHECK
        #@+node:AGP.20230214111049.231:class ENTRY
        class ENTRY:
            #@    @+others
            #@+node:AGP.20230214111049.232:__init__
            def __init__(self,c,n,w=500,h=20,e=1,a='nw',x=0,y=0,re=False,vs=False):
                self.Name = n
                
                bg=c["bg"]
                
                self.MasterFrame = mf = Tk.Frame(c,relief='groove',height=h,width=w,bg=bg)
                self.ID = c.create_window(x,y,anchor=a,window=mf,height=h,width=w)	
                
                self.Entry = Tk.Entry(mf,width=1,bg=bg)#,bg=bg)
                self.Entry.pack(side="right",fill="x",expand=e)
                l = Tk.Label(mf,text=n+":",bg=bg).pack(side="right")#,fg=fg
            #@-node:AGP.20230214111049.232:__init__
            #@+node:AGP.20230214111049.233:Get
            def Get(self):
                return self.Entry.get()
            #@-node:AGP.20230214111049.233:Get
            #@+node:AGP.20230214111049.234:Set
            def Set(self,text):
                self.Entry.delete(0,'end')
                self.Entry.insert('end',text)
            #@-node:AGP.20230214111049.234:Set
            #@-others
        #@-node:AGP.20230214111049.231:class ENTRY
        #@+node:AGP.20230214111049.235:class TEXT
        class TEXT:
            #@    @+others
            #@+node:AGP.20230214111049.236:__init__
            def __init__(self,c,n,w=500,h=100,a='nw',x=0,y=0,re=False,vs=False):#text are 3 column wide
                
                self.Name = n
                
                bg=c["bg"]
                
                self.MasterFrame = mf = Tk.Frame(c,relief='groove',bg=bg)
                self.ID = c.create_window(x,y+1,anchor=a,window=mf,width=w,height=h)
                
                lf = Tk.Frame(mf,relief='flat',bg=bg)
                lf.pack(side="top",fill="x",expand=1)			
                Tk.Label(lf,text=n+":",bg=bg).pack(side="left")#,fg=fg
                
                self.Text = Tk.Text(mf,bg=g.theme['shade'](0.05))
                self.Text.pack(side="top",fill="x",expand=1)
            #@-node:AGP.20230214111049.236:__init__
            #@+node:AGP.20230214111049.237:Get
            def Get(self):
                s = self.Text.get(1.0,'end')
                lines = s.splitlines()
                res = ""
                for l in lines:
                    if l != "":
                        res += l+"\n"
                return res
            #@-node:AGP.20230214111049.237:Get
            #@+node:AGP.20230214111049.238:Set
            def Set(self,text):
                self.Text.delete(1.0,'end')
                self.Text.insert('end',text)
            #@-node:AGP.20230214111049.238:Set
            #@-others
        #@-node:AGP.20230214111049.235:class TEXT
        #@+node:AGP.20230214111049.239:class LABEL
        class LABEL:
            #@    @+others
            #@+node:AGP.20230214111049.240:__init__
            def __init__(self,c,text,w=175,h=22,e=1,a='nw',x=0,y=0,color="#%02x%02x%02x" % (150,150,150)):
                bg=c["bg"]
                self.MasterFrame = mf = Tk.Frame(c,relief='groove',height=h,width=w,bg=bg)
                self.ID = c.create_window(x,y,anchor=a,window=mf,height=h,width=w)	
                
                self.Label = Tk.Label(c,text=text,justify='left',fg=color,bg=bg)
                self.ID = c.create_window(x,y,anchor=a,window=self.Label)
                
            #@nonl
            #@-node:AGP.20230214111049.240:__init__
            #@-others
        #@-node:AGP.20230214111049.239:class LABEL
        #@+node:AGP.20230214111049.241:class HELP
        class HELP(Tk.Button):
            #@    @+others
            #@+node:AGP.20230214111049.242:__init__
            def __init__(self,c,buttontext="Help",boxtitle="Help",msg="!",x=5,y=0):
                
                self.Title = boxtitle
                self.Message = msg
                Tk.Button.__init__(self,c,text=buttontext,command=self.Help,bg=c["bg"])
                self.ID = c.create_window(x,y,anchor='nw',window=self)
            #@nonl
            #@-node:AGP.20230214111049.242:__init__
            #@+node:AGP.20230214111049.243:Help
            def Help(self):
                tkMessageBox.showinfo(self.Title,self.Message)
            #@nonl
            #@-node:AGP.20230214111049.243:Help
            #@-others
        #@nonl
        #@-node:AGP.20230214111049.241:class HELP
        #@+node:AGP.20230214111049.244:__init__
        def __init__(self,cc,name):
            
            self.cc = cc
            self.name = name
            self.Objects = []
            Tk.Canvas.__init__(self,cc.LeoBodyParent,bg=g.theme['shade'](0.1))
            
            self.X=self.Y=self.W=self.H = 0
            
            self.page_width = 500
            
            
            self.buttonfg = g.theme['fg']
            
            
            pw = self.page_width
            px = py = 5
            hpx = pw/2+ px
            hpw = pw/2
            epx = pw+10
            
            self.layout = [px,py,pw,hpx,hpw,epx]
            
            self.CreateObjects(self)
            
            
        #@nonl
        #@-node:AGP.20230214111049.244:__init__
        #@+node:AGP.20230214111049.245:AddObject
        def AddObject(self,o):
        
            if o != None:
                self.Objects.append(o)
                self.X,self.Y,self.W,self.H = self.bbox('all')
        #@-node:AGP.20230214111049.245:AddObject
        #@+node:AGP.20230214111049.246:BBox
        def BBox(self):
            self.X,self.Y,self.W,self.H = self.bbox('all')
        #@-node:AGP.20230214111049.246:BBox
        #@+node:AGP.20230214111049.247:AddSep
        def AddSep(self,length=None,color="black"):
        
            if length == None:
                length = self.page_width
            
            self.create_line(5,self.H+4,length+5,self.H+4,fill=g.theme['shade'](0.4))
            self.H += 10
        #@-node:AGP.20230214111049.247:AddSep
        #@+node:AGP.20230214111049.248:CreateObjects
        def CreateObjects(self,master):#must overide
            pass
        #@-node:AGP.20230214111049.248:CreateObjects
        #@+node:AGP.20230214111049.249:SaveObjects
        def SaveObjects(self,pd=None):
            
            cc = self.cc
        
            if pd == None:
                pd = cc.sGet(self.name,init={})
            
            for o in self.Objects:
                pd[o.Name] = o.Get()
        #@-node:AGP.20230214111049.249:SaveObjects
        #@+node:AGP.20230214111049.250:LoadObjects
        def LoadObjects(self,pd=None):	
        
            cc = self.cc
            if pd == None:
                pd = cc.sGet(self.name,{})
                
            #g.trace(self.name,pd)
            
            for o in self.Objects:
                if o.Name not in pd:				
                    pd[o.Name] = o.Get()
                else:
                    o.Set(pd[o.Name])
        #@nonl
        #@-node:AGP.20230214111049.250:LoadObjects
        #@+node:AGP.20230214111049.251:ClearObjects
        def ClearObjects(self,value=""):
            for o in self.Objects:
                if o.Name == "Build sequence":
                    o.Set("COMPILE")
                else:
                    o.Set(value)
        #@nonl
        #@-node:AGP.20230214111049.251:ClearObjects
        #@+node:AGP.20230214111049.252:Hide
        def Hide(self):
            
            cc = self.cc
            self.pack_forget()
            
            b = cc.Config.GetButton(self.name)
            b.config(relief='groove',fg=self.buttonfg)
            
            cc.LeoYBodyBar.command=cc.LeoBodyText.yview
            cc.LeoBodyText.config(yscrollcommand=cc.LeoYBodyBar.set)
        #@nonl
        #@-node:AGP.20230214111049.252:Hide
        #@+node:AGP.20230214111049.253:Show
        def Show(self):
            
            cc = self.cc
            
            if cc.Config.ActivePage:
                cc.Config.ActivePage.Hide()
                
            cc.Config.ActivePage = self
            b = cc.Config.GetButton(self.name)
            self.buttonfg = b['fg']
            b.config(relief='sunken',fg=g.theme['accent'])	
            
            self.config(scrollregion=self.bbox('all'))
            self.config(yscrollcommand=cc.LeoYBodyBar.set)
            
            cc.LeoYBodyBar.command=self.yview
            cc.LeoYBodyBar.pack(side="right",fill="y")
            self.pack(expand=1,fill="both")
        #@-node:AGP.20230214111049.253:Show
        #@-others
    #@-node:AGP.20230214111049.225:  class PageClass
    #@+node:AGP.20230214111049.254: class CodePageClass
    #@+node:AGP.20230214111049.255:__init__
    #@-node:AGP.20230214111049.255:__init__
    #@+node:AGP.20230214111049.256:CreateObjects
    #@+node:AGP.20230214111049.257:Entries
    #@-node:AGP.20230214111049.257:Entries
    #@-node:AGP.20230214111049.256:CreateObjects
    #@-node:AGP.20230214111049.254: class CodePageClass
    #@+node:AGP.20230214111049.258: class CplPageClass
    class CplPageClass(PageClass):
        #@    @+others
        #@+node:AGP.20230214111049.259:__init__
        def __init__(self,cc):
            
            self.cc = cc
            ConfigClass.PageClass.__init__(self,cc,"Compiler")
        #@nonl
        #@-node:AGP.20230214111049.259:__init__
        #@+node:AGP.20230214111049.260:Browse
        def Browse(self):
            try:
                for o in self.Objects:
                    if o and o.Name == "Compiler":
                        break
                else: return
        
                ft = ('Executables', '.exe;.bin'),
                s = tkFileDialog.askopenfilename(filetypes=ft,title="Locate Compiler...")
                if s == None:
                    return Error("xcc: ","Action canceled by user!")
                elif s == "":
                    return Error("xcc: ","Empty path returned!")
        
                o.Set(os.path.normpath(s))
            except Exception:
                g.es_exception
        #@nonl
        #@-node:AGP.20230214111049.260:Browse
        #@+node:AGP.20230214111049.261:AddPath
        def AddPath(self,name):
            try:
                d = tkFileDialog.askdirectory()
                if d != "":
                    d = d.replace("\\",path_sym)
                    for o in self.Objects:
                        if o.Name == name:
                            opaths = o.Get().splitlines()
                            npaths = []
                        
                            for p in opaths:
                                p = p.strip()
                                if p != "":
                                    npaths.append(p)
                                
                            npaths.append(d)
                        
                            o.Set(string.join(npaths,"\n"))
            except Exception:
                g.es_exception
        #@nonl
        #@-node:AGP.20230214111049.261:AddPath
        #@+node:AGP.20230214111049.262:CreateObjects
        def CreateObjects(self,master): #must overide
            
            px,py,pw,hpx,hpw,epx = self.layout
            bg = master['bg']
            
            #@    @+others
            #@+node:AGP.20230214111049.263:Executable
            x=10
            y=10
            text_w = 350
            text_h = 80
            
            # compiler entry -
            self.AddObject(self.ENTRY(master,"Compiler",x=px,y=5,w=500,h=20))
            b = Tk.Button(master,text=" ...",command=self.Browse,bg=bg)
            master.create_window(epx,self.Y-2,anchor='nw',window=b)
            #@nonl
            #@-node:AGP.20230214111049.263:Executable
            #@+node:AGP.20230214111049.264:Arguments
            self.AddSep()
            #-------------------------------------------------
            
            t1 = self.TEXT(master,"Arguments",x=5,y=self.H,vs=True)
            self.HELP(master,boxtitle="Arguments info",msg=CplArgumentsHelp,x=epx,y=self.H+20)
            self.AddObject(t1)
            
            #------------------------------------------
            t1 = self.TEXT(master,"Debug arguments",x=5,y=self.H,vs=True)
            self.HELP(master,boxtitle="Debug arguments info",msg=CplDebugArgumentsHelp,x=epx,y=self.H+20)
            self.AddObject(t1)
            #@nonl
            #@-node:AGP.20230214111049.264:Arguments
            #@+node:AGP.20230214111049.265:Paths
            self.AddSep()
            #-------------------------------------------------------------
            b = Tk.Button(master,text="Browse",command=lambda:self.AddPath("Include search paths"),bg=bg)
            master.create_window(epx, self.H+58,anchor='nw',window=b)
            t1 = self.TEXT(master,"Include search paths",x=5,y=self.H)
            self.HELP(master,boxtitle="Include search paths info",msg=IncludeSearchPathsHelp, x=epx, y=self.H+20)
            self.AddObject(t1)
            #@nonl
            #@-node:AGP.20230214111049.265:Paths
            #@+node:AGP.20230214111049.266:Symbols
            ww =19
            self.AddSep()
            #------------------------------------------------------
            lf = Tk.Frame(master,relief='flat',bd=2,bg=bg)
            master.create_window(self.X,self.H+2,width=pw,height=20,anchor='nw',window=lf)
            Tk.Label(lf,text="Compiler symbols:",bg=bg).pack(side="left")
            self.H += 22
            
            self.HELP(master,boxtitle="Include path and Library path info",msg=IncludePathAndLibraryPathHelp,x=epx,y=self.H)
            #Include path
            e1 = self.ENTRY(master,"Include path",x=px,y=self.H,w=hpw)
            #Check syntaxe
            e2 = self.ENTRY(master,"Check syntaxe",x=hpx,y=self.H,w=hpw)
            self.AddObject(e1)
            self.AddObject(e2)
            #@nonl
            #@-node:AGP.20230214111049.266:Symbols
            #@+node:AGP.20230214111049.267:Error Detection
            # ------------------
            self.AddSep()
            e = self.ENTRY(master,"Error detection",x=px,y=self.H,re=True)
            self.HELP(master,boxtitle="Error detection info",msg=CplArgumentsHelp,x=epx,y=self.H)
            self.AddObject(e)
            #@nonl
            #@-node:AGP.20230214111049.267:Error Detection
            #@-others
        
        
        
        #@-node:AGP.20230214111049.262:CreateObjects
        #@-others
    #@-node:AGP.20230214111049.258: class CplPageClass
    #@+node:AGP.20230214111049.268: class DbgPageClass
    class DbgPageClass(PageClass):
        #@    @+others
        #@+node:AGP.20230214111049.269:__init__
        def __init__(self,cc):
            
            self.cc = cc
            ConfigClass.PageClass.__init__(self,cc,"Debugger")
        #@-node:AGP.20230214111049.269:__init__
        #@+node:AGP.20230214111049.270:Browse
        def Browse(self):
            try:
                for o in self.Objects:
                    if o != None and o.Name == "Debugger":
                        break
                else: return
        
                ft = ('Executables', '.exe;.bin'),
                s = tkFileDialog.askopenfilename(filetypes=ft,title="Locate Debugger...")
            
                if s == None:
                    return Error("xcc: ","Action canceled by user!")
                elif s == "":
                    return Error("xcc: ","Empty path returned!")
        
                o.Set(os.path.normpath(s))
            except Exception:
                g.es_exception()
        #@nonl
        #@-node:AGP.20230214111049.270:Browse
        #@+node:AGP.20230214111049.271:CreateObjects
        def CreateObjects(self,master):#must overide
        
            px,py,pw,hpx,hpw,epx = self.layout
            bg = master['bg']
            #@    @+others
            #@+node:AGP.20230214111049.272:Executable
            x=10
            y=10
            text_w = 350
            text_h = 80
                
            # compiler entry
            self.AddObject(self.ENTRY(master,"Debugger",x=px,y=5,h=20))
            b = Tk.Button(master,text=" ...",command=self.Browse,bg=bg)
            master.create_window(epx,self.Y-2,anchor='nw',window=b)	
            #@-node:AGP.20230214111049.272:Executable
            #@+node:AGP.20230214111049.273:Arguments
            self.AddSep()
            t1 = self.TEXT(master,"Arguments",x=px,y=self.H,vs=True)
            self.HELP(master,boxtitle="Arguments info",msg=DbgArgumentsHelp,x=epx,y=self.H+20)
            self.AddObject(t1)
            #@nonl
            #@-node:AGP.20230214111049.273:Arguments
            #@+node:AGP.20230214111049.274:Piping
            self.AddSep()
            e1 = self.ENTRY(master,"Prompt pattern",x=5,y=self.H,w=hpw,re=True) 
            e2 = self.ENTRY(master,"Pipe eol",x=hpx,y=self.H, w=hpw)
            
            self.HELP(master,boxtitle="Prompt pattern and Pipe eol info",msg=DbgPipingHelp,x=epx,y=self.H)
            self.AddObject(e1)
            self.AddObject(e2)
            #@nonl
            #@-node:AGP.20230214111049.274:Piping
            #@+node:AGP.20230214111049.275:Symbols
            ww =19
                
            self.AddSep()
                
            lf = Tk.Frame(master,relief='flat',bd=2,bg=bg)
            master.create_window(5,self.H+2, width=pw, height=20,anchor='nw',window=lf)
            Tk.Label(lf,text="Debugger commands symbols:",bg=bg).pack(side="left")
            self.H += 22
                
            # ------------------
            e1 = self.ENTRY(master,"Go",x=px,y=self.H, w=hpw)
            e2 = self.ENTRY(master,"Step in",x=hpx,y=self.H, w=hpw)
            self.AddObject(e1)
            self.AddObject(e2)
            
            # ------------------
            e1 = self.ENTRY(master,"Continue",x=px,y=self.H, w=hpw)
            e2 = self.ENTRY(master,"Step over",x=hpx,y=self.H, w=hpw)
            self.AddObject(e1)
            self.AddObject(e2)
                
            # ------------------
            e1 = self.ENTRY(master,"Stop",x=px,y=self.H, w=hpw)
            e2 = self.ENTRY(master,"Step out",x=hpx,y=self.H, w=hpw)
            self.AddObject(e1)
            self.AddObject(e2)
                
            # ------------------
            e1 = self.ENTRY(master,"Evaluate",x=px,y=self.H, w=hpw)
            e2 = self.ENTRY(master,"X cmd",x=hpx,y=self.H, w=hpw)
            self.AddObject(e1)
            self.AddObject(e2)
            #@nonl
            #@-node:AGP.20230214111049.275:Symbols
            #@+node:AGP.20230214111049.276:Startup Task
            #------------------------------------------------------
            self.AddSep()
            t1 = self.TEXT(master,"Startup task",x=px,y=self.H,vs=True)
            
            self.HELP(master,boxtitle="Startup task info",msg=DbgStartupTaskHelp,x=epx,y=self.H+20)
            
            self.AddObject(t1)
            #@nonl
            #@-node:AGP.20230214111049.276:Startup Task
            #@+node:AGP.20230214111049.277:Target PID
            # ------------------
            self.AddSep()
            e = self.ENTRY(master,"Target pid task",x=px,y=self.H,vs=True)
            
            self.HELP(master,boxtitle="Target pid task and Find pid info",msg=DbgTargetPidHelp,x=epx,y=self.H)
            self.AddObject(e)
            
            e = self.ENTRY(master,"Find pid",x=px,y=self.H,re=True,vs=True)
            self.AddObject(e)
            #@nonl
            #@-node:AGP.20230214111049.277:Target PID
            #@+node:AGP.20230214111049.278:Break info
            #------------------------------------------------------
            self.AddSep()
            self.HELP(master,boxtitle="Break detection info",msg=DbgBreakDetectionHelp,x=epx,y=self.H+20)
            self.AddObject(self.TEXT(master,"Break detection",x=px,y=self.H,w=pw,h=text_h,re=True))
            
            self.AddSep()
            e1 = self.ENTRY(master,"Set break",x=px,y=self.H,vs=True, w=hpw)
            e2 = self.ENTRY(master,"Clear break",x=hpx,y=self.H,vs=True, w=hpw)
            self.HELP(master,boxtitle="Set break and Clear break info",msg=DbgSetClearBreakHelp,x=epx,y=self.H)
            self.AddObject(e1)
            self.AddObject(e2)
            
            self.AddSep()
            self.HELP(master,boxtitle="List breaks and Identify break info",msg=DbgBreakIdHelp,x=epx,y=self.H)
            self.AddObject(self.ENTRY(master,"List breaks",x=px,y=self.H))
            e = self.ENTRY(master,"Identify break",x=px,y=self.H,re=True)
            self.AddObject(e)
            
            # ------------------
            self.AddSep()
            self.HELP(master,boxtitle="Query location and Find location info",msg=DbgLocationHelp,x=self.page_width+10,y=self.H)
            self.AddObject(self.ENTRY(master,"Query location",x=px,y=self.H))
            e = self.ENTRY(master,"Find location",x=px,y=self.H,re=True,vs=True)
            self.AddObject(e)
            #@nonl
            #@-node:AGP.20230214111049.278:Break info
            #@+node:AGP.20230214111049.279:Misc RE
            #-------------------------------------------------------------
            self.AddSep()
            t1 = self.TEXT(master,"Regular expression",x=px,y=self.H,w=hpw,re=True,vs=True)
            t2 = self.TEXT(master,"Task",x=hpx,y=self.H,vs=True, w=hpw)
            self.HELP(master,boxtitle="Regular expression and Task info",msg=DbgMiscExpHelp,x=epx,y=self.H+20)
            self.AddObject(t1)
            self.AddObject(t2)
            #@nonl
            #@-node:AGP.20230214111049.279:Misc RE
            #@-others
        #@-node:AGP.20230214111049.271:CreateObjects
        #@-others
    #@-node:AGP.20230214111049.268: class DbgPageClass
    #@+node:AGP.20230214111049.280: class ExePageClass
    class ExePageClass(PageClass):
        #@    @+others
        #@+node:AGP.20230214111049.281:__init__
        def __init__(self,cc):
            
            self.cc = cc
            ConfigClass.PageClass.__init__(self,cc,"Executable")
        #@-node:AGP.20230214111049.281:__init__
        #@+node:AGP.20230214111049.282:CreateObjects
        def CreateObjects(self,master):#must overide
            bd=self["background"]
            x=10
            y=10
            text_w = 350
            text_h = 80
            bg = master['bg']
            
            px,py,pw,hpx,hpw,epx = self.layout
            
            
            #@    @+others
            #@+node:AGP.20230214111049.283:Args
            self.AddObject(self.TEXT(master,"Execution arguments",x=px,y=5))
            
            #@-node:AGP.20230214111049.283:Args
            #@+node:AGP.20230214111049.284:Dll Caller
            #self.AddSep()
            #e1 = self.ENTRY(master,"Dll caller",x=5,y=self.H,w=280,h=20)
            #b = Tk.Button(master,text="Browse...",width=10,default='disabled')
            #master.create_window(self.X+285,self.H,width=60,height=20,anchor='nw',window=b)
            #self.AddObject(e1)
            #@nonl
            #@-node:AGP.20230214111049.284:Dll Caller
            #@+node:AGP.20230214111049.285:Piping
            self.AddSep()
            self.AddObject(self.ENTRY(master,"Pipe eol",x=px,y=self.H))
            #@nonl
            #@-node:AGP.20230214111049.285:Piping
            #@-others
            self.create_line(0,self.H+5,self.W+1,self.H+5)
        #@nonl
        #@-node:AGP.20230214111049.282:CreateObjects
        #@-others
    #@-node:AGP.20230214111049.280: class ExePageClass
    #@+node:AGP.20230214111049.286: class OptPageClass
    class OptPageClass(PageClass):
    
        #@    @+others
        #@+node:AGP.20230214111049.287:__init__
        def __init__(self,cc,cfgc):
            
            self.cc = cc
            self.cfgc = cfgc
            ConfigClass.PageClass.__init__(self,cc,"Options")
        #@-node:AGP.20230214111049.287:__init__
        #@+node:AGP.20230214111049.288:CreateObjects
        def CreateObjects(self,master): # must overide
            
            px,py,pw,hpx,hpw,epx = self.layout
            bg = master['bg']
            #@    @+others
            #@+node:AGP.20230214111049.289:Actions Switches
            s1 = self.CHECK(master,"Create files",x=px,y=self.H)
            self.AddObject(s1)
            
            s2 = self.CHECK(master,"Source files",x=px,y=self.H)
            s3 = self.CHECK(master,"Auto include header",x=hpx,y=self.H)
            self.AddObject(s2)
            self.AddObject(s3)
            
            s4 = self.CHECK(master,"Doc files",x=px,y=self.H)
            self.AddObject(s4)
            
            s1.dpd = [s2.c,s3.c,s4.c]
            #@nonl
            #@-node:AGP.20230214111049.289:Actions Switches
            #@+node:AGP.20230214111049.290:Import
            #@-node:AGP.20230214111049.290:Import
            #@+node:AGP.20230214111049.291:Build
            self.AddSep(length=pw)
            s1 = self.CHECK(master,"Build",x=px,y=self.H)
            s2 = self.CHECK(master,"Seek first error",x=hpx,y=self.H)
            
            s1.dpd = [s2.c]
            self.AddObject(s1)
            self.AddObject(s2)
            
            t = self.TEXT(master,"Build sequence",x=px,y=self.H,vs=True)
            self.HELP(master,boxtitle="Build sequence info",msg=OptBuildSequenceHelp,x=epx,y=self.H+20)
            self.AddObject(t)
            
            self.H = self.H+5
            
            
            #@-node:AGP.20230214111049.291:Build
            #@+node:AGP.20230214111049.292:Execution
            self.AddSep(length=pw)
            s1 = self.CHECK(master,"Execute",x=px,y=self.H)
            s2 = self.CHECK(master,"Connect to pipe",x=100,y=self.H)
            d2 = self.CHECK(master,"Seek breakpoints",x=200,y=self.H)
            self.AddObject(s1)
            self.AddObject(s2)
            self.AddObject(d2)
            s1.dpd = [s2.c,d2.c]
            
            d1 = self.CHECK(master,"Debug",x=px,y=self.H)
            self.AddObject(d1)
            
            
            
            #@-node:AGP.20230214111049.292:Execution
            #@+node:AGP.20230214111049.293:Output opts
            self.AddSep(pw)
            self.AddObject(self.CHECK(master,"Xcc verbose",x=px,y=self.H))
            self.AddObject(self.CHECK(master,"Filter output",x=px,y=self.H))
            #@nonl
            #@-node:AGP.20230214111049.293:Output opts
            #@+node:AGP.20230214111049.294:Load/Save
            
             #Load button
            
             
            b = Tk.Button(master,text="Load...",command=self.cfgc.LoadFromFile,bg=master['bg'])
            master.create_window(10,self.H+10,anchor='nw',window=b)
                
            #Save button
            b = Tk.Button(master,text="Save...",command=self.cfgc.SaveToFile,bg=master['bg'])
            master.create_window(75,self.H+10,anchor='nw',window=b)
            
            #Python Wrapper
            #b = Tk.Button(master,text="Wrap to pyton",command=self.cfgc.WrapToPython)
            #master.create_window(140,self.H+10,anchor='nw',window=b)
            #@nonl
            #@-node:AGP.20230214111049.294:Load/Save
            #@-others
        
            self.AddSep()
        #@nonl
        #@-node:AGP.20230214111049.288:CreateObjects
        #@-others
    #@-node:AGP.20230214111049.286: class OptPageClass
    #@+node:AGP.20230214111049.306: class LkrPageClass
    class LkrPageClass(PageClass):
        #@    @+others
        #@+node:AGP.20230214111049.307:__init__
        def __init__(self,cc):
            
            self.cc = cc
            ConfigClass.PageClass.__init__(self,cc,"Linker")
        #@nonl
        #@-node:AGP.20230214111049.307:__init__
        #@+node:AGP.20230214111049.308:Browse
        def Browse(self):
            try:
                for o in self.Objects:
                    if o and o.Name == "Linker":
                        break
                else: return
        
                ft = ('Executables', '.exe;.bin'),
                s = tkFileDialog.askopenfilename(filetypes=ft,title="Locate Linker...")
                if s == None:
                    return Error("xcc: ","Action canceled by user!")
                elif s == "":
                    return Error("xcc: ","Empty path returned!")
        
                o.Set(os.path.normpath(s))
            except Exception:
                g.es_exception()
        #@nonl
        #@-node:AGP.20230214111049.308:Browse
        #@+node:AGP.20230214111049.309:AddPath
        def AddPath(self,name):
            try:
                d = tkFileDialog.askdirectory()
                if d != "":
                    d = d.replace("\\",path_sym)
                    for o in self.Objects:
                        if o.Name == name:
                            opaths = o.Get().splitlines()
                            npaths = []
                        
                            for p in opaths:
                                p = p.strip()
                                if p != "":
                                    npaths.append(p)
                                
                            npaths.append(d)
                        
                            o.Set(string.join(npaths,"\n"))
            except Exception:
                g.es_exception
        #@nonl
        #@-node:AGP.20230214111049.309:AddPath
        #@+node:AGP.20230214111049.310:CreateObjects
        def CreateObjects(self,master): #must overide
        
            px,py,pw,hpx,hpw,epx = self.layout
            bg = master['bg']
            #@    @+others
            #@+node:AGP.20230214111049.311:Executable
            x=10
            y=10
            text_w = 350
            text_h = 80
            
            # compiler entry -
            self.AddObject(self.ENTRY(master,"Linker",x=5,y=5,w=350,h=20))
            b = Tk.Button(master,text=" ...",command=self.Browse,bg=bg)
            master.create_window(epx,self.Y-2,anchor='nw',window=b)
            #@nonl
            #@-node:AGP.20230214111049.311:Executable
            #@+node:AGP.20230214111049.312:Arguments
            self.AddSep()
            #-------------------------------------------------
            
            t1 = self.TEXT(master,"Arguments",x=5,y=self.H,vs=True)
            self.HELP(master,boxtitle="Arguments info",msg=CplArgumentsHelp,x=epx,y=self.H+20)
            self.AddObject(t1)
            
            #------------------------------------------
            t1 = self.TEXT(master,"Debug arguments",x=5,y=self.H,vs=True)
            self.HELP(master,boxtitle="Debug arguments info",msg=CplDebugArgumentsHelp,x=epx,y=self.H+20)
            self.AddObject(t1)
            #@nonl
            #@-node:AGP.20230214111049.312:Arguments
            #@+node:AGP.20230214111049.313:Paths
            self.AddSep()
            
            #-------------------------------------------------------------
            b = Tk.Button(master,text="Browse",command=lambda:self.AddPath("Library search paths"),bg=bg)
            master.create_window(360,self.H+58,anchor='nw',window=b)
            t1 = self.TEXT(master,"Library search paths",x=5,y=self.H)
            self.HELP(master,boxtitle="Library search paths info",msg=LibrarySearchPathsHelp,x=epx,y=self.H+20)
            self.AddObject(t1)
            
            #-------------------------------------------------------------
            t1 = self.TEXT(master,"Used libraries",x=5,y=self.H)
            self.HELP(master,boxtitle="Used libraries info",msg=UsedLibrariesHelp,x=epx,y=self.H+20)
            self.AddObject(t1)
            #@nonl
            #@-node:AGP.20230214111049.313:Paths
            #@+node:AGP.20230214111049.314:Symbols
            ww =19
            self.AddSep()
            #------------------------------------------------------
            lf = Tk.Frame(master,relief='flat',bd=2,bg=bg)
            master.create_window(self.X,self.H+2,width=text_w,height=20,anchor='nw',window=lf)
            Tk.Label(lf,text="Linker symbols:",bg=bg).pack(side="left")
            self.H += 22
            
            self.HELP(master,boxtitle="Include path and Library path info",msg=IncludePathAndLibraryPathHelp,x=epx,y=self.H)
            #Use library
            e1 = self.ENTRY(master,"Use library",x=px,y=self.H,w=hpw)
            #Library path
            e2 = self.ENTRY(master,"Library path",x=hpx,y=self.H,w=hpw)
            self.AddObject(e1)
            self.AddObject(e2)
            
            self.HELP(master,boxtitle="Build exe and Build dll info",msg=BuildExeAndBuildDllHelp,x=epx,y=self.H)
            #Build exe
            e1 = self.ENTRY(master,"Build exe",x=px,y=self.H,w=hpw)
            #Build dll
            e2 = self.ENTRY(master,"Build dll",x=hpx,y=self.H,w=hpw)
            self.AddObject(e1)
            self.AddObject(e2)
            #@nonl
            #@-node:AGP.20230214111049.314:Symbols
            #@+node:AGP.20230214111049.315:Error Detection
            # ------------------
            self.AddSep()
            e = self.ENTRY(master,"Error detection",x=5,y=self.H,w=350,re=True)
            self.HELP(master,boxtitle="Error detection info",msg=CplArgumentsHelp,x=epx,y=self.H)
            self.AddObject(e)
            #@nonl
            #@-node:AGP.20230214111049.315:Error Detection
            #@-others
        
        
        
        #@-node:AGP.20230214111049.310:CreateObjects
        #@-others
    #@-node:AGP.20230214111049.306: class LkrPageClass
    #@+node:AGP.20230214111049.316: class LangPageClass
    class LangPageClass(PageClass):
    
        #@    @+others
        #@+node:AGP.20230214111049.317:__init__
        def __init__(self,cc):
            
            self.cc = cc
            ConfigClass.PageClass.__init__(self,cc,"Language")
        #@-node:AGP.20230214111049.317:__init__
        #@+node:AGP.20230214111049.318:CreateObjects
        def CreateObjects(self,master): # must overide
        
            px,py,pw,hpx,hpw,epx = self.layout
            
            #@    @+others
            #@+node:AGP.20230214111049.319:Language
            e1 = self.ENTRY(master,"Language",x=px,y=15,w=hpw)
            e2 = self.ENTRY(master,"Comment symbol",x=hpx,y=15,w=hpw)
            self.AddObject(e1)
            self.AddObject(e2)
            
            e1 = self.ENTRY(master,"Source ext",x=px,y=self.H,w=hpw)
            e2 = self.ENTRY(master,"Header ext",x=hpx,y=self.H,w=hpw)
            self.AddObject(e1)
            self.AddObject(e2)
            
            e1 = self.ENTRY(master,"Binary ext",x=px,y=self.H,w=hpw)
            self.AddObject(e1)
            
            self.AddSep(length=self.W)
            
            e1 = self.ENTRY(master,"Fonction opening",x=px,y=self.H,w=hpw)
            self.AddObject(e1)
            e2 = self.ENTRY(master,"Fonction closing",x=px,y=self.H,w=hpw)
            self.AddObject(e2)
            
            e1 = self.ENTRY(master,"Class opening",x=px,y=self.H,w=hpw)
            self.AddObject(e1)
            e2 = self.ENTRY(master,"Class closing",x=px,y=self.H,w=hpw)
            self.AddObject(e2)
            #@nonl
            #@-node:AGP.20230214111049.319:Language
            #@-others
        
            self.AddSep(length=self.W)
        #@nonl
        #@-node:AGP.20230214111049.318:CreateObjects
        #@-others
    #@-node:AGP.20230214111049.316: class LangPageClass
    #@+node:AGP.20230214111049.295:AddPages
    def AddPages(self):
        
        cc = self.cc
        
        self.Pages.append(self.OptPageClass(cc,self))
        self.Pages.append(self.CplPageClass(cc))
        self.Pages.append(self.LkrPageClass(cc))
        self.Pages.append(self.DbgPageClass(cc))
        self.Pages.append(self.ExePageClass(cc))
        self.Pages.append(self.LangPageClass(cc))
        #self.Pages.append(self.CodePageClass(cc))
    #@nonl
    #@-node:AGP.20230214111049.295:AddPages
    #@+node:AGP.20230214111049.296:Apply
    def Apply(self):
        self.SaveToNode()
        self.Hide()
    #@-node:AGP.20230214111049.296:Apply
    #@+node:AGP.20230214111049.297:ClearConfig
    def ClearConfig(self):
        self.Title.delete(0,'end')
        self.Title.insert('end',"BLANK_CONFIG")
        for p in self.Pages:
            if p.name == "Options":
                p.ClearObjects("False")
            else:
                p.ClearObjects()
    #@-node:AGP.20230214111049.297:ClearConfig
    #@+node:AGP.20230214111049.298:GetButton
    def GetButton(self,name):
    
        for b in self.Buttons:
            if b and b["text"] == name:
                return b
    #@nonl
    #@-node:AGP.20230214111049.298:GetButton
    #@+node:AGP.20230214111049.299:GetPage
    def GetPage(self,name):
        
        for p in self.Pages:
            if p and p.name == name:
                return p
    #@nonl
    #@-node:AGP.20230214111049.299:GetPage
    #@+node:AGP.20230214111049.300:Hide
    def Hide(self,save=True):
        try:
            cc = self.cc
        
            if self.visible == True:
                self.ActivePage.Hide()	
                self.SwitchFrame.pack_forget()
                cc.LeoYBodyBar.command=cc.LeoBodyText.yview
                cc.LeoBodyText.config(yscrollcommand=cc.LeoYBodyBar.set)
                cc.LeoXBodyBar.pack(side = "bottom",fill="x")
                
                if cc.CHILD_NODE:
                    cc.BreakBar.Show()
                
                cc.LeoBodyText.pack(expand=1, fill="both")
            
                if save == True:
                    self.SaveToNode()
                
                cc.ToolBar.ConfigButton.config(command=self.Show,relief='raised')
                #cc.ToolBar.DisplayFrame.pack(side="top",fill="x",expand=1)
                self.visible = False
        except Exception:
            g.es_exception()
    #@nonl
    #@-node:AGP.20230214111049.300:Hide
    #@+node:AGP.20230214111049.301:LoadFromFile
    def LoadFromFile(self):
        try:
            ft = ('XCC Config files', '.xcc'),
            s = tkFileDialog.askopenfilename(filetypes=ft,title="Open xcc connfiguration file...")
        
            if s == "":
                Error("xcc: ","Load action canceled by user!")
                return
            
            #read file and compose code
            f = file(s,"r")
            td = None
            code = "td ="+f.readline()
            f.close()
            
            # load in temp dict
            try:
                exec code
            except Exception:
                TraceBack()
                Error("xcc: ","File content is invalid!")
                return
            
            #	load each pages
            for p in self.Pages:
                if p.name in td:
                    p.LoadObjects(td[p.name])
                    
            #set title to file name
            name,ext = os.path.splitext(s)
            path,name = os.path.split(name)		
            self.Title.delete(0,'end')
            self.Title.insert('end',name)		
            
            #save to node to ensure integrity
            self.SaveToNode()
            
        except Exception:
            TraceBack()
    
    
    
    
    #@-node:AGP.20230214111049.301:LoadFromFile
    #@+node:AGP.20230214111049.302:LoadFromNode
    def LoadFromNode(self):
    
        cc = self.cc
        self.Title.delete(0,'end')
        self.Title.insert('end',cc.sGet("Title"))
            
        for p in self.Pages:
            if p:
                p.LoadObjects()
    #@nonl
    #@-node:AGP.20230214111049.302:LoadFromNode
    #@+node:AGP.20230214111049.303:SaveToFile
    def SaveToFile(self):
        try:
            
        
            ft = ('XCC Config files', '.xcc'),
            s = tkFileDialog.asksaveasfilename(
            filetypes=ft,
            title="Save xcc connfiguration file...",
            initialfile = self.Title.get()
            )
            
            if s == "":
                Error("xcc: ","Save action canceled by user!")
                return		
            
            name,ext = os.path.splitext(s)
                    
            td = {}
            
            # save each pages
            for p in self.Pages:
                td[p.name] = {}
                p.SaveObjects(td[p.name])	
            
            #write the dict to file
            f = file(name+".xcc","w+")
            Message("xcc: ","Writing config in "+name+".xcc")
            f.write(str(td))
            f.close()
            
            # reset title to file name
            path,name = os.path.split(name)		
            self.Title.delete(0,'end')
            self.Title.insert('end',name)
            
            # save to node
            self.SaveToNode()
        except Exception:
            TraceBack()
    
    
    
    
    
    
    
    #@-node:AGP.20230214111049.303:SaveToFile
    #@+node:AGP.20230214111049.304:SaveToNode
    def SaveToNode(self):
        
        cc = self.cc
        
        cc.sSet("Title",self.Title.get())
        
        for p in self.Pages:
            p and p.SaveObjects()
    #@nonl
    #@-node:AGP.20230214111049.304:SaveToNode
    #@+node:AGP.20230214111049.305:Show
    def Show(self):
        try:
            cc = self.cc
            cc.HideWidgets()
            if cc.BreakBar.visible:
                cc.BreakBar.Hide()
            
            #cc.ToolBar.DisplayFrame.pack_forget()
            cc.LeoBodyText.pack_forget()
            cc.LeoXBodyBar.pack_forget()
            cc.LeoYBodyBar.pack_forget()
        
            self.SwitchFrame.pack(side="top", fill="x")
            
            self.LoadFromNode()
            self.ActivePage.Show()
            cc.ToolBar.ConfigButton.config(command=self.Hide,relief='sunken')
            self.visible = True
            #cc.c.redraw()
        except Exception:
            TraceBack()
    
    #@-node:AGP.20230214111049.305:Show
    #@-others
#@nonl
#@-node:AGP.20230214111049.223:class ConfigClass
#@+node:AGP.20230214111049.321:class ToolbarClass
class ToolbarClass(Tk.Frame):
    
    #@    @+others
    #@+node:AGP.20230214111049.322:__init__
    def __init__(self,cc):    
        self.cc = cc
        
        #print cc.c.frame.iconBar.iconFrame#cc.LeoBodyParent
        
        iconframe = cc.c.frame.iconBar.iconFrame
        
        fg = g.theme['fg']
        bg = iconframe['bg']#g.theme['shade'](0.2)
        
        Tk.Frame.__init__(self,iconframe,bg = bg)#,relief='groove',bd=1)
        
        
        
        f = self#Tk.Frame(self,bg=bg)
        #f.pack(side="right")#,fill="x")#,expand=1)
        
        leodir = g.app.leoDir
        w = h = 24
        #ico_dir = "../icons/white/"
        
        oldwd = os.getcwd()
        os.chdir(leodir+"/icons/white/")
        self.images = []
        
        
        colorim = Image.new('RGBA', (64,64), g.theme['shade'](0.7))#'#0000FFFF')
        #redim = Image.new('RGBA', (64,64), '#FF0000FF')
        
        #im = Image.open('play.png')
        #im = Image.blend(im,colorim,0.8)
        #im = Image.composite(colorim,im,im)
        
        
        
        
        #im2 = Image.open('stepin.png')
        #im2 = Image.composite(redim,im2,im2)
        #im2 = Image.alpha_composite(im,im2)
        
        
        
        #im = ImageTk.PhotoImage(im.resize((w, h), Image.ANTIALIAS))
        #im2 = ImageTk.PhotoImage(im2.resize((w, h), Image.ANTIALIAS))
        
        #self.images.append(im)
        #self.images.append(im2)
        #self.images.append(im)
        
        
        
        
        def open_image(filename):
            im = Image.open(filename)
            #im = Image.blend(im,colorim,0.8)
            im = Image.composite(colorim,im,im)
            im = ImageTk.PhotoImage(im.resize((w, h), Image.ANTIALIAS))
            self.images.append(im)
            return im
        
        #---------------------------------------------------
        
        self.ConfigButton = Tk.Button(f,image=open_image("settings.png"),command=cc.Config.Show,bg=bg)
        self.ConfigButton.pack(side="right")
        
        
        self.DasmButton = Tk.Button(f,image=open_image("xcmd.png"),command=cc.Dasm.Show,bg=bg)
        self.DasmButton.pack(side="right")    
        
        self.WatchButton = Tk.Button(f,image=open_image("watch.png"),command=cc.Watcher.Show,bg=bg)
        self.WatchButton.pack(side="right")
        
        self.DocButton = Tk.Button(f,image=open_image("doc.png"),command=cc.DocEdit.Show,bg=bg)
        self.DocButton.pack(side="right")
        
        #----------------------------------------------------
        
        self.DbgEntry = Tk.Entry(f,state='disabled')
        self.DbgEntry.bind("<Key>",self.OnKey)
        #self.DbgEntry.pack(side="right",fill='y')
        
        self.Prompt_e=Tk.PhotoImage(data=DecompressIcon(Prompt_e))
        self.PromptButton = Tk.Button(f,image=self.Prompt_e,command=self.Refresh,bg=bg,state='disabled')
        #self.PromptButton.pack(side="right",fill='y')
        self.dummyframe = Tk.Frame(f,width = 200,height = 32,bg=f['bg'])
        self.dummyframe.pack(side="right")
        
        
        #-------------------------------------------------
        self.StepOutButton = Tk.Button(f,image=open_image("stepout.png"),state='disabled',command=cc.aStepOut,bg=bg)
        self.StepOutButton.pack(side="right")
        
        self.StepInButton = Tk.Button(f,image=open_image("stepover.png"),state='disabled',command=cc.aStepOver,bg=bg)
        self.StepInButton.pack(side="right")
        
        self.StepButton = Tk.Button(f,image=open_image("stepin.png"),state='disabled',command=cc.aStepIn,bg=bg)
        self.StepButton.pack(side="right")
        
        self.StopButton = Tk.Button(f,image=open_image("stop.png"),command=cc.aStop,state='disabled',bg=bg)
        self.StopButton.pack(side="right")
        
        self.PauseButton = Tk.Button(f,image=open_image("pause.png"),command=cc.aPause,state='disabled',bg=bg)
        self.PauseButton.pack(side="right")
        
        self.GoButton = Tk.Button(f,command=self.Go,image=open_image("play.png"),bg=bg)
        self.GoButton.pack(side="right")
        
        
        
        
        #print self.images
        
        
        
        #self.StepIn_e=Tk.PhotoImage(data=DecompressIcon(StepIn_e))
        
        
        
        
        
        
        
        
        
        
        #s="<<"
        #e=">>"
        # command entry
        
        
        
        
        
        
        #self.DisplayFrame = Tk.Frame(self,bg=bg)
        #self.DisplayFrame.pack(side="top",fill="x",expand=1)
        
        #fgcolor = "#808080"#BreakBar.fgcolor
        #self.Spacer = Tk.Text(self.DisplayFrame,height=1,fg=fgcolor,relief='flat',font=cc.LeoFont,width=4,state='disabled')
        #self.Spacer.pack(side="left")
        
        #self.Display = Tk.Text(self.DisplayFrame,height=1,relief='flat',fg=fgcolor,bg=cc.BreakBar["bg"],font=cc.LeoFont,state='disabled')
        #self.Display.pack(side="left",fill="x",expand=1)
        os.chdir(oldwd)
    #@-node:AGP.20230214111049.322:__init__
    #@+node:AGP.20230214111049.323:Go
    def Go(self):    
        try:
            cc = self.cc
            
            
            if not cc.ACTIVE_NODE:
                if len(ProcessClass.List) > 0:
                    return Error("xcc: ","already running!")
                cc.sGo()
            elif cc.ACTIVE_NODE == cc.SELECTED_NODE:
                cc.aGo()
            else:
                Error("xcc: ",str(cc.ACTIVE_NODE)+" is already active!")            
        except Exception:
            g.es_exception()
    #@nonl
    #@-node:AGP.20230214111049.323:Go
    #@+node:AGP.20230214111049.324:Hide
    def Hide(self):
    
        cc = self.cc
        self.pack_forget()
        cc.LeoBodyText.config(wrap=cc.LeoWrap)
        if cc.Watcher.visible:
            cc.Watcher.Hide()
    #@nonl
    #@-node:AGP.20230214111049.324:Hide
    #@+node:AGP.20230214111049.325:Show
    def Show(self):
    
        cc = self.cc    
        self.pack(side="top",expand=1)#,fill="x")
        cc.LeoBodyText.config(wrap='none')
    
        if cc.Watcher.visible:
            cc.Watcher.Show()
    #@nonl
    #@-node:AGP.20230214111049.325:Show
    #@+node:AGP.20230214111049.326:OnKey
    def OnKey(self,event=None):
        
        cc = self.cc
        
        if cc.ACTIVE_NODE:
            if len(event.char)==1 and ord(event.char) == 13:
                cc.aWrite(self.DbgEntry.get().replace("\n",""))
                self.DbgEntry.delete(0,'end')
    #@nonl
    #@-node:AGP.20230214111049.326:OnKey
    #@+node:AGP.20230214111049.327:EnableStep
    def EnableStep(self):
    
        self.StepButton["state"] = 'normal'
        self.StepInButton["state"] = 'normal'
        self.StepOutButton["state"] = 'normal'
    #@nonl
    #@-node:AGP.20230214111049.327:EnableStep
    #@+node:AGP.20230214111049.328:DisableStep
    def DisableStep(self):
    
        self.StepButton["state"] = 'disabled'
        #self.StepButton["image"] = self.Step_d
        
        self.StepInButton["state"] = 'disabled'
        #self.StepInButton["image"] = self.StepIn_d
        
        self.StepOutButton["state"] = 'disabled'
        #self.StepOutButton["image"] = self.StepOut_d
    #@nonl
    #@-node:AGP.20230214111049.328:DisableStep
    #@+node:AGP.20230214111049.329:SyncDisplayToChild
    def SyncDisplayToChild(self,loc):
        
        cc = self.cc
        self.Display["cursor"] = ""
        self.Display.unbind("<Button-1>")
        self.Spacer["state"] = 'normal'
        #self.Spacer.pack(side="left")
        
        if cc.BreakBar.visible:
            self.Spacer["width"] = int(cc.BreakBar["width"])+1
        else:
            self.Spacer["width"] = 4
        
        hline = None
        
        if loc.FOUND_HEAD_SRC_LINE:
            hext = self.cc.SRC_EXT
            hline = "." + str(loc.FOUND_HEAD_SRC_LINE)
        
        if loc.FOUND_HEAD_HDR_LINE:
            hext = self.cc.HDR_EXT
            if hline != None:
                hline = ":" + str(loc.FOUND_HEAD_HDR_LINE)
            else:
                hline = "'" + str(loc.FOUND_HEAD_HDR_LINE)
        
        bfm = ""    #body file marker
        bext = ""
        if loc.FOUND_BODY_SRC_LINE:
            bext = self.cc.SRC_EXT
        
        if loc.FOUND_BODY_HDR_LINE:
            bext = self.cc.HDR_EXT
            if bfm != "":
                bfm = ":"
            else:
                bfm = "'"
        
        
        self.Spacer.delete(1.0,'end')
        self.Spacer.insert('insert'," "+bext)
        self.Spacer["state"] = 'disabled'
        
        disp = hline+" : " ; _as = ""
        for c in loc.CLASS_LIST:
            _as += c+" :: "
        disp += _as	
        off = 0
        if loc.CURRENT_RULE and loc.CURRENT_RULE != "class" and loc.CURRENT_RULE != "doc":
            off = len(disp)
            disp += cc.CHILD_NODE.headString()	
        
        self.Display["state"] = 'normal'
        self.Display.delete(1.0,'end')
        self.Display.tag_delete("marking")
        self.Display.insert("insert",disp)
        
        if loc.CURRENT_RULE == "func":
            spec,ret,name,params,pure,dest,ctors = loc.CURRENT_MO
            
            v,s,e = spec
            if v != "":
                self.Display.tag_add("marking","1."+str(s+off),"1."+str(e+off))
            
            v,s,e = ret
            if s != -1 and e != -1:
                self.Display.tag_add("marking","1."+str(s+off),"1."+str(e+off))		
            
            params,s,e = params
            if params != "()":
                s += 1
                params = params.split(",")
                for p in params:
                    pmo = re.search("[( ]*(?P<TYPE>.+) +(?P<NAME>[^) ]+)[ )]*",p)
                    if pmo != None:
                        s2,e2 = pmo.span("TYPE")
                        self.Display.tag_add("marking","1."+str(s+off+s2-1),"1."+str(s+off+(e2-s2)))
                        off += len(p)+1
                        
        
        if loc.CURRENT_RULE == "doc":
            self.Display.insert("insert",loc.DocName())
            
        self.Display.tag_config("marking",foreground="#7575e5")
        self.Display["state"] = 'disabled'
    #@-node:AGP.20230214111049.329:SyncDisplayToChild
    #@+node:AGP.20230214111049.330:SyncDisplayToError
    def SyncDisplayToError(self):
        cc = self.cc
        
        self.Spacer["state"] = 'normal'
            
        if cc.BreakBar.visible == True:
            self.Spacer["width"] = int(cc.BreakBar["width"])+1
        else:
            self.Spacer["width"] = 4
        
        self.Spacer.delete(1.0,'end')
        self.Spacer.insert("insert","ERR")
        self.Spacer["state"] = 'disabled'
        
        self.Display["state"] = 'normal'
        self.Display.delete(1.0,'end')
        self.Display.tag_delete("marking")
        
        self.Display.insert("insert",cc.PARSE_ERROR)
        self.Display.tag_add("marking","1.0",'end')
        self.Display.tag_config("marking",foreground="red")
        self.Display["state"] = 'disabled'
        
        self.Display["cursor"] = "hand2"
        self.Display.bind("<Button-1>",self.OnErrorLeftClick)
    
    #@-node:AGP.20230214111049.330:SyncDisplayToError
    #@+node:AGP.20230214111049.331:SetError
    def SetError(self,err,node=None):
        
        self.cc.PARSE_ERROR = err
        self.cc.PARSE_ERROR_NODE = node
    #@nonl
    #@-node:AGP.20230214111049.331:SetError
    #@+node:AGP.20230214111049.332:OnErrorLeftClick
    def OnErrorLeftClick(self,event):
        
        self.cc.GoToNode(self.cc.PARSE_ERROR_NODE)
    #@nonl
    #@-node:AGP.20230214111049.332:OnErrorLeftClick
    #@+node:AGP.20230214111049.333:HideInput
    def HideInput(self):
        self.PromptButton.pack_forget()
        self.DbgEntry.pack_forget()
    #@-node:AGP.20230214111049.333:HideInput
    #@+node:AGP.20230214111049.334:ShowInput
    def ShowInput(self):
        
        #self.ConfigButton.pack_forget()
        #self.WatchButton.pack_forget()
        
        self.PromptButton.pack(side="left")
        self.DbgEntry.pack(side="left",fill="x",expand=1)
    
        #self.ConfigButton.pack(side="right")
        #self.WatchButton.pack(side="right")
    #@nonl
    #@-node:AGP.20230214111049.334:ShowInput
    #@+node:AGP.20230214111049.335:Refresh
    def Refresh(self):
        try:
            cc = self.cc
    
            if (
                cc.ACTIVE_NODE and cc.DBG_PROMPT and
                cc.ACTIVE_NODE != cc.SELECTED_NODE
            ):
                cc.GoToNode(ACTIVE_NODE)
                QueryGoTaskClass(cc)
                cc.DbgOut("")
        except Exception:
            g.es_exception()
    #@nonl
    #@-node:AGP.20230214111049.335:Refresh
    #@-others

#@-node:AGP.20230214111049.321:class ToolbarClass
#@+node:AGP.20230214111049.336:class WatcherClass
class WatcherClass(Tk.Frame):

    #@    @+others
    #@+node:AGP.20230214111049.337:__init__
    def __init__(self,cc):
       
        self.cc = cc
        self.Watching = False
        self.visible = False
        
        Tk.Frame.__init__(self,cc.LeoBodyParent,relief='groove')
        
        self.EditFrame = Tk.Frame(self,relief='groove')
        self.VarEntry = Tk.Entry(self.EditFrame)
        self.VarEntry.bind("<Key>",self.OnEditKey)
        self.VarEntry.pack(side="left",fill="x",expand=1)
        self.EditFrame.pack(side="top",fill="x")
        
        self.BoxFrame = Tk.Frame(self,relief='groove')
        
        self.InFrame = Tk.Frame(self.BoxFrame,relief='groove')
        self.OutFrame = Tk.Frame(self.BoxFrame,relief='groove')
        self.BoxBar = Tk.Scrollbar(self.BoxFrame,command=self.yview)
        
        self.InFrame.pack(side="left",fill="both",expand=1)   
        self.BoxBar.pack(side="left",fill="y")
        self.OutFrame.pack(side="left",fill="both",expand=1)
        
        
        self.InXBar = Tk.Scrollbar(self.InFrame,orient="horizontal")
        self.InXBar.pack(side="bottom",fill="x")
        self.InBox = Tk.Text(
                self.InFrame,
                yscrollcommand=self.BoxBar.set,
                xscrollcommand=self.InXBar.set,font=cc.LeoFont,
                state='disabled',width=20,wrap='none',height=10,
                selectbackground="white",selectforeground="black")
        self.InXBar.config(command=self.InBox.xview)
        self.InBox.pack(side="bottom",fill="both",expand=1)
        
        self.OutXBar = Tk.Scrollbar(self.OutFrame,orient="horizontal")
        self.OutXBar.pack(side="bottom",fill="x")
        self.OutBox = Tk.Text(
            self.OutFrame,
            yscrollcommand=self.BoxBar.set,
            xscrollcommand=self.OutXBar.set,
            font=cc.LeoFont,state='disabled',width=20,wrap='none',height=10,
            selectbackground="white",selectforeground="black")
        self.OutXBar.config(command=self.OutBox.xview)   
        self.OutBox.pack(side="bottom",fill="both",expand=1)
    
        self.BoxFrame.pack(fill="both",expand=1)
        self.InBox.bind("<Delete>",self.OnDelete)
        self.OutBox.bind("<Delete>",self.OnDelete)
        self.InBox.bind("<Button-1>",self.OnLeftClick)
        self.OutBox.bind("<Button-1>",self.OnLeftClick)
    #@nonl
    #@-node:AGP.20230214111049.337:__init__
    #@+node:AGP.20230214111049.338:OnEditKey
    def OnEditKey(self,event):
        
        cc = self.cc
    
        if not self.Watching and len(event.char)==1 and ord(event.char) == 13:
            self.InBox.config(state='normal')
            self.OutBox.config(state='normal')
            
            var = self.VarEntry.get()
            cc.sGet("Watch",[]).append(var)
            
            self.InBox.mark_set("insert",'end')			
            self.InBox.insert("insert",var+"\n")
            
            self.OutBox.mark_set("insert",'end')
            self.OutBox.insert("insert","- ?? -\n")
            
            self.InBox.config(state='disabled')
            self.OutBox.config(state='disabled')
            self.VarEntry.delete(0, 'end')
            
            if cc.ACTIVE_PROCESS and cc.DBG_PROMPT and cc.SELECTED_NODE == cc.ACTIVE_NODE:
                WatchTaskClass(cc)
                cc.DbgOut("")
    #@nonl
    #@-node:AGP.20230214111049.338:OnEditKey
    #@+node:AGP.20230214111049.339:OnLeftClick
    def OnLeftClick(self,event):
       
        if self.InBox.get(1.0,'end').replace("\n",""):
            w = event.widget
            w.mark_set("insert","@0,"+str(event.y))
            l,c = w.index("insert").split(".")
        
            self.InBox.tag_delete("current")
            self.InBox.tag_add("current",l+".0",l+".end")
            self.InBox.tag_config("current",background=BreakColor)
        
            self.OutBox.tag_delete("current")
            self.OutBox.tag_add("current",l+".0",l+".end")
            self.OutBox.tag_config("current",background=BreakColor)
    #@nonl
    #@-node:AGP.20230214111049.339:OnLeftClick
    #@+node:AGP.20230214111049.340:OnDelete
    def OnDelete(self,event):
        if "current" in self.InBox.tag_names():
            ib = self.InBox ; ob = self.OutBox
            ib.config(state='normal')
            ob.config(state='normal')
            try:        
                s,e = ib.tag_nextrange("current","1.0")
                var = ib.get(s,e)	
                watchs = self.cc.sGet("Watch",[])
                if var in watchs:
                    watchs.remove(var)		
                ib.delete(s,e+"+1c")
                ib.tag_delete("current")
                
                s,e = ob.tag_nextrange("current","1.0")
                ob.delete(s,e+"+1c")
                ob.tag_delete("current")
                
            except Exception:
                pass
                
            ib.config(state='disabled')
            ob.config(state='disabled')
    #@nonl
    #@-node:AGP.20230214111049.340:OnDelete
    #@+node:AGP.20230214111049.341:yview
    def yview(self, *args):
        apply(self.InBox.yview,args)
        apply(self.OutBox.yview,args)
    #@nonl
    #@-node:AGP.20230214111049.341:yview
    #@+node:AGP.20230214111049.342:Hide
    def Hide(self):
        try:
            cc = self.cc
            self.pack_forget()
            self.visible = False
            cc.ToolBar.WatchButton.config(command=self.Show,relief='raised')
        except Exception:
            g.es_exception()
    #@nonl
    #@-node:AGP.20230214111049.342:Hide
    #@+node:AGP.20230214111049.343:Show
    def Show(self):
        try:
            cc = self.cc
            cc.HideWidgets()
            
            cc.LeoBodyText.pack_forget()
            cc.LeoXBodyBar.pack_forget()
            cc.LeoYBodyBar.pack_forget()
            
            self.pack(side = "bottom",fill="x")
            
            cc.LeoXBodyBar.pack(side = "bottom",fill="x")
            cc.LeoYBodyBar.pack(side="right",fill="y")
            if cc.BreakBar.visible:
                cc.BreakBar.Hide()
                cc.BreakBar.Show()
            cc.LeoBodyText.pack(fill="both",expand=1)
            
            cc.ToolBar.WatchButton.config(command=self.Hide,relief='sunken')
            self.visible = True
            self.Sync()
            
            if cc.ACTIVE_PROCESS and cc.DBG_PROMPT and cc.SELECTED_NODE == cc.ACTIVE_NODE:
                WatchTaskClass(cc)
                cc.DbgOut("")
        except Exception:
            g.es_exception()
    #@nonl
    #@-node:AGP.20230214111049.343:Show
    #@+node:AGP.20230214111049.344:Sync
    def Sync(self):
        
        cc = self.cc
    
        if self.visible == True:
            self.InBox.config(state='normal')
            self.OutBox.config(state='normal')
            
            self.InBox.delete(1.0,'end')
            self.OutBox.delete(1.0,'end')
            
            w = cc.sGet("Watch",[])
            for v in w:
                if v.strip() != "":
                    self.InBox.mark_set("insert",'end')
                    self.InBox.insert("insert",v+"\n")
                
                    self.OutBox.mark_set("insert",'end')
                    self.OutBox.insert("insert","- ?? -\n")
                else:
                    w.remove(v)
        
            self.InBox.config(state='disabled')
            self.OutBox.config(state='disabled')
    #@nonl
    #@-node:AGP.20230214111049.344:Sync
    #@-others
#@-node:AGP.20230214111049.336:class WatcherClass
#@+node:AGP.20230214111049.345:class DasmClass
class DasmClass(Tk.Frame):

    #@    @+others
    #@+node:AGP.20230214111049.346:__init__
    def __init__(self,cc):
       
        self.cc = cc
        self.Watching = False
        self.visible = False
        
        Tk.Frame.__init__(self,cc.LeoBodyParent,relief='groove')
        
        #self.DasmFrame = Tk.Frame(self,relief='groove')
        self.YBar = Tk.Scrollbar(self)
        self.XBar = Tk.Scrollbar(self,orient="horizontal")
        
        #self.DasmFrame.pack(side="left",fill="both",expand=1)   
        self.YBar.pack(side="right",fill="y")    
        self.XBar.pack(side="bottom",fill="x")
        
        self.DasmText = Tk.Text(
            self,
            yscrollcommand=self.YBar.set,
            xscrollcommand=self.XBar.set,
            font=cc.LeoFont,
            state='disabled',wrap='none',height=10)
        
        self.DasmText.pack(side="bottom",fill="both",expand=1)
        self.XBar.config(command=self.DasmText.xview)
        self.YBar.config(command=self.DasmText.yview)
    #@nonl
    #@-node:AGP.20230214111049.346:__init__
    #@+node:AGP.20230214111049.347:Hide
    def Hide(self):
        try:
            cc = self.cc
            self.pack_forget()
            self.visible = False
            cc.ToolBar.DasmButton.config(command=self.Show,relief='raised')
        except Exception:
            g.es_exception()
    #@nonl
    #@-node:AGP.20230214111049.347:Hide
    #@+node:AGP.20230214111049.348:Show
    def Show(self):
        try:
            cc = self.cc
            cc.HideWidgets()
            
            cc.LeoBodyText.pack_forget()
            cc.LeoXBodyBar.pack_forget()
            cc.LeoYBodyBar.pack_forget()
            
            self.pack(side = "bottom",fill="both",expand=1)
            
            cc.LeoXBodyBar.pack(side = "bottom",fill="x")
            cc.LeoYBodyBar.pack(side="right",fill="y")
            if cc.BreakBar.visible:
                cc.BreakBar.Hide()
                cc.BreakBar.Show()
            cc.LeoBodyText.pack(fill="both",expand=1)
            
            cc.ToolBar.DasmButton.config(command=self.Hide,relief='sunken')
            self.visible = True
            self.Sync()
            
            if cc.ACTIVE_PROCESS and cc.DBG_PROMPT and cc.SELECTED_NODE == cc.ACTIVE_NODE:
                DasmTaskClass(cc)
                cc.DbgOut("")
        except Exception:
            g.es_exception()
    #@nonl
    #@-node:AGP.20230214111049.348:Show
    #@+node:AGP.20230214111049.349:Sync
    def Sync(self):
        
        cc = self.cc
    
        if self.visible == True:
            self.DasmText.config(state='normal')
            
            self.DasmText.delete(1.0,'end')
            
            #for v in cc.sGet("Watch",[]):
            #    self.InBox.mark_set("insert",'end')			
            #    self.InBox.insert("insert",v+"\n")
                
            #    self.OutBox.mark_set("insert",'end')
            #    self.OutBox.insert("insert","- ?? -\n")	
        
            self.DasmText.config(state='disabled')
    #@nonl
    #@-node:AGP.20230214111049.349:Sync
    #@-others
#@-node:AGP.20230214111049.345:class DasmClass
#@+node:AGP.20230214111049.350:class BreakbarClass
class BreakbarClass(Tk.Text):

    #@    @+others
    #@+node:AGP.20230214111049.351:__init__
    def __init__(self,cc):
        
        self.cc = cc
        self.bodychanged = False	
        self.visible = False
        
        
        lbc = cc.LeoBodyText.winfo_rgb(cc.LeoBodyText["bg"])	
        lbc = red, green, blue = lbc[0]/256, lbc[1]/256, lbc[2]/256
        pred,pgreen,pblue = [-1,1][red<128],[-1,1][green<128],[-1,1][blue<128]
        
        #coff = 20
        #colors = red+pred*coff, green+pgreen*coff, blue+pblue*coff
        #bgcolor = self.bgcolor = "#%02x%02x%02x" % colors
        bgcolor = self.bgcolor = g.theme['shade'](0.1)
        #print bgcolor
        #coff = 30
        #colors = red+pred*coff, green+pgreen*coff, blue+pblue*coff
        #bg_dark  = "#%02x%02x%02x" % colors
        
        bg_dark = g.theme['shade'](0.05)
        
        #coff = 10
        #r,g,b = colors
        #colors = 255-r,255-g,255-b
        
        #colors = red+pred*coff, green+pgreen*coff, blue+pblue*coff
        
        #fgcolor = self.fgcolor = "#%02x%02x%02x" % colors
        fgcolor = self.fgcolor = g.theme['shade'](0.5)
        #print fgcolor
        
        bparent = cc.LeoBodyParent
        bbd = cc.LeoBodyText["bd"]
        bfont = cc.LeoFont
        bpady = cc.LeoBodyText["pady"]
        padx = 5
        #this is the header bar
        Tk.Text.__init__(self, bparent, bd=bbd, bg=bgcolor, fg=fgcolor, relief='flat', setgrid=0, font=bfont, padx=padx,pady=bpady, wrap='none',
            selectbackground = self.bgcolor,
            selectforeground = self.fgcolor,
            cursor="hand2",
            name='sidebar',
            width=4)
        
        self.source_bar = Tk.Text(bparent, bd=bbd, bg=bgcolor, fg=fgcolor, relief='flat', setgrid=0, font=bfont, padx=padx,pady=bpady, wrap='none',
            selectbackground = self.bgcolor,
            selectforeground = self.fgcolor,
            cursor="hand2",
            name='sidebar2',
            width=4)
        
        
        head_bar= self.head_bar = Tk.Frame(bparent)
        
        #bbd = 2
        #pady=1
        self.display = Tk.Text(head_bar, bd=bbd, bg=bg_dark, fg=g.theme['shade'](0.7), relief='flat', setgrid=0, font=bfont, padx=padx,pady=bpady, wrap='none',
            height=1,
            state='disabled')
            
        self.hdr_line = Tk.Text(head_bar, bd=bbd, bg=bgcolor, fg=fgcolor, relief='flat', setgrid=0, font=bfont, padx=padx,pady=bpady, wrap='none',
            height=1,
            width=4,
            #state='disabled'
            )
            
        self.src_line = Tk.Text(head_bar, bd=bbd, bg=bgcolor, fg=fgcolor, relief='flat', setgrid=0, font=bfont, padx=padx,pady=bpady, wrap='none',
            height=1,width=4,
            #state='disabled'
            )
            
        self.hdr_line.pack(side="left")
        self.display.pack(side="left",fill="x",expand=1)
        self.src_line.pack(side="right")
        
        #self.Display.pack(side="top",fill="x",expand=1)
        
        self.leowrap = cc.LeoBodyText["wrap"]
        #self.bind("<Button-1>",self.OnLeftClick)
        #self.bind("<Button-3>",self.OnRightClick)
        self["state"]='disabled'
        
        cc.LeoBodyText.pack_forget()
        cc.LeoXBodyBar.pack(side="bottom", fill="x")
        cc.LeoBodyText.pack(expand=1, fill="both")
    #@nonl
    #@-node:AGP.20230214111049.351:__init__
    #@+node:AGP.20230214111049.352:Scrollbar funcs
    #@+node:AGP.20230214111049.353:yview
    def yview(self,cmd=None,arg1=None,arg2=None):
        cc = self.cc ; w = cc.LeoBodyText
        #g.es("yview")
        if cmd:
            if arg1 != None:
                if arg2 != None:
                    w.yview(cmd,arg1,arg2)
                    Tk.Text.yview(self,cmd,arg1,arg2)
                    self.source_bar.yview(cmd,arg1,arg2)
                else:
                    w.yview(cmd,arg1)
                    Tk.Text.yview(self,cmd,arg1)
                    self.source_bar.yview(cmd,arg1)
        else:
            return w.yview()
    #@-node:AGP.20230214111049.353:yview
    #@+node:AGP.20230214111049.354:setForBody
    def setForBody(self,lo, hi):
        cc = self.cc
        #g.es("setforbody")
        Tk.Text.yview(self,'moveto',lo)
        self.source_bar.yview('moveto',lo)
        
        cc.LeoYBodyBar.set(lo,hi)	
    #@nonl
    #@-node:AGP.20230214111049.354:setForBody
    #@+node:AGP.20230214111049.355:setForBar
    def setForBar(self,lo, hi):
        cc = self.cc
        #g.es("setforbar")
        #cc.LeoBodyText.yview('moveto',lo)	
        cc.LeoYBodyBar.set(lo,hi)
    #@nonl
    #@-node:AGP.20230214111049.355:setForBar
    #@+node:AGP.20230214111049.356:Plug
    def Plug(self):
        
        cc = self.cc
        
        cc.LeoYBodyBar.command=self.yview
        cc.LeoBodyText["yscrollcommand"] = self.setForBody
        self["yscrollcommand"] = self.setForBar
        self.source_bar["yscrollcommand"] = self.setForBar
        
    #@nonl
    #@-node:AGP.20230214111049.356:Plug
    #@+node:AGP.20230214111049.357:UnPlug
    def UnPlug(self):
        
        cc = self.cc
        
        cc.LeoYBodyBar.command=cc.LeoBodyText.yview
        cc.LeoBodyText["yscrollcommand"] = cc.LeoYBodyBar.set
        self["yscrollcommand"] = None
        self.source_bar["yscrollcommand"] = None
        
    #@nonl
    #@-node:AGP.20230214111049.357:UnPlug
    #@-node:AGP.20230214111049.352:Scrollbar funcs
    #@+node:AGP.20230214111049.358:Events
    #@+node:AGP.20230214111049.359:OnRightClick
    def OnRightClick(self,event):
        try:
            m = Tk.Menu(self)
            m.add_command(label="Delete Node Breaks", command=self.DeleteNodeBreaks)
            m.add_command(label="Delete Project Breaks", command=self.DeleteProjectBreaks)
            m.add_separator()
            m.add_command(label="Cancel",command=lambda :self.Cancel(m))
            
            m.post(event.x_root,event.y_root)
        except Exception:
            g.es_exception()
        self.cc.LeoYBodyBar.focus_set()
    #@nonl
    #@-node:AGP.20230214111049.359:OnRightClick
    #@+node:AGP.20230214111049.360:OnLeftClick
    def OnLeftClick(self,event):
    
        cc = self.cc
        self["state"] = 'normal'	
        self.mark_set("insert","@0,"+str(event.y))
        self["state"] = 'disabled'
        l,c = self.index("insert").split(".")
        breaks = cc.cGet("BreakPoints")
        
        #print "onleftclick():"
        loc = LocatorClass(cc,cc.CHILD_NODE,l)
        if loc.FOUND_FILE_LINE == None:
            return
        
        filext = loc.FOUND_FILE_EXT.replace(".","")
        
        if l in breaks:
            self.DeleteBreak(filext,loc.FOUND_FILE_LINE,l)
        else:
            t = cc.LeoBodyText.get(str(l)+".0",str(l)+".end")
            if t != "\n" and t != "" and t.strip() != "@others":
                self.AddBreak(filext,loc.FOUND_FILE_LINE,l)
        
        self.tag_delete(Tk.SEL)
        self.cc.LeoYBodyBar.focus_set()
    #@nonl
    #@-node:AGP.20230214111049.360:OnLeftClick
    #@+node:AGP.20230214111049.361:IdleUpdate
    def IdleUpdate(self):
        if self.bodychanged == True:
            t,b = Tk.Text.yview(self)
            self.BreaksFromTags()
            Tk.Text.yview(self,Tk.MOVETO,t)
            self.bodychanged = False
    #@nonl
    #@-node:AGP.20230214111049.361:IdleUpdate
    #@-node:AGP.20230214111049.358:Events
    #@+node:AGP.20230214111049.362:Node breaks
    #@+node:AGP.20230214111049.363:AddNodeBreak
    def AddNodeBreak(self,l,s="Enabled"):
        self.cc.cGet("BreakPoints")[l] = s
    #@-node:AGP.20230214111049.363:AddNodeBreak
    #@+node:AGP.20230214111049.364:DeleteNodeBreak
    def DeleteNodeBreak(self,l):
        breaks = self.cc.cGet("BreakPoints")
        if l in breaks:
            del breaks[l]
    #@-node:AGP.20230214111049.364:DeleteNodeBreak
    #@+node:AGP.20230214111049.365:ClearNodeBreaks
    def ClearNodeBreaks(self):
        self.cc.cSet("BreakPoints",{})
    #@-node:AGP.20230214111049.365:ClearNodeBreaks
    #@+node:AGP.20230214111049.366:BreaksFromNode
    def BreaksFromNode(self):
        
        cc = self.cc
        self.ClearBreakTags()
        self.Sync()
        
        breaks = cc.cGet("BreakPoints",{})
        for l,s in breaks.iteritems():
            self.AddBarBreak(l,s)
            self.AddBreakTag(l)
    #@-node:AGP.20230214111049.366:BreaksFromNode
    #@-node:AGP.20230214111049.362:Node breaks
    #@+node:AGP.20230214111049.367:Bar Breaks
    #@+node:AGP.20230214111049.368:AddBarBreak
    def AddBarBreak(self,l,s="Enabled"):
        self["state"] = 'normal'
        #----------------------------------------
            
        fl = self.get(l+".0",l+".end")
        self.insert(l+".end",(int(self["width"])-len(str(fl))-1)*" "+">")
        self.tag_add(l,l+".0",l+".end")
        
        if s == "Enabled":
            self.tag_config(l,foreground="blue")
        else:
            self.tag_config(l,foreground="gray")
        #-----------------------------------------
        self["state"] = 'disabled'
    
    #@-node:AGP.20230214111049.368:AddBarBreak
    #@+node:AGP.20230214111049.369:DeleteBarBreak
    def DeleteBarBreak(self,l):
        self["state"] = 'normal'
        #----------------------------------------
        #self.insert(l+".end -2c","  ")
        self.delete(l+".end -1c",l+".end")
        self.tag_delete(l)	
        
        
        #-----------------------------------------
        self["state"] = 'disabled'
        self.update_idletasks()
    
    
    #@-node:AGP.20230214111049.369:DeleteBarBreak
    #@+node:AGP.20230214111049.370:ClearBarBreaks
    def ClearBarBreaks(self):
        
        cc = self.cc
        self["state"] = 'normal'
        self.delete(1.0,'end')	
        #----------------------------------------
        w =4
        if cc.CHILD_LINE and cc.CHILD_LINE != -1:
            yv = Tk.Text.yview(self)
            
            fl = cc.CHILD_LINE
            lines = cc.CHILD_NODE.bodyString().splitlines(True)
            l = ""
            while len(lines) > 0:
                l = lines.pop(0)
                if l.strip() != "@others":
                    self.insert("end",str(fl)+"\n")
                    fl += 1
                else:
                    break
                if len(lines)==0 and l[-1] == "\n":
                    self.insert("end",str(fl)+"\n")
        
            if l.strip() == "@others":
                self.insert("end","\n")
                
                #print "ckearbarbreak():"
                loc = LocatorClass(cc,cc.CHILD_NODE,fl-cc.CHILD_LINE+2)
                fl = loc.FOUND_FILE_LINE
                
                if fl != None:
                    while len(lines) > 0:
                        l = lines.pop(0)
                        self.insert("end",str(fl)+"\n")
                        fl += 1
                        if len(lines)==0 and l[-1] == "\n":
                            self.insert("end",str(fl)+"\n")
            if len(str(fl))+1 < w:
                pass
            else:
                w = len(str(fl))+1
                        
            self.yview(yv)
            self.config(width = w)
        #-----------------------------------------
        self["state"] = 'disabled'
    
    #@-node:AGP.20230214111049.370:ClearBarBreaks
    #@-node:AGP.20230214111049.367:Bar Breaks
    #@+node:AGP.20230214111049.371:tag breaks
    #@+node:AGP.20230214111049.372:AddBreakTag
    def AddBreakTag(self,l):
        
        w = self.cc.LeoBodyText
        
        w.tag_add("xcc_break",l+".0",l+".end")
    #@nonl
    #@-node:AGP.20230214111049.372:AddBreakTag
    #@+node:AGP.20230214111049.373:DeleteBreakTag
    def DeleteBreakTag(self,s,e=None):
        
        w = self.cc.LeoBodyText
        
        if e == None:
            w.tag_remove("xcc_break",s+".0",s+".end")
        else:
            w.tag_remove("xcc_break",s,e)
    #@nonl
    #@-node:AGP.20230214111049.373:DeleteBreakTag
    #@+node:AGP.20230214111049.374:ClearBreakTags
    def ClearBreakTags(self):
        
        w = self.cc.LeoBodyText
        w.tag_delete("xcc_break")
        w.tag_config("xcc_break",background=self.bgcolor)
    #@nonl
    #@-node:AGP.20230214111049.374:ClearBreakTags
    #@+node:AGP.20230214111049.375:BreaksFromTags
    def BreaksFromTags(self):
        
        cc = self.cc
        w = self.cc.LeoBodyText
        self.ClearNodeBreaks()
        self.ClearBarBreaks()
        range = w.tag_nextrange("xcc_break","1.0")
        while len(range) > 0:
            s,e = range
            el,ec = e.split(".")
            self.DeleteBreakTag(s,e)
            self.AddBreak(cc.CHILD_EXT,cc.CHILD_LINE,el)
            range = w.tag_nextrange("xcc_break",el+".end")
    #@nonl
    #@-node:AGP.20230214111049.375:BreaksFromTags
    #@-node:AGP.20230214111049.371:tag breaks
    #@+node:AGP.20230214111049.376:AddBreak
    def AddBreak(self,filext,fileline,bodyline,state="Enabled"):
        
        cc = self.cc
        breaks = cc.sGet("BreakPoints",{})
        
        breaks[filext+":"+str(fileline)] = state
        
        bl = str(bodyline)
        self.AddNodeBreak(bl,state)
        self.AddBarBreak(bl,state)
        self.AddBreakTag(bl)
        
        if cc.ACTIVE_PROCESS:
            bpat = cc.DBG.get("Set break")
            bpat = bpat.replace("_FILE_",cc.NAME+"."+filext).replace("_LINE_",str(fileline))
            DbgTaskClass(cc,bpat)
            if cc.DBG_PROMPT:
                cc.DbgOut("")
    
    #@-node:AGP.20230214111049.376:AddBreak
    #@+node:AGP.20230214111049.377:DeleteBreak
    def DeleteBreak(self,filext,fileline,bodyline):
        
        cc = self.cc
            
        bl = str(bodyline)
        self.DeleteNodeBreak(bl)
        self.DeleteBarBreak(bl)
        self.DeleteBreakTag(bl)
        
        if cc.SELECTED_NODE == cc.ACTIVE_NODE:
            if cc.DBG.get("Clear break",'').find("_ID_") != -1:
                BreakIdTaskClass(cc,[filext,str(fileline)])
            else:
                DbgTaskClass(cc,cc.ReplaceVars(cc.DBG["Clear break"]).replace("_FILE_",cc.NAME+"."+filext).replace("_LINE_",str(fileline)))
            
            if cc.DBG_PROMPT:
                cc.DbgOut("")
    #@-node:AGP.20230214111049.377:DeleteBreak
    #@+node:AGP.20230214111049.378:DeleteNodeBreaks
    def DeleteNodeBreaks(self):
        try:
            cc = self.cc
      
            breaks = cc.cGet("BreakPoints",{})
            
            if cc.CHILD_LINE and cc.CHILD_EXT:
                for bp in breaks.keys():
                    self.DeleteBreak(cc.CHILD_EXT,cc.CHILD_LINE+int(bp),int(bp))
        
            cc.cSelect(cc.CHILD_NODE)
        except Exception:
            g.es_exception()
    #@nonl
    #@-node:AGP.20230214111049.378:DeleteNodeBreaks
    #@+node:AGP.20230214111049.379:DeleteProjectBreaks
    def DeleteProjectBreaks(self):
        
        cc = self.cc
       
        if cc.SELECTED_NODE:
            for c in cc.SELECTED_NODE.subtree_iter():
                ua = cc.GetUnknownAttributes(c.v)
                if ua and "xcc_child_cfg" in ua.keys():
                    if "BreakPoints" in ua["xcc_child_cfg"].keys():
                        ua["xcc_child_cfg"]["BreakPoints"] = {}
        
            cc.cSelect(cc.CHILD_NODE)
    #@nonl
    #@-node:AGP.20230214111049.379:DeleteProjectBreaks
    #@+node:AGP.20230214111049.380:Hide
    def Hide(self,erase = False):
        
        w = self.cc.LeoBodyText
        self.UnPlug()
        
        self.pack_forget()
        self.source_bar.pack_forget()
        self.head_bar.pack_forget()
        
        w.pack(expand=1, fill="both")
        w.tag_delete("xcc_break")
        
        self.visible = False
    #@nonl
    #@-node:AGP.20230214111049.380:Hide
    #@+node:AGP.20230214111049.381:Show
    def Show(self,locator=None):
    
        cc = self.cc
        
        if not locator:
            locator = LocatorClass(cc,cc.CHILD_NODE,1)
            cc.CHILD_EXT = locator.FOUND_FILE_EXT
            cc.CHILD_LINE = locator.FOUND_FILE_LINE
        
        show_header_line = locator.FOUND_BODY_HDR_LINE or locator.FOUND_HEAD_HDR_LINE
        show_source_line = locator.FOUND_BODY_SRC_LINE or locator.FOUND_HEAD_SRC_LINE
        
        if True:#not self.visible:
            self.Plug()
            cc.LeoBodyText.pack_forget()
            cc.LeoYBodyBar.pack_forget()
            #cc.ToolBar.pack_forget()
        
            
        
            border = cc.LeoBodyText ["bd"]
            py = cc.LeoBodyText["pady"]
            self.config(pady=py,bd=border)
            self.source_bar.config(pady=py,bd=border)
            
            
            
            self.pack_forget()
            self.head_bar.pack_forget()
            self.source_bar.pack_forget()
            
            if self.leowrap != 'none':
                cc.LeoXBodyBar.pack(side="bottom",fill="x")
            
            self.head_bar.pack(side="top",fill="x")
            if show_header_line:
                self.pack(side='left',fill="y") #header
            if show_source_line:
                self.source_bar.pack(side='right',fill="y")
            
            
            
            #cc.LeoXBodyBar.pack(side="bottom",fill="x")
            cc.LeoYBodyBar.pack(side="right",fill="y")
            
            
            cc.LeoBodyText.pack(expand=1,fill="both")
        #self.BreaksFromNode()--------------
        if locator:        
            
            self.hdr_line.pack_forget()
            self.display.pack_forget()
            self.src_line.pack_forget()
            if show_header_line:
                self.hdr_line.pack(side="left")
            
            
            
            if show_source_line:
                self.src_line.pack(side="right")
            self.display.pack(side="left",fill="x",expand=1)
            
            self.ClearBreakTags()
                
            self.SyncDisplayToChild(locator)
            self.Sync(locator)
        
            breaks = cc.cGet("BreakPoints",{})
            for l,s in breaks.iteritems():
                self.AddBarBreak(l,s)
                self.AddBreakTag(l)
        
        #-------------------------------------
        
        
        
        
        self.visible = True
    #@nonl
    #@-node:AGP.20230214111049.381:Show
    #@+node:AGP.20230522153016:SyncDisplayToChild
    def SyncDisplayToChild(self,loc):
        
        cc = self.cc
        self.display["cursor"] = ""
        self.display.unbind("<Button-1>")
            
        
        hline = None
        
        if loc.FOUND_HEAD_SRC_LINE:
            hext = self.cc.SRC_EXT
            hline = "." + str(loc.FOUND_HEAD_SRC_LINE)
        
        if loc.FOUND_HEAD_HDR_LINE:
            hext = self.cc.HDR_EXT
            if hline != None:
                hline = ":" + str(loc.FOUND_HEAD_HDR_LINE)
            else:
                hline = "'" + str(loc.FOUND_HEAD_HDR_LINE)
           
        class_list = loc.CLASS_LIST
        if loc.CURRENT_RULE == "class" and len(class_list) > 0:
            class_list.pop(-1)
            
        #access specifier
        disp = "::".join(class_list)
        if len(disp) > 0:
            disp += "::"
        
        off = len(disp)
        disp += cc.CHILD_NODE.headString()
        
        self.display["state"] = 'normal'
        self.display.delete(1.0,'end')
        self.display.tag_delete("marking")
        self.display.insert("insert",disp)
        
        if loc.CURRENT_RULE == "class":
            spec,name,base,inst,dest = loc.CURRENT_CLASS_MO
            #print loc.CURRENT_CLASS_MO
            v,s,e = name
            if v != "":
                self.display.tag_add("marking","1.0","1."+str(s+off-1))
                
            v,s,e = base
            if v != "":
                do_search = True
                while do_search:
                    do_search = False
                    
                    for term in ["public","private","protected"]:
                        tl = len(term)
                        toff = v.find(term)
                        if toff != -1:
                            #print "term",term,toff
                            do_search = True
                            self.display.tag_add("marking","1."+str(s+off+toff),"1."+str(s+off+toff+tl))
                            v = v[toff+tl:]
        
        if loc.CURRENT_RULE == "func":
            spec,ret,name,params,pure,dest,ctors = loc.CURRENT_FUNC_MO
            
            v,s,e = spec
            if v != "":
                self.display.tag_add("marking","1."+str(s+off),"1."+str(e+off))
            
            v,s,e = ret
            if s != -1 and e != -1:
                self.display.tag_add("marking","1."+str(s+off),"1."+str(e+off))		
            
            params,s,e = params
            if params != "()":
                s += 1
                params = params.split(",")
                for p in params:
                    pmo = re.search("[( ]*(?P<TYPE>.+) +(?P<NAME>[^) ]+)[ )]*",p)
                    if pmo != None:
                        s2,e2 = pmo.span("TYPE")
                        self.display.tag_add("marking","1."+str(s+off+s2-1),"1."+str(s+off+(e2-s2)))
                        off += len(p)+1
                        
        
        if loc.CURRENT_RULE == "doc":
            self.display.insert("insert",loc.DocName())
            
        self.display.tag_config("marking",foreground=g.theme['keyword'])#"#7575e5")
        self.display["state"] = 'disabled'
    
    
    #@-node:AGP.20230522153016:SyncDisplayToChild
    #@+node:AGP.20230214111049.382:Sync
    def Sync(self,locator):
        
        cc = self.cc
        
        src_bar = self.source_bar
        self["state"] = 'normal'
        src_bar["state"] = 'normal'
        
        self.delete(1.0,'end')
        src_bar.delete(1.0,'end')
        
        
        
        self.hdr_line.delete(1.0,'end')
        self.src_line.delete(1.0,'end')
        #----------------------------------------
        
    
        bfm = ""    #body file marker
        if locator.FOUND_BODY_SRC_LINE:
            bfm = "."
        
        if locator.FOUND_BODY_HDR_LINE:
            bext = self.cc.HDR_EXT
            if bfm != "":
                bfm = ":"
            else:
                bfm = "'"
        
    
        bhlw = bslw = 1
        
        hhl = locator.FOUND_HEAD_HDR_LINE
        hsl = locator.FOUND_HEAD_SRC_LINE
        
        #print "sync",locator.FOUND_HEAD_HDR_LINE,locator.FOUND_HEAD_SRC_LINE
        
        if hhl:
            bhlw = len(str(hhl))
        
            self.hdr_line.insert("end",str(hhl)+"\n")
            #print "hdr_linr",hhl
        else:
            self.hdr_line.insert("end","\n")
            
        if hsl:
            bslw = len(str(hsl))
            self.src_line.insert("end",str(hsl)+"\n")
            #print "src_linr",hsl
        else:
            self.src_line.insert("end","\n")
    
    
        bhl = locator.FOUND_BODY_HDR_LINE
        bsl = locator.FOUND_BODY_SRC_LINE
    
        if cc.CHILD_LINE and cc.CHILD_LINE != -1:
            fl = cc.CHILD_LINE
            bs = cc.CHILD_NODE.bodyString()
            lines = bs.splitlines(True)
            
            
            
            if locator.FOUND_OTHERS:
                body_line,hdr_line,src_line = locator.FOUND_OTHERS
            else:
                body_line,hdr_line,src_line = -1,-1,-1
            
            #print body_line,hdr_line,src_line
            #print bhl,bsl
            
            for i in range(len(lines)):
                if i == len(lines)-1:
                    nl = ""
                else:
                    nl = "\n"
                
                if i == body_line-1:
                    if bhl:
                        self.insert("end",nl)
                        #fl = hdr_line
                        bhl = hdr_line+2
                    if bsl:
                        src_bar.insert("end",nl)
                        bsl = src_line+2
                    
                else:
                    if bhl:
                        self.insert("end",str(bhl)+nl)
                        src_bar
                        bhl += 1
                    if bsl:
                        src_bar.insert("end",str(bsl)+nl)
                        bsl += 1
            
                    
                  
            #if len(bhl) > 0:
            #self.delete("end - 1 chars")
            #if len(bsl) > 0:
            #self.source_bar.delete("end - 1 chars")
            
            """while len(lines) > 0:
                l = lines.pop(0)
                if l.strip() != "@others":
                    self.insert("end",str(fl)+"\n")
                    fl += 1
                else:
                    break
        
            if len(lines) > 0 and l.strip() == "@others":
                self.insert("end","\n")
                
                #print "sync():"
                #locator.ResumeParse(fl-cc.CHILD_LINE+2)
                #loc = LocatorClass(cc,cc.CHILD_NODE,fl-cc.CHILD_LINE+2)
                fl = locator.FOUND_FILE_LINE
                
                if fl != None:
                    while len(lines) > 0:
                        l = lines.pop(0)
                        self.insert("end",str(fl)+"\n")
                        fl += 1
                                """
            if len(str(bhl)) > bhlw:
                bhlw = len(str(bhl))
                
            if len(str(bsl)) > bslw:
                bslw = len(str(bsl))
            #print "width",bhlw,bslw
        self.config(width = bhlw)
        self.source_bar.config(width = bslw)
        
        self.hdr_line.config(width = bhlw)
        self.src_line.config(width = bslw)
        
        
        #cc.ToolBar.Spacer.config(width=w+1)
        #-----------------------------------------
        self.source_bar["state"] = 'disabled'
        self["state"] = 'disabled'
    #@-node:AGP.20230214111049.382:Sync
    #@+node:AGP.20230214111049.383:Cancel
    def Cancel(self,menu):
        menu.unpost()
        
    #@-node:AGP.20230214111049.383:Cancel
    #@-others
#@-node:AGP.20230214111049.350:class BreakbarClass
#@+node:AGP.20230214111049.384:class DocEditClass
class DocEditClass(Tk.Text):
    #@    @+others
    #@+node:AGP.20230214111049.385:__init__
    def __init__(self,cc):
        self.cc = cc
        
        self.MainFrame = Tk.Frame(cc.LeoBodyParent,relief='groove')
        
        
        #@    @+others
        #@+node:AGP.20230214111049.386:TopBar
        self.TopBar = Tk.Frame(self.MainFrame,relief='ridge',height=20,bd=2)
        self.TopBar.pack(side="top",fill="x",expand=1)    
        #@+others
        #@-others
        #@nonl
        #@-node:AGP.20230214111049.386:TopBar
        #@+node:AGP.20230214111049.387:New Topic
        self.CheckValue = Tk.StringVar()
        self.Check = Tk.Checkbutton(self.TopBar,
                                    offvalue="False",
                                    onvalue="True",
                                    command=self.SaveToNode,
                                    variable=self.CheckValue,
                                    text="New Topic")    
        self.Check.pack(side="left")
        #@nonl
        #@-node:AGP.20230214111049.387:New Topic
        #@+node:AGP.20230214111049.388:Use Head
        self.HeadValue = Tk.StringVar()
        self.Head = Tk.Checkbutton(self.TopBar,
                                    offvalue="False",
                                    onvalue="True",
                                    command=self.SaveToNode,
                                    variable=self.HeadValue,
                                    text="Use Head")    
        self.Head.pack(side="left")
        #@nonl
        #@-node:AGP.20230214111049.388:Use Head
        #@+node:AGP.20230214111049.389:Pre Format
        self.PreValue = Tk.StringVar()
        self.Pre = Tk.Checkbutton(self.TopBar,
                                    offvalue="False",
                                    onvalue="True",
                                    command=self.SaveToNode,
                                    variable=self.PreValue,
                                    text="Preformat")    
        self.Pre.pack(side="left")
        #@nonl
        #@-node:AGP.20230214111049.389:Pre Format
        #@-others
        
        coffset=10
        c = cc.LeoBodyText.winfo_rgb(cc.LeoBodyText["bg"])	
        red, green, blue = c[0]/256, c[1]/256, c[2]/256
        #red -= coffset ; green -= coffset
        
        pred,pgreen,pblue = [-1,1][red<128],[-1,1][green<128],[-1,1][blue<128]
        
        coff = 10
        colors = red+pred*coff, green+pgreen*coff, blue+pblue*coff
        
        bg = "#%02x%02x%02x" % colors
        
        Tk.Text.__init__(self,
            self.MainFrame,
            name='sidebar',
            bg=bg,#cc.BreakBar.cget("bg"),
            width=2,
            height=10,
            bd=cc.LeoBodyText["bd"],
            relief='flat',
            setgrid=0,
            font=cc.LeoFont,
            pady=cc.LeoBodyText["pady"],
            wrap='none'
        )
        
        self.YBar = Tk.Scrollbar(self.MainFrame,command=self.yview)
        self.YBar.pack(side="right",fill="y")
        
        self.bind("<KeyRelease>",self.OnKeyRelease)
        self.pack(side="top",fill="both",expand=1)    
        
        self.XBar = Tk.Scrollbar(self.MainFrame,orient="horizontal",command=self.xview)
        self.XBar.pack(side="bottom",fill="x")
        
        self.config(yscrollcommand=self.YBar.set)
        self.config(xscrollcommand=self.XBar.set)
        
        self.visible = False
    #@-node:AGP.20230214111049.385:__init__
    #@+node:AGP.20230214111049.390:Show
    def Show(self):
        try:
            cc = self.cc
            cc.HideWidgets()
            
            cc.LeoBodyText.pack_forget()
            cc.LeoXBodyBar.pack_forget()
            cc.LeoYBodyBar.pack_forget()
            
            self.MainFrame.pack(side = "bottom",fill="x")
            
            cc.LeoXBodyBar.pack(side = "bottom",fill="x")
            cc.LeoYBodyBar.pack(side="right",fill="y")
            if cc.BreakBar.visible:
                cc.BreakBar.Hide()
                cc.BreakBar.Show()
            cc.LeoBodyText.pack(fill="both",expand=1)
            
            cc.ToolBar.DocButton.config(command=self.Hide,relief='sunken')
            self.visible = True
            
            self.LoadFromNode()
            
        except Exception:
            g.es_exception()
    #@nonl
    #@-node:AGP.20230214111049.390:Show
    #@+node:AGP.20230214111049.391:Hide
    def Hide(self):
        try:
            cc = self.cc
            self.MainFrame.pack_forget()
            self.visible = False
            cc.ToolBar.DocButton.config(command=self.Show,relief='raised')
            #self.SaveToNode()
        except Exception:
            g.es_exception()
    #@nonl
    #@-node:AGP.20230214111049.391:Hide
    #@+node:AGP.20230214111049.392:LoadFromNode
    def LoadFromNode(self):
        cc = self.cc
        self.delete(1.0,'end')
        if cc.CHILD_NODE:        
            self.insert("insert",cc.cGet("DOC",""))
            self.Check.pack(side="left")
            self.Head.pack(side="left")
            self.Pre.pack(side="left")
            self.CheckValue.set(cc.cGet("NEW_TOPIC","False"))
            self.HeadValue.set(cc.cGet("USE_HEAD","False"))
            self.PreValue.set(cc.cGet("PRE_FORMAT","False"))
            
        else:
            self.insert("insert",cc.sGet("DOC",""))
            self.Check.pack_forget()
            self.Head.pack_forget()
            self.Pre.pack_forget()
    #@nonl
    #@-node:AGP.20230214111049.392:LoadFromNode
    #@+node:AGP.20230214111049.393:SaveToNode
    def SaveToNode(self):
        cc = self.cc  
        if cc.CHILD_NODE:
            cc.cSet("DOC",self.get(1.0,"end-1c"))
            cc.cSet("NEW_TOPIC",self.CheckValue.get())
            cc.cSet("USE_HEAD",self.HeadValue.get())
            cc.cSet("PRE_FORMAT",self.PreValue.get())
            cc.CHILD_NODE.setDirty()
        else:
            cc.sSet("DOC",self.get(1.0,"end-1c"))
            cc.SELECTED_NODE.setDirty()
        
        cc.c.setChanged(True)   
        #cc.c.redraw() #
    #@nonl
    #@-node:AGP.20230214111049.393:SaveToNode
    #@+node:AGP.20230214111049.394:OnKeyRelease
    def OnKeyRelease(self,event):
        self.SaveToNode()
        
    #@nonl
    #@-node:AGP.20230214111049.394:OnKeyRelease
    #@-others
#@nonl
#@-node:AGP.20230214111049.384:class DocEditClass
#@+node:AGP.20230214111049.395:HELP
#@+node:AGP.20230214111049.396:Options
#@+node:AGP.20230214111049.397:BuildSequence
OptBuildSequenceHelp = """
Tool launch sequence, each line represents a process 
and they are called in the order that they appear.

File name and arguments must be separated by an "@"
in the form:    pathandfilename@args
    
The COMPILE keyword triggers compilation.
The LINK keyword triggers linkage.

The following variables are supported:
        
    _ABSPATH_
    _RELPATH_
    _NAME_
    _EXT_
    _SRCEXT_
    _BUILD_
    _INCPATHS_
    _LIBPATHS_
    _LIBRARIES_"""
#@nonl
#@-node:AGP.20230214111049.397:BuildSequence
#@-node:AGP.20230214111049.396:Options
#@+node:AGP.20230214111049.398:Compiler
#@+node:AGP.20230214111049.399:CplArgumentsHelp
CplArgumentsHelp = """
Command line passed to to the compiler.
Each lines are concatenated using space.

The following variables are supported:
        
    _ABSPATH_
    _RELPATH_
    _NAME_
    _EXT_
    _SRCEXT_
    _BUILD_
    _INCPATHS_
    _LIBPATHS_
    _LIBRARIES_"""
#@nonl
#@-node:AGP.20230214111049.399:CplArgumentsHelp
#@+node:AGP.20230214111049.400:CplDebugArgumentsHelp
CplDebugArgumentsHelp = """
Command line passed to to the compiler 
when debugging is requested.
Each lines are concatenated using space.

The following variables are supported:
        
    _ABSPATH_
    _RELPATH_
    _NAME_
    _EXT_
    _SRCEXT_
    _BUILD_
    _INCPATHS_
    _LIBPATHS_
    _LIBRARIES_"""
#@nonl
#@-node:AGP.20230214111049.400:CplDebugArgumentsHelp
#@+node:AGP.20230214111049.401:IncludeSearchPathsHelp
IncludeSearchPathsHelp = """
Each lines is a path to be searched for include files.

These paths are assembled unsing the "Include path"
symbol to create the _INCPATHS_ variable."""
#@nonl
#@-node:AGP.20230214111049.401:IncludeSearchPathsHelp
#@+node:AGP.20230214111049.402:LibrarySearchPathsHelp
LibrarySearchPathsHelp = """
Each lines is a path to be searched for library files.

These paths are assembled unsing the "Library path"
symbol to create the _LIBPATHS_ variable."""
#@nonl
#@-node:AGP.20230214111049.402:LibrarySearchPathsHelp
#@+node:AGP.20230214111049.403:UsedLibrariesHelp
UsedLibrariesHelp = """
Each whitespace delimited word is a libary to be 
used while building the project.

These libraries are assembled unsing the "Use library"
symbol to create the _LIBRARIES_ variable."""
#@nonl
#@-node:AGP.20230214111049.403:UsedLibrariesHelp
#@+node:AGP.20230214111049.404:IncludePathAndLibraryPathHelp
IncludePathAndLibraryPathHelp = """
Include path:	
    Symbol used with "Include search path" field
    to create the _INCPATHS_ variable.
    
Library path:	
    Symbol used with "Library search path" field
    to create the _LIBPATHS_ variable."""
#@-node:AGP.20230214111049.404:IncludePathAndLibraryPathHelp
#@+node:AGP.20230214111049.405:UseLibraryAndCheckSyntaxeHelp
UseLibraryAndCheckSyntaxeHelp = """
Use library:	
    Symbol used with "Used libraries" field
    to create the _LIBRARIES_ variable.
    
Check syntaxe:	
    Symbol used when the project is a single
    header (.h extension). Header alone cant be 
    built but some compiler offer a syntaxe check."""
#@nonl
#@-node:AGP.20230214111049.405:UseLibraryAndCheckSyntaxeHelp
#@+node:AGP.20230214111049.406:BuildExeAndBuildDllHelp
BuildExeAndBuildDllHelp = """
One of these symbols will be used to replace
the _BUILD_ variable in the "Arguments" and 
"Debug arguments" fields.

The correct one is choosed according to the
project extension.

These generally determine if the output is 
single or multi-threaded.

Build exe:	
    Symbol used to build an executable.
    
Build dll:	
    Symbol used to build a dll."""
#@nonl
#@-node:AGP.20230214111049.406:BuildExeAndBuildDllHelp
#@+node:AGP.20230214111049.407:CompilePchAndUsePchHelp
CompilePchAndUsePchHelp = """
TODO: Support precompiled header auto creation/inclusion."""
#@nonl
#@-node:AGP.20230214111049.407:CompilePchAndUsePchHelp
#@+node:AGP.20230214111049.408:ErrorDetectionHelp
ErrorDetectionHelp = """
Regular expression used to detect error 
from the compiler output.

The following groups must be defined by
the regular expression:
    
    FILE
    LINE
    ID *
    DEF *
    
    * = Facultative groups"""
#@-node:AGP.20230214111049.408:ErrorDetectionHelp
#@-node:AGP.20230214111049.398:Compiler
#@+node:AGP.20230214111049.409:Debugger
#@+node:AGP.20230214111049.410:DbgArgumentsHelp
DbgArgumentsHelp = """
Command line passed to to the debugger.
Each lines are concatenated using space.

The following variables are supported:
        
    _ABSPATH_
    _RELPATH_
    _NAME_
    _EXT_
    _SRCEXT_"""
#@nonl
#@-node:AGP.20230214111049.410:DbgArgumentsHelp
#@+node:AGP.20230214111049.411:DbgPipingHelp
DbgPipingHelp = """
Prompt pattern:
    Regular expression used to detect the debugger prompt.
    
Pipe eol:
    End of line character used when sending command to the debugger."""
#@nonl
#@-node:AGP.20230214111049.411:DbgPipingHelp
#@+node:AGP.20230214111049.412:DbgStartupTaskHelp
DbgStartupTaskHelp = """
Commands sent to the debugger at startup.
These commands must leave the debugger breaked
in the entry point of the target.

The following variables are supported:
    
    _ABSPATH_
    _RELPATH_
    _NAME_
    _EXT_
    _SRCEXT_"""
#@nonl
#@-node:AGP.20230214111049.412:DbgStartupTaskHelp
#@+node:AGP.20230214111049.413:DbgTargetPidHelp
DbgTargetPidHelp = """
Target pid task:
    Command used to retreive the target process identifier.
    The target pid is used to break into the debugger.

    The following variables are supported:
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
    
Find pid:
    Regular expression used to retreive the target pid when
    the "Target pid task" is sent to the debugger.

    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        
    The following groups must be returned by the regular expression:
        
        PID"""
#@nonl
#@-node:AGP.20230214111049.413:DbgTargetPidHelp
#@+node:AGP.20230214111049.414:DbgBreakDetectionHelp
DbgBreakDetectionHelp = """
Regular expression used to detect a break in target code execution.

When an output line match one of the expressions, an attempt is 
made to find the current location in the target code using the
"Query location" and "Find location" fields.

Each line is a different regular expression."""
#@nonl
#@-node:AGP.20230214111049.414:DbgBreakDetectionHelp
#@+node:AGP.20230214111049.415:DbgSetClearBreakHelp
DbgSetClearBreakHelp = """
Set break:
    Command used to set a breakpoint.
    
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        _FILE_
        _LINE_

Clear break:
    Command used to clear/delete a breakpoint.
    
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        _FILE_
        _LINE_
        _ID_*
        
    *If _ID_ is used, attempt to find it using the
    "List breaks" and "Identify break" fields."""
#@-node:AGP.20230214111049.415:DbgSetClearBreakHelp
#@+node:AGP.20230214111049.416:DbgBreakIdHelp
DbgBreakIdHelp = """
List breaks:
    Command used to list the debugger's break table.
    
    This field is ignored if the "Clear break" field
    make no use of the _ID_ variable.
    
Identify break:
    Regular expresion used to find the id of a breakpoint
    when the "List breaks" command is sent to the debugger.
    
    This field is ignored if the "Clear break" field
    make no use of the _ID_ variable.
    
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        _FILE_
        _LINE_
        
    The following groups must be returned by the regular expression:
        
        ID"""
#@-node:AGP.20230214111049.416:DbgBreakIdHelp
#@+node:AGP.20230214111049.417:DbgLocationHelp
DbgLocationHelp = """
Query location:
    Command used to retreive the file and line where
    the debugger is currently breaked.
    
Find location:
    Regular expression used to retreiv the current 
    file and line when the "Query location" command
    is sent to the debugger.
    
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        
    The following groups must be returned by the regular expression:
        
        EXT
        LINE

"""
#@-node:AGP.20230214111049.417:DbgLocationHelp
#@+node:AGP.20230214111049.418:DbgMiscExpHelp
DbgMiscExpHelp = """
Regular expression:
    Each line is a separate regular expression.
    
    If an output line is matched by one of the expression,
    the corresponding "Task" line is sent to the debugger.
        
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_
        
Task:
    Each line is a separate task trigered by the corresponding
    "Regular expression" line.
    
    The following variables are supported:
        
        _ABSPATH_
        _RELPATH_
        _NAME_
        _EXT_
        _SRCEXT_"""
#@nonl
#@-node:AGP.20230214111049.418:DbgMiscExpHelp
#@-node:AGP.20230214111049.409:Debugger
#@-node:AGP.20230214111049.395:HELP
#@-node:AGP.20230214111049.222:Widget classes
#@+node:AGP.20230214111049.419:Parsing classes
#@+node:AGP.20230320235129:OUTPUT
class OUTPUT:
    #@    @+others
    #@+node:AGP.20230320235129.1:__init__()
    def __init__(self,parser,writer=None):
        
        self.parser = parser
        self.writer = writer
        
        self.tabstack = []
        self.endstack = []
        
        self.tablist = []
        self.endlist = []
        
        self.tabstring = ""
        self.endstring = ""
        
        self.CURRENT_LINE = 0
    #@nonl
    #@-node:AGP.20230320235129.1:__init__()
    #@+node:AGP.20230320235129.2:__call__():
    def __call__(self,lines,strip=True,nl=True):
        
        if isinstance(lines,basestring):
            lines = lines.split('\n')
        
        if len(lines) > 1 and lines[-1]=="":
            lines.pop(-1)
        
        
        ts = self.tabstring
        es = self.endstring
        
        if nl:
            es = es+'\n'
        
        p = self.parser
        w = self.write
        
        line_filter = p.line_filter
        
        CURRENT_LOCATION = p.CURRENT_LOCATION
        
        if CURRENT_LOCATION != 1:
            p.CURRENT_BODY_LINE = 0
        
        for l in lines:
            if CURRENT_LOCATION == 1:
                p.CURRENT_BODY_LINE += 1	
            
            #if nl:
            #    print "line++",nl
            self.CURRENT_LINE += 1
            #print "call()",ts,"|"
            #if strip:
            #    l = l.rstrip()
            
            if line_filter:
                l = line_filter(l)
            #print ts + l + es
            w( ts + l + es )
            
        
    
    
        
        
    #@nonl
    #@-node:AGP.20230320235129.2:__call__():
    #@+node:AGP.20230320235129.4:tab
    def tab(self,tab=None,end=None):
        if tab:
            self.tablist.append(tab)
        if end:
            self.endlist.insert(0,end)
        
        self.tabstring = "".join(self.tablist)
        self.endstring = "".join(self.endlist)
    #@nonl
    #@-node:AGP.20230320235129.4:tab
    #@+node:AGP.20230320235129.5:untab
    def untab(self,tab=True,end=True):
        if tab:
            self.tablist.pop(-1)
        if end:
            self.endlist.pop(0)
        
        self.tabstring = "".join(self.tablist)
        self.endstring = "".join(self.endlist)
    #@nonl
    #@-node:AGP.20230320235129.5:untab
    #@+node:AGP.20230320235129.6:pushtab
    def pushtab(self):
        self.tabstack.insert(0,self.tablist)
        self.tablist = []
        
        self.endstack.insert(0,self.endlist)
        self.endlist = []
        
        self.tabstring = "".join(self.tablist)
        self.endstring = "".join(self.endlist)
    #@nonl
    #@-node:AGP.20230320235129.6:pushtab
    #@+node:AGP.20230320235129.7:poptab
    def poptab(self):
        #self.tabstring = self.tablist.pop(-1)
        
        self.tablist = self.tabstack.pop(0)
        
        
        self.endlist = self.endstack.pop(0)
        
        self.tabstring = "".join(self.tablist)
        self.endstring = "".join(self.endlist)
    #@nonl
    #@-node:AGP.20230320235129.7:poptab
    #@+node:AGP.20230321135641:write()
    def write(self):
        pass
        
    #@nonl
    #@-node:AGP.20230321135641:write()
    #@-others
#@nonl
#@-node:AGP.20230320235129:OUTPUT
#@+node:AGP.20230529212053:OUTLIST
class OUTLIST:
    #@    @+others
    #@+node:AGP.20230529212053.1:__init__()
    def __init__(self,outputs):
        
        self.outputs = outputs
    #@-node:AGP.20230529212053.1:__init__()
    #@+node:AGP.20230529212053.2:__call__():
    def __call__(self,lines,strip=True,nl=True):
        
        for o in self.outputs:
            o(lines,strip,nl)
    #@-node:AGP.20230529212053.2:__call__():
    #@+node:AGP.20230529212053.3:tab
    def tab(self,tab,end):
        for o in self.outputs:
            o.tab(tab,end)
    #@-node:AGP.20230529212053.3:tab
    #@+node:AGP.20230529212053.4:untab
    def untab(self,tab,end):
        for o in self.outputs:
            o.untab(tab,end)
    #@-node:AGP.20230529212053.4:untab
    #@+node:AGP.20230529212053.5:pushtab
    def pushtab(self):
        for o in self.outputs:
            o.pushtab()
    #@-node:AGP.20230529212053.5:pushtab
    #@+node:AGP.20230529212053.6:poptab
    def poptab(self):
        for o in self.outputs:
            o.poptab()
    #@-node:AGP.20230529212053.6:poptab
    #@-others
#@nonl
#@-node:AGP.20230529212053:OUTLIST
#@+node:AGP.20230214111049.420:ParserClass
class ParserClass:
    
    #@    @+others
    #@+node:AGP.20230524141224:class CPPRULES
    class CPPRULES:
        #@    @+others
        #@+node:AGP.20230524141224.1:__init__()
        def __init__(self,parser):
            self.OUTFUNC_RULES = [self.basic_rules,self.func_rule,self.class_rule,self.default_rule]
            self.RULES = self.OUTFUNC_RULES
            self.INFUNC_RULES = [self.basic_rules,self.default_rule]
            
            
            self.parser = parser
            self.CMT = parser.cc.CMT
            parser.TrueTabWrite = parser.TabWrite
        #@nonl
        #@-node:AGP.20230524141224.1:__init__()
        #@+node:AGP.20230604135730:choose_writer()
        def choose_writer(self,head):
            
            p = self.parser
            
            if p.FUNC_WRITER:
                return p.FUNC_WRITER,head
            
            w = None
            
            if head.endswith(";") or head.endswith(">"):#put in source
                w = p.SOURCE
                
                if head.endswith("<>"): #put in both
                    if p.BIFILE:
                        w = p.BOTH
                        head = head[:-2]
                else:        
                    head = head[:-1]
                
                
            elif head.endswith("<"):
                head = head[0:-1]
                w = p.HEADER
            
            if not w and p.CLASS_WRITER:
                w = p.CLASS_WRITER
            
            if not w and p.PARENT_WRITER:
                w = p.PARENT_WRITER
                #print head,"parent writer",w
            
            if not w:
                w = p.HEADER
                #print head,"header writer",w
                
            p.PARENT_WRITER = w   
                
            return w,head
        #@nonl
        #@-node:AGP.20230604135730:choose_writer()
        #@+node:AGP.20230524154206:split_rule()
        def split_rule(self,node,head):
            
            p = self.Parser
            cc = p.cc
            
            w,head = self.choose_writer(head)
            
            parts = head.replace("\\t","\t").replace("\\n","\n").split("$")
            
            plen = len(parts)
            if plen > 1:
                head = parts[0]
                body = parts[1]
                
                lines = ""
                if plen > 2:
                    lines = parts[2]
                
                body_prefix = ""
                body_sufix =  ""
                
                if "@" in body:
                    bparts = body.split("@")
                    if len(bparts) > 1:
                        body_prefix = bparts[0]
                        body_sufix = bparts[1]  #maybe join the rest of bparts
                    else:
                        body_sufix = bparts[0]
                        
                
                    
                w,head = self.choose_writer(head)
                
                tab = "\t"
                end = ""
                
                if plen > 2:
                    lines = parts[2]
                    
                    if "@" in lines:
                        lparts = lines.split("@")
                        if len(lparts) > 1:
                            tab = lparts[0]
                            end = lparts[1]  #maybe join the rest of bparts
                        else:
                            end = lparts[0]
            
                
                
                p.CURRENT_RULE = "split"        
            
                return p.WriteNode(p.CURRENT_NODE,head+body_prefix,w,tab,end,doc=head,close=body_sufix)
            
                
                return True
                
            return None
        #@nonl
        #@-node:AGP.20230524154206:split_rule()
        #@+node:AGP.20230524143101:default_rule()
        def default_rule(self,head):
                
            p = self.parser
            cc = p.cc
            
            w,head = self.choose_writer(head)
                
            p.CURRENT_RULE = "default"
            
            close = "\n"
            doc = head
            tab = "\t"
            end=None
                
            
            return p.WriteNode(p.CURRENT_NODE,self.CMT+head,w,tab,end,doc=doc,close=close)
        #@-node:AGP.20230524143101:default_rule()
        #@+node:AGP.20230524143101.1:basic_rules()
        def basic_rules(self,head):
            
            #AT rule
            if head.startswith("@"):
                return True
            
            
            #Comment rule
            #print "commemt",self.CMT
        	
            if head.startswith(self.CMT):
                p = self.parser
                
                p.CURRENT_RULE = "comment"
                w,head = self.choose_writer(head)
                return p.WriteNode(p.CURRENT_NODE,head,w,"\t"+self.CMT,None,doc=head,close="\n")
            
            
            
            
            
            if "@" in head:
                
                p = self.parser
                
                p.CURRENT_RULE = "split"
                w,head = self.choose_writer(head)
                
                close = "\n"
                doc = head
                tab = "\t"
                end=None
                
                head = head.replace("\\t","\t").replace("\\n","\n")
                parts = head.split("@")
                lp = len(parts)
                
                head = parts[0]
                tail = parts[-1]
                
                if lp > 2:
                    tab = parts[1]
                    
                if lp > 3:
                    end = parts[2]
                
                
                if tail != "":
                    close = tail+"\n"
                
                return p.WriteNode(p.CURRENT_NODE,head,w,tab,end,doc=doc,close=close)
                
                
                #print "split",head,"@",tab,"@",end,"@",close
            
            
            
            
            return None
        #@nonl
        #@-node:AGP.20230524143101.1:basic_rules()
        #@+node:AGP.20230524143136:func_rule()
        def func_rule(self,head):
            p = self.parser
            mo = SplitFunc(head)
            
            if not mo:
                return None
                
            p.CURRENT_RULE = "func"
            
            #p.OnFunc(mo)
            
            spec,ret,name,params,pure,dest,ctors = self.Groups = p.CURRENT_FUNC_MO = mo
            
            TO_SRC = ";" in dest[0] or ">" in dest[0]
            DO_DEC = not "!" in dest[0]# ! mean the function is not declared, only defined in src, main()!
            IS_PURE = pure[0] != ""     #function only declared
            
            node = p.CURRENT_NODE
            WCLASS = p.CLASS_WRITER
            
            #SPLIT = p.DECLARE_IN_HDR and p.DEFINE_IN_SRC
            SPLIT = p.BIFILE
            
            HEADER = p.HEADER
            SOURCE = p.SOURCE
            
            if WCLASS:  # func is a class member
        
                if SPLIT:
                    if WCLASS == HEADER:  #class defined in header
                        if TO_SRC: #declare in header and define in source
                            if not self.DeclareFunc(HEADER):
                                return False
        
                            return self.DefineFunc(SOURCE,node)
                        
                        else:   #define in header
                            return self.DefineFunc(HEADER,node,full=True)
                    
                    else: #class defined in source, so is the func
                        return self.DefineFunc(SOURCE,node,full=True)
                
                else:
                    return self.DefineFunc(WCLASS,node,full=True)
                    
            else:
                
                if IS_PURE:# 
                    Error("xcc :","Pure virtual function outside a class is illegal!")
                    p.cc.GoToNode(node)
                    return False
                
                if SPLIT:
                    if TO_SRC: #declare in header and define in source
                        if DO_DEC:
                            if not self.DeclareFunc(HEADER):
                                return False
        
                        return self.DefineFunc(SOURCE,node)
                        
                    else:   #define in header
                        return self.DefineFunc(HEADER,node,full=True)
                
                else:   #there is only one file
                    if p.DECLARE_IN_HDR:
                        return self.DefineFunc(HEADER,node,full=True)
                    else:
                        return self.DefineFunc(SOURCE,node,full=True)
            
        
         
        #@-node:AGP.20230524143136:func_rule()
        #@+node:AGP.20230524143435:DeclareFunc
        def DeclareFunc(self,wf):
            
            p = self.parser
            spec,ret,name,params,pure,dest,ctors = self.Groups
            
            if name[0] == "":
                return False
            
            specs = spec[0].split()
            if "__asm" in specs:
                specs.remove("__asm")
                spec = (string.join(specs),spec[1],spec[2])
            
            
            p.CURRENT_FUNC = proto = spec[0] +" "+ ret[0] +" "+ name[0] + params[0] + pure[0] +";"
            
            p.CURRENT_FUNC = proto = " ".join(proto.split())
            
            p.CURRENT_LOCATION = 0  #head
            #print "|",wf.tabstring,"|",proto
            #wf(p.TAB_STRING+proto.strip()+"\n")
            wf(proto)
                
            return True
        #@nonl
        #@-node:AGP.20230524143435:DeclareFunc
        #@+node:AGP.20230524143443:DefineFunc
        def DefineFunc(self,w,node,full=False,push=False):            
            p = self.parser
            spec,ret,name,params,pure,dest,ctors = self.Groups
            
            if name[0] == "":
                p.cc.ToolBar.SetError("No function name in : "+GetNodePath(p.CURRENT_NODE),p.CURRENT_NODE)
                return False
                    
            p.FUNC_WRITER = w
            proto = ""
            _as = "" #access specifier
            
            asm = False
            specs = spec[0].split()
            if "__asm" in specs:
                specs.remove("__asm")
                asm = True
            
            if full == True:
                    #specs = spec[0].split()
                    #if "__asm" in specs:
                        #specs.remove("__asm")
                        #spec = (string.join(specs),spec[1],spec[2])
                    if not name[0].startswith("~"):     #remove any specifier form destructor outside of class definition
                        proto = string.join(specs)+" "
                    
                    params = params[0].strip("()")
            else:
                for n in p.CLASS_LIST:#if full == True, declared and defined at once, so no access specifier
                    if n != None:
                        #_as = n+"::"+_as
                        _as += n+"::"
                        push = True   #push tab flag, indicate to reset tab beacause class func defined in src
                #if this is not a full definition, must remove default parameter assignement
                params = params[0].strip("()")
                paramslist = params.split(",")
                params = ""
                for pmt in paramslist:
                    pa = pmt.split("=")
                    if params != "":
                        params += ","+pa[0]
                    else:
                        params += pa[0]
                        
            proto += ret[0]+" "+_as+name[0]+"("+params+")"+ctors
            proto = proto.strip()
            
            #@    @+others
            #@+node:AGP.20230524143443.1:doc
            nt = StrToBool(p.cc.cGet("NEW_TOPIC","False",node=node))
            uh = StrToBool(p.cc.cGet("USE_HEAD","False",node=node))    
            
            dh = None
            if nt:
                dh = name[0]
            elif uh:
                prms = SplitParams(params)
                dh = "<font color=\"blue\">"+spec[0]+" "+ret[0]+"</font> "+_as+name[0]+"("
                if prms != None:
                    for t,n,a in prms:                
                        dh += "<font color=\"blue\">"+t+"</font> "+n
                        if a != None:
                            dh += " = <font color=\"green\">"+a+"</font> "
                        
                        dh += ", "
                    dh = dh[:-2]
                
                dh += ")"
                        
            #@-node:AGP.20230524143443.1:doc
            #@+node:AGP.20230524143443.2:core
            
            
            p.CURRENT_LOCATION = 0  #head
            
            nl="\n"
            
            
            #wf(p.TAB_STRING+p.cc.FUNC_HDR)
            #print w
            w(p.cc.FUNC_HDR)#,False)
            
            if False:#node.bodyString().strip()=="" and not node.firstChild(): #empty bracket
                #Error("xcc :",str(p.CURRENT_SRC_LINE))
                
                p.CURRENT_FUNC = proto
                p.CURRENT_LOCATION = 0  #head
                
                
                print w
                #wf(p.TAB_STRING+proto+p.cc.FUNC_OPN+p.cc.FUNC_END)
                w(proto+p.cc.FUNC_OPN)
                
                p.CURRENT_LOCATION = 2  #tail
                
                w.pushtab()
                w(p.cc.FUNC_END+"\n",False)#---------------------------
                w.poptab()
                
                p.CURRENT_FUNC = ""
                
                
                #Error("xcc :",p.TAB_STRING+proto+p.cc.FUNC_OPN+p.cc.FUNC_END)
                #Error("xcc :",str(p.CURRENT_SRC_LINE))
            
            if True:
                push and w.pushtab()
                #wf(p.TAB_STRING+proto+p.cc.FUNC_OPN)#+"\n")#---------------------
                #w(proto+p.cc.FUNC_OPN+"\n")#---------------------
            
                p.CURRENT_FUNC = proto
            
                p.RULES = self.INFUNC_RULES#---------------------------------
                
                
                
                if asm:
                    p.line_filter = p.asm_line_filter
                
                if not p.WriteNode(node,proto+p.cc.FUNC_OPN,w,"\t",None,doc=dh):
                    return False
                
                if asm:
                    p.line_filter = None
            
                
                
                p.RULES = self.OUTFUNC_RULES#---------------------------
            
            
                
                p.CURRENT_LOCATION = 2  #tail
                
                w(p.cc.FUNC_END+"\n",False)#---------------------------
                p.CURRENT_FUNC = ""
            
            
                push and w.poptab()
            #@nonl
            #@-node:AGP.20230524143443.2:core
            #@-others
            
            p.FUNC_WRITER = None
            
            return True
        #@nonl
        #@-node:AGP.20230524143443:DefineFunc
        #@+node:AGP.20230524143703:class_rule()
        def class_rule(self,head):
                
            p = self.parser
            cc = p.cc
            
            class_s = head.find("class ")
            if class_s > -1:
                head = head.split()
                head = string.join(head)
                class_s = head.rfind("class ")
                
                spec = (head[:class_s],0,class_s)
                name_s = class_s+6		
                dest_s = head.find(";",name_s)
                inst_s = head.find("!",name_s)
                base_s = head.find(":",name_s)
                
                #dest -----------------------
                if dest_s > -1:
                    name_e = dest_s
                    dest = (head[dest_s:dest_s+1],dest_s,dest_s+1)
                    inst_e = dest_s
                    base_e = dest_s
                else:
                    dest = ("",-1,-1)
                    name_e = inst_e = base_e = len(head)
                
                #inst --------------------------
                if inst_s > -1:
                    name_e = inst_s
                    base_e = inst_s
                    inst = (head[inst_s:inst_e],inst_s,inst_e)
                else:
                    inst = ("",-1,-1)
                
                #base ---------------------------------		
                if base_s > -1:
                    name_e = base_s
                    base = (head[base_s:base_e],base_s,base_e)
                else:
                    base = ("",-1,-1)
                
                name = (head[name_s:name_e],name_s,name_e)
                oldmo = p.CURRENT_CLASS_MO
                p.CURRENT_CLASS_MO = mo = (spec,name,base,inst,dest)
                #@        @+others
                #@+node:AGP.20230524144233:on match
                p.CURRENT_RULE = "class"
                    
                #spec,name,base,inst,dest = mo
                
                #determine where to write
                if len(p.CLASS_LIST) == 0:#redirect only for the root class
                	if dest[0] != "":#directed toward source
                		p.CLASS_WRITER = p.SOURCE
                		push = True
                	else:
                		p.CLASS_WRITER = p.HEADER
                		push = False
                else:
                	if p.CLASS_WRITER == p.HEADER:
                		push = False
                	else:
                		push = True
                
                cw = p.CLASS_WRITER
                
                cdec = ""
                
                if spec[0] != "":
                	cdec += spec[0]+" "
                
                if name[0] == "":
                	p.cc.ToolBar.SetError("No name in class definition :"+GetNodePath(p.CURRENT_NODE),p.CURRENT_NODE)
                	return False
                
                cdec += "class "+name[0]
                
                if base[0] != "":
                	cdec += base[0]
                	
                push and cw.pushtab()
                
                p.CLASS_LIST.append(name[0])#-------------------------
                
                head = cc.CLASS_HDR + cdec+cc.CLASS_OPN+"\n"
                
                if not p.WriteNode(p.CURRENT_NODE,head,cw,"\t",None,doc=name[0]):
                        return False
                
                #p.CURRENT_LOCATION = 2  #tail
                inst = inst[0][1:]
                ce = cc.CLASS_END.replace("_INST_",inst)
                cw(ce+"\n")
                
                if p.DO_PARSE:  #fix for locator and syncdisplay
                    p.CLASS_LIST.pop()#-----------------------------------
                
                """
                #---------------------------------
                p.StartDoc(name[0],node)#-------------------------------
                
                p.CLASS_LIST.append(name[0])#-------------------------
                
                p.CURRENT_LOCATION = 0  #head
                cw(cc.CLASS_HDR)            #p.TAB_STRING+
                cw(cdec+cc.CLASS_OPN+"\n")  #p.TAB_STRING+
                
                cw.tab()
                
                if p.WriteOthers(node,cw) == False:#------------------
                	return False
                
                cw.untab()
                
                inst = inst[0][1:]
                ce = cc.CLASS_END.replace("_INST_",inst)
                
                p.CURRENT_LOCATION = 2  #tail
                cw(ce+"\n")#p.TAB_STRING+
                
                p.CLASS_LIST.pop()#-----------------------------------
                
                p.EndDoc(node)#--------------------------------------
                #---------------------------------
                
                push and cw.poptab()
                """
                if len(p.CLASS_LIST) == 0:
                	p.CLASS_WRITER = None		
                
                return True
                #@nonl
                #@-node:AGP.20230524144233:on match
                #@-others
                p.CURRENT_CLASS_MO = oldmo
            
        #@nonl
        #@-node:AGP.20230524143703:class_rule()
        #@-others
    #@-node:AGP.20230524141224:class CPPRULES
    #@+node:AGP.20230214111049.421:Rules
    #@+node:AGP.20230214111049.422:LoadCppRules
    def LoadCppRules(self):
        
        parser = self
    
        self.OUTFUNC_RULES = [
            self.ATRULE(),
            self.COMMENTRULE(parser),	#placed fisrt to allow functions and class to be commented out
            self.FUNCRULE(parser),
            self.CLASSRULE(parser),	#must be after CppFuncRule or it will catch template funcs
            self.DEFAULTRULE(parser)	#must be the last rule cos it always proceed
        ]
        
        self.RULES = self.OUTFUNC_RULES
        
        self.INFUNC_RULES = [
            self.ATRULE(),
            self.FUNCCOMMENTRULE(parser),	#placed fisrt to allow functions and class to be commented out
            self.FUNCASMRULE(parser),
            self.FUNCDEFAULTRULE(parser)	#must be the last rule cos it always proceed
        ]
    #@nonl
    #@-node:AGP.20230214111049.422:LoadCppRules
    #@+node:AGP.20230214111049.423:ATRULE
    class ATRULE:
        #@    @+others
        #@+node:AGP.20230214111049.424:Match
        def Match(self,head):
            if head.startswith("@"):
                return True
            return None
        
        #@-node:AGP.20230214111049.424:Match
        #@+node:AGP.20230214111049.425:OnMatch
        def OnMatch(self,mo,node):
            pass
        #@-node:AGP.20230214111049.425:OnMatch
        #@-others
    #@nonl
    #@-node:AGP.20230214111049.423:ATRULE
    #@+node:AGP.20230214111049.426:COMMENTRULE
    class COMMENTRULE:
        #@    @+others
        #@+node:AGP.20230214111049.427:ctor
        def __init__ (self,Parser):    
            self.Parser = Parser
            self.CMT = Parser.cc.CMT
        #@nonl
        #@-node:AGP.20230214111049.427:ctor
        #@+node:AGP.20230214111049.428:Match
        def Match(self,head):
            if head.startswith(self.CMT):
                if head.endswith(";"):
                    return True
                return False
            return None
        #@nonl
        #@-node:AGP.20230214111049.428:Match
        #@+node:AGP.20230214111049.429:OnMatch
        def OnMatch(self,mo,node):
            
            p = self.Parser
            cc = p.cc    
            
            p.CURRENT_RULE = "comment"
            
            if mo:#put in source
                w = p.SOURCE
                #cc.cSet("DESTINATION","SRC",node)
                head = node.headString()[2:-1]
            else:        
                if p.CLASS_WRITER:
                    w = p.CLASS_WRITER
                else:
                    w = p.HEADER
                #cc.cSet("DESTINATION","HDR",node)
                head = node.headString()[2:]
            
            
            
            #---------------------------------    
            p.StartDoc(head,node)#------------------------doc
            
            p.CURRENT_LOCATION = 0  #head
            
            w.tab(cc.CMT)
            w(head+"\n")    
            
            if p.WriteOthers(node,w) == False:#---------------
                return False
            
            p.CURRENT_LOCATION = 2  #tail
            w.untab(cc.CMT)
            w("\n")
        
            p.EndDoc(node)#-------------------------------doc
            #----------------------------------
            
            return True
        
        
        #@-node:AGP.20230214111049.429:OnMatch
        #@-others
    #@nonl
    #@-node:AGP.20230214111049.426:COMMENTRULE
    #@+node:AGP.20230214111049.430:FUNCRULE
    class FUNCRULE:
        #@    @+others
        #@+node:AGP.20230214111049.431:ctor
        def __init__ (self,Parser):    
            self.Parser = Parser
            Parser.TrueTabWrite = Parser.TabWrite
        #@nonl
        #@-node:AGP.20230214111049.431:ctor
        #@+node:AGP.20230214111049.432:Match
        def Match(self,head):	
           return SplitFunc(head)
            
        #@-node:AGP.20230214111049.432:Match
        #@+node:AGP.20230214111049.433:_OnMatch{}
        def _OnMatch(self,mo,node):
            
            p = self.Parser
            p.CURRENT_RULE = "func"
            
            #p.OnFunc(mo)
            
            spec,ret,name,params,pure,dest,ctors = self.Groups = p.CURRENT_FUNC_MO = mo
            
            if pure[0] == "":#define the func, possibly splitted
                
                if ";" in dest[0]:#put in source
                    
                    if "!" in dest[0]:# ! mean the function is not declared, only defined in src, main()!
                        
                        #no declaration in header
                        return self.DefineFunc(p.SOURCE,node,full=True)
                        
                    else:
                        
                        if self.DeclareFunc(p.HEADER) == False:
                            return False
                        
                        return self.DefineFunc(p.SOURCE,node)
                    
                
                else:
                    
                    if p.CLASS_WRITER:
                        
                        if p.CLASS_WRITER == p.HEADER:#func is split
                            if ";" in dest[0]:#put in source
                                
                                return self.DeclareFunc(p.CLASS_WRITER) and self.DefineFunc(p.SOURCE,node,push=True)
                                
                                #if self.DeclareFunc(p.CLASS_WRITER) == False:
                                #    return False
                                #return self.DefineFunc(p.SOURCE,node,push=True)
                            else:
                                return self.DefineFunc(p.HEADER,node,full=True)            
                                                
                        else:#func is not splitted, written with the class
                            return self.DefineFunc(p.CLASS_WRITER,node)
                
                    else:
                        
                        return self.DefineFunc(p.HEADER,node,full=True)
            
            else:#pure function, only declare the func, real destination depend upon DEST group and EXT
                if p.CLASS_WRITER:
                    p.CURRENT_FUNC_DST = "HDR"
                    #p.cc.cSet("DESTINATION","HDR",node)
                    return self.DeclareFunc(p.CLASS_WRITER)
                    
                else:
                    Error("xcc :","Pure virtual function outside a class is illegal!")
                    #cc.GoToNode(node)
                    return False
        #@nonl
        #@-node:AGP.20230214111049.433:_OnMatch{}
        #@+node:AGP.20230322091505:OnMatch{}
        def OnMatch(self,mo,node):
            
            p = self.Parser
            p.CURRENT_RULE = "func"
            
            #p.OnFunc(mo)
            
            spec,ret,name,params,pure,dest,ctors = self.Groups = p.CURRENT_FUNC_MO = mo
            
            TO_SRC = ";" in dest[0]
            DO_DEC = not "!" in dest[0]# ! mean the function is not declared, only defined in src, main()!
            IS_PURE = pure[0] != ""     #function only declared
            
            WDEC = p.HEADER
            WDEF = p.SOURCE
            
            WCLASS = p.CLASS_WRITER
            
            if WCLASS:
                WDEC = WCLASS
            
            elif IS_PURE:# 
                Error("xcc :","Pure virtual function outside a class is illegal!")
                #cc.GoToNode(node)
                return False
            
            SINGLE = WDEC == WDEF
            
            SPLIT = WDEC != WDEF    #class defined in header-> split
        
            
            if SPLIT:
                if DO_DEC and not self.DeclareFunc(WDEC):
                    return False
                    
                
                return not IS_PURE and self.DefineFunc(p.SOURCE,node)
            else:
                if WCLASS:
                    return self.DefineFunc(WCLASS,node,full=True)
                else:        
                    if TO_SRC:
                        return self.DefineFunc(p.SOURCE,node,full=True)
                    else:
                        return self.DefineFunc(p.HEADER,node,full=True)
            
         
        #@nonl
        #@-node:AGP.20230322091505:OnMatch{}
        #@+node:AGP.20230214111049.434:DeclareFunc
        def DeclareFunc(self,wf):
            
            p = self.Parser
            spec,ret,name,params,pure,dest,ctors = self.Groups
            
            if name[0] == "":
                return False
            
            specs = spec[0].split()
            if "__asm" in specs:
                specs.remove("__asm")
                spec = (string.join(specs),spec[1],spec[2])
            
            
            p.CURRENT_FUNC = proto = spec[0] +" "+ ret[0] +" "+ name[0] + params[0] + pure[0] +";"
            
            p.CURRENT_FUNC = proto = " ".join(proto.split())
            
            p.CURRENT_LOCATION = 0  #head
            #print "|",wf.tabstring,"|",proto
            #wf(p.TAB_STRING+proto.strip()+"\n")
            wf(proto)
                
            return True
        #@nonl
        #@-node:AGP.20230214111049.434:DeclareFunc
        #@+node:AGP.20230214111049.435:DefineFunc
        def DefineFunc(self,wf,node,full=False,push=False):            
            p = self.Parser
            spec,ret,name,params,pure,dest,ctors = self.Groups
            
            if name[0] == "":
                p.cc.ToolBar.SetError("No function name in : "+GetNodePath(p.CURRENT_NODE),p.CURRENT_NODE)
                return False
                    
            p.FUNC_WRITER = wf
            proto = ""
            _as = "" #access specifier
            
            asm = False
            specs = spec[0].split()
            if "__asm" in specs:
                specs.remove("__asm")
                asm = True
            
            if full == True:
                    #specs = spec[0].split()
                    #if "__asm" in specs:
                        #specs.remove("__asm")
                        #spec = (string.join(specs),spec[1],spec[2])
                    if not name[0].startswith("~"):     #remove any specifier form destructor outside of class definition
                        proto = string.join(specs)+" "
                    
                    params = params[0].strip("()")
            else:
                for n in p.CLASS_LIST:#if full == True, declared and defined at once, so no access specifier
                    if n != None:
                        #_as = n+"::"+_as
                        _as += n+"::"
                        push = True   #push tab flag, indicate to reset tab beacause class func defined in src
                #if this is not a full definition, must remove default parameter assignement
                params = params[0].strip("()")
                paramslist = params.split(",")
                params = ""
                for pmt in paramslist:
                    pa = pmt.split("=")
                    if params != "":
                        params += ","+pa[0]
                    else:
                        params += pa[0]
                        
            proto += ret[0]+" "+_as+name[0]+"("+params+")"+ctors
            proto = proto.strip()
            
            #@    @+others
            #@+node:AGP.20230214111049.436:doc
            
            
            nt = StrToBool(p.cc.cGet("NEW_TOPIC","False",node=node))
            uh = StrToBool(p.cc.cGet("USE_HEAD","False",node=node))    
            if nt:
                p.StartDoc(name[0],node)
            elif uh:
                prms = SplitParams(params)
                dh = "<font color=\"blue\">"+spec[0]+" "+ret[0]+"</font> "+_as+name[0]+"("
                if prms != None:
                    for t,n,a in prms:                
                        dh += "<font color=\"blue\">"+t+"</font> "+n
                        if a != None:
                            dh += " = <font color=\"green\">"+a+"</font> "
                        
                        dh += ", "
                    dh = dh[:-2]
                
                dh += ")"
                        
                p.StartDoc(dh,node)
            #---------------------
                        
            #@+others
            #@+node:AGP.20230214111049.437:core
            push and wf.pushtab()
            
            p.CURRENT_LOCATION = 0  #head
            
            nl="\n"
            
            
            #wf(p.TAB_STRING+p.cc.FUNC_HDR)
            wf(p.cc.FUNC_HDR)
            
            if node.bodyString().strip()=="" and not node.firstChild(): #empty bracket
                #Error("xcc :",str(p.CURRENT_SRC_LINE))
                
                #wf(p.TAB_STRING+proto+p.cc.FUNC_OPN+p.cc.FUNC_END)
                wf(proto+p.cc.FUNC_OPN+p.cc.FUNC_END)
                
                
                #Error("xcc :",p.TAB_STRING+proto+p.cc.FUNC_OPN+p.cc.FUNC_END)
                #Error("xcc :",str(p.CURRENT_SRC_LINE))
            
            else:
            
                #wf(p.TAB_STRING+proto+p.cc.FUNC_OPN)#+"\n")#---------------------
                wf(proto+p.cc.FUNC_OPN)#+"\n")#---------------------
            
                p.CURRENT_FUNC = proto
            
                p.RULES = p.INFUNC_RULES#---------------------------------
                wf.tab()
                
                if asm:
                    p.line_filter = p.asm_line_filter
                
                
                #if asm:
                #    if p.WriteOthers_asm(node,wf) == False:
                #        return False
                #else:
                if p.WriteOthers(node,wf) == False:
                    return False
                        
                if asm:
                    p.line_filter = None
            
                wf.untab()
                p.RULES = p.OUTFUNC_RULES#---------------------------
            
            
                
                p.CURRENT_LOCATION = 2  #tail
                #wf(p.TAB_STRING+p.cc.FUNC_END)#+"\n")#---------------------------
                wf(p.cc.FUNC_END)#+"\n")#---------------------------
                p.CURRENT_FUNC = ""
                
            push and wf.poptab()
            #@nonl
            #@-node:AGP.20230214111049.437:core
            #@-others
                    
            #---------------------
            p.EndDoc(node)
            #@nonl
            #@-node:AGP.20230214111049.436:doc
            #@-others
                        
            return True
        #@nonl
        #@-node:AGP.20230214111049.435:DefineFunc
        #@-others
    #@nonl
    #@-node:AGP.20230214111049.430:FUNCRULE
    #@+node:AGP.20230214111049.438:CLASSRULE
    class CLASSRULE:
        #@    @+others
        #@+node:AGP.20230214111049.439:ctor
        def __init__ (self,Parser):    
            self.Parser = Parser
        #@nonl
        #@-node:AGP.20230214111049.439:ctor
        #@+node:AGP.20230214111049.440:Match
        #spec class name base inst dest
        def Match(self,head):
            #return self.Matcher.search(head)
            class_s = head.find("class ")
            if class_s > -1:
                head = head.split()
                head = string.join(head)
                class_s = head.rfind("class ")
                
                spec = (head[:class_s],0,class_s)
                name_s = class_s+6		
                dest_s = head.find(";",name_s)
                inst_s = head.find("!",name_s)
                base_s = head.find(":",name_s)
                
                #dest -----------------------
                if dest_s > -1:
                    name_e = dest_s
                    dest = (head[dest_s:dest_s+1],dest_s,dest_s+1)
                    inst_e = dest_s
                    base_e = dest_s
                else:
                    dest = ("",-1,-1)
                    name_e = inst_e = base_e = len(head)
                
                #inst --------------------------
                if inst_s > -1:
                    name_e = inst_s
                    base_e = inst_s
                    inst = (head[inst_s:inst_e],inst_s,inst_e)
                else:
                    inst = ("",-1,-1)
                
                #base ---------------------------------		
                if base_s > -1:
                    name_e = base_s
                    base = (head[base_s:base_e],base_s,base_e)
                else:
                    base = ("",-1,-1)
                
                name = (head[name_s:name_e],name_s,name_e)
                        
                return (spec,name,base,inst,dest)
                    
            return None
        #@nonl
        #@-node:AGP.20230214111049.440:Match
        #@+node:AGP.20230214111049.441:OnMatch
        def OnMatch(self,mo,node):
            # global LOCATE_CHILD
            
            p = self.Parser
            cc = p.cc
            
            p.CURRENT_RULE = "class"
            
            spec,name,base,inst,dest = mo
            
            #determine where to write
            if len(p.CLASS_LIST) == 0:#redirect only for the root class
                if dest[0] != "":#directed toward source
                    p.CLASS_WRITER = p.SOURCE
                    push = True
                else:
                    p.CLASS_WRITER = p.HEADER
                    push = False
            else:
                if p.CLASS_WRITER == p.HEADER:
                    push = False
                else:
                    push = True
            
            cw = p.CLASS_WRITER
            
            cdec = ""
            
            if spec[0] != "":
                cdec += spec[0]+" "
            
            if name[0] == "":
                p.cc.ToolBar.SetError("No name in class definition :"+GetNodePath(p.CURRENT_NODE),p.CURRENT_NODE)
                return False
            
            cdec += "class "+name[0]
            
            if base[0] != "":
                cdec += base[0]
                
            push and cw.pushtab()
            
            #---------------------------------
            p.StartDoc(name[0],node)#-------------------------------
        
            p.CLASS_LIST.append(name[0])#-------------------------
            
            p.CURRENT_LOCATION = 0  #head
            cw(cc.CLASS_HDR)            #p.TAB_STRING+
            cw(cdec+cc.CLASS_OPN+"\n")  #p.TAB_STRING+
            
            cw.tab()
            
            if p.WriteOthers(node,cw) == False:#------------------
                return False
            
            cw.untab()
            
            inst = inst[0][1:]
            ce = cc.CLASS_END.replace("_INST_",inst)
            
            p.CURRENT_LOCATION = 2  #tail
            cw(ce+"\n")#p.TAB_STRING+
            
            p.CLASS_LIST.pop()#-----------------------------------
        
            p.EndDoc(node)#--------------------------------------
            #---------------------------------
            
            push and cw.poptab()
        
            if len(p.CLASS_LIST) == 0:
                p.CLASS_WRITER = None		
            
            return True
        #@-node:AGP.20230214111049.441:OnMatch
        #@-others
    #@nonl
    #@-node:AGP.20230214111049.438:CLASSRULE
    #@+node:AGP.20230214111049.442:DEFAULTRULE
    class DEFAULTRULE:
        #@    @+others
        #@+node:AGP.20230214111049.443:__init__
        def __init__(self,Parser):
            
            self.Parser = Parser
            self.Matcher = re.compile("(?P<HEAD>[^;]*)(?P<DEST>;$)*")
        #@nonl
        #@-node:AGP.20230214111049.443:__init__
        #@+node:AGP.20230214111049.444:Match
        def Match(self,head):
            return head.endswith(";")
        #@nonl
        #@-node:AGP.20230214111049.444:Match
        #@+node:AGP.20230214111049.445:OnMatch
        def OnMatch(self,mo,node):
                
            p = self.Parser
            cc = p.cc
            
            if mo:#put in source
                w = p.SOURCE
                head = node.headString()[:-1]        
            else:        
                if p.CLASS_WRITER:
                    w = p.CLASS_WRITER
                else:
                    w = p.HEADER
                head = node.headString()          
                
            p.CURRENT_RULE = "default"        
            
            #---------------------------    
            p.StartDoc(head,node)#----------------------------------
            
            p.CURRENT_LOCATION = 0  #head
            w(cc.CMT+head)
            
            #p.Tab() - for python compatibility
            if p.WriteOthers(node,w) == False:#-----------------------
                return False    
            #p.UnTab()- for python compatibility
            
            p.CURRENT_LOCATION = 2  #tail	
            w("\n")
            
            p.EndDoc(node)#---------------------------------------------
            #----------------------------
            return True
            
            
        #@nonl
        #@-node:AGP.20230214111049.445:OnMatch
        #@-others
    #@nonl
    #@-node:AGP.20230214111049.442:DEFAULTRULE
    #@+node:AGP.20230214111049.446:FUNCCOMMENTRULE
    class FUNCCOMMENTRULE:
        #@    @+others
        #@+node:AGP.20230214111049.447:__init__
        def __init__(self,Parser):
            
            self.Parser = Parser	
            self.Matcher = re.compile("^//(?P<HEAD>.*)")
            
        #@nonl
        #@-node:AGP.20230214111049.447:__init__
        #@+node:AGP.20230214111049.448:Match
        def Match(self,head):
            return self.Matcher.search(head)
        #@-node:AGP.20230214111049.448:Match
        #@+node:AGP.20230214111049.449:OnMatch
        def OnMatch(self,mo,node):
            
            p = self.Parser
            p.CURRENT_RULE = "funccomment"
            
            w = p.FUNC_WRITER
            groups = mo.groupdict()
            
            head = groups["HEAD"]
            if head == None:
                head = ""
                
            p.CURRENT_LOCATION = 0  #head
            w.tab(p.cc.CMT)
            w(head+"\n")
            
            if p.WriteOthers(node,w) == False:
                return False
            
            p.CURRENT_LOCATION = 2  #tail
            w.untab(p.cc.CMT)
            w("\n")
        
            return True
        #@-node:AGP.20230214111049.449:OnMatch
        #@-others
    #@nonl
    #@-node:AGP.20230214111049.446:FUNCCOMMENTRULE
    #@+node:AGP.20230214111049.450:FUNCASMRULE
    class FUNCASMRULE:
        #@    @+others
        #@+node:AGP.20230214111049.451:__init__
        def __init__(self,Parser):
            
            self.Parser = Parser	
            self.Matcher = re.compile("^__asm(?P<HEAD>.*)")
            
        #@nonl
        #@-node:AGP.20230214111049.451:__init__
        #@+node:AGP.20230214111049.452:Match
        def Match(self,head):
            return self.Matcher.search(head)
        #@-node:AGP.20230214111049.452:Match
        #@+node:AGP.20230214111049.453:OnMatch
        def OnMatch(self,mo,node):
            
            p = self.Parser
            p.CURRENT_RULE = "funcasm"
            
            w = p.FUNC_WRITER
            groups = mo.groupdict()
            
            head = groups["HEAD"]
            if head == None:
                head = ""
                
            p.CURRENT_LOCATION = 0  #head
            w.Tab()
            w("//__asm"+head+"\n")
            
            
            p.line_filter = p.asm_line_filter
            
            if p.WriteOthers(node,wf) == False:
                return False
                    
            p.line_filter = None
            
            
            p.CURRENT_LOCATION = 2  #tail
            w.UnTab()
            w("\n")
        
            return True
        #@-node:AGP.20230214111049.453:OnMatch
        #@-others
    #@nonl
    #@-node:AGP.20230214111049.450:FUNCASMRULE
    #@+node:AGP.20230214111049.454:FUNCDEFAULTRULE
    class FUNCDEFAULTRULE:
        #@    @+others
        #@+node:AGP.20230214111049.455:__init__
        def __init__(self,Parser):
            
            self.Parser = Parser
            self.Matcher = re.compile("(?P<HEAD>.*)")
        #@nonl
        #@-node:AGP.20230214111049.455:__init__
        #@+node:AGP.20230214111049.456:Match
        def Match(self,head):
        
            return self.Matcher.search(head)
        #@-node:AGP.20230214111049.456:Match
        #@+node:AGP.20230214111049.457:OnMatch
        def OnMatch(self,mo,node):
            
            p = self.Parser
            p.CURRENT_RULE = "funcdefault"
            
            w = p.FUNC_WRITER
            groups = mo.groupdict()
        
            head = groups["HEAD"]
            if head == None:
                head = ""
            
            #---------------------------    
            p.StartDoc(head,node)#----------------------------------
            
            p.CURRENT_LOCATION = 0  #head
            w(p.cc.CMT+head+"\n")
            w.tab()
            
            if p.WriteOthers(node,w) == False:
                return False
            
            w.untab()	
            p.CURRENT_LOCATION = 2  #tail
            w("\n")    
            p.EndDoc(node)#---------------------------------------------
            #----------------------------
            return True
        #@-node:AGP.20230214111049.457:OnMatch
        #@-others
    #@nonl
    #@-node:AGP.20230214111049.454:FUNCDEFAULTRULE
    #@-node:AGP.20230214111049.421:Rules
    #@+node:AGP.20230214111049.458:__init__
    def __init__(self,cc):
        self.cc = cc
        
        self.__name__ = "ParserClass"
        self.DO_PARSE = True	
        self.NOW_PARSING = False
        self.PARSE_TIME = 0.0
        
        self.RULES = []	
        self.OnStart = None
        self.OnEnd = None    
        
        self.DEC_PROC_LIST = []
        self.DEF_PROC_LIST = []
        self.DOC_PROC_LIST = []
        #self.OPN_PROC_LIST = []
        
        self.BODY_LINE_STACK = []
        
        self.CURRENT_SRC_LINE = 0
        self.CURRENT_HDR_LINE = 0
        self.CURRENT_DOC_LINE = 0
        
        self.CURRENT_BODY_LINE = 0
        self.CURRENT_VNODE = None
        self.CURRENT_NODE = None
        
        self.CURRENT_LOCATION = 0   # 0 = head, 1 = body, 2 = tail
        self.PYWNODE = None
        
        self.CURRENT_RULE = ""
        self.CURRENT_MO = None
        self.CURRENT_FUNC = ""
        self.CURRENT_FUNC_DST = ""
        self.CURRENT_CLASS_MO = None
        
        self.DECLARE_IN_HDR = True
        self.DEFINE_IN_SRC = True	
        
        self.CLASS_LIST = []
        self.CLASS_WRITER = None
        self.FUNC_WRITER = None
        
        self.PARENT_WRITER = None
        
        self.TAB_STRING = ""
        self.TAB_LIST = []
        
        
        
        self.DOC_NAMES = []
        
        self.OnParseNode = None
    
        
        self.line_filter = None
        
        
        
        #@    @+others
        #@+node:AGP.20230604195736:output files
        h = self.HEADER = OUTPUT(self)
        s = self.SOURCE = OUTPUT(self)
        self.BOTH = OUTLIST([h,s])
        
        self.cpprules = self.CPPRULES(self)
        
        self.BIFILE = True
          
        if cc.EXT == cc.SRC_EXT:
            self.DECLARE_IN_HDR = False
            self.BIFILE = False
            
            
        if cc.EXT == cc.HDR_EXT:
            self.DEFINE_IN_SRC = False
            self.BIFILE = False
        #@-node:AGP.20230604195736:output files
        #@-others
    #@-node:AGP.20230214111049.458:__init__
    #@+node:AGP.20230315110656:_Declare
    def _Declare(self,text):
        lines = text.splitlines(True)      
        
        #if len(lines)==1 and lines[0]=="":
        #    return
        
        if self.CURRENT_LOCATION == 1:
            for l in lines:
                self.CURRENT_BODY_LINE += 1	
                self.CURRENT_HDR_LINE += 1
                self.WriteHeader(l.rstrip("\n")+"\n")
            
        else:
            self.CURRENT_BODY_LINE = 0
            for l in lines:    
                self.CURRENT_HDR_LINE += 1
                self.WriteHeader(l.rstrip("\n")+"\n")
    #@-node:AGP.20230315110656:_Declare
    #@+node:AGP.20230521193408:Declare
    def Declare(self,text):
        self.HEADER(text)
    
    #@-node:AGP.20230521193408:Declare
    #@+node:AGP.20230315105014:_Define
    def _Define(self,text):
        lines = text.splitlines(True)      
        
        #if len(lines)==1 and lines[0]=="":
        #    return
        
        if self.CURRENT_LOCATION == 1:
            for l in lines:
                self.CURRENT_BODY_LINE += 1	
                self.CURRENT_SRC_LINE += 1
                self.WriteSource(l.rstrip("\n")+"\n")
            
        else:
            self.CURRENT_BODY_LINE = 0
            for l in lines:    
                self.CURRENT_SRC_LINE += 1
                self.WriteSource(l.rstrip("\n")+"\n")
    #@-node:AGP.20230315105014:_Define
    #@+node:AGP.20230521193302:Define
    def Define(self,text):
        self.SOURCE(text)
    #@-node:AGP.20230521193302:Define
    #@+node:AGP.20230214111049.461:WriteOthers
    def WriteOthers(self,node,w,tab=None):
        
        
        self.DocumNode(node)
        
        self.CURRENT_LOCATION = 1   #body
        
        cbt = node.bodyString()
        
        self.others = others = None
        
        if len(cbt) > 0:
        
            cbt = self.CURRENT_BODY_TEXT = node.bodyString().split("@others",1)
        
            others = len(cbt) > 1    
        
            t = cbt[0].split('\n')
        
            if others > 1 and len(t) > 0 and not t[-1].endswith(""):    #there is a tabing for @others
                tab = t.pop(-1)
            
            w(t)    # write pre-others text
            
            #print "preothers",( self.CURRENT_BODY_LINE, self.HEADER.CURRENT_LINE , self.SOURCE.CURRENT_LINE)
            
        if tab:
            w.tab(tab)
            
        self.PushBodyLine()
                
        if self.ParseNode(node) == False:
            return False
        
    
        self.PopBodyLine()
        
        
        if others:
            self.others = ( self.CURRENT_BODY_LINE, self.HEADER.CURRENT_LINE , self.SOURCE.CURRENT_LINE)
        
        
        
        if tab:
            w.untab()
        
        self.CURRENT_LOCATION = 1   #body
                
        if others:
            #self.others = others
            w( cbt[-1] )    #write the post-others text
            #self.others.pop(-1)
            
            
            
        
        
        return True
        
        """if o != -1:
            lb = b[:o]
            pnl = lb.rfind("\n")
            if pnl > -1:
                lb = lb[:pnl]
            
            tb = b[o+7:]
            pnl = tb.find("\n")		
            if pnl > -1:
                tb = tb[pnl+1:]        
            
            if lb != "":
                self.TabWrite(lb+"\n",w)
            
            self.PushBodyLine()
            if self.ParseNode(node) == False:
                return False
            self.PopBodyLine()
            self.CURRENT_LOCATION = 1   #body
            self.TabWrite(b[o+7:]+"\n",w)
            #self.TabWrite(b[o+7:],w)
        else:        
            #self.TabWrite(b+"\n",w)
            self.TabWrite(b,w)
            if self.ParseNode(node) == False:
                return False
        
        return True"""
        
    #@-node:AGP.20230214111049.461:WriteOthers
    #@+node:AGP.20230529114310:WriteNode
    def WriteNode(self,node,head,w,tab=None,end=None,doc=None,close=None):
        
        if doc:
            self.StartDoc(doc,node)
    		
        self.CURRENT_LOCATION = 0  #head
    	
        #w(head+"\n")
        w(head)
        
        if tab or end:
            w.tab(tab,end)
        
    	
        
        if self.WriteOthers(node,w) == False:#---------------
            return False
    		
        self.CURRENT_LOCATION = 2  #tail
        
        if tab or end:
            w.untab(tab,end)
        
        #w("\n")
        
        if close:
            w(close,False)
    
        if doc:
            self.EndDoc(node)
            
        return True
        
    #@-node:AGP.20230529114310:WriteNode
    #@+node:AGP.20230529211158:WriteBoth
    def WriteBoth(s,strip=True):
        self.HEADER(s,strip)
        self.SOURCE(s,strip)
    #@-node:AGP.20230529211158:WriteBoth
    #@+node:AGP.20230214111049.463:PushBodyLine
    def PushBodyLine(self):
        self.BODY_LINE_STACK.insert(0,self.CURRENT_BODY_LINE)
    #@-node:AGP.20230214111049.463:PushBodyLine
    #@+node:AGP.20230214111049.464:PopBodyLine
    def PopBodyLine(self):
        self.CURRENT_BODY_LINE = self.BODY_LINE_STACK.pop(0)
        
        
    #@-node:AGP.20230214111049.464:PopBodyLine
    #@+node:AGP.20230214111049.465:Parse
    def Parse(self):
        
        cc = self.cc
        #----------------------------------------------
        #self.LoadCppRules()
        
        
        #-----------------------------------------------------
        self.CURRENT_VNODE = cc.SELECTED_NODE.v
        self.CURRENT_NODE = cc.SELECTED_NODE
        
        #if not (self.OnStart and self.OnStart()):
        #    return False
            
        #-----------------------------------------------------
        if self.NOW_PARSING == True:
            Error("xcc: ","Already parsing!")
            return False
        
        self.NOW_PARSING = True    
        #------------------------------------------------------
        if not self.DECLARE_IN_HDR:
            self.PARENT_WRITER = self.SOURCE
        else:
            self.PARENT_WRITER = self.HEADER
        
        
        
        
        self.PushDoc(cc.NAME)
        
        #time.clock()
        start = time.clock()
        
        if self.BIFILE:
            if cc.OPTS.get("Auto include header") == "True":
                self.Define("#include \""+cc.NAME+".h\"\n")
        
        self.DocumNode(cc.SELECTED_NODE)
        #------------------------------------------------------		
        res = self.ParseNode(cc.SELECTED_NODE,reset=True)	
        #------------------------------------------------------
        if res:
            self.PopDoc()
        
        self.PARSE_TIME = time.clock()-start
        
        #self.OnEnd and self.OnEnd()	
        
        #print self.PARSE_TIME
        
        return res
    
    #@-node:AGP.20230214111049.465:Parse
    #@+node:AGP.20230214111049.466:ParseNode
    def ParseNode(self,node,reset=False):
        cc = self.cc
        
        if self.DO_PARSE == False:
            return False
        
        pw = self.PARENT_WRITER
        
        for cn in node.children_iter():        
            self.PARENT_WRITER = pw    #
            
            #self.OnParseNode(cn)		
            self.CURRENT_VNODE = cn.v
            self.CURRENT_NODE = cn.copy()
            ch = cn.headString()
            
            if self.OnParseNode != None:
                self.OnParseNode(cn)
            
            tcr = self.CURRENT_RULE
            tcmo = self.CURRENT_MO
            
            for r in self.cpprules.RULES:
                result = r(ch)
                if result == None:
                    continue
                    
                if result and self.DO_PARSE:
                    break
                
                return False        
            
            
            """
            for r in self.RULES:
                result = r.Match(ch)
                if result != None:
                    self.CURRENT_MO = result
                    if r.OnMatch(result,cn) == False or self.DO_PARSE == False:
                        return False
                    #else:
                    #    cc.cSet("RULE",self.CURRENT_RULE,cn)
                    break
            """
            self.CURRENT_RULE = tcr
            self.CURRENT_MO = tcmo
            
        self.CURRENT_NODE = node
        
        if self.OnParseNode != None and node != cc.SELECTED_NODE:
            self.OnParseNode(node,True)
            
            
        
        return True
    #@-node:AGP.20230214111049.466:ParseNode
    #@+node:AGP.20230323202248:asm_line_filter()
    def asm_line_filter(self,line):    
        line = line.strip()
        
        if line.find("/") > -1:
            chunks = line.split("//",1)
            if len(chunks) > 1:
                asm_code = chunks[0]
                if asm_code.strip() != "":
                    line = "asm(\""+asm_code+"\\n\");\t//"+chunks[1]
                
            chunks = line.split("/*",1)
            if len(chunks) > 1:
                asm_code = chunks[0]
                if asm_code.strip() != "":
                    line = "asm(\""+asm_code+"\\n\");\t/*"+chunks[1]
        
        else:
            if line != "":
                line = "asm(\""+line+"\\n\");"
        
        return line
            
    #@-node:AGP.20230323202248:asm_line_filter()
    #@+node:AGP.20230214111049.469:Tabing
    #@+node:AGP.20230214111049.470:Tab
    def Tab(self,sym="\t"):
        self.TAB_STRING += sym
    #@nonl
    #@-node:AGP.20230214111049.470:Tab
    #@+node:AGP.20230214111049.471:UnTab
    def UnTab(self,sym="\t"):
        self.TAB_STRING = self.TAB_STRING[:-len(sym)] 
    #@-node:AGP.20230214111049.471:UnTab
    #@+node:AGP.20230214111049.472:PushTab
    def PushTab(self):
        self.TAB_LIST.append(self.TAB_STRING)
        self.TAB_STRING = ""
    #@nonl
    #@-node:AGP.20230214111049.472:PushTab
    #@+node:AGP.20230214111049.473:PopTab
    def PopTab(self):
        self.TAB_STRING = self.TAB_LIST.pop(-1)
    #@nonl
    #@-node:AGP.20230214111049.473:PopTab
    #@+node:AGP.20230214111049.474:TabWrite
    def TabWrite(self,text,outfunc):
        if type(text) == "str":
            text = text.splitlines(True)
        
        for l in text:
            outfunc(self.TAB_STRING+l)
    #@-node:AGP.20230214111049.474:TabWrite
    #@+node:AGP.20230214111049.475:TabWrite_asm
    def TabWrite_asm(self,text,outfunc):
        if type(text) == "str":
            text = text.splitlines(True)
        
    
        for l in text:
            asm_code = l
            
            if l.find("/") > -1:
                chunks = l.split("//",1)
                asm_code = chunks[0].strip()
            
            if asm_code != "":
                asm_code = "asm(\""+asm_code+"\\n\");\t"
                chunks[0] = asm_code
                l = string.join(chunks,"//")
            
                chunks = l.split("/*",1)
                asm_code = chunks[0].strip()
                if asm_code != "":
                    asm_code = "asm(\""+asm_code+"\\n\");\t"
                chunks[0] = asm_code
                l = string.join(chunks,"/*")
            
            
            outfunc(self.TAB_STRING + l)
    #@-node:AGP.20230214111049.475:TabWrite_asm
    #@-node:AGP.20230214111049.469:Tabing
    #@+node:AGP.20230214111049.476:Documentation
    #@+node:AGP.20230214111049.477:Docum
    def Docum(self,text):
        pass
    #@-node:AGP.20230214111049.477:Docum
    #@+node:AGP.20230315124909:DocumNode
    def DocumNode(self,node):
        pass
    #@-node:AGP.20230315124909:DocumNode
    #@+node:AGP.20230214111049.478:PushDoc
    def PushDoc(self,name,intro=True):
        pass
    #@-node:AGP.20230214111049.478:PushDoc
    #@+node:AGP.20230214111049.479:PopDoc
    def PopDoc(self):
        pass
    #@-node:AGP.20230214111049.479:PopDoc
    #@+node:AGP.20230214111049.480:DocName
    def DocName(self,sym="_",s=0):
        pass
    #@-node:AGP.20230214111049.480:DocName
    #@+node:AGP.20230214111049.481:StartDoc
    def StartDoc(self,name,node):
        pass
    #@-node:AGP.20230214111049.481:StartDoc
    #@+node:AGP.20230214111049.482:EndDoc
    def EndDoc(self,node):
        pass
    #@-node:AGP.20230214111049.482:EndDoc
    #@-node:AGP.20230214111049.476:Documentation
    #@-others

#@-node:AGP.20230214111049.420:ParserClass
#@+node:AGP.20230214111049.483:WriterClass
class WriterClass(ParserClass):

    #@    @+others
    #@+node:AGP.20230214111049.484:__init__
    def __init__(self,cc):
        
        self.Result = False
        
        self.BeginHtml = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/html4/loose.dtd\">\n<html>\n<head>\n<title>TITLE</title>\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=iso-8859-1\">\n</head>\n<body>"
        
        self.EndHtml = "</body>\n</html>"
        self.DocTab = -5
        
        self.DOC_FILES = [] #must be initialized before cppparse is called
        self.DOC_MENU = None #
        self.DOC_NAMES = [] #
        self.DOC_FOLDER = cc.NAME+"_doc"
        
        ParserClass.__init__(self,cc)
        self.__name__ = "WriterClass"
        
        #self.OnStart = self.OnWriteStart
        #self.OnEnd = self.OnWriteEnd
            
        self.HDR_FILE = None
        self.SRC_FILE = None
        
        if cc.ABS_PATH != "":
            name = cc.ABS_PATH+"/"+cc.NAME
        else:
            name = cc.NAME
        
        cc.OUTEXT = cc.BIN_EXT
        if cc.OPTS.get("Source files") == "True":
            #create exe using .h and .cpp files
            if cc.EXT == cc.BIN_EXT or cc.EXT == "dll" or cc.EXT == "so" or cc.EXT == "":
                cc.sAddText("\" writing "+name+"."+cc.HDR_EXT+" and "+name+"."+cc.SRC_EXT+"...\n")
                
                self.HEADER.file = f = file(name+"."+cc.HDR_EXT,"w+")
                self.HEADER.write = f.write
                self.SOURCE.file = f = file(name+"."+cc.SRC_EXT,"w+")
                self.SOURCE.write = f.write
                
                if cc.EXT == "dll" or cc.EXT == "so":
                    cc.OUTEXT = cc.EXT
            #create a header and verify syntaxe	
            elif cc.EXT == cc.HDR_EXT:
                cc.sAddText("\" writing "+name+"."+cc.HDR_EXT+"...\n")
                
                self.HEADER.file = f = file(name+"."+cc.HDR_EXT,"w+")
                self.HEADER.write = f.write
                self.SOURCE.file = f
                self.SOURCE.write = f.write
            
            #create exe using .cpp or .c file
            elif cc.EXT == cc.SRC_EXT:
                cc.sAddText("\" writing "+name+"."+cc.EXT+"...\n")
                
                self.HEADER.file = f = file(name+"."+cc.EXT,"w+")
                self.HEADER.write = f.write
                self.SOURCE.file = f
                self.SOURCE.write = f.write
                    
            else:
                Error("xcc: ","Incoherent files extensions!")
                return False	
        
        
        if cc.CREATE_DOC == "True":
            self.CreateBaseDoc() 
            #self.DOC_PROC_LIST.append(self.WriteDoc)
            self.Docum = self.WriteDoc
        
        #---------------------------------------
        self.Result = self.Parse()
        #---------------------------------------
        
        #print "close file",self.HDR_FILE,self.SRC_FILE
        
        if self.HEADER.file:
            #self.HEADER.file.write("\n")
            self.HEADER.file.close()
            self.HEADER.file = None
            
            
        if self.SOURCE.file:
            #self.SOURCE.file.write("\n")
            self.SOURCE.file.close()
            self.SOURCE.file = None
            
        for df in self.DOC_FILES:
            if df:
                df.write(self.EndHtml)
                df.close()
                
        if self.DOC_MENU != None:
            self.DOC_MENU.close()
    #@-node:AGP.20230214111049.484:__init__
    #@+node:AGP.20230315102606:Documentation
    #@+node:AGP.20230315124706:DocumNode
    def DocumNode(self,node):    
        self.Docum(self.GetDoc(node))
    #@-node:AGP.20230315124706:DocumNode
    #@+node:AGP.20230315125225:GetDoc
    def GetDoc(self,node):
        #self.cc.sGet("DOC","")
        
        #cc = self.cc
        #print "getdoc:",node
        v = node.v
        cfg = None
        #print "getdoc:",node.v
        print node
        
        if not hasattr(v,"unknownAttributes"):
            return ""
        
        ua	=	v.unknownAttributes
        
        if "xcc_child_cfg" in ua:
            cfg = ua["xcc_child_cfg"]
            
        if "xcc_cfg" in ua:
            cfg = ua["xcc_cfg"]
        
        if cfg and "DOC" in cfg:
            return cfg["DOC"]
        
        return ""
    #@nonl
    #@-node:AGP.20230315125225:GetDoc
    #@+node:AGP.20230315102606.2:PushDoc
    def PushDoc(self,name,intro=True):
        self.DOC_NAMES.append(name)
        
    #@nonl
    #@-node:AGP.20230315102606.2:PushDoc
    #@+node:AGP.20230315102606.3:PopDoc
    def PopDoc(self):
        self.DOC_NAMES.pop()
        
        
    #@nonl
    #@-node:AGP.20230315102606.3:PopDoc
    #@+node:AGP.20230315102606.4:DocName
    def DocName(self,sym="_",s=0):
        name = ""
        for n in self.DOC_NAMES[s:]:
            if name == "":
                name += n
            else:
                name += sym+n
            
        return name
    #@nonl
    #@-node:AGP.20230315102606.4:DocName
    #@+node:AGP.20230315102606.5:StartDoc
    def StartDoc(self,name,node):
        cc = self.cc
        nt = StrToBool(cc.cGet("NEW_TOPIC","False",node=node))
        uh = StrToBool(cc.cGet("USE_HEAD","False",node=node))
        pf = StrToBool(cc.cGet("PRE_FORMAT","False",node=node))
        
        if nt:
            if uh:
                self.PushDoc(name)
            else:
                self.PushDoc(name,False)
        else:
            if uh:
                self.Docum("<H3>"+name+"</H3>\n")
                self.Docum("<blockquote>\n")
                
        
        if pf:
            self.Docum("<pre>")
                
                
    #@-node:AGP.20230315102606.5:StartDoc
    #@+node:AGP.20230315102606.6:EndDoc
    def EndDoc(self,node):
        cc = self.cc
        nt = StrToBool(cc.cGet("NEW_TOPIC","False",node=node))
        uh = StrToBool(cc.cGet("USE_HEAD","False",node=node))
        pf = StrToBool(cc.cGet("PRE_FORMAT","False",node=node))
        
        if pf:
            self.Docum("</pre>")
        
        if nt:
            self.PopDoc()
        elif uh:
            self.Docum("</blockquote>\n")
    #@nonl
    #@-node:AGP.20230315102606.6:EndDoc
    #@+node:AGP.20230214111049.485:PushDoc
    def PushDoc(self,name,intro=True):
        cc = self.cc    
        self.DocTab += 5
        self.DOC_NAMES.append(name)
        
        if cc.CREATE_DOC == "True":
            self.DOC_FILES.append(file(cc.ABS_PATH+"/"+self.DOC_FOLDER+"/"+self.DocName()+".html","w+b"))
        
            if len(self.DOC_FILES) > 1:
                self.WriteMenu("<a href=\""+self.DocName()+".html\" target=\"page_frame\">"+name+"</a><br>\n")    
        
        
            df = self.DOC_FILES[-1]
            df.write(self.BeginHtml.replace("TITLE",self.DocName()+" Documentation"))
        
            if len(self.DOC_FILES) == 1:
                df.write("<h1>"+name+"</h1><hr>")
            elif intro:
                df.write("<h1>"+self.DocName(" > ",1)+"</h1><hr>")
                
            cc.sAddText("\" writing "+cc.ABS_PATH+"/"+self.DOC_FOLDER+"/"+self.DocName()+".html\n")
    
    #@-node:AGP.20230214111049.485:PushDoc
    #@+node:AGP.20230214111049.486:PopDoc
    def PopDoc(self):
        #g.es("PopDoc("+self.DOC_NAMES.pop()+")")
        self.DOC_NAMES.pop()
        if self.cc.CREATE_DOC == "True":
            df = self.DOC_FILES.pop()
            self.DocTab -= 5
            if df != None:
                df.write(self.EndHtml)
                df.close()
    #@nonl
    #@-node:AGP.20230214111049.486:PopDoc
    #@+node:AGP.20230214111049.487:WriteDoc
    def WriteDoc(self,text):
        #self.CURRENT_DOC_LINE += 1
        
        self.DOC_FILES[-1].write(text.encode("utf-8","strict"))
    #@nonl
    #@-node:AGP.20230214111049.487:WriteDoc
    #@+node:AGP.20230214111049.491:CreateBaseDoc
    def CreateBaseDoc(self):
        cc = self.cc
        name = cc.NAME
        
        if self.DOC_FOLDER != "" and os.access(cc.ABS_PATH+"/"+self.DOC_FOLDER,os.F_OK) != 1:
            os.makedirs(cc.ABS_PATH+"/"+self.DOC_FOLDER)
        
        cc.sAddText("\" "+cc.ABS_PATH+"/"+self.DOC_FOLDER+"/index.html\n")
        self.BaseDoc = file(cc.ABS_PATH+"/"+self.DOC_FOLDER+"/index.html","w+b")    
        
        bs = self.BeginHtml.replace("<body>","").replace("TITLE",name+" Documentation")
        
        bs += "<frameset cols=\"25%,75%\">\n"
        bs += "<frame src=\""+name+"_menu.html\" name=\"menu_frame\" frameborder=0 scrolling=\"auto\">\n"
        bs += "<frame src=\""+name+".html\" name=\"page_frame\" frameborder=0 scrolling=\"auto\">\n"
        bs += "</frameset>\n"
    
        
        bs += self.EndHtml.replace("</body>","")    
        
        self.BaseDoc.write(bs)
        self.BaseDoc.close()
        
        
        cc.sAddText("\" writing "+cc.ABS_PATH+"/"+self.DOC_FOLDER+"/"+name+"_menu.html\n")    
        self.DOC_MENU = dm = file(cc.ABS_PATH+"/"+self.DOC_FOLDER+"/"+name+"_menu.html","w+b")
        
        dm.write(self.BeginHtml.replace("<body>","<body style=\"background-color:rgb(235,235,255);\">"))
        dm.write("<h1>"+"<a href=\"index.html\" target=\"_parent\">"+name+"</a></h1><hr align=\"left\" width = \"80%\">")
        
    #@-node:AGP.20230214111049.491:CreateBaseDoc
    #@-node:AGP.20230315102606:Documentation
    #@+node:AGP.20230214111049.488:WriteMenu
    def WriteMenu(self,text):
        s = self.DocTab*"&nbsp;"+text
        self.DOC_MENU.write(s)
    #@nonl
    #@-node:AGP.20230214111049.488:WriteMenu
    #@+node:AGP.20230214111049.489:OnWriteStart
    def OnWriteStart(self):    
        
        cc = self.cc
            
        self.HDR_FILE = None
        self.SRC_FILE = None
        
        if cc.ABS_PATH != "":
            name = cc.ABS_PATH+"/"+cc.NAME
        else:
            name = cc.NAME
        
        cc.OUTEXT = cc.BIN_EXT
        if cc.OPTS.get("Source files") == "True":
            #create exe using .h and .cpp files
            if cc.EXT == cc.BIN_EXT or cc.EXT == "dll" or cc.EXT == "so":
                cc.sAddText("\" writing "+name+"."+cc.HDR_EXT+" and "+name+"."+cc.SRC_EXT+"...\n")
                
                self.HEADER.file = f = file(name+"."+cc.HDR_EXT,"w+")
                self.HEADER.write = f.write
                self.SOURCE.file = f = file(name+"."+cc.SRC_EXT,"w+")
                self.SOURCE.write = f.write
                
                if cc.EXT == "dll" or cc.EXT == "so":
                    cc.OUTEXT = cc.EXT
            #create a header and verify syntaxe	
            elif cc.EXT == cc.HDR_EXT:
                cc.sAddText("\" writing "+name+"."+cc.HDR_EXT+"...\n")
                
                self.HEADER.file = f = file(name+"."+cc.HDR_EXT,"w+")
                self.HEADER.write = f.write
                self.SOURCE.file = f
                self.SOURCE.write = f.write
            
            #create exe using .cpp or .c file
            elif cc.EXT == cc.SRC_EXT:
                cc.sAddText("\" writing "+name+"."+cc.EXT+"...\n")
                
                self.HEADER.file = f = file(name+"."+cc.EXT,"w+")
                self.HEADER.write = f.write
                self.SOURCE.file = f
                self.SOURCE.write = f.write
                    
            else:
                Error("xcc: ","Incoherent files extensions!")
                return False	
        
            #if self.HDR_FILE != None:
            #    self.WriteHeader = self.HDR_FILE.write
            #else:
            #    self.WriteHeader = self.SRC_FILE.write
                
            #if self.SRC_FILE != None:
            #    self.WriteSource = self.SRC_FILE.write
            #else:
            #    self.WriteSource = self.SRC_FILE.write
            
            
            #------------------------------------------
            #if not self.DECLARE_IN_HDR:
            #    self.Declare = self.Define
            #    self.DEC_PROC_LIST.append(self.HDR_FILE.write)
            #else:
            #    self.DEC_PROC_LIST.append(self.SRC_FILE.write)
            
            #if not self.DEFINE_IN_SRC:
            #    self.Define = self.Declare
            #    self.DEF_PROC_LIST.append(self.SRC_FILE.write)
            #else:
            #    self.DEF_PROC_LIST.append(self.HDR_FILE.write)
        
        if cc.CREATE_DOC == "True":
            self.CreateBaseDoc() 
            #self.DOC_PROC_LIST.append(self.WriteDoc)
            self.Docum = self.WriteDoc
            
        
    
        return True
    #@nonl
    #@-node:AGP.20230214111049.489:OnWriteStart
    #@+node:AGP.20230214111049.490:OnWriteEnd
    def OnWriteEnd(self):
        
        if self.HDR_FILE:
            self.HDR_FILE.write("\n")
            self.HDR_FILE.close()
            self.HDR_FILE = None
            
        if self.SRC_FILE:
            self.SRC_FILE.write("\n")
            self.SRC_FILE.close()
            self.SRC_FILE = None
            
        for df in self.DOC_FILES:
            if df:
                df.write(self.EndHtml)
                df.close()
                
        if self.DOC_MENU != None:
            self.DOC_MENU.close()
    #@nonl
    #@-node:AGP.20230214111049.490:OnWriteEnd
    #@-others
#@-node:AGP.20230214111049.483:WriterClass
#@+node:AGP.20230214111049.492:BreakFinderClass
class BreakFinderClass(ParserClass):
    #@    @+others
    #@+node:AGP.20230214111049.493:__init__
    def __init__(self,cc):
        
        self.Result = False
        ParserClass.__init__(self,cc)
        
        self.OnStart = self.OnFindStart
        self.OnParseNode = self.BreakOPN
        
        self.Result = self.Parse()
    #@-node:AGP.20230214111049.493:__init__
    #@+node:AGP.20230214111049.494:OnFindStart
    def OnFindStart(self):
        # loading event funcs
        if self.DECLARE_IN_HDR:
            self.WriteHeader = self.BreakDec
        else:
            self.WriteHeader = self.BreakDef
            
        if self.DEFINE_IN_SRC:
            self.WriteSource = self.BreakDef
        else:
            self.WriteSource = self.BreakDec
    
            
        self.OnParseNode = self.BreakOPN
        
        self.BREAKS = {}
        
        self.CURRENT_BREAKS = None
    
        return True
    #@nonl
    #@-node:AGP.20230214111049.494:OnFindStart
    #@+node:AGP.20230214111049.495:BreakDec
    def BreakDec(self,text):
        
        cbl = self.CURRENT_BODY_LINE
        cb = self.CURRENT_BREAKS	
        
        if cb and str(cbl) in cb:
            self.BREAKS["h:"+str(self.CURRENT_HDR_LINE)] = cb[str(cbl)]
    #@nonl
    #@-node:AGP.20230214111049.495:BreakDec
    #@+node:AGP.20230214111049.496:BreakDef
    def BreakDef(self,text):
        
        cbl = self.CURRENT_BODY_LINE
        cb = self.CURRENT_BREAKS
        
        if cb and str(cbl) in cb:
            self.BREAKS[self.cc.SRC_EXT+":"+str(self.CURRENT_SRC_LINE)] = cb[str(cbl)]
    #@-node:AGP.20230214111049.496:BreakDef
    #@+node:AGP.20230214111049.497:BreakOPN
    def BreakOPN(self,node,back=False):
        
        cc = self.cc
        
        txcd = cc.cGetDict(node)
        if txcd and hasattr(txcd,"BreakPoints"):
            self.CURRENT_BREAKS = txcd.get("BreakPoints")
        else:
            self.CURRENT_BREAKS = None
    #@nonl
    #@-node:AGP.20230214111049.497:BreakOPN
    #@-others
#@nonl
#@-node:AGP.20230214111049.492:BreakFinderClass
#@+node:AGP.20230214111049.498:SeekErrorClass
class SeekErrorClass(ParserClass):
    #@    @+others
    #@+node:AGP.20230214111049.499:__init__
    def __init__(self,cc,line,ext,col="0",color="red"):
    
        ParserClass.__init__(self,cc)		
        self.SEEK_LINE = line
        self.SEEK_COL = col
        self.SEEK_EXT = ext
        self.FOUND_NODE = None
        self.FOUND_INDEX = "1."+col
        self.OnStart = self.OnStartSeek
        
        if self.Parse() == False and self.FOUND_NODE:
            cc.GoToNode(self.FOUND_NODE,self.FOUND_INDEX,tagcolor=color)
        else:
            Error("xcc: ","Unable to find line: "+str(line))
    #@nonl
    #@-node:AGP.20230214111049.499:__init__
    #@+node:AGP.20230214111049.500:OnStartSeek
    def OnStartSeek(self):
        
        if self.DECLARE_IN_HDR:
            self.HEADER.write = self.SeekDec
        else:
            self.HEADER.write = self.SeekDef
        
        if self.DEFINE_IN_SRC:
            self.SOURCE.write = self.SeekDef
        else:
            self.SOURCE.write = self.SeekDec
        
        return True
    #@nonl
    #@-node:AGP.20230214111049.500:OnStartSeek
    #@+node:AGP.20230214111049.501:SeekDec
    def SeekDec(self,text):
        if self.DO_PARSE:
            if self.CURRENT_HDR_LINE == self.SEEK_LINE and self.SEEK_EXT == self.cc.HDR_EXT:
                index = None
                if self.CURRENT_LOCATION == 0:  #head
                    index = "1."+self.SEEK_COL
                if self.CURRENT_LOCATION == 1:  #body
                    index = str(self.CURRENT_BODY_LINE)+"."+self.SEEK_COL
                if self.CURRENT_LOCATION == 2:  #tail
                    index = "1000."+self.SEEK_COL
                
                self.DO_PARSE = False
                self.FOUND_NODE = self.CURRENT_NODE.copy()
                self.FOUND_INDEX = index
    #@nonl
    #@-node:AGP.20230214111049.501:SeekDec
    #@+node:AGP.20230214111049.502:SeekDef
    def SeekDef(self,text):
        if self.DO_PARSE:
            if self.CURRENT_SRC_LINE == self.SEEK_LINE and self.SEEK_EXT == self.cc.SRC_EXT:
                index = None
                if self.CURRENT_LOCATION == 0:  #head
                    index = "1."+self.SEEK_COL
                if self.CURRENT_LOCATION == 1:  #body
                    index = str(self.CURRENT_BODY_LINE)+"."+self.SEEK_COL
                if self.CURRENT_LOCATION == 2:  #tail
                    index = "1000."+self.SEEK_COL
                
                self.DO_PARSE = False
                self.FOUND_NODE = self.CURRENT_NODE.copy()
                self.FOUND_INDEX = index
    #@nonl
    #@-node:AGP.20230214111049.502:SeekDef
    #@-others
#@nonl
#@-node:AGP.20230214111049.498:SeekErrorClass
#@+node:AGP.20230214111049.503:LocatorClass
class LocatorClass(ParserClass):
    #@    @+others
    #@+node:AGP.20230214111049.504:__init__
    def __init__(self,cc,node,line):
        
        ParserClass.__init__(self,cc)		
            
        self.LOCATE_NODE = node
        self.LOCATE_BODY_LINE = int(line)
        self.FOUND_FILE_LINE = None
        self.FOUND_FILE_EXT = None
        
        self.FOUND_HEAD_HDR_LINE = None
        self.FOUND_HEAD_SRC_LINE = None
        self.FOUND_BODY_HDR_LINE = None
        self.FOUND_BODY_SRC_LINE = None
        
        self.FOUND_OTHERS = None
        #self.OnStart = self.OnStartLocate
        
        #print "locator:"
        
        if self.DECLARE_IN_HDR:
            self.HEADER.write = self.LocateDec
        else:
            self.HEADER.write = self.LocateDef
            
        
        if self.DEFINE_IN_SRC:
            self.SOURCE.write = self.LocateDef
        else:
            self.SOURCE.write = self.LocateDec
        
        self.Parse()
    #@nonl
    #@-node:AGP.20230214111049.504:__init__
    #@+node:AGP.20230214111049.505:OnStartLocate
    def OnStartLocate(self):
        if self.DECLARE_IN_HDR:
            self.HEADER.write = self.LocateDec
        else:
            self.HEADER.write = self.LocateDef
            
        
        if self.DEFINE_IN_SRC:
            self.SOURCE.write = self.LocateDef
        else:
            self.SOURCE.write = self.LocateDec
    
        
        #self.DOC_PROC_LIST.append(self.LocateDoc)
        
        return True
    #@-node:AGP.20230214111049.505:OnStartLocate
    #@+node:AGP.20230214111049.506:LocateDec
    def LocateDec(self,text):
        #print "h:",self.HEADER.CURRENT_LINE,"b:",self.CURRENT_BODY_LINE,text
        if self.DO_PARSE == True:
            if self.CURRENT_NODE == self.LOCATE_NODE:
                
                if self.CURRENT_LOCATION == 0 :#and self.FOUND_HEAD_HDR_LINE == None:      #head
                    self.FOUND_HEAD_HDR_LINE = self.HEADER.CURRENT_LINE
                    #if self.CURRENT_RULE == "func":
                    #    print "func head dec:",self.HEADER.CURRENT_LINE,text
                elif self.CURRENT_LOCATION == 1:
                    if self.FOUND_BODY_HDR_LINE == None:    #body
                        self.FOUND_BODY_HDR_LINE = self.HEADER.CURRENT_LINE
                
                    if self.CURRENT_BODY_LINE == self.LOCATE_BODY_LINE:
                        self.FOUND_FILE_LINE = self.HEADER.CURRENT_LINE
                        self.FOUND_FILE_EXT = self.cc.HDR_EXT                    
                        #self.DO_PARSE = False
                        
                elif self.CURRENT_LOCATION == 2:    #tail, always at least a newline
                    self.FOUND_OTHERS = self.others
                    self.DO_PARSE = False
                    #if self.CURRENT_RULE == "func":
                    #    print "func tail dec:",self.HEADER.CURRENT_LINE,text
                    return
                
                """if self.CURRENT_RULE == "func" and self.CURRENT_MO[4][0]!= "":#(spec,ret,name,params,pure,dest,ctors)
                    self.FOUND_FILE_LINE = self.CURRENT_HDR_LINE
                    self.FOUND_FILE_EXT = self.cc.HDR_EXT                
                    self.DO_PARSE = False
                    
                    return"""
                
                
                    
                    
    #@nonl
    #@-node:AGP.20230214111049.506:LocateDec
    #@+node:AGP.20230214111049.507:LocateDef
    def LocateDef(self,text):
        #print "c:",self.SOURCE.CURRENT_LINE,"b:",self.CURRENT_BODY_LINE,text
        if self.DO_PARSE == True:        
            if self.CURRENT_NODE == self.LOCATE_NODE:
                
                if self.CURRENT_LOCATION == 0:# and self.FOUND_HEAD_SRC_LINE == None:
                    self.FOUND_HEAD_SRC_LINE = self.SOURCE.CURRENT_LINE
                    #if self.CURRENT_RULE == "func":
                    #    print "func head def:",self.SOURCE.CURRENT_LINE,text
                elif self.CURRENT_LOCATION == 1:
                    if self.FOUND_BODY_SRC_LINE == None:    #body
                        self.FOUND_BODY_SRC_LINE = self.SOURCE.CURRENT_LINE
                
                    if self.CURRENT_BODY_LINE == self.LOCATE_BODY_LINE:
                        self.FOUND_FILE_LINE = self.SOURCE.CURRENT_LINE
                        self.FOUND_FILE_EXT = self.cc.SRC_EXT
                        #self.DO_PARSE = False
                
                elif self.CURRENT_LOCATION == 2:    #tail, always at least a newline
                    self.FOUND_OTHERS = self.others
                    self.DO_PARSE = False
                    #if self.CURRENT_RULE == "func":
                    #    print "func tail def:",self.SOURCE.CURRENT_LINE,text
                    return
                
                """if self.CURRENT_RULE == "func" and self.CURRENT_MO[4][0]!= "":
                    self.FOUND_FILE_LINE = self.CURRENT_SRC_LINE
                    self.FOUND_FILE_EXT = self.cc.SRC_EXT                
                    self.DO_PARSE = False
                    
                    return  """         
    #@-node:AGP.20230214111049.507:LocateDef
    #@-others
#@-node:AGP.20230214111049.503:LocatorClass
#@-node:AGP.20230214111049.419:Parsing classes
#@-node:AGP.20230214111049.60:Classes
#@-others
#@nonl
#@-node:AGP.20230214111049:@thin xcc_nodes.py
#@-leo
