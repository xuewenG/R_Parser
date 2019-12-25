from tkinter import Tk, Button, Label, END, WORD
from tkinter.scrolledtext import ScrolledText

import util.Printer as Printer
from interpreter.Process import process_all


class UserInterface:
    def __init__(self):
        self.main_window = Tk(className="r_parser")
        # 设置主窗口标题
        self.main_window.title("R语言解释器")
        # 设置主窗口大小和居中
        ws = self.main_window.winfo_screenwidth()
        hs = self.main_window.winfo_screenheight()
        w = 500
        h = 800
        # 计算 x, y 位置
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.main_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # 提示信息
        self.code_input_label = Label(self.main_window, text="代码输入框")
        self.code_input_label.pack()
        # 代码输入框
        self.code_input = ScrolledText(self.main_window, height=35, wrap=WORD)
        self.code_input.pack()
        # 提示信息
        result_output_label = Label(self.main_window, text="运行结果")
        result_output_label.pack()
        # 结果输出框
        self.result_output = ScrolledText(self.main_window, height=18, width=80)
        self.result_output.pack()
        # 开始解释执行按钮
        self.button = Button(self.main_window, text="run", bg='#CCCCCC',
                             font=50, width=9, height=2, command=self.compile)
        self.button.alpha = 0.5
        self.button.pack()
        # 进入消息循环体
        self.main_window.mainloop()

    def compile(self):
        Printer.current_str = ''
        code_list = self.code_input.get(0.0, END)
        process_all(code_list)
        self.result_output.insert(END, Printer.current_str)
