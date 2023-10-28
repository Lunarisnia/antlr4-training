import antlr4
from grammar.TrainerParser import TrainerParser
from grammar.TrainerVisitor import TrainerVisitor

variable_hash_map = {}


class VisitorInterp(TrainerVisitor):
    def visitProgram(self, ctx: TrainerParser.ProgramContext):
        for i in range(0, ctx.getChildCount()):
            self.visit(ctx.getChild(i))
        return 0

    def visitFunc(self, ctx: TrainerParser.FuncContext):
        startToken: antlr4.Token = ctx.start
        if ctx.ID().__str__() == "say":
            print(ctx.STRING().__str__())
        else:
            print(f"Line {startToken.line} can't recognize {ctx.ID()}.")
        return super().visitFunc(ctx)

    def visitVar(self, ctx: TrainerParser.VarContext):
        variable_hash_map[ctx.ID(0).__str__()] = None
        for i in range(0, ctx.getChildCount()):
            self.visit(ctx.getChild(i))
        if ctx.ID(1) and (ctx.ID(1).__str__() in variable_hash_map):
            variable_hash_map[ctx.ID(0).__str__()] = variable_hash_map[
                ctx.ID(1).__str__()
            ]
        elif ctx.ID(1) and not (ctx.ID(1).__str__() in variable_hash_map):
            # TODO: Should stop the compilation entirely
            print(ctx.ID(1).__str__(), "is not defined")
        return

    def visitExpr(self, ctx: TrainerParser.ExprContext):
        # Can be used to check if the atom exist before traveling the child
        # print(ctx.atom())
        if ctx.calculation():
            for i in range(0, ctx.getChildCount()):
                self.visit(ctx.getChild(i))
        if ctx.atom():
            for i in range(0, ctx.getChildCount()):
                self.visit(ctx.getChild(i))
        return

    def visitAtom(self, ctx: TrainerParser.AtomContext):
        createdVariable = None
        if ctx.STRING():
            createdVariable = ctx.STRING().__str__()
        elif ctx.INT():
            createdVariable = int(ctx.INT().__str__())
        elif ctx.TRUE():
            createdVariable = True
        elif ctx.FALSE():
            createdVariable = False
        variable_hash_map[ctx.parentCtx.parentCtx.ID(0).__str__()] = createdVariable
        return

    def visitCalculation(self, ctx: TrainerParser.CalculationContext):
        # print([x.__str__() for x in ctx.ID()], [x.__str__() for x in ctx.INT()])
        calculation_result = 0
        if len(ctx.ID()):
            for var in ctx.ID():
                if var.__str__() not in variable_hash_map:
                    print(var.__str__(), "not defined")
                    return
            if ctx.ADD():
                calculation_result = variable_hash_map[ctx.ID(0).__str__()] + variable_hash_map[ctx.ID(1).__str__()]
            elif ctx.SUBTRACT():
                calculation_result = variable_hash_map[ctx.ID(0).__str__()] - variable_hash_map[ctx.ID(1).__str__()]
            elif ctx.MULTIPLY():
                calculation_result = variable_hash_map[ctx.ID(0).__str__()] * variable_hash_map[ctx.ID(1).__str__()]
            elif ctx.DIVIDE():
                calculation_result = variable_hash_map[ctx.ID(0).__str__()] / variable_hash_map[ctx.ID(1).__str__()]
            else:
                print("How the fuck do you got here?")
        elif len(ctx.INT()):
            if ctx.ADD():
                calculation_result = int(ctx.INT(0).__str__()) + int(ctx.INT(1).__str__())
            elif ctx.SUBTRACT():
                calculation_result = int(ctx.INT(0).__str__()) - int(ctx.INT(1).__str__())
            elif ctx.MULTIPLY():
                calculation_result = int(ctx.INT(0).__str__()) * int(ctx.INT(1).__str__())
            elif ctx.DIVIDE():
                calculation_result = int(ctx.INT(0).__str__()) / int(ctx.INT(1).__str__())
            else:
                print("How the fuck do you got here?")
        variable_hash_map[ctx.parentCtx.parentCtx.ID(0).__str__()] = calculation_result
        print(variable_hash_map)
        return
