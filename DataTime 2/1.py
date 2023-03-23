# 1) Создать в одной функции часы в окне документа в 24 часовом формате,
# а также вывести текущую дату,
# указав название месяца на русском языке.

from datetime import datetime

now = datetime.now()

def getMonth(month=now.month):

    j_year = [{
        id: 1,
        "Name": "январь",
    }, {
        id: 2,
        "Name": "февраль",
    }, {
        id: 3,
        "Name": "март",
    }, {
        id: 4,
        "Name": "апрель",
    }, {
        id: 5,
        "Name": "май",
    }, {
        id: 6,
        "Name": "июнь",
    }, {
        id: 7,
        "Name": "июль",
    }, {
        id: 8,
        "Name": "август",
    }, {
        id: 9,
        "Name": "сентябрь",
    }, {
        id: 10,
        "Name": "октябрь",
    }, {
        id: 11,
        "Name": "ноябрь"
    }, {
        id: 12,
        "Name": "декабрь."
    }]

    result1 = f"{now.day}.{now.month}.{now.year}"
    for i in j_year:
        if i[id] == int(month):
            return f"{result1}\n{i['Name']}"

print(getMonth())

