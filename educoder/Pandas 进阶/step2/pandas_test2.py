#-*- coding: utf-8 -*-
import pandas as pd

#创建透视表
def create_pivottalbe(data):
    ###### Begin ######
    pivot=data.pivot_table(values=['tip'],index=['day'],columns=['time'],margins=True,aggfunc=sum)
    return pivot
    ###### End ######

#创建交叉表
def create_crosstab(data):
    ###### Begin ######
    cross=pd.crosstab(values=data['tip'],index=data['day'],columns=data['time'],margins=True,aggfunc=sum)
    return cross
    ###### End ######

def main():
    #读取csv文件数据并赋值给data
    ###### Begin ######
    data=pd.read_csv('step2/tip.csv')
    ###### End ######
    piv_result = create_pivottalbe(data)
    cro_result = create_crosstab(data)
    print("透视表：\n{}".format(piv_result))
    print("交叉表：\n{}".format(cro_result))

if __name__ == '__main__':
    main()
