# Generated from /home/lars/Files/Tec de Monterrey/Octavo Semestre/Compiladores/Primer parcial/Basic compiler/antlr/marzo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete listener for a parse tree produced by marzoParser.
class marzoListener(ParseTreeListener):

    # Enter a parse tree produced by marzoParser#program.
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        pass

    # Exit a parse tree produced by marzoParser#program.
    def exitProgram(self, ctx:marzoParser.ProgramContext):
        pass


    # Enter a parse tree produced by marzoParser#arithExpr.
    def enterArithExpr(self, ctx:marzoParser.ArithExprContext):
        pass

    # Exit a parse tree produced by marzoParser#arithExpr.
    def exitArithExpr(self, ctx:marzoParser.ArithExprContext):
        pass


    # Enter a parse tree produced by marzoParser#relationalExpr.
    def enterRelationalExpr(self, ctx:marzoParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by marzoParser#relationalExpr.
    def exitRelationalExpr(self, ctx:marzoParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by marzoParser#logicalExpr.
    def enterLogicalExpr(self, ctx:marzoParser.LogicalExprContext):
        pass

    # Exit a parse tree produced by marzoParser#logicalExpr.
    def exitLogicalExpr(self, ctx:marzoParser.LogicalExprContext):
        pass


    # Enter a parse tree produced by marzoParser#compExpr.
    def enterCompExpr(self, ctx:marzoParser.CompExprContext):
        pass

    # Exit a parse tree produced by marzoParser#compExpr.
    def exitCompExpr(self, ctx:marzoParser.CompExprContext):
        pass


    # Enter a parse tree produced by marzoParser#add.
    def enterAdd(self, ctx:marzoParser.AddContext):
        pass

    # Exit a parse tree produced by marzoParser#add.
    def exitAdd(self, ctx:marzoParser.AddContext):
        pass


    # Enter a parse tree produced by marzoParser#sub.
    def enterSub(self, ctx:marzoParser.SubContext):
        pass

    # Exit a parse tree produced by marzoParser#sub.
    def exitSub(self, ctx:marzoParser.SubContext):
        pass


    # Enter a parse tree produced by marzoParser#intNumber.
    def enterIntNumber(self, ctx:marzoParser.IntNumberContext):
        pass

    # Exit a parse tree produced by marzoParser#intNumber.
    def exitIntNumber(self, ctx:marzoParser.IntNumberContext):
        pass


    # Enter a parse tree produced by marzoParser#declare.
    def enterDeclare(self, ctx:marzoParser.DeclareContext):
        pass

    # Exit a parse tree produced by marzoParser#declare.
    def exitDeclare(self, ctx:marzoParser.DeclareContext):
        pass


    # Enter a parse tree produced by marzoParser#assign.
    def enterAssign(self, ctx:marzoParser.AssignContext):
        pass

    # Exit a parse tree produced by marzoParser#assign.
    def exitAssign(self, ctx:marzoParser.AssignContext):
        pass


    # Enter a parse tree produced by marzoParser#gCond.
    def enterGCond(self, ctx:marzoParser.GCondContext):
        pass

    # Exit a parse tree produced by marzoParser#gCond.
    def exitGCond(self, ctx:marzoParser.GCondContext):
        pass


    # Enter a parse tree produced by marzoParser#goeCond.
    def enterGoeCond(self, ctx:marzoParser.GoeCondContext):
        pass

    # Exit a parse tree produced by marzoParser#goeCond.
    def exitGoeCond(self, ctx:marzoParser.GoeCondContext):
        pass


    # Enter a parse tree produced by marzoParser#orCond.
    def enterOrCond(self, ctx:marzoParser.OrCondContext):
        pass

    # Exit a parse tree produced by marzoParser#orCond.
    def exitOrCond(self, ctx:marzoParser.OrCondContext):
        pass


    # Enter a parse tree produced by marzoParser#identCond.
    def enterIdentCond(self, ctx:marzoParser.IdentCondContext):
        pass

    # Exit a parse tree produced by marzoParser#identCond.
    def exitIdentCond(self, ctx:marzoParser.IdentCondContext):
        pass


    # Enter a parse tree produced by marzoParser#intNumberCond.
    def enterIntNumberCond(self, ctx:marzoParser.IntNumberCondContext):
        pass

    # Exit a parse tree produced by marzoParser#intNumberCond.
    def exitIntNumberCond(self, ctx:marzoParser.IntNumberCondContext):
        pass


    # Enter a parse tree produced by marzoParser#andCond.
    def enterAndCond(self, ctx:marzoParser.AndCondContext):
        pass

    # Exit a parse tree produced by marzoParser#andCond.
    def exitAndCond(self, ctx:marzoParser.AndCondContext):
        pass


    # Enter a parse tree produced by marzoParser#lCond.
    def enterLCond(self, ctx:marzoParser.LCondContext):
        pass

    # Exit a parse tree produced by marzoParser#lCond.
    def exitLCond(self, ctx:marzoParser.LCondContext):
        pass


    # Enter a parse tree produced by marzoParser#loeCond.
    def enterLoeCond(self, ctx:marzoParser.LoeCondContext):
        pass

    # Exit a parse tree produced by marzoParser#loeCond.
    def exitLoeCond(self, ctx:marzoParser.LoeCondContext):
        pass


    # Enter a parse tree produced by marzoParser#notCond.
    def enterNotCond(self, ctx:marzoParser.NotCondContext):
        pass

    # Exit a parse tree produced by marzoParser#notCond.
    def exitNotCond(self, ctx:marzoParser.NotCondContext):
        pass


    # Enter a parse tree produced by marzoParser#ifnoelse.
    def enterIfnoelse(self, ctx:marzoParser.IfnoelseContext):
        pass

    # Exit a parse tree produced by marzoParser#ifnoelse.
    def exitIfnoelse(self, ctx:marzoParser.IfnoelseContext):
        pass


    # Enter a parse tree produced by marzoParser#ifelse.
    def enterIfelse(self, ctx:marzoParser.IfelseContext):
        pass

    # Exit a parse tree produced by marzoParser#ifelse.
    def exitIfelse(self, ctx:marzoParser.IfelseContext):
        pass


    # Enter a parse tree produced by marzoParser#print.
    def enterPrint(self, ctx:marzoParser.PrintContext):
        pass

    # Exit a parse tree produced by marzoParser#print.
    def exitPrint(self, ctx:marzoParser.PrintContext):
        pass


    # Enter a parse tree produced by marzoParser#print_op.
    def enterPrint_op(self, ctx:marzoParser.Print_opContext):
        pass

    # Exit a parse tree produced by marzoParser#print_op.
    def exitPrint_op(self, ctx:marzoParser.Print_opContext):
        pass


    # Enter a parse tree produced by marzoParser#assignment.
    def enterAssignment(self, ctx:marzoParser.AssignmentContext):
        pass

    # Exit a parse tree produced by marzoParser#assignment.
    def exitAssignment(self, ctx:marzoParser.AssignmentContext):
        pass


    # Enter a parse tree produced by marzoParser#declaration.
    def enterDeclaration(self, ctx:marzoParser.DeclarationContext):
        pass

    # Exit a parse tree produced by marzoParser#declaration.
    def exitDeclaration(self, ctx:marzoParser.DeclarationContext):
        pass



del marzoParser