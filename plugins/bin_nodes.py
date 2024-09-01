#@+leo-ver=4-thin
#@+node:AGP.20230307095223:@thin bin_nodes.py
"""Integrate C/C++ compiler and debugger in a node."""

#@<< About this plugin >>
#@+middle:AGP.20230307095223.1:Documentation
#@+node:AGP.20230307095223.2:<< About this plugin >>
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
#@-node:AGP.20230307095223.2:<< About this plugin >>
#@-middle:AGP.20230307095223.1:Documentation
#@nl
#@<< version history >>
#@+middle:AGP.20230307095223.1:Documentation
#@+node:AGP.20230307095223.3:<< version history >>
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
#@-node:AGP.20230307095223.3:<< version history >>
#@-middle:AGP.20230307095223.1:Documentation
#@nl
#@<< what I did >>
#@+middle:AGP.20230307095223.1:Documentation
#@+node:AGP.20230307095223.4:<< what I did >>
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
#@-node:AGP.20230307095223.4:<< what I did >>
#@-middle:AGP.20230307095223.1:Documentation
#@nl
#@<< what was redid/undid >>
#@+middle:AGP.20230307095223.1:Documentation
#@+node:AGP.20230307095223.5:<< what was redid/undid >>
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
#@-node:AGP.20230307095223.5:<< what was redid/undid >>
#@-middle:AGP.20230307095223.1:Documentation
#@nl
#@<< imports >>
#@+node:AGP.20230307095223.12:<< imports >>
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


Pmw = g.importExtension('Pmw',    pluginName=__name__,verbose=True,required=True)
#@nonl
#@-node:AGP.20230307095223.12:<< imports >>
#@nl

controllers = {}

