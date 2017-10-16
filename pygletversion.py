import pyglet
from math import sin, cos, pi, sqrt
twopi = 2*pi

window = pyglet.window.Window(600,400)
fps_display = pyglet.clock.ClockDisplay()

x,y = window.width / 2, window.height / 2
vx, vy = 80.0, 150.0

@window.event
def on_draw():
    window.clear()
    def circle_vertices():
        delta_angle = twopi / 20
        angle = 0
        while angle < twopi:
            yield x + 30 * cos(angle)
            yield y + 30 * sin(angle)
            angle += delta_angle

    pyglet.gl.glColor3f(1.0, 1.0, 0)
    pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                         ('v2f', tuple(circle_vertices())))

    fps_display.draw()


def update(dt):
    global x,y, vx, vy
    x += vx*dt
    y += vy*dt

    if x + 30 > window.width:
        x = window.width - 30
        vx = - vx

    if x - 30 < 0:
        x =  30
        vx = - vx

    if y + 30 > window.height:
        y = window.height - 30
        vy = - vy

    if y - 30 < 0:
        y = 30
        vy = - vy

pyglet.clock.schedule_interval(update, 1/60.0)

pyglet.app.run()

