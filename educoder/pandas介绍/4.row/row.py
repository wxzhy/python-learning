import os
# 更改pandas环境版本，因日志太多输入到文件不显示
os.system("pip3 install pandas==0.23.0 -i https://mirrors.cernet.edu.cn/pypi/web/simple > 123.txt")

import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None

# 请在此添加代码
#********** Begin **********#
toyota=f500.loc['Toyota Motor']
drink_companies=f500.loc[['Anheuser-Busch InBev','Coca-Cola','Heineken Holding']]
middle_companies=f500.loc['Tata Motors':'Nationwide','rank':'country']
print(toyota)
print(drink_companies)
print(middle_companies)


#********** End **********#