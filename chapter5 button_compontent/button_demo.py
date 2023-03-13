from tkinter import Tk, Button, Label


def show():
    Label(win, text="hello world").pack()

win = Tk()
btn = Button(win, command=show).pack()

win.mainloop()
