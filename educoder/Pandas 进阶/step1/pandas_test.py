import pandas as pd
import numpy as np

#返回最大值与最小值的差
def sub(df):
    ######## Begin #######
    return df.max()-df.min()
    ######## End #######

def main():
    ######## Begin #######
    df=pd.read_csv('step1/drinks.csv')
    dc={'wine_servings':sub,'beer_servings':np.sum}
    print(df.groupby('continent').agg(dc))

    ######## End #######

if __name__ == '__main__':
    main()