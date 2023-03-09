# Hello! Thank you for checking out ParseLib. 

### License Information

1. Permissions: Commercial and private Use, non-conditional modification, and distribution with stipulations.
2. Stipulations: Distributed versions must be open-source, identical license must reside in source code, documented changes

NOTICE: This license limits liability and does ***not*** provide any warranty. You may read the license in LICENSE.txt.

___

### Table of Contents
---
| Title               |  Section  |
|---------------------|-----------|
|   Introduction      |     I     |
|  Defining "Types"   |    II     |
|  Parsing and ASTs   |    III    |
___

### Introduction
---
Thanks again for checking out parselib! This is a pre-release interpreter package authored by Marcus Antonelli. The lexing/tokenization is executed using C, and the parsing/interpreting is executed in Python. The code is currently **not** functional, but collaboration is always welcome.

NOT YET INCLUDED: Within the package you'll also find a small UI module named "makefile," which can be used as a customizable code editor for microlanguage programming. This module is dependent on the lexer and parser module, so make sure not to separate the two. If you do, you will have to reprogram a large chunk of the logic. (A section and proper documentation will be written on this module later.)

And finally, here are some basic definitions for the terms you'll see mentioned:

1. **Token**: a string with *assigned meaning* (in this case, an object with assigned value & type)

2. **Lexer**: a program that converts a sequence of characters into a sequence of contextualized tokens. This process is called *lexing* or *tokenization*.

3. **Parser**: a program that analyzes strings (tokens) and matches the input to local syntax or grammar. In doing so, an **abstract syntax tree (AST)** is created.

4. **Interpreter**: a program that *interprets* the parser's AST. This executes each expression's assigned behavior by traversing a binary tree in order.

___

### Defining "Types"
---
1. Operators
   - e.g. +, -, *, /
   
2. Delimiters
   - e.g. (), [], {}
   
3. Keywords
   - e.g. True, if, return
   
4. Values
   - e.g. "hello", 2, 6.3 --> string, int, float

Using a regular expression, the lexer will split raw input into tokens. These tokens will be assigned a primitive 'value' and 'type.' The types will be determined through comparison using a large set of predefined & user-defined keywords, operators, etc. 

As this chunk of the code requires a time complexity of O(n), we'll be processing it in C. This is to avoid performance issues that will get progressively worse in Python versus C. After preprocessing the tokens, we will pass them to the parser module to add defined behavior and an execution order for the interpreter (via ASTs)

___

### Parsing and ASTs

......