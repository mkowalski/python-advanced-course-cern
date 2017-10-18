from contextlib import contextmanager
from time import time


class DummyClass:
    def __init__(self, t):
        self.time = t


@contextmanager
def timer():
    result = object.__new__(DummyClass)
    start = time()
    yield result
    result.__init__(time() - start)
