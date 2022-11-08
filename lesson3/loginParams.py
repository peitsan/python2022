#loginParams.py
data = {"aaa":["123456",3],
        "bbb":["888888",3],
        "ccc":["333333",3]}
act = input()
if not data.get(act):
    print("Wrong User")
else :
    truePwd = data.get(act)[0]
    while data.get(act)[1]> 0:
        pwd = input()
        if truePwd == pwd :
            data[act][1] -=1
            print("Success")
            break
        else:
            data[act][1]  -= 1
            if data[act][1] == 0:
                print("Login Denied")
            else:
                print("Fail,{:d} Times Left".format(data[act][1]))


