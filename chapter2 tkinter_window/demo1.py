from tkinter import Tk, Label

win = Tk()
win.title('tkinter window') # 设置窗口标题
win.configure(bg="#a7ea90") # 设置窗口背景颜色
winw = 300 # 设置窗口宽度
winh = 200 # 设置窗口高度
scrw = win.winfo_screenwidth() # 获取屏幕宽度
scrh = win.winfo_screenheight() # 获取屏幕高度
x = (scrw-winw) // 2 # 计算窗口水平位置
y = (scrh-winh) // 2 # 计算窗口垂直位置
win.geometry(f"{winw}x{winh}+{x}+{y}")
txt = Label(win, text="hello world!").pack()
win.mainloop()

