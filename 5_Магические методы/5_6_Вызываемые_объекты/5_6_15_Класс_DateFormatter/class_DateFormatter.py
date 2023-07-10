''' Первый вариант решения'''
from datetime import date


class DateFormatter:
    def __init__(self, country_code): 
        __code = {
        "ru": "%d.%m.%Y",
        "us": "%m-%d-%Y",
        "ca": "%Y-%m-%d",
        "br": "%d/%m/%Y",
        "fr": "%d.%m.%Y",
        "pt": "%d-%m-%Y"
    }
        self.country_code = __code[country_code]

    def __call__(self, date):
        return f"{date.strftime(self.country_code)}"
''' Второй вариант решения'''    
# class DateFormatter:
#     def __init__(self, country_code  ):
#         self.country_code   = country_code 
    
#     def __call__(self, d):
#         match self.country_code:
#             case 'ru' | 'fr':
#                 return f'{d:%d.%m.%Y}'
#             case 'us':
#                 return f'{d:%m-%d-%Y}'
#             case 'ca': 
#                 return f'{d:%Y-%m-%d}'
#             case 'br':
#                 return f'{d:%d/%m/%Y}'
#             case 'pt':
#                 return f'{d:%d-%m-%Y}'