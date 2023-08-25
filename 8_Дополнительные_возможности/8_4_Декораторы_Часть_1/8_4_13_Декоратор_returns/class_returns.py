''' Первый вариант решения'''
import functools


class returns:
    def __init__(self, datatype):
        self.datatype = datatype

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, self.datatype):
                return result
            raise TypeError
        return wrapper
''' Второй вариант решения'''    
# import functools


# class returns:
#     def __init__(self, datatype):
#         self.datatype = datatype

#     def __call__(self, func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             value = func(*args, **kwargs)
#             if not isinstance(value, self.datatype):
#                 raise TypeError
#             return value

#         return wrapper