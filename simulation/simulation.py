import sys
from Particle import Particle
from Colour import Colour


if sys.argv[1] == "tkinter":
    from TkinterDisplay import TkinterDisplay as Display

elif sys.argv[1] == "pyglet":
    from PygletDisplay import PygletDisplay as Display

else:
    raise Exception("No command")

d = Display()
d.add_particle(Particle(30, (100, 100), (80, 150), Colour.YELLOW))
d.add_particle(Particle(40, (150, 1), (30, 100), Colour.BLUE))
d.add_particle(Particle(20, (200, 200), (100, 30), Colour.GREEN))
d()
