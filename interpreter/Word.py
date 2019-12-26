class Word:
    def __init__(self, type, value):
        self.value = value
        self.type = type

    def __repr__(self):
        return self.type + "--" + self.value
