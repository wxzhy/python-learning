# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd
import pandas_2 as pd2
def test_pandas1():
    a=pd2.create_dataframe()
    test1=input()
    if(test1=='index'):
        if(set(a.keys())==set(['new_add','pops','years', 'states'])):
            print ("True")
        else:
            print ("False")
    if(test1=='column'):
        if set(a.index)==set(['four', 'three', 'five', 'two', 'one']):
            print ('True')
        else:
            print ("False")
    if(test1=='new_add'):
        if list(a['new_add'])==[7, 4, 5, 8, 2]:
            print ("True")
        else:
            print ("False")
test_pandas1()