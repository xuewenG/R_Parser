import chart.dev as dev
from atom.Class import class_r
from chart.Bar import barplot
from chart.Config import png
from chart.Hist import hist
from chart.Pie import pie
from chart.Plot import plot
from container.Matrix import matrix
from container.Vector import c
from exception.IdNotFoundException import IdNotFoundException
from exception.MissingArgumentException import MissingArgumentException
from exception.SyntaxException import SyntaxException
from interpreter.Lex import lex
from interpreter.Tables import keyword_table
from util.Length import length
from util.Printer import print_n
from util.Printer import print_r
from util.Rainbow import rainbow


def process_line(line):
    words = lex(line)
    if words[0] == 'print':
        process_print(words[2:-1])


def process_print(params):
    if params[0] == 'c':
        params = params[2:-1]
        params = filter(lambda item: item != ',', params)
        params = tuple(map(int, params))
    else:
        keyword_table[params[0]].print()


def analysis(input_str):
    try:
        exec(input_str)
    except NameError as e:
        id_str = e.__str__().split('\'')[1]
        print_n(IdNotFoundException(id_str))
    except SyntaxError as e:
        print_n(SyntaxException(e.__str__()))
    except TypeError:
        print_n(MissingArgumentException())


def introduction():
    print('c: ' + c().__str__())
    print('matrix: ' + matrix().__str__())
    print('class_r: ' + class_r.__str__())
    print('print_r: ' + print_r.__str__())
    print('length: ' + length.__str__())
    print('rainbow: ' + rainbow.__str__())
    print('dev: ' + dev.off.__str__())
    print('png: ' + png.__str__())
    print('plot: ' + plot.__str__())
    print('hist: ' + hist.__str__())
    print('pie: ' + pie.__str__())
    print('barplot: ' + barplot.__str__())

class word:
    type = "null"
    value = "none"
    def __init__(self,type,value):
        self.type = type
        self.value = value
class variable:
    name = "null"
    type = "null"
    value = "null"
    def __init__(self,name,type,value):
        self.name = name
        self.type = type
        self.value = value
def getArguments(words,index):
    arguments = []
    # continuing = True
    while(index < len(words)):
        # continuing = False
        if(words[index].type == "ide"):
            if(words[index+1].type == "ass" and words[index+1].value == "="):
                if(words[index+2].type == "int"):
                    vartemp = variable("", "float", float(words[index+2].value))
                    arguments.append(vartemp)
                    index = index+2
                elif (words[index+2].type == "float"):
                    vartemp = variable("", "float", float(words[index+2].value))
                    arguments.append(vartemp)
                    index = index+2
            elif(words[index].type == "del" and (words[index].value == "," or words[index].value == ")")):
                vartemp = variables[words[index].value]
                vartemp.name = ""
                arguments.append(vartemp)
        elif(words[index].type == "int"):
            vartemp = variable("", "int", int(words[index].value))
            arguments.append(vartemp)
        elif(words[index].type == "float"):
            vartemp = variable("", "float", float(words[index].value))
            arguments.append(vartemp)
        elif(words[index].type == "func" and words[index].value == "c"):
            arguments, index = getArguments(words, index+1)
            arguments.append(c(variableToTuple(arguments)))
        # elif(words[index].type == "del" and words[index].value == ","):
            # continuing = True
        elif(words[index].type == "del" and words[index].value == ")"):
            break
        index = index + 1
    return arguments,index

def variableToTuple(varList):
    l = []
    for item in varList:
        l.append(item.value)
    return l

def foundArg(arguments, name, type):
    for arg in arguments:
        if (arg.type == type and arg.name == name):
            return arg
    return False

