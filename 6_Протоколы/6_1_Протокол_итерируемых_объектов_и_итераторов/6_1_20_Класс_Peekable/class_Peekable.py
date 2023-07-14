''' Первый вариант решения'''
class Peekable:
    def __init__(self, iterables):
        self.iterables = list(iterables)
        self.__i = 0

    def peek(self, default=StopIteration):
        if self.__i >= len(self.iterables):
            if default == StopIteration:
                raise default
            else:
                return default
        return self.iterables[self.__i]

    def __iter__(self):
        return self

    def __next__(self):
        if self.__i >= len(self.iterables):
            raise StopIteration
        self.__i += 1
        return self.iterables[self.__i-1]
''' Второй вариант решения'''    
# class Peekable:
#     def __init__(self, iterable):
#         self.iterable = list(iterable)
#         self.index = -1 
    
#     def peek(self, default=StopIteration):
#         try:
#             return self.iterable[self.index + 1]
#         except:
#             if default == StopIteration:
#                 raise default
#             else:
#                 return default
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self.index += 1
#         if self.index == len(self.iterable):
#             raise StopIteration
#         return self.iterable[self.index]