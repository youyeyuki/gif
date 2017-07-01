# s = "32:64:39:30:61:39:30:38:31:63:62:38:64:61:63:38:61:64:65:65:61:34:63:33:61:66:30:33:34:39:32:61"
#
# a = s.split(":")
# tmp = ""
#
# for i in a:
#     tmp += chr(int(i, 16))
#
# print(tmp)
#
# s = 0x2d90a9081cb8dac8adeea4c3af03492a
#
#
# def hexToOCT(str):
#     str = "0x" + str
#
#
# dic = {12: "A", 53: "B", 33: "C", 32: "D", 31: "E", 42: "F", 52: "G", 62: "H", 81: "I", 72: "J", 82: "K", 92: "L",
#        73: "M", 63: "N", 91: "O", 1: "P", 11: "Q",
#        41: "R", 22: "S", 51: "T", 71: "U", 43: "V", 21: "W", 23: "X", 61: "Y", 13: "Z"}

# 9 10
# def check(sum, rs):
#     ls = []
#     for i in sum:
#         ls.append(i)
#     if len(list(set(ls))) == 10:
#         print(ls, rs)
#         exit()
#
#
# i = 9999
#
# while 1:
#     sum = i * i
#     check(str(sum), i)
#     i += 1


##

import requests

# s = "ud1SI80j4CJWDLImOTHoTS9lYPHG009MoD5Jiycn8MrBjAb2RVmN3zTR6id9mcN59J42XWa1I9a2FzLlES8dOccioEHICRE1GbX1T9tcwtXLzAqPtE8bZftNT4zYzqqewrU6bupJoNXTl77yR0toZXSxtvUS2Y27byESnaXnLmywttGrBSvaxGWMw85vBnAwOgOQTM5NjQuepaAyoajbHNbXvtctT67wIEtQzFun5FFefEKb0UHCPFyNI8wk0wk6KfMp4nZLkkn2cg1bJZSLvdOXel0a0tf8M3RZO9Pf6ri0pCgpswuhXbZ8E78oL7yeVbqX3q9kCvSspUNchH9TBU6ErASibidZ7ZfTKzCymgxejMCjtAT3NKIBIMmDtPibAUf133VtzezEfkYVq94mw7SiOmVoknyRfiWNrL8fEDtgXELheb4qfWhCwHBtfbfWNOnsgm1fBqG9FtAwGn2P35a5D1BtmRqja05He2rxoFMsuO5bcOsA3LTqRKQDpvIsqqQt1Lj6uHgkPJyKatBx8aRyHLUOkuxVisY1MvWsa9Q9tsCGKFKy35Om2nvJjDG469M10krlGtKK8rkcUrEl1fGeNzTjaStofHpiOd5EhaOWeV753fAn0jWl5ZBfkxbjH8nYBI35m1YAPHVtxkAPJaLbl9lpn8jQEjWegYVLhhERek23OnxSiIHJrfIl0Zc6oUw7tFhTwTIJshpfX1UXnCFnGUtGnOfcksvo21uzFRHCTktP3KjOqbZqazgkIUHPTP5l49MAlkFRQy2aARiNDKr04RFT0yo1k6QUiKBBTknlxUzN13tZ1S1NRPe3BLQ3Mxbwm9dy6HSiZ59vu1ZtMyMdSyyGUhCUHO5qYle53hKaWpU5SfCwh53O0vEne6D8rImrqa3CiKSahxDniwkV0eppfLDPAjeYkOAJlkljiD0LFNOTpOz9DCqbvEFUlSVeKiTWiTNYJnB0F0SorCuga5jcjt2ZOb2sDzth3PB2ltPq7OlUsKwonAgT6o2M9ceaW58h8Sa115v4Z1nFTiZk0u6YSSKpMy0uMqN5qFxMmJWBHykmMdgmClYtL7KgGksEQTCjk95C36UtQDjoxdLUZbXxcKyNIkpjuavUS82mYHipo1pbVowSTkS5PQAj0xSkwWHCcpA1G81nCkrIbvLTc9wwAXbfgxARU0E1Bd8906sMNrvhehyIacC3uZDJY5hnZcxgit8egoPzCgYuaDIPLEe7WqexF0XvavbRN4qsSZ9lziOg33FJoBfSUyxh0cE2N4xSLwunmjLJAbWlpZ6YSfT5DoRtkDtGLsxEDJAsAMnuyOIaHReX5p81S5ObZLQY7jYBc3kdhiQdmbVH3G1bSVIbL6kQAGXgWHXE3XQlMUNJR9pGBMjs9N2F0kGYVHFUIyNR1zbzi3fyS1HitBX8SHze4jffEJ83jj0SF5LIMFkJd7r0iY9fXNlMhkQPzHfjffQr1MCWyquB7QhcCTbg9eK7Dll5AqXsnaU1JfXxLo6DF4eRCHHfgpRN9xYL5GZ0U1B2boowMzb2OrGhNzw5ckbAvl5JSWOLpf1cFd5CjMCObrMfgCPztDWHUWaCYl1fLHBvExLX3Ae1X4YwYZ106s6GhGZQ0m9zmjjn7EYWfsLHGGw6tsmaO88cRduniEZALkS5Vr8uvHzQPhBYmSZuhAIGC3cbdPeyelfu94vKu42cDwfpims1Rnc4YTRxf1OxH83rnoDodfGG2UVa2vtHnuoFcPk2Q3Rkm5TTyag2eVH4ug8QEHn22mu2C39Yv69olNyFjDeFCzX8tYHfH0BkMAo0fFoDeG1TR9jsBng4zndn2RS0w1KbHIIhOnpGnjPIJEWnconqJSk2qpU4i7oAG9Fit0HEGSO4XAU3wKEtoUbzmBHNXhaDBrbyAMBoSCgqpJxiBQBQD8JfKEr56RPyYkJHlW4Te7wQ45MbwvrszESG1nqIatXXoNZdu27NIkrUTHXMAnZfggOZjd5P5fbxiJcNE83aq9VcdfJEH6TA9RuEbYdYYifZ6EaMpzDBbxee5FBpw9G6zjtpAOLWP4LfPOMeW0GuXZ5aIqeHphkJRpwJjGio4B0joeborTuRGVhlmLHuojRwPPRuT9T5wwcs4EXmnBI8lOtu4YydkkBaXSCTN2NcWs1xi1SVmZG3Sd9i6TaOfzWw2Ffdzw7QkB5Dl1NR9eOHQGYZreWMJ0Vj2eOLxRRBO54mkxj3wXRTKXVrSKJrGkatPLnMLbt3Ek2bgSwfA4NjpdAkuANjvJGM1jglNFQTyMSvMRcT8Gai5xjvD7HwZ9t73qqFA2HFSvpxQYfEsx8obe4KwvC2FN2FXLot5oyaakTO4kFs17rqiFdIciC575BL6navooIGd15Qlk7jKuAF8YM5psQ2DGBvqNY4LbxsH3OqWfxtM2nk1RsRrTDSuclvSCacZ82qzd13W3ASeUYlIcwvTbl5rJhx9n9pQCfi2rn40YuWvvajeujBtESj0GEufxi8mfqJusImDgublmQC9aPCWuZHtucc7POi17KzGWY26kh89g13PYGshLJ8NXO9G56LjRCrXRGI10zj2bSpbqDG31e804rknJ6cAQlQeAmNKdHyxx6r84mGSbcArEloSAr53OHwuhdxKYXoRRot4hgRLy2Tng1OVCRfRqyOPQzWzgB7F5RuiSusYHyc8XIm6TzLiXr2fBwslWtXZ0foJVR7kPKo2nSf5y9MQkCPhFlW28rwkogjCY4q7znUB84fGeBxanvMRNCx1rST46fc2A9bfSs6FHSpRK5RwtUvbWb6pyZLjNX3lRpVPOU6qld45pnGTUiulsyS8IqKTzsKBoYcpLo2xfb7m5OVjRYkkuul9I0Yg2hrkRkXiT9GpLmObaqS235xftztuAo4TxzwDFdrwyqw0CMAIWC14QkycGb12SoYIEMMb7w7Q9w0di3xZ7Mu57BkDBLKQtrmtp8G34q6lvNlZ39IPyEA45tvrRJj5509xSwoD9qS5eMOwwrpGkPy7Uq7HSPX6kpZaFBU1J42asyDKD5QkttKDpRI5mbnR2uMJEs5SksDOS4TnFY7ln3VIgGEKgFnsP46lBxY3PtKLGHd0Ox4IaItUgivYR4t1RKd36FWKQJeHrBIgrD6FcExEXI1S5qeoXTTzMjJx8WlmEWQei3tfjCJ1fNhfucKRZdRQDfpDBq97poOqNsWv5vzy5kaD24HO4NlptpT9LBXKzipczdbHWXurjkLeOh8e7HvOKYQU2gftfGFAdozfcMRrVHfyrBWXuwKjICofdAeck3jxce18vc2uvuukSipvhGSpRQ2EvqJiadaUq846DDOtRNs2D1JeHlcCzBjEC7pQJPUT6jr9fhLLTZAq8pxbEk9Z6rRcDCrHkFRgm7mGpcWOmrcXq4WzGN5kSKqqxCsC8tegBcL6INJQf2lBvrcecllT8BNtOqjxYJbtVAEEo3p2nGcj3n6QHSc7hux3eROahmTMLv2lf76RvcplsYLfP4SuUYaFWddqL2ofzxd9NukA2cen3Lcu59KMKUKeXA7a5wlE3VwLK0VnHA04WzQF1FrZTT060BUfTSyxOP9DmO30JxEA9W5xNR9k3lr2K7jCFpMvmtbEVujIdfgFXuQMvT547kqdEHnJT8oi55RRx8XqHigT4ZWRqMv3Z3ESweKRpPzJIVgvxkEep0RZcbMunRhZ7pUc4j3UfL9B9L5KtbyOHYthxQm9SKtKrboOBK07B64Rmso9DZSQ2RBWGhd2up5HZQgGv5r5OXGY7aIHhSgTjZoXXwGdkHyDTNnXLHEtPOguVyHyTSEHiHV0kA9IdMSp2qbewPrPsLoqR3j6pxKrZd8CMhWRcuVmEatnVAqvCZdVVBzu4ehrOon8Dt5tC2E7QIb3KSLgz8k6RImMl1zTv1uggGgUozkvPhw8AP2trnp92zRalK8v0l8Yl4uAbanTbyZ8MEPLioikK6kHv16xxnBiQ8G1Zt246PxJAd0oeKC9SXtzhbi2U8Lty7Tn6bCqu9apn6dFEyu6rL33XEofdRvNmWIJ2bxknIu6X05ez6y1u7E3ydiFLPTpOxRGBSND6WLsV2HbifS34DNGUlUz6d0kjTreAzjZd7TH4U4ai3XFQBchZOxKvZN9Ets9Bqs8ywjvRKwO2DdgabEosX2eNEabuhAWy1NQUj8GnhSk0lBWokCLpTE7peFnZPRFSmrwZb0EvxBwjxnSjXQcnAJCHrGVjC137rSuUbSXjCWedxHDSIjtwN91680TnFhMDMv5AbBdwkeQsG3aoZFaUXc4y7OTaZEts6VhzjWxxuUA8vf7QzkznIhsgxVIwOrq8zqrCf9bzcucob3l57hepWqIqVmoocQdufFlr1CeM0uvmeLhSZH7wmKWXZGpNJuxVdR3BMOwGH3Fn5gEGOaHUn2tBjSmmFEHTKqpQfYm33S6hy1YrTCJ5sApmj8DandpF6bJ9wXT9QsVK8hLF2qJMP3oD2HGUbe6YzoowCKiantZ1sjMgOpGXbMVQEgKGrVOMiUSIBuvGxihuBftXjCWpPbjqKVxrw8iovkddIekAglWIpBopBPRp4HGJtlo19OGf9zllWEnCkIXMvqng5GTTwMR2SPnuIEm4YtIVGCT5QCAxgxYKDTERVvjeqfKYb9yeepXFuPBVPzr8QsEYYRDSH5GHnYZVJE1ymwFmqwY6ftTvvUidWVsuJh4XsIqStAm4PEJbHz2enPzhOJslsRpkZ4E1hyg69EJGvwlZYYKA1tvBv4HAjLHm8Ro9DoiEEZPfL44IekGaxy75vxSoWZ3NblkKqGftfxkD3RGBewNC2XLYPuTLkRkzaxSsE32sasjqCjlgxpBMrhD1VH5crGXiHLwrmqGboHhXvc3kXZplhN4r1K9xgWHii2rUpUL2ldr4q98w1B6lb7YjQRE69EEbwvnJGxYf2lWkfqOyRDC0WoSJJhGiJFmcla9s8n786n0owCU7"
# rs2 = ""
# x = 1
# for i in s:
#     if x == 102:
#         rs2 += i
#     if x == 400:
#         rs2 += i
#     if x == 1201:
#         rs2 += i
#     if x == 1604:
#         rs2 += i
#     if x == 1800:
#         rs2 += i
#     x +=1
#
# print(rs2)


