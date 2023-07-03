''' Первый вариант решения'''
from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year: int, data: int) -> None:
        self.year = year
        self.month = data

    def __str__(self) -> str:
        return f"{self.year}-{self.month}"
    
    def __repr__(self) -> str:
        return f'{__class__.__name__}({repr((self.year))}, {self.month})'

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, tuple) and len(__value) == 2:
            return self.year == __value[0] and self.month == __value[1]
        elif isinstance(__value, Month):
            return self.year == __value.year and self.month == __value.month
        return NotImplemented

    def __lt__(self, __value: object) -> bool:
        if isinstance(__value, tuple) and len(__value) == 2:
            return self.year < __value[0] or (self.year == __value[0] and self.month < __value[1])
        elif isinstance(__value, Month):
            return self.year < __value.year or (self.year == __value.year and self.month < __value.month)
        return NotImplemented
''' Второй вариант решения'''    
# from functools import total_ordering


# @total_ordering
# class Month:
#     def __init__(self, year, month):
#         self.year = year
#         self.month = month

#     def __str__(self):
#         return f'{self.year}-{self.month}'

#     def __repr__(self):
#         return f"Month({self.year}, {self.month})"

#     def __eq__(self, other):
#         if isinstance(other, Month):
#             return (self.year, self.month) == (other.year, other.month)
#         elif isinstance(other, tuple):
#             return (self.year, self.month) == other
#         return NotImplemented

#     def __lt__(self, other):
#         if isinstance(other, Month):
#             return (self.year, self.month) < (other.year, other.month)
#         elif isinstance(other, tuple):
#             return (self.year, self.month) < other
#         return NotImplemented