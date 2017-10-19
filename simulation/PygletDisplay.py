from Display import Display
import pyglet
from math import sin, cos, pi


class PygletDisplay(Display):

    def __init__(self):
        super(PygletDisplay, self).__init__()

        self.w = pyglet.window.Window(self.canvas_size[0], self.canvas_size[1])
        self.fps_display = pyglet.clock.ClockDisplay()

        self.w.push_handlers(self.on_draw)

    def on_draw(self):
        self.w.clear()

        def circle_vertices(p):
            twopi = 2 * pi
            delta_angle = twopi / 20
            angle = 0
            while angle < twopi:
                yield p.x + p.r * cos(angle)
                yield p.y + p.r * sin(angle)
                angle += delta_angle

        for p in self.particles:
            pyglet.gl.glColor3f(*p.colour.as_rgb_01())
            pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                                ('v2f', tuple(circle_vertices(p))))

        self.fps_display.draw()

    def __call__(self, *args, **kwargs):
        pyglet.clock.schedule_interval(self.update, self.refresh_rate)
        pyglet.app.run()
