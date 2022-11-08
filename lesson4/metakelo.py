import random
from math import sqrt as Sqrt           #引入math库中的开方函数
from time import process_time as Clk    #引入计时器
DARTS = int(input())                #输入一个样本数字
hits = 0.0
random.seed(123)                  #设定随机数种子
Clk()                              #开始记时
for i in range(1,DARTS+1):
    x,y = random.random(), random.random()  #生成随机坐标
    dist = Sqrt(x ** 2 + y ** 2)   #计算随机生成坐标点到圆心的距离为
    if dist <= 1.0:             #限制随机生成坐标点离圆心距离为2（限制在圆内）
       hits += 1               #随机点计数器
pi = 4 * (hits/DARTS)         #根据圆形面积pi*R^2与正方形面积R^2 四分之一圆形与4分之一正方形 的比例为 (pi*R^2)/4 / 0.5R*0.5R = pi/4
print("{:.6f}".format(pi))   #打印圆周率结果
    # print("Time is {:5f}s".format(Clk()))  #打印程序运行耗时