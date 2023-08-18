''' Первый вариант решения'''
class USADate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return f'{self.month:02}-{self.day:02}-{self.year}'

    def iso_format(self):
        return f'{self.year}-{self.month:02}-{self.day:02}'


class ItalianDate(USADate):
    def format(self):
        return f'{self.day:02}/{self.month:02}/{self.year}'
''' Второй вариант решения'''    
# from abc import ABC, abstractmethod
# from datetime import date


# class DateFormat(ABC):
#     def __init__(self, year, month, day):
#         self._date = date(year, month, day)

#     def iso_format(self):
#         return self._date.isoformat()

#     @abstractmethod
#     def format(self):
#         pass


# class USADate(DateFormat):
#     def format(self):
#         return self._date.strftime('%m-%d-%Y')


# class ItalianDate(DateFormat):
#     def format(self):
#         return self._date.strftime('%d/%m/%Y')