def uno(_):
    return 1


def inc(n):
    return n+1


def inc_by(a):
    def inc(b):
        return a+b
    return inc


class INC_BY:

    def __init__(self, a):
        self.a = a

    def __call__(self, a):
        return a + self.a


@INC_BY(100)
@inc_by(10)
@inc
@uno
def hola():
    return 'hello'


# hola = uno(hola)
# hola = inc(uno(hola))


class Foo:
    @staticmethod
    def meth(*args):
        return args
