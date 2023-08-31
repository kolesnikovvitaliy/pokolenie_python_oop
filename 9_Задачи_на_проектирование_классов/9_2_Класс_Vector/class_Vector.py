''' Первый вариант решения'''
class Vector:
    def __init__(self, *args):
        self.x = args

    def __str__(self):
        return f'{self.x}'

    def __len__(self):
        return len(self.x)

    def norm(self):
        _x = pow(sum(map(lambda a: a ** 2, *self.__dict__.values())), 0.5)
        return _x

    @staticmethod
    def is_valid(func):
        def wrapper(self, other):
            if isinstance(other, __class__):
                if len(self.x) == len(other.x):
                    return func(self, other)
                raise ValueError('Векторы должны иметь равную длину')
            return NotImplemented
        return wrapper

    @is_valid
    def __add__(self, other):
        _x = tuple(map(sum, zip(*self.__dict__.values(),
                                *other.__dict__.values())))
        return __class__(*_x)

    @is_valid
    def __mul__(self, other):
        _x = sum(map(lambda a, b: a * b, *self.__dict__.values(),
                     *other.__dict__.values()))
        return _x

    @is_valid
    def __sub__(self, other):
        _x = tuple(map(lambda a, b: a - b, *self.__dict__.values(),
                       *other.__dict__.values()))
        return __class__(*_x)

    @is_valid
    def __eq__(self, other):
        return self.x == other.x
''' Второй вариант решения'''    
# class Vector:
#     def __init__(self, *args):
#         self.coords = args

#     def _if_different_coords(self, other):
#         if len(self.coords) != len(other.coords):
#             raise ValueError('Векторы должны иметь равную длину')

#     def norm(self):
#         return sum(digit ** 2 for digit in self.coords) ** 0.5

#     def __str__(self):
#         return str(self.coords)

#     def __add__(self, other):
#         self._if_different_coords(other)
#         if isinstance(other, type(self)):
#             return type(self)(*(self_coord + other_coord for self_coord, other_coord in zip(self.coords, other.coords)))
#         return NotImplemented

#     def __sub__(self, other):
#         self._if_different_coords(other)
#         if isinstance(other, type(self)):
#             return type(self)(*(self_coord - other_coord for self_coord, other_coord in zip(self.coords, other.coords)))
#         return NotImplemented

#     def __mul__(self, other):
#         self._if_different_coords(other)
#         if isinstance(other, type(self)):
#             return sum(self_coord * other_coord for self_coord, other_coord in zip(self.coords, other.coords))
#         return NotImplemented

#     def __eq__(self, other):
#         self._if_different_coords(other)
#         if isinstance(other, type(self)):
#             return self.coords == other.coords
#         return NotImplemented