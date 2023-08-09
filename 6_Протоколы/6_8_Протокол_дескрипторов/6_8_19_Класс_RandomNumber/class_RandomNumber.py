''' Первый вариант решения'''
from random import randint


class RandomNumber:
    _lst: dict = {}

    def __init__(self, start: int, end: int, cache=False):
        self._start = start
        self._end = end
        self._cache = cache
        self._random_int = randint(self._start, self._end)

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if self._cache:
            obj.__dict__.setdefault(self._attr, set()).add(self._random_int)
            return obj.__dict__[self._attr]
        else:
            return randint(self._start, self._end)

    def __set__(self, obj, value):
        raise AttributeError('Изменение невозможно')
''' Второй вариант решения'''    
# from random import randint

# class RandomNumber:
#     def __init__(self, start, end, cache=False):
#         self.start = start
#         self.end = end
#         self.cache = cache
#         self.permanent = randint(self.start, self.end)

#     def __set_name__(self, owner, attr):
#         self._attr = attr

#     def __set__(self, obj, value):
#         raise AttributeError('Изменение невозможно')

#     def __get__(self, obj, owner):
#         if obj is None:
#             return self
#         if not self.cache:
#             return randint(self.start, self.end)
#         return self.permanent