a = list(input().split(","))
sum = 1
for i in range(len(a)):
    sum = eval(a[i])*sum
print(sum)
