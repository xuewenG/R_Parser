class IdNotFoundException(object):
    def __init__(self, id_str):
        self.msg = 'Error: object \'%s\' not found' % id_str

    def __str__(self):
        return self.msg
