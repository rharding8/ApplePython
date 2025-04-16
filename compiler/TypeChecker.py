import sys
from antlr4 import *
sys.path.append('./')
from grammar.TypeWhileLexer import TypeWhileLexer
from grammar.TypeWhileParser import TypeWhileParser
from grammar.TypeWhileVisitor import TypeWhileVisitor
import logging
from textwrap import indent, dedent

symtab = {}  # E - environment

def check(condition, message):
    if not condition:
        sys.stderr.write(f"type error: {message}\n")
        exit(1)
    else:
        # no type error
        pass

class TypeChecker(TypeWhileVisitor):
  
    # Visit a parse tree produced by TypeWhileParser#Assignment.
    def visitAssignment(self, ctx:TypeWhileParser.AssignmentContext):
        check(ctx.ID().getText() in symtab, f"{ctx.ID().getText()} is undeclared")
        check(symtab[ctx.ID().getText()] == self.visit(ctx.e()), f"mismatch, {ctx.ID().getText()} is not {self.visit(ctx.e())} type")
        return None


    # Visit a parse tree produced by TypeWhileParser#Skip.
    def visitSkip(self, ctx:TypeWhileParser.SkipContext):
        return None


    # Visit a parse tree produced by TypeWhileParser#Compound.
    def visitCompound(self, ctx:TypeWhileParser.CompoundContext):
        [self.visit(s) for s in ctx.s()]
        return None


    # Visit a parse tree produced by TypeWhileParser#If.
    def visitIf(self, ctx:TypeWhileParser.IfContext):
        check(self.visit(ctx.e()) == "bool", "if condition not a 'bool'")
        self.visit(ctx.s(0))
        self.visit(ctx.s(1))
        return None


    # Visit a parse tree produced by TypeWhileParser#While.
    def visitWhile(self, ctx:TypeWhileParser.WhileContext):
        check(self.visit(ctx.e()) == "bool", "while condition not a 'bool'")
        self.visit(ctx.s())
        return None


    # Visit a parse tree produced by TypeWhileParser#Declaration.
    def visitDeclaration(self, ctx:TypeWhileParser.DeclarationContext):
        check(ctx.ID().getText() not in symtab, f"redeclaration of {ctx.ID().getText()}")
        match ctx.typeName.type:
            case TypeWhileParser.INT:
                return symtab.update({ctx.ID().getText(): ctx.INT().getText()})
            case TypeWhileParser.BOOL:
                return symtab.update({ctx.ID().getText(): ctx.BOOL().getText()})
            case _:
                check(False, "undefined error")
        return None


    # Visit a parse tree produced by TypeWhileParser#Not.
    def visitNot(self, ctx:TypeWhileParser.NotContext):
        check(self.visit(ctx.e()) == "bool", "only a 'bool' can be negated")
        return "bool"


    # Visit a parse tree produced by TypeWhileParser#Var.
    def visitVar(self, ctx:TypeWhileParser.VarContext):
        return symtab[ctx.ID().getText()]


    # Visit a parse tree produced by TypeWhileParser#Num.
    def visitNum(self, ctx:TypeWhileParser.NumContext):
        return "int"


    # Visit a parse tree produced by TypeWhileParser#True.
    def visitTrue(self, ctx:TypeWhileParser.TrueContext):
        return "bool"


    # Visit a parse tree produced by TypeWhileParser#False.
    def visitFalse(self, ctx:TypeWhileParser.FalseContext):
        return "bool"


    # Visit a parse tree produced by TypeWhileParser#BinOp.
    def visitBinOp(self, ctx:TypeWhileParser.BinOpContext):
        match ctx.op.type:
            case TypeWhileParser.PLUS | TypeWhileParser.MINUS | TypeWhileParser.MULT | TypeWhileParser.DIV:
                [check(self.visit(i) == "int", "operands must be ints") for i in ctx.e()]
                return "int"
            case TypeWhileParser.AND | TypeWhileParser.OR:
                [check(self.visit(b) == "bool", "operands must be bools") for b in ctx.e()]
                return "bool"
            case TypeWhileParser.EQ | TypeWhileParser.LT | TypeWhileParser.LE | TypeWhileParser.GT | TypeWhileParser.GE:
                [check(self.visit(i) == "int", "operands must be ints") for i in ctx.e()]
                return "bool"
        return None


    # Visit a parse tree produced by TypeWhileParser#Paren.
    def visitParen(self, ctx:TypeWhileParser.ParenContext):
        return self.visit(ctx.e())


input_stream = StdinStream()
lexer = TypeWhileLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = TypeWhileParser(stream)
tree = parser.s()
if parser.getNumberOfSyntaxErrors() > 0:
  print("syntax errors")
  exit(1)
typechecker = TypeChecker()
typechecker.visit(tree)
print("\n".join([ f"symtab[{name}]: {symtab[name]}" for name in symtab ]))
