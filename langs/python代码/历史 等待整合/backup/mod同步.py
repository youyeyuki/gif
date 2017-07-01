import hashlib
import json
import os

import requests
import sqlite3

# modPath = r"/.minecraft/versions/1.7.10/mods"
modPath = r".minecraft/versions/1.7.10/mods"
addPath = r".minecraft/versions/1.7.10/"

IP = "http://120.77.174.203/"

local_sql = """CREATE TABLE "local" (
"fileName"  TEXT,
"localMd5"  TEXT
);
"""
update_sql = """CREATE TABLE "remote" (
"fileName"  TEXT,
"remoteMd5"  TEXT
);
"""
remove_sql = """CREATE TABLE "remove" (
"fileName"  TEXT,
"removeMd5"  TEXT
);
"""

s = """
#######################################
# 程序 某teaCraft mods自动更新程序
# 版本 ver 1.0
# 作者 莜叶
# 日期 2017、1、05
########################################
"""


def md5Sum(spath):
    with open(spath, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash


def main():
    if os.path.exists('update.db'):
        os.remove("update.db")

    con = sqlite3.connect('update.db')
    cur = con.cursor()
    cur.execute(local_sql)
    cur.execute(remove_sql)
    cur.execute(update_sql)

    local_files = []
    for root, dirnames, filenames in os.walk(modPath):
        for filename in filenames:
            info = os.path.join(root, filename)
            local_md5 = md5Sum(info)
            local_files.append((info, local_md5))

    cur.executemany("INSERT INTO  local ('fileName','localMd5') VALUES (?,?)", local_files)
    con.commit()
    # 删除查询
    WriteToDB(con, cur, IP + "mc/remove.php", "remove")
    # 升级查询
    WriteToDB(con, cur, IP + "mc/update.php", "remote")

    # 删除本地文件
    del_sql = """select local.fileName from local WHERE   EXISTS(select removeMd5 from remove where removeMd5 = localMd5);"""
    cur.execute(del_sql)
    data = cur.fetchall()
    for i in data:
        os.remove(i[0])
        print("{} 被移除".format(i[0]))

    # 开始更新文件
    cur.execute(
        """SELECT remote.fileName FROM remote WHERE  NOT EXISTS(SELECT localMd5 FROM local WHERE remoteMd5 = localMd5);""")
    data = cur.fetchall()
    for i in data:
        p, f = os.path.split(addPath + i[0])
        if not os.path.exists(p):
            os.makedirs(p)
        print("{} 正在下载中....".format(i[0]))
        r = requests.get(IP + "mc/" + i[0], stream=True)
        r.encoding = 'utf-8'
        f = open(addPath + i[0], mode='wb+')
        f.write(r.content)
        f.close()
        print("{} 添加成功".format(i[0]))


def WriteToDB(con, cur, url, table):
    data = requests.get(url)
    jdata = json.loads(data.text)
    files = []
    if 0 == len(jdata):
        print('没有移除的文件列表')
    else:
        for num, item in enumerate(jdata):
            files.append((jdata[num]['path'], jdata[num]['md5']))

        cur.executemany("INSERT INTO  {} ('fileName','{}') VALUES (?,?)".format(table, table + "Md5"), files)
        con.commit()


if __name__ == '__main__':
    print(s)

    main()
    print("全部更新完成")
    os.system('pause')
