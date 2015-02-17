__author__ = 'Hrafnkell'


class Token(object):
    def __init__(self, lexeme, tCode):
        TokenCode = ["ID", "ASSIGN", "SEMICOL", "INT", "PLUS", "MINUS",
                     "MULT", "LPAREN", "RPAREN", "PRINT", "END", "ERROR"]
        self.lexeme = lexeme
        self.tCode = TokenCode[tCode]





