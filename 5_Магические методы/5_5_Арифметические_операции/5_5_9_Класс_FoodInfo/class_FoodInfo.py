''' Первый вариант решения'''
class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f"{__class__.__name__}({self.proteins}, {self.fats}, {self.carbohydrates})"
    
    def __add__(self, other):
        if isinstance(other, __class__):
            return __class__((self.proteins + other.proteins), (self.fats + other.fats), (self.carbohydrates + other.carbohydrates))
        return NotImplemented
    
    def __mul__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            return __class__((self.proteins * n), (self.fats * n), (self.carbohydrates * n))
        return NotImplemented
    
    def __truediv__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            return __class__((self.proteins / n), (self.fats / n), (self.carbohydrates / n))
        return NotImplemented
    
    def __floordiv__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            return __class__((self.proteins // n), (self.fats // n), (self.carbohydrates // n))
        return NotImplemented

''' Второй вариант решения'''    
# class FoodInfo:
#     def __init__(self, proteins, fats, carbohydrates):
#         self.proteins = proteins
#         self.fats = fats
#         self.carbohydrates = carbohydrates
        
#     def __repr__(self):
#         return f'FoodInfo({", ".join(map(str, self.__dict__.values()))})'
    
#     def __add__(self, other):
#         if isinstance(other, self.__class__):
#             return self.__class__(*map(lambda a, b: a + b, self.__dict__.values(), other.__dict__.values()))
#         return NotImplemented

#     def __mul__(self, other):
#         if isinstance(other, (int, float)):
#             return self.__class__(*(value * other for value in self.__dict__.values()))
#         return NotImplemented
    
#     def __truediv__(self, other):
#         if isinstance(other, (int, float)):
#             return self.__class__(*(value / other for value in self.__dict__.values()))
#         return NotImplemented
    
#     def __floordiv__(self, other):
#         if isinstance(other, (int, float)):
#             return self.__class__(*(value // other for value in self.__dict__.values()))
#         return NotImplemented