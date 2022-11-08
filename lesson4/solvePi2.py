from random import random
from math import sqrt as Sqrt
from time import process_time as Clk
DARTS = 1000
hits = 0.0
Clk()
for i in range(1,DARTS+1):
    x,y = random(), random()
    dist = Sqrt(x ** 2 + y ** 2)
    if dist <= 1.0:
        hits - hits + 1
pi = 4 * (hits/DARTS)
print("Pi is {:.5f}".format(pi))
print("Time is {:5f}s".format(Clk()))