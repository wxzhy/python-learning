# coding:utf-8 

counter = 0

def access():
#请在此添加代码，实现counter的调用，每次调用counter的值加1
#********** Begin *********#
    global counter
    counter+=1

#********** End **********#
  
for i in range(5):
  access()
  
print (counter)
