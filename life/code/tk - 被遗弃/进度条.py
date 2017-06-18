# -*- coding: cp936 -*-
from tkinter import *
import time
import threading

root = Tk()
root.title("hello world")
root.geometry()


class ye():
    def __init__(self, root):
        self.root = root
        self.t = None
        self.text =None
        self.list_item = [1, 2, 3, 4]


        self.initdata()

    def print_item(self):
        for i in range(10):
            self.lb.insert(END, i)
            time.sleep(3)
        print(self.lb.get(self.lb.curselection()))

    def add_threading(self, fun, name):
        self.t = threading.Thread(target=fun, args=())
        self.t.setName(name)
        self.t.setDaemon(False)

    def start(self):
        print(2333)
        self.text.insert(INSERT, "Hello.....\n")
        self.text.insert(END, "Bye Bye.....")



    def initdata(self):
        var = StringVar()
        self.lb = Listbox(root, listvariable=var)

        for item in self.list_item:
            self.lb.insert(END, item)

        self.text = Text(self.root)
        self.text.pack()
        button = Button(root, text="start", command=self.start)
        button.pack()
        # var.set(('a', 'ab', 'c', 'd'))   #重新设置了，这时控件的内容就编程var的内容了
        print(var.get())
        self.lb.bind('<ButtonRelease-1>', self.print_item)
        self.lb.pack()


s = ye(root)
root.mainloop()

