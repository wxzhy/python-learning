# coding=utf-8

import re

input_str = input()
# 1、基于贪心模式匹配字符串中连续出现5个数字以上的子字符串，并存储到变量a。

########## Begin ##########
a=re.findall(r'[\d]{5,}',input_str)

########## End ##########
print(a)

# 2、匹配字符串中都为数字的子字符串，并存储到变量b。
########## Begin ##########
b=re.findall(r'[\d]+',input_str)

########## End ##########
print(b)

