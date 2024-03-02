###begin
import string
p=input()
b=[False,False,False,False]
if len(p)<6:
    print("密码过于简单。")
else:
    for i in p:
        if i in string.ascii_uppercase:
            b[0]=True
        elif i in string.ascii_lowercase:
            b[1]=True
        elif i in string.digits:
            b[2]=True
        else:
            b[3]=True
    c=b.count(True)
    if c==4:
        print("密码强度强。")
    elif c>=2:
        print("密码强度中。")
    else:
        print("密码强度弱。")




###end