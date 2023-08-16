''' Первый вариант решения'''
from collections import UserList


def decorator_lst(func):
    def wrapper(self, args=[]):
        if isinstance(args, (list, NumberList)):
            if all([self.chek_int(i) for i in args]):
                return func(self, args)
            else:
                raise TypeError('Элементами экземпляра класса NumberList' +
                                ' должны быть числа')
        else:
            if self.chek_int(args):
                return func(self, args)
            else:
                raise TypeError('Элементами экземпляра класса NumberList' +
                                ' должны быть числа')
    return wrapper


class NumberList(UserList):
    @decorator_lst
    def __init__(self, iterable=[]):
        return super().__init__(iterable)

    @decorator_lst
    def __add__(self, other):
        return super().__add__(other)

    @decorator_lst
    def __radd__(self, other):
        return super().__radd__(other)

    @decorator_lst
    def __iadd__(self, other):
        return super().__iadd__(other)

    @decorator_lst
    def append(self, item):
        return super().append(item)

    @decorator_lst
    def extend(self, other):
        return super().extend(other)

    def insert(self, i, item):
        if self.chek_int(item):
            return super().insert(i, item)
        raise TypeError('Элементами экземпляра класса NumberList' +
                        ' должны быть числа')

    def chek_int(self, num):
        return isinstance(num, (int, float))
''' Второй вариант решения'''    
# from collections import UserList


# class NumberList(UserList):
#     def __init__(self, iterable=()):
#         super().__init__(self._validate(item) for item in iterable)

#     @staticmethod
#     def _validate(value):
#         if isinstance(value, (int, float)):
#             return value
#         raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

#     def insert(self, index, item):
#         self.data.insert(index, self._validate(item))

#     def append(self, item):
#         self.data.append(self._validate(item))

#     def extend(self, other):
#         if isinstance(other, type(self)):
#             self.data.extend(other)
#         else:
#             self.data.extend(self._validate(item) for item in other)

#     def __add__(self, other):
#         if isinstance(other, (type(self), list)):
#             return super().__add__(self._validate(item) for item in other)
#         return NotImplemented

#     def __iadd__(self, other):
#         super().__iadd__(self._validate(item) for item in other)
#         return self