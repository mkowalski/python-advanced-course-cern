class Colour:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


    @classmethod
    def from_rgb_01(cls, r, g, b):
        return cls(r, g, b)

    @classmethod
    def from_rgb_f(cls, rgb):
        r = int('0x'+rgb[0], 16) / 15
        g = int('0x'+rgb[1], 16) / 15
        b = int('0x'+rgb[2], 16) / 15
        return cls(r, g, b)

    def as_rgb_01(self):
        return self.r, self.g, self.b

    def as_rgb_f(self):
        rgb = self.r, self.g, self.b
        return ''.join('%x' % int(i*15) for i in rgb)


Colour.BLACK = Colour(0, 0, 0)
Colour.WHITE = Colour(1, 1, 1)
Colour.RED = Colour(1, 0, 0)
Colour.GREEN = Colour(0, 1, 0)
Colour.BLUE = Colour(0, 0, 1)
Colour.YELLOW = Colour(1, 1, 0)
Colour.CYAN = Colour(0, 1, 1)
Colour.MAGENTA = Colour(1, 0, 1)
Color = Colour
