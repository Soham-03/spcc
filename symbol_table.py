import re

def create_symbol_table(code):
    # This regex matches variable declarations and assignments (int a = 5; or int a;)
    pattern = r'\b(int|float|char)\s+([a-zA-Z_]\w*)\s*(=\s*[^;]+)?;'
    matches = re.findall(pattern, code)

    symbol_table = {}
    for match in matches:
        data_type, variable_name, value = match
        if value:
            # Evaluate the expression to the right of '=' if there is one
            # Unsafe but used here for simplicity
            try:
                # Remove '=' and spaces around it then evaluate
                value = eval(value.split('=')[1].strip())
            except:
                print("Error evaluating the value of", variable_name)
                continue
        else:
            # Default values based on type if no value is assigned
            value = 0 if data_type == 'int' else 0.0 if data_type == 'float' else '\0'

        symbol_table[variable_name] = {'type': data_type, 'value': value}

    return symbol_table

# Example usage:
code = """
int a = 5;
float b = 3.2;
char c = 'x';
int d;
"""
symbol_table = create_symbol_table(code)
print("Symbol Table:", symbol_table)