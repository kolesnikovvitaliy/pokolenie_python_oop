<h2 style="text-align:center">Класс DefaultList</h2>

### Реализуйте класс DefaultList, наследника класса UserList, описывающий список, который при попытке получить элемент по несуществующему индексу возвращает значение по умолчанию. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса DefaultList. Если не передан, начальный набор элементов считается пустым
* default — значение, возвращаемое при попытке получить элемент по несуществующему индексу. По умолчанию равняется None
##### Примечание 1. Экземпляр класса DefaultList не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса DefaultList измениться  не должен.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса DefaultList нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">defaultlist = DefaultList([1, 2, 3])<br>
                          print(defaultlist[0])<br>
                          print(defaultlist[-1])<br>
                          print(defaultlist[100])<br>
                          print(defaultlist[-100])<br></td>
      <td align="center">defaultlist = DefaultList([1, 2, 3], 0)<br>
                          print(defaultlist[0])<br>
                          print(defaultlist[-1])<br>
                          print(defaultlist[100])<br>
                          print(defaultlist[-100])<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        1<br>
                        3<br>
                        None<br>
                        None<br>
      </td>
      <td align="center">
                        1<br>
                        3<br>
                        0<br>
                        0<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from collections import UserList


class DefaultList(UserList):
    def __init__(self, iterable=[], default=None):
        super().__init__(iterable)
        self.default = default

    def __getitem__(self, i):
        try:
            if isinstance(i, slice):
                return self.__class__(self.data[i])
            else:
                return self.data[i]
        except IndexError:
            return self.default
```
* Второй вариант решения

```python
from collections import UserList


class DefaultList(UserList):
    def __init__(self, iterable=(), default=None):
        super().__init__(item for item in iterable)
        self._default = default

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except IndexError:
            return self._default
```


