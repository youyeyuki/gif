# from tkinter import *
#
#
# class yeButtons:
#     def __init__(self, master):
#         frame = Frame(master)
#         frame.pack()
#
#         self.printButton = Button(frame, text="Print Message ", command=self.printMessage)
#         self.printButton.pack(side=LEFT)
#
#         self.quitButton = Button(frame, text="exit ", command=frame.quit) # 不要括号
#
#         self.quitButton.pack(side=LEFT)
#
#     def printMessage(self):
#         print(" =======================")
#
#
# root = Tk()
# b = yeButtons(root)
# root.mainloop()



# drop down menus

# from tkinter import *
#
#
# def doNothing():
#     print(" dogn ")
#
#
# root = Tk()
#
# menu = Menu(root)
# root.config(menu=menu)
#
# subMeun = Menu(menu)
# menu.add_cascade(label="File", menu=subMeun)
# subMeun.add_command(label="Now Project...",command=doNothing)
# subMeun.add_command(label="Now ...",command=doNothing)
# subMeun.add_separator()  # 分离器 就是横线
# subMeun.add_command(label="exit",command=doNothing)
#
#
# editMeun = Menu(menu)
# menu.add_cascade(label="Edit",menu=editMeun)
# editMeun.add_command(label="Redo",command=doNothing)


# create toolbar
#
# from tkinter import *
#
#
# def doNothing():
#     print(" dogn ")
#
#
# root = Tk()
# # *************    Main meun   ***********
# menu = Menu(root)
# root.config(menu=menu)
#
# subMeun = Menu(menu)
# menu.add_cascade(label="File", menu=subMeun)
# subMeun.add_command(label="Now Project...", command=doNothing)
# subMeun.add_command(label="Now ...", command=doNothing)
# subMeun.add_separator()  # 分离器 就是横线
# subMeun.add_command(label="exit", command=doNothing)
#
# editMeun = Menu(menu)
# menu.add_cascade(label="Edit", menu=editMeun)
# editMeun.add_command(label="Redo", command=doNothing)
#
# # ************* tool bar ************
#
# toolbar = Frame(root, bg="blue")
# insertButt = Button(toolbar, text="Insert Image ", command=doNothing)
# insertButt.pack(side=LEFT, padx=2, pady=2)
# printButt = Button(toolbar, text="Print", command=doNothing)
# printButt.pack(side=LEFT, padx=2, pady=2)
#
# toolbar.pack(side=TOP, fill=X)
#
# # ************* status bar ************
#
# status = Label(root, text="Peraring to do nothing ", bd=1, relief=SUNKEN, anchor=W)
# status.pack(side=BOTTOM,fill=X)
#
#
# root.mainloop()


# message show
# from tkinter import *
# import tkinter.messagebox
#
# root = Tk()
# tkinter.messagebox.showinfo('windows title ','Monkeys can live up 200 geasss')
#
# answer = tkinter.messagebox.askquestion("Question ","Do you like silly faces ")
# if answer == 'yes':
#     print('@@@@@@@@@@@@@@@@@')
# root.mainloop()


# shapes and  graphics

# from tkinter import *
# import tkinter.messagebox
#
# root = Tk()
# canvas = Canvas(root, width=200, height=100)
# canvas.pack()
#
# blackLine = canvas.create_line(0, 0, 200, 50)
# redkLine = canvas.create_line(0, 100, 200, 50,fill="red")
# greenBox = canvas.create_rectangle(25,25,130,60,fill="green")
#
# canvas.delete(redkLine) #canvas.delete(ALL)
# root.mainloop()

#
# from tkinter import *
#
#
# root = Tk()
# pho =PhotoImage(file="1.png")
# label = Label(root,image=pho)
# label.pack()
#
#
# root.mainloop()
#


import time
from tkinter import *


class MyApp:
    def __init__(self, parent):
        self.myParent = parent  ### (7) remember my parent, the root
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        self.button1 = Button(self.myContainer1)
        self.button1.configure(text="Button")
        self.button1.pack()
        self.button1.bind("<Button-1>", self.button1Click)

        self.lbl = Label(self.myContainer1)
        self.lbl.pack()

        self.button2 = Button(self.myContainer1)
        self.button2.configure(text="Quit", background="red")
        self.button2.pack()
        self.button2.bind("<Button-1>", self.button2Click)

    def button1Click(self, event):  ### (3)
        # expensive process here
        # simulated by time.sleep
        self.lbl.configure(text='Running command...')
        self.myContainer1.update_idletasks()
        time.sleep(4)
        self.lbl.configure(text='Finished running command...')

    def button2Click(self, event):  ### (5)
        self.myParent.destroy()  ### (6)


root = Tk()
myapp = MyApp(root)
root.mainloop()
