''' Первый вариант решения'''
class Versioned:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr][-1]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        obj.__dict__.setdefault(self._attr, []).append(value)

    def get_version(self, obj, n: int):
        return obj.__dict__[self._attr][n-1]

    def set_version(self, obj, n: int):
        obj.__dict__[self._attr].append(obj.__dict__[self._attr][n-1])
''' Второй вариант решения'''    
# class Versioned:
#     def __init__(self):
#         self._index = -1

#     def __set_name__(self, owner, name):
#         self._attr = name

#     def __get__(self, obj, owner):
#         if obj is None:
#             return self
#         if self._attr in obj.__dict__:
#             return obj.__dict__[self._attr][self._index]
#         raise AttributeError('Атрибут не найден')

#     def __set__(self, obj, value):
#         if self._attr not in obj.__dict__:
#             obj.__dict__[self._attr] = []
#         obj.__dict__[self._attr].append(value)

#     def get_version(self, obj, n):
#         return obj.__dict__[self._attr][n - 1]

#     def set_version(self, obj, n):
#         self._index = n - 1