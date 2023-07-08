<h2 style="text-align:center">Класс Vector</h2>

### Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* x — координата вектора по оси x
* y — координата вектора по оси y
#### Экземпляр класса Vector должен иметь следующее формальное строковое представление:
> Vector(<координата x>, <координата y>)
#### Также экземпляры класса Vector должны поддерживать между собой операции сложения и вычитания с помощью операторов + и - соответственно:
* результатом сложения должен являться новый экземпляр класса Vector, координата по оси x которого равна сумме координат по оси x исходных векторов, координата по оси y — сумме координат по оси y исходных векторов
* результатом вычитания должен являться новый экземпляр класса Vector координата по оси x которого равна разности координат по оси x исходных векторов с учетом порядка, координата по оси y — разности координат по оси y исходных векторов с учетом порядка
#### Наконец, экземпляр класса Vector должен поддерживать операции умножения и деления на число n с помощью операторов * и / соответственно:
* результатом умножения должен являться новый экземпляр класса Vector, координаты которого умножены на n
* результатом деления должен являться новый экземпляр класса Vector, координаты которого поделены на n

#### Операция умножения должна быть выполнима независимо от порядка операндов, то есть должна быть возможность умножить как вектор на число, так и число на вектор.
##### Примечание 1. Числами будем считать экземпляры классов int и float. Также будем гарантировать, что экземпляр класса Vector всегда делится на ненулевое число.
##### Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 4. Никаких ограничений касательно реализации класса Vector нет, она может быть произвольной.
<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">a = Vector(1, 2)<br>
                        b = Vector(3, 4)<br>
                        print(a + b)<br>
                        print(a - b)<br>
                        print(b + a)<br>
                        print(b - a)<br></td>
      <td align="center">a = Vector(3, 4)<br>
                          print(a * 2)<br>
                          print(2 * a)<br>
                          print(a / 2)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Vector(4, 6)<br>
                        Vector(-2, -2)<br>
                        Vector(4, 6)<br>
                        Vector(2, 2)<br>
      </td>
      <td align="center">
                        Vector(6, 8)<br>
                        Vector(6, 8)<br>
                        Vector(1.5, 2.0)<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{__class__.__name__}({self.x}, {self.y})"
    
    def __add__(self, other):
        if isinstance(other, __class__):
            x,y = map(sum, zip(self.__dict__.values(), other.__dict__.values()))
            return __class__(x, y)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, __class__):
            x,y = map(lambda a,b: a - b, self.__dict__.values(), other.__dict__.values())
            return __class__(x, y)
        return NotImplemented
    
    def __mul__(self, n):
        if isinstance(n, (int, float)):
            x,y = map(lambda a: a * n, self.__dict__.values())
            return __class__(x, y)
        return NotImplemented
    
    def __rmul__(self, n):
        return self.__mul__(n)
    
    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            x,y = map(lambda a: a / n, self.__dict__.values())
            return __class__(x, y)
        return NotImplemented
    
    def __rtruediv__(self, n):
        return self.__truediv__(n)
```
* Второй вариант решения

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other)
        return NotImplemented
```


