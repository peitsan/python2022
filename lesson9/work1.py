#数组存储及读写
f1 = open("in162.txt", "r")
list = map(f1.readline().split( )[:10])
sum = 0
for i in list:
    sum += i
f2 = open("out162.txt", 'w').write("%.2f",i*0.454)