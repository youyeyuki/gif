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
        Head = {'Accept-Language': 'zh-CN,zh;q=0.8', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Host': 'tieba.baidu.com', 'Accept-Encoding': 'gzip, deflate', 'X-Requested-With': 'XMLHttpRequest',
                'Connection': 'keep-alive', 'Content-Length': '515',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Cookie': 'TIEBA_USERTYPE=d8c56c89e640a17b81484718; bdshare_firstime=1461424062714; TIEBAUID=a1c075c47ba9cfc47179002f; BDUSS=mdkT21WT0ZWTzZDM3FXSTJFd1NHMFZZMjNaaGN4TFV3bjEzc2dJelY4QTN3VWxYQVFBQUFBJCQAAAAAAAAAAAEAAAAqyYMQTXlMeTQ4NjkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADc0Ilc3NCJXd; rpln_guide=1; BAIDUID=CE4B1B5D8A0943883932F0549480FA6A:FG=1; BIDUPSID=CE4B1B5D8A0943883932F0549480FA6A; PSTM=1465797754; td_cookie=18446744071493015507; BDSFRCVID=XOFsJeC62Gqof5JRV7TO81Rcl2Ka28jTH6ao-C7YDrHum5uV50ILEG0PtOlQpYD-VIikogKK3gOTHxjP; H_BDCLCKID_SF=tRC8_CIhtCvbfP0kKP6qK4oH-UnLqhv93j7Z0l8Ktq3aDnLGyl54jp0geaQN5-AHWKCHVncmWIQHDT6JjprUKxk0hHotLjLjWmJ4KKJxbp7SVtJXQKc4ytFfhUJiB5JMBan7XncxfJOKHICGjju-DUa; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=1465_20317_18281_20076_19861_15801_12235_20253; Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1464709137,1465812790,1465812916,1465816823; Hm_lpvt_287705c8d9e2073d13275b18dbd746dc=1465825173; wise_device=0; LONGID=277072170',
                'Referer': 'http://tieba.baidu.com/p/4606774183?pn=9999', 'Origin': 'http://tieba.baidu.com'}

        data = {'content': '一加三来了 加油', 'kw': '一加手机', '__type__': 'reply', 'fid': '9224366', 'rich_text': '1',
                'tid': '4606774183', 'ie': 'utf-8', 'tbs': '40c781c776cd08201465825180'}
        self.add()
        if self.count < 2:
            print("这是sdfsdfsdf史蒂夫 ")
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
            if lastint == 999997:
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
