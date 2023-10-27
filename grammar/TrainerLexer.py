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
        4,0,5,49,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,1,1,1,1,2,1,2,3,2,22,8,2,1,3,1,3,1,3,5,3,27,8,3,
        10,3,12,3,30,9,3,1,3,1,3,1,4,4,4,35,8,4,11,4,12,4,36,1,4,1,4,1,5,
        1,5,5,5,43,8,5,10,5,12,5,46,9,5,1,6,1,6,1,28,0,7,1,1,3,2,5,0,7,0,
        9,3,11,4,13,5,1,0,5,2,0,10,10,13,13,1,0,34,34,3,0,9,10,12,13,32,
        32,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,51,0,1,1,
        0,0,0,0,3,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,
        0,0,3,17,1,0,0,0,5,21,1,0,0,0,7,23,1,0,0,0,9,34,1,0,0,0,11,40,1,
        0,0,0,13,47,1,0,0,0,15,16,5,60,0,0,16,2,1,0,0,0,17,18,5,62,0,0,18,
        4,1,0,0,0,19,22,9,0,0,0,20,22,8,0,0,0,21,19,1,0,0,0,21,20,1,0,0,
        0,22,6,1,0,0,0,23,28,5,34,0,0,24,27,3,5,2,0,25,27,8,1,0,0,26,24,
        1,0,0,0,26,25,1,0,0,0,27,30,1,0,0,0,28,29,1,0,0,0,28,26,1,0,0,0,
        29,31,1,0,0,0,30,28,1,0,0,0,31,32,5,34,0,0,32,8,1,0,0,0,33,35,7,
        2,0,0,34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,
        38,1,0,0,0,38,39,6,4,0,0,39,10,1,0,0,0,40,44,7,3,0,0,41,43,7,4,0,
        0,42,41,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,12,
        1,0,0,0,46,44,1,0,0,0,47,48,3,7,3,0,48,14,1,0,0,0,6,0,21,26,28,36,
        44,1,6,0,0
    ]

class TrainerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    WS = 3
    ID = 4
    STRING = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ID", "STRING" ]

    ruleNames = [ "T__0", "T__1", "RAW_STRING", "SINGLE_LINE_STRING", "WS", 
                  "ID", "STRING" ]

    grammarFileName = "Trainer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


