import http.cookiejar
import j
import re
import requests
import time
import threading
import time
from  bs4 import BeautifulSoup


################################
# python 进程问题 共享数据 提交6次就停止提交
#
#
#################################
class Th(threading.Thread):
    def __init__(self, thread_name, fuc):
        threading.Thread.__init__(self)
        self.setName(thread_name)
        self.fuc = fuc

    def run(self):
        print('This is thread ' + self.getName())
        self.fuc.getPage(self.getName())
        print(self.getName() + "is over")


class onePlus():
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def add(self):
        self.lock.acquire()
        self.count += 1
        self.lock.release()

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

    def main(self):
        Head = {'Accept-Encoding': 'gzip, deflate', 'Referer': 'http://tieba.baidu.com/p/4606774183',
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Connection': 'keep-alive',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Cookie': 'TIEBA_USERTYPE=e00402789c6588887439aa71; bdshare_firstime=1462708158742; BDUSS=UyVXdpYkxlYkR-clBwY09aZG1MMngzempjbzZlUHI1MnRQbnFzeUpjUWZ6MXBYQVFBQUFBJCQAAAAAAAAAAAEAAAB-qgk-QW5nZWxXaW5nc0xpbmsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB9CM1cfQjNXR2; TIEBAUID=2c5edaefe2df7be6289fde1e; BAIDUID=8AB76EACC2D03C1BE9138B04ADB0E2CF:FG=1; PSTM=1464768101; BIDUPSID=117CFFAFA9C356A5907CDE808C20A3EC; __cfduid=d23704e965009471b782944466629dfec1465646504; showCardBeforeSign=1; rpln_guide=1; H_PS_PSSID=1456_17943_20076_15105_12094; td_cookie=18446744071586013712; wise_device=0; LONGID=1040820862',
                'Accept': 'application/json, text/javascript, */*; q=0.01', 'Origin': 'http://tieba.baidu.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
                'Host': 'tieba.baidu.com'}

        data = {'kw': '一加手机', 'ie': 'utf-8', 'rich_text': '1', 'tbs': '171d02f9df525c451465906743', '__type__': 'reply',
                'tid': '4606774183', 'content': '一加三 我来了 ', 'fid': '9224366'}
        self.add()
        if self.count < 2:
            print("onepluse2 ")
            r = requests.post("http://tieba.baidu.com/f/commit/post/add", data=data, headers=Head)
            print(r.text)
            f = open("onePluse.txt", "w")
            f.write(r.text)
            f.close()
            print(self.count)


    def getPage(self, th):
        while 1:
            # start = time.clock()
            url = "http://tieba.baidu.com/p/4606774183?pn=9399"
            r = requests.get(url)

            last = re.findall("post_no&quot;:(\d{5,7}),", r.text)
            print(th + "    " + last[-1])
            # end = time.clock()
            # print(end - start)
            lastint = int(last[-1])
            if lastint == 999991:
                self.main()


s = onePlus()
thread1 = Th("T1", s)
thread1.start()
time.sleep(0.2)
thread2 = Th("T2", s)
thread2.start()
time.sleep(0.2)
thread3 = Th("T3", s)
thread3.start()
time.sleep(0.2)
thread4 = Th("T4", s)
thread4.start()
time.sleep(0.1)
thread5 = Th("T5", s)
thread5.start()
time.sleep(0.1)
# thread6 = Th("T6", s)
# thread6.start()
# time.sleep(0.4)
# thread7 = Th("T7", s)
# thread7.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
# thread6.join()
# thread7.join()
print("OVER")
