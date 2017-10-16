def return_result(fun):
    def proxy(*args):
        result = fun(*args)
        print(result)
        return result
    return proxy


def report_args(fun):
    def proxy(*args):
        print(args)
        return fun(*args)
    return proxy


@return_result
@report_args
def badd(a, b):
    """Fucked up addition"""
    return a * b


print(badd(2, 3))
