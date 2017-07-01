from __future__ import print_function
from bs4 import BeautifulSoup
import re
import requests
import mysql.connector
from mysql.connector import errorcode


class wuyun:
    def __init__(self):
        # 初始化头 request_header
        self.__request_init()
        self.parseCookies = ''
        self.condb()

    def __request_init(self):
        self.header_data = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36 QIHU 360SE',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wooyun.org/corps/'}

    def __getPage(self, url):
        r = requests.get(url, headers=self.header_data, cookies=self.parseCookies)
        r.encoding = 'UTF-8'
        self.parseCookies = r.cookies
        # print(r.text)
        return r.text

    def condb(self):
        try:
            config = {
                'user': 'root',
                'password': '',
                'host': '127.0.0.1',
                'raise_on_warnings': True,
            }
            self.cnx = mysql.connector.connect(**config)  # 尝试连接
            self.cursor = self.cnx.cursor()
            self.cnx.database = 'wuyun'

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")

    def getCorps(self, url, num):
        i = 1
        while 1:
            baseUrl = url + str(i)
            self.header_data.update({'Referer': baseUrl})
            soup = BeautifulSoup(self.__getPage(baseUrl), "html.parser")
            tag_tbody = soup.tbody

            for child in tag_tbody.children:
                s = BeautifulSoup(str(child), "html.parser")
                ls = s.find_all('td')
                if not ls:
                    pass
                else:
                    date = re.findall("<td [^>]+>(.*)</td>",
                                      str(ls[0]))[0]  # [^>] 匹配不包含> 的单独字符 加上+ 次或多次匹配前面的字符或子表达式 把前面的匹配为一个整体
                    company = re.findall("<td [^>]+><a [^>]+>(.*)</a></td>", str(ls[1]))[0]
                    web = re.findall("<td [^>]+><a [^>]+>(.*)</a></td>", str(ls[2]))[0]
                    sql = "INSERT INTO `crops` (`日期`, `公司`, `网站地址`) VALUES ('{}', '{}', '{}')".format(date, company, web)
                    print(sql)
                    try:
                        self.cursor.execute(sql)
                    except mysql.connector.Error as err:
                        print(err)
            print("第{}页面".format(i))
            i += 1
            if i > num:
                print("完成 ")
                exit()
    def getBugs(self, url, num):
        i = 2
        j = 0
        host = "http://www.wooyun.org"
        while 1:
            baseUrl = url + str(i)
            self.header_data.update({'Referer': baseUrl})
            soup = BeautifulSoup(self.__getPage(baseUrl), "html.parser")
            tag_tbody = soup.find_all('tbody')[2]

            for child in tag_tbody.children:

                s = BeautifulSoup(str(child), "html.parser")
                ls = s.find_all('tr')
                if not ls:
                    pass
                else:
                    try:
                        date = re.findall("<th>(.*)</th>", str(ls[0]))[0]
                        #                # [^>] 匹配不包含> 的单独字符 加上+ 次或多次匹配前面的字符或子表达式 把前面的匹配为一个整体
                        try:
                            title = re.findall("<td><a [^>]+>(.*)</a>\s{0,}</td>", str(ls[0]))[0]

                        except:
                            title = re.findall("<td><a [^>]+>(.*)</a>\s{0,}<img [^>]+>\s{0,}</img>\s{0,}</td>", str(ls[0]))[0]
                        try:
                            link = host + re.findall("<td><a href=\"(.*)\">[^<]+</a>\s{0,}</td>", str(ls[0]))[0]
                        except:
                            link = host + re.findall("<td><a href=\"(.*)\">.*</a>\s{0,}<img [^>]+>\s{0,}</img>\s{0,}</td>",
                                                     str(ls[0]))[0]
                        try:
                            reply, author = re.findall("<th><a [^>]+>(.*)</a></th>", str(ls[0]))
                        except:
                            print("获取失败")

                        sql = "INSERT INTO `bugs` (`日期`, `标题`, `链接`, `评论`, `作者`) VALUES ('{}', '{}', '{}', '{}', '{}')".format(
                            date, title, link, reply, author)
                        print(sql)
                        try:
                            self.cursor.execute(sql)
                        except mysql.connector.Error as err:
                            print(err)
                            pass
                    except:
                        f = open('erro.txt', 'w')
                        f.write("错误sql {} 第{}页 ".format(sql, i))
                        f.close()
                        pass
            print("第{}页面".format(i))
            i += 1
            if i > num:
                print("完成 ")
                exit()


s = wuyun()
# s.getCorps("http://www.wooyun.org/corps/page/", 44)
s.getBugs("http://www.wooyun.org/bugs/page/",4636)