if 1: # To be replaced by ivars
    #@    << globals >>
    #@+node:AGP.20230307095223.13:<< globals >>
    #@+others
    #@+node:AGP.20230307095223.14:Icons
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
    #@+node:AGP.20230307095223.15:Go
    Go_e = "S\'x\\xdam\\x8e\\xcbn\\x830\\x14D\\xf7\\xfcLk \\xb2\\xbc\\xe8\\xe2\\xda@\\xc4\\xd32\\xe0\\x90.!J\\xa1\\x04\\x02\\x04K\\x80\\xbf\\xbeV\\xd6\\x1d\\xe9\\xe8\\x8cf5\\xf9\\xe7p\\xe6\\xde\\xd0\\xf9\\x00\\x02R\\x01\\xc0\\x9b\\xbb\\xa3\\xf0\\xfdd@\\nWH5\\x95\\xe9\\x956\\xd6+\\xe6\\x844\\xdcl|\\xbf]\\x03\\xfd\\xb2\\t\\xc16r\\x96j \\xa7\\xe3f\\xe9\\xb9\\x90\\xea\\xfbH\\xb1[\\xf8\\xfa\\xa90v2\\xadG\\xf5\\xc2v\\xd6\\x7f\\x18\\x88\\x01\\x8d\\xaa\\xef\\x83\\xb9v\\x1es\\xdc\\xc1?a\\xdb[\\xd6\\xfb\\x11@X\\t(\\x19\\xdd\\xc35\\xa6\\xd4\\x83)\\x8d\\x1fG\\xeb\\x8a\\x98uB\\xa2K\\xd2\\xb5\\xc0#\\xf8\\xcd\\xe5xI\\x8ap\\x95\\xb1\\xdf\\x8b\\x15_\\x9eT\\xf8\\xac\\xf4X\\\'\\xd7\\xf9,\\xc0\\x92u\\x11\\xc0\\x81\\xf2i\\xd8\\xdbtIR\\xdaJw\\x9aD\\xbb\\xf1(b%\"\\xf5\\x02b\\x8b\\x7f\\x80n\\xa2E]\\xe1f~\\x00\\xe0\\xad_\\xd6\\x1f\\x96\\x88[)\'\np0\n."
    #@nonl
    #@-node:AGP.20230307095223.15:Go
    #@+node:AGP.20230307095223.16:StepIn
    StepIn_e = "S\'x\\xda\\x95\\xd0Ms\\x820\\x10\\x06\\xe0;\\x7f\\xa5\\x17\\x15\\xa6\\x0e\\x87\\x1e6\\x100|\\x9a\\xa4\\x0c\\xda\\x9bP\\x0b\\x02\\x82\"\\x18\\xf0\\xd77\\xe1\\xdaS3\\xf3dg\\x92\\xec\\xbb3a\\xab\\xc6\\x8d\\xed\\xa6\\xc4\\x00\\x14\\xa2\\x04 \\xce\\xae\\xfa\\x98\\x9d\\xf5a{^\\x0f\\xdbTy\\r\\x99\\x12+S\\xbe\\x95R\\xf3)\\r\\xd9\\xc6|J\\xb2\\xae\\xe5\\x93\\xb5\\xa6\\xb6\\xfe\\xb4\\x19n\\xa7\\xb4QZo\\xce\\x95\\xc6\\xe3\\x89Ry<\\xac\\xc8\\xac\\xe0\\x92\\xf0\\xc52I\\xca\\xf5\\xe1\\x95\\xeb\\xd1\\xe2\\xa4G\\xbd&sTV\\x7f\\xdcD\\x95\\x92\\xaa\\x84\\xfa\\xe6\\xf3\\xfaf\\xd1\\xda\\xb3h\\x85\\xa7\\x90\\xab\\x03\\x99\\xc3\\xea/\\x97\\x01\\xc5P\\x10\\x0b\\xfe.\\r\\xfe\\xb3,\\xb1\\x94\\xe5K\\x00H\\x05\\xb0\\xb7\\xd0D\\x1e>\\x02{\\xee\\xb8v\\x7f \\x01\\xc4A\\x05\\x159\\x8f^\\xd4\\xe8\\xb8+\\xef\\xcfQ5O\\x06\\xd0\\x10\\x17yq\\xddU\\xc4H(B(\\x19-\\x87N\\x82\\xcb\\x8e\\x82\\xf8c\\x8f\\x8aU\\xe8\\x072\\x9b\\x89\\x1d\\x08m\\x15\\xbb\\xc8f\\xc2\\xb7\\xf6\\xcc\\xeb.\\x07\\x84\\xcb\\x90\\xec\\x03Q\\xd0\\xb1\\xa4\\x989\\xf7\\x9f\\x16\\xdek,\\x1b>\\x9b\\xef\\xc0\\xb6\\x8f\\x1d=\\xc4\\xed\\xe5M\\x0e\\xe1\\x8c^Z\\xe4|\\xd2 j\\x10\\x1a\\xf8.\\xd3J\\xd1\\xcd\\x1e\\xb2\\rJb\\xd4\\x82i:\\x85 `?>\\xb4_\\xa4j\\x9b\\xc9\'\np0\n."
    #@nonl
    #@-node:AGP.20230307095223.16:StepIn
    #@+node:AGP.20230307095223.17:StepOver
    StepOver_e = "S\'x\\xda\\x95\\xd0Mo\\x830\\x0c\\x06\\xe0;\\xbf\\xa6|hh\\x87\\x1e\\x9c\\x10h`@\\x03\\xed(\\xbbA\\x86\\xc2\\x97J\\x05l\\x01~\\xfdHw\\x9f\\xb4Wz\\xec\\x8b-YN\\x0e\\xbd\\x17;}M\\x00\\x18DW\\x80\\xc8\\xae\\xf4\\xd9\\xce\\x94m.\\x95XY\\xb8\\xad\\xb8\\xca7\\xbf\\xed\\xb2We.\\rE\\xdfGuM\\x95\\xb1\\xccf\\xe5Q\\x18\\xf3\\xb8{\\x14Y\\xaf\\xdc\\x83\\x8c\\xdf\\xfd\\x95\\xf7\\xfez\\xed\\xe9\\x1a\\xb6t%5M\\x9f*s\\xb6+3\\xda\\xf8\\xae0#\\xb56j\\xb9\\xfe\\xbbz\\xed\\xfdTI\\xbbG\\x90v>f\\xed\\xf0\\x12\\xb7d\\t\\x93\\xee\\xc3K\\x80\\x11\\x10\\x14\\xc3\\xdf\\xd1\\xe0?\\xc1\\xf2\\xd9\\x9e/\\x01\\xa0\\x8d\\x847\\x8c\\x16:\\x05\\x08\\xe1uJ\\xb5\\xb1\\xc3IN]$\\x98\\x90\\\'\\x1f\\xa4\\xcc\\xc3\\xc0\\x850\\x8c\\x9a\\xba\\xa6A\\xec\\x92U\\xcf\\xc0At\\x10\\x11r\\x93\\xeb\\x019\\xc8bS\\x02\\x08\\x1f\\x863\\x96\\xcc\\xea.\\x1e\\x08\\xbd8a4hy\\x00\\x143\\xdf\\xee\\xef\\xb5\\xe0\\xd4\\xa3h\\xab\\x9c\\xf2\\xaba\\xef\\x1e\\xc6\\x84I\\xcag!\\xac\\x98\\x9cH\\xcbo\\x13\\x069Y\\xa9?b\\x03\\xce\\xedV[\\xc5%\\xac\\x97O\\xc2\\xb1!)\\xb9]4Q\\x87\\xab\\xe77\\xc2\\xca\\xf4\\xb30\\xf9\\xdb~\"\\xc4\\xf2x\\xd4~\\x00\\\'\\xed\\x9a\\xd0\'\np0\n."
    #@nonl
    #@-node:AGP.20230307095223.17:StepOver
    #@+node:AGP.20230307095223.18:StepOut
    StepOut_e = "S\"x\\xda\\x95\\xd0\\xddn\\x820\\x14\\xc0\\xf1{\\x9eF\\xc5\\x8c\\xedb\\x17\\xa7\\xa5`a\\x80\\x05;\\xd4;As\\xca\\x87\\x9bQ\\x94\\x8f\\xa7_\\xcb\\x1b\\xac\\xc9/\'9i\\xfeM\\x9a.Z?q[\\xc5\\x00\\x04\\xc4\\x12 )\\xae\\xf6\\xb3\\xb8\\xd8\\x9dsYvNnL]a$\\xc6P:\\xda\\xde{\\x95\\xf9\\x87\\xd1\\x15\\xab\\x8f\\x97\\xa6\\xe7\\xd2\\xd2\\xf7\\x96\\xc6\\xbd\\xc8;\\xe3vZiy\\xab\\x95?\\xc18k\\x83L\\xd6A\\x16\\xd5|\\x8c\\x14\\x1f\\x99\\xe2\\xd9\\xec\\xb2N\\x9d\\xf9U\\xad\\xb4\\xbb\\xc9*\\xedx2Nv|\\xd7\\x9d\\xd9a\\x15\\xd7F~\\x8duV\\x97\\x9a[\\x985\\x01\\x15\\xf5\\xef[R\\xb3!\\xca\\xccB\\xf7\\xd2\\xe6\\xe8\\xa7 \\x18 \\xa7\\x00`\\xc1\\x7f\\x0e\\xed\\xe71\\x7f\\t\\x00o\\x01\\xb6\\x94\\x0c\\\\\\xfa\\xd4E\\xc4\\xad\\xa5\\xb7\\x04\\x9b\\xfc\\x8b\\x02\\xde7A\\x8f\\xb8\\x90\\xa17E\\xef\\x8ce=6\\x8c\\xd0\\x1d[\\xec<\\xa2\\xb8\\xdc\\x10w|\\x84\\x02\\xf0\\xb6\\xe0\\xd2S4F\\xeaUp8\\xd1\\xe8\\x8ar\\x98\\xa0\\xea\\xad\\xa6<\\xb9(\\x90\\x9d_J\\x08\\xdf\\x150\\x9e/\\xacI\\x15J\\x97\\xba4\\x0f\\xfdjI c>\\xfb\\xe6\\x9b\\xfd/\\x0e\\x870\\x8a\\x08*2$\\x10\\x9c\\xf91\\xc3*>$t\\xbf\\x86\\xeaL,2\\xae\\xc6M\\xa3{O\\x07H\\xfa\\x90\\x94\\xef\\xa0/]_\\xb1\\xf2\\x8b\\xa0\\x80\\xa4\\xff\\xfc\\xb4\\xfe\\x00\\xd4\\xc7\\xa1 \"\np0\n."
    #@nonl
    #@-node:AGP.20230307095223.18:StepOut
    #@+node:AGP.20230307095223.19:Pause
    Pause_e = "S\'x\\xda\\x95\\xceKn\\x830\\x18\\x04\\xe0=\\x97i\\xf3t\\xba\\xc8\\xe2\\xb7\\t\\xc6N\\xb0e\\x08\\x02\\x96\\x85\\x02\\x86:\\x84\\x14Wn9}Q{\\x82\\x8e\\xf4I\\xb3\\x19i\\xe2gC\\xa5o\\xf4\\t@A\\xa4\\x00\\x04\\xaa7\\x16e+[f\\xbb\\xc5f1\\xdbR.]\\xce\\x13Z\\xe4\\xc1\\xcb!\\x0f\\xd0>3\\x03OR\\xc3\\x92\\x93\\t-\\xeaC1{\\x9a\\x8a\\xfeim?\\xea\\xb5\\xedM\\xc0\\x93\\xda\\xc1\\xffC\\xfeF\\xde\\xef#\\x00V(\\x10\\x04\\x7f\\xb1\\xe9\\xec\\xe3\\xd6U\\xb9\\x0c}\\xd82B\\xb4\\xdaJ\\xca\\xaf\\xeeN\\x19&8m8\\xef\\x8aT\\xf9\\xb4\\xd3\\xd3%}\\xcc\\xf7(\\x13\\xac\\xed\\xa2\\xc6\\x80\\xday\\xef\\xcc\\x07\\x03\\xac\\xba\\xc9\\x98\\x1d\\x1e\\x82\\xde\\xba\\xd1\\x0e\\xda\\xb1\\xf4\\xbb\\x91\\xe6Z]\\xe2\\xcf\\xbe(h\\x89\\xc1\\x9d\\x13\\xdc\\xb7N\\x91\\x81\\x8c\\x8e\\xbf\\xd11~\\x8d\\x08\\x80t\\xc7\\xa3\\xf7\\x03\\xce\\xc7^\\x95\'\np0\n."
    #@nonl
    #@-node:AGP.20230307095223.19:Pause
    #@+node:AGP.20230307095223.20:Stop
    Stop_e = "S\'x\\xda-\\x8c\\xc1\\x8e\\x820\\x14E\\xf7\\xfc\\x8c\\xa2\\x18\\xdc\\xb8x\\x14h\\x0b%\\x0e4LSv`\\xb4O@t\\xa4\\x19\\x18\\xbe~&d\\xee\\xe2\\x9c\\xe4,n\\xb1\\xed\\xe99\\xec1\\x02\\xc8Ad\\x00\\xe7\\xe6\\xb1\\xb7\\xfe\\xd5\\xb5\\xbeZl\\xa3\\x96\\xaf\\x9d}\\xd5\\xaal\\xd9_\\xdc\\xdb\\xb7>\\x1eR~\\xf9$\\xb4q\\t\\xbdx3\\x88\\xed\\x0b\\xfe\\xe7\\xac$\\xd3\\xaa\\xf5\\x10\\x80\\xab\\x1c\\x18\\tf>\\xa6a`&\\x9d\\xb0\\xb8\\xe5\\x1d\\xa5\\x811Z\\x8b\\x04y\\xa78\\x18\\x8c\\xde\\xb5\\x91P\\xd6\\t\\xbd\\xe3\\xc4\\xaa\\xef\\xc9s\\xb2Z\\x02\\xc8l\\xb8\\xde\\x97\\xaa\\x93\\x85\\xe8\\xe4\\xb8A\\x94\\xba|T\\xa2_2\\x16\\xc5$\\x7f\\xa6\\xb7\\x8f\\xc1\\xe0\\x0f13X\\x8a\\x05F&\\x1eZ\\xe9Y\\x1a\\x00\\x84\\xe3\\xc9\\xf9\\x05\\x1a\\x01HO\'\np0\n."
    #@nonl
    #@-node:AGP.20230307095223.20:Stop
    #@+node:AGP.20230307095223.21:Doc
    DocData = "S\'x\\xda\\xcd\\x92\\xb9\\x92\\x9b@\\x00Ds~E\\x01\\x08\\x81\\x80\\xc0\\xc1\\x0c\\x83Y\\x0e\\x89C \\xa1\\xcd\\xc4\\xc2\\x0c \\x98\\x11\\xe2\\xe6\\xeb\\x17\\xdb\\xa1S\\x07~U/\\xe9\\xea\\xea\\xa8C\\xa16=T\\x17\\x06\\x00\\x01\\xf0\\xee\\x008^\\xf58\\xde\\xea\\xd4-\\x8f\\xd8\\x1d4\\xfc\\x165\\xac\"\\x987\\x19\\xdf=s\\xb0\\xa7\"\\x9boM+IMH\\xedGQ\\xbene%\\xe7u\\x9d\\xb6\\nG\\\\q\\xf7\\xcb\"=\\xee\\n\\xc7)\\x9f\\xeez\\xe9\\\\\\xff\\xb3\\xef\\x10(5\\x14T\\\'\\xecQ5\\r\\xeb\\xaf$l\\xd4*\\xa6*\\x7f\\xa5\\x19J\\x9a\\x8c&4[\\xcbFM\\x02\\xf65&L=|r\\xed\\x19E\\xac\\xe3\\x83\\xae\\xa7q\\x9f\\xe1`\\xec\\x15<\\xf6>a9\\xda\\xa4m?\\xbc\\xbb\\xa1K\\xbd\\xa5\\x1b\\xbd\\xe5\\x8c\\xfd\\xa9G\\xde\\xac\\xa5\\xde\\x9c\\\'\\xcd\\xb4\\x1b\\x87)\\x7f\\xb7\\x8b\\x8f\\xe6\\x15\\xa3\\x99[\\x87\\x8a\\x89y\\xc5\\x0e~z8\\x0c\\xca \\xe7\\xfc(\\xf3\\x95,c*\\xcb\\xe3&?*\\n\\x9f\\x8a*^Uu<h\\x1a\\xbf\\x817\\\'\\xf0\\x17\\x1c\\xf8\\x87\\xfc\\xa7c\\xfa\\xf4g\\xec\\xf7-\\x00\\xb0(\\x81X\\x87\\xb3\\xd59\\x10\\x92%\\x16\\r#\\x9a\\xeeq`\\x932\\x0c^\\x1e\\n\\xee\\xad\\x0e\\xcd\\xc86\\x12\\x9bLS|:Y\\x86eR\\x07\\x11\\x89\\xc5\\xd0\\xac\\xe4\\x85\\xdb\\xeb\\x15`V\\x1e\\xd4\\x936X&,\\x8c&\\xf6\\xcc\\t\\xdc\\xe0\\xc7\\xf3%\\x03\\xd3o\\xa2k$\\xf5\\x91-,8x\\n\\xf6\\xaa\\xb0H~.\\xe9\\xa5\\x11Z\\xf7L\\x04\\xa7\\xbeT\\x11[\\x1f\\x1f\\xee \\xca\\x9ct,\\x9d\\x97\\x11\\xf2W\\x8bL\\xda\\x1d\\x18\\xfa\\xbc\\\'\\xf0gI\\x80d!c\\xbb\\xd1X\\x97P\\xb2\\x80\\x0e\\x88`\\xdcO[\\x1e\\x07\\x16\\x03af\\x19%`.,\\xa0\\x1e\\xfb\\x0e\\xd9\\x1a\\xa8\\xfb\\xc1}\\x03\\xa7@\\xeb\\x92\'\np0\n."
    #@nonl
    #@-node:AGP.20230307095223.21:Doc
    #@+node:AGP.20230307095223.22:Watch
    WatchData = "S\"x\\xda\\x95\\x90\\xdbr\\x820\\x10@\\xdf\\xf9\\x1a\\xc1Z\\xea\\xe3&\\x86\\x8b\\x96\\x8bf\\x18\\x8coBk \\xa4B!\\x8a\\xc9\\xd77\\xfa\\x07\\xdd\\x99\\xb3g\\xf7ewg\\x0f\\x0b\\x19f\\x1b\\xd9\\x10\\x80=\\xa4\\x05@Z\\x95\\xae\\xaaJ\\xa3\\xaa\\xec\\xc9\\xa3\\xf633\\xf9\\xd6\\xc7\\xcc\\x9d\\xfc\\xc0:p\\xa7c`,\\xf7\\xca\\xd6\\xa3\\xb7\\xbeW\\xdeZ\\x9d\\xbd\\xb5\\xb3\\xfc-\\xd7\\x16w5h\\x0bu\\xfdwO\\x8d\'\\xad\\xcco)\\x07F\\xe5\\xaa\\xd7\\xd2\\xf4T.\\x07Z\\x8fL\\xd7\\x8a\\xd1\\xfa~\\xd2\\x85\\xdc\\xd2\\xe2j\\x11\\xb1NDL\\x9f\\x10\\xe7\\x99\\x9a\\xe8Fd\\x94\\x91\\xe1x#\\xc2\\xfaj\\xfb&R~\\x13\\xa5\\xbe\\xb0X\\x9b\\xefejjO\\x99&T\\xe3\\xd9\\x1d\\x04\\xf3\\xd2\\xb3]g\\xb1\\x13\\xbbaG9\\x80\\x03\\xff\\t<\\xbf\\xf4z\\t@\\xdc\\x00D\\x18=\\x18\\xdbm\\x10\\x9f\\x07\\xe2\\xf4\\xb8El\\xda\\xda\\xe6\\xab,\\x82\\x16b\\x12F\\x98\\x7f\\x04|\\x143#\\x04\\x03\\x97\\x19N\\xda>\\xee>\\xa3\\x96s\\x9d$-\\xdbw1A\\xb3j\\xcfR\\xac\\x12\\xa0!\\xc6\\xec\\x92#~p\\xdeB\\x84\\x10]L\\xb7X\\xf3\\xbe\\xc8s\\x01\\x8f\\xe2\\x07o\\x0eo\\xfdq#`\\x9f\\x07!\\x1cz\\x8d\\n>\\xbb\\xdd\\xe5\\xb3y\\xef\\x92,Ar\\xde\\xdez\\xd4\\xa4\\xa5)\\xc7\\x92\\x04\\xdfWx\\xd4\\x1d:9\\xdcey\\x84\\x16{{\\xba\\xef\\xfc\\x01\\xdb\\xb2\\x9a\\xfc\"\np0\n."
    #@nonl
    #@-node:AGP.20230307095223.22:Watch
    #@+node:AGP.20230307095223.23:Config
    ConfigData = "S\'x\\xdaU\\xce\\xc1r\\x820\\x14\\x85\\xe1=O\\x03\\xd6\\x11\\xbb\\xbc\\t\\x84\\x06\\x0c\\x99@-\\xda\\x1d\\xa4N\\x10(j\\xc9\\x10\\xe0\\xe9k\\xd8yg\\xbe\\xb9\\x9b\\x7fq2\\xb7\\x8bx\\xd0\\xd5!\\x80\\x00&\\x00R\\xff\\xe2i\\xbf\\xf0tU,\\xba\\xe2\\xd6$}\\x8b\\x8c\\xf2D\\xa6\\xa7Q\\x16\\xefc\\xb5\\xb1l\\xe6\\xfd\\x95\\x1bm9\\xf7\\xb2\\xe8\\xfa\\xa4\\x90}<\\xaf::\\xb3\\x86\\xcea\\xfd\\xa1\\xfd\\xcb[\\xba\\xc8\\xb5K\\x9b\\xb3g\\xcb8?\\xb6\\xf7$W\\xf0z\\xd8\\xac\\xcfY\\x17\\x01\\xd0\\n \\xc68S7\\x16\\x802\\x8a\\xd0\\x01\\x1b\\x8a\\tF\\x8aR\\xce@\\x18N\\x00+\\x97\\x8a\\x14\\xc0$1\\xa0\\xba\\x1d\\xcaC-\\xdc\\x9c#\\x04\\xfbG\\x19\\xd57\\xe7\\xf8\\x0b(@\\xed\\x105\\x0b=3\\x1ev\\x8a\\xf5\\x15\\xc1\\xd0\\xee\\xd1!\\x80t\\xc74R\\xe2Hq\\x8f\\x94\\xfb\\xc5\\xae`\"\\x81\\x82O\\xd3d\\xd1\\xf5[\\xe5\\x12=\\xa6\\xed\\xcf)\\x84m\\xbb\\x1b\\x03\\xe7\\xb9\\xd8w\\xfe\\x01*\\x83e%\'\np0\n."
    #@nonl
    #@-node:AGP.20230307095223.23:Config
    #@+node:AGP.20230307095223.24:Prompt
    Prompt_e = "S\'x\\xda\\xad\\x90\\xcdn\\xab0\\x14\\x84\\xf7\\xbcJ\\x16\\xb9I\\xdbp\\xbb\\xe8\\xe2p\\xb0\\x8d\\xe1\\xf2\\xe3:\\xb4%;\\x12r\\r\\x86\\x14Zh\\x0cy\\xfa\\x92\\xf6\\t*\\xf5\\x93F\\xa3\\x91F\\xb3\\x98\\xc7?\\r\\x8b\\xdd\\xa6d\\x02\\x04D)@\\xb2\\x9c\\xf9\\x7fs\\xbfX\\x9e\\xed\\xc5\\xfet7\\xd8\\xc7\\x9ba\\xff\\xbc\\x9au\\xe9\\xed\\xf8\\xd2\\xbf\\xd0\\xf1\\x1a\\xf3\\xe7\\xa6\\xdbM\\x87W\\x7f:4|\\n5\\x97\\xc4*\\xbdk;\\xba\\x1c\\xd6\\xc3{>+[\\x0f:[G:[us\\xdd\\x97i\\xdd\\x05\\xb2\\xf6Q\\xe8v\\x13W\\xd7@J.\\x00\\x96c\\xbdc\\x8f \\x08(\\x8e\\xf0\\x8d\\x05\\xbf\\xc8\\xcf\\xc6\\xd0|\\xd9\\xd7%\\x00\\xfcm>\\x86\\xc5\\x0e\\xf4\\x81\\xeb(\\xa3\\xa8\\x85\\xf5\\x96\\xf7\\x01E\\x18y%\\xbb\\x91\\xf7G\\xdfE\\tSq\\xaeD\\x9f\\\'\\x9e\\x1e\\xf9G\\xd1\\x18q\\x9b\\\'\\xbe\\xae\\xc8S\\xd6Om\\x9b\\xba\\x1e:w\\xf1\\xae6\\x1da\\xa1\\x87\\x08\\xe2%\\xacn-\\x11\"\\xbaXli\\x0b\\xdc\\xb4\\x1c\\xdc1\\x13E\"D{@\\x07+\\x88\\\\L\\x03\\xf5\\x11zP\\xf6\\x9b\\xfd+(Ch\\xdaH\\xf8k\\xc3vl\\x81q45\\x8bC\\xbd\\x19d\\xce-TNU\\x94\\xda@J\\xa8\\xae)U\\\'\\xf8\\x97)BOR\\xaf\\xa0\\xdb\\xf9\\xf5\\xe2]\\x9d\\x19$|\\xb4\\x03\\xc5\\x02R\\x95\\xfc\\xb8]\\x0b\\x15I\\x80\\xd8<<X\\x9fJ\\x0f\\xa2\\xed\'\np0\n."
    #@nonl
    #@-node:AGP.20230307095223.24:Prompt
    #@+node:AGP.20230307095223.25:Xcmd
    Xcmd_icon = "S\'x\\xda\\xcd\\x93\\xc1r\\xa30\\x0c\\x86\\xef\\xbcJ/\\x01\\x9a\\xd0\\x1cz\\xb0\\xc1\\x10C\\x81\\x05J\\x13\\xb8\\x81\\xc3\\xd8\\x0b\\x9e\\xe2\\x82\\x13\\xc0O_g{\\xd8\\x17\\xd8\\xc3j\\xe6\\x9b_\\xd6H\\xb2\\xc7#\\xe5;\\x1e\\xa4\\x1eg\\x08\\x80\\x0c\\xa4\\x15\\x00I{V\\xb2M\\x1f\\xac\\xd76\\xbd\\x13\\\'U\\xb3\\x93\\xae\\xe4\\xe2\\x9b\\xb3\\xe3\\xdf\\xb5\\xaa\\xf9p\\xbc\\xb7\\xfa<YG\\xd9\\x9c\\x8f\\xb6\\xd8\\xcc\\xbd(L\\xc39Xrj,)\\xeaM*QH\\xfb\\xcb\\xe2\\x9f\\xe1\\xc6e\\xb5q5\\x16\\xdc\\xfe:\\x13\\x1enD\\xd4\\x05\\x99\\xaa\\x8d\\xc8z+\\xfb\\xb0(9\\xde\\xe2\\xfet\\x8b\\xc5%\\x8du\\x1cu\\xf6\\r\\x19\\xfc\\x94\"q\\xb9\\xa1>\\xb8!Q\\xe5NgK\\x87\\x9d\\xa4Cl\\xa9\\x88\\x9d\\xa8NC,\\xa9X U\\xf7s\\xefT\\x99\\xe1\\xc4\\x83\\xa4\\xafL\\xd1w\\x1a\\xad\\xcd\\x03\\xe3\\xcc\\xc3\\xa6\\xd1N\\xc9\\xc3B\\xfbE9\\x88(\\x1b\\xc2H\\xab\\xabU\\x83\\x0fi?j\\xd0\\x1a\\x17\\x88aM\\x90\\x0fu\\x90\\x83\\xcc\\x05\\x14\\xbb\\xe0\\xaf\\x19\\xe0\\x1f\\xda\\x7f\\xda\\xcc]~\\x9a\\xfd\\x19\\x0b\\x00\\xf0\\xb4\\x00\\xdf\\x85+\\x9e#\\x08A&\\x9b\\x05RH_\\x12H3>\\xe6>\\xa4\\x00\\x07\\xa1G\\x8f\\xedG\\xe0R]\\x05\\xa1\\x07\"\\x0f\\xe4\\x85\\x88\\x8a\\x14\\xb2}e\\x88\\x18R\\x1c\\xc7\\x1e\\xed\\x8f\\x91\\xf9\\xa9\\x7f4\\xab|\\x98\\x8d\\xbb\\xbb\\x9bc\\x11\\xd3\\xc4\\xdd\\xb2\\\'\\x9d\\xd2d\\xbf\\xdf\\xa1W~\\x90\\xc3\\xa9\\xcf\\xc7h\\x08\\xd0\\xaef\\xfe\\xe8\\xaf\\xf8\\xb9\\xc1\\xfe;&A\\xbff\\x06\\x9a\\x0b\\xfd\\x8c\\xeb\\xf8\\xe21\\xbaC\\xf5/Lc\\xf6\\xe4\\xc3\\x9c\\xa0(wwQ\\xb4\\x87\\xacZ(AtH\\x0e\\xee\\t\\xb65~\\x03@1k\\x80eF\\x94\\x17\\xe2\\xf3\\xe7\\xc5e\\xac c\\x07\\x0c\\xa4\\xac7\\x0c\\xebg0_=\\xba\\x0c\\x11|,\\xc2\\xf2\\xfaj|\\x03\\x12!\\xf4\\x1d\'\np0\n."
    #@nonl
    #@-node:AGP.20230307095223.25:Xcmd
    #@-node:AGP.20230307095223.14:Icons
    #@+node:AGP.20230307095223.26:Colors
    ErrorColor = "#%02x%02x%02x" % (255,200,200)
    BreakColor = "#%02x%02x%02x" % (200,200,255)
    LineNumColor = "#%02x%02x%02x" % (200,200,255)
    RegExpFgColor = "#%02x%02x%02x" % (0,0,255)
    VarSupBgColor = "#%02x%02x%02x" % (255,230,230)
    #@nonl
    #@-node:AGP.20230307095223.26:Colors
    #@-others
    
    path_sym = "\\"
    
    LeoTop = None
    LeoFrame = None
    
    LeoBodyText = None
    LeoBodyParent = None
    LeoYBodyBar = None
    LeoXBodyBar = None
    
    HexView = None
    #@-node:AGP.20230307095223.13:<< globals >>
    #@nl

