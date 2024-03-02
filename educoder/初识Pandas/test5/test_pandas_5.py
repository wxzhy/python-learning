# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
import pandas_5 as pd5
def test_pandas1():
    str1=input()
    a,b=pd5.delete_data()
    if(str1=="s1"):
        if(list(a.index)==['v','x','y']):
            print ("True")
        else:
            print ("False")
    if (str1 == "d1"):
        if (list(b.columns)==['xx','zz']):
            print ("True")
        else:
            print ("False")

test_pandas1()