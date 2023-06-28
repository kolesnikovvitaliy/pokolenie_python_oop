''' Первый вариант решения'''
import re


class StrExtension:
    
    @staticmethod
    def  remove_vowels(text):
        return ''.join(map(lambda x: x if not re.findall(r'[aeiouy]', x, re.IGNORECASE) else '', text))

    @staticmethod
    def leave_alpha(text):
        return ''.join(map(lambda x: x if re.findall(r'[a-z]', x, re.IGNORECASE) else '', text))
    
    @staticmethod  
    def replace_all(string, chars, char):
        return ''.join(map(lambda x: x if not re.findall(f'[{chars}]', x) else char, string))
''' Второй вариант решения'''    
# import re
# class StrExtension:
#     @staticmethod
#     def remove_vowels(string):
#         return re.sub(r'[aeiouy]', '', string, flags=re.I)
    
#     @staticmethod
#     def leave_alpha(string):
#         return re.sub(r'[^A-Za-z]', '', string)
    
#     @staticmethod
#     def replace_all(string, chars, char):
#         return re.sub(fr'[{chars}]', char, string)
