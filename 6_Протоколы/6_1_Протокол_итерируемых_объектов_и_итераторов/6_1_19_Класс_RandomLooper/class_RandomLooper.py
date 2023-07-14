''' Первый вариант решения'''
class RandomLooper:
    def __init__(self, *args):
        self.__lst = iter([j for i in args for j in i])

    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.__lst)
''' Второй вариант решения'''    
# import itertools as it
# import random


# class RandomLooper:
#     def __init__(self, *args):
#         self.iterables = list(it.chain(*args))
#         self.length = len(self.iterables)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if not self.length:
#             raise StopIteration
#         self.length -= 1
#         ind = random.randint(0, self.length)
#         return self.iterables.pop(ind)