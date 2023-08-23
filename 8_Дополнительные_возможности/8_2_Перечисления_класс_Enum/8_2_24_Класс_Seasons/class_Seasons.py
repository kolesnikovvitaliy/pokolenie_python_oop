''' Первый вариант решения'''
from enum import Enum


class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, item):
        match item:
            case 'ru':
                ru_seasons = ('зима', 'весна', 'лето', 'осень')
                codes = dict(zip(Seasons, ru_seasons))
                return codes[self]
            case 'en':
                en_seasons = ('winter', 'spring', 'summer', 'fall')
                codes = dict(zip(Seasons, en_seasons))
                return codes[self]
''' Второй вариант решения'''    
# from enum import Enum, auto


# class Seasons(Enum):
#     WINTER = auto()
#     SPRING = auto()
#     SUMMER = auto()
#     FALL = auto()

#     def text_value(self, country_code):
#         seasons_translate = {
#             'en': {
#                 self.WINTER: 'winter',
#                 self.SPRING: 'spring',
#                 self.SUMMER: 'summer',
#                 self.FALL: 'fall'
#             },
#             'ru': {
#                 self.WINTER: 'зима',
#                 self.SPRING: 'весна',
#                 self.SUMMER: 'лето',
#                 self.FALL: 'осень'
#             },
#         }
#         return seasons_translate[country_code][self]