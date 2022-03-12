# Generated from /home/lars/Files/Tec de Monterrey/Octavo Semestre/Compiladores/Primer parcial/Basic compiler/antlr/marzo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete generic visitor for a parse tree produced by marzoParser.

class marzoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by marzoParser#program.
    def visitProgram(self, ctx:marzoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#arithExpr.
    def visitArithExpr(self, ctx:marzoParser.ArithExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#relationalExpr.
    def visitRelationalExpr(self, ctx:marzoParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#logicalExpr.
    def visitLogicalExpr(self, ctx:marzoParser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#compExpr.
    def visitCompExpr(self, ctx:marzoParser.CompExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#add.
    def visitAdd(self, ctx:marzoParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#sub.
    def visitSub(self, ctx:marzoParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#intNumber.
    def visitIntNumber(self, ctx:marzoParser.IntNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#declare.
    def visitDeclare(self, ctx:marzoParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#assign.
    def visitAssign(self, ctx:marzoParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#gCond.
    def visitGCond(self, ctx:marzoParser.GCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#goeCond.
    def visitGoeCond(self, ctx:marzoParser.GoeCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#orCond.
    def visitOrCond(self, ctx:marzoParser.OrCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#identCond.
    def visitIdentCond(self, ctx:marzoParser.IdentCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#intNumberCond.
    def visitIntNumberCond(self, ctx:marzoParser.IntNumberCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#andCond.
    def visitAndCond(self, ctx:marzoParser.AndCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#lCond.
    def visitLCond(self, ctx:marzoParser.LCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#loeCond.
    def visitLoeCond(self, ctx:marzoParser.LoeCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#notCond.
    def visitNotCond(self, ctx:marzoParser.NotCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#ifnoelse.
    def visitIfnoelse(self, ctx:marzoParser.IfnoelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#ifelse.
    def visitIfelse(self, ctx:marzoParser.IfelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#print.
    def visitPrint(self, ctx:marzoParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#print_op.
    def visitPrint_op(self, ctx:marzoParser.Print_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#assignment.
    def visitAssignment(self, ctx:marzoParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#declaration.
    def visitDeclaration(self, ctx:marzoParser.DeclarationContext):
        return self.visitChildren(ctx)



del marzoParser