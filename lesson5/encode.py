#encode.py
#凯撒加密
#同时对大小写字母加密解密

d= {}
for c in range(65,97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13)%26 + c)
print("".join([d.get(c,c) for c in d]))

