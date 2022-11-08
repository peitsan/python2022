#set.py
# 集合中的字符串性质具有去重性
# 列表可以通过set 转为集合 集合可以用List（）转为列表
s1 = set("Hello")
s2 = set([1,3,1,2,7,6])
values = list(s2)
print("values:",values)
countries = {"CN","USA","JP"}

countries.add("ITY") #添加集合元素
countries.remove("JP")#删除元素



print("Set countries:",countries,"length = ",len(countries))
print("Germany in set countries?","GMY" in countries)

for x in countries:
    print(x)

numbers = {12,5,6,90,15}
print("max,min,sum of numbers:",max(numbers),min(numbers),sum(numbers))
numbers.add(16)
numbers.pop()
