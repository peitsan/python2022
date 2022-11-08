N = int(input())
temp = []
result = []
for i in range(2 * N - 1):
    for j in range(2 * N - 1):
        temp.append(0)
    result.append(temp)
    temp = []
flag = 1
for i in range(N):
    for j in range(i, 2 * N - 1 - i):
        result[i][j] = result[j][i] = result[j][2 * N - 2 - i] = result[2 * N - 2 - i][
            j] = flag
    flag += 1
f = open("out162.txt", 'w').write("%2d",result)
# for i in result:
#     for j in i:
#         print(j, end="")
#     print()

