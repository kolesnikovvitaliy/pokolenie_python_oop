''' Первый вариант решения'''

class Vector:
    def __init__(self, x: int=0, y: int=0):
        self.x = x
        self.y = y

    def abs(self):
        return f'{(pow(((self.x**2) + (self.y**2)), 0.5))}'
''' Второй вариант решения'''    
# from math import sqrt

# class Vector:
#     def __init__(self, x=0, y=0):
#         self.x, self.y = x, y
        
#     def abs(self):
#         return sqrt(self.x**2 + self.y**2)