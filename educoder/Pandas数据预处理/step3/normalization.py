import numpy as np
import pandas as pd


# 该函数读取step3/data1.csv和step3/data2.csv文件并返回需要输出的结果
def data_process():
    # ********** Begin *********#

    df1 = pd.read_csv('step3/data1.csv')
    df2 = pd.read_csv('step3/data2.csv')
    df = pd.merge(df2, df1, on=['airline','avail_seat_km_per_week'], how='outer')
    df=df.fillna(0)
    d1=df['fatal_accidents_00_14']
    d1=(d1-min(d1))/(max(d1)-min(d1))
    d2=df['fatal_accidents_85_99']
    d2=(d2-min(d2))/(max(d2)-min(d2))
    df['fatal_accidents_00_14']=d1
    df['fatal_accidents_85_99']=d2
    pivot=pd.pivot_table(df,index=['airline','avail_seat_km_per_week'],values=['fatal_accidents_00_14','fatal_accidents_85_99'])
    return pivot

# ********** End **********#


if __name__ == '__main__':
    print(data_process())
