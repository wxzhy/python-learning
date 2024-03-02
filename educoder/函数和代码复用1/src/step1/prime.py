# coding=utf-8

# 输入一个整数n
n =  int(input())

# 请在此添加代码，对输入的整数进行判断，如果是素数则输出True，否则输出False
########## Begin ##########
if n==1:
    b=False
else:
    for i in range(2,n):
        if n%i==0:
            b=False
            break
    else:
        b=True
print(b)



########## End ##########

