str=input()
if str.isdigit() or (str[0] == '-' and str.lstrip('-').isdigit()):
    if '3' in str or '4' in str:
        print('true')
    else:
        print('false')
else:
    print('illegal input')