import requests

url = "https://kstj.baidu.com/v.gif?pid=102&url=https%3A%2F%2Fzhidao.baidu.com%2F&isLogin=1&right_promotions=1&bottom_promotion=1&type=2014&action=click&pos=signin-dialog-submit"
headers = {'Connection': 'keep-alive', 'Host': 'kstj.baidu.com', 'Referer': 'https://zhidao.baidu.com/',
           'Accept-Encoding': 'gzip, deflate, sdch',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
           'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept': 'image/webp,image/*,*/*;q=0.8',
           'Cookie': 'BDUSS=mdkT21WT0ZWTzZDM3FXSTJFd1NHMFZZMjNaaGN4TFV3bjEzc2dJelY4QTN3VWxYQVFBQUFBJCQAAAAAAAAAAAEAAAAqyYMQTXlMeTQ4NjkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADc0Ilc3NCJXd; BAIDUID=43E99D613767DD3F9D0A1E769D481A8E:FG=1; PSTM=1466523361; __cfduid=d5df6b911a51f74c6719ccd90a9960b8c1470498495; BIDUPSID=E94E03C360178CAB0AAF7ACF32498F45; H_PS_PSSID=1423_20973_18241_17943_21119_20698_21226_21190_21160_20930'}

r = requests.get(url, headers=headers)
r.encoding = "UTF-8"
print(r.text)
