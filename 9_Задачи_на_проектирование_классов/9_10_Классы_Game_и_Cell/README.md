<h2 style="text-align:center">Классы Game и Cell</h2>

### В этой задаче вам необходимо реализовать поле для игры в Сапера в виде двух классов Game и Cell. Экземпляр первого класса будет описывать само игровое поле, экземпляр класса Cell — одну его ячейку. Экземпляр класса Game должен создаваться на основе трех значений: количество строк (длина поля), количество столбцов (ширина поля) и общее количество мин на поле:
```python
game = Game(14, 18, 40)    # 14 строк, 18 столбцов и 40 мин
```
#### Количество строк и столбцов, а также общее количество мин должны быть доступны по соответствующим атрибутам:
```python
print(game.rows)           # 14
print(game.cols)           # 18
print(game.mines)          # 40
```
#### Также экземпляр класса Game должен иметь атрибут board, представляющий игровое поле в виде двумерного списка. Количество подсписков в этом списке должно совпадать с количеством строк, количество элементов в подсписках — с количеством столбцов. Каждый элемент подсписка должен представлять собой экземпляр класса Cell и иметь соответствующий набор атрибутов:
```python
cell = game.board[0][0]

print(cell.row)            # 0; строка ячейки
print(cell.col)            # 0; столбец ячейки
print(cell.mine)           # True или False в зависимости от того, содержит ячейка мину или нет
print(cell.open)           # True или False в зависимости от того, открыта ячейка или нет, по умолчанию закрыта
print(cell.neighbours)     # число от 0 до 8, количество мин в соседних ячейках
```
#### Игровое поле при создании должно заполняться минами случайным образом.

##### Примечание 1. Для проверки того, что в экземпляре класса Cell хранится верное количество мин в соседних ячейках, в одном из тестов мы используем собственную функцию get_neighbours_count(), которая считает это количество.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">game = Game(14, 18, 40)<br>
                        print(game.rows)<br>
                        print(game.cols)<br>
                        print(game.mines)<br>
                        cell = game.board[0][0]<br>
                        print(cell.row)<br>
                        print(cell.col)<br>
                        print(0 <= cell.neighbours <= 3)<br></td>
      <td align="center">game = Game(10, 8, 14)<br>
                        for r, c in ((0, 0), (0, -1), (-1, 0), (-1, -1)):<br>
                            cell = game.board[r][c]<br>
                            print(0 <= cell.neighbours <= 3, type(cell))<br></td>
      <td align="center">game = Game(10, 8, 14)<br>
                        for r in (0, -1):<br>
                            for c in range(1, game.cols - 1):<br>
                                cell = game.board[r][c]<br>
                                print(0 <= cell.neighbours <= 5, type(cell))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        14<br>
                        18<br>
                        40<br>
                        0<br>
                        0<br>
                        True<br>
      </td>
      <td align="center">
                        True class '__main__.Cell'<br>
                        True class '__main__.Cell'<br>
                        True class '__main__.Cell'<br>
                        True class '__main__.Cell'<br>
      </td>
      <td align="center">
                        True class '__main__.Cell'<br>
                        True class '__main__.Cell'<br>
                        True class '__main__.Cell'<br>
                        True class '__main__.Cell'<br>
                        True class '__main__.Cell'<br>
                        True class '__main__.Cell'<br>
                        True class '__main__.Cell'<br>
                        True class '__main__.Cell'<br>
                        True class '__main__.Cell'<br>
                        True class '__main__.Cell'<br>
                        True class '__main__.Cell'<br>
                        True class '__main__.Cell'<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from dataclasses import dataclass
from random import shuffle, choice


@dataclass
class Cell:
    row: int = 0
    col: int = 0
    neighbours: int = 0
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
        self.__board = [[Cell() for i in range(self.cols)]
                        for j in range(self.rows)]
        self.__set_board_mines(self)

    @staticmethod
    def __set_board_mines(self):
        min = self.__mines(self)
        neighbours = 0
        for i in range(self.rows):
            for j in range(self.cols):
                mine = min.pop()
                if mine is True:
                    _open = False
                    self.__board[i][j] = Cell(i, j, neighbours, mine, _open)
                    self.__set_count_neighbours(self, i, j)
                else:
                    _open = choice([True, False])
                self.__board[i][j].open = _open

    @staticmethod
    def __set_count_neighbours(self, i, j):
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
```
* Второй вариант решения

```python
from random import sample
from itertools import product, chain
from dataclasses import dataclass, field

@dataclass(repr=False, order=False)
class Cell:
    row: int
    col: int
    mine: bool = False
    open: bool = False
    neighbours: int = field(default=0, init=False)
        
@dataclass(repr=False, order=False)
class Game:
    rows: int
    cols: int
    mines: int
    
    def __post_init__(self) -> None:
        self.board = [[Cell(i, j) for j in range(self.cols)] for i in range(self.rows)]
        for i in sample(list(chain(*self.board)), self.mines):
            i.mine = True
        for i, j in product(range(self.rows), range(self.cols)):
            self.help_mine(self.board[i][j])
    
    def help_mine(self, obj) -> None:
        x, y = 1, 0
        for i in range(8):
            row, col = obj.row + x, obj.col + y
            if self.rows > row >= 0 and self.cols > col >= 0:
                obj.neighbours += self.board[row][col].mine
            x, y = [(-y, x), (1, 1)][i == 3]
```


