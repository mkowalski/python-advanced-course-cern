class triplet:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __getitem__(self, item):
        if item == 0: return self.a
        if item == 1: return self.b
        if item == 2: return self.c
        raise IndexError

    def __len__(self):
        return 3

    def __iter__(self):
        return self.triplet_iter(self)

    class triplet_iter:
        def __init__(self, iterable):
            self._iterable = iterable
            self._count = -1

        def __iter__(self):
            return self

        def __next__(self):
            self._count += 1
            try:
                return self._iterable.__getitem__(self._count)
            except IndexError:
                raise StopIteration
