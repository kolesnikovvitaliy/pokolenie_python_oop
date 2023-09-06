<h2 style="text-align:center">Класс TicTacToe</h2>

### Реализуйте класс TicTacToe для игры в Крестики-Нолики. Экземпляр класса TicTacToe должен представлять собой игровое поле из трех строк и трех столбцов, на котором игроки по очереди могут помечать свободные клетки. Первый ход делает игрок, ставящий крестики:
```python
tictactoe = TicTacToe()

tictactoe.mark(1, 1)         # помечаем крестиком клетку с координатами (1; 1)
tictactoe.mark(3, 1)         # помечаем ноликом клетку с координатами (3; 1)
```
#### Помечать уже помеченные клетки нельзя. При попытке сделать это должен быть выведен текст Недоступная клетка:
```python
tictactoe.mark(1, 1)         # Недоступная клетка

tictactoe.mark(1, 3)         # помечаем крестиком клетку с координатами (1; 3)
tictactoe.mark(1, 2)         # помечаем ноликом клетку с координатами (1; 2)
tictactoe.mark(3, 3)         # помечаем крестиком клетку с координатами (3; 3)
tictactoe.mark(2, 2)         # помечаем ноликом клетку с координатами (2; 2)
tictactoe.mark(2, 3)         # помечаем крестиком клетку с координатами (2; 3)
```
#### С помощью метода winner() должна быть возможность узнать победителя игры. Метод должен вернуть:

* символ X, если победил игрок, ставящий крестики
* символ O, если победил игрок, ставящий нолики
* строку Ничья, если произошла ничья
* значение None, если победитель еще не определен
```python
print(tictactoe.winner())    # X
```
#### Помечать клетки после завершения игры нельзя. При попытке сделать это должен быть выведен текст Игра окончена:
```python
tictactoe.mark(2, 1)         # Игра окончена
```
#### С помощью метода show() должна быть возможность посмотреть текущее состояние игрового поля. Оно должно быть построено из символов | и -, а также X и O, если игроками были сделаны какие-либо ходы. Для приведенного выше поля tictactoe вызов tictactoe.show() должен вывести следующее:

> X|O|X
> -----
>  |O|X
> -----
> O| |X


