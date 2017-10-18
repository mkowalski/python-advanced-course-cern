from itertools import count


class cenumerate:
    def __init__(self, iterable, start=0):
        self.data = iterable
        self._it = iter(iterable)
        self._count = -1 + start

    def __iter__(self):
        return self

    def __next__(self):
        self._count += 1
        return self._count, next(self._it)


def genumerate(iterable, start=0):
    count = start
    for i in iterable:
        yield count, i
        count += 1


def ienumerate(iterable, start=0):
    return zip(count(start), iterable)
