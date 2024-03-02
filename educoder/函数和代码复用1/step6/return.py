# coding=utf-8

# 输入两个正整数a,b
a = int(input())
b = int(input())

# 请在此添加代码，求两个正整数的最大公约数
########## Begin ##########
def gcd(a,b):
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return i



########## End ##########

# 调用函数，并输出最大公约数
print(gcd(a,b))


