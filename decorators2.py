from functools import wraps


def inc_result_by(n):
    def decorator(fun):
        @wraps(fun)
        def proxy(*args):
            return fun(*args) + n
        return proxy
    return decorator


def WRAPS(org_fun):
    def nested_proxy(decorated_fun):
        decorated_fun.__name__ = org_fun.__name__
        decorated_fun.__doc__ = org_fun.__doc__
        decorated_fun.__module__ = org_fun.__module__
        return decorated_fun
    return nested_proxy


def return_result(fun):
    @wraps(fun)
    def proxy(*args):
        result = fun(*args)
        print(result)
        return result
    return proxy


def report_args(fun):
    @WRAPS(fun)
    def proxy(*args):
        print(args)
        return fun(*args)
    return proxy


@inc_result_by(10)
# @return_result
# @report_args
def badd(a, b):
    """Fucked up addition"""
    return a * b


print(badd(2, 3))
