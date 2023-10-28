import sys
import antlr4
from grammar.TrainerLexer import TrainerLexer
from grammar.TrainerParser import TrainerParser
from VisitorInterp import VisitorInterp


def main(argv):
    input_stream = antlr4.FileStream(argv[1])
    lexer = TrainerLexer(input_stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = TrainerParser(tokens) 
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        visitorInterp = VisitorInterp()
        visitorInterp.visit(tree)


if __name__ == "__main__":
    main(sys.argv)
