from interpreter.Grammer import analysis
from interpreter.Lex import pre_process


def process_all(input_str):
    input_str = pre_process(input_str)
    analysis(input_str)
