import pyglet
from math import sin, cos, pi, sqrt
twopi = 2*pi

window = pyglet.window.Window(600,400)
fps_display = pyglet.clock.ClockDisplay()

x,y = window.width / 2, window.height / 2
vx, vy = 80.0, 150.0

particle_size = 30

@window.event
def on_draw():
    window.clear()
    def circle_vertices():
        delta_angle = twopi / 20
        angle = 0
        while angle < twopi:
            yield x + particle_size * cos(angle)
            yield y + particle_size * sin(angle)
            angle += delta_angle

    pyglet.gl.glColor3f(1.0, 1.0, 0)
    pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                         ('v2f', tuple(circle_vertices())))

    fps_display.draw()


def update(dt):
    global x,y, vx, vy
    x += vx*dt
    y += vy*dt

    if x + particle_size > window.width:
        x = window.width - particle_size
        vx = - vx

    if x - particle_size < 0:
        x = particle_size
        vx = - vx

    if y + particle_size > window.height:
        y = window.height - particle_size
        vy = - vy

    if y - particle_size < 0:
        y = particle_size
        vy = - vy

pyglet.clock.schedule_interval(update, 1/60.0)

pyglet.app.run()

