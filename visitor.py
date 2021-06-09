from turtle3d import *

if __name__ is not None and "." in __name__:
    from .logo3dParser import logo3dParser
    from .logo3dVisitor import logo3dVisitor
else:
    from logo3dParser import logo3dParser
    from logo3dVisitor import logo3dVisitor


class Visitor(logo3dVisitor):
    def __init__(self):
        self.stack = []
        self.dictionary = {}
        self.procediments = {}
        self.started = False
        self.turtle = {}

    def visitRoot(self, ctx):
        children = list(ctx.getChildren())
        for i in children:
            self.visit(i)

    def visitDIV(self, ctx: logo3dParser.DIVContext):
        children = list(ctx.getChildren())
        op2 = self.visit(children[2])
        if op2 == 0:
            return "ZeroDivisionError: division by zero"
        else:
            return self.visit(children[0]) / op2

    def visitPOT(self, ctx: logo3dParser.POTContext):
        children = list(ctx.getChildren())
        return self.visit(children[0]) ** self.visit(children[2])

    def visitINT(self, ctx: logo3dParser.INTContext):
        children = list(ctx.getChildren())
        return int(children[0].getText())

    def visitBRACKETS(self, ctx: logo3dParser.BRACKETSContext):
        children = list(ctx.getChildren())
        return self.visit(children[1])

    def visitFLOAT(self, ctx: logo3dParser.FLOATContext):
        children = list(ctx.getChildren())
        return float(children[0].getText())

    def visitMULT(self, ctx: logo3dParser.MULTContext):
        children = list(ctx.getChildren())
        return self.visit(children[0]) * self.visit(children[2])

    def visitSUM(self, ctx: logo3dParser.SUMContext):
        children = list(ctx.getChildren())
        return self.visit(children[0]) + self.visit(children[2])

    def visitSUB(self, ctx: logo3dParser.SUBContext):
        children = list(ctx.getChildren())
        return self.visit(children[0]) - self.visit(children[2])

    def visitASSIGN(self, ctx: logo3dParser.ASSIGNContext):
        children = list(ctx.getChildren())
        self.dictionary[children[0].getText()] = self.visit(children[2])

    def visitWRITE(self, ctx: logo3dParser.WRITEContext):
        children = list(ctx.getChildren())
        print(self.visit(children[1]))

    def visitID(self, ctx: logo3dParser.IDContext):
        children = list(ctx.getChildren())
        return self.dictionary[children[0].getText()]

    def visitGTE(self, ctx: logo3dParser.GTEContext):
        children = list(ctx.getChildren())
        if self.visit(children[0]) >= self.visit(children[2]):
            return 1
        return 0

    def visitLTE(self, ctx: logo3dParser.LTEContext):
        children = list(ctx.getChildren())
        if self.visit(children[0]) <= self.visit(children[2]):
            return 1
        return 0

    def visitEQ(self, ctx: logo3dParser.EQContext):
        children = list(ctx.getChildren())
        if self.visit(children[0]) == self.visit(children[2]):
            return 1
        return 0

    def visitGT(self, ctx: logo3dParser.GTContext):
        children = list(ctx.getChildren())
        if self.visit(children[0]) > self.visit(children[2]):
            return 1
        return 0

    def visitLT(self, ctx: logo3dParser.LTContext):
        children = list(ctx.getChildren())
        if self.visit(children[0]) < self.visit(children[2]):
            return 1
        return 0

    def visitIF(self, ctx: logo3dParser.IFContext):
        children = list(ctx.getChildren())
        cond = self.visit(children[1])
        if cond < -1e-6 or cond > 1e-6:
            self.visit(children[3])
        else:
            if children[4].getText() == 'ELSE':
                self.visit(children[5])

    def visitDIF(self, ctx: logo3dParser.DIFContext):
        children = list(ctx.getChildren())
        if self.visit(children[0]) != self.visit(children[2]):
            return 1
        return 0

    def visitWHILE(self, ctx: logo3dParser.WHILEContext):
        children = list(ctx.getChildren())
        cond = self.visit(children[1])
        while cond < -1e-6 or cond > 1e-6:
            self.visit(children[3])
            cond = self.visit(children[1])

    def visitMAIN(self, ctx: logo3dParser.MAINContext):
        children = list(ctx.getChildren())
        name = children[1].getText()
        if self.procediments.get(name, "NOT REPEATED") != "NOT REPEATED":
            raise Exception("FUNCTION", name, "ALREADY DECLARED")
        args = {}
        bloc = children[len(children) - 2]
        self.procediments[name] = Procediment(args, bloc)

    def visitPROC(self, ctx: logo3dParser.PROCContext):
        children = list(ctx.getChildren())
        name = children[1].getText()
        if self.procediments.get(name, "NOT REPEATED") != "NOT REPEATED":
            raise Exception("FUNCTION", name, "ALREADY DECLARED")
        args = self.visit(children[3])
        bloc = children[len(children) - 2]
        self.procediments[name] = Procediment(args, bloc)

    def visitArgs(self, ctx: logo3dParser.ArgsContext):
        children = list(ctx.getChildren())
        dic = []
        for i in range(0, len(children)):
            if i % 2 == 0:
                dic.append(children[i].getText())
        return dic

    def visitCALLPROC(self, ctx: logo3dParser.CALLPROCContext):
        children = list(ctx.getChildren())
        self.visit(children[0])

    def visitCALLACTION(self, ctx: logo3dParser.CALLACTIONContext):
        children = list(ctx.getChildren())
        self.visit(children[0])

    # Prepares the call, saving the table of symbols in the stack and preparing
    # the list of parameters of the function
    def visitCall(self, ctx: logo3dParser.CallContext):
        children = list(ctx.getChildren())
        fun = self.procediments.get(children[0].getText(), "ERROR")
        if fun == "ERROR":
            raise Exception("NOT DEFINED PROCEDIMENT --> ",
                            children[0].getText())
        parameters = fun.get_parameters()
        if children[0].getText() != 'main()':
            args = self.visit(children[2])
        else:
            args = {}
        if len(args) != len(parameters):
            raise Exception("WRONG NUMBER OF PARAMETERS IN CALL "
                            "TO FUNCTION -->", children[0].getText())
        self.stack.append(self.dictionary)
        dic = self.dictionary
        self.dictionary = {}
        for i in range(0, len(args)):
            aux = args[i]
            size = len(aux)
            x = 0
            par = ""
            if aux[x] == '-':
                par = par + aux[x]
                x += 1
            while x < size and aux[x] != '-' and aux[x] != '+':
                par = par + aux[x]
                x += 1
            try:
                int(par)
                self.dictionary[parameters[i]] = int(par)
            except ValueError:
                try:
                    float(par)
                    self.dictionary[parameters[i]] = float(par)
                except ValueError:
                    self.dictionary[parameters[i]] = dic[par]
            while x < size:
                par = ""
                ite = x + 1
                while ite < size and aux[ite] != '-' and aux[ite] != '+':
                    par = par + aux[ite]
                    ite = ite + 1
                if "-" == aux[x]:
                    if str.isdigit(par):
                        self.dictionary[parameters[i]] = \
                            self.dictionary[parameters[i]] - int(par)
                    else:
                        self.dictionary[parameters[i]] = \
                            self.dictionary[parameters[i]] - dic[par]
                    x = ite
                elif "+" == aux[x]:
                    if str.isdigit(par):
                        self.dictionary[parameters[i]] = \
                            self.dictionary[parameters[i]] + int(par)
                    else:
                        self.dictionary[parameters[i]] = \
                            self.dictionary[parameters[i]] + dic[par]
                    x = ite
        res = self.visit(fun.get_context())
        self.dictionary = self.stack.pop()
        return res

    def visitREAD(self, ctx: logo3dParser.READContext):
        children = list(ctx.getChildren())
        input_stream = input('? ')
        self.dictionary[children[1].getText()] = int(input_stream)

    def visitFOR(self, ctx: logo3dParser.FORContext):
        children = list(ctx.getChildren())
        var = children[1].getText()
        self.dictionary[var] = self.visit(children[3])
        end = self.visit(children[5]) + 1
        start = self.dictionary[var]
        for i in range(start, end):
            self.visit(children[7])

    def visitCOLOR(self, ctx: logo3dParser.COLORContext):
        if not self.started:
            self.started = True
            self.turtle = Turtle3D()
        children = list(ctx.getChildren())
        col = [self.visit(children[2]),
               self.visit(children[4]),
               self.visit(children[6])]
        self.turtle.color(col)

    def visitFORWARD(self, ctx: logo3dParser.FORWARDContext):
        if not self.started:
            self.started = True
            self.turtle = Turtle3D()
        children = list(ctx.getChildren())
        self.turtle.forward(self.visit(children[2]))

    def visitLEFT(self, ctx: logo3dParser.LEFTContext):
        if not self.started:
            self.started = True
            self.turtle = Turtle3D()
        children = list(ctx.getChildren())
        self.turtle.left(self.visit(children[2]))

    def visitBACKWARD(self, ctx: logo3dParser.BACKWARDContext):
        if not self.started:
            self.started = True
            self.turtle = Turtle3D()
        children = list(ctx.getChildren())
        self.turtle.backward(self.visit(children[2]))

    def visitUP(self, ctx: logo3dParser.UPContext):
        if not self.started:
            self.started = True
            self.turtle = Turtle3D()
        children = list(ctx.getChildren())
        self.turtle.up(self.visit(children[2]))

    def visitDOWN(self, ctx: logo3dParser.DOWNContext):
        if not self.started:
            self.started = True
            self.turtle = Turtle3D()
        children = list(ctx.getChildren())
        self.turtle.down(self.visit(children[2]))

    def visitHIDE(self, ctx: logo3dParser.HIDEContext):
        if not self.started:
            self.started = True
            self.turtle = Turtle3D()
        self.turtle.hide()

    def visitHOME(self, ctx: logo3dParser.HOMEContext):
        if not self.started:
            self.started = True
            self.turtle = Turtle3D()
        self.turtle.home()

    def visitRIGHT(self, ctx: logo3dParser.RIGHTContext):
        if not self.started:
            self.started = True
            self.turtle = Turtle3D()
        children = list(ctx.getChildren())
        self.turtle.right(self.visit(children[2]))

    def visitSHOW(self, ctx: logo3dParser.SHOWContext):
        if not self.started:
            self.started = True
            self.turtle = Turtle3D()
        self.turtle.show()


class Procediment:
    def __init__(self, parameters, context):
        self.parameters = parameters
        self.context = context

    def get_parameters(self):
        return self.parameters

    def get_context(self):
        return self.context
