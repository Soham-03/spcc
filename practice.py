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

locationCount = 0
symbolTable = {}

for line in assembly_program:
    tokens = line.split()
    label = tokens[0]

    if(len(tokens)>1):
        directive_or_instrcution = tokens[1]
    else:
        directive_or_instrcution = ""
    
    if(directive_or_instrcution == "START"):
        locationCount = int(tokens[2])
        symbolTable[label] = format(locationCount, '04X')
    elif(directive_or_instrcution in MOT):
        locationCount += MOT[directive_or_instrcution]
    elif(directive_or_instrcution in POT):
        if(label!="**"):
            symbolTable[label] = format(locationCount, '04X')
        locationCount += POT[directive_or_instrcution]

print("Synmbol Table")
print("Synmbol Address")
for symbol, address in symbolTable.items():
    print(f"{symbol:6} {address}")
