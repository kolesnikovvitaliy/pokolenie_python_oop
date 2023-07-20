''' Первый вариант решения'''
class Grouper:
    def __init__(self, iterable, key):
        self._func = key
        self._dict = dict()
        {self.add(item) for item in iterable}

    def add(self, item):
        if self._func(item) in self._dict:
            self._dict[self._func(item)].append(item)
        else:
            self._dict.setdefault(self._func(item),[]).append(item)
    
    def group_for(self, item):
        return self._func(item)
    
    def __len__(self):
        return len(self._dict)
    
    def __iter__(self):
        yield from self._dict.items()

    def __contains__(self, item):
        return item in self._dict
    
    def __getitem__(self, key):
        return self._dict[key]
''' Второй вариант решения'''    
# class Grouper:
#     def __init__(self, iterable, key):
#         self._iterable = list(iterable)
#         self._key = key
#         self._make_groups(self._iterable)

#     def _make_groups(self, iterable):
#         self._groups = {}
#         for item in iterable:
#             self.add(item)

#     def add(self, item):
#         self._groups.setdefault(self._key(item), []).append(item)

#     def group_for(self, item):
#         return self._key(item)

#     def __len__(self):
#         return len(self._groups)

#     def __iter__(self):
#         return iter(self._groups.items())

#     def __contains__(self, item):
#         return item in self._groups

#     def __getitem__(self, key):
#         return self._groups[key]