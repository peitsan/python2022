with open('in.txt',  'r') as f1:
    data = f1.readlines()
with open('out.txt',  'w') as f2:
    for d in data:
        s = d.split()
        t = [eval(i) for i in s]
        iMax = t.index(max(t))
        iMin = t.index(min(t))
        f2.write(f'{s[iMax]}  {s[iMin]}\n')