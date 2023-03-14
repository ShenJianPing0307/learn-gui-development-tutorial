from tkinter.messagebox import showinfo
from tkinter import Tk, Button


def mess():
    showinfo("welcome!", "好久不见，欢迎回来！")


win = Tk()
win.title("会话框")
btn = Button(win, text="进入游戏", command=mess).pack(padx=20, pady=20)
win.mainloop()
