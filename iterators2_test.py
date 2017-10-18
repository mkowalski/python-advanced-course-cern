from iterators2 import triplet
from hypothesis import given
from hypothesis.strategies import lists, tuples
from hypothesis.strategies import integers as INT
from hypothesis.strategies import integers


@given(tuples(INT(), INT(), INT()))
def test_is_iterable_implicitly(data):
    assert list(triplet(*data)) == list(data)


@given(tuples(INT(), INT(), INT()))
def test_is_iterable_explicitly(data):
    assert list(iter(triplet(*data))) == list(data)


def test_independent_iterators():
    t = triplet(1, 2, 3)
    i1 = iter(t)
    i2 = iter(t)
    assert next(i1) == 1
    assert next(i1) == 2
    assert next(i2) == 1
