#######################################################
##   PPP   AAAA  RRR   SSSS  EEEE  L     III  BBB    ##    
##   P  P  A  A  R  R  S     E     L      I   B  B   ##
##   PPP   AAAA  RRR   SSSS  EEEE  L      I   BBB    ##
##   P     A  A  R  R     S  E     L      I   B  B   ##
##   P     A  A  R  R  SSSS  EEEE  LLLL  III  BBB    ##
#######################################################

author = 'marcus-a38'
author_email = 'marcus.a38@gmail.com'
project_version = '0.0.1'

####################### INIT ##########################


# every possible python keyword, used primarily to interpret tokens

# | | | | | | | | | | | | | | | | | | | | 
# v v v v v v v v v v v v v v v v v v v v

keys = {

'keyTrue' : r'True',
'keyFalse' : r'False',
'keyNone' : r'None',
'keyAnd' : r'and' ,
'keyAs' : r'as',
'keyAssert' : r'assert',
'keyAsync' : r'async',
'keyAwait' : r'await',
'keyBreak' : r'break',
'keyClass' : r'class',
'keyContinue' : r'continue',
'keyDef' : r'def',
'keyDel' : r'del',
'keyElif' : r'elif',
'keyElse' : r'else',
'keyExcept' : r'except',
'keyFinally' : r'finally',
'keyFor' : r'for',
'keyFrom' : r'from',
'keyGlobal' : r'global',
'keyIf' : r'if',
'keyImport' : r'import',
'keyIn' : r'in',
'keyIs' : r'is',
'keyLambda' : r'lambda',
'keyNonlocal' : r'nonlocal',
'keyNot' : r'not',
'keyOr' : r'or',
'keyPass' : r'pass',
'keyRaise' : r'raise',
'keyReturn' : r'return',
'keyTry' : r'try',
'keyWhile' : r'while',
'keyWith' : r'with',
'keyYield' : r'yield'

}

# all mathematical operators

operators = {

'add' : r'+',
'sub' : r'-',
'mul' : r'*',
'div' : r'//',
'tdiv' : r'/',
'mod' : r'%',
'exp' : r'**'

}


# Every possible tag that can be formed when parsing a token. 
# open delimiters (i.e open parentheses or open bracket) are 
# distinguished from closed delimiters to allow for expression
# 'defragmentation.'

# | | | | | | | | | | | | | | | | | | | | 
# v v v v v v v v v v v v v v v v v v v v

tag_types = {

1 : 'variable', 
2 : 'keyword', 
3 : 'open_d', 
4 : 'close_d', 
5 : 'operator', 
6 : 'value', 
7 : 'comment'

}

