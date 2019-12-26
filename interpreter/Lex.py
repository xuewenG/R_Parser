from interpreter.Tables import algorithm_operator_list
from interpreter.Tables import c_map
from interpreter.Tables import keyword_table
from interpreter.Tables import logical_operator_list
from interpreter.Tables import separator_list
from interpreter.Word import Word
from interpreter.type.AlgorithmicOperator import AlgorithmicOperator
from interpreter.type.Keyword import Keyword
from interpreter.type.LogicalOperator import LogicalOperator
from interpreter.type.Separator import Separator


def lex(line):
    for separator in separator_list:
        line = line.replace(separator, ' %s ' % separator)
    while '  ' in line:
        line = line.replace('  ', ' ')
    line = line.strip()
    words = [Word('func', '')]
    for item in line.split(' '):
        words.append(Word(Keyword.type_name, item))
    return words


def check_type(item):
    word = Word(type='', value=item)
    if item in separator_list:
        word.type_name = Separator.type_name
    elif item in logical_operator_list:
        word.type_name = LogicalOperator.type_name
    elif item in algorithm_operator_list:
        word.type_name = AlgorithmicOperator.type_name
    else:
        word.type_name = Keyword.type_name
        if word.value not in keyword_table.keys():
            keyword_table[word.value] = None
    return word


def pre_process(content):
    for line in content.splitlines():
        items = lex(line)
        for item in items:
            word = check_type(item)
    for item in c_map:
        content = content.replace(item[0], item[1])
    return content
