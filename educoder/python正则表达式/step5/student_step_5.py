# coding=utf-8

import re

input_str = input()

# 编写获取she或者he的字符串，并存储到变量a中
########## Begin ##########
a=re.findall(r's?he',input_str)

########## End ##########
print(a)
