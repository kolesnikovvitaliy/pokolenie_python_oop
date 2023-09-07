''' Первый вариант решения'''
from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    
    @process.register(tuple)
    @staticmethod
    def _tuple_process(data):
        return tuple(sorted(data))
    
    @process.register(str)
    @staticmethod
    def _str_process(data):
        return data.upper()
    
    @process.register(list)
    @staticmethod
    def _list_process(data):
        return sorted(data)

    @process.register(float)
    @staticmethod
    def _list_process(data):
        return data * 2
    
    @process.register(int)
    @staticmethod
    def _list_process(data):
        return data * 2
''' Второй вариант решения'''    
# from functools import singledispatchmethod

# class Processor:
#     @singledispatchmethod
#     @staticmethod
#     def process(data):
#         raise TypeError('Аргумент переданного типа не поддерживается')
        
#     @process.register(float)
#     @process.register(int)
#     @staticmethod
#     def _numeric_process(data):
#         return 2 * data
        
#     @process.register(str)
#     @staticmethod
#     def _str_process(data):
#         return data.upper()
        
#     @process.register(list)
#     @staticmethod
#     def _list_process(data):
#         return sorted(data)
    
#     @process.register(tuple)
#     @staticmethod
#     def _tuple_process(data):
#         return tuple(sorted(data))