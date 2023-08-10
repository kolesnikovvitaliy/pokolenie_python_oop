<h2 style="text-align:center">Классы Triangle и EquilateralTriangle</h2>

### Реализуйте класс Triangle, описывающий треугольник. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
* a — длина стороны треугольника
* b — длина стороны треугольника
* c — длина стороны треугольника
#### Класс Triangle должен иметь один метод экземпляра:
* perimeter() — метод, возвращающий периметр треугольника
### Также реализуйте класс EquilateralTriangle, наследника класса Triangle, описывающий равносторонний треугольник. При создании экземпляра класс должен принимать один аргумент:
* side — длина стороны треугольника

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">print(issubclass(EquilateralTriangle, Triangle))<br></td>
      <td align="center">triangle1 = Triangle(3, 4, 5)<br>
                          triangle2 = EquilateralTriangle(3)<br>
                          print(triangle1.perimeter())<br>
                          print(triangle2.perimeter())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
      </td>
      <td align="center">
                        12<br>
                        9<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def perimeter(self):
        return self._a + self._b + self._c


class EquilateralTriangle(Triangle):
    def __init__(self, said):
        super().__init__(said, said, said)
```
* Второй вариант решения

```python
class Triangle:
    def __init__(self, a, b, c):
        self._a, self._b, self._c = a, b, c
        
    def perimeter(self):
        return sum((self._a, self._b, self._c))
    
    
class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
```


