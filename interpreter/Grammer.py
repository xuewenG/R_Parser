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
from interpreter.Lex import lex, check_type
from interpreter.Tables import keyword_table
from interpreter.Word import Word
from util.Length import length
from util.Printer import print_n
from util.Printer import print_r
from util.Rainbow import rainbow

input_all = ''


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


class Variable:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value


def get_arguments(words, index):
    arguments = []
    while index < len(words):
        if words[index].type == "ide":
            if words[index + 1].type == "ass" and words[index + 1].value == "=":
                if words[index + 2].type == "int":
                    vartemp = Variable("", "float", float(words[index + 2].value))
                    arguments.append(vartemp)
                    index = index + 2
                elif words[index + 2].type == "float":
                    vartemp = Variable("", "float", float(words[index + 2].value))
                    arguments.append(vartemp)
                    index = index + 2
            elif words[index].type == "del" and (words[index].value == "," or words[index].value == ")"):
                vartemp = variables[words[index].value]
                vartemp.name = ""
                arguments.append(vartemp)
        elif words[index].type == "int":
            vartemp = Variable("", "int", int(words[index].value))
            arguments.append(vartemp)
        elif words[index].type == "float":
            vartemp = Variable("", "float", float(words[index].value))
            arguments.append(vartemp)
        elif words[index].type == "func" and words[index].value == "c":
            arguments, index = get_arguments(words, index + 1)
            arguments.append(c(variable_to_tuple(arguments)))
        # elif(words[index].type == "del" and words[index].value == ","):
        # continuing = True
        elif words[index].type == "del" and words[index].value == ")":
            break
        index = index + 1
    return arguments, index


def variable_to_tuple(var_list):
    l = []
    for item in var_list:
        l.append(item.value)
    return l


def found_arg(arguments, name, type):
    for arg in arguments:
        if arg.type == type and arg.name == name:
            return arg
    return False


def analysis(input_str):
    global input_all
    input_all = input_str
    input_list = input_str.splitlines()
    try:
        for line in input_list:
            words = lex(line)
            analyze_line(words)
            input_all = ''
    except NameError as e:
        id_str = e.__str__().split('\'')[1]
        print_n(IdNotFoundException(id_str))
    except SyntaxError as e:
        print_n(SyntaxException(e.__str__()))
    except TypeError:
        print_n(MissingArgumentException())


variables = {}
words = [Word("func", "print"),
         Word("del", "("),
         Word("int", "5"),
         Word("del", ","),
         Word("ide", "num"),
         Word("ass", "="),
         Word("int", "6"),
         Word("del", ")"),
         Word("del", ";"),
         Word("del", ";")]


def analyze_line(words):
    if words[0].type == "ide":
        if words[1].type == "ass":
            if words[1].value == "<-" or "=":
                if words[2].type == "int":
                    variables[words[0].value] = Variable(words[0].value, words[2].type, int(words[2].value))
                elif words[2].type == "float":
                    variables[words[0].value] = Variable(words[0].value, words[2].type, float(words[2].value))
                elif words[2].type == "func":
                    if words[2].value == "c":
                        arguments, temp_index = get_arguments(words, 3)
                        vec = c(variable_to_tuple(arguments))
                        variables[words[0].value] = Variable(words[0].value, "vec", vec)
                    elif words[2].value == "matrix":
                        arguments, temp_index = get_arguments(words, 3)
                        has_arg = []
                        vec, has_arg[0] = found_arg(arguments, "", "vec")
                        nr, has_arg[1] = found_arg(arguments, "nrow", "int")
                        nc, has_arg[2] = found_arg(arguments, "ncol", "int")
                        br, has_arg[3] = found_arg(arguments, "byrow", "logical")
                        for has in has_arg:
                            if ~has:
                                return
                        mat = matrix(vec, nrow=nr, ncol=nc, byrow=br)
                        variables[words[0].value] = Variable(words[0].value, "matrix", mat)
    elif words[0].type == "func":
        if words[0].value == "print":
            arguments, temp_index = get_arguments(words, 1)
            # for item in arguments:
            #     print(item.name, item.type, item.value)
            # print(temp_index)
            if len(arguments) == 1:
                print_n(arguments[0])
        elif words[0].value == "png":
            arguments, temp_index = get_arguments(words, 1)
            has_arg = []
            file, has_arg[0] = found_arg(arguments, "file", "string")
            for has in has_arg:
                if ~has:
                    return
            png(file)
        elif words[0].value == "pie":
            arguments, temp_index = get_arguments(words, 1)
            has_arg = []
            x, has_arg[0] = found_arg(arguments, "", "vec")
            labels, has_arg[1] = found_arg(arguments, "", "vec")
            col, has_arg[2] = found_arg(arguments, "col", "string")
            main, has_arg[3] = found_arg(arguments, "main", "string")
            for has in has_arg:
                if ~has:
                    return
            barplot(x, labels, main=main, col=col)
        elif words[0].value == '':
            for item in words:
                check_type(words[0].value)
            exec(input_all)
        elif words[0].value == "hist":
            arguments, temp_index = get_arguments(words, 1)
            has_arg = []
            v, has_arg[0] = found_arg(arguments, "", "vec")
            xlab, has_arg[1] = found_arg(arguments, "xlab", "string")
            col, has_arg[2] = found_arg(arguments, "col", "string")
            border, has_arg[3] = found_arg(arguments, "border", "string")
            xlim, has_arg[4] = found_arg(arguments, "xlim", "vec")
            ylim, has_arg[5] = found_arg(arguments, "ylim", "vec")
            breaks, has_arg[6] = found_arg(arguments, "breaks", "int")
            for has in has_arg:
                if ~has:
                    return
            hist(v, xlab=xlab, col=col, border=border, xlim=xlim, ylim=ylim, breaks=breaks)
            # hist(v, xlab="Weight", col="green", border="red", xlim=c(0, 40), ylim=c(0, 5), breaks=5)
        elif words[0].value == "barplot":
            arguments, temp_index = get_arguments(words, 1)
            has_arg = []
            vec, has_arg[0] = found_arg(arguments, "", "vec")
            names_arg, has_arg[1] = found_arg(arguments, "names.arg", "vec")
            xlab, has_arg[2] = found_arg(arguments, "xlab", "string")
            ylab, has_arg[3] = found_arg(arguments, "ylab", "string")
            col, has_arg[4] = found_arg(arguments, "col", "string")
            main, has_arg[5] = found_arg(arguments, "main", "string")
            border, has_arg[6] = found_arg(arguments, "border", "string")
            for has in has_arg:
                if ~has:
                    return
            barplot(vec, arg=names_arg, xlab=xlab, ylab=ylab, col=col, main=main, border=border)
        elif words[0].value == "plot":
            arguments, temp_index = get_arguments(words, 1)
            has_arg = []
            vec, has_arg[0] = found_arg(arguments, "", "vec")
            type, has_arg[1] = found_arg(arguments, "type", "string")
            for has in has_arg:
                if ~has:
                    return
            plot(vec, type)
        elif words[0].value == "dev.off":
            dev.off()
