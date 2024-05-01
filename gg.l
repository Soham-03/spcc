%{
#include <stdio.h>
int newlines = 0, spaces = 0, words = 0;
%}

%%
\n      { ++newlines; }
[ \t]+  { ++spaces; }
[a-zA-Z]+ { ++words; }
.       { /* ignore other characters */ }
%%

int main(int argc, char **argv)
{
    yylex();
    printf("Newlines: %d\n", newlines);
    printf("Spaces: %d\n", spaces);
    printf("Words: %d\n", words);
    return 0;
}

int yywrap()
{
    return 1;
}