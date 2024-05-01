def process_macros(input_lines):
    MNT = {}  # Macro Name Table
    MDT = []  # Macro Definition Table
    in_macro_definition = False
    macro_name = ""

    for line in input_lines:
        stripped_line = line.strip()
        if "MACRO" in stripped_line:
            in_macro_definition = True
        elif "MEND" in stripped_line:
            in_macro_definition = False
            MNT[macro_name] = len(MDT)
            macro_name = ""
        elif in_macro_definition:
            if macro_name == "":
                # This is the line with the macro name
                macro_name = stripped_line
                MNT[macro_name] = len(MDT) + 1  # +1 because MDT is 0-indexed
            else:
                # These are the macro body lines
                MDT.append(stripped_line)
        # Else, it's part of the rest of the code, which we ignore for Pass 1

    return MNT, MDT

# Sample input from the user
assembly_program = [
    "MACRO",
    "INCR",
    "AR  2,3",
    "MR  1,2",
    "ST  1,2",
    "MEND",
    "PG1            START",
    "USING    *,15",
    "L     1,FIVE",
    "A      1, FOUR",
    "INCR",
    "ST    1,TEMP",
    "M    1,FIVE",
    "INCR",
    "FIVE            DC    F’5’",
    "FOUR          DC   F’4’",
    "TEMP          DS   1F",
    "END"
]

MNT, MDT = process_macros(assembly_program)

print("Macro Name Table (MNT):")
for name, index in MNT.items():
    print(f"{name}: Starts at MDT index {index}")

print("\nMacro Definition Table (MDT):")
for i, line in enumerate(MDT):
    print(f"{i+1}: {line}")
