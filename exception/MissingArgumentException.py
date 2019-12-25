class MissingArgumentException(object):
    def __init__(self):
        self.msg = 'Error: Invalid argument'

    def __str__(self):
        return self.msg
