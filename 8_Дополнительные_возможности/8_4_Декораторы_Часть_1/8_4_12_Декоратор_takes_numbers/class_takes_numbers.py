''' Первый вариант решения'''
import functools


class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        arg = [isinstance(i, (int, float)) for i in args]
        kwarg = [isinstance(i, (int, float)) for i in kwargs.values()]
        if not all(arg + kwarg):
            raise TypeError('Аргументы должны принадлежать типам int или float')
        return self.func(*args, **kwargs)
''' Второй вариант решения'''    
# import functools


# class takes_numbers:
#     def __init__(self, func):
#         functools.update_wrapper(self, func)
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         if any((
#                 not all(isinstance(arg, (int, float)) for arg in args),
#                 not all(isinstance(arg, (int, float)) for arg in kwargs.values())
#         )):
#             raise TypeError('Аргументы должны принадлежать типам int или float')
#         return self.func(*args, **kwargs)