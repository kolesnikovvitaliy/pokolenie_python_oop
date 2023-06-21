<h2 style="text-align:center">Класс Scales</h2>

### Реализуйте класс Scales, описывающий весы с двумя чашами. При создании экземпляра класс не должен принимать никаких аргументов.


#### Класс Scales должен иметь три метода экземпляра:
* add_right() — метод, принимающий в качестве аргумента массу груза в килограммах и добавляющий на правую чашу весов этот груз
* add_left() — метод, принимающий в качестве аргумента массу груза в килограммах и добавляющий на левую чашу весов этот груз
* get_result() — метод, возвращающий строку Весы в равновесии, если массы грузов на чашах совпадают, Правая чаша тяжелее — если правая чаша тяжелее, Левая чаша тяжелее — если левая чаша тяжелее

##### Примечание 1. Пустые весы всегда находятся в равновесии.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.


<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">scales = Scales()<br>
                        scales.add_right(1)<br>
                        scales.add_right(1)<br>
                        scales.add_left(2)<br>
                        print(scales.get_result())<br></td>
      <td align="center">scales = Scales()<br>
                          scales.add_right(1)<br>
                          scales.add_left(2)<br>
                          print(scales.get_result())<br></td>
    <td align="center">scales = Scales()<br>
                      scales.add_right(2)<br>
                      scales.add_left(1)<br>
                      print(scales.get_result())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
      Весы в равновесии<br>
      </td>
      <td align="center">
                       Левая чаша тяжелее<br>
      </td>
      <td align="center">
                       Правая чаша тяжелее<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Scales:
    def __init__(self):
        self.right = 0
        self.left = 0
    
    def add_right(self, n):
        self.right += n

    def add_left(self, n):
        self.left += n
    
    def get_result(self):
        if self.right > self.left:
            return 'Правая чаша тяжелее'
        elif self.right < self.left:
            return 'Левая чаша тяжелее'
        else: 
            return 'Весы в равновесии'

```
* Второй вариант решения
```python
class Scales:
    def __init__(self):
        self.left = 0
        self.right = 0

    def add_left(self, w):
        self.left += w

    def add_right(self, w):
        self.right += w

    def get_result(self):
        if self.left == self.right:
            return 'Весы в равновесии'
        return ('Левая чаша тяжелее', 'Правая чаша тяжелее')[self.right > self.left]
```


