# bottom_up_parser.py
from lexer import Lexer

class ShiftReduceParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.stack = []

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def advance(self):
        self.pos += 1

    def shift(self):
        token = self.current_token()
        if token:
            self.stack.append(token)
            self.advance()

    def reduce(self):
        # Example grammar rule for assignment: IDENTIFIER ASSIGN NUMBER
        if len(self.stack) >= 3:
            if (self.stack[-3][0] == 'IDENTIFIER' and 
                self.stack[-2][0] == 'ASSIGN' and 
                self.stack[-1][0] == 'NUMBER'):
                
                value = self.stack.pop()  # Remove NUMBER
                self.stack.pop()  # Remove ASSIGN
                var_name = self.stack.pop()  # Remove IDENTIFIER
                print(f"Reduced: {var_name[1]} = {value[1]}")
                # After reduction, we can push a non-terminal back to the stack
                self.stack.append(('ASSIGNMENT', f"{var_name[1]} = {value[1]}"))

    def parse(self):
        while self.current_token() or len(self.stack) > 0:
            if self.current_token():
                self.shift()
            self.reduce()

# Example usage
if __name__ == "__main__":
    code = '''a = 10;'''
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = ShiftReduceParser(tokens)
    parser.parse()
