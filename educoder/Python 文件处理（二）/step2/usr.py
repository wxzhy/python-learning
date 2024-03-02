def Read(path):
    #解析文件内容成一个字典
    #   请在此添加实现代码   #
    # ********** Begin *********#
    d=dict()
    f=open(path)
    for e in f.readlines():
        k=e.split(':')
        d[k[0].strip()]=float(k[1].strip())
    return d



    # ********** End **********#