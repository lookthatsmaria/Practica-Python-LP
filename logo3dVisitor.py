# Generated from logo3d.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .logo3dParser import logo3dParser
else:
    from logo3dParser import logo3dParser

# This class defines a complete generic visitor for a parse tree produced by logo3dParser.

class logo3dVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by logo3dParser#root.
    def visitRoot(self, ctx:logo3dParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#args.
    def visitArgs(self, ctx:logo3dParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#call.
    def visitCall(self, ctx:logo3dParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#CALLPROC.
    def visitCALLPROC(self, ctx:logo3dParser.CALLPROCContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#MAIN.
    def visitMAIN(self, ctx:logo3dParser.MAINContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#PROC.
    def visitPROC(self, ctx:logo3dParser.PROCContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#block.
    def visitBlock(self, ctx:logo3dParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#ASSIGN.
    def visitASSIGN(self, ctx:logo3dParser.ASSIGNContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#WRITE.
    def visitWRITE(self, ctx:logo3dParser.WRITEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#IF.
    def visitIF(self, ctx:logo3dParser.IFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#WHILE.
    def visitWHILE(self, ctx:logo3dParser.WHILEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#FOR.
    def visitFOR(self, ctx:logo3dParser.FORContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#READ.
    def visitREAD(self, ctx:logo3dParser.READContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#COLOR.
    def visitCOLOR(self, ctx:logo3dParser.COLORContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#FORWARD.
    def visitFORWARD(self, ctx:logo3dParser.FORWARDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#BACKWARD.
    def visitBACKWARD(self, ctx:logo3dParser.BACKWARDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#LEFT.
    def visitLEFT(self, ctx:logo3dParser.LEFTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#RIGHT.
    def visitRIGHT(self, ctx:logo3dParser.RIGHTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#UP.
    def visitUP(self, ctx:logo3dParser.UPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#DOWN.
    def visitDOWN(self, ctx:logo3dParser.DOWNContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#HOME.
    def visitHOME(self, ctx:logo3dParser.HOMEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#HIDE.
    def visitHIDE(self, ctx:logo3dParser.HIDEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#SHOW.
    def visitSHOW(self, ctx:logo3dParser.SHOWContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#CALLACTION.
    def visitCALLACTION(self, ctx:logo3dParser.CALLACTIONContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#EQ.
    def visitEQ(self, ctx:logo3dParser.EQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#GT.
    def visitGT(self, ctx:logo3dParser.GTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#GTE.
    def visitGTE(self, ctx:logo3dParser.GTEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#LT.
    def visitLT(self, ctx:logo3dParser.LTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#LTE.
    def visitLTE(self, ctx:logo3dParser.LTEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#DIF.
    def visitDIF(self, ctx:logo3dParser.DIFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#integernumber.
    def visitIntegernumber(self, ctx:logo3dParser.IntegernumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#floatnumber.
    def visitFloatnumber(self, ctx:logo3dParser.FloatnumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#DIV.
    def visitDIV(self, ctx:logo3dParser.DIVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#BRACKETS.
    def visitBRACKETS(self, ctx:logo3dParser.BRACKETSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#SUB.
    def visitSUB(self, ctx:logo3dParser.SUBContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#FLOAT.
    def visitFLOAT(self, ctx:logo3dParser.FLOATContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#POT.
    def visitPOT(self, ctx:logo3dParser.POTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#MULT.
    def visitMULT(self, ctx:logo3dParser.MULTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#SUM.
    def visitSUM(self, ctx:logo3dParser.SUMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#ID.
    def visitID(self, ctx:logo3dParser.IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#INT.
    def visitINT(self, ctx:logo3dParser.INTContext):
        return self.visitChildren(ctx)



del logo3dParser