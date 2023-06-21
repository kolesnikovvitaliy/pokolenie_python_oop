''' Первый вариант решения'''
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.radius*2
        self.area = pi*(self.radius**2)

''' Второй вариант решения'''    
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#         self.diameter = radius * 2
#         self.area = __import__('math').pi * radius ** 2