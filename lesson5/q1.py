M =  int(input())
N =  int(input())
def rec(m,n):
    # 默认m>n，若不是，则交换
    if m < n:
        m,n = n,m
    # 终止条件
    if n == 0:
        return m,(M*N)/m
    # 递归部分
    return rec(n,m%n)
tu = rec(M,N)
print(int(tu[0]),int(tu[1]))
