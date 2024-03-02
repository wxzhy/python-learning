#********* Begin *********#
import turtle as t
t.pencolor('brown')
t.pensize(3)
t.fillcolor('orange')
t.begin_fill()
t.circle(30,360)
t.end_fill()
t.circle(60,360)
t.circle(120,360)




#********* End *********#
#保存屏幕图片
ts = t.getscreen()
ts.getcanvas().postscript(file="step3/sj.ps")
