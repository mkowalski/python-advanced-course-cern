import tkinter as tk

master = tk.Tk()

w = tk.Canvas(master, width=600, height=400, bg='black')
w.pack()

x,y = w.winfo_height() / 2, w.winfo_width() / 2
vx, vy = 80.0, 150.0

particle_size = 60
particle = w.create_oval(x, y, particle_size, particle_size, outline='yellow')

def update(dt, refresh_time=17):
    global x,y, vx, vy
    oldx, oldy = x,y
    x += vx*dt
    y += vy*dt

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

    w.move(particle, x-oldx, y-oldy)
    w.update()

    w.after(refresh_time, update, 1/60.0)

update(0)

tk.mainloop()
