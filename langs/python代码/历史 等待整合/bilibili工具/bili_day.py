# http://www.bilibili.com/video/bagumi_offical_1.html#!page=1
###############################################################################
# 类化  收集数据库 使用sqlite3
# 名称 up 时间  图片
# 插入数据库
#
#
#
###############################################################################
from bs4 import BeautifulSoup
import re
import sqlite3
import os
import j
import http.cookiejar
import requests
import datetime

# 全局定义区


####################################
import threading
import time


class collect_data:
    def __init__(self):
        self.src = ""
        self.videoLink = ""
        self.title = ""
        self.v_desc = ""
        self.gk = ""
        self.dm = ""
        self.sc = ""
        self.pic_save = ""
        self.mode = 10
        self.tableName = ""

        self.author_link = ""
        self.author_name = ""
        self.v_date = ""

        self.list = []
        self.thName = ""

        self.headers = {'Accept-Language': 'zh-CN,zh;q=0.8', 'Cache-Control': 'max-age=0',
                        'Accept-Encoding': 'gzip, deflate, sdch',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                        'Upgrade-Insecure-Requests': '1', 'Host': 'i2.hdslb.com', 'Connection': 'keep-alive'}

        self.cookies = self.loadCookie("cookies.txt")

        self.getPageHEaders = {'Upgrade-Insecure-Requests': '1',
                               'Connection': 'keep-alive', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept': '*/*',
                               'Accept-Encoding': 'gzip, deflate, sdch',
                               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
                               'Host': 'www.bilibili.com'}

    def loadCookie(self, path):
        cookie_jar = http.cookiejar.MozillaCookieJar()
        cookies = open(path).read()
        for cookie in j.loads(cookies):
            # print(cookie['name'])
            cookie_jar.set_cookie(
                http.cookiejar.Cookie(version=0, name=cookie['name'], value=cookie['value'], port=None,
                                      port_specified=False,
                                      domain=cookie['domain'], domain_specified=False, domain_initial_dot=False,
                                      path=cookie['path'], path_specified=True, secure=cookie['secure'],
                                      expires=None,
                                      discard=True, comment=None, comment_url=None, rest={'HttpOnly': None},
                                      rfc2109=False))
        return cookie_jar

        #########################
        #  init pic path
        #
        #
        ########################

    def dataBaseCheck(self, dbname, create_table, tableName):
        # 默认db库是放在脚本运行的目录
        self.tableName = tableName
        if not os.path.exists("bilibili_data/" + tableName):
            os.makedirs("bilibili_data/" + tableName)
            print("{} 图片存放目录已经创建".format("bilibili_data/" + tableName))

        self.cn = sqlite3.connect(dbname)
        self.cur = self.cn.cursor()
        try:
            self.cur.execute(create_table)
        except sqlite3.Error as e:
            print(e)

    def main(self, page, dbname, create_table, tableName, url, thName):
        self.thName = thName
        self.dataBaseCheck(dbname, create_table, tableName)
        dataTime = datetime.datetime.now().strftime('%Y-%m-%d')

        while 1:
            while 1:
                print("{}  解析第{}个  ".format(self.thName, page) + url.format(page, dataTime))
                try:
                    r = requests.get(url.format(page, dataTime), headers=self.getPageHEaders, cookies=self.cookies)
                except:
                    print("解析请求错误")
                    pass
                if r.status_code == 200:
                    data = r.content.decode()
                    break
            self.htmlAnalysis(data)
            page -= 1
            if page == 0:
                break

    def htmlAnalysis(self, data):
        many = []  # 下次插入会清空列表
        start = time.clock()
        soup = BeautifulSoup(data, "html.parser")
        liData = soup.find('ul', class_='vd-list l2')
        if not liData:
            liData = soup.find('ul', class_='vd-list l1')

        i = 0

        for s in liData.find_all('li'):
            linkInfo = s.find('a', class_='preview')
            try:
                self.videoLink = re.findall('href="(.*?)"', str(linkInfo))[0]
            except:
                print("数组越界 video {}".format(self.videoLink))
            try:
                self.title = re.findall('title="(.*?)"', str(linkInfo))[0]  # 当正则遇上转义字符 不会看看怎么抛出啊 修改就好了
            except:
                self.title = re.findall('title=\'(.*?)\'', str(linkInfo))[0]
                print("数组越界 修正为 title {}".format(self.title))

            self.src = re.findall('src="(.*?)"', str(linkInfo))[0].replace("_320x200.jpg", "")
            if self.src == "http://static.hdslb.com/images/transparent.gif":
                try:
                    self.src = re.findall('data-img="(.*?)"', str(linkInfo))[0].replace("_320x200.jpg", "")
                except:
                    print("错误 默认图片")
                    self.src == "http://static.hdslb.com/images/transparent.gif"
            # print(self.videoLink, self.title, self.src)

            # 详细信息
            self.v_desc = s.find('div', class_='v-desc').get_text()
            # 匹配后分别是 观看数 弹幕 收藏
            # <span class="v-info-i gk"><i class="b-icon b-icon-v-play" title="观看"></i><span number="2">2</span></span>
            # <span class="v-info-i dm"><i class="b-icon b-icon-v-dm" title="弹幕"></i><span number="0">0</span></span>
            # <span class="v-info-i sc"><i class="b-icon b-icon-v-fav" title="收藏"></i><span number="0">0</span></span>

            try:
                self.gk, self.dm, self.sc = re.findall('<span number="\d+">(\d+)</span>', str(s))
            except:
                self.gk == 0

            e = "0"
            try:
                self.pic_save = re.findall('\d+', self.videoLink)[0] + ".jpg"
                # authorInfo = s.find('div', class_='up-info')
                self.author_link, self.author_name, self.v_date = re.findall(
                    '<a class="[^"]+" href="([^"]+)" target="_blank" title="([^"]+)">[^<]+</a><span class="v-date" title="日期">([^<]+)</span>',
                    str(s))[0]  # 解包通过去掉外面这层包裹 妈的 [^>]+> 少用  遇到空白就不知怎么处理了

            except:
                # print(self.author_link, self.author_name, self.v_date)
                # if not self.author_link:
                #     self.author_link = "error"
                #     print("author_link not found")
                # if not self.author_name:
                #     self.author_name = "error"
                #     print(" author_name not found")
                # if not self.v_date:
                #     self.v_date = "error"
                #     print("v_date  not found")
                try:
                    self.author_link, self.author_name, self.v_date = re.findall(
                    '<a class="[^"]+" href="(.*?)" target="_blank" title="(.*?)"></a><span class="v-date" title="日期">([^<]+)</span>',
                    str(s))[0]  # 解包通过去掉外面这层包裹 妈的 [^>]+> 少用  遇到空白就不知怎么处理了
                except:
                    print("抛出异常有可能是网页问题 详细情况请看error.txt 文件")
                    e = "1"



                # #########################################################
            # # 网络请求下载
            # # self.src
            # # 不下载图片了
            # #########################################################
            # host = self.src.split("/")[2]
            # self.headers.update({"Host": host})
            # r = requests.get(self.src, headers=self.headers, cookies=self.cookies, stream=True)
            # r.encoding = 'UTF-8'
            # f = open("bilibili_data/" + self.tableName + "/" + self.pic_save, 'wb')
            # f.write(r.content)
            # f.close()

            if e == "1":
                f1 = open("day_error.txt", "a", encoding="UTF-8")
                f1.write("{} {} {}".format(self.author_link, self.author_name, self.v_date) + "\n")
                f1.write(str(s) + "\n")
                f1.close()

                    # 对进入数据库的关键字进行转义
            # 这里是for 循环
            try:
                # print("INSERT INTO `" + self.tableName + "`  VALUES (?,?,?,?,?,?,?,?,?,?,?)", many)
                # self.list 是前一次的数据
                # 查询用之前的列表把重复的列表去掉


                self.cur.execute("INSERT INTO " + self.tableName + "  VALUES (?,?,?,?,?,?,?,?,?,?,?)", (
                    "http://www.bilibili.com" + self.videoLink, self.pic_save, self.title, self.src,
                    self.v_desc,
                    self.gk, self.dm, self.sc, self.author_name, self.author_link, self.v_date))

                print("{}新数据插入成功".format(self.tableName))


            except sqlite3.Error as e:
                pass

            self.cn.commit()

        # if self.mode == 10:
        #         try:
        #             self.cur.execute("INSERT INTO bagumi_offical VALUES {}".format(value))
        #         except sqlite3.Error as e:
        #             print(e)
        #         self.cn.commit()
        #     else:
        #         if i == 0:
        #             self.sql = value
        #         else:
        #             self.sql = self.sql + "," + value
        #
        #     i += 1
        # # for 循环结束
        # if self.mode != 10:
        #     try:
        #         self.cur.execute("INSERT INTO bagumi_offical VALUES {}".format(self.sql))
        #         print( "INSERT INTO bagumi_offical VALUES {}".format(self.sql))
        #     except sqlite3.Error as e:
        #         print(e)
        #     self.cn.commit()

        end = time.clock()
        print("解析耗时 " + str(end - start))




        # input()


class Th(threading.Thread):
    def __init__(self, thread_name, page, create_table, fileName, url):
        threading.Thread.__init__(self)
        self.setName(thread_name)
        self.page = page
        self.create_table = create_table
        self.fileName = fileName
        self.url = url

    def run(self):
        print('This is thread ' + self.getName())

        s = collect_data()

        s.main(self.page, "bilibili.db", self.create_table, self.fileName, self.url, self.getName())

        print(self.getName() + "is over")


####################################
if __name__ == '__main__':
    create_table = """create table "{}" (
"video_link"  text,
"av_number"  text not null,
"video_title"  text,
"video_pic_src"  text,
"video_desc"  text,
"video_gk"  integer,
"video_sc"  integer,
"video_dm"  integer,
"video_author_name"  text,
"video_author_link"  text,
"video_date"  text,
primary key ("av_number" asc)
);

"""

    ##############################################
    # 传入 连载 http://www.bilibili.com/list/default-33-3-2016-05-16~2016-05-23.html
    # 文件夹名字 filename
    # 建表语句
    # 表名 bagumi_offical
    # 完结动画 http://www.bilibili.com/list/default-32-3-2016-05-16~2016-05-23.html
    #
    #
    #############################################
    start = time.clock()
    bili = [["官方延伸", "http://www.bilibili.com/list/default-152-{}-2016-05-15~{}.html", 1150],
            ["资讯", "http://www.bilibili.com/list/default-51-{}-2016-05-16~{}.html", 270],
            ["完结动画", "http://www.bilibili.com/list/default-32-{}-2016-05-16~{}.html", 437],
            ["连载动画", "http://www.bilibili.com/list/default-33-{}-2016-05-16~{}.html", 969],
            ["MAD", "http://www.bilibili.com/list/default-24-{}-2016-05-16~{}.html", 5711],
            ["MMD", "http://www.bilibili.com/list/default-25-{}-2016-05-16~{}.html", 5124],
            ["手书", "http://www.bilibili.com/list/default-47-{}-2016-05-16~{}.html", 1016],
            ["综合", "http://www.bilibili.com/list/default-27-{}-2016-05-16~{}.html", 4429],
            ["美妆健身", "http://www.bilibili.com/list/default-157-{}-2016-05-16~{}.html", 733],
            ["服饰", "http://www.bilibili.com/list/default-158-{}-2016-05-16~{}.html", 105],
            ["时尚资讯", "http://www.bilibili.com/list/default-159-{}-2016-05-16~{}.html", 128],
            ["连载剧集", "http://www.bilibili.com/list/default-15-{}-2016-05-16~{}.html", 1145],
            ["完结剧集", "http://www.bilibili.com/list/default-34-{}-2016-05-16~{}.html", 421],
            ["特摄_布袋", "http://www.bilibili.com/list/default-86-{}-2016-05-16~{}.html", 165],
            ["电视剧相关", "http://www.bilibili.com/list/default-128-{}-2016-05-16~{}.html", 6011],
            ["电影相关", "http://www.bilibili.com/list/default-82-{}-2016-05-16~{}.html", 2672],
            ["短片", "http://www.bilibili.com/list/default-85-{}-2016-05-16~{}.html", 567],
            ["欧美电影", "http://www.bilibili.com/list/default-145-{}-2016-05-16~{}.html", 642],
            ["日本电影", "http://www.bilibili.com/list/default-146-{}-2016-05-16~{}.html", 142],
            ["国产电影", "http://www.bilibili.com/list/default-147-{}-2016-05-16~{}.html", 207],
            ["其他国家", "http://www.bilibili.com/list/default-83-{}-2016-05-16~{}.html", 490],
            ["鬼畜调教", "http://www.bilibili.com/list/default-22-{}-2016-05-16~{}.html", 1323],
            ["音MAD", "http://www.bilibili.com/list/default-26-{}-2016-05-16~{}.html", 810],
            ["人力VOCALOID", "http://www.bilibili.com/list/default-126-{}-2016-05-16~{}.html", 330],
            ["教程演示", "http://www.bilibili.com/list/default-127-{}-2016-05-16~{}.html", 7],
            ["搞笑", "http://www.bilibili.com/list/default-138-{}-2016-05-16~{}.html", 2222],
            ["生活", "http://www.bilibili.com/list/default-21-{}-2016-05-16~{}.html", 12245],
            ["动物圈", "http://www.bilibili.com/list/default-75-{}-2016-05-16~{}.html", 1252],
            ["美食圈", "http://www.bilibili.com/list/default-76-{}-2016-05-16~{}.html", 2027],
            ["综艺", "http://www.bilibili.com/list/default-71-{}-2016-05-16~{}.html", 3877],
            ["娱乐圈", "http://www.bilibili.com/list/default-137-{}-2016-05-16~{}.html", 4074],
            ["Korea相关", "http://www.bilibili.com/list/default-131-{}-2016-05-16~{}.html", 4879],
            ["机械", "http://www.bilibili.com/list/default-98-{}-2016-05-16~{}.html", 927],
            ["数码", "http://www.bilibili.com/list/default-95-{}-2016-05-16~{}.html", 1444],
            ["星海", "http://www.bilibili.com/list/default-96-{}-2016-05-16~{}.html", 898],
            ["翻唱", "http://www.bilibili.com/list/default-31-{}-2016-05-16~{}.html", 6443],
            ["VOCALOID_UTAU", "http://www.bilibili.com/list/default-30-{}-2016-05-16~{}.html", 3640],
            ["演奏", "http://www.bilibili.com/list/default-59-{}-2016-05-16~{}.html", 2079],
            ["三次元音乐", "http://www.bilibili.com/list/default-29-{}-2016-05-16~{}.html", 4575],
            ["同人音乐", "http://www.bilibili.com/list/default-28-{}-2016-05-16~{}.html", 3980],
            ["OP/ED/OST", "http://www.bilibili.com/list/default-54-{}-2016-05-16~{}.html", 633],
            ["音乐选集", "http://www.bilibili.com/list/default-130-{}-2016-05-16~{}.html", 2212],
            ["宅舞", "http://www.bilibili.com/list/default-20-{}-2016-05-16~{}.html", 2374],
            ["三次元舞蹈", "http://www.bilibili.com/list/default-154-{}-2016-05-16~{}.html", 692],
            ["舞蹈教程", "http://www.bilibili.com/list/default-156-{}-2016-05-16~{}.html", 135],
            ["单机联机", "http://www.bilibili.com/list/default-17-{}-2016-05-16~{}.html", 35581],
            ["网游_电竞", "http://www.bilibili.com/list/default-65-{}-2016-05-16~{}.html", 14138],
            ["音游", "http://www.bilibili.com/list/default-136-{}-2016-05-16~{}.html", 1522],
            ["Mugen", "http://www.bilibili.com/list/default-19-{}-2016-05-16~{}.html", 933],
            ["GMV", "http://www.bilibili.com/list/default-121-{}-2016-05-16~{}.html", 659],
            ["纪录片", "http://www.bilibili.com/list/default-37-{}-2016-05-16~{}.html", 804],
            ["趣味科普人文", "http://www.bilibili.com/list/default-124-{}-2016-05-16~{}.html", 1742],
            ["野生技术协会", "http://www.bilibili.com/list/default-122-{}-2016-05-16~{}.html", 2053],
            ["演讲_公开课", "http://www.bilibili.com/list/default-39-{}-2016-05-16~{}.html", 493],
            ["国产动画", "http://www.bilibili.com/list/default-153-{}-2016-05-16~{}.html", 120]
            ]
    ## 55 个对象

    threadNum = len(bili)
    i = 0  # i 用来计算执行的线程数
    while (i < threadNum):
        if i < threadNum:
            thread1 = Th("线程一 ", 10, create_table.format(bili[i][0]), bili[i][0], bili[i][1])
            thread1.start()
            i += 1
        if i < threadNum:
            thread2 = Th("线程二 ", 10, create_table.format(bili[i][0]), bili[i][0], bili[i][1])
            thread2.start()
            i += 1
        if i < threadNum:
            thread3 = Th("线程三 ", 10, create_table.format(bili[i][0]), bili[i][0], bili[i][1])
            thread3.start()
            i += 1
        if i < threadNum:
            thread4 = Th("线程四 ", 10, create_table.format(bili[i][0]), bili[i][0], bili[i][1])
            thread4.start()
            i += 1
        if i < threadNum:
            thread5 = Th("线程五 ", 10, create_table.format(bili[i][0]), bili[i][0], bili[i][1])
            thread5.start()
            i += 1
        # 进程等待
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()
        progress = "当前进度 {}%".format(i / threadNum)
        f = open("day_progress.txt", "a", encoding="UTF-8")
        f.write(progress + "\n")
        f.close()
        print(progress)

    end = time.clock()
    all_time = "全部爬完耗时 " + str(end - start)
    print()
    f = open("day_progress.txt", "a", encoding="UTF-8")
    f.write(all_time + "\n")
    f.close()
    print("完成退出中.....")

