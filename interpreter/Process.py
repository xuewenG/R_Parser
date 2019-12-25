from interpreter.Lex import pre_process
from interpreter.Grammer import analysis


def process_all(input_str):
    input_str = pre_process(input_str)
    analysis(input_str)
