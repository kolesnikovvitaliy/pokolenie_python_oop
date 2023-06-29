''' Первый вариант решения'''
from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    
    @format.register(int)
    @staticmethod
    def _int_format(data):
        print(f'Целое число: {data}')

    @format.register(float)
    @staticmethod
    def _int_format(data):
        print(f'Вещественное число: {data}')

    @format.register(tuple)
    @staticmethod
    def _int_format(data):
        print(f"Элементы кортежа: {', '.join(map(str,data))}")

    @format.register(list)
    @staticmethod
    def _int_format(data):
        print(f"Элементы списка: {', '.join(map(str,data))}")

    @format.register(dict)
    @staticmethod
    def _int_format(data):
        print(f"Пары словаря: {', '.join(map(str,data.items()))}")
''' Второй вариант решения'''    
# from functools import singledispatchmethod

# class Formatter:
#     @singledispatchmethod
#     @staticmethod
#     def format(data):
#         raise TypeError('Аргумент переданного типа не поддерживается')
    
#     @format.register(int)
#     @staticmethod
#     def _(data):
#         print(f'Целое число: {data}')
    
#     @format.register(float)
#     @staticmethod
#     def _(data):
#         print(f'Вещественное число: {data}')
    
#     @format.register(tuple)
#     @staticmethod
#     def _(data):
#         print(f'Элементы кортежа: {", ".join([str(obj) for obj in data])}')
    
#     @format.register(list)
#     @staticmethod
#     def _(data):
#         print(f'Элементы списка: {", ".join([str(obj) for obj in data])}')
    
#     @format.register(dict)
#     @staticmethod
#     def _(data):
#         print(f'Пары словаря: {", ".join([str(pair) for pair in data.items()])}')