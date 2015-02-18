__author__ = 'Hrafnkell'


class Token(object):
    ''' A class for each token in the programming language '''
    def __init__(self, lexeme, tCode):
        TokenCode = {"id": "ID", "=": "ASSIGN", ";": "SEMICOL", "int": "INT", "+": "PLUS", "-": "MINUS",
                     "*": "MULT", "(": "LPAREN", ")": "RPAREN", "print": "PRINT", "end": "END", "error": "ERROR"}
        self.lexeme = lexeme
        self.tCode = TokenCode[tCode]

#tok = Token("+", "PLUS")
#print(tok.tCode)




