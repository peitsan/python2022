#!/usr/bin/python
TempStr = input("What is the temperature?")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1])-32)/1.8
    print("The converted temperature is {}C".format(int(C)))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1])+32
    print("The converted temperature is {}F".format(int(F)))
else:
    print("格式错误")