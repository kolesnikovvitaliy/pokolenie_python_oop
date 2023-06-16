''' Первый вариант решения'''
from datetime import datetime
import calendar

year, month = [*map(int,(input() for i in range(2)))]
list_date = []
for i in range(1, calendar.monthrange(year, month)[1]+1):
    date = datetime(year, month, i)
    if date.weekday() == 3:
        list_date.append(date.strftime('%d.%m.%Y'))
print(list_date[3])
    
''' Второй вариант решения'''    
# from datetime import date, timedelta

# year, month = int(input()), int(input())
# d = date(year, month, 1)

# while d.isoweekday() != 4:
#     d += timedelta(days=1)

# d += timedelta(days=21)
# print(d.strftime('%d.%m.%Y'))