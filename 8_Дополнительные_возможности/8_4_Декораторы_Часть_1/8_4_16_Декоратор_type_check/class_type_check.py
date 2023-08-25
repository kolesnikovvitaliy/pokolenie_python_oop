''' Первый вариант решения'''
import functools


class type_check:
    def __init__(self, types):
        self.types = iter(types)

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            all_arg = zip(self.types, args)
            arg = map(lambda x: True if type(x[1]) == x[0] else False, all_arg)
            if not all(arg):
                raise TypeError
            result = func(*args, **kwargs)
            return result
        return wrapper

''' Второй вариант решения'''    
# import functools


# class type_check:
#     def __init__(self, types):
#         self.types = types

#     def __call__(self, func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for arg, arg_type in zip(args, self.types):
#                 if not isinstance(arg, arg_type):
#                     raise TypeError
#             value = func(*args, **kwargs)
#             return value

#         return wrapper