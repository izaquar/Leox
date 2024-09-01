#@+leo-ver=4-thin
#@+node:danr7.20060902215215.1:@thin leo_to_html.py
#@@language python
#@@tabwidth -4

#@<< docstring >>
#@+node:danr7.20060902215215.2:<< docstring >>
'''leoToHTML 1.0 plugin by Dan Rahmel, bullet list code by Mike Crowe.

This plugin takes an outline stored in LEO and outputs it as an HTML file. The outline
is output as either a set of headings or an unordered list.

If this plug-in loads properly, you should have an "Outline to HTML"
option added to your File > Export... menu in Leo.

Settings such as outputing just the headlines (vs. headlines & body text) and whether
to include or ignore the contents of @file nodes are stored in the html_export.ini file
in your Leo\plugins folder.

The default export path is also stored in the INI file. By default, it's set to c:\ so
you may need to modify it depending on your system.


'''
#@-node:danr7.20060902215215.2:<< docstring >>
#@nl
#@<< version history >>
#@+node:danr7.20060902215215.3:<< version history >>
#@@killcolor
#@+at
# 
# 1.00 - Finished testing with 4 different options & outlines
# 0.91 - Got initial headline export code working. Resolved bug in INI file 
# checking
# 0.90 - Created initial plug-in framework
#@-at
#@nonl
#@-node:danr7.20060902215215.3:<< version history >>
#@nl
#@<< imports >>
#@+node:danr7.20060902215215.4:<< imports >>
import leoGlobals as g
import leoPlugins
import ConfigParser
import tkMessageBox

#@-node:danr7.20060902215215.4:<< imports >>
#@nl

__version__ = "1.0"

#@+others
#@+node:danr7.20060902215215.5:createExportMenu
def createExportMenu (tag,keywords):

    c = keywords.get("c")

    # Get reference to current File > Export... menu
    exportMenu = c.frame.menu.getMenu('Export...')
    # Insert leoToRTF in #3 position of the File > Export menu.  
    exportMenu.insert(3,'command',label='Outline to HTML',command= lambda c = c : export_html(c))
#@-node:danr7.20060902215215.5:createExportMenu
#@+node:danr7.20060902215215.6:export_html
def export_html( c ):
    # Show messagebox to ask if headline output or bullet list
    
    if g.app.unitTesting:
        flagHeadings = True
    else:
        flagHeadings = tkMessageBox.askyesno(
            "askyesno", "Save outline as HTML headings? \n(No will save outline as bullet list)")

    g.es("Exporting HTML...")

    # Get user preferences from INI file 
    fileName = g.os_path_join(g.app.loadDir,"../","plugins","leo_to_html.ini")
    config = ConfigParser.ConfigParser()
    config.read(fileName)
    flagIgnoreFiles =  config.get("Main", "flagIgnoreFiles") == "Yes"
    flagJustHeadlines = config.get("Main", "flagJustHeadlines") == "Yes"
    filePath = config.get("Main", "exportPath").strip() # "c:\\"
    
    myFileName = c.frame.shortFileName()    # Get current outline filename
    myFileName = myFileName[:-4]            # Remove .leo suffix
    
    g.es(" Leo -> HTML started...",color="turquoise4")
    
    # Open file for output
    f=open(filePath + myFileName + ".html", 'w')
    
    # Write HTML header information
    f.write("<HTML>")
    f.write("<BODY>")

    myLevel = -1
    for p in c.allNodes_iter():
        curLevel = p.level() + 1    # Store current level
        if curLevel <> myLevel and not flagHeadings:
            if curLevel > myLevel:
                f.write("<ul>\n")   # If level is greater, open new UL
            else:
                f.write("</ul>\n"*(myLevel-curLevel))   # If level is less, close ULs to reach current level
                
        myLevel = curLevel
        myHeadline = p.headString()
       
        # Check if node is an @file and ignore if configured to
        if not (myHeadline[:5] == "@file" and flagIgnoreFiles):
            myOutput = myHeadline
            myOutput = myOutput.encode( "utf-8" )   # Encode to html standard output
            # If writing file as heading list, do that. Otherwise, write the bullet list items
            if flagHeadings:
                f.write("<H" + str(myLevel) + ">" + myOutput + "</H" + str(myLevel) + ">")
            else:
                f.write("<li><H" + str(myLevel) + ">" + myOutput + "</H" + str(myLevel) + "></li>")
                

            # If including outline body text, convert it to HTML usable format
            if not flagJustHeadlines:
                myBody = p.bodyString().encode( "utf-8" )
                # Insert line breaks where newline characters were 
                myBody = myBody.rstrip().replace("\n","<br>\n")
                # Make sure there is body text before writing
                if len(myBody)>0: 
                    if flagHeadings:
                        f.write("<p>" + myBody)
                    else:
                        f.write("<ul><li>" + myBody + "</li></ul>\n")  
    
    # Write final level closes
    if not flagHeadings:
        f.write("</ul>\n"*(myLevel))
    
    # Write HTML close
    f.write("</BODY></HTML>")  
    
    # Close file
    f.close()
    g.es(" Leo -> HTML completed.",color="turquoise4")
    
#@nonl
#@-node:danr7.20060902215215.6:export_html
#@-others

if 1: # Ok for unit testing: creates menu.
    leoPlugins.registerHandler("create-optional-menus",createExportMenu)
    g.plugin_signon(__name__)
#@nonl
#@-node:danr7.20060902215215.1:@thin leo_to_html.py
#@-leo
