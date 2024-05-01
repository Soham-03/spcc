#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Define a structure to hold symbol table entries
typedef struct {
    char symbol[10];
    int address;
} SymbolTableEntry;

// Global symbol table array and counter
SymbolTableEntry symbolTable[100];
int symbolCount = 0;

// Function to add a symbol to the symbol table
void addSymbol(const char* symbol, int address) {
    if (symbolCount < 100) {  // Check to prevent overflow of the symbol table
        strncpy(symbolTable[symbolCount].symbol, symbol, sizeof(symbolTable[symbolCount].symbol) - 1);
        symbolTable[symbolCount].symbol[sizeof(symbolTable[symbolCount].symbol) - 1] = '\0';  // Null-terminate
        symbolTable[symbolCount].address = address;
        symbolCount++;
    }
}

// Main function
int main() {
    // Example assembly input, split by lines
    char* assemblyProgram[] = {
        "PG1 START 0",
        "** USING *,15",
        "** L 1,FIVE",
        "** A 1,FOUR",
        "** ST 1,TEMP",
        "FIVE DC F'5'",
        "FOUR DC F'4'",
        "TEMP DS 1F",
        "** END PG1"
    };
    int numLines = sizeof(assemblyProgram) / sizeof(assemblyProgram[0]);

    int locationCounter = 0;
    char buffer[50];  // Buffer to safely manipulate strings

    // Process each line of the assembly program
    for (int i = 0; i < numLines; i++) {
        strcpy(buffer, assemblyProgram[i]);  // Use buffer to avoid modifying original strings
        char* token = strtok(buffer, " ");  // Get the first token
        if (token != NULL && token[0] != '*') {  // Check if line is a comment
            char symbol[10];
            strncpy(symbol, token, sizeof(symbol) - 1);
            symbol[sizeof(symbol) - 1] = '\0';  // Null-terminate

            token = strtok(NULL, " ");  // Get the next token
            if (token != NULL) {
                if (strcmp(token, "START") == 0) {
                    token = strtok(NULL, " ");
                    locationCounter = atoi(token);
                    addSymbol(symbol, locationCounter);
                } else if (strcmp(token, "DC") == 0) {
                    addSymbol(symbol, locationCounter);
                    locationCounter += 4;  // Assume 4 bytes for DC
                } else if (strcmp(token, "DS") == 0) {
                    addSymbol(symbol, locationCounter);
                    locationCounter += 4;  // Assume 4 bytes for DS
                } else if (strcmp(token, "A") == 0) {
                    locationCounter += 5;  // Size for A
                } else if (strcmp(token, "L") == 0) {
                    locationCounter += 6;  // Size for L
                } else if (strcmp(token, "ST") == 0) {
                    locationCounter += 7;  // Size for ST
                }
            }
        }
    }

    // Print the symbol table
    printf("Symbol Table:\n");
    printf("Symbol   Address\n");
    for (int i = 0; i < symbolCount; i++) {
        printf("%-6s   %04X\n", symbolTable[i].symbol, symbolTable[i].address);
    }

    return 0;
}
