def add(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c


def sub(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] - b[i])
    return c


def mul(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])
    return c


def div(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] / b[i])
    return c


def and_(a, b):
    c = []
    for i in range(len(a)):
        c.append(bool(a[i] and b[i]))
    return c


def or_(a, b):
    c = []
    for i in range(len(a)):
        c.append(bool(a[i] or b[i]))
    return c


def not_(a):
    c = []
    for i in range(len(a)):
        c.append(bool(not a[i]))
    return c


def equal(a, b):
    c = []
    for i in range(len(a)):
        c.append(bool(a[i] == b[i]))
    return c


def smaller(a, b):
    c = []
    for i in range(len(a)):
        c.append(bool(a[i] < b[i]))
    return c


def bigger(a, b):
    c = []
    for i in range(len(a)):
        c.append(bool(a[i] > b[i]))
    return c
