b = input().split()
sr = input()
for i in range(len(b) - 1):
    print("{}".format(b[i]) + sr, end='')
print(b[-1])
