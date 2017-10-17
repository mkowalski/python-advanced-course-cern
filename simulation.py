import sys
import tkinter as tk
import pyglet
from math import sin, cos, pi, sqrt
from Particle import Particle


class Display:

    def __init__(self):
        self.p = Particle(30, (100, 100), (80, 150))
        self.refresh_rate = 1 / 60.0


class PygletDisplay(Display):

    def __init__(self):
        super(PygletDisplay, self).__init__()

        self.w = pyglet.window.Window(600, 400)
        self.fps_display = pyglet.clock.ClockDisplay()

        self.w.push_handlers(self.on_draw)

    def on_draw(self):
        self.w.clear()

        def circle_vertices():
            p = self.p

            twopi = 2 * pi
            delta_angle = twopi / 20
            angle = 0
            while angle < twopi:
                yield p.x + p.r * cos(angle)
                yield p.y + p.r * sin(angle)
                angle += delta_angle

        pyglet.gl.glColor3f(1.0, 1.0, 0)
        pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                             ('v2f', tuple(circle_vertices())))

        self.fps_display.draw()

    def update(self, dt):
        p, w = self.p, self.w
        p.move(dt)
        p.bounce((0, w.get_size()[0], 0, w.get_size()[1]))

    def __call__(self, *args, **kwargs):
        pyglet.clock.schedule_interval(self.update, self.refresh_rate)
        pyglet.app.run()


class TkinterDisplay(Display):

    def __init__(self):
        super(TkinterDisplay, self).__init__()

        master = tk.Tk()

        w = tk.Canvas(master, width=600, height=400, bg='black')
        w.pack()
        self.w = w

        self.refresh_time = 17

    def update(self, dt):
        p, w = self.p, self.w
        p.move(dt)
        p.bounce((0, w.winfo_width(), 0, w.winfo_height()))

        w.delete(tk.ALL)

        w.create_oval(p.x - p.r, p.y - p.r,
                      p.x + p.r, p.y + p.r,
                      outline='yellow')

        w.update()
        w.after(self.refresh_time, self.update, self.refresh_rate)

    def __call__(self, *args, **kwargs):
        self.update(0)
        tk.mainloop()


if sys.argv[1] == "tkinter":
    simulation = TkinterDisplay()

elif sys.argv[1] == "pyglet":
    simulation = PygletDisplay()

else:
    raise Exception("No command")

simulation()
