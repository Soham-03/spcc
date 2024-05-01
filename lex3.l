%{
    #include<stdio.h>
    int identifiers = 0, constants = 0, operators=0, specialsym = 0;
%}

%%
[a-zA-Z_]+[a-zA-Z0-9_]* {++identifiers;}
[0-9]+ {++constants;}
"+"|"-"|"*"|"/"|"++"|"--"|"+="|"-=" {++operators;}
";"|","|"("|")"|"{"|"}" {++specialsym;}
%%

int main(){
    yylex();
    printf("Identifiers: %d\n", identifiers);
    printf("Constants: %d\n", constants);
    printf("Operators: %d\n", operators);
    printf("Special Symbols: %d\n", specialsym);
    return 0;
}

int yywrap(){
    return 1;
}