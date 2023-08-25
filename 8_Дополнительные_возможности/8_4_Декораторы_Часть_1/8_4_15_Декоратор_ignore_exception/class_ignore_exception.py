''' Первый вариант решения'''
import functools


class ignore_exception:
    def __init__(self, *args):
        self.args = args

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as error:
                if type(error) in self.args:
                    print(f'Исключение {type(error).__name__} обработано')
                else:
                    raise type(error)
        return wrapper
''' Второй вариант решения'''    
# import functools


# class ignore_exception:
#     def __init__(self, *exceptions):
#         self.exceptions = exceptions

#     def __call__(self, func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 value = func(*args, **kwargs)
#                 return value
#             except self.exceptions as e:
#                 print(f'Исключение {e.__class__.__name__} обработано')

#         return wrapper