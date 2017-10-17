from magic import *
from hypothesis import given
from hypothesis.strategies import integers

@given(integers(), integers())
def test_complex1_magic(a, b):
    assert magic(b, a) == magic(a, b)

@given(integers())
def test_complex2_magic(a):
    assert a == magic(a, 1)
    assert a == magic(1, a)

@given(integers(), integers(), integers())
def test_comple3_magic(a, b, c):
    assert magic(a, magic(b, c)) == magic(magic(a, b), c)
