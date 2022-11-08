#grade.py
grade = float(input())
if not 0<=grade<=100:
    print("Not valid")
else:
    if 89<grade<=100:
        print("A")
    elif 79<grade<=89:
        print("B")
    elif 69<grade<=79:
        print("C")
    elif 59<grade<=69:
        print("D")
    elif 0<=grade<=59:
        print("E")