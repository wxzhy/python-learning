# coding=utf-8

import re

input_str = input()

# 编写获取(任意字符)+ython的字符串，并存储到变量a中
########## Begin ##########
a=re.findall(r'.ython',input_str)

########## End ##########
print(a)
