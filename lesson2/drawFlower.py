import time
import turtle as t     #导入turtle库
t.setup(800,500,200,50)
t.pensize(1)           #修改画笔粗细
t.color('orange','yellow')
img = t.getscreen()
t.begin_fill()         #画布填充颜色
for i in range(36):    #循环语句
    t.fd(300)
    t.left(170)
t.end_fill()
time.sleep(5)
img.getcanvas().postscript(file='sunflower.eps')