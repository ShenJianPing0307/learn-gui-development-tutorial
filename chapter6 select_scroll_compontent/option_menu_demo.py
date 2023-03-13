from tkinter import Tk, StringVar, OptionMenu
from tkinter.ttk import OptionMenu

win = Tk()
val = StringVar()

option_menu = OptionMenu(win, val, *("苹果", "香蕉", "葡萄"))
option_menu.pack()
win.mainloop()