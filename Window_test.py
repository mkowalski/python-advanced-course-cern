from Window import Window, BorderWindow

from hypothesis import given
from hypothesis.strategies import integers


@given(integers(), integers(), integers(), integers())
def test_class_constructor1(x, y, w, h):
    w = Window.constructor1(x, y, w, h)


@given(integers(), integers(), integers(), integers())
def test_class_constructor2(x1, y1, x2, y2):
    w = Window.constructor2(x1, y1, x2, y2)


def test_method_area():
    w = Window.constructor1(0, 0, 0, 0)
    w.area()


def test_method_perimeter():
    w = Window.constructor1(0, 0, 0, 0)
    w.perimeter()


def test_borderwindow_subclass():
    w1 = BorderWindow.constructor1(0, 0, 0, 0)
    w2 = BorderWindow.constructor2(0, 0, 0, 0)
