''' Первый вариант решения'''
class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def color(self):
        return self._color

    def __repr__(self):
        return f"{__class__.__name__}({self.x}, {self.y}, '{self.color}')"
    
    def __eq__(self, __value: object):
        if isinstance(__value, __class__):
            return self.x == __value.x and self.y == __value.y and self.color == __value.color
        return NotImplemented
    
    def __ne__(self, __value: object):
        if isinstance(__value, __class__):
            return self.x != __value.x or self.y != __value.y or self.color != __value.color
        return NotImplemented
    
    def __hash__(self):
        return hash((self.x, self.y, self.color))
''' Второй вариант решения'''    
# class ColoredPoint:
#     def __init__(self, x, y, color):
#         self._x = x
#         self._y = y
#         self._color = color
         
#     @property
#     def x(self):
#         return self._x
    
#     @property
#     def y(self):
#         return self._y
    
#     @property
#     def color(self):
#         return self._color

#     @property
#     def _fields(self):
#         return self._x, self._y, self._color
    
#     def __repr__(self):
#         return "ColoredPoint({}, {}, '{}')".format(*self._fields)

#     def __eq__(self, other):
#         if isinstance(other, ColoredPoint):
#             return self._fields == other._fields
#         return NotImplemented

#     def __hash__(self):
#         return hash(self._fields)