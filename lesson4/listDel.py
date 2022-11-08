from random import randint,seed
n = int(input())
seed(n)
m = randint(1,n)
ls = [i+1 for i in range(n)]
print(ls)
for i in ls:
    if i % m == 0:
        ls.remove(i)
print(ls)