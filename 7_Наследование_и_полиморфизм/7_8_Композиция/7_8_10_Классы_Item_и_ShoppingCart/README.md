<h2 style="text-align:center">Классы Item и ShoppingCart</h2>

### 1. Реализуйте класс Item, описывающий товар. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

* name — название товара
* price — цена товара в долларах
#### Экземпляр класса Item должен иметь следующее неформальное строковое представление:

> <название товара>, <цена товара>$
### 2. Также реализуйте класс ShoppingCart, описывающий корзину для покупок. При создании экземпляра класс должен принимать один аргумент:

* items — итерируемый объект, определяющий начальный набор товаров в корзине. Если не передан, корзина считается пустой
#### Класс ShoppingCart должен иметь три метода экземпляра:

* add() — метод, принимающий в качестве аргумента товар и добавляющий его в корзину
* total() — метод, возвращающий суммарную стоимость всех товаров в корзине
* remove() — метод, принимающий в качестве аргумента название товара и удаляющий его из корзины. Если в корзине несколько товаров с указанным именем, они должны быть удалены все
#### Экземпляр класса ShoppingCart должен иметь следующее неформальное строковое представление:

> <название первого товара в корзине>, <цена первого товара в корзине>

> <название второго товара в корзине>, <цена второго товара в корзине>

> ...
##### Примечание 1. Если корзина для покупок пуста, то ее неформальным строковым представлением должна быть пустая строка.

##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

##### Примечание 3. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">item1 = Item('Yoga Mat', 130)<br>
                          item2 = Item('Flannel Shirt', 22)<br>
                          print(item1)<br>
                          print(item2)<br></td>
      <td align="center">shopping_cart = ShoppingCart([Item('Yoga Mat', 130)])<br>
                          shopping_cart.add(Item('Flannel Shirt', 22))<br>
                          print(shopping_cart)<br>
                          print(shopping_cart.total())<br>
      <td align="center">shopping_cart = ShoppingCart([Item('Yoga Mat', 130), Item('Flannel Shirt', 22)])<br>
                          shopping_cart.remove('Yoga Mat')<br>
                          print(shopping_cart)<br>
                          print(shopping_cart.total())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        Yoga Mat, 130$<br>
                        Flannel Shirt, 22$<br>
      </td>
      <td align="center">
                        Yoga Mat, 130$<br>
                        Flannel Shirt, 22$<br>
                        152<br>
      </td>
      <td align="center">
                        Flannel Shirt, 22$<br>
                        22<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'


class ShoppingCart:
    def __init__(self, items=[]):
        self.items = items

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum(map(lambda x: int(str(x).split()[-1][:-1]), self.items))

    def remove(self, name):
        for k, v in enumerate(self.items):
            if name in str(v):
                del self.items[k]

    def __str__(self):
        return '\n'.join(map(str, self.items))
```
* Второй вариант решения

```python
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'


class ShoppingCart:
    def __init__(self, items=()):
        self.items = list(items)

    def add(self, item):
        self.items.append(item)

    def remove(self, name):
        self.items = [item for item in self.items if item.name != name]

    def total(self):
        return sum(item.price for item in self.items)

    def __str__(self):
        return '\n'.join(str(item) for item in self.items)
```


