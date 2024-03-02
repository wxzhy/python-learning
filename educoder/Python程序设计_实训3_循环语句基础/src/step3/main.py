#********** Begin **********#
s=input()
x=""
for c in s:
    if int(c)%2==0:
        x+=c
if len(x)>0:
    x=int(x[::-1])
    print(x//2)
else:
    print("0")



#********** End **********#