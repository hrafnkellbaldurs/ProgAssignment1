from Token import Token
import string

__author__ = 'Hrafnkell'


class Lexer(object):
    def __init__(self):
        pass

    def nextToken(self, word):
            return self.get_tokencode(word)

    def get_tokencode(self, lexeme):
        if lexeme == "+":
            return Token("+", "PLUS")
        elif lexeme == "-":
            return Token("-", "MINUS")
        elif lexeme == "*":
            return Token("*", "MULT")
        elif lexeme == "(":
            return Token("(", "LPAREN")
        elif lexeme == ")":
            return Token(")", "RPAREN")
        elif lexeme == "=":
            return Token("=", "ASSIGN")
        elif lexeme == ";":
            return Token(";", "SEMICOL")
        elif lexeme == "end":
            return Token("end", "END")
        elif lexeme == "print":
            return Token("print", "PRINT")
        elif lexeme.isdigit():
            return Token(lexeme, "INT")
        elif self.is_ID(lexeme):
            return Token(lexeme, "ID")
        else:
            return Token("Syntax error!: %s" % (lexeme), "ERROR")

    def is_ID(self, token):
        ''' returns true if token is an ID (A-Z, a-z)+ '''
        ans = False
        for char in token:
            if (char in list(string.ascii_lowercase)) or (char in list(string.ascii_uppercase)):
                ans = True
            else:
                return False
        return ans

lex = Lexer()

while True:
    stdin = input()
    for i in stdin.split():
        print(lex.nextToken(i).lexeme)


