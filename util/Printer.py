from container.Matrix import matrix
from container.Vector import c

current_str = ''


def print_r(obj):
    global current_str
    if isinstance(obj, c) or isinstance(obj, matrix):
        current_str = current_str + obj.__str__() + '\n'
    else:
        current_str = current_str + c(obj).__str__() + '\n'


def print_n(obj):
    global current_str
    current_str = current_str + obj.__str__() + '\n'
