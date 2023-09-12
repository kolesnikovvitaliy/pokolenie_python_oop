''' Первый вариант решения'''
class Predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __invert__(self):
        def invert_func(*args, **kwargs):
            return not self(*args, **kwargs)
        return __class__(invert_func)

    def __and__(self, other):
        def and_func(*args, **kwargs):
            return self(*args, **kwargs) and other(*args, **kwargs)
        return __class__(and_func)

    def __or__(self, other):
        def or_func(*args, **kwargs):
            return self(*args, **kwargs) or other(*args, **kwargs)
        return __class__(or_func)


def predicate(func):
    return Predicate(func)
''' Второй вариант решения'''    
# class predicate:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         return self.func(*args, **kwargs)

#     def __invert__(self):
#         def not_func(*args, **kwargs):
#             return not self.func(*args, **kwargs)

#         return type(self)(not_func)

#     def __or__(self, other):
#         def or_func(*args, **kwargs):
#             return self.func(*args, **kwargs) or other.func(*args, **kwargs)

#         return type(self)(or_func)

#     def __and__(self, other):
#         def and_func(*args, **kwargs):
#             return self.func(*args, **kwargs) and other.func(*args, **kwargs)

#         return type(self)(and_func)