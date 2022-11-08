count = 0
def Hanoi(n, a, b, c):
    if n==1:
        Move(a, b)
    else:
        Hanoi(n-1, a, c, b)
        Move(a, b)
        Hanoi(n-1, c, b, a)
def Move(a, b):
    global count
    count+=1
    print("[STEP{:>4}]".format(count),"%c->%c"%(a,b))
n = int(input())
Hanoi(n,'A','C','B')