import os
import shutil
import j
if not os.path.exists("替换音乐存放目录"):
    os.mkdir("替换音乐存放目录")

f = open("修改音乐清单.txt", encoding="UTF-8")
ls = f.read().split("\n")

jf = open("1.7.10.json", encoding="UTF-8")
j = j.load(jf, encoding="UTF-8")

for i in ls:
    x, y = i.split("|")
    if  y.strip() != "替换音乐存放目录/":
        dst = j["objects"][x.strip()]["hash"]
        dstfile = ".minecraft/assets/objects/"+dst[:2]+"/"+dst
        try:
            print(y.strip(),dstfile)
            shutil.copy(y.strip(),dstfile)
        except:
            print("错误检查 文件输入输出目录 和 目标文件 还有1.7.10 才能用 ogg 格式音频")

f.close()
jf.close()
