from container.Vector import c
import math
from util import List


class matrix:
    type_name = 'matrix'

    def __init__(self, vec, nrow=0, ncol=0, byrow=False):
        self.data = vec
        self.row = int(nrow)
        self.col = int(ncol)
        self.by_row = bool(byrow)
        if self.row == 0:
            if self.col == 0:
                self.col = 1
            self.row = int(math.ceil(self.data.get_number() / self.col))
        elif self.col == 0:
            self.col = int(math.ceil(self.data.get_number() / self.row))

    def get_data(self):
        return self.data.get_data()

    def __add__(self, other):
        old = self.get_data()
        new = other.get_data()
        new = List.add(new, old)
        new = c(tuple(new))
        out = matrix(new, self.row, self.col, self.by_row)
        return out

    def __sub__(self, other):
        old = self.get_data()
        new = other.get_data()
        new = List.sub(old, new)
        new = c(tuple(new))
        out = matrix(new, self.row, self.col, self.by_row)
        return out

    def __mul__(self, other):
        old = self.get_data()
        new = other.get_data()
        new = List.mul(old, new)
        new = c(tuple(new))
        out = matrix(new, self.row, self.col, self.by_row)
        return out

    def __truediv__(self, other):
        old = self.get_data()
        new = other.get_data()
        new = List.div(old, new)
        new = c(tuple(new))
        out = matrix(new, self.row, self.col, self.by_row)
        return out

    def __str__(self):
        out = ''
        out += '    '
        for i in range(self.col):
            out += ("[,%-d]" % (i+1)).rjust(5)
        out += '\n'
        row = self.row
        col = self.col
        for i in range(row):
            out += "[%-d,]" % (i+1)
            for j in range(col):
                temp = i * col + j
                if not self.by_row:
                    temp = j * row + i
                if temp < self.data.get_number():
                    out += str(self.data.get_data()[temp]).rjust(5)
            out += '\n'
        return out
