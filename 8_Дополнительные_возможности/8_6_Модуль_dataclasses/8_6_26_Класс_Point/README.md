<h2 style="text-align:center">Класс Point</h2>

### Реализуйте класс данных Point, описывающий точку на координатной плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

* x — координата точки по оси x (тип float), по умолчанию имеет значение 0.0
* y — координата точки по оси y (тип float), по умолчанию имеет значение 0.0
### Экземпляр класса Point должен иметь три атрибута:

* x — координата точки по оси x
* y — координата точки по оси y
* quadrant — координатная четверть, к которой принадлежит точка (тип int). Если точка лежит на одной из осей, координатная четверть считается равной 0
#### Класс Point должен иметь два метода экземпляра:

* symmetric_x() — метод, возвращающий новый экземпляр класса Point, представляющий точку, симметричную текущей точке относительно оси x
* symmetric_y() — метод, возвращающий новый экземпляр класса Point, представляющий точку, симметричную текущей точке относительно оси y
#### Экземпляр класса Point должен иметь следующее формальное строковое представление:

> Point(x=<координата x>, y=<координата y>, quadrant=<координатная четверть>)
#### Наконец, экземпляры класса Point должны поддерживать между собой операцию сравнения с помощью операторов == и!=. Две точки считаются равными, если их координаты по обеим осям совпадают.

#####  Примечание 1. Для точки с координатами (x,y) симметричной относительно оси x будем считать точку с координатами (x,−y), симметричной относительно оси y — точку с координатами (−x,y).

##### Примечание 2. Координатные четверти:

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/8_Дополнительные_возможности/8_6_Модуль_dataclasses/8_6_26_Класс_Point/img/task.png" title="Git" **alt="Git">
​</div>


<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">point = Point()<br>
                          print(point)<br>
                          print(point.x)<br>
                          print(point.y)<br>
                          print(point.quadrant)<br></td>
      <td align="center">point = Point(1.0, 2.0)<br>
                          print(point.symmetric_x())<br>
                          print(point.symmetric_y())<br></td>
      <td align="center">point1 = Point(1, 2)<br>
                          point2 = Point(1, 2)<br>
                          point3 = Point(3, 4)<br>
                          print(point1 == point2)<br>
                          print(point1 == point3)<br>
                          print(point2 != point3)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        Point(x=0.0, y=0.0, quadrant=0)<br>
                        0.0<br>
                        0.0<br>
                        0<br>
      </td>
      <td align="center">
                        Point(x=1.0, y=-2.0, quadrant=4)<br>
                        Point(x=-1.0, y=2.0, quadrant=2)<br>
      </td>
      <td align="center">
                        True<br>
                        False<br>
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from dataclasses import dataclass, field


@dataclass
class Point:
    x: float = field(default=0.0)
    y: float = field(default=0.0)
    quadrant: int = field(default=0, init=False, compare=False)

    def __post_init__(self):
        if (self.x or self.y) == 0.0:
            self.quadrant = 0
        else:
            if self.x > 0 < self.y:
                self.quadrant = 1
            elif self.x < 0 < self.y:
                self.quadrant = 2
            elif self.x < 0 > self.y:
                self.quadrant = 3
            elif self.x > 0 > self.y:
                self.quadrant = 4

    def symmetric_x(self):
        return __class__(self.x, -self.y)

    def symmetric_y(self):
        return __class__(-self.x, self.y)
```
* Второй вариант решения

```python
from dataclasses import dataclass, field


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(default=0, compare=False)

    def __post_init__(self):
        if self.x > 0 and self.y != 0:
            self.quadrant = (1, 4)[self.y < 0]
        elif self.x < 0 and self.y != 0:
            self.quadrant = (2, 3)[self.y < 0]

    def symmetric_x(self):
        return type(self)(self.x, -self.y)

    def symmetric_y(self):
        return type(self)(-self.x, self.y)
```


