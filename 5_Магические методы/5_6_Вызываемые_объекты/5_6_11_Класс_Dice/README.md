<h2 style="text-align:center">Класс Dice</h2>

### Реализуйте класс Dice, описывающий игральный кубик с определенным количеством граней. При создании экземпляра класс должен принимать один аргумент:
* sides — количество граней игрального кубика
#### Экземпляр класса Dice должен являться вызываемым объектом и не принимать никаких аргументов. При вызове он должен возвращать значение случайной грани игрального кубика. Например, если кубик имеет 6 граней, экземпляр класса Dice должен вернуть случайное число из диапазона [1; 6].

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса Dice нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">kingdice = Dice(6)<br>
                          print(kingdice() in [1, 2, 3, 4, 5, 6])<br>
                          print(kingdice() in [1, 2, 3, 4, 5, 6])<br>
                          print(kingdice() in [7, 8, 9, 10])<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
                        True<br>
                        False<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Dice:
    def __init__(self, sides):
        self.sides = sides

    def __call__(self):
        import random
        return random.randint(1, self.sides)
```
* Второй вариант решения

```python
from random import randint

class Dice:
    def __init__(self, sides):
        self.sides = sides
    
    def __call__(self):
        return randint(1, self.sides)
```


