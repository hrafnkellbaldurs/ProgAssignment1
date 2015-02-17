__author__ = 'Hrafnkell'


class Token(object):
    ''' A class for each token in the programming language '''
    def __init__(self, lexeme, tCode):
        TokenCode = {"ID": 1, "ASSIGN": 2, "SEMICOL": 3, "INT": 4, "PLUS": 5, "MINUS": 6,
                     "MULT": 7, "LPAREN": 8, "RPAREN": 9, "PRINT": 10, "END": 11, "ERROR": 12}
        self.lexeme = lexeme
        self.tCode = TokenCode[tCode]

#tok = Token("+", "PLUS")
#print(tok.tCode)




