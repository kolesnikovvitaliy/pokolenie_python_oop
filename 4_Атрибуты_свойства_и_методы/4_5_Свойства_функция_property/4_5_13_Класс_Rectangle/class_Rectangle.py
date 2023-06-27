''' Первый вариант решения'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def get_perimeter(self):
        return 2*(self.length+self.width)

    def get_area(self):
        return self.length*self.width
    
    perimeter = property(fget=get_perimeter)
    area = property(fget=get_area)


''' Второй вариант решения'''    
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
     
#     @property
#     def perimeter(self):
#         return 2*(self.length + self.width)

#     @property
#     def area(self):
#         return self.length * self.width