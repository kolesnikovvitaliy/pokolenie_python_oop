''' Первый вариант решения'''
class AdvancedList(list):
    def join(self, separator=' '):
        return separator.join(map(str, self))
    
    def map(self, func):
        self[:] = map(func, self)
        return self
        
    def filter(self, func):
        self[:] = filter(func, self)
        return self
''' Второй вариант решения'''    
# class AdvancedList(list):
#     def __init__(self, iterable=(), default=None):
#         super().__init__(item for item in iterable)
#         self._default = default

#     def extend_self(self, data):
#         self.clear()
#         self.extend(data)

#     def join(self, sep=' '):
#         return sep.join(str(item) for item in self)

#     def map(self, func):
#         new_data = list(func(item) for item in self)
#         self.extend_self(new_data)

#     def filter(self, predicate):
#         new_data = list(filter(predicate, self))
#         self.extend_self(new_data)