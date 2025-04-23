# Generated from pyBasic.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .pyBasicParser import pyBasicParser
else:
    from pyBasicParser import pyBasicParser

# This class defines a complete generic visitor for a parse tree produced by pyBasicParser.

class pyBasicVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pyBasicParser#prog.
    def visitProg(self, ctx:pyBasicParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#line.
    def visitLine(self, ctx:pyBasicParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#linenumber.
    def visitLinenumber(self, ctx:pyBasicParser.LinenumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#AmperStatement.
    def visitAmperStatement(self, ctx:pyBasicParser.AmperStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#CommentStatement.
    def visitCommentStatement(self, ctx:pyBasicParser.CommentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#RemStatement.
    def visitRemStatement(self, ctx:pyBasicParser.RemStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#HomeStatement.
    def visitHomeStatement(self, ctx:pyBasicParser.HomeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#StopStatement.
    def visitStopStatement(self, ctx:pyBasicParser.StopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#EndStatement.
    def visitEndStatement(self, ctx:pyBasicParser.EndStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#ReturnStatement.
    def visitReturnStatement(self, ctx:pyBasicParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#RestoreStatement.
    def visitRestoreStatement(self, ctx:pyBasicParser.RestoreStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#GetStatement.
    def visitGetStatement(self, ctx:pyBasicParser.GetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#NextStatement.
    def visitNextStatement(self, ctx:pyBasicParser.NextStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#PrintStatement.
    def visitPrintStatement(self, ctx:pyBasicParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#IfStatement.
    def visitIfStatement(self, ctx:pyBasicParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#InLineForStatement.
    def visitInLineForStatement(self, ctx:pyBasicParser.InLineForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#ForStatement.
    def visitForStatement(self, ctx:pyBasicParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#InputStatement.
    def visitInputStatement(self, ctx:pyBasicParser.InputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#TabStatement.
    def visitTabStatement(self, ctx:pyBasicParser.TabStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#DimStatement.
    def visitDimStatement(self, ctx:pyBasicParser.DimStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#GotoStatement.
    def visitGotoStatement(self, ctx:pyBasicParser.GotoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#GosubStatement.
    def visitGosubStatement(self, ctx:pyBasicParser.GosubStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#ReadStatement.
    def visitReadStatement(self, ctx:pyBasicParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#DataStatement.
    def visitDataStatement(self, ctx:pyBasicParser.DataStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#DefStatement.
    def visitDefStatement(self, ctx:pyBasicParser.DefStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#LetStatement.
    def visitLetStatement(self, ctx:pyBasicParser.LetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#vardecl.
    def visitVardecl(self, ctx:pyBasicParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#printlist.
    def visitPrintlist(self, ctx:pyBasicParser.PrintlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#printseparator.
    def visitPrintseparator(self, ctx:pyBasicParser.PrintseparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#datum.
    def visitDatum(self, ctx:pyBasicParser.DatumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#number.
    def visitNumber(self, ctx:pyBasicParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#StringLiteralFunction.
    def visitStringLiteralFunction(self, ctx:pyBasicParser.StringLiteralFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#NumberFunction.
    def visitNumberFunction(self, ctx:pyBasicParser.NumberFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#TabFunction.
    def visitTabFunction(self, ctx:pyBasicParser.TabFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#DeclarationFunction.
    def visitDeclarationFunction(self, ctx:pyBasicParser.DeclarationFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#CharacterFunction.
    def visitCharacterFunction(self, ctx:pyBasicParser.CharacterFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#SquareRootFunction.
    def visitSquareRootFunction(self, ctx:pyBasicParser.SquareRootFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#LengthFunction.
    def visitLengthFunction(self, ctx:pyBasicParser.LengthFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#StringFunction.
    def visitStringFunction(self, ctx:pyBasicParser.StringFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#AsciiFunction.
    def visitAsciiFunction(self, ctx:pyBasicParser.AsciiFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#MidFunction.
    def visitMidFunction(self, ctx:pyBasicParser.MidFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#LargestIntegerFunction.
    def visitLargestIntegerFunction(self, ctx:pyBasicParser.LargestIntegerFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#SpcFunction.
    def visitSpcFunction(self, ctx:pyBasicParser.SpcFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#LeftFunction.
    def visitLeftFunction(self, ctx:pyBasicParser.LeftFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#ValueFunction.
    def visitValueFunction(self, ctx:pyBasicParser.ValueFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#RightFunction.
    def visitRightFunction(self, ctx:pyBasicParser.RightFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#FnFunction.
    def visitFnFunction(self, ctx:pyBasicParser.FnFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#SinFunction.
    def visitSinFunction(self, ctx:pyBasicParser.SinFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#CosFunction.
    def visitCosFunction(self, ctx:pyBasicParser.CosFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#TanFunction.
    def visitTanFunction(self, ctx:pyBasicParser.TanFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#ArcTanFunction.
    def visitArcTanFunction(self, ctx:pyBasicParser.ArcTanFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#RandFunction.
    def visitRandFunction(self, ctx:pyBasicParser.RandFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#SignFunction.
    def visitSignFunction(self, ctx:pyBasicParser.SignFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#ExpFunction.
    def visitExpFunction(self, ctx:pyBasicParser.ExpFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#NaturalLogFunction.
    def visitNaturalLogFunction(self, ctx:pyBasicParser.NaturalLogFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#AbsoluteFunction.
    def visitAbsoluteFunction(self, ctx:pyBasicParser.AbsoluteFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#ParentheticalFunction.
    def visitParentheticalFunction(self, ctx:pyBasicParser.ParentheticalFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#signExpression.
    def visitSignExpression(self, ctx:pyBasicParser.SignExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#exponentExpression.
    def visitExponentExpression(self, ctx:pyBasicParser.ExponentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#multiplyingExpression.
    def visitMultiplyingExpression(self, ctx:pyBasicParser.MultiplyingExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#addingExpression.
    def visitAddingExpression(self, ctx:pyBasicParser.AddingExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#relationalExpression.
    def visitRelationalExpression(self, ctx:pyBasicParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#expression.
    def visitExpression(self, ctx:pyBasicParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#var_.
    def visitVar_(self, ctx:pyBasicParser.Var_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#varname.
    def visitVarname(self, ctx:pyBasicParser.VarnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyBasicParser#varsuffix.
    def visitVarsuffix(self, ctx:pyBasicParser.VarsuffixContext):
        return self.visitChildren(ctx)



del pyBasicParser