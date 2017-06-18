# from tkinter import *
# from PIL import Image,ImageTk
# root = Tk()
#
# png_image = PhotoImage(file=r"1.png")
# label = Label(root, image=png_image)
# label.pack()
#
#
#
# root.geometry()
# root.mainloop()
#
#
# class Window(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#



# import tkinter
#
# root = tkinter.Tk()
# root.overrideredirect(True)
# root.geometry("300x200+10+10")
# png_image = tkinter.PhotoImage(file=r"1.png")
# canvas = tkinter.Canvas(root)
# canvas.configure(width=300)
# canvas.configure(height=200)
# canvas.configure(bg='blue')
# canvas.configure(highlightthickness=0)
# canvas.pack()
# x, y = 0, 0
#
#
# def move(event):
#     global x, y
#     new_x = (event.x - x) + root.winfo_x()
#     new_y = (event.y - y) + root.winfo_y()
#     s = "300x200+" + str(new_x) + "+" + str(new_y)
#     root.geometry(s)
#     print("s = ", s)
#     print(root.winfo_x(), root.winfo_y())
#     print(event.x, event.y)
#     print()
#
#
# def button_1(event):
#     global x, y
#     x, y = event.x, event.y
#     print("event.x, event.y = ", event.x, event.y)
#
#
# canvas.bind("<B1-Motion>", move)
# canvas.bind("<Button-1>", button_1)
# root.mainloop()


#
# from tkinter import *
# from PIL import ImageTk
#
# root=Tk()
# root.overrideredirect(True)
# root.attributes("-transparentcolor","white")
# canvas = Canvas(root,width = 600, height = 400, bg = None)
# canvas.pack(expand = YES, fill = BOTH)
#
# image = ImageTk.PhotoImage(file = r"1.png")
# canvas.create_image(100, 100, image = image, anchor = NW)
#
# root.mainloop()

# -*- coding: utf-8 -*-

# import tkinter
#
# root = tkinter.Tk()
# #这一行可以隐藏掉窗口边框和标题栏
# root.overrideredirect(True)
# root["width"] = 100
# root["height"] = 80
# #这一行可以将所有的白色透明掉
# root.attributes("-transparentcolor","white")
# root["background"] = "white"
#
# x, y = 0, 0
#
# def StartMove(event):
#     global x, y
#     x = event.x
#     y = event.y
# def StopMove(event):
#     x = None
#     y = None
# def OnMotion(event):
#     global x, y
#     deltax = event.x - x
#     deltay = event.y - y
#     _x = root.winfo_x() + deltax
#     _y = root.winfo_y() + deltay
#     root.geometry("+%s+%s" % (_x, _y))
#
#
# label = tkinter.Label(root, text="ddddd", bg="white")
# label.place(x=10, y=10, anchor=tkinter.NW)
#
# root.bind("<ButtonPress-1>", StartMove)
# root.bind("<ButtonRelease-1>", StopMove)
# root.bind("<B1-Motion>", OnMotion)
#
# root.mainloop()


# import time
# import ttk
# from tkinter import *
#
# mGui = Tk()
#
# mGui.geometry('450x450')
# mGui.title('Hanix Downloader')
#
# mpb = ttk.Progressbar(mGui,orient ="horizontal",length = 200, mode ="determinate")
# mpb.pack()
# mpb["maximum"] = 10000000000000000000000000000
# mpb["value"] =1
# mpb.tk_setPalette()
# # for i in range(1000):
# #     mpb["value"] = i
# #     input()
#
#
#
# mGui.mainloop()
import hashlib
import os

from pydub import AudioSegment
from pydub.playback import play

from tkinter import *
from tkinter import ttk
import threading
import time
import sqlite3


class clock():
    def __init__(self):
        self.hour = 0
        self.min = 0
        self.sec = 0
        self.time = 0

    def getTime(self, time):
        self.time = int(time)
        self.hour, self.min, self.sec = self.sec_to_min(time)
        print("{:0>2}:{:0>2}:{:0>2}".format(self.hour, self.min, self.sec))

    def sec_to_min(self, time):
        hour = time // 3600
        min, sec = divmod((time % 3600), 60)
        return (int(hour), int(min), int(sec))

    def count_down(self):
        cd_time = self.time
        while cd_time:
            time.sleep(1)
            cd_time -= 1
            print("{:0>2}:{:0>2}:{:0>2}".format(*self.sec_to_min(cd_time)))
        print("over")


