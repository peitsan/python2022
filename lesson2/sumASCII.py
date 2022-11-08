#sumASCII.py

str = input()
a=0
b=0
c=0
for i in str:
    if 65<=ord(i)<=90: a+=1
    elif 97<=ord(i)<=122: b+=1
    elif 48 <=ord(i)<=57:c+=1
print("{}\n{}\n{}".format(a,b,c))