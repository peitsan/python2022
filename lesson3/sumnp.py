#sumnp.py
str = []
a = int(input())
upper,lower,sum,sort = 0,0,0,0
while a:
    str.append(a)
    a = int(input())
    sort += 1
for key in str:
    sum += int(key)
    if key > 0:
        upper += 1
    elif int(key) < 0:
        lower += 1
print(sum/sort)
print(upper)
print(lower)