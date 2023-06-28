<h2 style="text-align:center">Класс Rectangle</h2>

### Реализуйте класс Rectangle, описывающий прямоугольник. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* length — длина прямоугольника
* width — ширина прямоугольника
#### Экземпляр класса Rectangle должен иметь два атрибута:
* length — длина прямоугольника
* width — ширина прямоугольника
#### Класс Rectangle должен иметь один метод класса:
* square() — метод, принимающий в качестве аргумента число side и возвращающий экземпляр класса Rectangle c длиной и шириной, равными side

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">rectangle = Rectangle(4, 5)<br>
                          print(rectangle.length)<br>
                          print(rectangle.width)<br></td>
      <td align="center">rectangle = Rectangle.square(5)<br>
                        print(rectangle.length)<br>
                        print(rectangle.width)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        4<br>
                        5<br>
      </td>
      <td align="center">
                        5<br>
                        5<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @classmethod
    def square(cls, side):
        return cls(side, side)
```
* Второй вариант решения

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @classmethod
    def square(cls, side):
        return cls(side, side)
```


