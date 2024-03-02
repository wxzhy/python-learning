# coding:utf-8 
from math import sqrt

a = float(input()); b = float(input()); c = float(input())

def roots(a,b,c):
#请在此添加代码，求方程 ax^2+bx+c = 0的解,返回由方程根构成的列表,若方程有无数解，返回['inf']
#********** Begin *********#
    delta=b*b-4*a*c
    if delta>0:
        x1=(-b+sqrt(delta))/(2*a)
        x2=(-b-sqrt(delta))/(2*a)
        lst=[x1,x2]
        return lst
    elif delta==0:
        x=-b/(2*a)
        lst=[x]
        return lst
    else:
        return []


#********** End **********#
print (roots(a,b,c))
