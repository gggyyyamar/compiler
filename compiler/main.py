# main.py
from lexer import Lexer
from top_down_parser import RecursiveDescentParser  # Make sure this is implemented
from bottom_up_parser import ShiftReduceParser

if __name__ == "__main__":
    # Input Zara code
    code = '''int a = 10; float b = 3.14;'''

    # Lexical analysis
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    print("Tokens:")
    for token in tokens:
        print(token)

    # Top-down parsing
    print("\nTop-Down Parsing:")
    top_down_parser = RecursiveDescentParser(tokens)
    top_down_parser.parse()

    # Bottom-up parsing
    print("\nBottom-Up Parsing:")
    bottom_up_parser = ShiftReduceParser(tokens)
    bottom_up_parser.parse()
