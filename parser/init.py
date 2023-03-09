author = 'marcus-a38'
author_email = 'marcus.a38@gmail.com'
project_version = '0.0.1a'

#___________________________________________________________#
#                                                           #
# this is basically a copy of definitions.h for the parser! #
#___________________________________________________________#


# Identifiers
IDENTIFIER = "IDENTIFIER"
STRING = "STRING"
INTEGER = "INTEGER"
FLOAT = "FLOAT"
BOOLEAN = "BOOLEAN"
NULL = "NULL"

# Keywords
AND = "AND"
OR = "OR"
NOT = "NOT"
IF = "IF"
ELSE = "ELSE"
ELIF = "ELIF"
WHILE = "WHILE"
FOR = "FOR"
IN = "IN"
RANGE = "RANGE"
BREAK = "BREAK"
CONTINUE = "CONTINUE"
DEF = "DEF"
RETURN = "RETURN"
CLASS = "CLASS"
TRUE = "TRUE"
FALSE = "FALSE"

# Delimiters
LDELIM = "{[("
RDELIM = "}])"

# Other
EOF = "EOF"
PACKAGE = "PACKAGE"
COMMENT = "COMMENT"
EXPRESSION = "EXPRESSION"
ATTRIBUTE = "ATTRIBUTE"
FUNCTION = "FUNCTION"
CLASS = "CLASS"
OBJECT = "OBJECT"

# Symbols
SYMBOLS = {
    "#" : "POUND",
    "+" : "PLUS",
    "-" : "MINUS",
    "*" : "ASTERICK",
    "/" : "SLASH",
    "(" : "LEFT_PARENTH",
    ")" : "RIGHT_PARENTH",
    "{" : "LEFT_BRACE",
    "}" : "RIGHT_BRACE",
    "[" : "LEFT_BRACKET",
    "]" : "RIGHT_BRACKET",
    "," : "COMMA",
    "." : "DOT",
    ";" : "SEMICOLON",  
    ":" : "COLON",
    "==": "EQUIVALENT",
    "=" : "EQUAL",
    "<" : "LESSER",
    ">" : "GREATER",
    "<=" : "LESS_EQUAL",
    ">=" : "GREAT_EQUAL",
    "!=" : "NOT_EQUAL",
    "+=" : "ADDEQUAL",
    "-=" : "SUBEQUAL",
    "++" : "INCREMENT",
    "--" : "DECREMENT",
    "{[(" : "LEFT_DELIM",
    "}])" : "RIGHT_DELIM",
}