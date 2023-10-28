# Generated from ./grammar/Trainer.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,47,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,5,0,15,8,0,10,0,12,0,18,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,
        2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,35,8,3,1,4,1,4,3,4,39,8,4,1,5,1,5,
        1,5,1,5,3,5,45,8,5,1,5,0,0,6,0,2,4,6,8,10,0,2,2,0,5,7,12,12,1,0,
        8,11,45,0,16,1,0,0,0,2,21,1,0,0,0,4,26,1,0,0,0,6,34,1,0,0,0,8,38,
        1,0,0,0,10,40,1,0,0,0,12,15,3,2,1,0,13,15,3,10,5,0,14,12,1,0,0,0,
        14,13,1,0,0,0,15,18,1,0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,19,1,
        0,0,0,18,16,1,0,0,0,19,20,5,0,0,1,20,1,1,0,0,0,21,22,5,13,0,0,22,
        23,5,1,0,0,23,24,5,5,0,0,24,25,5,2,0,0,25,3,1,0,0,0,26,27,7,0,0,
        0,27,5,1,0,0,0,28,29,5,12,0,0,29,30,7,1,0,0,30,35,5,12,0,0,31,32,
        5,13,0,0,32,33,7,1,0,0,33,35,5,13,0,0,34,28,1,0,0,0,34,31,1,0,0,
        0,35,7,1,0,0,0,36,39,3,4,2,0,37,39,3,6,3,0,38,36,1,0,0,0,38,37,1,
        0,0,0,39,9,1,0,0,0,40,41,5,13,0,0,41,44,5,3,0,0,42,45,3,8,4,0,43,
        45,5,13,0,0,44,42,1,0,0,0,44,43,1,0,0,0,45,11,1,0,0,0,5,14,16,34,
        38,44
    ]

class TrainerParser ( Parser ):

    grammarFileName = "Trainer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'", "'='", "<INVALID>", "<INVALID>", 
                     "'T'", "'F'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WS", "STRING", "TRUE", "FALSE", "ADD", "SUBTRACT", 
                      "MULTIPLY", "DIVIDE", "INT", "ID" ]

    RULE_program = 0
    RULE_func = 1
    RULE_atom = 2
    RULE_calculation = 3
    RULE_expr = 4
    RULE_var = 5

    ruleNames =  [ "program", "func", "atom", "calculation", "expr", "var" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    WS=4
    STRING=5
    TRUE=6
    FALSE=7
    ADD=8
    SUBTRACT=9
    MULTIPLY=10
    DIVIDE=11
    INT=12
    ID=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TrainerParser.EOF, 0)

        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrainerParser.FuncContext)
            else:
                return self.getTypedRuleContext(TrainerParser.FuncContext,i)


        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrainerParser.VarContext)
            else:
                return self.getTypedRuleContext(TrainerParser.VarContext,i)


        def getRuleIndex(self):
            return TrainerParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = TrainerParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 14
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 12
                    self.func()
                    pass

                elif la_ == 2:
                    self.state = 13
                    self.var()
                    pass


                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19
            self.match(TrainerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TrainerParser.ID, 0)

        def STRING(self):
            return self.getToken(TrainerParser.STRING, 0)

        def getRuleIndex(self):
            return TrainerParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = TrainerParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(TrainerParser.ID)
            self.state = 22
            self.match(TrainerParser.T__0)
            self.state = 23
            self.match(TrainerParser.STRING)
            self.state = 24
            self.match(TrainerParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TrainerParser.INT, 0)

        def TRUE(self):
            return self.getToken(TrainerParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(TrainerParser.FALSE, 0)

        def STRING(self):
            return self.getToken(TrainerParser.STRING, 0)

        def getRuleIndex(self):
            return TrainerParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = TrainerParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4320) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CalculationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(TrainerParser.INT)
            else:
                return self.getToken(TrainerParser.INT, i)

        def ADD(self):
            return self.getToken(TrainerParser.ADD, 0)

        def SUBTRACT(self):
            return self.getToken(TrainerParser.SUBTRACT, 0)

        def DIVIDE(self):
            return self.getToken(TrainerParser.DIVIDE, 0)

        def MULTIPLY(self):
            return self.getToken(TrainerParser.MULTIPLY, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TrainerParser.ID)
            else:
                return self.getToken(TrainerParser.ID, i)

        def getRuleIndex(self):
            return TrainerParser.RULE_calculation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalculation" ):
                listener.enterCalculation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalculation" ):
                listener.exitCalculation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalculation" ):
                return visitor.visitCalculation(self)
            else:
                return visitor.visitChildren(self)




    def calculation(self):

        localctx = TrainerParser.CalculationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_calculation)
        self._la = 0 # Token type
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(TrainerParser.INT)
                self.state = 29
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 30
                self.match(TrainerParser.INT)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.match(TrainerParser.ID)
                self.state = 32
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 33
                self.match(TrainerParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(TrainerParser.AtomContext,0)


        def calculation(self):
            return self.getTypedRuleContext(TrainerParser.CalculationContext,0)


        def getRuleIndex(self):
            return TrainerParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = TrainerParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.calculation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TrainerParser.ID)
            else:
                return self.getToken(TrainerParser.ID, i)

        def expr(self):
            return self.getTypedRuleContext(TrainerParser.ExprContext,0)


        def getRuleIndex(self):
            return TrainerParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = TrainerParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(TrainerParser.ID)
            self.state = 41
            self.match(TrainerParser.T__2)
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 42
                self.expr()
                pass

            elif la_ == 2:
                self.state = 43
                self.match(TrainerParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





