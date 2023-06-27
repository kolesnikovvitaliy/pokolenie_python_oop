''' Первый вариант решения'''
class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.__d = (self.b ** 2) - (4 * self.a * self.c)
        

    @property
    def x1(self):
        if self.__d >= 0:
            return (-self.b - pow(((self.b**2) - (4 * self.a * self.c)), 0.5)) / (2 * self.a)
    
    @property
    def x2(self):
        if self.__d >= 0:
            return (-self.b + pow(((self.b**2) - (4 * self.a * self.c)), 0.5)) / (2 * self.a)
        else:
            return None
        
    @property    
    def view(self):
        return str(self.a) + 'x^2' +  str(*[' + ' if self.b >= 0 else ' - ']) + str(abs(self.b)) + 'x' + str(*[' + ' if self.c >= 0 else ' - ']) + str(abs(self.c))
    
    @property
    def coefficients(self):
        return (self.a, self.b, self.c)
    
    @coefficients.setter
    def coefficients(self, coefficients):
        self.a, self.b, self.c = coefficients
        self.__d = (self.b ** 2) - (4 * self.a * self.c)
''' Второй вариант решения'''    
# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.a, self.b, self.c = a, b, c

#     @property
#     def d(self):
#         return self.b ** 2 - 4 * self.a * self.c

#     @property
#     def x1(self):
#         return (-self.b - self.d ** 0.5) / (2 * self.a) if self.d >= 0 else None

#     @property
#     def x2(self):
#         return (-self.b + self.d ** 0.5) / (2 * self.a) if self.d >= 0 else None

#     @property
#     def view(self):
#         b, sign_b = abs(self.b), '-' if self.b < 0 else '+'
#         c, sign_c = abs(self.c), '-' if self.c < 0 else '+'
#         return f'{self.a}x^2 {sign_b} {b}x {sign_c} {c}'

#     @property
#     def coefficients(self):
#         return self.a, self.b, self.c

#     @coefficients.setter
#     def coefficients(self, coeff):
#         a, b, c = coeff
#         self.a, self.b, self.c = a, b, c