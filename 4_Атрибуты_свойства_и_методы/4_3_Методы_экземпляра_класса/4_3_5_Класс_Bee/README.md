<h2 style="text-align:center">Класс Bee</h2>

### Реализуйте класс Bee, описывающий пчелку, которая перемещается по координатной плоскости в четырех направлениях: вверх, вниз, влево и вправо. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* x — координата пчелки по оси x, по умолчанию имеет значение 0
* y — координата пчелки по оси y, по умолчанию имеет значение 0

#### Экземпляр класса Bee должен иметь два атрибута:
* x — координата пчелки по оси x
* y — координата пчелки по оси y
#### Класс Bee должен иметь четыре метода экземпляра:
* move_up() — метод, принимающий в качестве аргумента целое число n и увеличивающий координату пчелки по оси y на n
* move_down() — метод, принимающий в качестве аргумента целое число n и уменьшающий координату пчелки по оси y на n
* move_right() — метод, принимающий в качестве аргумента целое число n и увеличивающий координату пчелки по оси x на n
* move_left() — метод, принимающий в качестве аргумента целое число n и уменьшающий координату пчелки по оси x на n



##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.


<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">bee = Bee()<br>
                        print(bee.x, bee.y)<br></td>
      <td align="center">bee = Bee()<br>
                         bee.move_up(1)<br>
                         bee.move_right(1)<br>
                         bee.move_down(1)<br>
                         bee.move_left(1)<br>
                         print(bee.x, bee.y)<br></td>
      <td align="center">bee = Bee()<br>
                         bee.move_right(2)<br>
                        bee.move_right(2)<br>
                        bee.move_up(3)<br>
                        bee.move_left(1)<br>
                        bee.move_down(1)<br>
                        print(bee.x, bee.y)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
      0 0<br>
      </td>
      <td align="center">
                       0 0<br>
      </td>
      <td align="center">
                       3 2<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Bee:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_up(self, n):
        self.y += n

    def move_down(self, n):
        self.y -= n

    def move_right(self, n):
        self.x += n

    def move_left(self, n):
        self.x -= n
```
* Второй вариант решения
```python
class Bee:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def move_up(self, n: int):
        self.y += n

    def move_down(self, n: int):
        self.y -= n

    def move_right(self, n: int):
        self.x += n

    def move_left(self, n: int):
        self.x -= n
```


