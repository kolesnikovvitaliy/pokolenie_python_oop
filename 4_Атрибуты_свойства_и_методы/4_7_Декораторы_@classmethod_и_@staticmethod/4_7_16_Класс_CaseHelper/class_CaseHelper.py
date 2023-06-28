''' Первый вариант решения'''
import re


class CaseHelper:
    
    @staticmethod
    def is_snake(string):
        return False if (re.findall(r'[A-Z]', string) and not re.findall(r'_', string) or re.findall(r'__', string))  else True

    @staticmethod
    def is_upper_camel(string):
        return True if (re.findall(r'[A-Z]', string) and not re.findall(r'_', string) and re.findall(r'^[A-Z]', string)) else False

    @staticmethod
    def to_snake(string):
        return re.sub(r'(?<=\w)(?=[A-Z])', '_', string).lower()       

    @staticmethod
    def to_upper_camel(string):
        return ''.join(map(lambda x: x.title(), string.split('_')))
''' Второй вариант решения'''    
# import re

# class CaseHelper:
#     @staticmethod
#     def is_snake(string):
#         return re.match(r'^[a-z]+(_[a-z]+)*$', string) is not None

#     @staticmethod
#     def is_upper_camel(string):
#         return re.match(r'^([A-Z][a-z]+)+$', string) is not None

#     @staticmethod
#     def to_snake(string):
#         return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()

#     @staticmethod
#     def to_upper_camel(string):
#         return ''.join(map(str.capitalize, string.split('_')))