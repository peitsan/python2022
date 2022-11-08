def compare(A,B):
    s1,s2 = sum(A),sum(B)
    if s1 == s2:
        res = 'equal'
    elif s1 < s2:
        res = 'smaller'
    elif  s1 > s2:
        res = 'bigger'
    return res

def Group(coins):
    n = len(coins)
    A = coins[0: n // 2]
    B = coins[n // 2: n // 2 * 2]
    C = coins[n // 2 * 2: n]  # 余数堆,最大为一
    if len(C) == 1: C[0] = n - 1
    return A, B, C


def findFalseCoin(coins,start,n):
    if n == 1:
        print("Fake coin:{}".format(start))
        return
    A, B, C = Group(coins)
    res = compare(A,B)
    if res == 'bigger':
        findFalseCoin(A, start, n // 2)
    elif res == 'smaller':
        findFalseCoin(B, start + n // 2, n // 2)
    elif res == 'equal' and len(C) == 0:
        print("Fake coin is not found")
    elif res == 'equal' and len(C) == 1:
        print("Fake coin:{}".format(C[0]))


coins = list(map(int, input().split(',')))
findFalseCoin(coins, 0, len(coins))
