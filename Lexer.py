from Token import Token
import string

__author__ = 'Hrafnkell'


class Lexer(object):
    ''' Diagnoses each token and describes it for the computer '''
    def __init__(self):
        self.stdin = input()

    def nextToken(self):
            return self.get_tokencode(self.stdin)

    def get_tokencode(self, lexeme):
        if lexeme == "+":
            return Token("+", "+")
        elif lexeme == "-":
            return Token("-", "-")
        elif lexeme == "*":
            return Token("*", "*")
        elif lexeme == "(":
            return Token("(", "(")
        elif lexeme == ")":
            return Token(")", ")")
        elif lexeme == "=":
            return Token("=", "=")
        elif lexeme == ";":
            return Token(";", ";")
        elif lexeme == "end":
            return Token("end", "end")
        elif lexeme == "print":
            return Token("print", "print")
        elif lexeme.isdigit():
            return Token(lexeme, "int")
        elif self.is_ID(lexeme):
            return Token(lexeme, "id")
        else:
            return Token("Syntax error!", "error")

    def is_ID(self, token):
        ''' returns true if token is an ID (A-Z, a-z)+ '''
        ans = False
        for char in token:
            if (char in list(string.ascii_lowercase)) or (char in list(string.ascii_uppercase)):
                ans = True
            else:
                return False
        return ans

#while True:
#    stdin = input()
#    for i in stdin.split():
#        print(lex.nextToken(i).tCode)


