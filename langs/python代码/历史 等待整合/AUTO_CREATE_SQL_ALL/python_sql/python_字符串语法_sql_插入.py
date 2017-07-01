# -*- coding:utf-8 -*-
__author__ = 'Wings'
def add_(str_data):
    str_data = "\""+str_data+"\""
    return str_data

print "输入表名"
table_name = raw_input()

#直接以逗号隔开输入
print "输入字段值 并以逗号隔开 注意是英文符号的逗号"
filed = raw_input()

print "输入插入的数据的变量 并以逗号隔开 注意是英文符号的逗号"
values = raw_input()
values = values.split(",")

insert = "INSERT INTO " +table_name

left_bracket ="("

right_bracket =") "

plus = "+"
comma = ","

semicolon =";"

single_quote = "'"

insert = insert+ left_bracket+filed+right_bracket+"VALUES"
#a,b,c是变量
a ="a"
b = "b"
c = "c"
#留空白相加
insert_values = ""
for each in values:
    insert_values = insert_values+add_(single_quote)+plus+each+plus+add_(single_quote)+plus+add_(comma)+plus
insert_values = insert_values[:-1]
insert_values = insert_values[:-1]
insert_values = insert_values[:-1]
insert_values = insert_values[:-1]
insert_values = insert_values[:-1]

print  insert_values


sql_insert = add_(insert) + plus+add_(left_bracket)+plus+insert_values+plus+add_(right_bracket)+plus+add_(semicolon)

print "python插入sql语句是"
print sql_insert


