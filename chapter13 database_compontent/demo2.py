from tkinter import Tk, END
from tkinter.ttk import Treeview
import sqlite3


conn = sqlite3.connect('mrsoft.db')

cursor = conn.cursor()

cursor.execute('select * from user')

result = cursor.fetchall()





win = Tk()
win.title("查看用户信息")
tree = Treeview(win, columns=("id","name"), show="headings")
tree.pack()

tree.heading("id", text="序号")
tree.heading("name", text="用户名")

for i in range(len(result)):
    tree.insert("", END, values=result[i])
conn.close()
win.mainloop()