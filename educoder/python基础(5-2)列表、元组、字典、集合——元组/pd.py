#此部分为读入订单测试数据到list1中
list1 = []
while True:
    try:
        order= input()
        list1.append(order)
    except:
        break

##########  Begin  #########
#（1）定义元组，将list1中元素按顺序去掉重复值并保存在元组中，输出整个元组


#（2）查找最大当日订单数，并输出年月日：格式如下：180101
tup=()
cnt=()
for i in list1:
    if i not in tup:
        tup+=(i,)
        cnt+=(int(i[-3:]),)
print(tup)
index=cnt.index(max(cnt))
print(tup[index][:6])
##########  End  #########