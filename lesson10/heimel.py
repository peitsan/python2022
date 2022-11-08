#-*- coding: utf-8 -*-
def getText():
    t = open("hamlet.txt", "r").read()  # 读
    t = t.lower()  # 全体小写
    for i in "!\"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~":  # 略
        t = t.replace(i, " ")
    return t


h = getText()
s = int(input())  # 指定数
words = h.split()  # 列表化
counts = {}  # 暂存字典
for word in words:  # 统计
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)  # 降序统计
for i in range(s):  # 格式化输出
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))

