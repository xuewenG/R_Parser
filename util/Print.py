from container.Vector import c
from container.Matrix import matrix

result_str = ''


def print_r(obj):
    global result_str
    if isinstance(obj, c) or isinstance(obj, matrix):
        result_str = result_str + obj.__str__() + '\n'
    else:
        result_str = result_str + c(obj).__str__() + '\n'
