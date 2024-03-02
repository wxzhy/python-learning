# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
import pandas_6 as pd6
def test_pandas1():
    str1=input()
    a=pd6.add_way()
    if(str1=="add"):
        if(int(a.ix[0]['e'])==8):
            print ("True")
        else:
            print ("False")

test_pandas1()