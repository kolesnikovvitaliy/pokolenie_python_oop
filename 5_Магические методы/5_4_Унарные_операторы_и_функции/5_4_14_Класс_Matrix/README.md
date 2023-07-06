<h2 style="text-align:center">Класс Matrix</h2>


### Реализуйте класс Matrix, описывающий двумерную матрицу. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
* rows — количество строк в матрице
* cols — количество столбцов в матрице
* value — начальное значение для элементов матрицы, по умолчанию имеет значение 0
#### Экземпляр класса Matrix должен иметь два атрибута:
* rows — количество строк в матрице
* cols — количество столбцов в матрице

#### Класс Matrix должен иметь два метода экземпляра:
* get_value() — метод, принимающий в качестве аргументов строку row и столбец col и возвращающий элемент матрицы со строкой row и столбцом col
* set_value() — метод, принимающий в качестве аргументов строку row, столбец col и значение value и устанавливающий в качестве значения элемента матрицы со строкой row и столбцом col значение value
#### Экземпляр класса Matrix должен иметь следующее формальное строковое представление:
> Matrix(<количество строк в матрице>, <количество столбцов в матрице>)
#### Неформальным строковым представлением должна быть строка, в которой перечислены все элементы матрицы. Элементы строки матрицы должны быть разделены пробелом, строки матрицы должны быть разделены символом переноса строки \n. Например, для объекта Matrix(2, 3) неформальным строковым представлением должна быть строка 0 0 0\n0 0 0, которая при выводе будет отображаться следующим образом:
> 0 0 0
> 0 0 0

#### Также экземпляр класса Matrix должен поддерживать унарные операторы +, - и ~:
* результатом унарного + должен являться новый экземпляр класса Matrix c исходным количеством строк и столбцов и с исходными элементами
* результатом унарного - должен являться новый экземпляр класса Matrix c исходным количеством строк и столбцов и с элементами, взятыми с противоположным знаком
* результатом унарного ~ должен являться новый экземпляр класса Matrix, представляющий транспонированную матрицу
##### Наконец, при передаче экземпляра класса Matrix в функцию round() должен возвращаться новый экземпляр класса Matrix c исходным количеством строк и столбцов и с элементами, округленными с помощью функции round(). Во время передачи в функцию round() должна быть возможность в качестве второго необязательного аргумента указать целое число, определяющее количество знаков после запятой при округлении.
##### Примечание 1. Индексация строк и столбцов в матрице начинается с нуля.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса Matrix нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">print(Matrix(2, 3))<br></td>
      <td align="center">matrix = Matrix(2, 3, 1)<br>
                        print(+matrix)<br>
                        print()<br>
                        print(-matrix)<br></td>
      <td align="center">matrix = Matrix(2, 3, 1)<br>
                          print(matrix)<br>
                          print()<br>
                          print(~matrix)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        0 0 0<br>
                        0 0 0<br>
      </td>
      <td align="center">
                        1 1 1<br>
                        1 1 1<br>
<br>
                        -1 -1 -1<br>
                        -1 -1 -1<br>
      </td>
      <td align="center">
                        1 1 1<br>
                        1 1 1<br>
<br>
                        1 1<br>
                        1 1<br>
                        1 1<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.__value = value
        if type(self.__value) is int:
            self.__matrix = [[value for j in range(cols)] for i in range(rows)]
        else:
            self.set_value(self.rows, self.cols, self.__value)        

    def get_value(self, rows, cols):
        return self.__matrix[rows][cols]

    def set_value(self, rows, cols, value=0):
        if type(value) is int or type(value) is float:
            self.__matrix[rows][cols] = value
        else:
            self.__matrix = [[0 for j in range(cols)] for i in range(rows)]
            for i in range(len(value)):
                for j in range(len(value[0])):
                    self.__matrix[i][j] = value[i][j]
        return self.__matrix[-1]        

    def __str__(self) -> str:
        __str = ''
        for i in self.__matrix:
            __str += ' '.join(map(str,i)) + '\n'
        return __str.strip()           
        
    def __repr__(self) -> str:
        return f"{__class__.__name__}({self.rows}, {self.cols})"
    
    def __pos__(self):
        return __class__(self.rows, self.cols, self.__value)

    def __neg__(self):
        return __class__(self.rows, self.cols, [[-i for i in v] for v in self.__matrix])
    
    def __invert__(self):
        self.__m = [[0 for j in range(len(self.__matrix))] for i in range(len(self.__matrix[0]))]
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[0])):
                self.__m[j][i] = self.__matrix[i][j]
        return __class__(len(self.__m), len(self.__m[0]), self.__m)
    
    def __round__(self, round_volue=0):
        return __class__(self.rows, self.cols, [[round(i, round_volue) for i in  v] for v in self.__matrix])


```
* Второй вариант решения

```python
class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = [[value] * cols for _ in range(rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def _create_matrix_instance(self, rows, cols, sign=1, do_transpose=False, do_round=False, n=None):
        matrix = Matrix(rows, cols)
        for row in range(rows):
            for col in range(cols):
                r, c = (col, row) * do_transpose or (row, col)
                value = round(self.get_value(r, c) * sign, n) * do_round or self.get_value(r, c) * sign
                matrix.set_value(row, col, value)
        return matrix

    def __str__(self):
        string_matrix = [' '.join(map(str, item)) for item in self.matrix]
        return '\n'.join(string_matrix)

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __pos__(self):
        return self._create_matrix_instance(self.rows, self.cols)

    def __neg__(self):
        return self._create_matrix_instance(self.rows, self.cols, sign=-1)

    def __invert__(self):
        return self._create_matrix_instance(self.cols, self.rows, do_transpose=True)

    def __round__(self, n=None):
        return self._create_matrix_instance(self.rows, self.cols, do_round=True, n=n)
```


