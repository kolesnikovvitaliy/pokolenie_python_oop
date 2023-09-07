''' Первый вариант решения'''
from dataclasses import dataclass
from random import shuffle, choice


@dataclass
class Cell:
    row: int
    col: int
    neighbours: int
    mine: bool = False
    open: bool = False


class Game:
    def __init__(self, row: int, col: int, mine: int):
        self.rows = row
        self.cols = col
        self.mines = mine
        self.board = []

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, lst):
        self.__board = [['' for i in range(self.cols)]
                        for j in range(self.rows)]
        self.__set_board_mines(self)
        self.__set_count_neighbours(self)

    @staticmethod
    def __set_board_mines(self):
        min = self.__mines(self)
        neighbours = 0
        for i in range(self.rows):
            for j in range(self.cols):
                mine = min.pop()
                if mine is True:
                    _open = False
                else:
                    _open = choice([True, False])
                self.__board[i][j] = Cell(i, j, neighbours, mine, _open)

    @staticmethod
    def __set_count_neighbours(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.__board[i][j].mine:
                    for k in range(self.rows):
                        for v in range(self.cols):
                            if abs(i - k) <= 1 and abs(j - v) <= 1 and\
                                 not ((i-k) == 0 and (j-v) == 0):
                                self.__board[i-(i-k)][j-(j-v)].neighbours += 1

    @staticmethod
    def __mines(self):
        min = [True for _ in range(self.mines)] +\
              [False for _ in range(self.rows * self.cols - self.mines)]
        shuffle(min)
        return min
''' Второй вариант решения'''    
# from random import sample
# from itertools import product, chain
# from dataclasses import dataclass, field

# @dataclass(repr=False, order=False)
# class Cell:
#     row: int
#     col: int
#     mine: bool = False
#     open: bool = False
#     neighbours: int = field(default=0, init=False)
        
# @dataclass(repr=False, order=False)
# class Game:
#     rows: int
#     cols: int
#     mines: int
    
#     def __post_init__(self) -> None:
#         self.board = [[Cell(i, j) for j in range(self.cols)] for i in range(self.rows)]
#         for i in sample(list(chain(*self.board)), self.mines):
#             i.mine = True
#         for i, j in product(range(self.rows), range(self.cols)):
#             self.help_mine(self.board[i][j])
    
#     def help_mine(self, obj) -> None:
#         x, y = 1, 0
#         for i in range(8):
#             row, col = obj.row + x, obj.col + y
#             if self.rows > row >= 0 and self.cols > col >= 0:
#                 obj.neighbours += self.board[row][col].mine
#             x, y = [(-y, x), (1, 1)][i == 3]