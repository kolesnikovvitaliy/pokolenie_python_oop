''' Первый вариант решения'''
class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iterable):
        cls.a, cls.b, cls.c = iterable
        return cls

    @classmethod
    def from_str(cls, text):
        cls.a, cls.b, cls.c = map(float, text.split())
        return cls
''' Второй вариант решения'''    
# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.a, self.b, self.c = a, b, c

#     @classmethod
#     def from_iterable(cls, iterable):
#         return cls(*iterable)

#     @classmethod
#     def from_str(cls, string):
#         iterable = (float(digit) for digit in string.split())
#         return cls.from_iterable(iterable)