''' Первый вариант решения'''
class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def perimeter(self):
        return self._a + self._b + self._c


class EquilateralTriangle(Triangle):
    def __init__(self, said):
        super().__init__(said, said, said)
''' Второй вариант решения'''    
# class Triangle:
#     def __init__(self, a, b, c):
#         self._a, self._b, self._c = a, b, c
        
#     def perimeter(self):
#         return sum((self._a, self._b, self._c))
    
    
# class EquilateralTriangle(Triangle):
#     def __init__(self, side):
#         super().__init__(side, side, side)