import os
# 更改pandas环境版本，因日志太多输入到文件不显示
os.system("pip3 install pandas==0.23.0 -i https://mirrors.cernet.edu.cn/pypi/web/simple > 123.txt")

import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None

# 请在此添加代码，分别打印f500的类型和形状大小
#********** Begin **********#
f500_type=type(f500)
f500_shape=f500.shape
print(f500_type)
print(f500_shape)
#********** End **********#