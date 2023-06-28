''' Первый вариант решения'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @classmethod
    def square(cls, side):
        return cls(side, side)
''' Второй вариант решения'''    
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     @property
#     def length(self):
#         return self._length

#     @length.setter
#     def length(self, length):
#         self._length = length

#     @property
#     def width(self):
#         return self._width

#     @width.setter
#     def width(self, width):
#         self._width = width

#     @classmethod
#     def square(cls, side):
#         return cls(side, side)