import os
# 更改pandas环境版本，因日志太多输入到文件不显示
os.system("pip3 install pandas==0.23.0 -i https://mirrors.cernet.edu.cn/pypi/web/simple > 123.txt")

import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None

# 请在此添加代码
#********** Begin **********#
industries=f500['industry']
industries_type=type(industries)
countries=f500['country']
revenues_years=f500[['revenues','years_on_global_500_list']]
ceo_to_sector=f500.loc[:,'ceo':'sector']
print(industries_type)
print(countries)
print(revenues_years)
print(ceo_to_sector)


#********** End **********#