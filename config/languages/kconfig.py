#@+leo-ver=4
#@+node:@file languages/kconfig.py
#alias = None

from string import whitespace,ascii_letters,digits

USE_BLOCKSTRING = False
LINE_ESCAPE = None

DIRECTIVE_START = None

STRING_DELIMS = "\""

COMMENT_START = "#"

BLOCK_COMMENT_START = None
BLOCK_COMMENT_END = None

VALID_NAME_CHARS = ascii_letters + digits + "_"
VALID_NAME_START_CHARS = ascii_letters + "_"

keywords = [
    "bool",
"choice",
"config",
"default",
"depend on",
"endchoice",
"endif",
"endmenu",
"help",
"if"
"imply",
"int",
"mainmenu",
"menu",
"menuconfig",
"n",
"prompt",
"select",
"source",
"string",
"tristate"
"y",
    ]
#@-node:@file languages/kconfig.py
#@-leo
