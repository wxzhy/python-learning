# 本程序要求返回算到N_list列表中每一项时的圆周率值，并用列表进行存储，最终输出列表结果

N_list = [int(i) for i in input().split(',')]

#   请在此添加实现代码   #
# ********** Begin *********#
l=[]
pi=0.0
for i in range(1,N_list[-1]+1,2):
    if i%4==3:
        pi-=1/i
    else:
        pi+=1/i
    if i in N_list:
        l.append("%.8f"%(pi*4))
print(l)




# ********** End **********#
