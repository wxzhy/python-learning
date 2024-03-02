# 本程序计算小球向上斜抛在不同时间点的高度

theta = int(input())  # 单位：角度

#   请在此添加实现代码   #
# ********** Begin *********#
import math
theta = theta / 180 * math.pi
v0, g, y0, x = 25, 9.8, 1, 0.5
v0 /= 3.6
y = x * math.tan(theta) - 1 / (2 * v0) * (g * x * x) / (math.cos(theta) **2) + y0
print("y值计算结果为：%.5f米" % y)

# ********** End **********#
