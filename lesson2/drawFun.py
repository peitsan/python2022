#e.2.3DrawPython.py
import turtle as t
def drawSnake(rad,ang,length):
    t.seth(-40)
    for i in range(length):
        t.circle(rad,ang)
        t.circle(-rad,ang)
    t.circle(rad,ang/2)
    t.fd(40)
    t.circle(16,180)
    t.fd(40*2/3)
t.setup(650,350,200,20)
t.penup()
t.fd(-250)
t.pendown()
t.pensize(25)
t.pencolor("purple")
drawSnake(40,80,4)
t.done