#@@language python
#@@tabwidth -4

__version__ = "0.5"

#@+others
#@+node:AGP.20230307095223.1:Documentation
#@+node:AGP.20230307095223.6:Known Flaws
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
#@-node:AGP.20230307095223.6:Known Flaws
#@+node:AGP.20230307095223.7:Future Features
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
#@-node:AGP.20230307095223.7:Future Features
#@+node:AGP.20230307095223.8:Tracing Problems
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
#@-node:AGP.20230307095223.8:Tracing Problems
#@+node:AGP.20230307095223.9:XCC Explanation
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
#@+node:AGP.20230307095223.10:The Three Distinctive Nodes
#@+at
# Amongst the members of the controllerclass, SELECTED_NODE, ACTIVE_NODE and 
# CHILD_NODE are some valuable and cherished companions. Hence they are great 
# clue of generale implement's stance. One who meddle with therein divine 
# matter is to make vigilant awareness of the nameless trinity.
#@-at
#@nonl
#@-node:AGP.20230307095223.10:The Three Distinctive Nodes
#@+node:AGP.20230307095223.11:The Parser
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
#@-node:AGP.20230307095223.11:The Parser
#@-node:AGP.20230307095223.9:XCC Explanation
#@-node:AGP.20230307095223.1:Documentation
#@+node:AGP.20230307095223.27:Module level
#@+node:AGP.20230307095223.28:init
def init ():
     

    #@    @+others
    #@-others
    
    data = (
        (("new","open2"), OnCreate),
        # ("start2",      OnStart2),
        ("select2",     OnSelect2),
        #("idle",        OnIdle),
        #("command2",    OnCommand2),
        #("bodydclick2", OnBodyDoubleClick),
        #("bodykey2",    OnBodyKey2),
        ("headkey2",    OnHeadKey2),
        #("end1",        OnQuit),
    )
    
    for hook,f in data:
        leoPlugins.registerHandler(hook,f)
        
    

    g.plugin_signon(__name__)

    return True



