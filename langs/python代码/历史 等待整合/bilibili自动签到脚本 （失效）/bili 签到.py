import j
import sys
import time
import random
import http.cookiejar
import requests
import os
import re

# for i in range(0,100):
#     sys.stdout.write("现在是" + str(i)+"\r",)
#     sys.stdout.flush()
#     time.sleep(1)
def randomNumTryAgain():
    while True:
        fNum = random.uniform(0.0, 1.0)
        if len(str(fNum)) == 18:
            print(fNum)
            return str(fNum)
            break


def 超越世界线吧():
    for i in range(60):
        sys.stdout.write(float(randomNumTryAgain()) + "\r", )
        sys.stdout.flush()
        if i == 59:
            print("世界线  " + randomNumTryAgain(), flush=True)
        time.sleep(1)


def loadCookie():
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


path = os.getcwd()

head_data = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}

# for i in range(0, 500):
#     r = requests.get("http://mooc1-2.chaoxing.com/img/code", headers=head_data, stream=True)
#     r.encoding = 'UTF-8'
#     f = open(path + "\\pic_collection\\" + str(i) + ".jpg", 'wb')
#     print("下载第{}个样本".format(i))
#     f.write(r.content)
#     f.close()


code = 'pxnew'
nodeid = "86884657"


def dlvcode():
    r = requests.get("http://mooc1-2.chaoxing.com/img/code", headers=head_data,cookies=loadCookie(), stream=True)
    r.encoding = 'UTF-8'
    f = open("caoxin.jpg", 'wb')
    f.write(r.content)
    f.close()



def sendVcode(nodeid, code):

    classid = "619106"
    vadate = "http://mooc1-2.chaoxing.com/img/ajaxValidate?code={}".format(code)
    r = requests.post(vadate, headers=head_data, cookies=loadCookie())
    print(r.text)
    Ocr_code = "http://mooc1-2.chaoxing.com/edit/selfservice?code={}&nodeid={}&clazzid={}".format(code, nodeid, classid)
    r = requests.get(Ocr_code, headers=head_data, cookies=loadCookie())
    print(r.text)
    return r.text





classid = "619106"
flag = 0
f = open("x", mode='r')
data = f.read()
s = re.findall('id="cur(.*?)"',data)
f.close()
for i in s:
    if i == "86884697":
        flag = 1
    if(flag):

        r =  requests.get("http://mooc1-2.chaoxing.com/edit/validate?clazzid={}&nodeid={}".format(classid,i), headers=head_data, cookies=loadCookie())


        print("现在进行解锁 "+i)
        dlvcode()
        code = input()
        sendVcode(i, code)

        # while sendVcode(i, code) == 'false':
        #         r =  requests.get("http://mooc1-2.chaoxing.com/edit/validate?clazzid={}&nodeid={}".format(classid,i), headers=head_data, cookies=loadCookie())
        #         print(r.text)
        #
        #         print("现在进行解锁 "+i)
        #         dlvcode()
        #         code = input()



