''' Первый вариант решения'''
class CyclicList:
    def __init__(self, iterable):
        self.iterable = iterable.copy()
        
    def append(self, obj):
        self.iterable.append(obj)

    def pop(self, index=None):
        if index is None:
            return self.iterable.pop()
        return self.iterable.pop(index)

    def __len__(self):
        return len(self.iterable)

    def __iter__(self):
        for _ in self.iterable:
            yield from self.iterable
            
    def __getitem__(self, key):
        if len(self.iterable) < key:
            key = key % len(self.iterable)
            return self.iterable[key]
        return self.iterable[key]
''' Второй вариант решения'''    
# from itertools import cycle


# class CyclicList:
#     def __init__(self, iterable=()):
#         self._data = list(iterable) or []

#     def append(self, item):
#         self._data.append(item)

#     def pop(self, index=None):
#         if index is None:
#             return self._data.pop()
#         return self._data.pop(index)

#     def __len__(self):
#         return len(self._data)

#     def __iter__(self):
#         yield from cycle(self._data)

#     def __getitem__(self, index):
#         return self._data[index % len(self._data)]