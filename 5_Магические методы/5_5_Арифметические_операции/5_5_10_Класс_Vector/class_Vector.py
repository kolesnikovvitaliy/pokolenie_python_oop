''' Первый вариант решения'''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{__class__.__name__}({self.x}, {self.y})"
    
    def __add__(self, other):
        if isinstance(other, __class__):
            x,y = map(sum, zip(self.__dict__.values(), other.__dict__.values()))
            return __class__(x, y)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, __class__):
            x,y = map(lambda a,b: a - b, self.__dict__.values(), other.__dict__.values())
            return __class__(x, y)
        return NotImplemented
    
    def __mul__(self, n):
        if isinstance(n, (int, float)):
            x,y = map(lambda a: a * n, self.__dict__.values())
            return __class__(x, y)
        return NotImplemented
    
    def __rmul__(self, n):
        return self.__mul__(n)
    
    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            x,y = map(lambda a: a / n, self.__dict__.values())
            return __class__(x, y)
        return NotImplemented
    
    def __rtruediv__(self, n):
        return self.__truediv__(n)
''' Второй вариант решения'''    
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'

#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x + other.x, self.y + other.y)
#         return NotImplemented

#     def __sub__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x - other.x, self.y - other.y)
#         return NotImplemented

#     def __mul__(self, other):
#         if isinstance(other, (int, float)):
#             return Vector(self.x * other, self.y * other)
#         return NotImplemented

#     def __rmul__(self, other):
#         return self.__mul__(other)

#     def __truediv__(self, other):
#         if isinstance(other, (int, float)):
#             return Vector(self.x / other, self.y / other)
#         return NotImplemented