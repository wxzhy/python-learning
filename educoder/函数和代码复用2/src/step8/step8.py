# coding:utf-8


Lst = input()
Lst = Lst.split(',')

def abs_sum(L):
#请在此添加代码，以递归的方式设计函数abs_sum(L)返回列表L（假设其中全是整数）中所有整数绝对值之和
#********** Begin *********#
    if len(L)==1:
        return abs(int(L[0]))
    else:
        return abs(int(L[0]))+abs_sum(L[1:])


#**********  End  *********#

print(abs_sum(Lst))
