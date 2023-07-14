''' Первый вариант решения'''
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def _lst(self):
        return self.x, self.y, self.z

    def __repr__(self) -> str:
        return f"{__class__.__name__}{self._lst}"
    
    def __iter__(self):
        yield from self._lst
''' Второй вариант решения'''    
# class Point:
#     def __init__(self, x, y, z):
#         self.x, self.y, self.z = x, y, z

#     def __repr__(self):
#         return f'Point({self.x}, {self.y}, {self.z})'

#     def __iter__(self):
#         yield from (self.x, self.y, self.z)