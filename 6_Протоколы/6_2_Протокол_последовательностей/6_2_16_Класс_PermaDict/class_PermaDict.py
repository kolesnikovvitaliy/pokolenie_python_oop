''' Первый вариант решения'''
from copy import deepcopy


class PermaDict:
    def __init__(self, data={}):
        self.data = deepcopy(data or {})
    
    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        yield from self.data

    def __setitem__(self, key, __value):
        if key in self.data:
            raise KeyError('Изменение значения по ключу невозможно')
        self.data[key] = __value

    def __getitem__(self, __value):
        return self.data[__value]
    
    def __delitem__(self, key):
        del self.data[key]

''' Второй вариант решения'''    
# class PermaDict:
#     def __init__(self, data=()):
#         self._data = dict(data) or {}

#     def keys(self):
#         return self._data.keys()

#     def values(self):
#         return self._data.values()

#     def items(self):
#         return self._data.items()

#     def __len__(self):
#         return len(self._data)

#     def __iter__(self):
#         return iter(self.keys())

#     def __delitem__(self, key):
#         del self._data[key]

#     def __setitem__(self, key, value):
#         if key in self.keys():
#             raise KeyError('Изменение значения по ключу невозможно')
#         self._data[key] = value

#     def __getitem__(self, key):
#         return self._data[key]