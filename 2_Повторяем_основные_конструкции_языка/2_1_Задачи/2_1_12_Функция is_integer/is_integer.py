''' Первый вариант решения'''
def is_integer(string):
    try:
        return bool(int(string))
    except:
        return False

# print(is_integer('-0001'))
# print(is_integer('0001'))
    
''' Второй вариант решения'''    
#import re


# def is_integer(string: str) -> bool:
#     regex_obj = re.compile(r'-?\d+')
#     return bool(regex_obj.fullmatch(string))