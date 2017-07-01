# -*- coding:utf-8 -*-
__author__ = 'Wings'

print "输入表名"
table_name = raw_input()

#直接以逗号隔开输入
print "输入字段值 并以逗号隔开 注意是英文符号的逗号"
filed = raw_input()
filed = filed.split(",")

table = "CREATE TABLE " +table_name

left_bracket ="("

right_bracket =") "

val ="   varchar(100) NULL"

comma = ","

semicolon =";"

single_quote = "'"

filed_data = ""
for each in filed:
    filed_data = filed_data+each+val+comma
filed_data = filed_data[:-1]

table_create = table + left_bracket+filed_data+right_bracket+semicolon

print table_create
