# Generated from .\Speak.g4 by ANTLR 4.13.0
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
        4,1,5,26,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,1,
        1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,
        0,0,20,0,10,1,0,0,0,2,12,1,0,0,0,4,16,1,0,0,0,6,21,1,0,0,0,8,23,
        1,0,0,0,10,11,3,2,1,0,11,1,1,0,0,0,12,13,3,4,2,0,13,14,3,4,2,0,14,
        15,5,0,0,1,15,3,1,0,0,0,16,17,3,6,3,0,17,18,5,1,0,0,18,19,3,8,4,
        0,19,20,5,5,0,0,20,5,1,0,0,0,21,22,5,2,0,0,22,7,1,0,0,0,23,24,5,
        3,0,0,24,9,1,0,0,0,0
    ]

class SpeakParser ( Parser ):

    grammarFileName = "Speak.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "SAYS", "WORD", "TEXT", "WHITESPACE", 
                      "NEWLINE" ]

    RULE_prog = 0
    RULE_chat = 1
    RULE_line = 2
    RULE_name = 3
    RULE_opinion = 4

    ruleNames =  [ "prog", "chat", "line", "name", "opinion" ]

    EOF = Token.EOF
    SAYS=1
    WORD=2
    TEXT=3
    WHITESPACE=4
    NEWLINE=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chat(self):
            return self.getTypedRuleContext(SpeakParser.ChatContext,0)


        def getRuleIndex(self):
            return SpeakParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = SpeakParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.chat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpeakParser.LineContext)
            else:
                return self.getTypedRuleContext(SpeakParser.LineContext,i)


        def EOF(self):
            return self.getToken(SpeakParser.EOF, 0)

        def getRuleIndex(self):
            return SpeakParser.RULE_chat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChat" ):
                listener.enterChat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChat" ):
                listener.exitChat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChat" ):
                return visitor.visitChat(self)
            else:
                return visitor.visitChildren(self)




    def chat(self):

        localctx = SpeakParser.ChatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_chat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.line()
            self.state = 13
            self.line()
            self.state = 14
            self.match(SpeakParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(SpeakParser.NameContext,0)


        def SAYS(self):
            return self.getToken(SpeakParser.SAYS, 0)

        def opinion(self):
            return self.getTypedRuleContext(SpeakParser.OpinionContext,0)


        def NEWLINE(self):
            return self.getToken(SpeakParser.NEWLINE, 0)

        def getRuleIndex(self):
            return SpeakParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = SpeakParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.name()
            self.state = 17
            self.match(SpeakParser.SAYS)
            self.state = 18
            self.opinion()
            self.state = 19
            self.match(SpeakParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(SpeakParser.WORD, 0)

        def getRuleIndex(self):
            return SpeakParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = SpeakParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(SpeakParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpinionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(SpeakParser.TEXT, 0)

        def getRuleIndex(self):
            return SpeakParser.RULE_opinion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpinion" ):
                listener.enterOpinion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpinion" ):
                listener.exitOpinion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpinion" ):
                return visitor.visitOpinion(self)
            else:
                return visitor.visitChildren(self)




    def opinion(self):

        localctx = SpeakParser.OpinionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_opinion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(SpeakParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





