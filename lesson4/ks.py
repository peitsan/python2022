a = input().split(" ", 1)
b = int(a[0])
for i in a[-1]:
    if(ord(i) >= ord("a") and ord(i) <= ord("z")):
        print(chr(ord("a")+(ord(i)-ord("a") + b) % 26), end="")
    elif(ord(i) >= ord("A") and ord(i) <= ord("z")):
        print(chr(ord("A")+(ord(i)-ord("A") + b) % 26), end="")
    else:
        print(i, end="")