# 3)  Выведите на экран текущий день.
#  Выведите на экран текущий месяц.
#  Выведите на экран текущий год
# Выведите на экран номер текущего дня недели

from datetime import datetime

now = datetime.now()

def calcDays(month = now.month):

    # 1,3,5,7,8,10,12  = 31
    # 2 = 28

    days = 0
    i = 1
    while i < month:
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            days += 31
        elif i == 2:
            days += 28
        else:
            days += 30
        i += 1

    days += now.day
    return days

result = calcDays()

print(now.day)
print(now.month)
print(now.year)
print(int(result / 7))