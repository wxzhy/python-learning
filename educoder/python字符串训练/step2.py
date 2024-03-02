
str1 = "apple,pear,peach,banana,pear"
lst1 = ["apple","pear", "peach", "banana", "pear"]
###begin
print(str1.index('pear'),str1.rindex('pear'),str1.index('p'),str1.count('p'))
print(str1.split(','))
print(str1.split(' '))
print(str1.partition(','))
print(str1.partition(' '))
print(':'.join(lst1))
print('?'.join(lst1))


###end