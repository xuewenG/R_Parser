from container.Vector import c
from container.Matrix import matrix
from atom.Class import class_r
from util.Length import length
from util.Rainbow import rainbow
from util.Printer import print_r as print
import chart.dev as dev
from chart.Config import png
from chart.Plot import plot
from chart.Hist import hist
from chart.Pie import pie
from chart.Bar import barplot


process_line = exec


def analysis(input_str):
    process_line(input_str)
