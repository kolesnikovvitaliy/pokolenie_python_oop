''' Первый вариант решения'''
import functools


def auto_repr(args, kwargs):
    lst_args = [*args]
    lst_kwargs = [*kwargs]

    def wrapper(cls):
        old_repr = cls.__repr__

        @functools.wraps(old_repr)
        def decorator(self):
            tmp = []
            for i in lst_args:
                tmp.append(repr(self.__dict__[i]))
            for i in lst_kwargs:
                tmp.append(f'{i}={repr(self.__dict__[i])}')
            return f'{cls.__name__}({", ".join(map(str,tmp))})'
        cls.__repr__ = decorator
        return cls
    return wrapper
''' Второй вариант решения'''    
# def auto_repr(args, kwargs):
#     def wrapper(cls):
#         def __repr__(self):
#             cls_args = [repr(self.__dict__[k]) for k in args]
#             cls_kwargs = [f'{k}={self.__dict__[k]!r}' for k in kwargs]
#             return f'{type(self).__name__}({", ".join(cls_args + cls_kwargs)})'

#         cls.__repr__ = __repr__
#         return cls

#     return wrapper