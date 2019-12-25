import util.Printer as Printer
from tkinter import Tk, Button, Label, END, WORD, Text
from tkinter.scrolledtext import ScrolledText
from interpreter.Process import process_all


class UserInterface:
    def __init__(self):
        self.main_window = Tk(className="R编译器")

        # 开始解释执行按钮
        self.button = Button(self.main_window, text="run", bg="#76b3e4",
                             font=50, width=16, height=5, command=self.compile)
        self.button.alpha = 0.5
        self.button.pack()
        # 提示信息
        self.code_input_label = Label(self.main_window, text="代码输入框")
        self.code_input_label.pack()
        # 代码输入框
        self.code_input = ScrolledText(self.main_window, height=15, wrap=WORD)
        self.code_input.pack()
        # 提示信息
        result_output_label = Label(self.main_window, text="文本结果输出框")
        result_output_label.pack()
        # 结果输出框
        self.result_output = Text(self.main_window, height=30, width=80)
        self.result_output.pack()
        # 进入消息循环体
        self.main_window.mainloop()

    def compile(self):
        Printer.current_str = ''
        code_list = self.code_input.get(0.0, END)
        process_all(code_list)
        self.result_output.insert(END, Printer.current_str)
