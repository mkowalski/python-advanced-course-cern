from Display import Display
import pyglet
from math import sin, cos, pi


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
