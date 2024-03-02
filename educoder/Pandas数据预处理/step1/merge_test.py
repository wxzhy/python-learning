import pandas as pd
import numpy as np


def data_merge():
    raw_data_1 = {
        "subject_id": ["1", "2", "3", "4", "5"],
        "first_name": ["Alex", "Amy", "Allen", np.nan, np.nan],
        "last_name": ["Anderson", "Ackerman", "Ali", "Aoni", "Atiches"]}

    raw_data_2 = {
        "subject_id": ["4", "5", "6", "7", "8"],
        "first_name": ["Billy", "Brian", "Bran", "Bryce", "Betty"],
        "last_name": ["Bonder", "Black", "Balwner", "Brice", "Btisan"]}

    raw_data_3 = {
        "subject_id": ["1", "2", "3", "4", "5", "7", "8", "9", "10", "11"],
        "test_id": [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

    # ********** Begin *********#
    df1 = pd.DataFrame(raw_data_1)
    df2 = pd.DataFrame(raw_data_2)
    df3 = pd.DataFrame(raw_data_3)
    print(pd.merge(df1, df2, on='subject_id', how='left'))
    # print('----------------------------------------------------------')
    print(pd.concat([df1, df3],axis=1,join='inner'))
    # print('----------------------------------------------------------')
    print(df1.combine_first(df2))
    # ********** End **********#


if __name__ == '__main__':
    data_merge()