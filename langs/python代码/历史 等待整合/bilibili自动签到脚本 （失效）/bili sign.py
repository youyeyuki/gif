import j
import http.cookiejar
import requests
import time
import random
import os
import re


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


def parsejson(remsg):
    data = j.loads(remsg, encoding='utf-8')
    if data["code"] == 0:
        print("签到成功")
        return 0
    else:
        print("错误代码 {}".format(data["code"]))
        print("{}".format("你今天已经签到"))
        return 1


def randomNumTryAgain():
    while True:
        fNum = random.uniform(0.0, 1.0)
        if len(str(fNum)) == 18:
            print(fNum)
            return str(fNum)
            break


def CurrentTaskjson(text):
    data = j.loads(text, encoding='utf-8')
    if data["code"] == 0:
        print("CurrentTaskGet  {} minute".format(data["data"]["minute"]))
        return data["data"]["minute"]
    else:
        print("错误代码 {}  {}".format(data["code"],data["msg"]))
        if data["code"] == -10017:
            print("随便输入一个字符退出......")
            s = input()
            exit(0)
        return 1


def readFile(path):
    f = open(path, 'r', encoding='utf-8')
    return f.read()


def ocrIdentify(curPath):
    commandPath = "\"D:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe\" "
    FileName = curPath + "\\getCaptcha.jpg"
    outFile = curPath + "\\getCaptcha"
    os.popen("{} {}  -l bili {}".format(commandPath, FileName, outFile))
    print("{} {} -l bili {}".format(commandPath, FileName, outFile))
    time.sleep(3)
    code = readFile("D:\\py\python3.5\\bilibili自动签到脚本\\getCaptcha.txt")  # 读取文本内容
    print(code)
    if code == '':
        print("空文本识别")
        return -1
    else:
        s = re.findall("(\d+)([-+])(\d+)", code.strip())
        if s[0][1] == '-':
            identifyCode = int(s[0][0]) - int(s[0][2])
            print("计算结果{}".format(identifyCode))
        elif s[0][1] == '+':
            identifyCode = int(s[0][0]) + int(s[0][2])
            print("计算结果{}".format(identifyCode))
        else:
            print("ocr识别错误 -1")
            return -1
        return identifyCode


cookie_jar = loadCookies().getCookies()
head_data = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
r = requests.get("http://live.bilibili.com/sign/doSign/", headers=head_data, cookies=cookie_jar)
check = parsejson(r.text)

# 签到另开线程

# 初始化操作
curPath = os.getcwd()
cookies_tmp = cookie_jar
TaskHeads = ({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Host': 'live.bilibili.com', 'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8', 'Referer': 'http://live.bilibili.com/3',
    'Accept-Encoding': 'gzip, deflate, sdch', 'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest'}
)

heartheads = ({'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'zh-CN,zh;q=0.8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
               'Referer': 'http://live.bilibili.com/3', 'X-Requested-With': 'XMLHttpRequest',
               'Connection': 'keep-alive', 'Host': 'live.bilibili.com', 'Accept-Encoding': 'gzip, deflate',
               'Content-Length': '0', 'Origin': 'http://live.bilibili.com'}
              )
imgHeards = ({'Accept': 'image/webp,image/*,*/*;q=0.8', 'Connection': 'keep-alive',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
              'Referer': 'http://live.bilibili.com/3', 'Accept-Language': 'zh-CN,zh;q=0.8',
              'Host': 'live.bilibili.com', 'Accept-Encoding': 'gzip, deflate, sdch'}
             )

while 1:
    randomStr = randomNumTryAgain()

    getCurrentTask = "http://live.bilibili.com/FreeSilver/getCurrentTask?r=" + randomStr
    r = requests.get(getCurrentTask, headers=head_data, cookies=cookie_jar)
    finTime = CurrentTaskjson(r.text)
    # time.sleep(60 * 剩下等待时间 + 5)
    for i in range(0, finTime):
        r = requests.get("http://live.bilibili.com/feed/heartBeat/heartBeat", headers=head_data, cookies=cookie_jar)
        print("心跳线heartBeat " + r.text)
        r = requests.get("http://live.bilibili.com/freeSilver/heart?r=" + randomNumTryAgain(), headers=heartheads,
                         cookies=cookie_jar)
        print("心跳线 验证 " + r.text)
        time.sleep(60)
        print("已经过 {}".format((i + 1) * 60))
    time.sleep(5)

    # 确认用户是否存在
    r = requests.post("http://live.bilibili.com/User/userOnlineHeart", cookies=cookie_jar, headers=TaskHeads)
    print("确认用户是否存在" + r.text)

    getSurplus = "http://live.bilibili.com/freeSilver/getSurplus?r=" + randomNumTryAgain()
    r = requests.get(getSurplus, headers=TaskHeads, cookies=cookie_jar)
    print("Surplus" + r.text)

    while True:
        print("获取验证码")

        getCaptcha = "http://live.bilibili.com/FreeSilver/getCaptcha?t=" + randomStr

        r = requests.get(getCaptcha, headers=imgHeards, cookies=cookie_jar, stream=True)
        print("获取验证码图片" + getCaptcha)
        r.encoding = 'UTF-8'
        f = open("getCaptcha.jpg", 'wb')
        f.write(r.content)
        f.close()
        # ocr解析
        identifyCode = ocrIdentify(curPath)
        if identifyCode != -1:
            break
    # 提交验证

    r = requests.get("http://live.bilibili.com/feed/heartBeat/heartBeat", headers=head_data, cookies=cookie_jar)
    print("心跳线heartBeat " + r.text)
    r = requests.get("http://live.bilibili.com/freeSilver/heart?r=" + randomNumTryAgain(), headers=heartheads,
                     cookies=cookie_jar)
    print("心跳线 验证 " + r.text)

    print("提交验证")
    getAwardHeads = ({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Connection': 'keep-alive', 'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'http://live.bilibili.com/3', 'Accept-Encoding': 'gzip, deflate, sdch',
        'Host': 'live.bilibili.com', 'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'zh-CN,zh;q=0.8'}
    )
    getAward = "http://live.bilibili.com/freeSilver/getAward?r={}&captcha={}".format(randomNumTryAgain(), str(identifyCode))
    print(getAward)
    r = requests.get(getAward, headers=getAwardHeads, cookies=cookie_jar)
    print("getAward " + r.text)
