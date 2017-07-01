# -*- coding:utf-8 -*-
__author__ = 'Wings'

print "输入表名"
table_name = raw_input()

#直接以逗号隔开输入
print "输入字段值 并以逗号隔开 注意是英文符号的逗号"
filed = raw_input()
filed = filed.split(",")

print "输入插入的数据 并以逗号隔开 注意是英文符号的逗号"
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

#留空白相加
update_values = ""
for i in range(0, len(filed)):
    update_values = update_values+filed[i]+equal+single_quote+values[i]+single_quote+comma

update_values =update_values[:-1]

where_code = "WHERE "+left_bracket+key+equal+single_quote+key_data+single_quote+right_bracket+semicolon

update_values = insert_first+update_values+where_code

print update_values
