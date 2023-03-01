# Hello! Thank you for checking out ParseLib. 

### License Information

1. Permissions: Commercial and private Use, non-conditional modification, and distribution with stipulations.
2. Stipulations: Distributed versions must be open-source, identical license must reside in source code, documented changes

NOTICE: This license limits liability and does ***not*** provide any warranty. You may read the license in LICENSE.txt.

---

### Table of Contents

| Title               |  Section  |
|---------------------|-----------|
|   Introduction      |     I     |
|  Defining "Types"   |    II     |

---

### Introduction

Thanks again for checking out parselib. This is an incomplete, early development project authored by Marcus Antonelli.
This project employs basic Pythonic logic to execute straightforward lexing, parsing, and interpreting with some string or list.

Parselib consists of a few interconnected modules, with support for syntaxed and formatted documents formed with token info.
Some of the modules may be implemented standalone, but would require heavylifting to loosen the dependency on other modules.

And finally, here are some basic summarizations for the lingo being thrown around:

1. Lexer: a program that converts a sequence of characters into a sequence of contextualized tokens. This process is called lexing or tokenization.

2. Parser: a program that analyzes strings (tokens) and matches the input to local syntax or grammar. In doing so, a syntax tree is created.

3. Interpreter: a program that interprets the parser's syntax tree (or abstract syntax tree; AST.) This executes each expression's assigned behavior.

4. Token: a string with assigned meaning (in this case, an object with assigned attributes)
___
### Defining "Types"

1. Operators
   - e.g. +, -, *, /
   
2. Delimiters
   - e.g. (), [], {}
   
3. Keywords
   - e.g. True, if, return
   
4. Values
   - e.g. "hello", 2, 6.3 --> string, int, float
  
Since Python documentation refers to boolean operators as keywords, type 'operator' will only be assigned to mathematical operators. Boolean operators will be instead listed under type 'keyword'. This may or may not be important dependent on the application.

---

TO BE CONTINUED ...

