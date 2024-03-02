import os
# 更改pandas环境版本，因日志太多输入到文件不显示
os.system("pip3 install pandas==0.23.0 -i https://mirrors.cernet.edu.cn/pypi/web/simple > 123.txt")

import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None
countries = f500['country']
countries_counts = countries.value_counts()

# 请在此添加代码
#********** Begin **********#
india=countries_counts['India']
north_america=countries_counts[['USA','Canada','Mexico']]
print(india)
print(north_america)

#********** End **********#