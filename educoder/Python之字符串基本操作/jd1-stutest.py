s1="我住长江头，君住长江尾。日日思君不见君，共饮长江水。此水几时休，此恨何时已。只愿君心似我心，定不负相思意。"
#求s1的长度
n1=len(s1)
#求s1中"君"字的个数
n2=s1.count("君")
#求s1中"长江"的位置
n3=s1.find("长江")
#求s1中"黄河"的位置
n4=s1.find("黄河")
#输出统计后的结果
print(n1,n2,n3,n4)