# coding=utf-8

import re

input_str = input()

# 1、编写获取到单词的正则，并输出匹配到的信息
########## Begin ##########
r1=re.findall(r'\w',input_str)
print(r1)

########## End ##########

# 2、编写获取到不是单词的正则，并输出匹配到的信息
########## Begin ##########
r2=re.findall(r'\W',input_str)
print(r2)

########## End ##########



