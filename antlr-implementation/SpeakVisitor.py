# Generated from .\Speak.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SpeakParser import SpeakParser
else:
    from SpeakParser import SpeakParser

# This class defines a complete generic visitor for a parse tree produced by SpeakParser.

class SpeakVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SpeakParser#prog.
    def visitProg(self, ctx:SpeakParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakParser#chat.
    def visitChat(self, ctx:SpeakParser.ChatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakParser#line.
    def visitLine(self, ctx:SpeakParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakParser#name.
    def visitName(self, ctx:SpeakParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakParser#opinion.
    def visitOpinion(self, ctx:SpeakParser.OpinionContext):
        return self.visitChildren(ctx)



del SpeakParser