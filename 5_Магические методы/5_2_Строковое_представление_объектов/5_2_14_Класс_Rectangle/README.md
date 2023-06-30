<h2 style="text-align:center">Класс Rectangle</h2>

### Вам доступен класс Rectangle, описывающий прямоугольник. При создании экземпляра класс принимает два аргумента в следующем порядке:
* length — длина прямоугольника
* width — ширина прямоугольника

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
```
#### Реализуйте для экземпляров класса Rectangle следующее формальное и неформальное строковое представление:
> Rectangle(<длина прямоугольника>, <ширина прямоугольника>)
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса Rectangle нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">rectangle = Rectangle(1, 2)<br>
                          print(str(rectangle))<br>
                          print(repr(rectangle))<br></td>
      <td align="center">rectangle1 = Rectangle(1, 2)<br>
                        rectangle2 = Rectangle(3, 4)<br>
                        print(rectangle1)<br>
                        print(repr(rectangle2))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Rectangle(1, 2)<br>
                        Rectangle(1, 2)<br>
      </td>
      <td align="center">
                        Rectangle(1, 2)<br>
                        Rectangle(3, 4)<br>
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
    
    def __repr__(self) -> str:
        return f"Rectangle({self.length}, {self.width})"
```
* Второй вариант решения

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def __repr__(self):
        return f'{self.__class__.__name__}({self.length}, {self.width})'
```


