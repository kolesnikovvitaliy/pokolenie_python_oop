''' Первый вариант решения'''
from keyword import iskeyword


class NonKeyword:
    def __init__(self, name):
        self._attr = name

    def __get__(self, obj, cls):
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if type(value) is not str or not iskeyword(value):
            obj.__dict__[self._attr] = value
        else:
            raise ValueError('Некорректное значение')
''' Второй вариант решения'''    
# from keyword import kwlist


# class NonKeyword:
#     def __init__(self, name):
#         self._attr = name

#     def __get__(self, obj, cls):
#         if obj is None:
#             return self
#         if self._attr not in obj.__dict__:
#             raise AttributeError('Атрибут не найден')
#         return obj.__dict__[self._attr]

#     def __set__(self, obj, value):
#         if value in kwlist:
#             raise ValueError('Некорректное значение')
#         obj.__dict__[self._attr] = value