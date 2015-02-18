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
        self.nextToken = Token()

    ''' Goes through input and diagnoses syntax '''
    def parse(self):
        self.nextToken = self.lexer.nextToken()
        self.statements()

    ''' Statements -> Statement ; Statements | end '''
    def statements(self):
        if self.nextToken == "END":
            self.nextToken == self.lexer.nextToken()
            sys.exit(1)
        else:
            self.statement()
            if self.nextToken == "SEMICOL":
                self.nextToken == self.lexer.nextToken()
                self.statements()

    ''' Statement -> id = Expr | print id '''
    def statement(self):
        if self.nextToken == "ID":
            self.nextToken == self.lexer.nextToken()
            if self.nextToken == "ASSIGN":
                self.nextToken == self.lexer.nextToken()
                self.expr()
            else:
                self.error()
        elif self.nextToken == "PRINT":
            self.nextToken == self.lexer.nextToken()
            if self.nextToken == "ID":
                self.nextToken == self.lexer.nextToken()
                #Skrifa ut assembly
            else:
                self.error()
        else:
            self.error()


    ''' Expr -> Term | Term + Expr | Term - Expr '''
    def expr(self):
        self.term()
        if self.nextToken == "PLUS":
            self.nextToken == self.lexer.nextToken()
            self.expr()
        elif self.nextToken == "MINUS":
            self.nextToken == self.lexer.nextToken()
            self.expr()
        else:
            self.error()

    ''' Term -> Factor | Factor * Term '''
    def term(self):
        self.factor()
        if self.nextToken == "MULT":
            self.nextToken == self.lexer.nextToken()
            self.term()
        else:
            self.error()


    ''' Factor -> int | id | (Expr) '''
    def factor(self):
        # if token is INT
        if self.nextToken == "INT":
            self.nextToken = self.lexer.nextToken()

        # if token is ID
        elif self.nextToken == "ID":
            self.nextToken == self.lexer.nextToken()

        # LPAREN
        elif self.nextToken == "LPAREN":
            self.nextToken == self.lexer.nextToken()
            self.expr()

            # RPAREN
            if self.nextToken == "RPAREN":
                self.nextToken == self.lexer.nextToken()
            else:
                self.error()
        else:
            self.error()


    def error(self):
        print(self.nextToken.lexeme)
        sys.exit(1)

#token = Token("+", "PLUS")







