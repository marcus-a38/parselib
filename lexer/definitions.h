#ifndef DEFINITIONS_H
#define DEFINITIONS_H

// Identifiers
#define IDENTIFIER "IDENTIFIER"
#define STRING "STRING"
#define INTEGER "INTEGER"
#define FLOAT "FLOAT"
#define BOOLEAN "BOOLEAN"
#define NULLTYPE "NULL"

// Keywords
#define AND "AND"
#define OR "OR"
#define NOT "NOT"
#define IF "IF"
#define ELSE "ELSE"
#define ELIF "ELIF"
#define WHILE "WHILE"
#define FOR "FOR"
#define IN "IN"
#define RANGE "RANGE"
#define BREAK "BREAK"
#define CONTINUE "CONTINUE"
#define DEF "DEF"
#define RETURN "RETURN"
#define CLASS "CLASS"
#define TRUE "TRUE"
#define FALSE "FALSE"

// Symbols
#define POUND "#"
#define PLUS "+"  
#define MINUS "-"
#define ASTERICK "*"
#define FSLASH "/"
#define LEFT_PARENTH "("
#define RIGHT_PARENTH ")"
#define LEFT_BRACE "{"
#define RIGHT_BRACE "}"
#define LEFT_BRACKET "["
#define RIGHT_BRACKET "]"
#define COMMA "," 
#define DOT "."
#define SEMICOLON ";"  
#define COLON ":"
#define EQUIVALENT "=="
#define EQUAL "="  
#define LESSER "<"  
#define GREATER ">"  
#define LESS_EQUAL "<="  
#define GREAT_EQUAL ">="  
#define NOT_EQUAL "!=" 
#define ADDEQUAL "+="  
#define SUBEQUAL "-="  
#define INCREMENT "++"  
#define DECREMENT "--" 
#define LEFT_DELIM "{[(" 
#define RIGHT_DELIM "}])" 

// Other
#define EOF "EOF"
#define PACKAGE "PACKAGE"
#define COMMENT "COMMENT"
#define DEFINITION "DEFINITION"
#define EXPRESSION "EXPRESSION"
#define ATTRIBUTE "ATTRIBUTE"
#define FUNCTION "FUNCTION"
#define CLASS "CLASS"
#define OBJECT "OBJECT"

// Define Token type
typedef struct Token {
  char* value;
  char* type;
} Token;

#endif
