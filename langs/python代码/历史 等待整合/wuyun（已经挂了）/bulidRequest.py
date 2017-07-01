import re

data = """Accept-Ranges:bytes
Connection:keep-alive
Content-Length:10567
Content-Type:text/css
Date:Fri, 18 Mar 2016 10:34:40 GMT
Last-Modified:Mon, 07 Sep 2015 09:17:52 GMT
Server:nginx"""
ls = data.split('\n')
dic = {}
for num, data in enumerate(ls):
    # print(data)
    rels = re.findall('[^:]+', data)
    try:
        rels[1] = "{}:{}".format(rels[1], rels[2])
    except:
        pass
    dic[rels[0]] = rels[1]
print(dic)
