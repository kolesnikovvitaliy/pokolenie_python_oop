''' Первый вариант решения'''
class OrderedSet:
    def __init__(self, iterable=None):
        if iterable:
            self.iterable = {k: None for k in iterable.copy()} 
        else:
            self.iterable = dict() 

    def add(self, __value):
        self.iterable[__value] = None

    def discard(self, __value):
        if __value in self.iterable:
            del self.iterable[__value]
        return self.iterable
        
    
    def __len__(self):
        return len(self.iterable)

    def __iter__(self):
        yield from self.iterable

    # def __next__(self):
    #     # return self.iterable 
    #     pass

    def __contains__(self, item):
        return item in self.iterable

    def __eq__(self, __value: object):
        if isinstance(__value, __class__):
            if len(self.iterable) == len(__value.iterable):
                if False in (map(lambda x, y: x == y, self.iterable, __value.iterable)):
                    return False
                return True
        elif isinstance(__value, set):
            if len(self.iterable) == len(__value):
                if not set(self.iterable).isdisjoint(__value):
                    return True
            return False
        else:
            return NotImplemented
''' Второй вариант решения'''    
# class OrderedSet:
#     def __init__(self, iterable=()):
#         self._data = dict.fromkeys(iterable, None)

#     def __len__(self):
#         return len(self._data)

#     def add(self, item):
#         self._data.setdefault(item, None)

#     def discard(self, item):
#         self._data.pop(item, None)

#     def __iter__(self):
#         yield from self._data

#     def __eq__(self, other):
#         if isinstance(other, OrderedSet):
#             return len(self._data) == len(other._data) and all(x == y for x, y in zip(self._data, other._data))
#         if isinstance(other, set):
#             return set(self._data) == other
#         return NotImplemented