import os
# 更改pandas环境版本，因日志太多输入到文件不显示
os.system("pip3 install pandas==0.23.0 -i https://mirrors.cernet.edu.cn/pypi/web/simple > 123.txt")

import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None

# 请在此添加代码
#********** Begin **********#
big_movers=f500.loc[['Aviva','HP','JD.com','BHP Billiton'],['rank','previous_rank']]
bottom_companies=f500.loc['National Grid':'AutoNation',['rank','sector','country']]
print(big_movers)
print(bottom_companies)

#********** End **********#