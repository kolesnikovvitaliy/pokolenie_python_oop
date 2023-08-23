<h2 style="text-align:center">Класс Shape</h2>


### Реализуйте класс Shape, описывающий геометрическую фигуру. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

* name — название фигуры
* color — цвет фигуры
* area — площадь фигуры
#### Экземпляр класса Shape должен иметь три атрибута:

* name — название фигуры
* color — цвет фигуры
* area — площадь фигуры
#### Помимо приведенных выше трех атрибутов, экземпляр класса Shape не должен иметь возможности получить какие-либо другие атрибуты.

#### Также экземпляр класса Shape должен иметь следующее неформальное строковое представление:

> <цвет фигуры> <название фигуры> (<площадь фигуры>)
#### Наконец, экземпляры класса Shape должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=. Две фигуры считаются равными, если их площади совпадают. Фигура считается больше другой фигуры, если ее площадь больше.

##### Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

##### Примечание 3. Никаких ограничений касательно реализации класса Shape нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">shape = Shape('triangle', 'red', 12)<br>
                          print(shape.name)<br>
                          print(shape.color)<br>
                          print(shape.area)<br></td>
      <td align="center">print(Shape('Square', 'Red', 4))<br></td>
      <td align="center">print(Shape('rectangle', 'green', 12) == Shape('triangle', 'red', 12))<br>
                          print(Shape('triangle', 'red', 15) > Shape('triangle', 'red', 12))<br></td>
      <td align="center">shape = Shape('triangle', 'red', 12)<br>
                        try:<br>
                            shape.perimeter = 9<br>
                        except AttributeError:<br>
                            print('Error')<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        triangle<br>
                        red<br>
                        12<br>
      </td>
      <td align="center">
                        Red Square (4)<br>
      </td>
      <td align="center">
                        True<br>
                        True<br>
      </td>
      <td align="center">
                        Error<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from functools import total_ordering


@total_ordering
class Shape:
    __slots__ = ('name', 'color', 'area')

    def __init__(self, name, color, area):
        self.name = name
        self.color = color
        self.area = area

    def __str__(self):
        return f'{self.color} {self.name} ({self.area})'

    def __eq__(self, other):
        if isinstance(other, __class__):
            return self.area == other.area
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, __class__):
            return self.area < other.area
        return NotImplemented
```
* Второй вариант решения

```python
from functools import total_ordering


@total_ordering
class Shape:
    __slots__ = ('name', 'color', 'area')

    def __init__(self, name, color, area):
        self.name = name
        self.color = color
        self.area = area

    def __str__(self):
        return f'{self.color} {self.name} ({self.area})'

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.area == other.area
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.area < other.area
        return NotImplemented
```


