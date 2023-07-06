''' Первый вариант решения'''
class ColoredPoint:
    def __init__(self, x, y, color=(0, 0, 0, )):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"{__class__.__name__}({self.x}, {self.y}, {self.color})"
    
    def __pos__(self):
        return __class__(self.x, self.y, self.color)
    
    def __neg__(self):
        return __class__(self.x*-1, self.y*-1, self.color)
    
    def __invert__(self):
        if self.color == (0, 0, 0):
            return __class__(self.y, self.x, self.color)
        else:
            __color = tuple(255-i for i in self.color)
            return __class__(self.y, self.x, __color)
''' Второй вариант решения'''    
# class ColoredPoint:
#     def __init__(self, x, y, color=(0, 0, 0)):
#         self.x = x
#         self.y = y
#         self.color = color
        
#     def __str__(self):
#         return f'({self.x}, {self.y})'
        
#     def __repr__(self):
#         return f'ColoredPoint({self.x}, {self.y}, {self.color})'
    
#     def __pos__(self):
#         return ColoredPoint(self.x, self.y, self.color)
    
#     def __neg__(self):
#         return ColoredPoint(-self.x, -self.y, self.color)
    
#     def __invert__(self):
#         return ColoredPoint(self.y, self.x, tuple(255 - c for c in self.color))