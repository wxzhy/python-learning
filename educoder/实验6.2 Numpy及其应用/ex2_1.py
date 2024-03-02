# -*- coding: utf-8 -*-
import numpy as np
#1 使用numpy的linspace函数，创建初值为1，终止为5，元素个数为5的等差数组
########## begin ##########
# 请在此填写代码
A=np.linspace(1,5,5)
########## end ##########   
print(A)

#2 将数组B变换成2行5列的二维数组
B=np.arange(0,20,2)
# 请在此填写代码
B=B.reshape(2,5)
########## end ##########   
print(B)

#3 随机数种子为8，生成2行2列的随机数数组，值在[0,1)之间
np.random.seed(8)
# 请在此填写代码
C=np.random.rand(4)
C=C.reshape(2,2)
########## end ##########   
print(C)
#4 随机数种子为11，生成3行3列的正态分布随机数数组，期望值为5，标准差为2
np.random.seed(11)
# 请在此填写代码
D=np.random.normal(5,2,9)
D=D.reshape(3,3)
########## end ##########   
print(D)

#5 使用斐波那契数列(1,1,2,3,5,...)生成一个5行4列的numpy数组，数组名为E
# 请在此填写代码
E=[1,1]
for i in range(3,21):
    E.append(E[-1]+E[-2])
E=np.array(E)
E=E.reshape(5,4)


########## end ##########   
print(E)
#6使用numpy的logspace函数，创建初值为1，终止为1000，元素个数为4的等比数组
########## begin ##########
# 请在此填写代码
G=np.logspace(0,3,4)
########## end ##########    
print(G)