from Lexer import Lexer
from Parser import Parser

__author__ = 'Hrafnkell'

myLexer = Lexer()
myParser = Parser(myLexer)
myParser.parse()
