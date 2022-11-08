def stepMulti(n):   #封装一个阶乘函数,使用for循环进行连续乘法
    s = 1;
    for i in range(1,n+1):
        s *= i
    return s

def combination(n,m):  #封装一个组合数函数,基于阶乘函数带入组合数公式求得
    if n>m:
        print("error")
    else:                   #注意这里返回时由于使用到除法要取整
        return int( stepMulti(m) /( stepMulti(n) * stepMulti(m -n ) ))

def printYH(M):             #封装杨辉三角打印矩阵
    arr =[                  #初始化一个对角空列表
        [0]*(_+1) for _ in range(0,M+1)
    ]
    for i in range(0,M+1):   #使用双重for对初始化数组中每列数据使用封装好的组合数函数计算结果
        for k in range(0,i+1):
            arr[i][k] = combination(k,i)
    width = int(M / 2) + 1     #根据行元素宽计算元素所占打印宽度，动态调整
    for p in range(0, M):       #按行打印杨辉三角循环
        s = ''                  #以字符串形式居中打印
        for j in range(0, len(arr[p])):    #取出列表中元素拼接成字符串 将
                s = s + str(arr[p][j]).center(width)    #以间隔width宽度居中
        s = s.center(width * M)            #居中打印第 i 行字符串
        print(s)                           #每次循环的打印一行

def Main():
    M = eval(input())
    printYH(M)
Main()