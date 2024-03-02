# 本关的编程任务具体要求如下：
# (1)键盘中输入数据，以,隔开
# (2)输入数据放入一个列表中，并将列表转为迭代器
# (3)用next()函数遍历迭代器IterList
# (4)输出对应的值的2倍
# 预期输入：
# 5,6,7,8,9
# 预期输出：
# 10
# 12
# 14
# 16
# 18
List = []
member = input()
#请在此添加代码，将输入数据以,隔开，并存入列表
#********** Begin *********#
List=member.split(',')
List=list(map(int,List))
#********** End **********#
#请在此添加代码，将List转换为迭代器的代码
#********** Begin *********#
List=iter(List)
#********** End **********#
while True:
    try:
        #请在此添加代码，用next()函数遍历IterList的代码
        #********** Begin *********#
        print(next(List)*2)
    except StopIteration:
        break
#********** End **********#