# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd
import os

#os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
import pandas_4 as pd4
def test_pandas1():
    str1=input()
    s2,d2=pd4.sort_gate()
    if( str1=='s2'):
        print (s2.equals(Series([4, 3, 7, 2, 8], index=['z', 'y', 'j', 'i', 'e']).sort_index()))
    if(str1 == "d2"):
        print (d2.equals(DataFrame({'e':[4,2,6,1],'f':[0,5,4,2]}).sort_values(by='f')))



test_pandas1()