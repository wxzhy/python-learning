# 请用函数实现Machin公式计算，包含隐含参数N



def arctg(x, N=5):   # 迭代项数N的缺省值是5，即如果调用时不给值就用5
    #   请在此添加实现代码   #
    # ********** Begin *********#
    r=0.0
    for n in range(1,N+1):
        r+=(-1)**(n-1)*x**(2*n-1)/(2*n-1)
    return r




    # ********** End **********#


