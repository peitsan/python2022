n = eval(input())
with open('text.txt', 'r', encoding='utf8') as f:
    mark=True
    if type(n) == type(1):
          for i in range(n):
            txt = f.readline().replace('\n', '')
            if txt:
                if "A" == txt[0]:
                  print(txt)
                  mark=False
          if mark:
            print("not found")
    else:
        print("illegal input")