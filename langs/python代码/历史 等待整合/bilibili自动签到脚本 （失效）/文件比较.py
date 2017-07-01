import hashlib
import requests
import os
import sqlite3


def md5Sum(spath):
    with open(spath, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash
ls = []
path = os.getcwd()

head_data = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
#
# for i in range(0, 15000):
#     r = requests.get("http://mooc1-2.chaoxing.com/img/code", headers=head_data, stream=True)
#     r.encoding = 'UTF-8'
#     f = open(path + "\\pic_collection\\" + str(i) + ".jpg", 'wb')
#     print("下载第{}个样本".format(i))
#     f.write(r.content)
#     f.close()
insert=""
for i in range(0,15000):
        if i == 0:
            insert += "('{}','{}')".format(str(i), md5Sum("D:\\py\\python3.5\\bilibili自动签到脚本\\pic_collection\\"+str(i)+".jpg"))
        else:
            insert += ",('{}','{}')".format(str(i), md5Sum("D:\\py\\python3.5\\bilibili自动签到脚本\\pic_collection\\"+str(i)+".jpg"))
        if i %100 == 0:
            print(i)



cn = sqlite3.connect("D:\\py\\python3.5\\bilibili自动签到脚本\\cp.db")
cur = cn.cursor()
sql = "INSERT INTO 'cp' VALUES "+insert
print(sql)
cur.execute(sql)
cn.commit()
cn.close()
# os.system("shutdown -s -t 60")