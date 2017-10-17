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

        # A whole particle inside
        if self.x - self.r >= xmin and self.x + self.r <= xmax and self.y - self.r >= ymin and self.y + self.r <= ymax:
            pass

        # Left border crossed
        elif self.x - self.r < xmin:
            self.vx = -self.vx
            # ... far
            if self.x < xmin:
                self.x = xmin + far_miss(self.x, xmin, self.r) + self.r
            # ... near
            else:
                self.x = self.x + near_miss(self.x, xmin, self.r)

        # Right border crossed
        elif self.x + self.r > xmax:
            self.vx = -self.vx
            # ... far
            if self.x > xmax:
                self.x = xmax - far_miss(self.x, xmax, self.r) - self.r
            # ... near
            else:
                self.x = self.x - near_miss(self.x, xmax, -self.r)

        # Top border crossed
        elif self.y + self.r > ymax:
            self.vy = -self.vy
            # ... far
            if self.y > ymax:
                self.y = ymax - far_miss(self.y, ymax, self.r) - self.r
            # ... near
            else:
                self.y = self.y - near_miss(self.y, ymax, -self.r)

        # Bottom border crossed
        elif self.y - self.r < ymin:
            self.vy = -self.vy
            # ... far
            if self.y < ymin:
                self.y = ymin + far_miss(self.y, ymin, self.r) + self.r
            # ... near
            else:
                self.y = self.y + near_miss(self.y, ymin, self.r)
