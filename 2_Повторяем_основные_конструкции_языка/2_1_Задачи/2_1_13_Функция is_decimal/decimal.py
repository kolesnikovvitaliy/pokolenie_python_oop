''' Первый вариант решения'''
import re


def is_decimal(string: str) -> bool:
    regex_obj = re.compile(r'-?\.?\d+\.\d+')
    try:
        return bool(float(string))
    except:
        return bool(regex_obj.fullmatch(string))
# print(is_decimal('-.95'))
# print(is_decimal('.-95'))
# print(is_decimal('--10.1'))

''' Второй вариант решения'''    
# import re

# def is_decimal(n):
#     return bool(re.search(r'^-?(?:\d+\.?\d*|\d*\.?\d+)$', n))