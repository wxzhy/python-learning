# coding:utf-8
from math import sqrt

a=float(input()); b=float(input()); c=float(input())

def roots(a, b, c):
#请在此添加代码，在a不等于0的情况下编写函数求解方程的两个根并将根返回
#********** Begin *********#
    delta=b*b-4*a*c
    tup=()
    if delta>0:
        x1=(-b+sqrt(delta))/(2*a)
        x2=(-b-sqrt(delta))/(2*a)
        tup+=(x1,x2)
    elif delta==0:
        x=-b/(2*a)
        tup+=(x,x)
    return tup
        



#********** End **********#

if a != 0:
  print (roots(a,b,c))
