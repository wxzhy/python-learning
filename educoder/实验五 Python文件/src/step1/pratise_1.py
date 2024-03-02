# 判断两个文件是否相同。要求用函数实现文件比较功能，在main函数中进行验证。
# 下述函数完成文件是否相同的比较功能
def compareFile(file1,file2):

    #请在此添加代码，实现文件是否相同的判断
    # 如果相等返回[1,0,0]
    # 如果不相等返回[0,a,b] a,b表示第一个不相等字符所在的行号和列号
    #********** Begin *********#
    f1=open(file1,encoding='utf-8')
    f2=open(file2,encoding='utf-8')
    l1=f1.readlines()
    l2=f2.readlines()
    if l1==l2:
        return [1,0,0]
    else:
        for a in range(max(len(l1),len(l2))):
            if l1[a]!=l2[a]:
                for b in range(max(len(l1[a]),len(l2[a]))):
                    if l1[a][b]!=l2[a][b]:
                        return [0,a+1,b+1]



    #********** End *********#

# 定义函数main，完成文件名输入、比较函数调用和结果输出功能
def main():
    # 输入两个文件所在路径和文件名，如：d:\temp\t1.txt
    str1=input('')
    str2=input('')
    #请在此添加代码，完成相应功能
    #********** Begin *********#
    r=compareFile(str1,str2)
    if r[0]==1:
        print("这两个文件相等")
    else:
        print("这两个文件在%d行%d列开始不相等"%(r[1],r[2]))



    #********** End *********#

main()




