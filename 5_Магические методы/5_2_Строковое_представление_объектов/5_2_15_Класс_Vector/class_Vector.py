''' Первый вариант решения'''
class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Вектор на плоскости с координатами ({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"
''' Второй вариант решения'''    
# class Vector:
#     def __init__(self, x, y):
#         self.point = (x, y)
       
#     def __repr__(self):
#         return f'Vector{self.point}'
    
#     def __str__(self):
#         return f'Вектор на плоскости с координатами {self.point}'