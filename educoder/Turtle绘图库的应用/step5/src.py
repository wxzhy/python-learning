#********* Begin *********#
import turtle as t
t.pu()
t.pencolor('brown')
t.pensize(3)
t.fillcolor('orange')
t.pu()
t.rt(90)
t.fd(40)
t.lt(90)
t.pd()
t.begin_fill()
t.circle(40,360)
t.end_fill()
t.pu()
t.rt(90)
t.fd(40)
t.lt(90)
t.pd()
t.circle(80,360)
t.pu()
t.rt(90)
t.fd(40)
t.lt(90)
t.pd()
t.circle(120,360)





#********* End *********#
#保存屏幕图片
ts = t.getscreen()
ts.getcanvas().postscript(file="step5/sj.ps")
