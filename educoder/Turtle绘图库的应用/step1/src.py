#********* Begin *********#
import turtle as t
t.pencolor('brown')
t.pensize(5)
t.fillcolor('yellow')
t.begin_fill()
for i in range(9):
    t.fd(100)
    t.lt(40)
t.end_fill()



#********* End *********#
#保存屏幕图片
ts = t.getscreen()
ts.getcanvas().postscript(file="step1/sj.ps")
