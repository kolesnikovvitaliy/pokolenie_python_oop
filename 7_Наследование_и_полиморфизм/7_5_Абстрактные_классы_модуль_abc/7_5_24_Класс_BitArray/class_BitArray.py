''' Первый вариант решения'''
from collections.abc import Sequence


class BitArray(Sequence):
    def __init__(self, iterable=[]):
        self.lst = iterable[:]

    def __str__(self):
        return f"{self.lst}"

    def __iter__(self):
        return iter(self.lst)

    def __contains__(self, value):
        return value in self.lst

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, index):
        return self.lst[index]

    def __invert__(self):
        return __class__(list(
            map(lambda x: 1 if x == 0 else 0, self.lst)))

    def __or__(self, other):
        if isinstance(other, __class__):
            return __class__(list(
                map(lambda x, y: x | y, self.lst, other.lst)))
        return NotImplemented

    def __and__(self, other):
        if isinstance(other, __class__):
            return __class__(list(
                map(lambda x, y: x & y, self.lst, other.lst)))
        return NotImplemented
''' Второй вариант решения'''    
# from collections.abc import Sequence


# class BitArray(Sequence):
#     def __init__(self, iterable=()):
#         self._data = list(iterable)

#     def __str__(self):
#         return str(self._data)

#     def __len__(self):
#         return len(self._data)

#     def __getitem__(self, index):
#         if isinstance(index, (int, slice)):
#             return self._data[index]
#         return NotImplemented

#     def __invert__(self):
#         return type(self)(int(not item) for item in self._data)

#     def __or__(self, other):
#         if isinstance(other, type(self)):
#             return type(self)(self_item | other_item for self_item, other_item in zip(self._data, other._data))
#         return NotImplemented

#     def __and__(self, other):
#         if isinstance(other, type(self)):
#             return type(self)(self_item & other_item for self_item, other_item in zip(self._data, other._data))
#         return NotImplemented