class SampleApp():
    def __init__(self, root):

        self.appUI(root)

        self.bytes = 0
        self.first = 0

        ########################
        self.progress["value"] = 0
        self.progress["maximum"] = 300
        self.isStop = True
        # l = Label(root, text="show", bg="green", font=("Arial", 12), width=5, height=2)
        # l.grid(side=LEFT)  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM

        ########################


        ##############################
        # sqlite


        #################################

        ##############
        self.songs_list = ["Here Comes The King_X-Ray Dog.mp3", ""]
        self.song_local = []
        self.now = ""
        self.th = []
        self.th1 = None

        ###############
        self.init_data()

    def appUI(self, root):
        self.lb = Listbox(root, width=40, height=20)
        self.lb.grid()

        self.progress = ttk.Progressbar(root, orient="horizontal",
                                        length=700, mode="determinate")
        self.progress.grid(row=1, column=1)

        self.btn = ttk.Button(root, text="开始播放", command=self.start)
        self.btn.grid(row=1, column=0)

        self.text = Text(root)
        self.text.grid(row=0, column=1)

    def init_data(self):

        self.add_threading("parseData", self.parseJson, "解析数据中")
        self.add_threading("playmusic", self.playMusic)
        self.add_threading("status", self.status_bar)

    def add_threading(self, name, fun, *arg):
        th1 = threading.Thread(target=fun, args=(arg))
        self.th.append(th1)
        th1.setName(name)
        th1.setDaemon(False)

    def startTj(self):
        for x in self.th:
            x.start()

    def parseJson(self, xc):
        i = 1
        while 1:
            print(xc + "121222")
            time.sleep(1000)
            i += 1
            if i % 50 == 0:
                self.text.insert(i)
                self.add_list("play list {}".format(i))

    def add_list(self, music):
        self.songs_list.append(music)
        print('now list is .....\n')
        for i in self.songs_list:
            print(i)
        print("\n\n")

    def sec_to_min(self, time):
        hour = time // 3600
        min, sec = divmod((time % 3600), 60)
        return (int(hour), int(min), int(sec))

    def add_localMusic(self):
        cn = sqlite3.connect("musicDataBases.db")
        cur = cn.cursor()
        sql = "SELECT localPath FROM localMusic ORDER BY RANDOM() limit 10"
        cur.execute(sql)
        for x in cur.fetchall():
            self.song_local.append(x[0])

    def showsongs(self, x=0):

        print("播放列表\n")
        for i in x:
            #self.lb.insert(i)
            print(i)

    def playMusic(self):
        while 1:
            if self.isStop:
                if not self.songs_list:

                    if not self.song_local:
                        # 没有音乐添加本地音乐
                        self.add_localMusic()
                    if not self.songs_list:
                        self.bytes = 0
                        try:
                            self.now = self.song_local[0]
                            mysong = AudioSegment.from_mp3(self.now)
                            self.progress["maximum"] = mysong.duration_seconds
                            self.isStop = False
                            print("本地歌曲播放")
                            threading.Thread(target=self.showsongs, args=self.song_local).start()
                            # playing 之前update
                            play(mysong)
                            self.song_local = self.song_local[1:]
                            self.isStop = True
                        except:
                            self.song_local = self.song_local[1:]
                            print("文件不存在 播放跳到下一首")

                else:
                    print("网络歌曲播放")
                    self.bytes = 0
                    try:
                        self.now = self.songs_list[0]
                        mysong = AudioSegment.from_mp3(self.now)

                        self.progress["maximum"] = mysong.duration_seconds
                        self.isStop = False
                        self.showsongs(self.songs_list)
                        # playing 之前update
                        play(mysong)
                        self.songs_list = self.songs_list[1:]
                        self.isStop = True
                    except:
                        self.songs_list = self.songs_list[1:]
                        print("文件不存在 播放跳到下一首")

    def start(self):

        self.startTj()
        print("===============================")

    def status_bar(self):
        while 1:
            if not self.isStop:
                self.bytes += 2
                self.progress["value"] = self.bytes
                if self.bytes < self.progress["maximum"]:
                    # read more bytes after 100 ms
                    try:
                        sys.stdout.write(
                            "\r{} {:0>2}:{:0>2}:{:0>2}".format(self.now, *self.sec_to_min(self.progress["value"])))
                        sys.stdout.flush()
                    except:
                        print("播放列表为空")

                    time.sleep(2)


def md5Sum(spath):
    with open(spath, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash


def initData():
    localTable = """
        create table "localMusic" ("musicName" TEXT ,"localPath" TEXT ,"md5" TEXT,"tag" TEXT ,PRIMARY KEY ("localPath"))
        """
    netTable = """
        create table "netMusic" ("songs_name" TEXT ,"songs_id" INTEGER ,"pic_url" TEXT,"songs_audio" TEXT ,"songs_page" TEXT ,"netPath" TEXT ,"md5" TEXT ,"tag" TEXT,PRIMARY KEY ("netPath"))
        """
    cn = sqlite3.connect("musicDataBases.db", timeout=10)
    cur = cn.cursor()
    try:
        cur.execute(netTable)
        cur.execute(localTable)
        cn.commit()
    except:
        pass
    os.mkdir("local")
    os.mkdir("net")


def walkPath(FilePath):
    for root, dirnames, filenames in os.walk(FilePath):
        for filename in filenames:
            print(root, filename)


root = Tk()
app = SampleApp(root)
root.mainloop()
