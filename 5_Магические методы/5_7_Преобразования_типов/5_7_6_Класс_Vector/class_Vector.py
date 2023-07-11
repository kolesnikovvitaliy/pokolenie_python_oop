''' Первый вариант решения'''
class Vector: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__vector = pow((self.x**2 + self.y**2),0.5)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __bool__(self):
        return self.x != 0 or self.y != 0
    
    def __int__(self):
        return abs(int(self.__vector))
    
    def __float__(self):
        return abs(float(self.__vector))
    
    def __complex__(self):
        return complex(self.x, self.y)
''' Второй вариант решения'''    
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return "({}, {})".format(self.x, self.y)
    
#     def __bool__(self):
#         return not not (self.x or self.y)
    
#     def __int__(self):
#         return int((self.x**2 + self.y**2)**0.5)
    
#     def __float__(self):
#         return float((self.x**2 + self.y**2)**0.5)
    
#     def __complex__(self):
#         return complex(self.x, self.y)