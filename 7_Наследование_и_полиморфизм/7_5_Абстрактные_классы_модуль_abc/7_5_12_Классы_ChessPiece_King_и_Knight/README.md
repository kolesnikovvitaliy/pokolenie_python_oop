<h2 style="text-align:center">Классы ChessPiece, King и Knight</h2>

### 1. Реализуйте абстрактный класс ChessPiece, описывающий шахматную фигуру. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* horizontal — координата фигуры по горизонтали, представленная латинской буквой от a до h
* vertical — координата фигуры по вертикали, представленная целым числом от 1 до 8 включительно
#### Класс ChessPiece должен иметь один метод экземпляра:
* can_move() — пустой абстрактный метод
### 2. Также реализуйте класс King, наследника класса ChessPiece, описывающий шахматного короля. Процесс создания экземпляра класса King должен совпадать с процессом создания экземпляра класса ChessPiece.
#### Класс King должен иметь один метод экземпляра:
* can_move() — метод, принимающий в качестве аргументов шахматные координаты по горизонтали и вертикали и возвращающий True, если фигура может переместиться по указанным координатам, или False в противном случае
#### Экземпляр класса King  должен иметь два атрибута:
* horizontal — координата фигуры по горизонтали, представленная латинской буквой от a до h
* vertical — координата фигуры по вертикали, представленная целым числом от 1 до 8 включительно
### 3. Наконец, реализуйте класс Knight, наследника класса ChessPiece, описывающий шахматного коня. Процесс создания экземпляра класса Knight должен совпадать с процессом создания экземпляра класса ChessPiece.
#### Класс Knight должен иметь один метод экземпляра:
* can_move() — переопределенный родительский метод, принимающий в качестве аргументов координаты по горизонтали и вертикали и возвращающий True, если фигура может переместиться по указанным координатам, и False в противном случае
#### Экземпляр класса Knight  должен иметь два атрибута:
* horizontal — координата фигуры по горизонтали, представленная латинской буквой от a до h
* vertical — координата фигуры по вертикали, представленная целым числом от 1 до 8 включительно

##### Примечание 1. Шахматная доска имеет вид:
<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/7_Наследование_и_полиморфизм/7_5_Абстрактные_классы_модуль_abc/7_5_12_Классы_ChessPiece_King_и_Knight/img/task.png" title="Git" **alt="Git">
​</div>

##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализаций классов нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">king = King('b', 2)<br>
                          print(king.can_move('c', 3))<br>
                          print(king.can_move('a', 1))<br>
                          print(king.can_move('f', 7))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
                        True<br>
                        False<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
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
```
* Второй вариант решения

```python
from abc import ABC, abstractmethod

class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal, self.vertical = horizontal, vertical

    @abstractmethod
    def can_move(self, h, v): ...

class King(ChessPiece):
    def can_move(self, h, v):
        return (ord(self.horizontal) - ord(h)) ** 2 + (self.vertical - v) ** 2 in (1, 2)

class Knight(ChessPiece):
    def can_move(self, h, v):
        return (ord(self.horizontal) - ord(h)) ** 2 + (self.vertical - v) ** 2 == 5
```


