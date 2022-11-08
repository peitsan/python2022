f_1 = open("in162.txt", "r")
s = 0
count = 0
line = f_1.readline()    
weight = list(line.split()) 
for item in weight:
    s += eval(item)*0.454
    count += 1
    if count == 10:
        break
f_2 = open("out162.txt", 'w')
f_2.write("%.2f" % s)
f_1.close()
f_2.close()
