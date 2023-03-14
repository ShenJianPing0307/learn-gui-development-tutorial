from tkinter import Tk
from tkinter.ttk import Treeview
import os


class Tree:

    def __init__(self, path):
        self.win = Tk()
        self.win.title("显示")
        self.tree = Treeview()
        self.tree.heading("#0", text="file")
        temppath = os.path.basename(path)

        treeF = self.tree.insert('', 0, text=temppath)
        self.show_tree(path, treeF)
        self.win.mainloop()

    def show_tree(self, path, root):
        file_list = os.listdir(path)

        for file_name in file_list:
            abs_path = os.path.join(path, file_name)
            tree_fin_side = self.tree.insert(root, 0, text=file_name, values=(abs_path))
            if os.path.isdir(abs_path):
                self.show_tree(abs_path, tree_fin_side)


tree = Tree("E:\\python-tutorial\\learn-gui-development-tutorial")
