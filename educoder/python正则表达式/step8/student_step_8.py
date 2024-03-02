# coding=utf-8

import re

input_str = input()

# 1、编写获取到数字的正则，并输出匹配到的信息
########## Begin ##########
r1=re.findall(r'[0-9]',input_str)
print(r1)

########## End ##########

# 2、编写获取到不是数字的正则，并输出匹配到的信息
########## Begin ##########
r2=re.findall(r'[^0-9]',input_str)
print(r2)

########## End ##########



