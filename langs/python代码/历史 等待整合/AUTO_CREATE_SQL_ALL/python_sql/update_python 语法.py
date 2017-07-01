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
filed = filed.split(",")

print "输入插入的变量 并以逗号隔开 注意是英文符号的逗号"
values = raw_input()
values = values.split(",")

print "输入主键"
key =raw_input()
print  "输入主键的数据"
key_data = raw_input()

insert_first = "UPDATE " +table_name+" SET "

left_bracket ="("

right_bracket =") "

comma = ","

semicolon =";"

single_quote = "\'"

equal ="="

plus = "+"
#留空白相加
update_values = ""
for i in range(0, len(filed)):
    update_values = update_values+add_(filed[i]+equal)+plus+add_(single_quote)+plus+values[i]+plus+add_(single_quote)+plus+add_(comma)

update_values =update_values[:-1]
update_values =update_values[:-1]
update_values =update_values[:-1]
update_values =update_values[:-1]


where_code = add_(" WHERE")+plus+add_(left_bracket)+plus+key+plus+add_(equal)+plus+add_(single_quote)+plus+key_data+plus+add_(single_quote)+plus+add_(right_bracket)+plus+add_(semicolon)


update_values =add_(insert_first)+plus+update_values+plus+where_code
print "python 语句是"
print update_values

