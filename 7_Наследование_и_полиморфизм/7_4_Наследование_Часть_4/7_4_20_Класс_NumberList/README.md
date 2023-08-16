<h2 style="text-align:center">Класс NumberList</h2>

### Реализуйте класс NumberList, наследника класса UserList, описывающий список, элементами которого могут быть лишь числа. При создании экземпляра класс должен принимать один аргумент:
* iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса NumberList. Если хотя бы один элемент переданного итерируемого объекта не является числом, должно быть возбуждено исключение TypeError с текстом:
> Элементами экземпляра класса NumberList должны быть числа
#### Итерируемый объект может быть не передан, в таком случае начальный набор элементов считается пустым
#### При изменении экземпляра класса NumberList с помощью индексов, операций сложения (+, +=) и методов append(), extend() и insert() должна производиться проверка на то, что добавляемые элементы являются числами, в противном случае должно возбуждаться исключение TypeError с текстом:
> Элементами экземпляра класса NumberList должны быть числа
##### Примечание 1. Числами будет считать экземпляры классов int и float.
##### Примечание 2. Экземпляр класса NumberList не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса NumberList измениться  не должен.
##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 4. Никаких ограничений касательно реализации класса NumberList нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">numberlist = NumberList([1, 2])<br>
                          numberlist.append(3)<br>
                          numberlist.extend([4, 5])<br>
                          numberlist.insert(0, 0)<br>
                          print(numberlist)<br></td>
      <td align="center">numberlist = NumberList([0, 1.0])<br>
                          numberlist[1] = 1<br>
                          numberlist = numberlist + NumberList([2, 3])<br>
                          numberlist += NumberList([4, 5])<br>
                          print(numberlist)<br></td>
      <td align="center">try:<br>
                              numberlist = NumberList(['a', 'b', 'c'])<br>
                          except TypeError as error:<br>
                              print(error)<br></td>
      <td align="center">numberlist = NumberList([1, 2, 3])<br>
                          try:<br>
                              numberlist.append('4')<br>
                          except TypeError as error:<br>
                              print(error)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        [0, 1, 2, 3, 4, 5]<br>
      </td>
      <td align="center">
                        [0, 1, 2, 3, 4, 5]<br>
      </td>
      <td align="center">
                        Элементами экземпляра класса NumberList должны быть числа<br>
      </td>
      <td align="center">
                        Элементами экземпляра класса NumberList должны быть числа<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from collections import UserList


def decorator_lst(func):
    def wrapper(self, args=[]):
        if isinstance(args, (list, NumberList)):
            if all([self.chek_int(i) for i in args]):
                return func(self, args)
            else:
                raise TypeError('Элементами экземпляра класса NumberList' +
                                ' должны быть числа')
        else:
            if self.chek_int(args):
                return func(self, args)
            else:
                raise TypeError('Элементами экземпляра класса NumberList' +
                                ' должны быть числа')
    return wrapper


class NumberList(UserList):
    @decorator_lst
    def __init__(self, iterable=[]):
        return super().__init__(iterable)

    @decorator_lst
    def __add__(self, other):
        return super().__add__(other)

    @decorator_lst
    def __radd__(self, other):
        return super().__radd__(other)

    @decorator_lst
    def __iadd__(self, other):
        return super().__iadd__(other)

    @decorator_lst
    def append(self, item):
        return super().append(item)

    @decorator_lst
    def extend(self, other):
        return super().extend(other)

    def insert(self, i, item):
        if self.chek_int(item):
            return super().insert(i, item)
        raise TypeError('Элементами экземпляра класса NumberList' +
                        ' должны быть числа')

    def chek_int(self, num):
        return isinstance(num, (int, float))
```
* Второй вариант решения

```python
from collections import UserList


class NumberList(UserList):
    def __init__(self, iterable=()):
        super().__init__(self._validate(item) for item in iterable)

    @staticmethod
    def _validate(value):
        if isinstance(value, (int, float)):
            return value
        raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def insert(self, index, item):
        self.data.insert(index, self._validate(item))

    def append(self, item):
        self.data.append(self._validate(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(self._validate(item) for item in other)

    def __add__(self, other):
        if isinstance(other, (type(self), list)):
            return super().__add__(self._validate(item) for item in other)
        return NotImplemented

    def __iadd__(self, other):
        super().__iadd__(self._validate(item) for item in other)
        return self
```


