from test_helpers import assert_evolution
from pytest import raises
from operator import eq, gt

def test_assert_evolution_should_work_with_constant_expression_and_eq():
    assert_invariant = assert_evolution(lambda:x, eq)
    for x in 'aaaaa':
        assert_invariant()

def test_assert_evolution_should_fail_with_non_constant_expression_and_eq():
    assert_invariant = assert_evolution(lambda:x, eq)
    x = 1
    assert_invariant()
    assert_invariant()
    x = 2
    with raises(AssertionError):
        assert_invariant()

def test_assert_evolution_should_work_with_increasing_expression_and_gt():
    assert_increasing = assert_evolution(lambda:x, gt)
    for x in range(20):
        assert_increasing()

    x -= 2
    with raises(AssertionError):
        assert_increasing()

def test_assert_evolution_should_fail_with_constant_expression_and_gt():
    assert_increasing = assert_evolution(lambda:x, gt)
    x = 1
    assert_increasing()
    with raises(AssertionError):
        assert_increasing()
