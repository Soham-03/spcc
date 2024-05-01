class RecursiveDescentParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.current_token = tokens[0] if tokens else None

    def next_token(self):
        self.current_token_index += 1
        if self.current_token_index < len(self.tokens):
            self.current_token = self.tokens[self.current_token_index]
        else:
            self.current_token = None  # EOF

    def accept(self, expected_token):
        if self.current_token == expected_token:
            self.next_token()
            return True
        return False

    def parse_E(self):
        # E -> TE'
        self.parse_T()
        self.parse_E_prime()

    def parse_E_prime(self):
        # E' -> +TE' | epsilon
        if self.accept('+'):
            self.parse_T()
            self.parse_E_prime()

    def parse_T(self):
        # T -> FT'
        self.parse_F()
        self.parse_T_prime()

    def parse_T_prime(self):
        # T' -> *FT' | epsilon
        if self.accept('*'):
            self.parse_F()
            self.parse_T_prime()

    def parse_F(self):
        # F -> (E) | id
        if self.accept('('):
            self.parse_E()
            if not self.accept(')'):
                raise Exception("Syntax Error: Missing ')'")
        elif self.accept('id'):
            pass  # Just accept 'id'
        else:
            raise Exception("Syntax Error: Expected 'id' or '('")

    def parse(self):
        self.parse_E()
        if self.current_token is not None:
            raise Exception("Syntax Error: Extra input after last parse.")

# Example usage
tokens = ["id", "+", "id", "*", "(", "id", "+", "id", ")", "*", "id"]
parser = RecursiveDescentParser(tokens)
try:
    parser.parse()
    print("Parsing successful.")
except Exception as e:
    print(str(e))
