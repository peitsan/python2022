ls = []
with open(file=r'in.txt', mode='r') as f:
    for lines in range(len(f.readline())):
        zf_list = f.readline().replace('\n', '')
        if zf_list:
            sz_list = []
            for i in zf_list.split(" "):
                sz_list.append(i)
                sorted_list = sorted(sz_list, reverse=True)
                print(str(sorted_list[0]) + " " + str(sorted_list[len(sz_list) - 1]))
                list = str(sorted_list[0])+" "+str(sorted_list[len(sz_list)-1])
                ls.append(list)
fo = open('out.txt', "w+")
fo.writelines(ls)