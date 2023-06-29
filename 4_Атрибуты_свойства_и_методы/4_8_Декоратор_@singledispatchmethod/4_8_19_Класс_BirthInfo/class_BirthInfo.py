''' Первый вариант решения'''
from functools import singledispatchmethod
from datetime import date, datetime, timedelta


class BirthInfo:
    @singledispatchmethod
    def __init__(self, arg):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def _(self, arg):
        self.birth_date = arg

    @__init__.register(str)
    def _(self, arg):
        arg = datetime.date(datetime.strptime(arg, "%Y-%m-%d"))
        self.birth_date = arg

    @__init__.register(tuple)
    @__init__.register(list)
    def _(self, arg):
        arg = datetime.date(datetime(*arg))
        self.birth_date = arg

    @property
    def age(self):
        age = datetime.date(datetime.today()) - self.birth_date
        a = int(age.days // 365.2)
        return a
''' Второй вариант решения'''    
# from functools import singledispatchmethod
# from datetime import date 


# class BirthInfo:
#     @singledispatchmethod
#     def __init__(self, birth_date):
#         raise TypeError('Аргумент переданного типа не поддерживается')
    
#     @__init__.register(date)
#     def _(self, birth_date):
#         self.birth_date = birth_date
        
#     @__init__.register(str)
#     def _(self, birth_date):
#         self.birth_date = date.fromisoformat(birth_date)
        
#     @__init__.register(list)
#     @__init__.register(tuple)
#     def _(self, birth_date):
#         self.birth_date = date(*birth_date)
    
#     @property
#     def age(self):
#         return current_age(self.birth_date, date.today())