# coding = utf-8
data=input()
# 补全每一步的代码，实现字符串的反转
#第一步，将字符串转换为列表
lst=[a for a in data]
#第二步：将列表反转
lst.reverse()
#第三步：用join方法返回一个新字符串，该字符串由将反转后的列表的每一个元素组成，元素间用''分割
str=''.join(lst)
#第四步：输出新的字符串
print(str)