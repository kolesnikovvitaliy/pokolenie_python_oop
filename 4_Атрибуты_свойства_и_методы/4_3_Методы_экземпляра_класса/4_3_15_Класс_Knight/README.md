<h2 style="text-align:center">Класс Knight</h2>

### Реализуйте класс Knight, описывающий шахматного коня. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
* horizontal — координата коня по горизонтали, представленная латинской буквой от a до h
* vertical — координата коня по вертикали, представленная целым числом от 1 до 8 включительно
* color — цвет коня (black или white)
#### Экземпляр класса Knight должен иметь три атрибута:
* chorizontal — координата коня на шахматной доске по горизонтали
* vertical — координата коня на шахматной доске по вертикали
* color — цвет коня
#### Класс Knight должен иметь четыре метода экземпляра:
* get_char() — метод, возвращающий символ N
* can_move() — метод, принимающий в качестве аргументов координаты клетки по горизонтали и по вертикали, и возвращающий True, если конь может переместиться на клетку с данными координатами, или False в противном случае
* move_to() — метод, принимающий в качестве аргументов координаты клетки по горизонтали и по вертикали и заменяющий текущие координаты коня на переданные. Если конь из текущей клетки не может переместиться на клетку с указанными координатами, его координаты должны остаться неизменными
* draw_board() — метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки, на которые может переместиться конь. Пустые клетки должны быть отображены символом ., конь — символом N, клетки, на которые может переместиться конь, — символом *
##### Примечание 1. Шахматное поле имеет вид:

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/4_Атрибуты_свойства_и_методы/4_3_Методы_экземпляра_класса/4_3_15_Класс_Knight/img/task.png" title="Git" **alt="Git">
​</div>

##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">knight = Knight('c', 3, 'white')<br>
                        print(knight.color, knight.get_char())<br>
                        print(knight.horizontal, knight.vertical)<br></td>
      <td align="center">knight = Knight('c', 3, 'white')<br>
                        print(knight.horizontal, knight.vertical)<br>
                        print(knight.can_move('e', 5))<br>
                        print(knight.can_move('e', 4))<br>
                        knight.move_to('e', 4)<br>
                        print(knight.horizontal, knight.vertical)<br></td>
      <td align="center">knight = Knight('c', 3, 'white')<br>
                        knight.draw_board()<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
      white N<br>
            c 3<br>
      </td>
      <td align="center">
                       c 3<br>
                        False<br>
                        True<br>
                        e 4<br>
      </td>
      <td align="center">
                       ........<br>
                        ........<br>
                        ........<br>
                        .*.*....<br>
                        *...*...<br>
                        ..N.....<br>
                        *...*...<br>
                        .*.*....<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Knight:
    def __init__(self, horizontal: str, vertical: int, color: str):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return 'N'
    
    def can_move(self, x: str, y: int):
        import re
        if re.findall('[a-h]', x) and y in range(0,9):
            if (self.vertical - y == 2) or (y - self.vertical  == 2):
               if chr(ord(self.horizontal)+1) == x or chr(ord(self.horizontal)-1) == x:
                   return True
            elif chr(ord(self.horizontal)+2) == x or chr(ord(self.horizontal)-2) == x:
                if (self.vertical - y == 1) or (y - self.vertical  == 1):
                    return True
        return False
            
    def move_to(self, x: str, y: int):
        if self.can_move(x, y):
            self.horizontal = x
            self.vertical = y
            
    def draw_board(self):
        col = {v: k for k,v in enumerate([chr(i) for i in range(ord('a'), ord('i'))])}
        row = {k:v for k,v in list(zip(range(1,9),range(7,-1,-1)))}
        arr = [["N" if [i, j] == [row[self.vertical], col[self.horizontal]] else '.' for j in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                if (row[self.vertical] - i) * (col[self.horizontal] - j) in [-2, 2]: arr[i][j] = "*" 
        for line in arr:
            print(*line, sep = '')
```
* Второй вариант решения
```python
class Knight:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        
    def get_char(self):
        return 'N'
    
    def can_move(self, col, row):
        return (ord(self.col) - ord(col))**2 + (self.row - row)**2 == 5
    
    def move_to(self, col, row):
        if self.can_move(col, row):
            self.col = col
            self.row = row
            
    def draw_board(self):
        for row in range(8, 0, -1):
            for col in 'abcdefgh':
                if self.col == col and self.row == row:
                    print(self.get_char(), end='')
                elif self.can_move(col, row):
                    print('*', end='')
                else:
                    print('.', end='')
            print()
```


