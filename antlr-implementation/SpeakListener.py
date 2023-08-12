# Generated from .\Speak.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SpeakParser import SpeakParser
else:
    from SpeakParser import SpeakParser

# This class defines a complete listener for a parse tree produced by SpeakParser.
class SpeakListener(ParseTreeListener):

    # Enter a parse tree produced by SpeakParser#prog.
    def enterProg(self, ctx:SpeakParser.ProgContext):
        pass

    # Exit a parse tree produced by SpeakParser#prog.
    def exitProg(self, ctx:SpeakParser.ProgContext):
        pass


    # Enter a parse tree produced by SpeakParser#chat.
    def enterChat(self, ctx:SpeakParser.ChatContext):
        pass

    # Exit a parse tree produced by SpeakParser#chat.
    def exitChat(self, ctx:SpeakParser.ChatContext):
        pass


    # Enter a parse tree produced by SpeakParser#line.
    def enterLine(self, ctx:SpeakParser.LineContext):
        pass

    # Exit a parse tree produced by SpeakParser#line.
    def exitLine(self, ctx:SpeakParser.LineContext):
        pass


    # Enter a parse tree produced by SpeakParser#name.
    def enterName(self, ctx:SpeakParser.NameContext):
        pass

    # Exit a parse tree produced by SpeakParser#name.
    def exitName(self, ctx:SpeakParser.NameContext):
        pass


    # Enter a parse tree produced by SpeakParser#opinion.
    def enterOpinion(self, ctx:SpeakParser.OpinionContext):
        pass

    # Exit a parse tree produced by SpeakParser#opinion.
    def exitOpinion(self, ctx:SpeakParser.OpinionContext):
        pass



del SpeakParser