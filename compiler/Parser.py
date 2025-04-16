import sys
from antlr4 import *
sys.path.append('./')  # if you want to avoid PYTHONPATH
from grammar.WhileLexer import WhileLexer
from grammar.WhileParser import WhileParser
from grammar.WhileVisitor import WhileVisitor
import logging
from textwrap import indent, dedent

class Printer(WhileVisitor):
    ind = 0
    
    # Visit a parse tree produced by WhileParser#Assignment.
    def visitAssignment(self, ctx:WhileParser.AssignmentContext):
        for i in range(0, self.ind):
            print('  ', end="")
        print(ctx.ID(), end="")
        print('',ctx.getToken(WhileParser.T__0, 0), end=" ")
        self.visitChildren(ctx)
        return


    # Visit a parse tree produced by WhileParser#Skip.
    def visitSkip(self, ctx:WhileParser.SkipContext):
        for i in range(0, self.ind):
            print('  ', end="")
        print(ctx.getToken(WhileParser.T__1, 0), end="")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#If.
    def visitIf(self, ctx:WhileParser.IfContext):
        for i in range(0, self.ind):
            print('  ', end="")
        print(ctx.getToken(WhileParser.T__5, 0), end=" ")
        self.visit(ctx.b())
        print('',ctx.getToken(WhileParser.T__6, 0))
        self.ind = self.ind + 1
        self.visit(ctx.s(0))
        print()
        for i in range(0, self.ind - 1):
            print('  ', end="")
        print(ctx.getToken(WhileParser.T__7, 0))
        self.visit(ctx.s(1))
        self.ind = self.ind - 1
        return


    # Visit a parse tree produced by WhileParser#While.
    def visitWhile(self, ctx:WhileParser.WhileContext):
        for i in range(0,self.ind):
            print('  ', end="")
        print(ctx.getToken(WhileParser.T__8, 0), end=" ")
        self.visit(ctx.b())
        print('', ctx.getToken(WhileParser.T__9, 0))
        self.ind = self.ind + 1
        self.visit(ctx.s())
        self.ind = self.ind - 1
        return


    # Visit a parse tree produced by WhileParser#Compound.
    def visitCompound(self, ctx:WhileParser.CompoundContext):
        for i in range(0, self.ind):
            print('  ', end="")
        print(ctx.getToken(WhileParser.T__2, 0))
        self.ind = self.ind + 1
        isFirst = True
        for c in ctx.s():
            if isFirst:
                isFirst = False
            else:
                print(ctx.getToken(WhileParser.T__3, 0))
            self.visit(c)
        print()
        for i in range(0, self.ind - 1):
            print('  ', end="")
        print(ctx.getToken(WhileParser.T__4, 0))
        self.ind = self.ind - 1
        return


    # Visit a parse tree produced by WhileParser#Not.
    def visitNot(self, ctx:WhileParser.NotContext):
        print(ctx.NOT(), end=" ")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#ROp.
    def visitROp(self, ctx:WhileParser.ROpContext):
        self.visit(ctx.a(0))
        print('', end=" ")
        match ctx.op.type:
            case WhileParser.LT:
                print(ctx.LT(), end=" ")
            case WhileParser.LE:
                print(ctx.LE(), end=" ")
            case WhileParser.EQ:
                print(ctx.EQ(), end=" ")
            case WhileParser.GT:
                print(ctx.GT(), end=" ")
            case WhileParser.GE:
                print(ctx.GE(), end=" ")
            case _:
                print("?", end=" ")
        self.visit(ctx.a(1))
        return


    # Visit a parse tree produced by WhileParser#Or.
    def visitOr(self, ctx:WhileParser.OrContext):
        self.visit(ctx.b(0))
        print('', ctx.OR(), end=" ")
        self.visit(ctx.b(1))
        return


    # Visit a parse tree produced by WhileParser#And.
    def visitAnd(self, ctx:WhileParser.AndContext):
        self.visit(ctx.b(0))
        print('', ctx.AND(), end=" ")
        self.visit(ctx.b(1))
        return


    # Visit a parse tree produced by WhileParser#True.
    def visitTrue(self, ctx:WhileParser.TrueContext):
        print(ctx.TRUE(), end="")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#False.
    def visitFalse(self, ctx:WhileParser.FalseContext):
        print(ctx.FALSE(), end="")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#BParen.
    def visitBParen(self, ctx:WhileParser.BParenContext):
        print(ctx.getToken(WhileParser.T__10, 0), end="")
        self.visitChildren(ctx)
        print(ctx.getToken(WhileParser.T__11, 0), end="")
        return


    # Visit a parse tree produced by WhileParser#AOp.
    def visitAOp(self, ctx:WhileParser.AOpContext):
        self.visit(ctx.a(0))
        print('', end=" ")
        match ctx.op.type:
            case WhileParser.PLUS:
                print(ctx.PLUS(), end=" ")
            case WhileParser.MINUS:
                print(ctx.MINUS(), end=" ")
            case WhileParser.MULT:
                print(ctx.MULT(), end=" ")
            case WhileParser.DIV:
                print(ctx.DIV(), end=" ")
            case _:
                print("?", end=" ")
        self.visit(ctx.a(1))
        return


    # Visit a parse tree produced by WhileParser#Var.
    def visitVar(self, ctx:WhileParser.VarContext):
        print(ctx.ID(), end="")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Num.
    def visitNum(self, ctx:WhileParser.NumContext):
        print(ctx.NUM(), end="")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#AParen.
    def visitAParen(self, ctx:WhileParser.AParenContext):
        print(ctx.getToken(WhileParser.T__10, 0), end="")
        self.visitChildren(ctx)
        print(ctx.getToken(WhileParser.T__11, 0), end="")
        return

input_stream = StdinStream()
lexer = WhileLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = WhileParser(stream)
tree = parser.s()
if parser.getNumberOfSyntaxErrors() > 0:
  print("syntax errors")
  exit(1)
printer = Printer()
printer.visit(tree)
