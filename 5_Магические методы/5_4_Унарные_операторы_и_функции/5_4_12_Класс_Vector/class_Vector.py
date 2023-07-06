''' Первый вариант решения'''
class Vector:
    def __init__(self, x: int, y: int) -> str:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "({}, {})".format(self.x, self.y)

    def __repr__(self) -> str:
        return "{}({}, {})".format(__class__.__name__, self.x, self.y)
    
    def __pos__(self):
        return __class__(self.x, self.y)
    
    def __neg__(self):
        return __class__(self.x*-1, self.y*-1)
    
    def __abs__(self):
        return pow((self.x**2 + self.y**2), 0.5)
''' Второй вариант решения'''    
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __str__(self):
#         return f'({self.x}, {self.y})'
    
#     def __repr__(self):
#         return f'Vector{self.__str__()}'
    
#     def __pos__(self):
#         return Vector(self.x, self.y)
    
#     def __neg__(self):
#         return Vector(-self.x, -self.y)
    
#     def __abs__(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5