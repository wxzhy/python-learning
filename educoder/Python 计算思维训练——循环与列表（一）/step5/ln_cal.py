# 请实现ln函数
from math import log,e,fabs

def ln(x, N=50):
    '''

    :param x: 输入值
    :param N: 迭代项数
    :return: 对数值，误差的绝对值
    '''
    #   请在此添加实现代码   #
    # ********** Begin *********#
    y=0.0
    xt=x-1
    for n in range(1,N+1):
        y+=(-1)**(n+1)/n*xt**n
    r=fabs(log(x,e)-y)
    return y,r

    # ********** End **********#

