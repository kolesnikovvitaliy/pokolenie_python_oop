''' Первый вариант решения'''
import re
def is_fraction(string: str) -> bool:
    regex_obj = re.compile(r'-?[0-9]+/0*[1-9]\d*')
    return bool(regex_obj.fullmatch(string))

''' Второй вариант решения'''    
# def is_fraction(string):
#     regex = r'^-?\d+/[1-9]\d*$'
#     rez = bool(__import__('re').fullmatch(regex, string))
#     return rez