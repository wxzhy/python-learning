import numpy as np

np.random.seed(233)     # 请勿修改随机种子
# 请在下面的 Begin-End 之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 使用 input 获取列表，并打乱列表的顺序
arr=np.array(eval(input()))
arr=np.random.choice(a=arr,size=len(arr),replace=False)
print(list(arr))


########## End ##########
