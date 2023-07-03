<h2 style="text-align:center">Класс Vector</h2>

### Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* x — координата вектора по оси x
* y — координата вектора по оси y
#### Экземпляр класса Vector должен иметь следующее формальное строковое представление:
> Vector(<координата x>, <координата y>)
##### Также экземпляры класса Vector должны поддерживать операции сравнения с помощью операторов == и!=. Два вектора считаются равными, если их координаты по обеим осям совпадают. Методы, реализующие операции сравнения, должны уметь сравнивать как два вектора между собой, так и вектор с кортежем из двух чисел, представляющих координаты x и y.


##### Примечание 1. Числами будем считать экземпляры классов int и float.
##### Примечание 2. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
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
                          b = Vector(1, 2)<br>
                          print(a == b)<br>
                          print(a != b)<br></td>
      <td align="center">a = Vector(1, 2)<br>
                        pair1 = (1, 2)<br>
                        pair2 = (3, 4)<br>
                        pair3 = (5, 6, 7)<br>
                        pair4 = (1, 2, 3, 4)<br>
                        pair5 = (1, 4, 3, 2)<br>
                        print(a == pair1)<br>
                        print(a == pair2)<br>
                        print(a == pair3)<br>
                        print(a == pair4)<br>
                        print(a == pair5)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
                        False<br>
      </td>
      <td align="center">
                        True<br>
                        False<br>
                        False<br>
                        False<br>
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
    
    def __repr__(self) -> str:
        return f"{__class__.__name__}({self.x}, {self.y})"

    
    def __eq__(self, __value) -> bool:
        if isinstance(__value, tuple) or isinstance(__value, list):
            if  len(__value) == 2 and map(int, __value):
                return self.x == __value[0] and self.y == __value[1]
            return NotImplemented
        elif isinstance(__value, Vector):
            return self.x == __value.x and self.y == __value.y
        return NotImplemented
```
* Второй вариант решения

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            return (self.x, self.y) == other
        elif isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented
```


