<h2 style="text-align:center">Класс House</h2>

### Вам доступен класс House, описывающий дом. При создании экземпляра класс принимает два аргумента в следующем порядке:
* color — цвет дома
* rooms — количество комнат в доме

#### Экземпляр данного класса имеет два атрибута:
* color — цвет дома
* rooms — количество комнат в доме
#### Реализуйте для класса House два метода экземпляра:
* paint() — метод, принимающий в качестве аргумента значение new_color и изменяющий текущий цвет дома на new_color
* add_rooms() — метод, принимающий в качестве аргумента целое число n и увеличивающий количество комнат в доме на n

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
```python
class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms
```

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">house = House('white', 4)<br>
                        print(house.color)<br>
                        print(house.rooms)<br></td>
      <td align="center">house = House('white', 4)<br>
                         house.paint('black')<br>
                         house.add_rooms(1)<br>
                         print(house.color)<br>
                         print(house.rooms)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
      white<br>
      4<br>
      </td>
      <td align="center">
                       black<br>
                       5<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def paint(self, new_color):
        self.color = new_color

    def add_rooms(self, n):
        self.rooms += n
```



