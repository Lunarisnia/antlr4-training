# Generated from ./grammar/Trainer.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TrainerParser import TrainerParser
else:
    from TrainerParser import TrainerParser

# This class defines a complete listener for a parse tree produced by TrainerParser.
class TrainerListener(ParseTreeListener):

    # Enter a parse tree produced by TrainerParser#program.
    def enterProgram(self, ctx:TrainerParser.ProgramContext):
        pass

    # Exit a parse tree produced by TrainerParser#program.
    def exitProgram(self, ctx:TrainerParser.ProgramContext):
        pass


    # Enter a parse tree produced by TrainerParser#func.
    def enterFunc(self, ctx:TrainerParser.FuncContext):
        pass

    # Exit a parse tree produced by TrainerParser#func.
    def exitFunc(self, ctx:TrainerParser.FuncContext):
        pass


    # Enter a parse tree produced by TrainerParser#atom.
    def enterAtom(self, ctx:TrainerParser.AtomContext):
        pass

    # Exit a parse tree produced by TrainerParser#atom.
    def exitAtom(self, ctx:TrainerParser.AtomContext):
        pass


    # Enter a parse tree produced by TrainerParser#calculation.
    def enterCalculation(self, ctx:TrainerParser.CalculationContext):
        pass

    # Exit a parse tree produced by TrainerParser#calculation.
    def exitCalculation(self, ctx:TrainerParser.CalculationContext):
        pass


    # Enter a parse tree produced by TrainerParser#expr.
    def enterExpr(self, ctx:TrainerParser.ExprContext):
        pass

    # Exit a parse tree produced by TrainerParser#expr.
    def exitExpr(self, ctx:TrainerParser.ExprContext):
        pass


    # Enter a parse tree produced by TrainerParser#var.
    def enterVar(self, ctx:TrainerParser.VarContext):
        pass

    # Exit a parse tree produced by TrainerParser#var.
    def exitVar(self, ctx:TrainerParser.VarContext):
        pass



del TrainerParser