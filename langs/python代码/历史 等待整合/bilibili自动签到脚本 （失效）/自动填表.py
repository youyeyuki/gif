import calendar
import sys

class count:
    def __init__(self):
        self.time = 0
        self.flag = 0
    def calc(self,year, month, days):

        weekday = calendar.weekday(year, month, days)
        if weekday == 0:
            print("{} {} {:0>2} 星期一 10:30 - 12:30 2小时 ".format(year, month, days))
            self.time += 2
    
        elif weekday == 2:
            print("{} {} {:0>2} 星期三 18:30 - 21:30"
                  " 3小时 ".format(year, month, days))
            self.time += 3
        elif weekday == 4:
            print("{} {} {:0>2} 星期五 14:00 - 15:00 1小时 ".format(year, month, days))
            self.time += 1
        if self.time >= 20:
            if self.flag == 0:
                print("现在的工作时间等于或超过最大时间 计算是{}".format(self.time))
                self.flag = 1



def list_to_num(ls):
    for index, item in enumerate(ls):
        ls[index] = int(item)


if __name__ == '__main__':

    print("输入参数为 year month 要排除的日期  例如: python fillTable.py 2016 4     2,3,4,5  # 排除2345天")
    year = sys.argv[1]
    month = sys.argv[2]
    outDate = sys.argv[3]
    outDate = outDate.split(",")
    list_to_num(outDate)  # 直接改变 无需复制赋值
    ye = count()
    print("现在填的表是 {}年 {}月份 的表格  ".format(year,month))
    listDate = calendar.monthcalendar(int(year), int(month))
    for i in sum(listDate, []):
        if i != 0:
            if i not in outDate:
                ye.calc(int(year), int(month), i)
