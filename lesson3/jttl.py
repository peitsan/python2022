#jttl.py
iHeads,iFeet = map(int,input().split(" ")) #同时输入头数和脚数
#input  format format输出要求
iRabbits = (iFeet  - 2 * iHeads)/2#兔数
iChicken = iHeads - iRabbits   #鸡数
if  iRabbits*iChicken>=0:
    print("{:d} {:d}".format(int(iChicken),int(iRabbits)))
elif  iRabbits*iChicken<0:
    print("Data Error!")