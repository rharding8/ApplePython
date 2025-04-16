import sys
from antlr4 import *
sys.path.append('./')  # if you want to avoid PYTHONPATH
from grammar.WhileLexer import WhileLexer
from grammar.WhileParser import WhileParser
from grammar.WhileVisitor import WhileVisitor
import logging
from textwrap import indent, dedent

symtab = {}

class Interpreter(WhileVisitor):
    # Visit a parse tree produced by WhileParser#Assignment.
    def visitAssignment(self, ctx:WhileParser.AssignmentContext):
        return symtab.update({ctx.ID().getText(): self.visit(ctx.a())})


    # Visit a parse tree produced by WhileParser#Skip.
    def visitSkip(self, ctx:WhileParser.SkipContext):
        return None


    # Visit a parse tree produced by WhileParser#If.
    def visitIf(self, ctx:WhileParser.IfContext):
        if (self.visit(ctx.b())):
            self.visit(ctx.s(0))
        else:
            self.visit(ctx.s(1))
        
        return None


    # Visit a parse tree produced by WhileParser#While.
    def visitWhile(self, ctx:WhileParser.WhileContext):
        while self.visit(ctx.b()):
            self.visit(ctx.s())
        return None


    # Visit a parse tree produced by WhileParser#Compound.
    def visitCompound(self, ctx:WhileParser.CompoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Not.
    def visitNot(self, ctx:WhileParser.NotContext):
        return not self.visit(ctx.b())


    # Visit a parse tree produced by WhileParser#ROp.
    def visitROp(self, ctx:WhileParser.ROpContext):
        a0 = self.visit(ctx.a(0))
        a1 = self.visit(ctx.a(1))
        match ctx.op.type:
            case WhileParser.LT:
                return a0 < a1
            case WhileParser.LE:
                return a0 <= a1
            case WhileParser.EQ:
                return a0 == a1
            case WhileParser.GT:
                return a0 > a1
            case WhileParser.GE:
                return a0 >= a1
            case _:
                return None
        return None


    # Visit a parse tree produced by WhileParser#Or.
    def visitOr(self, ctx:WhileParser.OrContext):
        return self.visit(ctx.b(0)) or self.visit(ctx.b(1))


    # Visit a parse tree produced by WhileParser#And.
    def visitAnd(self, ctx:WhileParser.AndContext):
        return self.visit(ctx.b(0)) and self.visit(ctx.b(1))


    # Visit a parse tree produced by WhileParser#True.
    def visitTrue(self, ctx:WhileParser.TrueContext):
        return True


    # Visit a parse tree produced by WhileParser#False.
    def visitFalse(self, ctx:WhileParser.FalseContext):
        return False


    # Visit a parse tree produced by WhileParser#BParen.
    def visitBParen(self, ctx:WhileParser.BParenContext):
        return self.visit(ctx.b())


    # Visit a parse tree produced by WhileParser#AOp.
    def visitAOp(self, ctx:WhileParser.AOpContext):
        a0 = int(self.visit(ctx.a(0)))
        a1 = int(self.visit(ctx.a(1)))
        match ctx.op.type:
            case WhileParser.PLUS:
                return str(a0 + a1)
            case WhileParser.MINUS:
                return str(a0 - a1)
            case WhileParser.MULT:
                return str(a0 * a1)
            case WhileParser.DIV:
                return str(int(a0 / a1))
            case _:
                return None
        return None


    # Visit a parse tree produced by WhileParser#Var.
    def visitVar(self, ctx:WhileParser.VarContext):
        return symtab[ctx.ID().getText()]


    # Visit a parse tree produced by WhileParser#Num.
    def visitNum(self, ctx:WhileParser.NumContext):
        return ctx.NUM().getText()


    # Visit a parse tree produced by WhileParser#AParen.
    def visitAParen(self, ctx:WhileParser.AParenContext):
        return self.visit(ctx.a())

input_stream = StdinStream()
lexer = WhileLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = WhileParser(stream)
tree = parser.s()
if parser.getNumberOfSyntaxErrors() > 0:
  print("syntax errors")
  exit(1)
interpreter = Interpreter()
interpreter.visit(tree)
print("\n".join([ f"symtab[{name}]: {symtab[name]}" for name in symtab ]))