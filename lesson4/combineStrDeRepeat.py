str1 = input().split(' ')
str2 = input().split(' ')
str3 = str1 + str2
str3.sort()
res = []
[res.append(i) for i in str3 if i not in res]
for i in res:
    print(i,end="")

