<h2 style="text-align:center">Класс Item</h2>


### Требовалось реализовать класс Item, описывающий предмет. При создании экземпляра класс должен был принимать три аргумента в следующем порядке:
* name — название предмета
* price — цена предмета в рублях
* quantity — количество предметов
#### Предполагалось, что при обращении к атрибуту name экземпляра класса Item будет возвращаться его название с заглавной буквы, а при обращении к атрибуту total — произведение цены предмета на его количество.
#### Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте правильный класс Item.
```python
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        if name == 'total': 
            return self.price * self.quantity
        elif name == 'name':
            return self.name.title()
        return self.__dict__[name]
```
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса Item нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">fruit = Item('banana', 15, 5)<br>
                          print(fruit.price)<br>
                          print(fruit.quantity)<br></td>
      <td align="center">fruit = Item('banana', 15, 5)<br>
                          print(fruit.name)<br>
                          print(fruit.total)<br></td>                      
      <td align="center">course = Item('pygen', 3900, 2)<br>
                        print(course.name)<br>
                        print(course.price)<br>
                        print(course.quantity)<br>
                        print(course.total)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        15<br>
                        5<br>
      </td>
      <td align="center">
                        Banana<br>
                        75<br>
      </td>
      <td align="center">
                        Pygen<br>
                        3900<br>
                        2<br>
                        7800<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        if name == 'total': 
            return self.price * self.quantity
        elif name == 'name':
            return object.__getattribute__(self, name).title()
        return object.__getattribute__(self, name)
```
* Второй вариант решения

```python
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, attr):
        if attr == 'name':
            return object.__getattribute__(self, attr).title()
        return object.__getattribute__(self, attr)
    
    def __getattr__(self, attr):
        if attr == 'total':
            return self.price * self.quantity
        raise AttributeError
```


