class SyntaxException:
    def __init__(self, msg):
        self.msg = 'Error: %s' % msg

    def __str__(self):
        return self.msg
