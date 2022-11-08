ls = ['the lord of the rings','anaconda','legally blonde','gone with the wind']
keypatch = input()
if keypatch == '1':
    print([ x*x*x for x in range(0,10)])
elif keypatch == '2':
    print([x * x * x for x in range(0, 9) if x %2 ==0])
elif keypatch == '3':
    print([(x,x*x*x)for x in range(0, 10) if x %2 ==1])
elif keypatch == '4':
    print([str.capitalize() for str in ls])
else:
    print('End of the program')