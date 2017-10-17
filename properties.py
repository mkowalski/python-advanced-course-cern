class Rect:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        # self.a = w*h

    @property
    def a(self):
        return self.w * self.h

    @a.setter
    def a(self, new):
        self.w = new / self.h


r = Rect(2, 3)
assert r.w == 2
assert r.h == 3
assert r.a == 6

r.w = 4
assert r.w == 4
assert r.h == 3
assert r.a == 12

r.a = 6
assert r.w == 2
assert r.h == 3
assert r.a == 6
