#listDelRepeat.py
str = input().split(',')
res = []
[res.append(i) for i in str if i not in res]
print(res)