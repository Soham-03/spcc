# Definitions for MOT, POT, and Symbol Table (ST)
mot = {
    'A': '5A',
    'L': '6A',
    'ST': '7A',
    'END': ''
}
pot = ['DS', 'DC', 'START', 'USING']
symbol_table = {
    'FIVE': '12',
    'FOUR': '16',
    'TEMP': '20'
}

# Assembly program
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

# Process the assembly program to generate machine code
def generate_machine_code(assembly_program, mot, pot, symbol_table):
    machine_code = []
    for line in assembly_program:
        tokens = line.split()
        if tokens[0] == '**':  # This means it's an actual instruction or directive
            if len(tokens) > 2 and tokens[1] in mot:  # Ensure there are enough tokens and it's a MOT instruction
                instruction_parts = tokens[2].split(',')
                if len(instruction_parts) > 1:  # Check that there is an operand after the comma
                    operand = instruction_parts[1]  # Get the operand after the comma
                    if operand in symbol_table:
                        # Append opcode and the symbol's address
                        machine_code.append(f"{mot[tokens[1]]} {symbol_table[operand]}")
            continue  # Skip further processing if this is an instruction line
        # Check for labels that might be data definitions
        if tokens[0] in symbol_table:
            if len(tokens) > 1 and tokens[1] in pot:
                # Handling DC and DS, assuming simple values to be stored for DC
                if tokens[1] == 'DC':
                    # Extract the value within F'5' -> 5
                    value = tokens[2].split('F')[1].strip("'")
                    machine_code.append(f"00 {value}")  # Assuming 00 is a placeholder for data
                elif tokens[1] == 'DS':
                    machine_code.append("00 00")  # Placeholder for uninitialized data
    return machine_code

# Generate and print the machine code
mc = generate_machine_code(assembly_program, mot, pot, symbol_table)
for code in mc:
    print(code)
