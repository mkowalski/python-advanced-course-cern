from operator import add, sub, mul, truediv, neg


def Vector(spec):

    def __init__(self, *args):
        if len(args) != len(self.dimensions) and len(args) != 0: raise TypeError
        for id, char in enumerate(self.dimensions):
            try:
                setattr(self, char, args[id])
            except IndexError:
                setattr(self, char, 0)

    def __getitem__(self, arg):
        return getattr(self, self.dimensions[arg])

    def __setitem__(self, arg, val):
        setattr(self, self.dimensions[arg], val)

    def _arithmetic_generator(operation):
        def fun(self, other):
            new = type(self)()
            if type(self) == type(other): arg = (lambda x: getattr(other, x))
            else: arg = (lambda x: other)
            [ setattr(new, elem, operation(getattr(self, elem), arg(elem))) for elem in self.dimensions ]
            return new
        return fun

    def __neg__(self):
        new = type(self)()
        for elem in self.dimensions:
            setattr(new, elem, neg(getattr(self, elem)))
        return new

    def __abs__(self):
        res = 0
        for elem in self.dimensions:
            res += getattr(self, elem) ** 2
        return res ** 0.5

    def __repr__(self):
        repr = list('Vector("')
        [ repr.append(elem) for elem in self.dimensions ]
        repr.append('")(')
        [ repr.append(str(getattr(self, elem)) + ',') for elem in self.dimensions ]
        repr.append(')')
        return "".join(repr)

    def __eq__(self, other):
        for elem in self.dimensions:
            if getattr(self, elem) != getattr(other, elem): return False
        return True

    return type('Vector('+spec+')', (), {
        'dimensions': spec,
        '__init__': __init__,
        '__getitem__': __getitem__,
        '__setitem__': __setitem__,
        '__add__': _arithmetic_generator(add),
        '__sub__': _arithmetic_generator(sub),
        '__mul__': _arithmetic_generator(mul),
        '__rmul__': _arithmetic_generator(mul),
        '__truediv__': _arithmetic_generator(truediv),
        '__neg__': __neg__,
        '__abs__': __abs__,
        '__repr__': __repr__,
        '__eq__': __eq__,
    })


Vector2D = Vector('xy')
Vector3D = Vector('xyz')
