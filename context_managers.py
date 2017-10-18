import _pytest


class MyRaises:

    def __init__(self, exc_exp):
        self.exc_exp = exc_exp
        self.exc_ret = object.__new__(_pytest._code.ExceptionInfo)

    def __enter__(self):
        return self.exc_ret

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exc_ret.__init__((exc_type, exc_type(exc_val), exc_tb))

        if exc_type == self.exc_exp or exc_type in self.exc_exp:
            assert True
        else:
            assert False
        return True
