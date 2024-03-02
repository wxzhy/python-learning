# coding=utf-8

import re

input_str = input()

# 1、编写获取到以educoder开头的正则，并存储到变量a
########## Begin ##########
a=re.search(r'^educoder',input_str)

########## End ##########
if a is not None:
    print(a.span())
else:
    print(a)


# 2、编写获取到以educoder结束的正则，并存储到变量b
########## Begin ##########
b=re.search(r'educoder$',input_str)

########## End ##########
if b is not None:
    print(b.span())
else:
    print(b)


