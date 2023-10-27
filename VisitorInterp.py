import sys
from antlr4 import *
from grammar.TrainerParser import TrainerParser
from grammar.TrainerVisitor import TrainerVisitor

class VisitorInterp(TrainerVisitor):
    # TODO: try and do variable assignment plus calculation
    # TODO: try and do variable calculation assignment
    def visitProgram(self, ctx: TrainerParser.ProgramContext):
        for i in range(0, ctx.getChildCount()):
            self.visit(ctx.getChild(i))
        return 0
    
    def visitFunc(self, ctx: TrainerParser.FuncContext):
        startToken : Token = ctx.start
        if (ctx.ID().__str__() == "say"):
            print(ctx.STRING().__str__())
        else:
            print(f"Line {startToken.line} can't recognize Function {ctx.ID()}.")
        return super().visitFunc(ctx)

    def visitVar(self, ctx: TrainerParser.VarContext):
        for i in range(0, ctx.getChildCount()):
            self.visit(ctx.getChild(i))
        return 0
    
    def visitExpr(self, ctx: TrainerParser.ExprContext):
        # Can be used to check if the atom exist before traveling the child
        # print(ctx.atom())
        if ctx.atom():
            for i in range(0, ctx.getChildCount()):
                self.visit(ctx.getChild(i))
        return super().visitExpr(ctx)
    
    def visitAtom(self, ctx: TrainerParser.AtomContext):
        print("ATOM")
        return super().visitAtom(ctx)