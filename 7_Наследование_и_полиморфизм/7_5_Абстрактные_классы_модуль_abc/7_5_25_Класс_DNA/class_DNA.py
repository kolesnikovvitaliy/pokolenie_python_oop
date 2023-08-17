''' Первый вариант решения'''
from collections.abc import Sequence


class DNA(Sequence):
    def __init__(self, chain):
        self.dna = chain
        self._lst = self.combinations(chain)

    @staticmethod
    def combinations(data):
        __lst = []
        for i in data:
            if i == 'A':
                __lst.append(('A', 'T'))
            if i == 'G':
                __lst.append(('G', 'C'))
            if i == 'T':
                __lst.append(('T', 'A'))
            if i == 'C':
                __lst.append(('C', 'G'))
        return __lst

    def __str__(self):
        return ''.join(self.dna)

    def __getitem__(self, index):
        return self._lst[index]

    def __len__(self):
        return len(self.dna)

    def __reversed__(self):
        a = [i for i in reversed(self.dna)]
        return __class__(a)

    def __contains__(self, value):
        return value in self.dna

    def __eq__(self, __value):
        if isinstance(__value, __class__):
            return self._lst[0] == __value._lst[0]
        return NotImplemented

    def __ne__(self, __value):
        if isinstance(__value, __class__):
            return self._lst[0] != __value._lst[0]
        return NotImplemented

    def __add__(self, obj):
        if isinstance(obj, __class__):
            return __class__(f'{self.dna}{obj.dna}')
        return NotImplemented
''' Второй вариант решения'''    
# from collections.abc import Sequence


# class DNA(Sequence):
#     __BASE = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}

#     def __init__(self, chain):
#         self._chain = chain

#     def __str__(self):
#         return self._chain

#     def __len__(self):
#         return len(self._chain)

#     def __getitem__(self, index):
#         if isinstance(index, (int, slice)):
#             return self._chain[index], type(self).__BASE[self._chain[index]]
#         return NotImplemented

#     def __eq__(self, other):
#         if isinstance(other, type(self)):
#             return self._chain == other._chain
#         return NotImplemented

#     def __add__(self, other):
#         if isinstance(other, type(self)):
#             return type(self)(self._chain + other._chain)
#         return NotImplemented

#     def __contains__(self, item):
#         return item in self._chain