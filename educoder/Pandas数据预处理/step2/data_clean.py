import pandas as pd


def clean():


# ********** Begin *********#
    df=pd.read_csv('step2/message.csv')
    df=df.dropna()
    df=df.drop_duplicates()
    #左侧添加Index
    df=df.reset_index(drop=False)
    return df

# ********** End **********#

if __name__ == '__main__':
    print(clean())