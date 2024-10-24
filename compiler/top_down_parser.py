# parser.py
from symbol_table import SymbolTable
from lexer import Lexer

class Parser:
    def __init__(self):
        self.token_index = 0
        self.tokens = []
        self.symbol_table = SymbolTable()

    def load_tokens(self, tokens):
        self.tokens = tokens
        self.token_index = 0

    def next_token(self):
        if self.token_index < len(self.tokens):
            self.token_index += 1
            return self.tokens[self.token_index - 1]
        return None

    def peek_token(self):
        if self.token_index < len(self.tokens):
            return self.tokens[self.token_index]
        return None

    def expect(self, token_type):
        token = self.next_token()
        if token and token[0] == token_type:
            return token
        else:
            raise SyntaxError(f"Expected {token_type} but got {token}")

    def parse_expression(self):
        token = self.peek_token()
        if token[0] in ['INT_LITERAL', 'FLOAT_LITERAL','STRING_LITERAL', 'IDENTIFIER']:
            self.next_token()
            if self.peek_token() and self.peek_token()[0] == 'OPERATOR':
                self.next_token()
                self.parse_expression()
        else:
            raise SyntaxError(f"Invalid expression at {token}")

    def parse_if(self):
        self.expect('KEYWORD_IF')
        self.expect('PARENTHESIS')
        self.parse_expression()
        self.expect('PARENTHESIS')
        self.expect('BRACE')
        self.parse_statements()
        self.expect('BRACE')

    def parse_do_while(self):
        self.expect('KEYWORD_DO')
        self.expect('BRACE')
        self.parse_statements()
        self.expect('BRACE')
        self.expect('KEYWORD_WHILE')
        self.expect('PARENTHESIS')
        self.parse_expression()
        self.expect('PARENTHESIS')

    def parse_declaration(self):
        token = self.next_token()
        if token[0] not in ['TYPE_INT', 'TYPE_FLOAT', 'TYPE_STRING']:
            raise SyntaxError(f"Expected type but got {token}")
        identifier = self.expect('IDENTIFIER')
        if self.peek_token() and self.peek_token()[0] == 'OPERATOR' and self.peek_token()[1] == '=':
            self.next_token()
            self.parse_expression()
        self.expect('SEMICOLON')
        self.symbol_table.add_symbol(identifier[1], token[0])

    def parse_statement(self):
        token = self.peek_token()
        if token[0] in ['TYPE_INT', 'TYPE_FLOAT', 'TYPE_STRING']:
            self.parse_declaration()
        elif token[0] == 'KEYWORD_IF':
            self.parse_if()
        elif token[0] == 'KEYWORD_DO':
            self.parse_do_while()
        else:
            self.parse_expression()
            self.expect('SEMICOLON')

    def parse_statements(self):
        while self.peek_token() and self.peek_token()[0] != 'BRACE':
            self.parse_statement()
