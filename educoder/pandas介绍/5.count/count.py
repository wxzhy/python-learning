import os
# 更改pandas环境版本，因日志太多输入到文件不显示
os.system("pip3 install pandas==0.23.0 -i https://mirrors.cernet.edu.cn/pypi/web/simple > 123.txt")

import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None
f500_sel = f500.iloc[[0,1,2,3,4,8]]

# 请在此添加代码
#********** Begin **********#
countries=f500_sel['country']
country_counts=countries.value_counts()
print(countries)
print(country_counts)


#********** End **********#