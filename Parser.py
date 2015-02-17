from Lexer import Lexer
from Token import Token

__author__ = 'Hrafnkell'


class Parser(object):
    ''' The parser checks for syntax correctness '''

    ''' Public variables for easy syntax diagnosis '''

    ''' Constructor '''
    def __init__(self, lexer):
        self.lexer = lexer
        self.token = Token()

    ''' Goes through input and diagnoses syntax '''
    def parse(self):
        output = []
        while True:
            stdin = input()
            for i in stdin.split():
                self.token = self.lexer.nextToken(i)
                #if self.statements(self.token):


    ''' Statements -> Statement ; Statements | end '''
    def statements(self):
        pass

    ''' Statement -> id = Expr | print id '''
    def statement(self):
        pass

    ''' Expr -> Term | Term + Expr | Term - Expr '''
    def expr(self):
        pass

    ''' Term -> Factor | Factor * Term '''
    def term(self):
        pass

    ''' Factor -> int | id | (Expr) '''
    def factor(self):
        pass





