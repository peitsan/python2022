#narray
import numpy as np
n,m = map(int,input().split(" "))
arr= np.zeros(n)
arr[m-1] = 1
print(np.array([arr]))
