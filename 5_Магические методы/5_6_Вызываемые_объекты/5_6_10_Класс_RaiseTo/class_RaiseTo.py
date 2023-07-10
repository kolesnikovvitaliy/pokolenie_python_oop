''' Первый вариант решения'''
class  RaiseTo:
    def __init__(self, degree: int):
        self.degree = degree

    def __call__(self, x: int):
        return x**self.degree
''' Второй вариант решения'''    
# class RaiseTo:
#     def __init__(self, degree):
#         self.degree = degree
        
#     def __call__(self, x):
#         return x ** self.degree