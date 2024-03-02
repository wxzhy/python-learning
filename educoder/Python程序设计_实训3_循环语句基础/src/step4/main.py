#********** Begin **********#
s=input()
x=""
for c in range(-2,-len(s)-1,-2):
    x+=s[c]
if len(x)>0:
    x=int(x)
    r=x%2
    if r==0:
        print(x//2)
    else:
        print(x//2,r)
else:
    print(0)

#********** End **********#