variables = {}
words = [word("func", "print"), word("del", "("), word("int", "5"), word("del", ","), word("ide", "num"), word("ass", "="), word("int", "6"), word("del", ")"), word("del", ";"), word("del", ";")]
def analize(words):
    if(len(words) > 0):
        if(words[0].type == "ide"):
            if(words[1].type == "ass"):
                if(words[1].value == "<-" or "="):
                    if(words[2].type == "int"):
                        variables[words[0].value] = variable(words[0].value,words[2].type,int(words[2].value))
                    elif(words[2].type == "float"):
                        variables[words[0].value] = variable(words[0].value,words[2].type,float(words[2].value))
                    elif(words[2].type == "func"):
                        if(words[2].value == "c"):
                            arguments,tempIndex = getArguments(words,3)
                            vec = c(variableToTuple(arguments))
                            variables[words[0].value] = variable(words[0].value, "vec", vec)
                        elif(words[2].value == "matrix"):
                            arguments,tempIndex = getArguments(words,3)
                            hasArg = []
                            vec, hasArg[0] = foundArg(arguments,"","vec")
                            nr, hasArg[1] = foundArg(arguments,"nrow","int")
                            nc, hasArg[2] = foundArg(arguments,"ncol","int")
                            br, hasArg[3] = foundArg(arguments,"byrow","logical")
                            for has in hasArg:
                                if(~has):
                                    return
                            mat = matrix(vec, nrow=nr, ncol=nc, byrow=br)
                            variables[words[0].value] = variable(words[0].value, "matrix", mat)
        elif(words[0].type == "func"):
            if(words[0].value == "print"):
                arguments,tempIndex = getArguments(words,1)
                # for item in arguments:
                #     print(item.name, item.type, item.value)
                # print(tempIndex)
                if(len(arguments) == 1):
                    print_n(arguments[0])
            elif(words[0].value == "png"):
                arguments, tempIndex = getArguments(words, 1)
                hasArg = []
                file, hasArg[0] = foundArg(arguments, "file", "string")
                for has in hasArg:
                    if (~has):
                        return
                png(file)
            elif(words[0].value == "pie"):
                arguments, tempIndex = getArguments(words, 1)
                hasArg = []
                x, hasArg[0] = foundArg(arguments, "", "vec")
                labels, hasArg[1] = foundArg(arguments, "", "vec")
                col, hasArg[2] = foundArg(arguments, "col", "string")
                main, hasArg[3] = foundArg(arguments, "main", "string")
                for has in hasArg:
                    if (~has):
                        return
                barplot(x, labels, main=main, col=col)
            elif(words[0].value == "hist"):
                arguments, tempIndex = getArguments(words, 1)
                hasArg = []
                v, hasArg[0] = foundArg(arguments, "", "vec")
                xlab, hasArg[1] = foundArg(arguments, "xlab", "string")
                col, hasArg[2] = foundArg(arguments, "col", "string")
                border, hasArg[3] = foundArg(arguments, "border", "string")
                xlim, hasArg[4] = foundArg(arguments, "xlim", "vec")
                ylim, hasArg[5] = foundArg(arguments, "ylim", "vec")
                breaks, hasArg[6] = foundArg(arguments, "breaks", "int")
                for has in hasArg:
                    if (~has):
                        return
                hist(v, xlab=xlab, col=col, border=border, xlim=xlim, ylim=ylim, breaks=breaks)
                # hist(v, xlab="Weight", col="green", border="red", xlim=c(0, 40), ylim=c(0, 5), breaks=5)
            elif(words[0].value == "barplot"):
                arguments, tempIndex = getArguments(words, 1)
                hasArg = []
                vec, hasArg[0] = foundArg(arguments, "", "vec")
                names_arg, hasArg[1] = foundArg(arguments, "names.arg", "vec")
                xlab, hasArg[2] = foundArg(arguments, "xlab", "string")
                ylab, hasArg[3] = foundArg(arguments, "ylab", "string")
                col, hasArg[4] = foundArg(arguments, "col", "string")
                main, hasArg[5] = foundArg(arguments, "main", "string")
                border, hasArg[6] = foundArg(arguments, "border", "string")
                for has in hasArg:
                    if (~has):
                        return
                barplot(vec, arg=names_arg, xlab=xlab, ylab=ylab, col=col, main=main, border=border)
            elif(words[0].value == "plot"):
                arguments, tempIndex = getArguments(words, 1)
                hasArg = []
                vec, hasArg[0] = foundArg(arguments, "", "vec")
                type, hasArg[1] = foundArg(arguments, "type", "string")
                for has in hasArg:
                    if (~has):
                        return
                plot(vec, type)
            elif(words[0].value == "dev.off"):
                dev.off()

analize(words)
# print(variables["var1"].type)