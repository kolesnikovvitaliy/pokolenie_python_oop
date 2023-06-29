''' Первый вариант решения'''
from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _int_neg(data):
        return -data
    
    @neg.register(bool)
    @staticmethod
    def _bool_neg(data):
        return not data
''' Второй вариант решения'''    
# from functools import singledispatchmethod


# class Negator:
#     @singledispatchmethod
#     @staticmethod
#     def neg(data):
#         raise TypeError('Аргумент переданного типа не поддерживается')
    
#     @neg.register(int)
#     @neg.register(float)
#     @staticmethod
#     def _int_neg(data):
#         return arg * (-1)
    
#     @neg.register(bool)
#     @staticmethod
#     def _bool_neg(data):
#         return bool([1, 0][data])