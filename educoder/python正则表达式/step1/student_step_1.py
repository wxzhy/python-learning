# coding=utf-8

# 在此导入python正则库
########## Begin ##########
import re

########## End ##########

check_name = input()
# 在此使用正则匹配'张明'的信息，结果存储到is_zhangming中
########## Begin ##########
is_zhangming=re.search(r'张明',check_name)

########## End ##########

if is_zhangming is not None:
    print(is_zhangming.span())
else:
    print(is_zhangming)
