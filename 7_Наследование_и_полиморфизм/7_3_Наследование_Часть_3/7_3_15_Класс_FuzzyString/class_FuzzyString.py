''' Первый вариант решения'''
class FuzzyString(str):
    def __new__(cls, obj=''):
        obj = super().__new__(cls, str(obj).lower())
        return obj

    def __eq__(self, other):
        if isinstance(other, (str)):
            return len(self) == len(other)
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, (str)):
            return len(self) != len(other)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, (str)):
            return len(self) < len(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, (str)):
            return len(self) > len(other)
        return NotImplemented

    def __contains__(self, other):
        return self in other.lower()

    def __le__(self, other):
        if isinstance(other, str):
            return self.__lt__(other) or self.__eq__(other)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, str):
            return not self.__lt__(other)
        return NotImplemented
''' Второй вариант решения'''    
# from functools import total_ordering

# @total_ordering
# class FuzzyString(str):
    
#     def __le__(self, other):
#         if isinstance(other, str):
#             return self.lower() <= other.lower()
#         return NotImplemented

#     def __eq__(self, other):
#         if isinstance(other, str):
#             return self.lower() == other.lower()
#         return NotImplemented

#     def __contains__(self, substring):
#         if isinstance(substring, str):
#             return substring.lower() in self.lower()
#         return NotImplemented
    
#     __lt__ = getattr(object, '__lt__', None)
#     __gt__ = getattr(object, '__gt__', None)
#     __ge__ = getattr(object, '__ge__', None)
#     __ne__ = getattr(object, '__ne__', None)