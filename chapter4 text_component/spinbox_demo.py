from tkinter import Tk, Spinbox, Label

win = Tk()
win.title("购买道具")

Label(win, text="购买道具：").grid(row=0, column=0, pady=10)
Spinbox(win, values=("绿水晶","红宝石","生命水")).grid(row=0, column=1, pady=10)

Label(win, text="购买道具：").grid(row=1, column=0, pady=10)
Spinbox(win, from_=1, to=5).grid(row=1, column=1, pady=10)


win.mainloop()