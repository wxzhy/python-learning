import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#  不要改变上面的顺序


def Draw():
    appl = "step3/AAPL.csv"  # 苹果
    google = "step3/GOOG.csv"  # 谷歌
    ms = "step3/MSFT.csv"  # 微软

    # 在此绘制折线图
    #   请在此添加实现代码   #
    # ********** Begin *********#
    appl_df = pd.read_csv(appl)
    google_df = pd.read_csv(google)
    ms_df = pd.read_csv(ms)
    appl_date = np.array(pd.to_datetime(appl_df['Date']))
    google_date = np.array(pd.to_datetime(google_df['Date']))
    ms_date = np.array(pd.to_datetime(ms_df['Date']))
    appl_open = np.array(appl_df['Open'])
    google_open = np.array(google_df['Open'])
    ms_open = np.array(ms_df['Open'])
    # 画图
    plt.plot(appl_date, appl_open, label='Apple', color='red', linewidth=1.0)
    plt.plot(google_date, google_open, label='Google', color='green', linewidth=1.0)
    plt.plot(ms_date, ms_open, label='Microsoft', color='blue', linewidth=1.0)
    plt.legend()
    plt.xticks(rotation=45)
    plt.ylabel('Open')

    # plt.show()
    # ********** End **********#

    plt.savefig("step3/output/data.png")
# 如果有必要，可以增加别的函数协助完成任务，可在此添加实现代码
# ********** Begin *********#
# ********** End **********#
