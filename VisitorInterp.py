import sys
from antlr4 import *
from grammar.TrainerParser import TrainerParser
from grammar.TrainerVisitor import TrainerVisitor

class VisitorInterp(TrainerVisitor):
    def visitProgram(self, ctx: TrainerParser.ProgramContext):
        for i in range(0, ctx.getChildCount()):
            self.visit(ctx.getChild(i))
        return 0
    
    def visitFunc(self, ctx: TrainerParser.FuncContext):
        startToken : Token = ctx.start
        terminalNode : TerminalNode = ctx.ID()
        # print(terminalNode.__str__())
        if (ctx.ID().__str__() == "say"):
            print(ctx.toStringTree())
        else:
            print(f"Line {startToken.line} can't recognize Function {ctx.ID()}.")
        return super().visitFunc(ctx)