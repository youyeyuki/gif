import j
import http.cookiejar
import requests
import time
import random


class loadCookies:
    def __loadCookie(self):
        cookie_jar = http.cookiejar.MozillaCookieJar()
        cookies = open('cookies.txt').read()
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

    def getCookies(self):
        return self.__loadCookie()  # 开放接口
def randomNumTryAgain():
    while True:
        fNum = random.uniform(0.0, 1.0)
        if len(str(fNum)) == 18:
            print(fNum)
            return str(fNum)
            break
cookie_jar = loadCookies().getCookies()
head_data = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}

heartheads = ({'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'zh-CN,zh;q=0.8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
               'Referer': 'http://live.bilibili.com/3', 'X-Requested-With': 'XMLHttpRequest',
               'Connection': 'keep-alive', 'Host': 'live.bilibili.com', 'Accept-Encoding': 'gzip, deflate',
               'Content-Length': '0', 'Origin': 'http://live.bilibili.com'}
              )
TaskHeads = ({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Host': 'live.bilibili.com', 'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8', 'Referer': 'http://live.bilibili.com/3',
    'Accept-Encoding': 'gzip, deflate, sdch', 'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest'}
)
while True:
        r = requests.get("http://live.bilibili.com/feed/heartBeat/heartBeat", headers=head_data, cookies=cookie_jar)
        print("心跳线heartBeat " + r.text)
        r = requests.get("http://live.bilibili.com/freeSilver/heart?r=" + randomNumTryAgain(), headers=heartheads,
                         cookies=cookie_jar)
        print("心跳线 验证 " + r.text)
        # 确认用户是否存在
        r = requests.post("http://live.bilibili.com/User/userOnlineHeart", cookies=cookie_jar, headers=TaskHeads)
        print("确认用户是否存在" + r.text)
        time.sleep(60)