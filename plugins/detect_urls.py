#@+leo-ver=4-thin
#@+node:ekr.20060506070443.1:@thin detect_urls.py
#@<< docstring >>
#@+node:vpe.20060426084738:<< docstring >>
"""
Colorizes URLs everywhere in node's body on node selection. 
Double click on any URL launches it in default browser.

URL regex:  (http|https|ftp)://[^\s'"]+[\w=/]

Related plugins:  color_markup.py; rClick.py
"""
#@nonl
#@-node:vpe.20060426084738:<< docstring >>
#@nl
#@@language python
#@@tabwidth -4
import leoGlobals as g
import leoPlugins
import re
url_regex = re.compile(r"""(http|https|ftp)://[^\s'"]+[\w=/]""")

#@+others
#@+node:vpe.20060305064323.5:openURL()
def openURL(tag,keywords):
    c = keywords.get("c")
    row,col = c.frame.body.getInsertionPoint().split(".") # cursor position
    line = c.frame.body.getTextRange("%s.0" %row, "%s.end" %row) # current line
    
    for match in url_regex.finditer(line):
        if ( match.start() < int(col) < match.end() ):
            url = match.group()
            start, end = match.start(), match.end()
            c.frame.body.setTextSelection("%s.%s" %(row,start), "%s.%s" %(row,end))
            try:
                import webbrowser
                webbrowser.open(url)
            except:
                g.es("exception opening " + url)
                g.es_exception()
            return 1 # force to skip word selection if url found
#@-node:vpe.20060305064323.5:openURL()
#@+node:vpe.20060426062042:colorizeURLs()
def colorizeURLs(tag,keywords):
    c = keywords.get("c")
    c.frame.body.tag_configure("URL", underline=1, foreground="blue")
    
    lines = c.frame.body.getTextRange("1.0","end").split("\n")
    row=1
    for line in lines:
        for match in url_regex.finditer(line):
            start, end = match.start(), match.end()
            c.frame.body.tag_add("URL", "%s.%s" %(row,start), "%s.%s" %(row,end))
        row+=1
#@-node:vpe.20060426062042:colorizeURLs()
#@-others

if 1:
    leoPlugins.registerHandler("bodydclick1", openURL)
    leoPlugins.registerHandler("select2", colorizeURLs)
    g.plugin_signon(__name__)
#@-node:ekr.20060506070443.1:@thin detect_urls.py
#@-leo
