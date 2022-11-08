f=open("grade.txt","r")
a=f.read()
ls=a.split(sep='\n')
ls2=[]
ping,b=0,0
for i in ls:
    ping=ping+float(i)
    ls2.append(int(i))
    b+=1
ls2.sort()
gao=ls2[-1]
di=ls2[0]
ping="%.1f" % (ping/b)
fo=open("result.txt","w")
fo.write(str(gao))
fo.write('\n')
fo.write(str(di))
fo.write('\n')
fo.write(str(ping))
f.close()
fo.close()