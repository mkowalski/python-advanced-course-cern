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
        yield self.a
        yield self.b
        yield self.c
