''' Первый вариант решения'''
from collections import UserString
from copy import copy


class MutableString(UserString):
    def __init__(self, string):
        super().__init__(string)

    def __setitem__(self, key, item):
        __lst = list(self.data)
        __lst[key] = item
        self.data = ''.join(copy(__lst))
        return self

    def __delitem__(self, key):
        __lst = list(self.data)
        del __lst[key]
        self.data = ''.join(copy(__lst))
        return self

    def lower(self):
        self.data = copy(self.data.lower())
        return self

    def upper(self):
        self.data = copy(self.data.upper())
        return self

    def sort(self, key=lambda x: x, reverse=False):
        self.data = ''.join(sorted(self.data, key=key, reverse=reverse))
        return self
''' Второй вариант решения'''    
# from collections import UserString


# class MutableString(UserString):
#     def __setitem__(self, index, value):
#         data_as_list = list(self.data)
#         data_as_list[index] = value
#         self.data = "".join(data_as_list)

#     def __delitem__(self, index):
#         data_as_list = list(self.data)
#         del data_as_list[index]
#         self.data = "".join(data_as_list)

#     def upper(self):
#         self.data = self.data.upper()

#     def lower(self):
#         self.data = self.data.lower()

#     def sort(self, key=None, reverse=False):
#         self.data = "".join(sorted(self.data, key=key, reverse=reverse))