<h2 style="text-align:center">Класс ColoredPoint</h2>


### Реализуйте класс ColoredPoint, описывающий цветную точку на плоскости. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
* x — координата точки по оси x
* y — координата точки по оси y
* color — цвет точки
#### Класс ColoredPoint должен иметь три свойства:
* x — свойство, доступное только для чтения, возвращающее координату точки по оси x
* y — свойство, доступное только для чтения, возвращающее координату точки по оси y
* color — свойство, доступное только для чтения, возвращающее цвет точки
#### Экземпляр класса ColoredPoint должен иметь следующее формальное строковое представление:
> ColoredPoint(<координата x>, <координата y>, '<цвет точки>')
#### Также экземпляры класса ColoredPoint должны поддерживать между собой операции сравнения с помощью операторов == и!=. Две цветные точки считаются равными, если их цвета и координаты по обеим осям совпадают.
#### Наконец, при передаче экземпляра класса ColoredPoint в функцию hash() должно возвращаться его хеш-значение, вычисленное с помощью функции hash() на основе кортежа, первым элементом которого является координата точки по оси x, вторым — координата точки по оси y, третьим — цвет точки.

##### Примечание 1. Если объект, с которым происходит сравнение, некорректен, метод, реализующий операцию сравнения, должен вернуть константу NotImplemented.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса ColoredPoint нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">point1 = ColoredPoint(1, 2, 'white')<br>
                          point2 = ColoredPoint(1, 2, 'white')<br>
                          point3 = ColoredPoint(3, 4, 'black')<br>
                          print(point1 == point2)<br>
                          print(hash(point1) == hash(point2))<br>
                          print(point1 == point3)<br>
                          print(hash(point1) == hash(point3))<br></td>
      <td align="center">points = {ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2, 'black'): 20}<br>
                        print(points)<br></td>
      <td align="center">point = ColoredPoint(1, 2, 'white')<br>
                        try:<br>
                            point.color = 'black'<br>
                        except AttributeError as e:
                            print('Error')<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
                        True<br>
                        False<br>
                        False<br>
      </td>
      <td align="center">
                        {ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2, 'black'): 20}<br>
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
class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def color(self):
        return self._color

    def __repr__(self):
        return f"{__class__.__name__}({self.x}, {self.y}, '{self.color}')"
    
    def __eq__(self, __value: object):
        if isinstance(__value, __class__):
            return self.x == __value.x and self.y == __value.y and self.color == __value.color
        return NotImplemented
    
    def __ne__(self, __value: object):
        if isinstance(__value, __class__):
            return self.x != __value.x or self.y != __value.y or self.color != __value.color
        return NotImplemented
    
    def __hash__(self):
        return hash((self.x, self.y, self.color))
```
* Второй вариант решения

```python
class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color
         
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def color(self):
        return self._color

    @property
    def _fields(self):
        return self._x, self._y, self._color
    
    def __repr__(self):
        return "ColoredPoint({}, {}, '{}')".format(*self._fields)

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self._fields == other._fields
        return NotImplemented

    def __hash__(self):
        return hash(self._fields)
```


