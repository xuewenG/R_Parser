from util import List

TYPE_STR = 1
TYPE_NUM = 0

CAL_NOT = 0
CAL_YET = 1


class c:
    type_name = 'vector'

    def __init__(self, *param):
        self.cal = CAL_NOT
        self.type = TYPE_NUM
        self.data = self.get_tuple(param)
        for item in range(len(self.data)):
            if isinstance(self.data[item], str):
                self.type = TYPE_STR
                break

    def get_tuple(self, param):
        if len(param) > 0:
            if isinstance(param[0], tuple) or isinstance(param[0], list):
                param = param[0]
        return param

    def __str__(self):
        out = ''
        if self.cal == 0:
            out += '[1] '
        for i in range(len(self.data)):
            if self.type == TYPE_STR:
                out += '"%s" ' % str(self.data[i])
            else:
                out += str(self.data[i]) + " "
        return out

    def __add__(self, other):
        old = list(self.data)
        new = list(other.data)
        new = List.add(new, old)
        new = c(tuple(new))
        new.cal = 1
        return new

    def __sub__(self, other):
        old = list(self.data)
        new = list(other.data)
        new = List.sub(old, new)
        new = c(tuple(new))
        new.cal = 1
        return new

    def __mul__(self, other):
        old = list(self.data)
        new = list(other.data)
        new = List.mul(old, new)
        new = c(tuple(new))
        new.cal = 1
        return new

    def __truediv__(self, other):
        old = list(self.data)
        new = list(other.data)
        new = List.div(old, new)
        new = c(tuple(new))
        new.cal = 1
        return new

    def __and__(self, other):
        old = list(self.data)
        new = list(other.data)
        new = List.and_(old, new)
        new = c(tuple(new))
        new.cal = 1
        return new

    def __or__(self, other):
        old = list(self.data)
        new = list(other.data)
        new = List.or_(old, new)
        new = c(tuple(new))
        new.cal = 1
        return new

    def __invert__(self):
        new = List.not_(list(self.data))
        type_ = self.type
        new = c(tuple(new))
        new.cal = 1
        new.type = type_
        return new

    def __ge__(self, other):
        old = list(self.data)
        new = list(other.data)
        type_ = self.type or other.type
        new = List.bigger(old, new)
        new = c(tuple(new))
        new.type = type_
        new.cal = 1
        return new

    def __eq__(self, other):
        old = list(self.data)
        new = list(other.data)
        type_ = self.type or other.type
        new = List.equal(old, new)
        new = c(tuple(new))
        new.cal = 1
        new.type = type_
        return new

    def __lt__(self, other):
        old = list(self.data)
        new = list(other.data)
        new = List.smaller(old, new)
        type_ = self.type or other.type
        new = c(tuple(new))
        new.cal = 1
        new.type = type_
        return new

    def get_number(self):
        return float(len(self.data))

    def get_data(self):
        return self.data
