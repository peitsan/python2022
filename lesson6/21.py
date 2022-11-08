a = int(input())
def ca (a):
    if (0 <= a < 5):
       print(a)
    elif (5 <= a < 15):
      print(a+6)
    elif (15 <= a):
      print(a-6)
    else:
      print('illegal input')
ca(a)