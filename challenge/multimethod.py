class MultiMethod:

    registry = {}

    def __init__(self, fun):
        self.fun = fun
        self.types = {}

    def register(self, fun):
        types = fun.__annotations__
        self.types[tuple(types.values())] = fun

    def __call__(self, *args, **kwargs):
        typing = tuple(i.__class__ for i in args)
        print("typowanie")
        print(typing)
        try:
            return self.types[typing](*args)
        except KeyError:
            for id, val in reversed(list(enumerate(args))):
                for parent in val.__class__.__bases__:
                    print("test bazowej " + str(parent))
                    type = list(typing)
                    type[id] = parent
                    try:
                        print("proba")
                        print(tuple(type))
                        return self.types[tuple(type)](*args)
                    except KeyError:
                        continue

            raise TypeError("Method does not exist for parameters provided")


def multimethod(fun):
    name = fun.__name__
    register = MultiMethod.registry

    def decorator(*args):
        return register[name](*args)

    entry = register.get(name)
    if not entry:
        entry = register[name] = MultiMethod(fun)
    entry.register(fun)

    return decorator