# # 小明的数学作业，你能帮他完成这道题吗？ s=1+2*3+4*5···98*99+100，求s的值。164251
#
# s = 0
# i = 1
#
# while 1:
#     if i == 1:
#         s += i
#         i += 1
#     else:
#         s += i * (i + 1)
#         print(i, "   ", i + 1)
#         i += 2
#     if i > 98:
#         break
# print(s + 100)


hex_code = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

md5_ls = ""
md5 = "4d1e3cbl10c094e4f7c704232956bc34"
# print(md5)
# print(len(md5))
# for i in md5:
#     if ord("f") - ord(i) >= 0:
#         md5_ls += i
#     else:
#         print(i)
#
# print(md5_ls, "     ", len(md5_ls))

# for i in hex_code:
#     req = md5.replace("l",i)
#     print(req)
#     r =requests.post("http://106.75.8.230:16371/index.php?str="+req)
#     print(r.text)

# s = "synt{91o19r02-4so7-45o6-n59o-4rqnp2o1q2nq}"
#
# f = ""
#
# for i in s:
#     if "a" < i < "z":
#         f += chr(ord(i)-13)
#     else:
#         f += i
# print(f)
#
# for i in range(1235,10000):
#     print("http://106.75.8.230:12866/"+str(i).zfill(4)+".php")
#     r = requests.get("http://106.75.8.230:12866/"+str(i).zfill(4)+".php")
#     if r.status_code ==200:
#         print(r.text)
#         break

