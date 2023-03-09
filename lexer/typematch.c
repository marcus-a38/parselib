#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <regex.h>
#include "definitions.h"

/* . HIGHLY EXPERIMENTAL . NOT COMPLETE AT ALL . DO NOT USE .*/


void determineType(Token* token) { // checks all variable assignment Tokens for type

    char* tokenValue = token->value;
    regex_t regex;
    int ret;

   ret = regcomp(&regex, "^\".*\"$", REG_NOSUB); // match string literal enclosed in ""
    if (ret == 0 && regexec(&regex, tokenValue, 0, NULL, 0) == 0) {
        token->type = STRING;
        regfree(&regex);
        return;
    }
    regfree(&regex);


    ret = regcomp(&regex, "^[-+]?[0-9]*\\.?[0-9]+([eE][-+]?[0-9]+)?$", REG_NOSUB); // match floats various formats
    if (ret == 0 && regexec(&regex, tokenValue, 0, NULL, 0) == 0) {
        token->type = FLOAT;
        regfree(&regex);
        return;
    }
    regfree(&regex);


    ret = regcomp(&regex, "^[-+]?[0-9]+$", REG_NOSUB); // match negative or positive int
    if (ret == 0 && regexec(&regex, tokenValue, 0, NULL, 0) == 0) {
        token->type = INT;
        regfree(&regex);
        return;
    }
    regfree(&regex);


    ret = regcomp(&regex, "^[a-zA-Z_][a-zA-Z0-9_]*$", REG_NOSUB); // match ASCII characters -- variable
    if (ret == 0 && regexec(&regex, tokenValue, 0, NULL, 0) == 0) {
        token->type = IDENTIFIER;
        regfree(&regex);
        return;
    }
    regfree(&regex);

    /* TO ADD:  MATCH NULL VALUES,  MATCH BOOLEAN TRUE FALSE*/
    
}

void createTag(Token* token, char* type) {

    char* tempTokenType;

    // utilizing a conditional ladder to set token type. this'll be long lol

    if (strcasecmp("SOME_TOKEN_TEXT", tempTokenType)) {
      token->type = SOME_TOKEN_TYPE;
    }
    else if (strcasecmp("SOME_TOKEN_TEXT", tempTokenType)) {
        token->type = SOME_TOKEN_TYPE;
    }

    token->type = type;
    
}