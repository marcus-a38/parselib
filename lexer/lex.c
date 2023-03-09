#define LEXERERROR do { \
    printf("Error lexing."); \
    exit(1); \
} while (0) // for readability

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <regex.h>
#include "definitions.h" // header file with token type definitions
#include "typematch.c" // create types for the tokens

/*
    original author: marcus antonelli
    author github: github.com/marcus-a38
    project title: parselib
    to be: converted to a .so file
    WARNING: HIGHLY EXPERIMENTAL. DO NOT USE.

*/

Token* createToken(const char* type, const char* value) { // called everytime a substr is split
    Token* token = malloc(sizeof(Token));
    token->type = strdup(type);
    token->value = strdup(value);
    return token;
}


void freeToken(Token* token) { // self explanatory
    free(token->type);
    free(token->value);
    free(token);
}


Token** lexerTokenize(const char* input, int* numTokens){

    int count = 0, i = 0, regexTemp = 0;
    const char* tokenString = input;
    const int max_matches = 100; 
    const char* pattern = "[^[:space:]]+"; // this needs to be CHANGED. This is just for testing basic tokenization.

    regex_t regex;
    regmatch_t matches[max_matches];
    

// compile the regular expression

    regexTemp = regcomp(&regex, pattern, REG_EXTENDED);

    if (regexTemp != 0){
        LEXERERROR;
    }
    
// get number of tokens so we can initialize an array of tokens

    regexTemp = regexec(&regex, tokenString, max_matches, matches, 0);

    while (regexTemp == 0) {
        count++;
        tokenString += matches[0].rm_eo;
        regexTemp = regexec(&regex, tokenString, max_matches, matches, 0);
    }

// tokenize & append to token array

    Token** tokenList = malloc(count * sizeof(Token*));
    tokenString = strdup(input);
    regexTemp = regexec(&regex, tokenString, max_matches, matches, 0);

    while (regexTemp == 0) {

        int length = matches[0].rm_eo - matches[0].rm_so; // get length of substr (end - beginning)
        char* lexToken = strndup(tokenString + matches[0].rm_so, length); // duplicate substring

        tokenList[i] = createToken("NONE", lexToken);

        tokenString += matches[0].rm_eo;
        regexTemp = regexec(&regex, tokenString, max_matches, matches, 0);
        i++;

    }

    *numTokens = count;
    regfree(&regex);
    return tokenList;

}
