from tkinter import Tk, IntVar
from tkinter.ttk import Progressbar
import random
import time

win = Tk()
vari = IntVar()
vari.set(0)
# for i in range(1, 101):
#     vari.set(i)
#     time.sleep(random.uniform(0.5, 1.0))
Progressbar(win, variable=vari, mode="determinate").pack()
win.mainloop()