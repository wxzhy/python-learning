# ***Begin your code here***#
from ipaddress import summarize_address_range


s = input()
sum = 0
if len(s) == 3:
   for c in s:
       sum += int(c)**3
   if sum == int(s):
        print("narcissistic")
   else:
        print("neither")
elif len(s)==4:
    for c in s:
        sum+=int(c)**4
    if sum==int(s):
        print("rose")
    else:
        print("neither")
else:
    print("neither")
#***End your code here***#