separator_list = ['(', ')', ',', '"']
logical_operator = ['!', '&', '|']
algorithm_operator = ['+', '-', '*', '/']
identifier = {}
c_map = [['<-', '='],
         ['{', ':'],
         ['} ', ''],
         ['}', ''],
         ['&&', ' and '],
         ['class(', 'class_r('],
         ['print(', 'print_r('],
         ['names.arg', 'arg']]


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


def pre_process(content):
    for item in c_map:
        content = content.replace(item[0], item[1])
    return content
