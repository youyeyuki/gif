try:  # python2
    from Tkinter import *
except ImportError:
    # python3
    from tkinter import *
    from tkinter import ttk


#################################################
def quitapp():
    mainwindow.destroy()


#################################################
mainwindow = Tk()

# topframe = Frame(mainwindow, padx=10, pady=10)
# topframe.pack(side=LEFT)

var = StringVar()
lb = Listbox(mainwindow, width=40, height=20)
lb.grid()
for i in range(15):
    lb.insert(END, "local\風のように_S.E.N.S..mp3")

p1 = ttk.Progressbar(mainwindow, length=700, mode="determinate", orient=HORIZONTAL)
p1.grid(row=1, column=1)
lable = Label(mainwindow,textvariable=var )
lable.grid()
lable.setvar("22222222222")
btn = ttk.Button(mainwindow, text="开始播放", command=lambda: print("2222"))
btn.grid(row=1, column=0)

text = Text(mainwindow)
text.grid(row=0, column=1)

for i in range(30):
    text.insert(END, str(i) + "\n")

mainwindow.title("My App")
mainwindow.mainloop()
###END###
