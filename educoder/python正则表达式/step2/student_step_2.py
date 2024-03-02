# coding=utf-8

import re

input_str = input()

# 编写获取python和Python的正则，并存储到match_python变量中

########## Begin ##########
match_python=re.findall(r'[Pp]ython',input_str)

########## End ##########

print(match_python)

