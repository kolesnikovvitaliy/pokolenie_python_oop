<h2 style="text-align:center">Класс Vector</h2>

### Реализуйте класс Vector, экземпляр которого представляет собой вектор произвольной размерности. Экземпляр класса Vector должен создаваться на основе собственных координат:

* a = Vector(1, 2, 3)
* b = Vector(3, 4, 5)
* c = Vector(5, 6, 7, 8)
#### В качестве неформального строкового представления вектор должен иметь собственные координаты, заключенные в круглые скобки:

* print(a)                       # (1, 2, 3)
* print(b)                       # (3, 4, 5)
* print(c)                       # (5, 6, 7, 8)
#### Векторы должны поддерживать между собой операции сложения, вычитания, произведения и нормирования:

* print(a + b)                   # (4, 6, 8)
* print(a - b)                   # (-2, -2, -2)
* print(a * b)                   # 1*3 + 2*4 + 3*5 = 26
* print(c.norm())                # sqrt(5**2 + 6**2 + 7**2 + 8**2) = sqrt(174) = 13.19090595827292
#### а также операции сравнения на равенство и неравенство:

* print(a == Vector(1, 2, 3))    # True
* print(a == Vector(4, 5, 6))    # False
#### При попытке выполнить какую-либо операцию с векторами разной размерности должно быть возбуждено исключение ValueError с текстом:

> Векторы должны иметь равную длину

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">vector1 = Vector(1, 2, 3)<br>
                          vector2 = Vector(3, 4, 5)<br>
                          vector3 = Vector(5, 6, 7, 8)<br>
                          print(vector1 + vector2)<br>
                          print(vector1 - vector2)<br>
                          print(vector1 * vector2)<br>
                          print(vector3.norm())<br></td>
      <td align="center">vector1 = Vector(1, 2, 3)<br>
                          vector2 = Vector(3, 4, 5)<br>
                          vector3 = Vector(5, 6, 7, 8)<br>
                          print(vector1 == Vector(1, 2, 3))<br>
                          print(vector1 == Vector(4, 5, 6))<br>
                          print(vector1 != vector2)<br></td>
      <td align="center">vector1 = Vector(1, 2, 3)<br>
                        vector2 = Vector(5, 6, 7, 8)<br>
                        try:<br>
                            print(vector1 == vector2)<br>
                        except ValueError as e:<br>
                            print(e)<br></td>
      <td align="center">vector1 = Vector(1, 2)<br>
                          vector2 = Vector(3, 4)<br>
                          vector3 = vector1 + vector2<br>
                          vector4 = vector1 - vector2<br>
                          print(type(vector3))<br>
                          print(type(vector4))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        (4, 6, 8)<br>
                        (-2, -2, -2)<br>
                        26<br>
                        13.19090595827292<br>
      </td>
      <td align="center">
                        True<br>
                        False<br>
                        True<br>
      </td>
      <td align="center">
                        Векторы должны иметь равную длину<br>
      </td>
      <td align="center">
                        class '__main__.Vector'<br>
                        class '__main__.Vector'<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Vector:
    def __init__(self, *args):
        self.x = args

    def __str__(self):
        return f'{self.x}'

    def __len__(self):
        return len(self.x)

    def norm(self):
        _x = pow(sum(map(lambda a: a ** 2, *self.__dict__.values())), 0.5)
        return _x

    @staticmethod
    def is_valid(func):
        def wrapper(self, other):
            if isinstance(other, __class__):
                if len(self.x) == len(other.x):
                    return func(self, other)
                raise ValueError('Векторы должны иметь равную длину')
            return NotImplemented
        return wrapper

    @is_valid
    def __add__(self, other):
        _x = tuple(map(sum, zip(*self.__dict__.values(),
                                *other.__dict__.values())))
        return __class__(*_x)

    @is_valid
    def __mul__(self, other):
        _x = sum(map(lambda a, b: a * b, *self.__dict__.values(),
                     *other.__dict__.values()))
        return _x

    @is_valid
    def __sub__(self, other):
        _x = tuple(map(lambda a, b: a - b, *self.__dict__.values(),
                       *other.__dict__.values()))
        return __class__(*_x)

    @is_valid
    def __eq__(self, other):
        return self.x == other.x
```
* Второй вариант решения

```python
class Vector:
    def __init__(self, *args):
        self.coords = args

    def _if_different_coords(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError('Векторы должны иметь равную длину')

    def norm(self):
        return sum(digit ** 2 for digit in self.coords) ** 0.5

    def __str__(self):
        return str(self.coords)

    def __add__(self, other):
        self._if_different_coords(other)
        if isinstance(other, type(self)):
            return type(self)(*(self_coord + other_coord for self_coord, other_coord in zip(self.coords, other.coords)))
        return NotImplemented

    def __sub__(self, other):
        self._if_different_coords(other)
        if isinstance(other, type(self)):
            return type(self)(*(self_coord - other_coord for self_coord, other_coord in zip(self.coords, other.coords)))
        return NotImplemented

    def __mul__(self, other):
        self._if_different_coords(other)
        if isinstance(other, type(self)):
            return sum(self_coord * other_coord for self_coord, other_coord in zip(self.coords, other.coords))
        return NotImplemented

    def __eq__(self, other):
        self._if_different_coords(other)
        if isinstance(other, type(self)):
            return self.coords == other.coords
        return NotImplemented
```


