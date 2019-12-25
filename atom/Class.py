from atom.Character import Character
from atom.Complex import Complex
from atom.Integer import Integer
from atom.Logical import Logical
from atom.Numeric import Numeric
from atom.Raw import Raw
from container.Matrix import matrix
from container.Vector import c


def class_r(obj):
    if isinstance(obj, matrix):
        return matrix.type_name
    if not isinstance(obj, c):
        obj = c(obj)
    data = obj.data
    if is_float(data) or is_digit(data):
        return Numeric.type_name
    if is_integer(data):
        return Integer.statement
    if Logical(data):
        return Logical.type_name
    if is_complex(data):
        return Complex.type_name
    if is_raw(data):
        return Raw.type_name
    return Character.type_name


def is_float(data):
    for item in data:
        if not isinstance(item, float):
            return False
    return True


def is_digit(data):
    for item in data:
        if not isinstance(item, int):
            return False
    return True


def is_integer(data):
    return isinstance(data, Integer)


def is_logical(data):
    return isinstance(data, Logical)


def is_complex(data):
    return isinstance(data, Complex)


def is_raw(data):
    return isinstance(data, Raw)
