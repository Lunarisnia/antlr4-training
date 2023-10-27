import sys
from antlr4 import *
from grammar.TrainerLexer import TrainerLexer
from grammar.TrainerParser import TrainerParser
from VisitorInterp import VisitorInterp

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = TrainerLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = TrainerParser(tokens)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        visitorInterp = VisitorInterp()
        visitorInterp.visit(tree)

if __name__ == "__main__":
    main(sys.argv)