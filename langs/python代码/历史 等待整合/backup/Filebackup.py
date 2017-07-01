import os
import hashlib
import shutil
import sqlite3
import time
import threading


# 文件处理
def createPath(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
            print("{} 创建成功".format(path))
        except:
            print("文件创建失败 请检查权限")


def delFile(sourceFile):
    if os.path.exists(sourceFile):
        try:
            os.remove(sourceFile)
            print("{} 文件删除成功".format(sourceFile))
        except:
            print("删除文件失败")
    else:
        print("{} 不存在".format(sourceFile))


def delDir(sourceFile):
    if os.path.exists(sourceFile):
        try:
            os.rmdir(sourceFile)
            print("{}  文件夹成功删除".format(sourceFile))
        except:
            print("删除文件夹失败")
    else:
        print("{} 不存在".format(sourceFile))


def cpoyFile(source, target):
    try:
        if os.path.isdir(source):
            pass
        else:
            shutil.copyfile(source, target)  # 只能是文件
            print("复制文件{} 成功".format(source))
    except:
        print("复制文件{} 失败".format(source))


def createFIle(path):
    if not os.path.exists(path):
        try:
            os.mknod("path")
            print("{} 成功创建", path)
        except:
            print("{} 创建失败", path)


def md5Sum(spath):
    with open(spath, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash
        # 创建文件目录


# 数据库 处理类



def insert_sourcesdir(dbPath, data):
    cn = sqlite3.connect(dbPath)
    cur = cn.cursor()
    sql = "INSERT INTO 'sourcedir'  VALUES ('{}')".format(data)
    print(sql)
    cur.execute(sql)
    cn.commit()
    cn.close()


def insert_backupdir(dbPath, data):
    cn = sqlite3.connect(dbPath)
    cur = cn.cursor()
    sql = "INSERT INTO 'backupdir' VALUES ('{}')".format(data)
    print(sql)
    cur.execute(sql)
    cn.commit()
    cn.close()


def insert_backupInfo(dbPath, filename, md5):
    cn = sqlite3.connect(dbPath)
    cur = cn.cursor()
    sql = "INSERT INTO 'backupInfo' VALUES ('{}','{}')".format(filename, md5)
    print(sql)
    cur.execute(sql)
    cn.commit()
    cn.close()


def insert_sourcesInfo(dbPath, filename, md5):
    cn = sqlite3.connect(dbPath)
    cur = cn.cursor()
    sql = "INSERT INTO 'sourceInfo' VALUES ('{}','{}')".format(filename, md5)
    print(sql)
    cur.execute(sql)
    cn.commit()
    cn.close()


# 读取并写入数据库
def getList(dbPath, FilePath):
    print("==========")
    for root, dirnames, filenames in os.walk(FilePath):
        for dirname in dirnames:
            tmp = os.path.join(root, dirname)
            insert_sourcesdir(dbPath, tmp.replace(FilePath, ''))
        for filename in filenames:
            tmp = os.path.join(root, filename)
            insert_sourcesInfo(dbPath, tmp.replace(FilePath, ''), md5Sum(tmp))


def getListbackup(dbPath, FilePath):
    print("back")
    for root, dirnames, filenames in os.walk(FilePath):
        for dirname in dirnames:
            tmp = os.path.join(root, dirname)
            insert_backupdir(dbPath, tmp.replace(FilePath, ''))
        for filename in filenames:
            tmp = os.path.join(root, filename)
            insert_backupInfo(dbPath, tmp.replace(FilePath, ''), md5Sum(tmp))


def updateSource(dbPath, FilePath):
    cn = sqlite3.connect(dbPath)
    cur = cn.cursor()
    cur.execute("DELETE FROM {}".format("sourcedir"))
    cur.execute("DELETE FROM {}".format("sourceInfo"))
    cn.commit()
    cn.close()
    getList(dbPath, FilePath)


def updateBackup(dbPath, FilePath):
    cn = sqlite3.connect(dbPath)
    cur = cn.cursor()
    cur.execute("DELETE FROM {}".format("backupdir"))
    cur.execute("DELETE FROM {}".format("backupInfo"))
    cn.commit()
    cn.close()
    getListbackup(dbPath, FilePath)


def backupAndRecovery(sdir, bdir, sinfo, binfo, SourcePath, BackupPath):
    新增加文件夹 = """SELECT {} FROM {} EXCEPT SELECT {} FROM {}""".format(sdir, sdir, bdir, bdir)

    删除的文件 = """SELECT filename FROM {} EXCEPT SELECT filename FROM {}""".format(binfo, sinfo)

    新加文件 = """SELECT filename FROM {} EXCEPT SELECT filename FROM {}""".format(sinfo, binfo)

    删除文件夹 = """SELECT {} FROM {} EXCEPT SELECT {} FROM {}""".format(bdir, bdir, sdir, sdir)

    # source to file
    md5验证替换 = """SELECT filename FROM {} WHERE EXISTS
(SELECT filename FROM {} WHERE {}.filename={}.filename)
AND NOT EXISTS(SELECT md5 FROM {} WHERE {}.md5={}.md5)
""".format(sinfo, binfo, sinfo, binfo, binfo, sinfo, binfo)

    print(新增加文件夹)
    cn = sqlite3.connect("j:\\DB\\test.db")
    cur = cn.cursor()
    cur.execute(新增加文件夹)
    r = cur.fetchall()
    if len(r) > 0:
        for i in range(len(r)):
            createPath(BackupPath + str(r[i][0]))

    print("==============")
    print(删除的文件)
    cur.execute(删除的文件)
    r = cur.fetchall()
    if len(r) > 0:
        for i in range(len(r)):
            delFile(BackupPath + str(r[i][0]))
    print("==============")

    print(新加文件)
    cur.execute(新加文件)
    r = cur.fetchall()
    if len(r) > 0:
        for i in range(len(r)):
            cpoyFile(SourcePath + str(r[i][0]), BackupPath + str(r[i][0]))
    print("==============")
    print(删除文件夹)
    cur.execute(删除文件夹)
    r = cur.fetchall()
    if len(r) > 0:
        for i in range(len(r)):
            delDir(BackupPath + str(r[i][0]))
    print("==============")
    print(md5验证替换)
    cur.execute(md5验证替换)
    r = cur.fetchall()
    if len(r) > 0:
        for i in range(len(r)):
            cpoyFile(SourcePath + str(r[i][0]), BackupPath + str(r[i][0]))


def emptyDB(dbPath):
    cn = sqlite3.connect(dbPath)
    cur = cn.cursor()
    t = {'sourcedir', 'sourceInfo', 'backupInfo', 'backupdir'}
    for i in t:
        cur.execute("DELETE FROM {}".format(i))
    cn.commit()


def main():
    get = input()
    if get == "1":
        threading.Thread(target=getList,args=(dbPath, FilePath)).start()
        threading.Thread(target=getListbackup,args=(dbPath, BackupPath)).start()
    elif get == "2":
        updateSource(dbPath, FilePath)
        # 这里是 源文件 备份到 备份文件      参数逆转为恢复文件到源文件
        # 备份设置"sourcedir", "backupdir", "sourceInfo", "backupInfo", FilePath, BackupPath)
        backupAndRecovery("sourcedir", "backupdir", "sourceInfo", "backupInfo", FilePath, BackupPath)

    elif get == "3":
        updateSource(dbPath, FilePath)
        # 恢复
        backupAndRecovery("backupdir", "sourcedir", "backupInfo", "sourceInfo", BackupPath, FilePath)
    elif get == "5":
        emptyDB(dbPath)



if __name__ == '__main__':
    # 要进行对比的两个文件名称 注意
    FilePath = "J:\\File"
    BackupPath = "J:\\Backup"
    dbPath = "j:\\DB\\test.db"

    createPath(BackupPath)
    createFIle(dbPath)
    message = """
    1.初始化备份
    2.文件增量文件
    3.文件恢复到上次状态
    """
    print(message)
    main()
