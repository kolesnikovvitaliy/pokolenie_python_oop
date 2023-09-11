''' Первый вариант решения'''
class Currency:
    def __init__(self, item, currency):
        self.item = item
        self.currency = currency

    def __str__(self):
        return f'{round(self.item, 2)} {self.currency}'

    @staticmethod
    def is_instance_decorator(func):
        def wrapper(self, other):
            if isinstance(other, (__class__, int, float)):
                other.change_to(self.currency)
                return func(self, other)
            return NotImplemented
        return wrapper

    @is_instance_decorator
    def __add__(self, other):
        return __class__(self.item + other.item, self.currency)

    @is_instance_decorator
    def __sub__(self, other):
        return __class__(self.item - other.item, self.currency)

    @is_instance_decorator
    def __mul__(self, other):
        return __class__(self.item * other.item, self.currency)

    @is_instance_decorator
    def __truediv__(self, other):
        return __class__(self.item / other.item, self.currency)

    def change_to(self, currency):
        __RATE = {
            'EUR': {'EUR': 1, 'USD': 1.1, 'RUB': 90},
            'USD': {'EUR': 1 / 1.1, 'USD': 1,  'RUB': 1 / 1.1 * 90},
            'RUB': {'EUR': 1 / 90, 'USD': 1 / 90 * 1.1, 'RUB': 1}
        }
        self.item = self.item * __RATE[self.currency][currency]
        self.currency = currency
''' Второй вариант решения'''    
# from enum import Enum


# class Values(Enum):
#     EUR = 1
#     RUB = 90
#     USD = 1.1


# class Currency:
#     def __init__(self, value, unit):
#         self.value = value
#         self.unit = unit
#         self.in_eur = value if unit == 'EUR' else value / Values.__dict__[unit].value

#     def __str__(self):
#         return f'{round(self.value, 2)} {self.unit}'

#     @staticmethod
#     def other_value(other, unit):
#         return other.in_eur * Values.__dict__[unit].value

#     def change_to(self, unit):
#         self.unit = unit
#         self.value = self.in_eur * Values.__dict__[unit].value

#     def __add__(self, other):
#         if isinstance(other, type(self)):
#             return type(self)(self.value + self.other_value(other, self.unit), self.unit)
#         return NotImplemented

#     def __mul__(self, other):
#         if isinstance(other, type(self)):
#             return type(self)(self.value * self.other_value(other, self.unit), self.unit)
#         return NotImplemented

#     def __sub__(self, other):
#         if isinstance(other, type(self)):
#             return type(self)(self.value - self.other_value(other, self.unit), self.unit)
#         return NotImplemented

#     def __truediv__(self, other):
#         if isinstance(other, type(self)):
#             return type(self)(self.value / self.other_value(other, self.unit), self.unit)
#         return NotImplemented