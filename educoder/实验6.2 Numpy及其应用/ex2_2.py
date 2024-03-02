# -*- coding: utf-8 -*-
import numpy as np
n,m=map(int,input().split(' '))
np.random.seed(7)
a=[np.random.randint(1,100) for i in range(n*m)]
b=np.array(a).reshape(n,m)
row,col=1,1
maxx=b[0,0]
###################begin################
#在此填写代码
for i in range(n):
    for j in range(m):
        if b[i,j]>maxx:
            maxx=b[i,j]
            row=i+1
            col=j+1


#############end################
print("最大值为：%d" %maxx)
print("所在位置为：%d行%d列" %(row,col))





