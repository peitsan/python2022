def f2c(temp):          #封装华氏度转摄氏度函数
    return 5 * (temp - 32)/ 9

def printF2Ctable(f1,f2):  #封装朱行打印华氏度对照表函数
    for i in range(f1,f2):
        if not (i-f1) % 2:   #判断并以2为刻度值输出
            print("{} : {:.2f}".format(i,f2c(i)))
def Main():            #封装输入、输出判断主函数
    f1,f2 = map(int,input().split(","))
    if f1>f2:
        print("error")
    else:
        printF2Ctable(f1,f2)
Main()