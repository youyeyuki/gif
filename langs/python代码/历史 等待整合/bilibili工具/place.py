from openpyxl import Workbook
from openpyxl import load_workbook
import sqlite3
import random

import time


def random_num():
    return random.randint(1, 9)


start = time.clock()
one = "自行车"

two = "摩托"

three = "小客车"

four = "大客车"
tb = """CREATE TABLE "sdata" (
"chepa"  TEXT,
"time"  TEXT,
"address"  TEXT
);

"""
time = ""
车牌 = ""
address = ""
cn = sqlite3.connect("dsxjm.db")
cur = cn.cursor()

# cur.execute(tb)
# cn.commit()

wb = load_workbook(r"C:\Users\wings\Desktop\20140901.xlsx")
sheet = wb.get_sheet_by_name('Sheet1')
ws_rows_len = len(sheet.rows)  # 行数
data = []
num = 1
for i in range(2, ws_rows_len):
    A = "A" + str(i)
    B = "B" + str(i)
    C = "C" + str(i)

    if sheet[B].value == "无车牌" or sheet[B].value == "无牌":
        车牌 = one
        time = sheet[A].value
        address = sheet[C].value

    else:
        ttt = random_num()
        if ttt == 1:
            车牌 = one
            time = sheet[A].value
            address = sheet[C].value
        elif 1 < ttt <= 4:
            车牌 = two
            time = sheet[A].value
            address = sheet[C].value
        elif 5 < ttt <= 7:
            车牌 = " {} 小客车".format(sheet[B].value)
            time = sheet[A].value
            address = sheet[C].value
        elif 8 <= ttt <= 9:
            车牌 = "{} 大客车".format(sheet[B].value)
            time = sheet[A].value
            address = sheet[C].value
    #print((车牌, time, address))

    if num != 1000:

        num += 1
        if time != "":
            data.append((车牌, time, address))

    else:

        cur.executemany("INSERT INTO sdata VALUES (?,?,?) ", data)
        #print(data)
        print("插入数据 100行完成")
        cn.commit()
        num = 0
        data.clear()
end = time.clock()
print("read: %f s" % (end - start))
