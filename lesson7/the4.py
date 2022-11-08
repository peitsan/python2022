from math import *
def isPrime(num):
    isprime = 1
    for i in range(2, int(sqrt(num+1))):
        if num % i == 0:
            isprime = 0
    return isprime

def isGdbh(n):
    list = [i for i in range(2,n) if isPrime(i)]
    for i in list:
        for j in list:
            if  i + j == n:
                print("N = {} + {}".format(i,j))
                return 1
    return 0

def Main():
    n = eval(input())
    if n % 2 == 0:
        isGdbh(n)
    else:
        print("Data error!")

Main()