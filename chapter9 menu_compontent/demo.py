from tkinter import Menu, Tk

win = Tk()
win.title("添加菜单")
menu1 = Menu(win)

menu1.add_command(label="游戏")
menu1.add_command(label="帮助")
menu1.add_command(label="退出")

win.configure(menu=menu1)
win.mainloop()