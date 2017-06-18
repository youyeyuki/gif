import hashlib
import tkinter as tk
import threading
import time

import sqlite3
import ttk
import os


class soong():
    def __init__(self):
        self.songs_name = ""
        self.song_id = ""
        self.pic_url = ""
        self.songs_audio = ""
        self.songs_page = ""
        self.netPath = ""
        self.md5 = ""

        self.musicName = ""
        self.localPath = ""

        self.cn = sqlite3.connect("musicDataBases.db")
        self.cur = self.cn.cursor()
        self.list=[]

    def md5Sum(self, spath):
        with open(spath, 'rb') as f:
            md5obj = hashlib.md5()
            md5obj.update(f.read())
            hash = md5obj.hexdigest()
            return hash

    def walkPath(self, FilePath):
        for root, dirnames, filenames in os.walk(FilePath):
            for filename in filenames:
                path = os.path.join(root, filename)
                self.musicName = filename
                self.localPath = path
                self.md5 = self.md5Sum(path)

                self.cur.execute("INSERT INTO localMusic ('musicName', 'localPath', 'md5') VALUES (?,?,?)",
                                 (self.musicName, self.localPath, self.md5))
                self.cn.commit()
    def fetchLocalData(self):


        print(self.list)




s = soong()
s.fetchLocalData()

