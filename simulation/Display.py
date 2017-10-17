from Particle import Particle


class Display:

    def __init__(self):
        self.p = Particle(30, (100, 100), (80, 150))
        self.refresh_rate = 1 / 60.0
