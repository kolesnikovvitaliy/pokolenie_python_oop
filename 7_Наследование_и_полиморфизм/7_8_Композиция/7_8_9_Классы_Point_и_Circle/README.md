<h2 style="text-align:center">Классы Point и Circle</h2>

### 1. Реализуйте класс Point, описывающий точку на плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* x — координата точки по оси x
* y — координата точки по оси y
#### Экземпляр класса Point должен иметь следующее неформальное строковое представление:
> ​(<координата x>, <координата y>)
### 2. Также реализуйте класс Circle, описывающий окружность на плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* radius — радиус окружности
* center — точка с координатами центра окружности, представленная экземпляром класса Point
#### Экземпляркласса Circle должен иметь следующее неформальное строковое представление:
> (<координата центра по оси x>, <координата центра по оси y>), r = <радиус>

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">point = Point(1, 1)<br>
                          circle = Circle(5, point)<br>
                          print(point)<br>
                          print(circle)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        (1, 1)<br>
                        (1, 1), r = 5<br>
      </td>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


class Circle:
    def __init__(self, radius, center):
        self.radius = radius
        self.center = center

    def __str__(self):
        return f'{self.center}, r = {self.radius}'
```
* Второй вариант решения

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


class Circle:
    def __init__(self, radius, center: Point):
        self.radius = radius
        self.center = center

    def __str__(self):
        return f'{str(self.center)}, r = {self.radius}'
```


