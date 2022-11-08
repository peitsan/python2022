f=open("sensor-data-1k.txt", "r") #打开目标文件 权限为只读
n = 0
sum = 0
for row in f:
 list = row.split(" ")
 n += 1
 sum += eval(list[4])
print("{:.2f}".format(sum/n))