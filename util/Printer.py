from container.Vector import c
from container.Matrix import matrix

current_str = ''


def print_r(obj):
    global current_str
    if isinstance(obj, c) or isinstance(obj, matrix):
        current_str = current_str + obj.__str__() + '\n'
    else:
        current_str = current_str + c(obj).__str__() + '\n'
