<h2 style="text-align:center">Класс Circle</h2>

### Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:
* radius — радиус круга
#### Экземпляр класса Circle должен иметь три атрибута:
* _radius — радиус круга
* _diameter — диаметр круга
* _area — площадь круга
#### Класс Circle должен иметь три метода экземпляра:
* get_radius() — метод, возвращающий радиус круга
* get_diameter() — метод, возвращающий диаметр круга
* get_area() — метод, возвращающий площадь круга

##### Примечание 1. Площадь круга вычисляется по формуле πr**2 , где r — радиус круга, π — константа, которая выражает отношение длины окружности к ее диаметру.
##### Примечание 2. Импортировать константу π можно из модуля math:
```python
from math import pi
```

##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">circle = Circle(1)<br>
                          print(circle.get_radius())<br>
                          print(circle.get_diameter())<br>
                          print(round(circle.get_area()))<br></td>
      <td align="center">circle = Circle(5)<br>
                          print(circle.get_radius())<br>
                          print(circle.get_diameter())<br>
                          print(round(circle.get_area()))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        1<br>
                        2<br>
                        3<br>
      </td>
      <td align="center">
                        5<br>
                        10<br>
                        79<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from math import pi


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = self._radius * 2
        self._area = pi * (self._radius**2)
    
    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area
```
* Второй вариант решения
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = self._radius * 2
        self._area = (__import__("math").pi) * (self._radius**2)
    
    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area
```


