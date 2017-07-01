# -*- coding:utf-8 -*-
__author__ = 'Wings'

print "输入表名"
table_name = raw_input()

#直接以逗号隔开输入
print "输入字段值 并以逗号隔开 注意是英文符号的逗号"
filed = raw_input()

print "输入插入的数据 并以逗号隔开 注意是英文符号的逗号"
values = raw_input()
values = values.split(",")

insert = "INSERT INTO " +table_name

left_bracket ="("

right_bracket =") "


comma = ","

semicolon =";"

single_quote = "'"

insert = insert+ left_bracket+filed+right_bracket

#留空白相加
insert_values = ""
for each in values:
    insert_values = insert_values+single_quote+each+single_quote+comma

insert_values = insert_values[:-1]

insert_values = "VALUES"+left_bracket+insert_values +right_bracket+semicolon

sql_insert = insert + insert_values

print sql_insert
