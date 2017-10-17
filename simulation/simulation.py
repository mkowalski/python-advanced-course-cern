import sys

if sys.argv[1] == "tkinter":
    from TkinterDisplay import TkinterDisplay as Display

elif sys.argv[1] == "pyglet":
    from PygletDisplay import PygletDisplay as Display

else:
    raise Exception("No command")

d = Display()
d()
