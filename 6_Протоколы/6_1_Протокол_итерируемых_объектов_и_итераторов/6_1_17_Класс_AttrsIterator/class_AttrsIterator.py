''' Первый вариант решения'''
class AttrsIterator:
    def __init__(self, object):
        self.__lst_object = list(object.__dict__.items())
        self.__i = 0

    def __iter__(self):
        yield from self.__lst_object
    
    def __next__(self):
        if self.__i > len(self.__lst_object)-1:
            raise StopIteration
        self.__i += 1
        return self.__lst_object[self.__i-1]
''' Второй вариант решения'''    
# class AttrsIterator:
#     def __init__(self, obj):
#         self.iterator = iter(obj.__dict__.items())
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         return next(self.iterator)