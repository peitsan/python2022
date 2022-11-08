#tuple.py
patient = ("2012011",'Eric Zhang','male',77,True,(67,22,78))
print(type(patient),patient)
print(len(patient))
#序列类型 字符串 元组 列表 （有序 有索引和下标）
print(patient[1:4])
print(patient.count(True))
print(True in  patient)
print(max((1,3,5)))

print((1,2)+(2,3)+(4,))
print((1,2)*5)