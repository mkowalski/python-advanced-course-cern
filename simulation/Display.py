from Particle import Particle


class Display:

    def __init__(self):
        self.canvas_size = (600, 400)

        self.p = Particle(30, (100, 100), (80, 150))
        self.refresh_rate = 1 / 60.0

        self.w = None

    def update(self, dt):
        p, w = self.p, self.w
        p.move(dt)
        p.bounce((0, self.canvas_size[0], 0, self.canvas_size[1]))
