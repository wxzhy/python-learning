# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd
import pandas_1 as pd1


def test_pandas1():
    str1=input()
    a,b,c=pd1.create_series()
    if(str1=="Series_a"):
        if(a.equals(Series([1,2,5,7],index=['nu','li','xue','xi']))==1):
            print ("Series_a is true")
            #       a.all()==Series([1,2,5,7],index=['nu','li','xue','xi'])):

        else:
            print ("Series_a is false")
    if (str1 == "dict_a"):
        if (b == {"ting":1,"shuo":2,"du":32,"xie":44}):
            print ("dict_a is true")
        else:
            print ("dict_a is false")

    if(str1 == "Series_b"):
        if (c.equals(Series(b))==1):
            print ("Series_b is true")
        else:
            print ("Series_b is false")

test_pandas1()