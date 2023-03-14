from tkinter import Canvas, Tk

win = Tk()
win.title("创建canvas画布")

win.geometry("300x200")
canvas = Canvas(win, width=200, height=200, bg="#EFEFA3").pack()
win.mainloop()