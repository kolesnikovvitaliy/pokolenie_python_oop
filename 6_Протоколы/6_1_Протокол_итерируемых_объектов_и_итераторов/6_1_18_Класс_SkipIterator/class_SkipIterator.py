''' Первый вариант решения'''
class SkipIterator:
    def __init__(self, iterable, n) -> None:
        self.iterable = list(iterable)
        self.n = n
        self.__i = 0

    def __iter__(self):
        return self

    def __next__(self):
        __lst = self.iterable[0::self.n+1]
        if self.__i >= len(__lst):
            raise StopIteration
        self.__i += 1
        return __lst[self.__i-1]
''' Второй вариант решения'''    
# class SkipIterator:
#     def __init__(self, iterable, n):
#         self.iterable = iter(iterable)
#         self.n = n
#         self.first = True

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.first:
#             self.first = False
#             return next(self.iterable)
#         for _ in range(self.n):
#             next(self.iterable)
#         return next(self.iterable)