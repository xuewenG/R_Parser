class Integer:
    data = 0
    type_name = "integer"

    def __init__(self, data):
        self.data = data

    def get_class(self):
        return self.type_name
