<h2 style="text-align:center">Класс Vector</h2>

### Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* x — координата вектора по оси x
* y — координата вектора по оси y
#### Экземпляр класса Vector должен иметь следующее неформальное строковое представление:
> (<координата x>, <координата y>)
#### Также экземпляр класса Vector должен поддерживать приведение к типам bool, int, float и complex:
* при приведении к типу bool значением вектора должно являться значение True, если хотя бы одна его координата не равна нулю, или False в противном случае
* при приведении к типу int значением вектора должен являться его модуль в виде целого числа с отброшенной дробной частью
* при приведении к типу float значением вектора должен являться его модуль в виде вещественного числа
* при приведении к типу complex значением вектора должно являться комплексное число, вещественная часть которого равна координате вектора по оси x, мнимая часть — координате вектора по оси y

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/5_Магические методы/5_7_Преобразования_типов/5_7_6_Класс_Vector/img/task.png" title="Git" **alt="Git">
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
      <td align="center">vector = Vector(3, 4)<br>
                          print(vector)<br>
                          print(int(vector))<br>
                          print(float(vector))<br>
                          print(complex(vector))<br></td>
      <td align="center">print(bool(Vector(1, 2)))<br>
                          print(bool(Vector(1, 0)))<br>
                          print(bool(Vector(0, 1)))<br>
                          print(bool(Vector(0, 0)))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        (3, 4)<br>
                        5<br>
                        5.0<br>
                        (3+4j)<br>
      </td>
      <td align="center">
                        True<br>
                        True<br>
                        True<br>
                        False<br>
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
        self.__vector = pow((self.x**2 + self.y**2),0.5)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __bool__(self):
        return self.x != 0 or self.y != 0
    
    def __int__(self):
        return abs(int(self.__vector))
    
    def __float__(self):
        return abs(float(self.__vector))
    
    def __complex__(self):
        return complex(self.x, self.y)
```
* Второй вариант решения

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def __bool__(self):
        return not not (self.x or self.y)
    
    def __int__(self):
        return int((self.x**2 + self.y**2)**0.5)
    
    def __float__(self):
        return float((self.x**2 + self.y**2)**0.5)
    
    def __complex__(self):
        return complex(self.x, self.y)
```


