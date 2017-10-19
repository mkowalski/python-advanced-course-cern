class assert_evolution:

    def __init__(self, new, operator):
        self.operator = operator
        self.prev = None
        self.new = new

    def __call__(self):
        if self.prev and not self.operator(self.new(), self.prev):
            raise AssertionError
        self.prev = self.new()


def assert_evolution(new, operator):
    prev = None

    def closure():
        nonlocal prev
        if prev and not operator(new(), prev):
            raise AssertionError
        prev = new()
    return closure


def assert_evolution(new, operator):
    def gen_assert_evolution():
        prev = None
        while True:
            if prev and not operator(new(), prev):
                raise AssertionError
            prev = new()
            yield
    return gen_assert_evolution().__next__
