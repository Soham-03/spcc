%{
    #include<stdio.h>
    int operators = 0, operands = 0;
%}

%%
"+"|"-"|"*"|"/"|"++"|"--"|"=="|"+="|"-=" {++operators;}
[0-9]+ {++operands;}
[a-zA-Z_]+[a-zA-Z0-9]* {++operands;}
[ \t\n]+ {}
. {}
%%

int main(){
    yylex();
    printf("Number of operators: %d\n", operators);
    printf("Number of operands: %d\n", operands);
    return 0;
}

int yywrap(){
    return 1;
}

