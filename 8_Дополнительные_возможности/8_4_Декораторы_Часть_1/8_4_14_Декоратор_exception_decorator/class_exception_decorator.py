''' Первый вариант решения'''
import functools


class exception_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            result = self.func(*args, **kwargs)
            return result, None
        except TypeError:
            return None, TypeError
''' Второй вариант решения'''    
# import functools


# class exception_decorator:
#     def __init__(self, func):
#         functools.update_wrapper(self, func)
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         try:
#             value = self.func(*args, **kwargs)
#             return value, None
#         except Exception as e:
#             return None, type(e)
