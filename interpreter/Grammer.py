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
