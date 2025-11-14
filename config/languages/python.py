#@+leo-ver=4
#@+node:@file languages/python.py
#alias = ("py","py2")

from string import whitespace,ascii_letters,digits

USE_BLOCKSTRING = True
LINE_ESCAPE = None

DIRECTIVE_START = None

STRING_DELIMS = "\"'"

COMMENT_START = "#"

BLOCK_COMMENT_START = None
BLOCK_COMMENT_END = None

VALID_NAME_CHARS = ascii_letters + digits + "_"
VALID_NAME_START_CHARS = ascii_letters + "_"

keywords = [
    "and",       "del",       "for",       "is",        "raise",    
    "assert",    "elif",      "from",      "lambda",    "return",   
    "break",     "else",      "global",    "not",       "try",      
    "class",     "except",    "if",        "or",        "yield",   
    "continue",  "exec",      "import",    "pass",      "while",
    "def",       "finally",   "in",        "print"]
    
#@-node:@file languages/python.py
#@-leo
