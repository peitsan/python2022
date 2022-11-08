# C = (P+n) mod 26
bitMove,Str = input().split(' ',1)  #使用split函数对输入字符串进行元组解包，在第一个空格位置切片
bitMove = int(bitMove)              #输入时默认经过切片后输出的变量为诶字符型 需要转为整形才能才能与运算
for p in Str:                       #遍历输入数组的所有元素
    if "a" <= p <= "z":             #对所有小写字母做凯撒加密
        print(chr(ord("a") +(ord(p) - ord("a") + bitMove) % 26), end="")
    elif "A"<= p <="Z":             #对所有大写字母做凯撒加密
        print(chr(ord("A")+(ord(p) - ord("A")+ bitMove) % 26),end="")
    else:
        print(p,end="")             #对其他情况如输入数字空格保持原型不修改
