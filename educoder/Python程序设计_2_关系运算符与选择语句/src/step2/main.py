#***Begin your code here***#
a,b,c = list(map(int, input().split()))
lst=sorted([a,b,c])
lst.reverse()
for i in lst:
    print(i,end=' ')

#***End your code here***#