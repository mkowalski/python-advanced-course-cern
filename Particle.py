class Particle:

    def __init__(self, size, position, velocity):
        self.r = size
        (self.x, self.y) = position
        (self.vx, self.vy) = velocity

    def move(self, velocity):
        self.x, self.y = self.x + velocity * self.vx, self.y + velocity * self.vy

    def bounce(self, board):
        (xmin, xmax, ymin, ymax) = board

        def far_miss(particle, border, size):
            return abs(border - particle) + size

        def near_miss(particle, border, size):
            return abs(particle - size - border) * 2

        if self.x - self.r >= xmin and self.x + self.r <= xmax and self.y - self.r >= ymin and self.y + self.r <= ymax:
            pass

        elif self.x - self.r < xmin or self.x + self.r > xmax:
            self.vx = -self.vx

            if self.x - self.r < xmin and self.x < xmin:  self.x = xmin + far_miss(self.x, xmin, self.r) + self.r
            elif self.x - self.r < xmin: self.x = self.x + near_miss(self.x, xmin, self.r)
            elif self.x + self.r > xmax and self.x > xmax: self.x = xmax - far_miss(self.x, xmax, self.r) - self.r
            else: self.x = self.x - near_miss(self.x, xmax, -self.r)

        else:
            self.vy = -self.vy

            if self.y + self.r > ymax and self.y > ymax: self.y = ymax - far_miss(self.y, ymax, self.r) - self.r
            elif self.y + self.r > ymax: self.y = self.y - near_miss(self.y, ymax, -self.r)
            elif self.y - self.r < ymin and self.y < ymin: self.y = ymin + far_miss(self.y, ymin, self.r) + self.r
            else: self.y = self.y + near_miss(self.y, ymin, self.r)

    def bounce(self, bounding_box):
        xmin, xmax, ymin, ymax = bounding_box

        beyond_right = self.x + self.r - xmax
        if beyond_right > 0:
            self.x -= 2 * beyond_right
            self.vx = - self.vx

        beyond_left = self.x - self.r - xmin
        if beyond_left < 0:
            self.x -= 2 * beyond_left
            self.vx = - self.vx

        beyond_top = self.y + self.r - ymax
        if beyond_top > 0:
            self.y -= 2 * beyond_top
            self.vy = - self.vy

        beyond_bottom = self.y - self.r - ymin
        if beyond_bottom < 0:
            self.y -= 2 * beyond_bottom
            self.vy = - self.vy
