from fib import fib
from pytest import mark


@mark.parametrize('input_ expected_output'.split(),
                  ((0, 0),
                   (1, 1),
                   (2, 1),
                   (3, 2),
                   (4, 3),
                   (5, 5),
                   (6, 8)))
def test_fib_should_give_correct_outputs(input_, expected_output):
    assert fib(input_) == expected_output
