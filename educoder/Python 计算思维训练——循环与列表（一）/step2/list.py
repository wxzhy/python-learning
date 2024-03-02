#请验证输入的列表N_list中的整数是否为三位数，并返回三位数整数的百位数值

N_list = [int(i) for i in input().split(',')]

#   请在此添加实现代码   #
# ********** Begin *********#
l=[]
for i in N_list:
    if i>=100 and i<1000:
        l.append(i//100)
print(l)




# ********** End **********#
