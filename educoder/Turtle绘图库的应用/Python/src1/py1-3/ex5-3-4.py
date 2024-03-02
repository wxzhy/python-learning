import turtle as t
#********* Begin *********#
t.pencolor('red')
t.fd(200)
t.lt(120)
t.fd(200)
t.lt(120)
t.fd(200)
t.bk(100)
t.lt(60)
t.pencolor('blue')
t.fillcolor('yellow')
t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()
t.bk(50)
t.lt(60)
t.pencolor('red')
t.fillcolor('white')
t.begin_fill()
t.fd(50)
t.lt(120)
t.fd(50)
t.lt(120)
t.fd(50)
t.end_fill()






#********* End *********#
#保存屏幕图片
ts = t.getscreen()
ts.getcanvas().postscript(file="Python/src1/py1-3/yourimg/sj.ps")
