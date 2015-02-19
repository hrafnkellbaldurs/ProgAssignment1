from Lexer import Lexer
from Token import Token
import sys

__author__ = 'Hrafnkell'


class Parser(object):
    ''' The parser checks for syntax correctness '''

    ''' Public variables for easy syntax diagnosis '''

    ''' Constructor '''
    def __init__(self, lexer):
        self.lexer = lexer
        self.nextToken = Token("+", "+")

    ''' Goes through input and diagnoses syntax '''
    def parse(self):
        self.nextToken = self.lexer.nextToken()
        self.statements()

    ''' Statements -> Statement ; Statements | end '''
    def statements(self):
        if self.nextToken.tCode == "END":
            #self.nextToken == self.lexer.nextToken()
            sys.exit(1)
        else:
            self.statement()
            if self.nextToken.tCode == "SEMICOL":
                self.nextToken = self.lexer.nextToken()
                self.statements()
        if(self.nextToken.tCode == "ERROR"):
            self.error()

    ''' Statement -> id = Expr | print id '''
    def statement(self):
        if self.nextToken.tCode == "ID":
            print("PUSH " + self.nextToken.lexeme)
            self.nextToken = self.lexer.nextToken()
            if self.nextToken.tCode == "ASSIGN":
                self.nextToken = self.lexer.nextToken()
                self.expr()
                print("ASSIGN")
            else:
                self.error()
        elif self.nextToken.tCode == "PRINT":
            self.nextToken = self.lexer.nextToken()
            #print("PRINT")
            if self.nextToken.tCode == "ID":
                print("PUSH " + self.nextToken.lexeme)
                print("PRINT")
                self.nextToken = self.lexer.nextToken()
            else:
                self.error()
        else:
            self.error()
        if(self.nextToken.tCode == "ERROR"):
            self.error()


    ''' Expr -> Term | Term + Expr | Term - Expr '''
    def expr(self):
        self.term()
        if self.nextToken.tCode == "PLUS":
            self.nextToken = self.lexer.nextToken()
            self.expr()
            print("ADD")
        elif self.nextToken.tCode == "MINUS":
            self.nextToken = self.lexer.nextToken()
            self.expr()
            print("SUB")
        if(self.nextToken.tCode == "ERROR"):
            self.error()

    ''' Term -> Factor | Factor * Term '''
    def term(self):
        self.factor()
        if self.nextToken.tCode == "MULT":
            self.nextToken = self.lexer.nextToken()
            self.term()
            print("MULT")
        if(self.nextToken.tCode == "ERROR"):
            self.error()


    ''' Factor -> int | id | (Expr) '''
    def factor(self):
        if self.nextToken.tCode == "INT":
            print("PUSH " + self.nextToken.lexeme)
            self.nextToken = self.lexer.nextToken()
        elif self.nextToken.tCode == "ID":
            print("PUSH " + self.nextToken.lexeme)
            self.nextToken = self.lexer.nextToken()
        elif self.nextToken.tCode == "LPAREN":
            self.nextToken = self.lexer.nextToken()
            self.expr()
            if self.nextToken.tCode == "RPAREN":
                self.nextToken = self.lexer.nextToken()
            else:
                self.error()
        else:
            self.error()
        if(self.nextToken.tCode == "ERROR"):
            self.error()


    def error(self):
        print("Syntax error!")
        sys.exit(1)










