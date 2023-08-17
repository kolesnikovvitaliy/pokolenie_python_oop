''' Первый вариант решения'''
from collections.abc import Sequence


class SortedList(Sequence):
    def __init__(self, iterable=[]):
        self.iterable = sorted(iterable)

    def add(self, other):
        if isinstance(other, int):
            tmp_list = [self.iterable, [other]]
            self.iterable = sorted([i for lst in tmp_list for i in lst])
        else:
            self.__add_list(self, other)
        return self.iterable

    @staticmethod
    def __add_list(self, other):
        tmp_list = [self.iterable, other]
        self.iterable = sorted([i for lst in tmp_list for i in lst])
        return self

    def discard(self, obj):
        self.iterable = [i for i in self.iterable if i != obj]
        return __class__(self.iterable)

    def update(self, obj):
        return __class__.add(self, obj)

    def append(self, item):
        raise NotImplementedError

    def insert(self, index, item):
        raise NotImplementedError

    def extend(self, item):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def __repr__(self):
        return f'{__class__.__name__}({self.iterable})'

    def __len__(self):
        return len(self.iterable)

    def __reversed__(self):
        raise NotImplementedError

    def __iter__(self):
        yield from self.iterable

    def __getitem__(self, index):
        return self.iterable[index]

    def __setitem__(self, index, item):
        raise NotImplementedError

    def __delitem__(self, index):
        del self.iterable[index]

    def __add__(self, other):
        if isinstance(other, __class__):
            tmp_list = [self.iterable, other]
            self = sorted([i for lst in tmp_list for i in lst])
            return __class__(self)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, __class__):
            self.__add_list(self, other)
            return self
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, int):
            self.iterable = sorted(self.iterable * n)
            return self
        return NotImplemented

    def __imul__(self, n):
        if isinstance(n, int):
            self.iterable = sorted(self.iterable * n)
            return self
        return NotImplemented
''' Второй вариант решения'''    
# from collections.abc import Sequence
# class SortedList(Sequence):
#     def __init__(self, iterable=()):
#         self.iterable = sorted(iterable)

#     def __getitem__(self, index):
#         return self.iterable[index]

#     def __setitem__(self, index, value):
#         raise NotImplementedError

#     def __reversed__(self):
#         raise NotImplementedError

#     def append(self, other):
#         raise NotImplementedError

#     def insert(self, index, other):
#         raise NotImplementedError

#     def extend(self, other):
#         raise NotImplementedError

#     def reverse(self):
#         raise NotImplementedError

#     def __delitem__(self, key):
#         del self.iterable[key]

#     def __len__(self):
#         return len(self.iterable)

#     def add(self, other):
#         self.iterable.append(other)

#     def discard(self, other):
#         self.iterable = list(filter(lambda x: x != other, self.iterable))

#     def update(self, other):
#         self.iterable.extend(other)
#         self.iterable = sorted(self.iterable)

#     def __add__(self, other):
#         if isinstance(other, type(self)):
#             return SortedList(self.iterable + other.iterable)
#         return NotImplemented

#     def __iadd__(self, other):
#         if not isinstance(other, SortedList):
#             return NotImplemented
#         self.iterable += other.iterable
#         self.iterable.sort()
#         return self

#     def __mul__(self, n):
#         if isinstance(n, int):
#             return SortedList(sorted(self.iterable * n))
#         return NotImplemented

#     def __imul__(self, n):
#         if not isinstance(n, int):
#             return NotImplemented
#         self.iterable = self.iterable * n
#         self.iterable.sort()
#         return self

#     def __str__(self):
#         return f"SortedList({sorted(self.iterable)})"