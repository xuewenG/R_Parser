from container.Vector import c
from container.Matrix import matrix
from atom.Class import class_r
from util.Length import length
from util.Rainbow import rainbow
from util.Print import print_r as print
import chart.dev as dev
from chart.Config import png
from chart.Plot import plot
from chart.Hist import hist
from chart.Pie import pie
from chart.Bar import barplot


process_line = exec


def process_all(input_str):
    input_str = pre_process(input_str)
    process_line(input_str)


def pre_process(input_str):
    input_str = input_str.replace('<-', '=')
    input_str = input_str.replace('{', ':')
    input_str = input_str.replace('} ', '')
    input_str = input_str.replace('}', '')
    input_str = input_str.replace('&&', ' and ')
    input_str = input_str.replace('class(', 'class_r(')
    input_str = input_str.replace('names.arg', 'arg')
    return input_str
