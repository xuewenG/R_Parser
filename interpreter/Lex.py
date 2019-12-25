from container.Vector import c
from container.Matrix import matrix
from atom.Class import class_r


separator_list = ['(', ')', ',', '"']
logical_operator = ['!', '&', '|']
algorithm_operator = ['+', '-', '*', '/']
identifier = {
    'abc': c(1, 2, 3),
    'xyz': matrix(c(3, 9, -1, 4, 2, 6), nrow=2, ncol=3),
    'cl': class_r('qw')
}


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
        identifier[params[0]].print()


def lex(line):
    for separator in separator_list:
        line = line.replace(separator, ' %s ' % separator)
    while '  ' in line:
        line = line.replace('  ', ' ')
    line = line.strip()
    return line.split(' ')