#@-node:AGP.20230307095223.28:init
#@+node:AGP.20230307095223.29:Module-level event handlers
#@+node:AGP.20230307101554:OnCreate
def OnCreate(tag,keywords):
    global LeoTop,LeoFrame,LeoBodyText,LeoBodyParent,LeoYBodyBar,LeoXBodyBar
    c = keywords.get('c')
    #@    @+others
    #@-others
#@nonl
#@-node:AGP.20230307101554:OnCreate
#@+node:AGP.20230307095223.32:OnSelect2
def OnSelect2(tag,keywords):
    global HexView
    c = keywords.get('c')
    p = c.currentPosition()
    
    if p.headString()[0:5] == "@bin ":
        print "bin node selected"
        
        LeoBodyText.pack_forget()
        LeoYBodyBar.pack_forget()
        LeoXBodyBar.pack_forget()
        if not HexView:
            HexView = Pmw.ScrolledText(LeoBodyParent,
                                        rowheader=1,
                                        columnheader=1,
                                        rowcolumnheader=1,
                                        rowheader_width = 8,
                                        rowcolumnheader_width = 3
                                        
                                        )
            HexView.component('columnheader').insert('0.0', " 0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  Dump")
            HexView.component('rowheader').insert('end', "00000000")
            HexView.component('rowheader').insert('end', "\n00000010")
            HexView.component('text').config(wrap=Tk.NONE)
        HexView.pack(fill="both",expand=1)
        
        return True
    else:
        if HexView:
            HexView.pack_forget()
        
        if LeoXBodyBar:
            LeoXBodyBar.pack(side="bottom",fill="x")
        if LeoYBodyBar:
            LeoYBodyBar.pack(side="right",fill="y")
        if LeoBodyText:
            LeoBodyText.pack(fill="both",expand=1)
        print "bin node unselected"
        return False
