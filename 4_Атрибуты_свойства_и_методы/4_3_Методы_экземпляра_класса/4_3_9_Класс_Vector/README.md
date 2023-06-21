<h2 style="text-align:center">Класс Vector</h2>

### Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* x — координата вектора по оси x, по умолчанию имеет значение 0
* y — координата вектора по оси y, по умолчанию имеет значение 0

#### Экземпляр класса Vector должен иметь два атрибута:
* x — координата вектора по оси x
* y — координата вектора по оси y
#### Класс Vector должен иметь один метод экземпляра:
* abs() — метод, возвращающий модуль вектора

<div>
<img src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/4_Атрибуты_свойства_и_методы/4_3_Методы_экземпляра_класса/4_3_9_Класс_Vector/img/task.png" title="Git" **alt="Git">
​</div>

##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.


<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">vector = Vector()<br>
                          print(vector.x, vector.y)<br>
                          print(vector.abs())<br></td>
      <td align="center">vector = Vector(3, 4)<br>
                          print(vector.x, vector.y)<br>
                          print(vector.abs())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
      0 0<br>
      0.0<br>
      </td>
      <td align="center">
                       3 4<br>
                       5.0<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Vector:
    def __init__(self, x: int=0, y: int=0):
        self.x = x
        self.y = y

    def abs(self):
        return f'{(pow(((self.x**2) + (self.y**2)), 0.5))}'
```
* Второй вариант решения
```python
from math import sqrt

class Vector:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        
    def abs(self):
        return sqrt(self.x**2 + self.y**2)
```


