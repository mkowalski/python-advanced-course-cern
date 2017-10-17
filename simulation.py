import sys
import tkinter as tk
import pyglet
from math import sin, cos, pi, sqrt


class Display:
    pass


class PygletDisplay(Display):

    def __init__(self):
        self.window = pyglet.window.Window(600, 400)
        self.fps_display = pyglet.clock.ClockDisplay()

        self.x, self.y = self.window.width / 2, self.window.height / 2
        self.vx, self.vy = 80.0, 150.0

        self.particle_size = 30

        self.window.push_handlers(self.on_draw)

    def on_draw(self):
        self.window.clear()

        def circle_vertices():
            twopi = 2 * pi
            delta_angle = twopi / 20
            angle = 0
            while angle < twopi:
                yield self.x + self.particle_size * cos(angle)
                yield self.y + self.particle_size * sin(angle)
                angle += delta_angle

        pyglet.gl.glColor3f(1.0, 1.0, 0)
        pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                             ('v2f', tuple(circle_vertices())))

        self.fps_display.draw()

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        if self.x + self.particle_size > self.window.width:
            self.x = self.window.width - self.particle_size
            self.vx = - self.vx

        if self.x - self.particle_size < 0:
            self.x = self.particle_size
            self.vx = - self.vx

        if self.y + self.particle_size > self.window.height:
            self.y = self.window.height - self.particle_size
            self.vy = - self.vy

        if self.y - self.particle_size < 0:
            self.y = self.particle_size
            self.vy = - self.vy

    def __call__(self, *args, **kwargs):
        pyglet.clock.schedule_interval(self.update, 1 / 60.0)
        pyglet.app.run()


class TkinterDisplay(Display):

    def __init__(self):
        master = tk.Tk()

        self.w = tk.Canvas(master, width=600, height=400, bg='black')
        self.w.pack()

        self.x, self.y = self.w.winfo_height() / 2, self.w.winfo_width() / 2
        self.vx, self.vy = 80.0, 150.0

        self.particle_size = 60
        self.particle = self.w.create_oval(self.x, self.y, self.particle_size, self.particle_size, outline='yellow')

    def update(self, dt, refresh_time=17):
        oldx, oldy = self.x, self.y
        self.x += self.vx * dt
        self.y += self.vy * dt

        if self.x + self.particle_size > self.w.winfo_width():
            self.x = self.w.winfo_width() - self.particle_size
            self.vx = - self.vx

        if self.x < 0:
            self.x = 0
            self.vx = - self.vx

        if self.y + self.particle_size > self.w.winfo_height():
            self.y = self.w.winfo_height() - self.particle_size
            self.vy = - self.vy

        if self.y < 0:
            self.y = 0
            self.vy = - self.vy

        self.w.move(self.particle, self.x - oldx, self.y - oldy)
        self.w.update()

        self.w.after(refresh_time, self.update, 1 / 60.0)

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
