<h2 style="text-align:center">Класс Vector</h2>


### Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* x — координата вектора по оси x
* y — координата вектора по оси y
#### Экземпляр класса Vector должен иметь следующее формальное строковое представление:
> Vector(<координата x>, <координата y>)
#### И следующее неформальное строковое представление:
> Вектор на плоскости с координатами (<координата x>, <координата y>)
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса Vector нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">vector = Vector(1, 2)<br>
                          print(str(vector))<br>
                          print(repr(vector))<br></td>
      <td align="center">vectors = [Vector(1, 2), Vector(3, 4)]<br>
                          print(vectors)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Вектор на плоскости с координатами (1, 2)<br>
                        Vector(1, 2)<br>
      </td>
      <td align="center">
                        [Vector(1, 2), Vector(3, 4)]<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Вектор на плоскости с координатами ({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"
```
* Второй вариант решения

```python
class Vector:
    def __init__(self, x, y):
        self.point = (x, y)
       
    def __repr__(self):
        return f'Vector{self.point}'
    
    def __str__(self):
        return f'Вектор на плоскости с координатами {self.point}'
```


