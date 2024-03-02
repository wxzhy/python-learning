import turtle
#********* Begin *********#
turtle.pencolor('red')
turtle.fd(200)
turtle.lt(120)
turtle.fd(200)
turtle.lt(120)
turtle.fd(200)




#********* End *********#
#保存屏幕图片
ts = turtle.getscreen()
ts.getcanvas().postscript(file="Python/src1/py1-1/yourimg/sj.ps")