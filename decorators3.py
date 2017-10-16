class COUNT_CALLS:

    def __init__(self, fn):
        self._fn = fn
        self._count = 0

    def __call__(self, *args, **kwargs):
        self._count += 1
        print(self._count)
        return self._fn(*args, **kwargs)


def count_calls(fn):
    count = 0

    def proxy(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        return fn(*args, **kwargs)
    return proxy


@count_calls
def badd(a, b):
    return a*b

