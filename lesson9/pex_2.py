f = open("out162.txt", 'w').write("%.2f" %sum(i*0.454 for i in list(map(float,open("in162.txt", "r").readline().split( )[:10]))))
