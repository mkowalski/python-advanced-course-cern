class Window:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @classmethod
    def constructor1(cls, x, y, width, height):
        return cls(x, y, width, height)

    @classmethod
    def constructor2(cls, x1, y1, x2, y2):
        return cls(x1, y1, abs(x2-x1), (y2-y1))

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


class BorderWindow(Window):

    def __init__(self, x, y, width, height):
        # Window.__init__(self, x, y, width + 10, height + 10)
        super().__init__(x, y, width + 10, height + 10)
