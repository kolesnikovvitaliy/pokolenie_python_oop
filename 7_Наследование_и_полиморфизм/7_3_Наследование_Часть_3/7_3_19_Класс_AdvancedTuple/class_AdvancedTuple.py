''' Первый вариант решения'''
class AdvancedTuple(tuple):
    def __add__(self, other):
        return __class__((tuple(self) + tuple(other)))

    def __iadd__(self, other):
        return __class__((tuple(self) + tuple(other)))

    def __radd__(self, other):
        return __class__(tuple(other) + tuple(self))
''' Второй вариант решения'''    
# class AdvancedTuple(tuple):
#     def __add__(self, other):
#         if hasattr(other, '__iter__'):
#             return AdvancedTuple(super().__add__(tuple(other)))

#     def __radd__(self, other):
#         return tuple(other).__add__(self)