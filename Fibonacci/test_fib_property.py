from fib import fib

from hypothesis import given
from hypothesis.strategies import integers


@given(integers(min_value=2, max_value=10000))
def test_fib_should_be_sum_of_previous_two(n):
    assert fib(n) == fib(n-1) + fib(n-2)
