# Assembler First Pass to Generate a Symbol Table

# Define the input for the assembler
assembly_program = [
    "PG1 START 0",
    "** USING *,15",
    "** L 1,FIVE",
    "** A 1,FOUR",
    "** ST 1,TEMP",
    "FIVE DC F'5'",
    "FOUR DC F'4'",
    "TEMP DS 1F",
    "** END PG1"
]

# Define the Machine Operation Table (MOT) with opcode and their size
MOT = {
    "A": 5,  # 'A' instruction size
    "L": 6,  # 'L' instruction size
    "ST": 7  # 'ST' instruction size
}

# Pseudo Operation Table (POT) with operation and their assumed sizes
POT = {
    "START": 0,
    "DC": 4,   # Assuming 'F' format occupies 4 bytes
    "DS": 4,   # Assuming '1F' format occupies 4 bytes
    "END": 0
}

# Initialize the location counter
location_counter = 0

# Symbol table to store symbols and their addresses
symbol_table = {}

# Process each line in the assembly program
for line in assembly_program:
    tokens = line.split()  # Split the line into tokens
    label = tokens[0]  # The first token might be a label
    
    # Check if line contains a label and an instruction/directive
    if len(tokens) > 1:
        directive_or_instruction = tokens[1]
    else:
        directive_or_instruction = ""

    # Update the location counter for START directive
    if directive_or_instruction == "START":
        location_counter = int(tokens[2])  # Set location counter to the specified start address
        symbol_table[label] = format(location_counter, '04X')  # Add to symbol table
    elif directive_or_instruction in MOT:
        # If the directive is an operation, update location based on MOT size
        location_counter += MOT[directive_or_instruction]
    elif directive_or_instruction in POT:
        if label != "**":
            symbol_table[label] = format(location_counter, '04X')  # Add to symbol table
        # Update location counter based on the size defined in POT
        location_counter += POT[directive_or_instruction]

# Print the symbol table
print("Symbol Table:")
print("Symbol   Address")
for symbol, address in symbol_table.items():
    print(f"{symbol:6}   {address}")

