# coding=utf-8

import re

input_str = input()
# 1、基于贪心模式匹配字符串中重复出现2个数字的子字符串，并存储到变量a。

########## Begin ##########

a=re.findall(r'[\d]{2}',input_str)
########## End ##########
print(a)

# 2、基于贪心模式匹配字符串中重复出现4-7个数字的子字符串，并存储到变量b。
########## Begin ##########
b=re.findall(r'[\d]{4,7}',input_str)

########## End ##########
print(b)


