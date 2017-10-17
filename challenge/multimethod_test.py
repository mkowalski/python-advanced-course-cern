from pytest import raises, mark
from multimethod import multimethod


def test_simple_multiple_dispatch_should_work():
    class Rock:     pass

    class Paper:    pass

    class Scissors: pass

    @multimethod
    def winner(l: Rock, r: Paper):    return 'right'

    @multimethod
    def winner(l: Paper, r: Scissors): return 'right'

    @multimethod
    def winner(l: Scissors, r: Rock):     return 'right'

    @multimethod
    def winner(l: Paper, r: Rock):     return 'left'

    @multimethod
    def winner(l: Scissors, r: Paper):    return 'left'

    @multimethod
    def winner(l: Rock, r: Scissors): return 'left'

    rock, paper, scissors = Rock(), Paper(), Scissors()

    assert winner(rock, paper) == 'right'
    assert winner(paper, scissors) == 'right'
    assert winner(scissors, rock) == 'right'
    assert winner(paper, rock) == 'left'
    assert winner(scissors, paper) == 'left'
    assert winner(rock, scissors) == 'left'


def test_multimethod_should_raise_TypeError_if_no_method_matching_argument_types_exists():
    class A: pass

    @multimethod
    def baz(a: A, b: int): pass

    with raises(TypeError):
        baz(1, 2)


def test_multimethods_should_respect_inheritance():
    class A:    pass

    class B(A): pass

    class MyInt(int): pass

    @multimethod
    def zot(a: A, i: int): return A, int

    assert zot(B(), MyInt()) == (A, int)

    # After adding a better matching method to the generic function,
    # the new method should be found in response to the same request
    @multimethod
    def zot(b: B, i: int): return (B, int)

    assert zot(B(), MyInt()) == (B, int)


def test_multimethods_should_respect_inheritance_harraudeau_bug():
    class A:    pass

    class B(A): pass

    class C(A): pass

    @multimethod
    def qux(l: A, r: A): return A, A

    @multimethod
    def qux(l: B, r: B): return B, B

    assert qux(B(), C()) == (A, A)


@mark.parametrize('i j'.split(),
                  ((1, 2),
                   (4, 5)))
def test_values_are_used(i, j):
    @multimethod
    def fubar(a: int, b: int):
        return a + b

    assert fubar(i, j) == i + j


def test_can_overload_on_number_of_arguments():
    @multimethod
    def argnum():
        return 0

    @multimethod
    def argnum(_: int):
        return 1

    @multimethod
    def argnum(_: int, __: int):
        return 2

    @multimethod
    def argnum(_: int, __: int, ___: int):
        return 3

    assert argnum(1, 2, 3) == 3
    assert argnum() == 0
    assert argnum(4) == 1
    assert argnum(5, 6) == 2


def test_generic_functions_do_not_clobber_eachothers_methods():
    @multimethod
    def genfn1(a: int, b: int):
        return a + b

    assert genfn1(3, 4) == 7

    @multimethod
    def genfn2(a: int, b: int):
        return a - b

    assert genfn2(3, 4) == -1
    assert genfn1(3, 4) == 7


@mark.skipif(False, reason="Had enough of this exercise")
def test_choosing_between_multiple_applicable_methods():
    # When more than one method is applicable, preference should be
    # given to those methods which have nearer type-matches in the
    # arguments nearer the front of the argument list.

    class A1:     pass

    class A2(A1): pass

    class B1:     pass

    class B2(B1): pass

    class C1:     pass

    class C2(C1): pass

    @multimethod
    def luck(a: A1, b: B1, c: C1): return A1, B1, C1

    @multimethod
    def luck(a: A2, b: B1, c: C1): return A2, B1, C1

    @multimethod
    def luck(a: A1, b: B2, c: C1): return A1, B2, C1

    @multimethod
    def luck(a: A1, b: B1, c: C2): return A1, B1, C2

    @multimethod
    def luck(a: A1, b: B2, c: C2): return A1, B2, C2

    @multimethod
    def luck(a: A2, b: B1, c: C2): return A2, B1, C2

    @multimethod
    def luck(a: A2, b: B2, c: C1): return A2, B2, C1

    assert luck(A2(), B2(), C2()) == (A2, B2, C1)

    # To Do

    # Add test which checks that you cannot pass by storing the result of
    # the first method call, rather than the method itself.

    # Remove generic function

    # Docstrings ?

    # Removal of Methods ?

    # Call next method ?
