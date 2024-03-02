import numpy as np

# 请在下面的 Begin-End 之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 完成 ndarray 对象的变形
arr=np.array(eval(input()))
arr=arr.reshape((1,-1))
arr.resize(len(arr[0]))
print(arr)

########## End ##########
