<h2 style="text-align:center">Класс Postman</h2>

### Реализуйте класс Postman, описывающий почтальона. При создании экземпляра класс не должен принимать никаких аргументов.


#### Экземпляр класса Postman должен иметь один атрибут:
* delivery_data — изначально пустой список адресов, по которым следует доставить письма
#### Экземпляр класса Postman должен иметь три метода экземпляра:
* add_delivery() — метод, принимающий в качестве аргументов улицу, дом и квартиру, и добавляющий в список адресов эти данные в виде кортежа:
(<улица>, <дом>, <квартира>)
* get_houses_for_street() — метод, принимающий в качестве аргумента улицу и возвращающий список всех домов на этой улице, в которые требуется доставить письма
* get_flats_for_house() — метод, принимающий в качестве аргументов улицу и дом и возвращающий список всех квартир в этом доме, в которые требуется доставить письма
##### Примечание 1. Дома и квартиры в списках, возвращаемых методами get_houses_for_street() и get_flats_for_house(), должны располагаться в том порядке, в котором они были добавлены.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">postman = Postman()<br>
                          print(postman.delivery_data)<br>
                          print(postman.get_houses_for_street('3-я ул. Строителей'))<br>
print(postman.get_flats_for_house('3-я ул. Строителей', 25))<br></td>
      <td align="center">postman = Postman()<br>
                          postman.add_delivery('Советская', 151, 74)<br>
                          postman.add_delivery('Советская', 151, 75)<br>
                          postman.add_delivery('Советская', 90, 2)<br>
                          postman.add_delivery('Советская', 151, 74)<br>
                          print(postman.get_houses_for_street('Советская'))<br>
print(postman.get_flats_for_house('Советская', 151))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
      []<br>
      []<br>
      []<br>
      </td>
      <td align="center">
                       [151, 90]<br>
                       [74, 75]<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from collections import Counter


class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, st, h, ap):
        self.delivery_data.append((st, h, ap))

    def get_houses_for_street(self, st):
        return list(map(lambda j: j[0], Counter(map(lambda y: y[1], filter(lambda x: st in x , self.delivery_data ))).items()))
    def get_flats_for_house(self, st, h):
        return list(map(lambda j: j[0], Counter(map(lambda y: y[2], filter(lambda x: st in x and h in x, self.delivery_data ))).items()))


```
* Второй вариант решения
```python
class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, apartment):
        self.delivery_data.append((street, house, apartment))

    def get_houses_for_street(self, street):
        return list({h: None for s, h, _ in self.delivery_data if s == street})

    def get_flats_for_house(self, street, house):
        return list({a: None for s, h, a in self.delivery_data if s == street and h == house})
```


