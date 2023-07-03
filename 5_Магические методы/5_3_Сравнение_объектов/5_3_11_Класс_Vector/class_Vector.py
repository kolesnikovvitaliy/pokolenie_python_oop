''' Первый вариант решения'''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"{__class__.__name__}({self.x}, {self.y})"

    
    def __eq__(self, __value) -> bool:
        if isinstance(__value, tuple) or isinstance(__value, list):
            if  len(__value) == 2 and map(int, __value):
                return self.x == __value[0] and self.y == __value[1]
            return NotImplemented
        elif isinstance(__value, Vector):
            return self.x == __value.x and self.y == __value.y
        return NotImplemented
''' Второй вариант решения'''    
# class Vector:
#     def __init__(self, x, y):
#         self.x, self.y = x, y

#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'

#     def __eq__(self, other):
#         if isinstance(other, tuple) and len(other) == 2:
#             return (self.x, self.y) == other
#         elif isinstance(other, Vector):
#             return self.x == other.x and self.y == other.y
#         return NotImplemented