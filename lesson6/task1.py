#task1.pyn
import math #引入math库用于开根号 对素数遍历范围进行简化

def getPrime(n):  #求素数函数
        for i in range(2, int(math.sqrt(n)) + 1):  #使用for循环语句求余判断素数
            if n % i == 0:                         #使用穷举法对所有小于待测数 判断是否有非1因子
                return 0                            #如果有多余的因子 则返回”假“，不是素数
        return 1                                    #如果有只有本身和1 则返回”真“，是素数

n = eval(input())                                   #输入一个整数n
prime = list(range(2,n))                            # 初始化一个递增列表
for i in prime:                                     #对列表中的测试数据依次判断是否是素数
    if(getPrime(i)==0):                             #如果不是则把该位数据赋为-1
        prime[i-2]=-1
prime=set(prime)                                    #利用集合的特性将所有的非素数-1合并
prime=list(prime)                                   #在转为列表 此时列表包括 -1 和一组素数
prime.remove(-1)
prime=sorted(prime)#删去列表中的-1元素即所求的列表
for i in prime:
    print(i,end=' ')
