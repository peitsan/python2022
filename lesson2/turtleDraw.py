#e2.1Drawpython.py
# from turtle import *
import turtle as tl
tl.setup(650, 350, 200, 200)
tl.penup()
tl.fd(-250)
tl.pendown()
tl.pensize(25)
tl.pencolor("purple")
tl.seth(-40)
for i in range(4):
    tl.circle(40, 80)
    tl.circle(-40, 80)
tl.circle(40, 80/2)
tl.fd(40)
tl.circle(16, 180)
tl.fd(40 * 2/3)