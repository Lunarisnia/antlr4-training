# Generated from ./Trainer.g4 by ANTLR 4.13.1
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
        4,1,13,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,5,0,13,
        8,0,10,0,12,0,16,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,3,3,34,8,3,1,4,1,4,1,4,1,4,1,4,0,0,5,0,2,4,6,
        8,0,2,2,0,5,7,12,12,1,0,8,11,38,0,14,1,0,0,0,2,19,1,0,0,0,4,24,1,
        0,0,0,6,33,1,0,0,0,8,35,1,0,0,0,10,13,3,2,1,0,11,13,3,8,4,0,12,10,
        1,0,0,0,12,11,1,0,0,0,13,16,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,
        15,17,1,0,0,0,16,14,1,0,0,0,17,18,5,0,0,1,18,1,1,0,0,0,19,20,5,13,
        0,0,20,21,5,1,0,0,21,22,5,5,0,0,22,23,5,2,0,0,23,3,1,0,0,0,24,25,
        7,0,0,0,25,5,1,0,0,0,26,34,3,4,2,0,27,28,5,12,0,0,28,29,7,1,0,0,
        29,34,5,12,0,0,30,31,5,13,0,0,31,32,7,1,0,0,32,34,5,13,0,0,33,26,
        1,0,0,0,33,27,1,0,0,0,33,30,1,0,0,0,34,7,1,0,0,0,35,36,5,13,0,0,
        36,37,5,3,0,0,37,38,3,6,3,0,38,9,1,0,0,0,3,12,14,33
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
    RULE_expr = 3
    RULE_var = 4

    ruleNames =  [ "program", "func", "atom", "expr", "var" ]

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
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 12
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 10
                    self.func()
                    pass

                elif la_ == 2:
                    self.state = 11
                    self.var()
                    pass


                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 17
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
            self.state = 19
            self.match(TrainerParser.ID)
            self.state = 20
            self.match(TrainerParser.T__0)
            self.state = 21
            self.match(TrainerParser.STRING)
            self.state = 22
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
            self.state = 24
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(TrainerParser.AtomContext,0)


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
        self.enterRule(localctx, 6, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(TrainerParser.INT)
                self.state = 28
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 29
                self.match(TrainerParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.match(TrainerParser.ID)
                self.state = 31
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 32
                self.match(TrainerParser.ID)
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

        def ID(self):
            return self.getToken(TrainerParser.ID, 0)

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
        self.enterRule(localctx, 8, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(TrainerParser.ID)
            self.state = 36
            self.match(TrainerParser.T__2)
            self.state = 37
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





