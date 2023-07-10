<h2 style="text-align:center">Класс Filter</h2>

### Реализуйте класс Filter, описывающий объект для фильтрации элементов итерируемых объектов. При создании экземпляра класс должен принимать один аргумент:
* predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
#### Экземпляр класса Filter должен являться вызываемым объектом и принимать один аргумент:
* iterable — итерируемый объект
#### Экземпляр класса Filter должен возвращать список, элементами которого являются элементы итерируемого объекта iterable, для которых функция predicate вернула значение True.

##### Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного в качестве аргумента значения.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса Filter нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">leave_even = Filter(lambda x: x % 2 == 0)<br>
                          numbers = [1, 2, 3, 4, 5, 6]<br>
                          print(leave_even(numbers))<br></td>
      <td align="center">more_than_five = Filter(lambda x: x > 5)<br>
                          numbers = [13, 1, 4, 10, 10, 7]<br>
                          print(more_than_five(numbers))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        [2, 4, 6]<br>
      </td>
      <td align="center">
                        [13, 10, 10, 7]<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Filter:
    def __init__(self, predicate=None):
        self.predicate = predicate

    def __call__(self, iterable):
        if self.predicate is not None:
            return list(filter(self.predicate, iterable))
        return list(filter(bool, iterable))
```
* Второй вариант решения

```python
class Filter:
    def __init__(self, func):
        self.func = func or bool
        
    def __call__(self, itrbl):
        return [x for x in itrbl if self.func(x)]
```


