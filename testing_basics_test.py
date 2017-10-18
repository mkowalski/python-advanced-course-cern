from math import sqrt
import pytest

from hypothesis import given
from hypothesis.strategies import integers

from context_managers import MyRaises
from context_managers2 import MyRaises2


@given(integers(min_value=-1000, max_value=-1))
def test_negative_manual(n):
    try:
        sqrt(n)
    except ValueError: assert True
    except Exception:  assert False
    else:              assert False


@given(integers(min_value=-1000, max_value=-1))
def test_sqrt_negative(n):
    with pytest.raises(ValueError) as exc_info:
        sqrt(n)

    assert exc_info.type == ValueError


@given(integers(min_value=-1000, max_value=-1))
def test_sqrt_negative_my_class(n):
    with MyRaises(ValueError) as exc_info:
        sqrt(n)

    assert exc_info.type == ValueError


@given(integers(min_value=-1000, max_value=-1))
def test_sqrt_negative_my_class2(n):
    with MyRaises2(ValueError) as exc_info:
        sqrt(-1)

    assert exc_info.type == ValueError
