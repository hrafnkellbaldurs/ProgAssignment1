from Token import Token
import string
from sys import stdin


__author__ = 'Hrafnkell'


class Lexer(object):
    ''' Diagnoses each token and describes it for the computer '''
    def __init__(self):
        self.c = ""
        #self.string = ""
        #self.string = stdin.read()
        #self.string = self.string.replace(" ", "")
        #self.string = self.string.replace("\n", "")
        #self.string = self.string.replace("\t", "")
        #self.i = 0

    def nextToken(self):
        token = ""
        if(self.c == ""):
            token = self.get_tokencode(self.next_char())
        else:
            token = self.get_tokencode(self.c)
            self.c = ""
        return token

    def get_tokencode(self, lexeme):
        while lexeme == " " or lexeme == "\n" or lexeme == "\t":
            lexeme = self.next_char()
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
        elif lexeme.isdigit():
            tmpLex = lexeme
            while True:
                nxt_char = self.next_char()
                if nxt_char.isdigit():
                    tmpLex += nxt_char
                else:
                    self.c = nxt_char
                    break
            return Token(tmpLex, "int")
        elif lexeme.isalpha():
            tmpLex = lexeme
            while True:
                nxt_char = self.next_char()
                if nxt_char.isalpha():
                    tmpLex += nxt_char
                    if tmpLex == "print":
                        return Token("print", "print")
                    elif tmpLex == "end":
                        return Token("end", "end")
                else:
                    self.c = nxt_char
                    break
            return Token(tmpLex, "id")
        else:
            return Token("error", "error")

    def next_char(self):
        return stdin.read(1)


#lex = Lexer()

#print(lex.nextToken().tCode)
#print(lex.nextToken().tCode)
#print(lex.nextToken().tCode)





#for i in range(10):

#    print(next_char())


#print("running")

#string = stdin.read()
#print(string)

#while True:
#    stdin = input()
#    for i in stdin.split():
#        print(lex.nextToken(i).tCode)


#lex = Lexer()

#string = ""

#while lex.i != len(lex.stdin):
#    tok = lex.nextToken()
#    print(tok.tCode + " " + tok.lexeme)


#print(string)
