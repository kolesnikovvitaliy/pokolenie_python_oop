''' Первый вариант решения'''
from enum import Enum
from datetime import timedelta


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class NextDate:
    def __init__(self, today, weekday, after_today=False):
        self.today = today
        self.weekday = weekday
        self.after_today = after_today

    def date(self):
        if self.today.weekday() < self.weekday.value:
            return self.today + timedelta(days=(self.weekday.value-self.today.weekday()))
        elif self.today.weekday() > self.weekday.value:
            return self.today + timedelta(days=(7 - self.today.weekday()+self.weekday.value))
        elif self.today.weekday() is self.weekday.value:
            if self.after_today:
                return self.today + timedelta(days=0)
            return self.today + timedelta(days=7)

    def days_until(self):
        return (self.date() - self.today).days
''' Второй вариант решения'''    
# from datetime import timedelta
# from enum import IntEnum

# Weekday = IntEnum('Weekday', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], start=0)


# class NextDate:
#     def __init__(self, today, weekday, after_today=False):
#         self.today = today
#         self.weekday = weekday
#         self.after_today = after_today

#     def date(self):
#         next_date = self.today + timedelta((self.weekday - self.today.weekday()) % 7)
#         if not self.after_today and next_date == self.today:
#             next_date += timedelta(7)
#         return next_date

#     def days_until(self):
#         return (self.date() - self.today).days