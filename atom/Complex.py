class Complex:
    a = 0
    b = 0
    type_name = "complex"

    def __init__(self, data):
        self.data = data

    def get_class(self):
        return self.type_name
