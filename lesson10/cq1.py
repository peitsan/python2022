#cq1.py
import numpy as np
n = eval(input())
arr = np.zeros([n,n],dtype=np.float64)
for i in range(n):
    arr[i][i] = i+1
print(arr)

