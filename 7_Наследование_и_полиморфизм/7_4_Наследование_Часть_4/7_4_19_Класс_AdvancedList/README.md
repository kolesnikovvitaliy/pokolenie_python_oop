<h2 style="text-align:center">Класс AdvancedList</h2>

### Реализуйте класс AdvancedList, наследника класса list, описывающий список с дополнительным функционалом. Процесс создания экземпляра класса AdvancedList должен совпадать с процессом создания экземпляра класса list.
#### Класс AdvancedList должен иметь три метода экземпляра:
* join() — метод, объединяющий все элементы экземпляра класса AdvancedList в строку и возвращающий полученный результат. Метод должен принимать один строковый аргумент, по умолчанию равный пробелу, который является разделителем элементов списка в результирующей строке
* map() — метод, принимающий в качестве аргумента функцию func и применяющий ее к каждому элементу экземпляра класса AdvancedList. Метод должен изменять исходный экземпляр класса AdvancedList, а не возвращать новый
* filter() — метод, принимающий в качестве аргумента функцию func и удаляющий из экземпляра класса AdvancedList те элементы, для которых функция func вернула значение False. Метод должен изменять исходный экземпляр класса AdvancedList, а не возвращать новый

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса AdvancedList нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">advancedlist = AdvancedList([1, 2, 3, 4, 5])<br>
                          print(advancedlist.join())<br>
                          print(advancedlist.join('-'))<br></td>
      <td align="center">advancedlist = AdvancedList([1, 2, 3, 4, 5])<br>
                        advancedlist.map(lambda x: -x)<br>
                        print(advancedlist)<br></td>
      <td align="center">advancedlist = AdvancedList([1, 2, 3, 4, 5])<br>
                        advancedlist.filter(lambda x: x % 2 == 0)<br>
                        print(advancedlist)<br></td>
      <td align="center">advancedlist = AdvancedList([0, 1, 2, '', 3, (), 4, 5, False, {}])<br>
                        id1 = id(advancedlist)<br>
                        advancedlist.filter(bool)<br>
                        id2 = id(advancedlist)<br>
                        print(advancedlist)<br>
                        print(id1 == id2)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        1 2 3 4 5<br>
                        1-2-3-4-5<br>
      </td>
      <td align="center">
                        [-1, -2, -3, -4, -5]<br>
      </td>
      <td align="center">
                        [2, 4]<br>
      </td>
      <td align="center">
                        [1, 2, 3, 4, 5]<br>
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class AdvancedList(list):
    def join(self, separator=' '):
        return separator.join(map(str, self))
    
    def map(self, func):
        self[:] = map(func, self)
        return self
        
    def filter(self, func):
        self[:] = filter(func, self)
        return self
```
* Второй вариант решения

```python
class AdvancedList(list):
    def __init__(self, iterable=(), default=None):
        super().__init__(item for item in iterable)
        self._default = default

    def extend_self(self, data):
        self.clear()
        self.extend(data)

    def join(self, sep=' '):
        return sep.join(str(item) for item in self)

    def map(self, func):
        new_data = list(func(item) for item in self)
        self.extend_self(new_data)

    def filter(self, predicate):
        new_data = list(filter(predicate, self))
        self.extend_self(new_data)
```


