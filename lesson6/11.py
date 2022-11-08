def hello_world():
    print('ST',end="*")
def three_hellos():
    for i in range(3):
        hello_world()
three_hellos()