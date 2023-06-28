''' Первый вариант решения'''
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        cls.radius = diameter / 2
        return cls
''' Второй вариант решения'''    
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     @classmethod
#     def from_diameter(cls, diameter):
#         return cls(diameter / 2)