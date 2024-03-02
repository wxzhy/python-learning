def get_md5(file_name):
    m1 = hashlib.md5()   
    f1 = open(file_name, 'rb')
    m1.update(f1.read())   
    f1.close()
    return m1.hexdigest()


import stud_pd1
import hashlib   

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='simHei' #显示汉字
plt.rcParams['axes.unicode_minus'] = False  #显示负号
def check(file1, file2):
    code1 = get_md5(file1)
    code2 = get_md5(file2)
    print('结果正确') if code1==code2 else print('结果错误')
import pandas as pd
data=pd.read_excel('学生成绩表.xlsx')
def f1_t(outfile):
############begin###########################
#显示平均分<60的所有人员信息，填写代码开始
    da1=data[data.平均分<60]
##########end###############################
    da1.to_excel(outfile)
def f2_t(outfile):
############begin###########################
#显示数学分>=90的所有人员信息，填写代码开始
    da2=data.loc[data.数学>=90, '姓名':'数学' ] 
##########end###############################
    da2.to_excel(outfile)
def f3_t(outfile):
############begin###########################
#显示2,3,8行1,3列的信息，填写代码开始
    da3=data.iloc[ [2,3,8], [1,3]]
##########end###############################
    da3.to_excel(outfile)
path_s='a1_1.xlsx'
stud_pd1.f1(path_s)
path_t='a1_1_t.xlsx'
f1_t(path_t)
check(path_s, path_t)
    

path_s='a1_2.xlsx'
stud_pd1.f2(path_s)
path_t='a1_2_t.xlsx'
f2_t(path_t)
check(path_s, path_t)


path_s='a1_3.xlsx'
stud_pd1.f3(path_s)
path_t='a1_3_t.xlsx'
f3_t(path_t)
check(path_s, path_t)

