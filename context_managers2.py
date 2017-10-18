import contextlib
import _pytest

@contextlib.contextmanager
def MyRaises2(exc_exp):
    exc_ret = object.__new__(_pytest._code.ExceptionInfo)
    _exc = None

    try:
        yield exc_ret
    except exc_exp as exc:
        _exc = exc
        assert True
    except Exception as exc:
        _exc = exc
        assert False
    finally:
        exc_ret.__init__((type(_exc), type(_exc)(_exc), _exc.__traceback__))

