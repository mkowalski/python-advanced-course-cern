import sys
if sys.argv[1] == "tkinter":
    import tkinter as tk

    master = tk.Tk()

    w = tk.Canvas(master, width=600, height=400, bg='black')
    w.pack()

    x, y = w.winfo_height() / 2, w.winfo_width() / 2
    vx, vy = 80.0, 150.0

    particle_size = 60
    particle = w.create_oval(x, y, particle_size, particle_size,
                             outline='yellow')


    def update(dt, refresh_time=17):
        global x, y, vx, vy
        oldx, oldy = x, y
        x += vx * dt
        y += vy * dt

        if x + particle_size > w.winfo_width():
            x = w.winfo_width() - particle_size
            vx = - vx

        if x < 0:
            x = 0
            vx = - vx

        if y + particle_size > w.winfo_height():
            y = w.winfo_height() - particle_size
            vy = - vy

        if y < 0:
            y = 0
            vy = - vy

        w.move(particle, x - oldx, y - oldy)
        w.update()

        w.after(refresh_time, update, 1 / 60.0)


    update(0)

    tk.mainloop()

elif sys.argv[1] == "pyglet":
    import pyglet
    from math import sin, cos, pi, sqrt

    twopi = 2 * pi

    window = pyglet.window.Window(600, 400)
    fps_display = pyglet.clock.ClockDisplay()

    x, y = window.width / 2, window.height / 2
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
        global x, y, vx, vy
        x += vx * dt
        y += vy * dt

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


    pyglet.clock.schedule_interval(update, 1 / 60.0)

    pyglet.app.run()

