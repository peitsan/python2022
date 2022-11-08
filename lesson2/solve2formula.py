#solve2formula.py
import math
a,b,c = map(float,input().split(' '))
delta = math.pow(b,2)-4*a*c
if(delta < 0):
    print("No")
else:
    root1 = (-b+math.pow(delta,0.5)) / (2 * a)
    root2 = (-b-math.pow(delta,0.5)) / (2 * a)
    print("{:.2f} {:.2f}".format(root1,root2))