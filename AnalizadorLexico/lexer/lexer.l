%{
#include <stdio.h>
#include <string.h>

// Lista de palabras clave
const char* keywords[] = {
    "auto", "break", "case", "char", "const", "continue", "default",
    "do", "double", "else", "enum", "extern", "float", "for",
    "goto", "if", "int", "signed", "sizeof", "static", "struct",
    "switch", "typedef", "union", "unsigned", "void", "volatile", "while",
    NULL
};

// Función para verificar si un token es una palabra clave
int is_keyword(const char* token) {
    for (int i = 0; keywords[i] != NULL; ++i) {
        if (strcmp(keywords[i], token) == 0) {
            return 1;
        }
    }
    return 0;
}
%}

%%

[0-9]+         { printf("NUMBER: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]* {
    if (is_keyword(yytext)) {
        printf("PALABRA RESERVADA: %s\n", yytext);
    } else {
        printf("IDENTIFICADOR: %s\n", yytext);
    }
}
[%-*+=/@$#!<>]        { printf("OPERADOR: %s\n", yytext); }
[\(\)\[\]\{\};,]  { printf("SEPARADOR: %s\n", yytext); }
\"([^\\\"]|\\.)*\" { printf("STRING_LITERAL: %s\n", yytext); }
\n              { /* Ignorar líneas nuevas */ }
[ \t]+         { /* Ignorar espacios y tabulaciones */ }
.               { printf("UNKNOWN: %s\n", yytext); }


%%

int main(int argc, char **argv) {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
