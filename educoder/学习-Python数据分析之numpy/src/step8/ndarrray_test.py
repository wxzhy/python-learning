import numpy as np
# 请在下面的 Begin-End 之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 过滤出 input 函数获取的列表中的所有的大写字母，并以列表的形式返回过滤掉的大写字母
arr=np.array(eval(input()))
print(arr[(arr>='A') & (arr<='Z')])

########## End ##########
