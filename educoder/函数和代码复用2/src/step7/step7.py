# coding:utf-8
import random
from functools import reduce

n = input()  # useless
n = random.randint(5,10)
L = []
for i in range(n):
 L.append(random.randint(1,n))
 
def sum_of_paras(*arg):
#请在此添加代码，返回参数列表 arg 中所有数的和
#********** Begin *********#


#**********  End  *********#
    
strcall = "sum_of_paras(";
strcall += reduce(lambda x, y: x+","+y, [str(s) for s in L])
strcall +=")"

if eval(strcall) == sum(L):
  print("Y")
else:
  print("N")
