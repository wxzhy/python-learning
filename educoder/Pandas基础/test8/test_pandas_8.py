# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
import pandas_8 as pd8
def test_pandas1():
    str1=input()
    a=pd8.suoying()
    if(str1=="Stack"):
        if(list(a.index)==['a','b','c','d'] and list(a.columns)==[1,2,3]):
            print ("操作成功")
        
        else:
            print ("操作失败")


test_pandas1()