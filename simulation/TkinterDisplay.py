from Display import Display
import tkinter as tk


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
