dict = {
    'A':4.0,'A-':3.7,'B+':3.3,'B':3.0,'B-':2.7,'C+':2.3,'C':2.0,'C-':1.5,'D':1.3,'D-':1.0,'F':0
}
grade = []
score = []
sumScore = 0.0
allScore = 0.0
temp = ' '
while 1:
    temp = input()
    if temp[0] == '-':
        break
    grade.append(temp)
    tmp = int(input())
    score.append(tmp)
for i in range(len(grade)):
    sumScore += dict.get(grade[i]) * score[i]
    allScore += score[i]
print("{:.2f}".format(sumScore/allScore))