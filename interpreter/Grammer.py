from container.Vector import c
from container.Matrix import matrix
from atom.Class import class_r
from util.Length import length
from util.Rainbow import rainbow
from util.Printer import print_r
from util.Printer import print_n
from chart.Config import png
from chart.Plot import plot
from chart.Hist import hist
from chart.Pie import pie
from chart.Bar import barplot
import chart.dev as dev
from exception.SyntaxException import SyntaxException
from exception.IdNotFoundException import IdNotFoundException
from exception.MissingArgumentException import MissingArgumentException


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
