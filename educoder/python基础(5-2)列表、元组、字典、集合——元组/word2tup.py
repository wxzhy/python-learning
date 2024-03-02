#此部分为读入测试字符串到变量s中
s= input()

##########  Begin  #########
#将读入的s按单词转换为tup并整体打印
tup=()
for i in s.split(' '):
    tup+=(i,)
print(tup)


##########  End  #########