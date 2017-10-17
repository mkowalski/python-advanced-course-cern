class Particle:

    def __init__(self, size, position, velocity):
        self.r = size
        (self.x, self.y) = position
        (self.vx, self.vy) = velocity

    def move(self, velocity):
        self.x, self.y = self.x + velocity * self.vx, self.y + velocity * self.vy

    def bounce(self, board):
        (xmin, xmax, ymin, ymax) = board
        # A whole particle inside
        if self.x - self.r >= xmin and self.x + self.r <= xmax and self.y - self.r >= ymin and self.y + self.r <= ymax:
            pass

        # Left border crossed
        elif self.x - self.r < xmin:
            self.vx = -self.vx
            # ... far
            if self.x < xmin:
                miss = abs(xmin - self.x) + self.r
                self.x = xmin + miss + self.r
            # ... near
            else:
                miss = abs(self.x - self.r - xmin)
                self.x = self.x + miss*2

        # Right border crossed
        elif self.x + self.r > xmax:
            self.vx = -self.vx
            # ... far
            if self.x > xmax:
                miss = abs(xmax - self.x) + self.r
                self.x = xmax - miss - self.r
            # ... near
            else:
                miss = abs(self.x + self.r - xmax)
                self.x = self.x - miss * 2

        # Top border crossed
        elif self.y + self.r > ymax:
            self.vy = -self.vy
            # ... far
            if self.y > ymax:
                miss = abs(ymax - self.y) + self.r
                self.y = ymax - miss - self.r
            # ... near
            else:
                miss = abs(self.y + self.r - ymax)
                self.y = self.y - miss * 2

        # Bottom border crossed
        elif self.y - self.r < ymin:
            self.vy = -self.vy
            # ... far
            if self.y < ymin:
                miss = abs(ymin - self.y) + self.r
                self.y = ymin + miss + self.r
            # ... near
            else:
                miss = abs(self.y - self.r - ymin)
                self.y = self.y + miss*2
