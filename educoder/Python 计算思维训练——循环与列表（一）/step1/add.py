# 本程序计算1-N整数平方的累加和

N = int(input())
#   请在此添加实现代码   #
# ********** Begin *********#
s=0
for i in range(1,N+1):
    s+=i*i
print(s)

# ********** End **********#

