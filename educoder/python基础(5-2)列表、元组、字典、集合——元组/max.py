#此部分为读入测试数据到list1中
list1 = []
while True:
    try:
        n= int(input())
        list1.append(n)
    except:
        break

##########  Begin  #########
#（1）定义元组，将list1中元素按顺序保存在元组中，输出整个元组


#（2）查找元组中最大值，输出最大值和对应下标
tu=()
for i in list1:
    tu+=(i,)
print(tu)
m=max(tu)
print(m,tu.index(m))
##########  End  #########