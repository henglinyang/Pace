from collections import namedtuple

class Const(object):
    class ConstError(Exception):
        pass

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

if __name__ == '__main__':
    c = Const(3)
    #c.value = 0


                                
