#此部分为读入测试数据到list1中
list1 = []
while True:
    try:
        item= input()
        list1.append(item)
    except:
        break

######### Begin ##########
#将读入的list1转换为tup并整体打印
tup=()
for c in list1:
    tup+=(c,)
print(tup)


##########  End  #########