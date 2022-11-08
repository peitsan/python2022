def isprime(num):                   #牛顿迭代法判断是否是质数
    isprime = 1
    for i in range(2,num):
        if num%i==0:
            isprime = 0
    return isprime
li = [ i for i in range(2,1000) if isprime(i)==1]        #生成一个完全有质数组成的列表
n = int(input())                                         #输入一个待测数字
num = n
m=[]                                                #初始化因数列表
while n!=1:
    for j in range(len(li)):                        #遍历质数列表 当为待测数的因数时 则添加到结果列表
        if n % li[j] == 0:
            m.append((li[j]))
            n = n/li[j]
    if n==1:
        break
m.sort()
print(m)