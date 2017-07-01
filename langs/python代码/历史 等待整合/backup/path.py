import os

import sys


# python文件遍历是是根目录遍历 到文件夹 文件夹的子目录等遍历方法 dirname 只是列出文件名  主要是filename
def writeBaseInfo(root, filename):
    f = open(os.path.join(root, "base.ini"), mode='a',encoding='utf-8')
    f.write(filename+"\n")
    f.close()


def writeSelfData(filepath):
    f = open(filepath, mode='a',encoding='utf-8')
    f.write(DATA)
    f.close()
    print("{} 完成".format(filepath))


def walk(filePath):
    for root, dirnames, filenames in os.walk(filePath):

        # for dirname in dirnames:
        #     print(root, dirname)

        for filename in filenames:
            try:     
                writeBaseInfo(root,filename)
                writeSelfData(os.path.join(root, filename))
            except:
                print("中文字符out")
                fw = open('error.txt',"a",encoding='utf-8')
                fw.write(os.path.join(root, filename)+"\n")
                fw.close()
        print("======================")


def main():
    print("输入文件的目录")
    path = input()
    print(path)
    input("确认目录")

    if os.path.exists(path):
        print("cc")
        walk(path)
        print("全部完成")
    else:
        print("目录不存在")


if __name__ == '__main__':
    DATA = "\ u t ye login glig ----"
    while 1:
        main()

