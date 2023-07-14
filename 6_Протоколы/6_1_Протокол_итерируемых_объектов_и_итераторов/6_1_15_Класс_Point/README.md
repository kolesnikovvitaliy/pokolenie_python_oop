<h2 style="text-align:center">Класс Point</h2>

### Реализуйте класс Point, описывающий точку в пространстве. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
* x — координата точки по оси x
* y — координата точки по оси y
* z — координата точки по оси z
#### Экземпляр класса Point должен иметь следующее формальное строковое представление:
> Point(<координата x>, <координата y>, <координата z>)
#### Также экземпляр класса Point должен быть итерируемым объектом, элементами которого являются его координаты по осям x, y и z.

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса Point нет, она может быть произвольной.
<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">point = Point(1, 2, 3)<br>
                          print(list(point))<br></td>
      <td align="center">point = Point(1, 2, 3)<br>
                          x, y, z = point<br>
                          print(x, y, z)<br></td>
      <td align="center">points = [Point(4, 7, 0), Point(1, 5, 10), Point(12, 23, 44)]<br>
                          print(points)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        [1, 2, 3]<br>
      </td>
      <td align="center">
                        1 2 3<br>
      </td>
      <td align="center">
                        [Point(4, 7, 0), Point(1, 5, 10), Point(12, 23, 44)]<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def _lst(self):
        return self.x, self.y, self.z

    def __repr__(self) -> str:
        return f"{__class__.__name__}{self._lst}"
    
    def __iter__(self):
        yield from self._lst
```
* Второй вариант решения

```python
class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return f'Point({self.x}, {self.y}, {self.z})'

    def __iter__(self):
        yield from (self.x, self.y, self.z)
```


