################
#
# 修改minecraft 音乐
################
import j
import re
import os
class traversalDirs():
    def __init__(self):
        self.tmp = ""
        self.initclass()
    def initclass(self):
        try:
            os.makedirs("替换音乐存放目录")
        except:
            print("")


class modify():
    def __init__(self):
        self.s = ""




# s = traversalDirs()
f = open("1.7.10.json", encoding="UTF-8")
j = j.load(f, encoding="UTF-8")
for x in iter(j["objects"]):
    if re.search("minecraft/sounds/ambient/weather/*",x):
            print(x , "  ",j["objects"][x])
print(j["objects"]["minecraft/sounds/records/blocks.ogg"]["hash"])
f.close()
#天气 minecraft/sounds/ambient/weather/
# 液体声音 minecraft/sounds/liquid
# 行走 minecraft/sounds/step
# 怪物 minecraft/sounds/mob
# minecraft/sounds/random 物品声音
# minecraft/sounds/music/game/* 游戏音效
# def walk_dir(dirname):
#     for root, dirs, files in os.walk(dirname):
#         print(dirs)
#         for f in files:
#             yield os.path.join(root, f)

# for root, dirnames, filenames in os.walk("D:\\py\\python3.5\\bilibili工具"):
#
#     for dirname in dirnames:
#         print(root,dirname)
#
#     for filename in filenames:
#         print(root,filename)
#     print("======================")



# for d in os.listdir("D:\\py\\python3.5\\bilibili工具"):
#     print(d)