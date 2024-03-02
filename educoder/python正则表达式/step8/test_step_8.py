# coding=utf-8

import re

input_str = input()

# 1、编写获取到数字的正则，并输出匹配到的信息
###### Begin ######
a = re.findall(r'[0-9]', input_str)
print(a)
####### End #######

# 2、编写获取到不是数字的正则，并输出匹配到的信息
###### Begin ######
b = re.findall(r'[^0-9]', input_str)
print(b)
####### End #######



