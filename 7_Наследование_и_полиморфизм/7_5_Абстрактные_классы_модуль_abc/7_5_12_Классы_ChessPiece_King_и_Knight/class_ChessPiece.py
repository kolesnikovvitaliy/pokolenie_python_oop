''' Первый вариант решения'''
from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal: str, vertical: int):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, col: str, row: int):
        pass


class King(ChessPiece):
    def can_move(self, col: str, row: int):
        x = abs(self.vertical - row)
        y = abs(ord(self.horizontal) - ord(col))
        if x == 0 and y == 0:
            return False
        return x <= 1 and y <= 1


class Knight(ChessPiece):
    def can_move(self, col: str, row: int):
        return (ord(self.horizontal) - ord(col))**2 + (self.vertical - row) \
                ** 2 == 5
''' Второй вариант решения'''    
# from abc import ABC, abstractmethod

# class ChessPiece(ABC):
#     def __init__(self, horizontal, vertical):
#         self.horizontal, self.vertical = horizontal, vertical

#     @abstractmethod
#     def can_move(self, h, v): ...

# class King(ChessPiece):
#     def can_move(self, h, v):
#         return (ord(self.horizontal) - ord(h)) ** 2 + (self.vertical - v) ** 2 in (1, 2)

# class Knight(ChessPiece):
#     def can_move(self, h, v):
#         return (ord(self.horizontal) - ord(h)) ** 2 + (self.vertical - v) ** 2 == 5