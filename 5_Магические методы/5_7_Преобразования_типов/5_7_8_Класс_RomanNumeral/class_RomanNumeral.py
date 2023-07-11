''' Первый вариант решения'''
from functools import total_ordering

@total_ordering
class RomanNumeral:
    def __init__(self, number):
        if type(number) == str:
            self.number = self.__checkio(number)
        else:
            self.number = number

    def __str__(self) -> str:
        return f"{self.__checkio(self.number)}"
                   
    def __int__(self):
        return self.number
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, __class__):
            return self.number == __value.number
        return NotImplemented
        
    def __lt__(self, __value: object) -> bool:
        if isinstance(__value, __class__):
            return self.number < __value.number
        return NotImplemented
    
    def __add__(self, __value: object):
        if isinstance(__value, __class__):
            return __class__(self.number + __value.number)
        return NotImplemented
    
    def __radd__(self, __value: object):
        return self.number.__add__(__value.number)
    
    def __sub__(self, __value: object):
        if isinstance(__value, __class__):
            return __class__(self.number - __value.number)
        return NotImplemented
    
    def __rsub__(self, __value: object):
        return self.number.__sub__(__value.number)
    
    def __checkio(self, n):
        __lst_roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        if type(n) == int:
            rez_roman = ''
            for arab, roman in __lst_roman.items():
                while n >= arab:
                    rez_roman += roman
                    n -= arab
            return rez_roman
        else:
            num = 0
            for arab, roman in __lst_roman.items():
                while n.startswith(roman):
                    if roman in n:
                        num+= arab
                    n = n[len(roman):]
            return num
''' Второй вариант решения'''    
# from functools import total_ordering

# @total_ordering
# class RomanNumeral:
#     def __init__(self, number):
#         self.number = number
        
#     def __str__(self):
#         return self.number
    
#     def __int__(self):
#         return RomanNumeral.roman_to_int(self.number)
    
#     def __add__(self, other):
#         if isinstance(other, RomanNumeral):
#             num1 = int(self)
#             num2 = int(other)
#             return RomanNumeral(RomanNumeral.int_to_roman(num1 + num2))
#         else:
#             return NotImplemented
    
#     def __sub__(self, other):
#         if isinstance(other, RomanNumeral):
#             num1 = int(self)
#             num2 = int(other)
#             return RomanNumeral(RomanNumeral.int_to_roman(num1 - num2))
#         else:
#             return NotImplemented
    
#     def __eq__(self, other):
#         if isinstance(other, RomanNumeral):
#             return self.number == other.number
#         else:
#             return NotImplemented
        
#     def __gt__(self, other):
#         if isinstance(other, RomanNumeral):
#             return RomanNumeral.roman_to_int(self.number) > RomanNumeral.roman_to_int(other.number)
#         else:
#             return NotImplemented
    
#     @staticmethod
#     def int_to_roman(number):
#         int_roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 
#                      10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 
#                      100: 'C', 400: 'CD',  500: 'D', 900: 'CM', 1000: 'M'}
#         result = ''
#         for n in (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1):
#             while n <= number:
#                 result += int_roman[n]
#                 number -= n
#         return result
     
#     @staticmethod
#     def roman_to_int(number):
#         roman_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         summ = 0
#         for i in range(len(number) - 1, -1, -1):
#             num = roman_int[number[i]]
#             if 3*num < summ: 
#                 summ -= num
#             else: 
#                 summ += num
#         return summ