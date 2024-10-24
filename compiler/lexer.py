# lexer.py
import re

class Lexer:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.current_char = self.code[self.pos] if self.code else None
        self.token_regex = [
            (r'[ \t\n]+', None),            # Ignore whitespace
            (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),
            (r'=', 'ASSIGN'),
            (r'\d+', 'NUMBER'),
            (r';', 'SEMICOLON'),
            (r'.', 'UNKNOWN'),              # Catch-all for unknown characters
        ]

    def tokenize(self):
        tokens = []
        while self.pos < len(self.code):
            matched = False
            for regex, token_type in self.token_regex:
                pattern = re.compile(regex)
                match = pattern.match(self.code, self.pos)
                if match:
                    matched = True
                    if token_type:  # If there is a token type
                        tokens.append((token_type, match.group(0)))
                    self.pos = match.end()
                    break
            if not matched:
                raise ValueError(f'Illegal character: {self.current_char}')
        return tokens
