# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd
import pandas_3 as pd3
def test_pandas1():
    str1=input()
    a,b=pd3.read_csv_data()
    if(str1=="columns"):
        if(list(a.columns)==['water_year','rain_octsep','outflow_octsep','rain_decfeb', 'outflow_decfeb', 'rain_junaug', 'outflow_junaug']):
            print ("True")
        else:
            print ("False")
    if (str1 == "length1"):
        if (b == len(a)):
            print ("True")
        else:
            print ("False")
test_pandas1()