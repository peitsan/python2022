n = eval(input())
def sums (n,base):
    tmp = 1
    for i in range(1,n+1):
        tmp =tmp *i
    base += tmp
    return base

sum = 0
for i in range(1,n+1):
    sum = sums(i,sum)
print(sum)