# Generated from pyBasic.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .pyBasicParser import pyBasicParser
else:
    from pyBasicParser import pyBasicParser

# This class defines a complete listener for a parse tree produced by pyBasicParser.
class pyBasicListener(ParseTreeListener):

    # Enter a parse tree produced by pyBasicParser#prog.
    def enterProg(self, ctx:pyBasicParser.ProgContext):
        pass

    # Exit a parse tree produced by pyBasicParser#prog.
    def exitProg(self, ctx:pyBasicParser.ProgContext):
        pass


    # Enter a parse tree produced by pyBasicParser#line.
    def enterLine(self, ctx:pyBasicParser.LineContext):
        pass

    # Exit a parse tree produced by pyBasicParser#line.
    def exitLine(self, ctx:pyBasicParser.LineContext):
        pass


    # Enter a parse tree produced by pyBasicParser#linenumber.
    def enterLinenumber(self, ctx:pyBasicParser.LinenumberContext):
        pass

    # Exit a parse tree produced by pyBasicParser#linenumber.
    def exitLinenumber(self, ctx:pyBasicParser.LinenumberContext):
        pass


    # Enter a parse tree produced by pyBasicParser#AmperStatement.
    def enterAmperStatement(self, ctx:pyBasicParser.AmperStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#AmperStatement.
    def exitAmperStatement(self, ctx:pyBasicParser.AmperStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#CommentStatement.
    def enterCommentStatement(self, ctx:pyBasicParser.CommentStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#CommentStatement.
    def exitCommentStatement(self, ctx:pyBasicParser.CommentStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#RemStatement.
    def enterRemStatement(self, ctx:pyBasicParser.RemStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#RemStatement.
    def exitRemStatement(self, ctx:pyBasicParser.RemStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#HomeStatement.
    def enterHomeStatement(self, ctx:pyBasicParser.HomeStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#HomeStatement.
    def exitHomeStatement(self, ctx:pyBasicParser.HomeStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#StopStatement.
    def enterStopStatement(self, ctx:pyBasicParser.StopStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#StopStatement.
    def exitStopStatement(self, ctx:pyBasicParser.StopStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#EndStatement.
    def enterEndStatement(self, ctx:pyBasicParser.EndStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#EndStatement.
    def exitEndStatement(self, ctx:pyBasicParser.EndStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#ReturnStatement.
    def enterReturnStatement(self, ctx:pyBasicParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#ReturnStatement.
    def exitReturnStatement(self, ctx:pyBasicParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#RestoreStatement.
    def enterRestoreStatement(self, ctx:pyBasicParser.RestoreStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#RestoreStatement.
    def exitRestoreStatement(self, ctx:pyBasicParser.RestoreStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#GetStatement.
    def enterGetStatement(self, ctx:pyBasicParser.GetStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#GetStatement.
    def exitGetStatement(self, ctx:pyBasicParser.GetStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#NextStatement.
    def enterNextStatement(self, ctx:pyBasicParser.NextStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#NextStatement.
    def exitNextStatement(self, ctx:pyBasicParser.NextStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#PrintStatement.
    def enterPrintStatement(self, ctx:pyBasicParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#PrintStatement.
    def exitPrintStatement(self, ctx:pyBasicParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#IfStatement.
    def enterIfStatement(self, ctx:pyBasicParser.IfStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#IfStatement.
    def exitIfStatement(self, ctx:pyBasicParser.IfStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#InLineForStatement.
    def enterInLineForStatement(self, ctx:pyBasicParser.InLineForStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#InLineForStatement.
    def exitInLineForStatement(self, ctx:pyBasicParser.InLineForStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#ForStatement.
    def enterForStatement(self, ctx:pyBasicParser.ForStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#ForStatement.
    def exitForStatement(self, ctx:pyBasicParser.ForStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#InputStatement.
    def enterInputStatement(self, ctx:pyBasicParser.InputStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#InputStatement.
    def exitInputStatement(self, ctx:pyBasicParser.InputStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#TabStatement.
    def enterTabStatement(self, ctx:pyBasicParser.TabStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#TabStatement.
    def exitTabStatement(self, ctx:pyBasicParser.TabStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#DimStatement.
    def enterDimStatement(self, ctx:pyBasicParser.DimStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#DimStatement.
    def exitDimStatement(self, ctx:pyBasicParser.DimStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#GotoStatement.
    def enterGotoStatement(self, ctx:pyBasicParser.GotoStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#GotoStatement.
    def exitGotoStatement(self, ctx:pyBasicParser.GotoStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#GosubStatement.
    def enterGosubStatement(self, ctx:pyBasicParser.GosubStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#GosubStatement.
    def exitGosubStatement(self, ctx:pyBasicParser.GosubStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#ReadStatement.
    def enterReadStatement(self, ctx:pyBasicParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#ReadStatement.
    def exitReadStatement(self, ctx:pyBasicParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#DataStatement.
    def enterDataStatement(self, ctx:pyBasicParser.DataStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#DataStatement.
    def exitDataStatement(self, ctx:pyBasicParser.DataStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#DefStatement.
    def enterDefStatement(self, ctx:pyBasicParser.DefStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#DefStatement.
    def exitDefStatement(self, ctx:pyBasicParser.DefStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#LetStatement.
    def enterLetStatement(self, ctx:pyBasicParser.LetStatementContext):
        pass

    # Exit a parse tree produced by pyBasicParser#LetStatement.
    def exitLetStatement(self, ctx:pyBasicParser.LetStatementContext):
        pass


    # Enter a parse tree produced by pyBasicParser#vardecl.
    def enterVardecl(self, ctx:pyBasicParser.VardeclContext):
        pass

    # Exit a parse tree produced by pyBasicParser#vardecl.
    def exitVardecl(self, ctx:pyBasicParser.VardeclContext):
        pass


    # Enter a parse tree produced by pyBasicParser#printlist.
    def enterPrintlist(self, ctx:pyBasicParser.PrintlistContext):
        pass

    # Exit a parse tree produced by pyBasicParser#printlist.
    def exitPrintlist(self, ctx:pyBasicParser.PrintlistContext):
        pass


    # Enter a parse tree produced by pyBasicParser#printseparator.
    def enterPrintseparator(self, ctx:pyBasicParser.PrintseparatorContext):
        pass

    # Exit a parse tree produced by pyBasicParser#printseparator.
    def exitPrintseparator(self, ctx:pyBasicParser.PrintseparatorContext):
        pass


    # Enter a parse tree produced by pyBasicParser#datum.
    def enterDatum(self, ctx:pyBasicParser.DatumContext):
        pass

    # Exit a parse tree produced by pyBasicParser#datum.
    def exitDatum(self, ctx:pyBasicParser.DatumContext):
        pass


    # Enter a parse tree produced by pyBasicParser#number.
    def enterNumber(self, ctx:pyBasicParser.NumberContext):
        pass

    # Exit a parse tree produced by pyBasicParser#number.
    def exitNumber(self, ctx:pyBasicParser.NumberContext):
        pass


    # Enter a parse tree produced by pyBasicParser#StringLiteralFunction.
    def enterStringLiteralFunction(self, ctx:pyBasicParser.StringLiteralFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#StringLiteralFunction.
    def exitStringLiteralFunction(self, ctx:pyBasicParser.StringLiteralFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#NumberFunction.
    def enterNumberFunction(self, ctx:pyBasicParser.NumberFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#NumberFunction.
    def exitNumberFunction(self, ctx:pyBasicParser.NumberFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#TabFunction.
    def enterTabFunction(self, ctx:pyBasicParser.TabFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#TabFunction.
    def exitTabFunction(self, ctx:pyBasicParser.TabFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#DeclarationFunction.
    def enterDeclarationFunction(self, ctx:pyBasicParser.DeclarationFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#DeclarationFunction.
    def exitDeclarationFunction(self, ctx:pyBasicParser.DeclarationFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#CharacterFunction.
    def enterCharacterFunction(self, ctx:pyBasicParser.CharacterFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#CharacterFunction.
    def exitCharacterFunction(self, ctx:pyBasicParser.CharacterFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#SquareRootFunction.
    def enterSquareRootFunction(self, ctx:pyBasicParser.SquareRootFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#SquareRootFunction.
    def exitSquareRootFunction(self, ctx:pyBasicParser.SquareRootFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#LengthFunction.
    def enterLengthFunction(self, ctx:pyBasicParser.LengthFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#LengthFunction.
    def exitLengthFunction(self, ctx:pyBasicParser.LengthFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#StringFunction.
    def enterStringFunction(self, ctx:pyBasicParser.StringFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#StringFunction.
    def exitStringFunction(self, ctx:pyBasicParser.StringFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#AsciiFunction.
    def enterAsciiFunction(self, ctx:pyBasicParser.AsciiFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#AsciiFunction.
    def exitAsciiFunction(self, ctx:pyBasicParser.AsciiFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#MidFunction.
    def enterMidFunction(self, ctx:pyBasicParser.MidFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#MidFunction.
    def exitMidFunction(self, ctx:pyBasicParser.MidFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#LargestIntegerFunction.
    def enterLargestIntegerFunction(self, ctx:pyBasicParser.LargestIntegerFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#LargestIntegerFunction.
    def exitLargestIntegerFunction(self, ctx:pyBasicParser.LargestIntegerFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#SpcFunction.
    def enterSpcFunction(self, ctx:pyBasicParser.SpcFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#SpcFunction.
    def exitSpcFunction(self, ctx:pyBasicParser.SpcFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#LeftFunction.
    def enterLeftFunction(self, ctx:pyBasicParser.LeftFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#LeftFunction.
    def exitLeftFunction(self, ctx:pyBasicParser.LeftFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#ValueFunction.
    def enterValueFunction(self, ctx:pyBasicParser.ValueFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#ValueFunction.
    def exitValueFunction(self, ctx:pyBasicParser.ValueFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#RightFunction.
    def enterRightFunction(self, ctx:pyBasicParser.RightFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#RightFunction.
    def exitRightFunction(self, ctx:pyBasicParser.RightFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#FnFunction.
    def enterFnFunction(self, ctx:pyBasicParser.FnFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#FnFunction.
    def exitFnFunction(self, ctx:pyBasicParser.FnFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#SinFunction.
    def enterSinFunction(self, ctx:pyBasicParser.SinFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#SinFunction.
    def exitSinFunction(self, ctx:pyBasicParser.SinFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#CosFunction.
    def enterCosFunction(self, ctx:pyBasicParser.CosFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#CosFunction.
    def exitCosFunction(self, ctx:pyBasicParser.CosFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#TanFunction.
    def enterTanFunction(self, ctx:pyBasicParser.TanFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#TanFunction.
    def exitTanFunction(self, ctx:pyBasicParser.TanFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#ArcTanFunction.
    def enterArcTanFunction(self, ctx:pyBasicParser.ArcTanFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#ArcTanFunction.
    def exitArcTanFunction(self, ctx:pyBasicParser.ArcTanFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#RandFunction.
    def enterRandFunction(self, ctx:pyBasicParser.RandFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#RandFunction.
    def exitRandFunction(self, ctx:pyBasicParser.RandFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#SignFunction.
    def enterSignFunction(self, ctx:pyBasicParser.SignFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#SignFunction.
    def exitSignFunction(self, ctx:pyBasicParser.SignFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#ExpFunction.
    def enterExpFunction(self, ctx:pyBasicParser.ExpFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#ExpFunction.
    def exitExpFunction(self, ctx:pyBasicParser.ExpFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#NaturalLogFunction.
    def enterNaturalLogFunction(self, ctx:pyBasicParser.NaturalLogFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#NaturalLogFunction.
    def exitNaturalLogFunction(self, ctx:pyBasicParser.NaturalLogFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#AbsoluteFunction.
    def enterAbsoluteFunction(self, ctx:pyBasicParser.AbsoluteFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#AbsoluteFunction.
    def exitAbsoluteFunction(self, ctx:pyBasicParser.AbsoluteFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#ParentheticalFunction.
    def enterParentheticalFunction(self, ctx:pyBasicParser.ParentheticalFunctionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#ParentheticalFunction.
    def exitParentheticalFunction(self, ctx:pyBasicParser.ParentheticalFunctionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#signExpression.
    def enterSignExpression(self, ctx:pyBasicParser.SignExpressionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#signExpression.
    def exitSignExpression(self, ctx:pyBasicParser.SignExpressionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#exponentExpression.
    def enterExponentExpression(self, ctx:pyBasicParser.ExponentExpressionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#exponentExpression.
    def exitExponentExpression(self, ctx:pyBasicParser.ExponentExpressionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#multiplyingExpression.
    def enterMultiplyingExpression(self, ctx:pyBasicParser.MultiplyingExpressionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#multiplyingExpression.
    def exitMultiplyingExpression(self, ctx:pyBasicParser.MultiplyingExpressionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#addingExpression.
    def enterAddingExpression(self, ctx:pyBasicParser.AddingExpressionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#addingExpression.
    def exitAddingExpression(self, ctx:pyBasicParser.AddingExpressionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#relationalExpression.
    def enterRelationalExpression(self, ctx:pyBasicParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#relationalExpression.
    def exitRelationalExpression(self, ctx:pyBasicParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#expression.
    def enterExpression(self, ctx:pyBasicParser.ExpressionContext):
        pass

    # Exit a parse tree produced by pyBasicParser#expression.
    def exitExpression(self, ctx:pyBasicParser.ExpressionContext):
        pass


    # Enter a parse tree produced by pyBasicParser#var_.
    def enterVar_(self, ctx:pyBasicParser.Var_Context):
        pass

    # Exit a parse tree produced by pyBasicParser#var_.
    def exitVar_(self, ctx:pyBasicParser.Var_Context):
        pass


    # Enter a parse tree produced by pyBasicParser#varname.
    def enterVarname(self, ctx:pyBasicParser.VarnameContext):
        pass

    # Exit a parse tree produced by pyBasicParser#varname.
    def exitVarname(self, ctx:pyBasicParser.VarnameContext):
        pass


    # Enter a parse tree produced by pyBasicParser#varsuffix.
    def enterVarsuffix(self, ctx:pyBasicParser.VarsuffixContext):
        pass

    # Exit a parse tree produced by pyBasicParser#varsuffix.
    def exitVarsuffix(self, ctx:pyBasicParser.VarsuffixContext):
        pass



del pyBasicParser