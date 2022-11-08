import math as m
pi = 0
k = 0
while len(str(pi))<16:
    pi += (1/m.pow(16,k))*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
    k += 1
print(pi)

