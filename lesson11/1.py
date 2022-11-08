fname = input("请输入要写入的文件: ")
fo = open(fname, "w+") 
ls = ["清明时节雨纷纷，","路上行人欲断魂，","借问酒家何处有？","牧童遥指杏花村。"] 
fo.writelines(ls) 
fo.seek(0) 
for line in fo: 
      print(line) 
fo.close()