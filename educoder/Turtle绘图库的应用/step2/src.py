#********* Begin *********#
import turtle as t
for i in range(6):
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.rt(60)





#********* End *********#
#保存屏幕图片
ts = t.getscreen()
ts.getcanvas().postscript(file="step2/sj.ps")