<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">tictactoe = TicTacToe()<br>
                          tictactoe.mark(1, 1)<br>
                          tictactoe.mark(3, 1)<br>
                          tictactoe.mark(1, 1)<br>
                          tictactoe.mark(1, 3)<br>
                          tictactoe.mark(1, 2)<br>
                          tictactoe.mark(3, 3)<br>
                          tictactoe.mark(2, 2)<br>
                          tictactoe.mark(2, 3)<br>
                          print(tictactoe.winner())<br>
                          tictactoe.mark(2, 1)<br>
                          tictactoe.show()<br></td>
      <td align="center">tictactoe = TicTacToe()<br>
                          tictactoe.mark(1, 1)<br>
                          tictactoe.mark(3, 2)<br>
                          tictactoe.mark(1, 1)<br>
                          tictactoe.mark(1, 3)<br>
                          tictactoe.mark(1, 2)<br>
                          tictactoe.mark(3, 3)<br>
                          tictactoe.mark(2, 2)<br>
                          tictactoe.mark(2, 3)<br>
                          print(tictactoe.winner())<br>
                          tictactoe.show()<br></td>
      <td align="center">tictactoe = TicTacToe()<br>
                          tictactoe.mark(1, 1)<br>
                          tictactoe.mark(3, 2)<br>
                          tictactoe.mark(1, 3)<br>
                          tictactoe.mark(1, 2)<br>
                          tictactoe.mark(3, 3)<br>
                          tictactoe.mark(2, 3)<br>
                          tictactoe.mark(3, 1)<br>
                          tictactoe.mark(2, 1)<br>
                          tictactoe.mark(2, 2)<br>
                          print(tictactoe.winner())<br>
                          tictactoe.show()<br>
                          tictactoe.mark(2, 2)<br></td>
      <td align="center">tictactoe = TicTacToe()<br>
                          tictactoe.mark(1, 1)<br>
                          tictactoe.mark(1, 3)<br>
                          tictactoe.mark(3, 1)<br>
                          tictactoe.mark(2, 1)<br>
                          print(tictactoe.winner())<br>
                          tictactoe.mark(3, 2)<br>
                          tictactoe.mark(3, 3)<br>
                          tictactoe.mark(1, 2)<br>
                          tictactoe.mark(2, 2)<br>
                          tictactoe.mark(2, 3)<br>
                          print(tictactoe.winner())<br>
                          tictactoe.show()<br>
                          tictactoe.mark(2, 2)<br>
                          print(tictactoe.winner())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        Недоступная клетка<br>
                        X<br>
                        Игра окончена<br>
                        X|O|X<br>
                        -----<br>
                        |O|X<br>
                        -----<br>
                        O| |X<br>
      </td>
      <td align="center">
                        Недоступная клетка<br>
                        Игра окончена<br>
                        O<br>
                        X|O|X<br>
                        -----<br>
                        |O| <br>
                        -----<br>
                        |O|X<br>
      </td>
      <td align="center">
                        X<br>
                        X|O|X<br>
                        -----<br>
                        O|X|O<br>
                        -----<br>
                        X|O|X<br>
                        Игра окончена<br>
      </td>
      <td align="center">
                        None<br>
                        Ничья<br>
                        X|X|O<br>
                        -----<br>
                        O|O|X<br>
                        -----<br>
                        X|X|O<br>
                        Игра окончена<br>
                        Ничья<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class TicTacToe:
    def __init__(self):
        self.tic = [[' ' for i in range(3)] for j in range(3)]
        self.count = 0
        self.flag = None

    def mark(self, i: int, j: int):
        self.flag = self.winner()

        if self.flag:
            print('Игра окончена')
            return

        if self.tic[i-1][j-1] != ' ':
            print('Недоступная клетка')
            return
        else:
            if self.count % 2 == 0:
                self.tic[i-1][j-1] = 'X'
                self.count += 1
            else:
                self.tic[i-1][j-1] = 'O'
                self.count += 1

    def chec_win(self, items: list):
        if ' ' in items:
            return
        elif all(map(lambda x: x == items[0], items)):
            return items[0]
        return

    def win(self):
        tasks = ('self.tic[i][j]', 'self.tic[j][i]',
                 'self.tic[j][j]', 'self.tic[j][-1-j]')
        flag = None
        item = []
        for k in tasks:
            for i in range(3):
                for j in range(3):
                    item.append(eval(k))
                    if len(item) == 3:
                        flag = self.chec_win(item)
                        if flag:
                            return flag
                        else:
                            item.clear()
        return flag

    def winner(self):
        flag = self.win()
        _lst = [j for i in self.tic for j in i]

        if ' ' not in _lst and not flag:
            return 'Ничья'

        if not flag:
            return
        return flag

    def show(self):
        _lst = [['|'.join(i)] for i in self.tic]
        for k, v in enumerate(_lst):
            if k < len(_lst)-1:
                print(*v, end='\n-----\n')
            else:
                print(*v)
```
* Второй вариант решения

```python
class TicTacToe:
    def __init__(self):
        self._game_field = [[' ' for _ in range(3)] for _ in range(3)]
        self._player = 'X'
        self._move = 0

    def _is_win(self, mark):
        if any((
                any(([mark, mark, mark] == self._game_field[r]) for r in range(3)),
                any(((mark, mark, mark) == list(zip(*self._game_field))[r]) for r in range(3)),
                all((mark == self._game_field[r][r]) for r in range(3)),
                all((mark == self._game_field[r][-r - 1]) for r in range(3)),
        )):
            return True
        return None

    def winner(self):
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        if self._move >= 9:
            return 'Ничья'
        return None

    def mark(self, r, c):
        if self.winner() or self._move >= 9:
            print('Игра окончена')
        elif self._game_field[r - 1][c - 1] != ' ':
            print('Недоступная клетка')
        else:
            self._move += 1
            self._game_field[r - 1][c - 1] = self._player
            self._player = ['X', 'O'][self._move % 2]

    def show(self):
        field = ['|'.join(self._game_field[r]) for r in range(3)]
        print(*('\n-----\n'.join(field)), sep='')
```


