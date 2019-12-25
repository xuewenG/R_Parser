# import pandas as pd
# import xlrd
#
# class read:
#
#     def csv(name):
#         df = pd.read_csv(name)
#         return df
#
#     # def __str__(self):
#     #     out = self.data
#     #     # print(file)
#
#     def xlsx(*tup):
#         name = tup[0]
#         number = tup[1]
#         book = xlrd.open_workbook(name)
#         sheet1 = book.sheets()[number]
#         return str(read.get(sheet1))
#
#     def get(file):
#         out = ''
#         row_num = file.nrows
#         col_num = file.ncols
#         out += "".rjust(2)
#         # print("".rjust(2), end='')
#         for j in range(col_num):
#             out += str(str(file.cell_value(0, j)) + ",").rjust(6)
#             # print(str(str(file.cell_value(0, j)) + ",").rjust(6), end='')
#         out += '\n'
#         # print('')
#
#         for i in range(1, row_num):
#             out += str(i)
#             # print(i, end='')
#             for j in range(col_num):
#                 if isinstance(file.cell_value(i, j), float):
#                     out += str(int(file.cell_value(i, j))).rjust(6)
#                     # print(str(int(file.cell_value(i, j))).rjust(6), end='')
#                 else:
#                     out += str(file.cell_value(i, j)).rjust(6)
#                     # print(str(file.cell_value(i, j)).rjust(6), end='')
#             out += '\n'
#             # print('')
#         return out
#
#
# class write:
#
#     def csv(*tup):
#         name = tup[1]
#         text = tup[0]
#         text.to_csv(name, index=False)
