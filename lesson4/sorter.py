#sorter.py
names = ['AA','BBBB','CCC']
names.sort()
print(names)
names.sort(key = len)
print(names)
print(names.reverse())
scores = [82,66,66,93,24,15,22.8]
scores.sort(reverse=True)
a = scores.sort(reverse=True)  #表示空对象  scores.sort()已经完成对列表顺序的操作 无法竞选ref引用

print(scores)
print(a)

namess = ['CC',"DDDD","A",'B']
namessReverse = sorted(namess)  #函数方法可以引用
print(namess)
print(namessReverse)

# 列表推导式
# 列表推导式使用非常简洁的方式来快捷生成满足需求的列表
# [expression for exp1 in squence1 if condition1
#             for exp2 in squence1 if condition2
#             for exp3 in squence1 if condition3
#             for exp4 in squence1 if condition4
# ]
# 聊表推导式
alist = [x*x for x in range(10)]
print(alist)

blist = []
for x in range(10):
    blist.append(x*x)
print(blist)

FreshFruit= ['banana','apple','passion']
alist = [w.strip() for w in FreshFruit]
print(alist)

for w in FreshFruit:
    alist.append(w)
print(alist)

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
# blist =[]
# for i in range(4):
#     for j in range(4):
#         blist[i][j] = alist[j][i]

clist =[
    [row[i] for row in  matrix] for i in range(4)
]
print(clist)