import numpy as np

# 请在下面的 Begin-End 之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 使用 input 获取两个列表，将列表分别转换为 ndarray 对象
a=np.array(eval(input()))
b=np.array(eval(input()))

# 计算两个 ndarray 的点积
res=np.dot(a,b)

# 打印计算后得到的 ndarray 中的最大值
print(res.max())
########## End ##########
