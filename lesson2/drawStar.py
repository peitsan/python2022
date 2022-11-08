import turtle as t     #导入turtle库
t.setup(500,500,50,50)
t.pensize(8)           #修改画笔粗细
t.color('orange','yellow')
t.left(72)             #调整画笔方向到初始位置
t.begin_fill()
for i in range(5):
    t.fd(100)
    t.right(144)
    t.fd(100)
    t.left(72)
t.end_fill()
img = t.getscreen()
img.getcanvas().postscript(file='star.eps')

