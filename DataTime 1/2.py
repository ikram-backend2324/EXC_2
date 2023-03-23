# 2) Выведите на экран текущий месяц словом, по-русски.

from datetime import datetime

now = datetime.now()
month = [{
    id: 1,
    "Name": "Январь",
    }, {
    id: 2,
    "Name": "Февраль"
    }, {
    id: 3,
    "Name": "Март"
    }, {
    id: 4,
    "Name": "Апрель"
    }, {
    id: 5,
    "Name": "Май"
    }, {
    id: 6,
    "Name": "Июнь"
    }, {
    id: 7,
    "Name": "Июль"
    }, {
    id: 8,
    "Name": "Август"
    }, {
    id: 9,
    "Name": "Сентябрь"
    }, {
    id: 10,
    "Name": "Октябрь"
    }, {
    id: 11,
    "Name": "Ноябрь"
    }, {
    id: 12,
    "Name": "Декабрь"
    }]

def getMonth(id_number = now.month):

    for item in month:
        if item[id] == int(id_number):
            return item["Name"]

print(getMonth())

