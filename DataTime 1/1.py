# 1)  Выведите на экран текущие день, месяц и год в формате 'год-месяц-день'.

from datetime import datetime

now = datetime.now()
print(now.date())


