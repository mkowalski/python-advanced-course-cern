from string import hexdigits

from pytest import mark

parametrize = mark.parametrize

from hypothesis import given
from hypothesis.strategies import text
from hypothesis.strategies import sampled_from

O1 = sampled_from(tuple(x / 100 for x in range(101)))

from Colour import Colour, Color


@parametrize('Colour', (Colour, Color))
@given(O1, O1, O1)
def test_rgb_01_should_be_retreivable(Colour, r, g, b):
    c = Colour.from_rgb_01(r, g, b)
    assert c.as_rgb_01() == (r, g, b)


@parametrize('Colour', (Colour, Color))
@parametrize('name, rgb',
             (('BLACK', (0, 0, 0)),
              ('WHITE', (1, 1, 1)),
              ('RED', (1, 0, 0)),
              ('GREEN', (0, 1, 0)),
              ('BLUE', (0, 0, 1)),
              ('YELLOW', (1, 1, 0)),
              ('CYAN', (0, 1, 1)),
              ('MAGENTA', (1, 0, 1))))
def test_named_colours_should_be_available(Colour, name, rgb):
    assert getattr(Colour, name).as_rgb_01() == rgb


@parametrize('Colour', (Colour, Color))
@parametrize('r, g, b, fff',
             ((0, 0, 0, '000'),
              (0.5, 0.5, 0.5, '777'),
              (1, 1, 1, 'fff')))
def test_rgb_f_should_be_retreivable_from_rgb_01(Colour, r, g, b, fff):
    c = Colour.from_rgb_01(r, g, b)
    assert c.as_rgb_f() == fff


@parametrize('Colour', (Colour, Color))
@given(text(alphabet=hexdigits, min_size=3, max_size=3))
def test_rgb_f_should_have_stable_roundtrip(Colour, original):
    assert Colour.from_rgb_f(original).as_rgb_f() == original.lower()
