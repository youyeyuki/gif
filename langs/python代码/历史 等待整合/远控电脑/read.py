# -*- coding:utf-8 -*-
# __author__ = 'Wings'

import base64
import getpass, imaplib
import email

M = imaplib.IMAP4('imap.163.com')
M.login('youyeadmin@163.com', 'hskdvjczijdijzix')
print M.select()
typ, data = M.search('utf-8', 'ALL')
msgList = data[0].split()
typ, data = M.fetch(msgList[0], '(RFC822)')
msg = email.message_from_string(data[0][1])
content = msg.get_payload(decode=True)
print content
# 更正 暂时英文能获取 中文还不行
M.close()
M.logout()

# 官方例子
# M = imaplib.IMAP4('imap.163.com')
# M.login('user', 'passwd')
# print M.select()
# typ, data = M.search('utf-8', 'ALL')
# for num in data[0].split():
#     typ, data = M.fetch(num, '(RFC822)')
#     print 'Message %s\n%s\n' % (num, data[0][1])
# M.close()
# M.logout()


# 以下是pop3 7bitdecode失败 不能继续进行 使用imp4进行 下一步
# import poplib  # 收取邮件
# import mimetools
# from email.header import decode_header
#
#
# readEmail = poplib.POP3('pop.163.com')
# readEmail.user('youyeadmin@163.com')
# readEmail.pass_('hskdvjczijdijzix')
# ret = readEmail.stat()  # 返回邮箱的基本信息 第一个邮件数目  第二个是邮箱的字节数
# myMessage = readEmail.top(ret[0], 0)
# a = myMessage[1]
#
# for i in a:
#     print i
#


# print a
# for i in range(1, ret[0]+1):
#     mlist = readEmail.top(i, 0)
#     print 'line: ', len(mlist[1])
#
#
# ret = readEmail.list()
# print ret
# # 取第一封邮件完整信息，在返回值里，是按行存储在down[1]的列表里的。down[0]是返回的状态信息
# down = readEmail.retr(1)
# print 'lines:', len(down)
#
# for line in down[1]:
#     print line
#readEmail.quit()



