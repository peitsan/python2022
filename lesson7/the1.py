def multiS (n):
    k = 1
    for i in range(1 , n+1):
        k *= i
    return k

def sum(n):
    Sum = 0
    for i in range(1,n+1):
        Sum += multiS(i)
    return Sum

if __name__ =='__main__':
    n = eval(input())
    print(sum(n))
