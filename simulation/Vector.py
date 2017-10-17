class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, arg):
        if arg == 0: return self.x
        elif arg == 1: return self.y
        else: raise KeyError()

    def __setitem__(self, key, value):
        if key == 0: self.x = value
        elif key == 1: self.y = value
        else: raise KeyError()

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __neg__(self):
        self.x = -self.x
        self.y = -self.y
        return self

    def __mul__(self, other):
        self.x *= other
        self.y *= other
        return self

    __rmul__ = __mul__

    def __truediv__(self, other):
        self.x = self.x / other
        self.y = self.y / other
        return self

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
