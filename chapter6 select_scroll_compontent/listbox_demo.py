from tkinter import Tk, Listbox, END

win = Tk()
items = ["苹果", "香蕉", "葡萄"]

list_box = Listbox(win)

for item in items:
    list_box.insert(END, item)

list_box.pack()
win.mainloop()

