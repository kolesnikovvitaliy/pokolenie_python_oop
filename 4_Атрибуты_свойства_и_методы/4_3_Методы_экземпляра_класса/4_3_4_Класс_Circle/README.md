<h2 style="text-align:center">Класс Circle</h2>

### Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:
* radius — радиус круга

#### Экземпляр класса Circle должен иметь три атрибута:
* radius — радиус круга
* diameter — диаметр круга
* area — площадь круга

<div>
<img src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/4_Атрибуты_свойства_и_методы/4_3_Методы_экземпляра_класса/4_3_4_Класс_Circle/img/task.png" title="Git" **alt="Git">
​</div>

```python
from math import pi
```
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.


<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">circle = Circle(1)<br>
                        print(circle.radius)<br></td>
      <td align="center">circle = Circle(5)<br>
                         print(circle.radius)<br>
                         print(circle.diameter)<br>
                         print(circle.area)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
      1<br>
      </td>
      <td align="center">
                       5<br>
                       10<br>
                       78.53981633974483<br>
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
        self.radius = radius
        self.diameter = self.radius*2
        self.area = pi*(self.radius**2)
```
* Второй вариант решения
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.area = __import__('math').pi * radius ** 2
```


