<h2 style="text-align:center">Класс Vector</h2>

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/4_Атрибуты_свойства_и_методы/4_6_Декоратор_@property/4_6_15_Класс_QuadraticPolynomial/img/task_1.png" title="Git" **alt="Git">
​</div>

### Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* x — координата вектора по оси x
* y — координата вектора по оси y
#### Экземпляр класса Vector должен иметь следующее формальное строковое представление:
> Vector(<координата x>, <координата y>)
#### И следующее неформальное строковое представление:
> (<координата вектора по оси x>, <координата вектора по оси y>)

#### Также экземпляр класса Vector должен поддерживать унарные операторы + и -:
* результатом унарного + должен являться новый экземпляр класса Vector с исходными координатами
* результатом унарного - должен являться новый экземпляр класса Vector с координатами, взятыми с противоположным знаком
##### Наконец, при передаче экземпляра класса Vector в функцию abs() должен возвращаться его модуль.

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/5_Магические методы/5_4_Унарные_операторы_и_функции/5_4_12_Класс_Vector/img/task.png" title="Git" **alt="Git">
​</div>

##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса Vector нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">rectangle = Rectangle(4, 5)<br>
                            print(rectangle.length)<br>
                            print(rectangle.width)<br>
                            print(rectangle.perimeter)<br>
                            print(rectangle.area)<br></td>
      <td align="center">rectangle = Rectangle(4, 5)<br>
                            rectangle.length = 2<br>
                            rectangle.width = 3<br>
                            print(rectangle.length)<br>
                            print(rectangle.width)<br>
                            print(rectangle.perimeter)<br>
                            print(rectangle.area)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        4<br>
                        5<br>
                        18<br>
                        20<br>
      </td>
      <td align="center">
                        2<br>
                        3<br>
                        10<br>
                        6<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Vector:
    def __init__(self, x: int, y: int) -> str:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "({}, {})".format(self.x, self.y)

    def __repr__(self) -> str:
        return "{}({}, {})".format(__class__.__name__, self.x, self.y)
    
    def __pos__(self):
        return __class__(self.x, self.y)
    
    def __neg__(self):
        return __class__(self.x*-1, self.y*-1)
    
    def __abs__(self):
        return pow((self.x**2 + self.y**2), 0.5)
```
* Второй вариант решения

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        return f'Vector{self.__str__()}'
    
    def __pos__(self):
        return Vector(self.x, self.y)
    
    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
```