# import base64
#
# s = ""
#
# for i in range(128):
#     str = "6ZWc6Iqx5_C05pyI".replace("_", chr(i))
#     try:
#         r = requests.post("http://106.75.8.230:17048/index.php?str="+str,timeout=5)
#         if r.status_code == 200:
#             print(str, r.text)
#     except:
#         pass




# peigeng1 = {"00000": "A", "00001": "B", "00010": "C", "00011": "D", "00100": "E", "00101": "F", "00110": "G",
#             "00111": "H", "01000": "I", "01001": "J", "01010": "K", "01011": "L", "01100": "M", "01101": "N",
#             "01110": "O", "01111": "P", "10000": "Q", "10001": "R",
#             "10010": "S", "10011": "T", "10100": "U", "10101": "V", "10110": "W", "10111": "X", "11000": "Y",
#             "11001": "Z"}
#
# peigeng2 = {"00000": "a", "00001": "b", "00010": "c", "00011": "d", "00100": "e", "00101": "f", "00110": "g",
#             "00111": "h", "01000": "i", "01000": "j", "01001": "k", "01010": "l", "01011": "m", "01100": "n",
#             "01101": "o", "01110": "p", "01111": "Q", "10000": "r",
#             "10001": "s", "10010": "t", "10011": "u", "10011": "v", "10100": "w", "10101": "x", "10110": "y",
#             "10111": "z"}
#
#
#
# s = "01001 00100 01100 01100 00000 10000 00011".split(" ")
# tmp =""
# for i in s:
#     tmp += peigeng2[i]
# print(tmp)

# s="mzdvezc"
# tmp =""
# for i in s:
#     tmp += chr((ord(i)-12)%5)
# print(tmp)

s = 0x5555555595555A65556AA696AA6666666955
a  = str(bin(s)[2:])
tmp =""
print(a)
while 1:
    c = a[0:2]
    print(c)
    a = a[2:]
    if c == "01":
        tmp += "0"
    elif c == "10":
        tmp += "1"
    elif c == "00":
        tmp += "0"
    elif c == "11":
        tmp += "1"
    else:
        print("++")
    if len(a) <= 0:
        break
# print(tmp)
# s =""
# print(int("00000000000000001000000000110100000001111101100111110101010101010110000",16))
#
# s= "401a03ecfaaab0"
s="7fffbfe5fc13040000"
import binascii
print(binascii.b2a_hex())