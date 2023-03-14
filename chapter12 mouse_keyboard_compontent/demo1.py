from tkinter import Tk, Label


def show1(event):
    label.config(text="我是Label组件")


def hidden1(event):
    label.config(text="")


win = Tk()
label = Label(win, bg="#C5E1EF", width=20, height=3)
label.pack(pady=20, padx=20)
label.bind("<Enter>", show1)
label.bind("<Leave>", hidden1)

win.mainloop()
