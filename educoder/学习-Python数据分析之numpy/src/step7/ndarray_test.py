import numpy as np

# 请在下面的 Begin-End 之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 根据输入的数据筛选出大于指定数值的值
arr=np.array(eval(input()))
n=eval(input())
arr=arr.reshape((1,-1))
print(arr[arr>n])


########## End ##########
