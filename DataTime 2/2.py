# 2) - Определить, сколько дней осталось до нового учебного года.

from datetime import *

now = datetime.now()

def getSchoolDate(y_month=9, y_day=6):
    result = 0
    if now.month < y_month:
        month = y_month - now.month-1
        result += month * 30
        result += now.day
        result += y_day

    elif y_day > now.day:
        day = y_day - now.day
    return f"{result} дней осталось до нового учебного года"
print(getSchoolDate())