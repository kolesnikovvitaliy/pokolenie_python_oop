''' Первый вариант решения'''
class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a 
        self.b = b 
        self.c = c
    
    def __call__(self, x):
        return self.a*x**2 + self.b*x + self.c
''' Второй вариант решения'''    
# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.a, self.b, self.c = a, b, c
        
#     def __call__(self, x):
#         return self.a * (x ** 2) + self.b * x + self.c