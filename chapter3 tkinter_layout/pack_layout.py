from tkinter import Tk, Label

win = Tk()

txt1 = "春眠不觉晓"
txt2 = "处处闻啼鸟"

Label(win, text=txt1, bg="#F5DFCC").pack(side="bottom")
Label(win, text=txt1).pack(side="bottom")

win.mainloop()


