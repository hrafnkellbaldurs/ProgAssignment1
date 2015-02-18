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
        elif lexeme.isalpha():
            return Token(lexeme, "id")
        else:
            return Token("Syntax error!", "error")

#while True:
#    stdin = input()
#    for i in stdin.split():
#        print(lex.nextToken(i).tCode)


