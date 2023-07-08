''' Первый вариант решения'''
class SuperString:
    def __init__(self, string: str):
        self.string = string

    def __str__(self) -> str:
        return f'{self.string}'
    
    def __add__(self, other):
        if isinstance(other, __class__):
            return __class__(self.string + other.string)
        return NotImplemented
    
    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return __class__(self.string * n)
        return NotImplemented
    
    def __rmul__(self, n):
        return self.__mul__(n)
    
    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            return __class__(self.string[:len(self.string) // n])
        return NotImplemented
    
    def __lshift__(self, n):
        if isinstance(n, (int, float)):
           if n >= len(self.string):
                return __class__('')
           elif n == 0:
               return __class__(self.string)
           return __class__(self.string[:-n])
        return NotImplemented
    
    def __rshift__(self, n):
        if isinstance(n, (int, float)):
           if n >= len(self.string):
                return __class__('')
           return __class__(self.string[n:])
        return NotImplemented
''' Второй вариант решения'''    
# class SuperString:
#     def __init__(self, string):
#         self.string = string

#     def __str__(self):
#         return self.string

#     def __add__(self, other):
#         if isinstance(other, SuperString):
#             return SuperString(self.string + other.string)
#         return NotImplemented

#     def __mul__(self, other):
#         if isinstance(other, int):
#             return SuperString(self.string * other)
#         return NotImplemented

#     def __rmul__(self, other):
#         return self.__mul__(other)

#     def __truediv__(self, other):
#         if isinstance(other, int):
#             return SuperString(self.string[:len(self.string) // other])
#         return NotImplemented

#     def __lshift__(self, other):
#         if isinstance(other, int):
#             if (length := len(self.string)) <= other:
#                 return SuperString('')
#             else:
#                 return SuperString(self.string[0:length - other])
#         return NotImplemented

#     def __rshift__(self, other):
#         if isinstance(other, int):
#             if len(self.string) <= other:
#                 return SuperString('')
#             else:
#                 return SuperString(self.string[other:])
#         return NotImplemented