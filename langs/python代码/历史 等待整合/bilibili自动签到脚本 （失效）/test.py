

import requests
url ="http://www.bilibili.com/video/bagumi_offical_1.html#!page=1145.html"
r = requests.get(url)

r.content.decode()