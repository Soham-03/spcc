def expand_macros(input_lines, MNT, MDT):
    expanded_code = []
    in_macro = False

    for line in input_lines:
        stripped_line = line.strip()
        if stripped_line in MNT:
            # Macro invocation found, expand it
            mdt_index = MNT[stripped_line] - 1  # Adjusting index as MNT is 1-based
            while MDT[mdt_index] != "MEND":
                expanded_code.append(MDT[mdt_index])
                mdt_index += 1
        else:
            # Not a macro invocation, add it to expanded code
            expanded_code.append(stripped_line)

    return expanded_code

# MNT and MDT from Pass 1 (supposedly already computed)
MNT = {'INCR': 3}  # Macro starts at index 2 in MDT (1-based index)
MDT = [
    "AR  2,3",
    "MR  1,2",
    "ST  1,2",
    "MEND"
]

# Sample input from the user (including macro calls)
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

# Expand the macros
expanded_code = expand_macros(assembly_program, MNT, MDT)

# Print the expanded source code
print("Expanded Source Code:")
for line in expanded_code:
    print(line)
