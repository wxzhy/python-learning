#********* Begin *********#
import turtle as t

#绘制右上弧段
t.circle(100,87)

#绘制左上弧段
t.pu();t.home();t.pd()  #通过home()函数，将海龟移动到画布中心位置，并且角度为0度
t.seth(180)
t.circle(-100, 87)

#绘制右下弧段
t.pu();t.home();t.pd()
t.seth(180)
t.circle(100, -87)

#绘制左下弧段
t.pu();t.home();t.pd()
t.circle(-100, -87) 
#********* End *********#
#保存屏幕图片
ts = t.getscreen()
ts.getcanvas().postscript(file="step4/sj.ps")
