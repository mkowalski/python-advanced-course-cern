class Display:

    def __init__(self):
        self.canvas_size = (600, 400)
        self.refresh_rate = 1 / 60.0

        self.w = None

        self.particles = []

    def update(self, dt):
        w = self.w

        for p in self.particles:
            p.move(dt)
            p.bounce((0, self.canvas_size[0], 0, self.canvas_size[1]))

    def add_particle(self, particle):
        self.particles.append(particle)
