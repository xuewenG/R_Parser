class Character:
    data = ""
    type_name = "character"

    def __init__(self, data):
        self.data = data

    def get_class(self):
        return self.type_name
