class assert_evolution:

    def __init__(self, fun, operator):
        self.fun = fun
        self.operator = operator
        self.prev = None
        self.current = None

    def __call__(self):
        self.current = self.fun()
        if self.prev and not self.operator(self.current, self.prev):
            raise AssertionError
        self.current, self.prev = self.prev, self.current


def assert_evolution(fun, operator):
    fun = fun
    operator = operator
    c = [None, None]

    def closure():
        c[1] = fun()
        if c[0] and not operator(c[1], c[0]):
            raise AssertionError
        c[0], c[1] = c[1], c[0]
    return closure


def assert_evolution(fun, operator):

    def gen_assert_evolution(fun, operator):
        yield

        fun = fun
        operator = operator
        c = [None, None]

        while True:
            c[1] = fun()
            if c[0] and not operator(c[1], c[0]):
                raise AssertionError
            c[0], c[1] = c[1], c[0]
            yield

    c = gen_assert_evolution(fun, operator)
    next(c)
    return c.__next__
