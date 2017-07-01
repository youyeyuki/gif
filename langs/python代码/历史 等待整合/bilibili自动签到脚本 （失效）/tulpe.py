import sys

import j
# # t = sys.argv[1]
# t = "1,2,3"
# l = t.split(",")
# print(tuple(l))
# i = (1, 2, 3, 4, 5, 6,)
# for a in i:
#     if a not in tuple(l):
#         print(a)
def parseawardjson(remsg):
    data = j.loads(remsg, encoding='utf-8')
    if data["code"] == 0:
        print("领奖成功")
        print("当前的银瓜子是{} 奖励银瓜子{} 获取投票劵 {} ".format(data["data"]["awardSilver"],data["data"]["awardSilver"],data["data"]["getVote"]))

    else:
        print("错误代码 {}".format(data["code"]))
        print("{}".format(data["msg"]))
str  = """{"code":0,"msg":"ok","data":{"silver":1330,"awardSilver":30,"getVote":1,"svote":18,"vote":null}}"""

parseawardjson(str)