#@-node:AGP.20230307095223.32:OnSelect2
#@+node:AGP.20230307182804:OnCreate
def OnCreate(tag,keywords):
    try:
        c = keywords.get("c")
        if c:
            controllers [c] = controllerClass(c)
        
    except Exception:
        g.es_exception()
#@nonl
#@-node:AGP.20230307182804:OnCreate
#@+node:AGP.20230307095223.37:OnHeadKey2
def OnHeadKey2(tag,keywords):
    c = keywords.get("c")
        if c:
            controllers [c] = controllerClass(c)
            return controllers.get(c).onHeadKey2(keywords)
    
    
#@-node:AGP.20230307095223.37:OnHeadKey2
#@-node:AGP.20230307095223.29:Module-level event handlers
#@-node:AGP.20230307095223.27:Module level
#@+node:AGP.20230307182502:class controllerClass
class controllerClass:

    #@    @+others
    #@+node:AGP.20230307182502.1:__init__
    def __init__ (self,c):
        
        self.c = c
        
        self.current = None
        
        #Leo's Controls shortcut
        self.LeoTop = c
        self.LeoFrame = c.frame	
        self.LeoBodyText = self.LeoFrame.body.bodyCtrl
        self.LeoBodyParent = self.LeoBodyText.nametowidget(self.LeoBodyText.winfo_parent())
        self.LeoYBodyBar = self.LeoFrame.body.bodyBar
        self.LeoXBodyBar = self.LeoFrame.body.bodyXBar
        
        self.HexView = Pmw.ScrolledText(self.LeoBodyParent,
                                            rowheader=1,
                                            columnheader=1,
                                            rowcolumnheader=1,
                                            rowheader_width = 8,
                                            rowcolumnheader_width = 3
                                            
                                            )
                
        cheader = HexView.component('columnheader')
        cheader.insert('0.0', " 0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  Dump")
                
        rheader = HexView.component('rowheader')
        rheader.insert('end', "00000000")
        rheader.insert('end', "\n00000010")
                
        self.HexView.component('text').config(wrap=Tk.NONE)
        
        self.HexView.pack(fill="both",expand=1)
    #@nonl
    #@-node:AGP.20230307182502.1:__init__
    #@+node:AGP.20230307182502.12:Event handlers
    #@+node:AGP.20230307182502.13:onSelect
    def onSelect(self):
        p = self.c.currentPosition()
        
        next = p
        if not IsAtBin(next):#child bin
            next = self.GetParentBin(next)
                 
        
                
    
        if next:
            if not self.current:
                self.ShowHexedit()
                
            self.current = next
        
        else:
            if self.current:
                self.ShowHexedit()
                    
            self.current = None
            
    #@-node:AGP.20230307182502.13:onSelect
    #@+node:AGP.20230307182502.15:onCommand2
    def onCommand2(self,keywords):
        cc = self
        label = keywords.get("label")
        if label in ["undo","redo","backward-delete-char","delete-char","cut-text","paste-text"]:
            if cc.SELECTED_NODE:
                cc.BreakBar.bodychanged = True
    #@nonl
    #@-node:AGP.20230307182502.15:onCommand2
    #@+node:AGP.20230307182502.18:onHeadKey2
    def onHeadKey2(self,keywords):    
        cc = self
        p = cc.c.currentPosition()
        
        
        c = keywords.get('c')
        p = c.currentPosition()
    
        if p.headString()[0:5] == "@bin ":
            print "bin node selected"
            return True
        else:
            print "bin node unselected"
            return False
            
        
        if IsAtBin(p):
            
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
    #@-node:AGP.20230307182502.18:onHeadKey2
    #@-node:AGP.20230307182502.12:Event handlers
    #@+node:AGP.20230307185825:GetParentBin()
    def GetParentBin(self,node):
        for p in node.parents_iter():
    		h = p.headString()
    		if h[0:5] == "@bin ":
    			return p
    	
    	return None
    #@nonl
    #@-node:AGP.20230307185825:GetParentBin()
    #@+node:AGP.20230307185825.1:IsAtBin()
    def IsAtBin(self,p):
        if p.headString()[0:5] == "@bin ":
            return True
            
        return False
    #@-node:AGP.20230307185825.1:IsAtBin()
    #@+node:AGP.20230307185825.2:ShowHexed()
    def ShowBody(self):
        global HexView
        c = keywords.get('c')
        p = c.currentPosition()
        
        self.LeoBodyText.pack_forget()
        self.LeoYBodyBar.pack_forget()
        self.LeoXBodyBar.pack_forget()
        
            
    #@-node:AGP.20230307185825.2:ShowHexed()
    #@+node:AGP.20230307185825.3:HideHexed()
    def HideHexed(self):
        self.HexView.pack_forget()
            
        self.LeoXBodyBar.pack(side="bottom",fill="x")
        self.LeoYBodyBar.pack(side="right",fill="y")
        self.LeoBodyText.pack(fill="both",expand=1)
        
    #@-node:AGP.20230307185825.3:HideHexed()
    #@-others
#@nonl
#@-node:AGP.20230307182502:class controllerClass
#@-others
#@nonl
#@-node:AGP.20230307095223:@thin bin_nodes.py
#@-leo
