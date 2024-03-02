# coding = utf-8
data=input() #从键盘输入一个5位数
# 请在下面添加代码
###### Begin ######
x1=int(data)
x2=int(data[::-1])
if x1==x2:
    print("%d是回文数"%x1)
else:
    print("%d不是回文数"%x1)



####### End #######