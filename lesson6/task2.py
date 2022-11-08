n = 100  #定义100为默认输入量
key = 0  #初始化一个猜中的数满足 key！=n
while not key == n:         #使用for循环进行猜数字轮询
    key = eval(input())      #每次都需要输入一个整数
    if key > n:              #如果过大打印提示语
        print("larger than expected")
    elif key < n:            #如果过小打印提示语
        print("less than expected")
    else:                    #如果正确打印提示 此时循环结束
        print("you win")