class Logical:
    data = False
    type_name = "logical"

    def __init__(self, data):
        self.data = data

    def get_class(self):
        return self.type_name
