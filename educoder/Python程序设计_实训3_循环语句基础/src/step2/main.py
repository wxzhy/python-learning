#********** Begin **********#
s=input()
lst=s.split(' ')
l=int(lst[0])
x=0
for i in range(l):
    x+=int(lst[1+i])*10**(l-i-1)
y=int(lst[-1])
print(x%y)


#********** End **********#