from Token import Token
import string
import sys

__author__ = 'Hrafnkell'


class Lexer(object):
    ''' Diagnoses each token and describes it for the computer '''
    def __init__(self):
        self.stdin = ""
        while True:
            io = input()
            self.stdin += io
            if "end" in io:
                break
        self.stdin = self.stdin.replace(" ", "")
        self.stdin = self.stdin.replace("\n", "")
        self.stdin = self.stdin.replace("\t", "")
        self.i = 0

    def nextToken(self):
        token = self.get_tokencode(self.stdin[self.i])
        self.i += 1
        return token

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
        elif lexeme == "e" and self.is_end(lexeme):
            return Token("end", "end")
        elif lexeme == "p" and self.is_print(lexeme):
            return Token("print", "print")
        elif lexeme.isdigit():
            tmpLex = lexeme
            iter = self.i + 1
            while True:
                if self.stdin[iter].isdigit():
                    tmpLex += self.stdin[iter]
                    iter += 1
                else:
                    self.i = iter - 1
                    break
                #else:
                #    if self.stdin[iter].isalpha() or self.stdin[iter] == "=":
                #        self.i = iter - 1
                #        return Token("Syntax error!", "error")
                #    self.i = iter - 1
                #    break
            return Token(tmpLex, "int")
        elif lexeme.isalpha():
            tmpLex = lexeme
            iter = self.i + 1
            while True:
                if self.stdin[iter].isalpha():
                    tmpLex += self.stdin[iter]
                    iter += 1
                else:
                    self.i = iter - 1
                    break
            return Token(tmpLex, "id")
        else:
            return Token("Syntax error!", "error")

    def is_end(self, lexeme):
        iter = self.i
        if self.stdin[iter + 1] == "n" and self.stdin[iter + 2] == "d":
            self.i += 2
            return True
        else:
            return False

    def is_print(self, lexeme):
        iter = self.i
        if self.stdin[iter + 1] == "r" and self.stdin[iter + 2] == "i" and self.stdin[iter + 3] == "n" and self.stdin[iter + 4] == "t" :
            self.i += 4
            return True
        else:
            return False



#while True:
#    stdin = input()
#    for i in stdin.split():
#        print(lex.nextToken(i).tCode)


lex = Lexer()

#string = ""

while lex.i != len(lex.stdin):
    tok = lex.nextToken()
    print(tok.tCode + " " + tok.lexeme)


#print(string)
