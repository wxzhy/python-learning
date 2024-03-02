from turtle import *
#********* Begin *********#
pencolor('red')
fd(200)
lt(120)
fd(200)
lt(120)
fd(200)
bk(100)
lt(60)
pencolor('blue')
fillcolor('yellow')
begin_fill()
fd(100)
lt(120)
fd(100)
lt(120)
fd(100)
end_fill()





#********* End *********#
#保存屏幕图片
ts = getscreen()
ts.getcanvas().postscript(file="Python/src1/py1-2/yourimg/sj.ps")
