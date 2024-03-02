# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
import pandas_7 as pd7
def test_pandas1():
    str1=input()
    a=pd7.delete_duplicated()
    if(str1=="duplicated"):
        if(list(a.index)==[0,2,3,5]):
            print ("True")
        else:
            print ("False")

test_pandas1()