import tkinter as tk

master = tk.Tk()

w = tk.Canvas(master, width=600, height=400, bg='black')
w.pack()

x,y = w.winfo_height() / 2, w.winfo_width() / 2
vx, vy = 80.0, 150.0

particle = w.create_oval(x,y, 60,60, outline='yellow')

def update(dt):
    global x,y, vx, vy
    oldx, oldy = x,y
    x += vx*dt
    y += vy*dt

    if x + 60 > w.winfo_width():
        x = w.winfo_width() - 60
        vx = - vx

    if x < 0:
        x = 0
        vx = - vx

    if y + 60 > w.winfo_height():
        y = w.winfo_height() - 60
        vy = - vy

    if y < 0:
        y = 0
        vy = - vy

    w.move(particle, x-oldx, y-oldy)
    w.update()
    w.after(17, update, 1/60.0)

update(0)

tk.mainloop()
