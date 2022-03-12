from posixpath import split
import sys
from antlr4 import *
from more_itertools import first
from antlr.marzoLexer import marzoLexer
from antlr.marzoListener import marzoListener
from antlr.marzoParser import marzoParser
import re


# https://www.geeksforgeeks.org/cc-tokens/
# https://www.educative.io/edpresso/what-are-expressions-in-c


class GenCode(marzoListener):
    def __init__(self):
        self.list = []
        self.__dataMips = []
        self.__mainMips = []

    def enterProgram(self, ctx: marzoParser.ProgramContext):
        pass

    def enterAdd(self, ctx: marzoParser.AddContext):
        firstNum, secondNum = ctx.getText().split("+")
        self.__mainMips.append("li $t0, " + firstNum)
        self.__mainMips.append("li $t1, " + secondNum)
        self.__mainMips.append("add $t2, $t0, $t1")
        # print(ctx.getText())

    def enterDeclare(self, ctx: marzoParser.DeclareContext):
        varName = re.sub("int", "", ctx.getText())
        self.__dataMips.append(varName + ": .word NULL")
        # print(ctx.getText())

    def enterIfelse(self, ctx: marzoParser.IfelseContext):
        # Get if condition
        cond = re.search(r"\((.*?)\)", ctx.getText()).group(1)
        firstTokCond, secondTokCond = cond.split(">")

        # Get 'then' expressions
        then_exprs = re.search("then(.*)else", ctx.getText()).group(1)

        # Get 'else' expressions
        else_exprs = re.search("else(.*)end", ctx.getText()).group(1)

        # If (cond) then L1 else L2
        self.__mainMips.append("lw $t0, " + firstTokCond)
        self.__mainMips.append("li $t1, " + secondTokCond)
        self.__mainMips.append("bgt $t0, $t1, L1")
        self.__mainMips.append("j L2")

        # L1
        self.__mainMips.append("L1:")

        textToPrint = re.sub("print", "", then_exprs)
        self.__dataMips.append('out_string_L1: .asciiz "' + textToPrint + '"')

        self.__mainMips.append("li $v0, 4")
        self.__mainMips.append("la $a0, out_string_L1")
        self.__mainMips.append("syscall")
        self.__mainMips.append("j exit")

        # L2
        self.__mainMips.append("L2:")

        textToPrint = re.sub("print", "", else_exprs)
        self.__dataMips.append('out_string_L2: .asciiz "' + textToPrint + '"')

        self.__mainMips.append("li $v0, 4")
        self.__mainMips.append("la $a0, out_string_L2")
        self.__mainMips.append("syscall")
        self.__mainMips.append("j exit")

    def enterAssign(self, ctx: marzoParser.AssignContext):
        varName, value = ctx.getText().split("=")
        self.__mainMips.append("la $t0, " + varName)
        self.__mainMips.append("li $t1, " + value)
        self.__mainMips.append("sw $t1, 0($t0)")
        # print(ctx.getText())

    def enterGCond(self, ctx: marzoParser.GCondContext):
        firstNum, secondNum = ctx.getText().split(">")
        self.__mainMips.append("li $t0, " + firstNum)
        self.__mainMips.append("li $t1, " + secondNum)
        self.__mainMips.append("bgt $t1, $t0, exit")
        # print(ctx.getText())

    # https://courses.cs.vt.edu/cs2506/Spring2013/Notes/L04.MIPSAssemblyOverview.pdf
    def enterPrint(self, ctx: marzoParser.PrintContext):
        textToPrint = re.sub("print", "", ctx.getText())
        self.__dataMips.append('out_string: .asciiz "' + textToPrint + '"')
        self.__mainMips.append("li $v0, 4")
        self.__mainMips.append("la $a0, out_string")
        self.__mainMips.append("syscall")
        # print(ctx.getText())

    def exitProgram(self, ctx: marzoParser.ProgramContext):
        print(".data")
        for str_mips in self.__dataMips:
            print(str_mips)
        print(".text")
        print(".globl main")
        print("main:")
        for str_mips in self.__mainMips:
            print(str_mips)


#   https://github.com/antlr/antlr4/blob/master/doc/python-target.md
def main():
    input_stream = FileStream("input.txt")
    lexer = marzoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = marzoParser(stream)
    tree = parser.program()

    printer = GenCode()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == "__main__":
    main()
