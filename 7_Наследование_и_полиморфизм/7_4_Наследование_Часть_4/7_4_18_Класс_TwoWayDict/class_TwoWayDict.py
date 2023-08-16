''' Первый вариант решения'''
from collections import UserDict


class TwoWayDict(UserDict):
    def __setitem__(self, key, item):
        self.data[key] = item
        self.data[item] = key
''' Второй вариант решения'''    
# from collections import UserDict

# class TwoWayDict(UserDict):
#     def __setitem__(self, key, value):
#         self.data.__setitem__(key, value)
#         self.data.__setitem__(value, key)