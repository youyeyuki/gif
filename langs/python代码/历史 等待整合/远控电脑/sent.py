# -*- coding:utf-8 -*-
import poplib  # 收取邮件
import smtplib  # 发送邮件
from email.header import decode_header
from email.mime.text import MIMEText  # 设置邮件内容
import email

# 登录邮箱

sentMail = smtplib.SMTP('smtp.163.com')
sentMail.login('youyeadmin@163.com', 'hskdvjczijdijzix')

# 发送邮件
toEmail = ['youyeadmin@163.com', '1593808367@qq.com']
content = MIMEText('I am you~~~ ')   # 邮件内容
content['Subject'] = 'youyeadmin'    # 标题
content['From'] = 'youyeadmin@163.com'
content['To'] = ','.join(toEmail) # 把列表的元素用，隔开 邮件发送地址
sentMail.sendmail('youyeadmin@163.com', toEmail, content.as_string()) # 用as_string方式发
sentMail.close()
print content['To']
