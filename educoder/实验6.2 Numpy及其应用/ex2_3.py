# -*- coding: utf-8 -*-
#输出n行的杨辉三角形
import numpy as np
n=int(input())
a=[0]*n**2
b=np.array(a ).reshape(n,n)
for i in range(n):
    b[i,0]=1
    b[i,i]=1
############begin###########################
#填写代码开始
for i in range(n):
    for j in range(i+1):
        if b[i,j]==0:
             b[i][j]=b[i-1][j-1]+b[i-1][j]
for i in range(n):
    print('   '*(n-i-1),end='')
    for j in range(i):
        print('%3d'%b[i,j],end='   ')
    print('%3d'%b[i,i])
##########end###############################



