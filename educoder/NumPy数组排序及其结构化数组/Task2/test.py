import numpy as np
def studen(file_name):
    '''
    读取文件内容转换为结构化数组并筛选年龄在10岁之上的平均score
    :return: None
    '''
    # ********* Begin *********#
    data=np.loadtxt(file_name,dtype=[("name","S10"),("age","<i4"),("score","<f4")],skiprows=1)
    data=data[data['age']>10]['score']
    print("%.1f"%data.mean())
    # ********* End *********#

