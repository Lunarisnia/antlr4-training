# Generated from ./Trainer.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TrainerParser import TrainerParser
else:
    from TrainerParser import TrainerParser

# This class defines a complete generic visitor for a parse tree produced by TrainerParser.

class TrainerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TrainerParser#program.
    def visitProgram(self, ctx:TrainerParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TrainerParser#func.
    def visitFunc(self, ctx:TrainerParser.FuncContext):
        return self.visitChildren(ctx)



del TrainerParser