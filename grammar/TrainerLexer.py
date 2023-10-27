# Generated from ./Trainer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,13,85,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,3,3,40,8,3,1,4,1,
        4,1,4,5,4,45,8,4,10,4,12,4,48,9,4,1,4,1,4,1,5,4,5,53,8,5,11,5,12,
        5,54,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,
        1,11,1,12,1,12,1,13,4,13,75,8,13,11,13,12,13,76,1,14,1,14,5,14,81,
        8,14,10,14,12,14,84,9,14,1,46,0,15,1,1,3,2,5,3,7,0,9,0,11,4,13,5,
        15,6,17,7,19,8,21,9,23,10,25,11,27,12,29,13,1,0,6,2,0,10,10,13,13,
        1,0,34,34,3,0,9,10,12,13,32,32,1,0,48,57,3,0,65,90,95,95,97,122,
        4,0,48,57,65,90,95,95,97,122,88,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,
        0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,
        0,0,1,31,1,0,0,0,3,33,1,0,0,0,5,35,1,0,0,0,7,39,1,0,0,0,9,41,1,0,
        0,0,11,52,1,0,0,0,13,58,1,0,0,0,15,61,1,0,0,0,17,63,1,0,0,0,19,65,
        1,0,0,0,21,67,1,0,0,0,23,69,1,0,0,0,25,71,1,0,0,0,27,74,1,0,0,0,
        29,78,1,0,0,0,31,32,5,60,0,0,32,2,1,0,0,0,33,34,5,62,0,0,34,4,1,
        0,0,0,35,36,5,61,0,0,36,6,1,0,0,0,37,40,9,0,0,0,38,40,8,0,0,0,39,
        37,1,0,0,0,39,38,1,0,0,0,40,8,1,0,0,0,41,46,5,34,0,0,42,45,3,7,3,
        0,43,45,8,1,0,0,44,42,1,0,0,0,44,43,1,0,0,0,45,48,1,0,0,0,46,47,
        1,0,0,0,46,44,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,49,50,5,34,0,0,
        50,10,1,0,0,0,51,53,7,2,0,0,52,51,1,0,0,0,53,54,1,0,0,0,54,52,1,
        0,0,0,54,55,1,0,0,0,55,56,1,0,0,0,56,57,6,5,0,0,57,12,1,0,0,0,58,
        59,3,9,4,0,59,60,6,6,1,0,60,14,1,0,0,0,61,62,5,84,0,0,62,16,1,0,
        0,0,63,64,5,70,0,0,64,18,1,0,0,0,65,66,5,43,0,0,66,20,1,0,0,0,67,
        68,5,45,0,0,68,22,1,0,0,0,69,70,5,42,0,0,70,24,1,0,0,0,71,72,5,47,
        0,0,72,26,1,0,0,0,73,75,7,3,0,0,74,73,1,0,0,0,75,76,1,0,0,0,76,74,
        1,0,0,0,76,77,1,0,0,0,77,28,1,0,0,0,78,82,7,4,0,0,79,81,7,5,0,0,
        80,79,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,30,1,
        0,0,0,84,82,1,0,0,0,7,0,39,44,46,54,76,82,2,6,0,0,1,6,0
    ]

class TrainerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    WS = 4
    STRING = 5
    TRUE = 6
    FALSE = 7
    ADD = 8
    SUBTRACT = 9
    MULTIPLY = 10
    DIVIDE = 11
    INT = 12
    ID = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'", "'='", "'T'", "'F'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "STRING", "TRUE", "FALSE", "ADD", "SUBTRACT", "MULTIPLY", 
            "DIVIDE", "INT", "ID" ]

    ruleNames = [ "T__0", "T__1", "T__2", "RAW_STRING", "SINGLE_LINE_STRING", 
                  "WS", "STRING", "TRUE", "FALSE", "ADD", "SUBTRACT", "MULTIPLY", 
                  "DIVIDE", "INT", "ID" ]

    grammarFileName = "Trainer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[6] = self.STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     


