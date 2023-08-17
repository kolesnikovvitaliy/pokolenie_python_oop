<h2 style="text-align:center">Класс BitArray</h2>


### Реализуйте класс BitArray, описывающий битовый список, то есть список, элементами которого являются только нули и единицы. При создании экземпляра класс должен принимать один аргумент:
* iterable — итерируемый объект, определяющий начальный набор элементов битового списка. Если не передан, начальный набор считается пустым
#### Экземпляр класса BitArray должен иметь следующее неформальное строковое представление:
> [<первый элемент битового списка>, <второй элемент битового списка>, ...]
#### При передаче экземпляра класса BitArray в функцию len() должно возвращаться количество элементов в нем. При передаче экземпляра класса BitArray в функцию reversed() должен возвращаться итератор, элементами которого являются элементы переданного экземпляра класса BitArray , расположенные в обратном порядке.
#### Экземпляр класса BitArray должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.
#### Помимо этого, экземпляр класса BitArray должен поддерживать операцию проверки на принадлежность с помощью оператора in.
#### Также экземпляр класса BitArray должен позволять получать значения своих элементов с помощью индексов, причем как положительных, так и отрицательных.
#### Вдобавок ко всему, экземпляр класса BitArray должен поддерживать унарный оператор ~, выполняющий операцию логического отрицания для каждого бита битового списка, тем самым преобразуя 0 в 1, а 1 в 0. Результатом работы оператора должен являться новый экземпляр класса BitArray.
#### Наконец, экземпляры класса BitArray должны поддерживать между собой логические операции с помощью операторов & и |:
* оператор & должен выполнять операцию логического И над каждой парой битов двух битовых списков равной длины. Результатом работы оператора должен являться новый экземпляр класса BitArray

* оператор | должен выполнять операцию логического ИЛИ над каждой парой битов двух битовых списков равной длины. Результатом работы оператора должен являться новый экземпляр класса BitArray

##### Примечание 1. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве родительского.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Экземпляр класса BitArray не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса BitArray измениться  не должен.
##### Примечание 4. Если объект, с которым выполняется логическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
##### Примечание 5. Никаких ограничений касательно реализации класса BitArray нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">bitarray = BitArray([1, 0, 1, 1])<br>
                          print(bitarray)<br>
                          print(~bitarray)<br>
                          print(bitarray[0])<br>
                          print(bitarray[1])<br>
                          print(bitarray[-1])<br>
                          print(0 in bitarray)<br>
                          print(1 not in bitarray)<br></td>
      <td align="center">bitarray1 = BitArray([1, 0, 1, 1])<br>
                        bitarray2 = BitArray([0, 0, 0, 1])<br>
                        bitarray3 = bitarray1 | bitarray2<br>
                        bitarray4 = bitarray1 & bitarray2<br>
                        bitarray5 = ~bitarray1<br>
                        print(bitarray3, type(bitarray3))<br>
                        print(bitarray4, type(bitarray4))<br>
                        print(bitarray5, type(bitarray5))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        [1, 0, 1, 1]<br>
                        [0, 1, 0, 0]<br>
                        1<br>
                        0<br>
                        1<br>
                        True<br>
                        False<br>
      </td>
      <td align="center">
                        [1, 0, 1, 1] <class '__main__.BitArray'><br>
                        [0, 0, 0, 1] <class '__main__.BitArray'><br>
                        [0, 1, 0, 0] <class '__main__.BitArray'><br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from collections.abc import Sequence


class BitArray(Sequence):
    def __init__(self, iterable=[]):
        self.lst = iterable[:]

    def __str__(self):
        return f"{self.lst}"

    def __iter__(self):
        return iter(self.lst)

    def __contains__(self, value):
        return value in self.lst

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, index):
        return self.lst[index]

    def __invert__(self):
        return __class__(list(
            map(lambda x: 1 if x == 0 else 0, self.lst)))

    def __or__(self, other):
        if isinstance(other, __class__):
            return __class__(list(
                map(lambda x, y: x | y, self.lst, other.lst)))
        return NotImplemented

    def __and__(self, other):
        if isinstance(other, __class__):
            return __class__(list(
                map(lambda x, y: x & y, self.lst, other.lst)))
        return NotImplemented
```
* Второй вариант решения

```python
from collections.abc import Sequence


class BitArray(Sequence):
    def __init__(self, iterable=()):
        self._data = list(iterable)

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        if isinstance(index, (int, slice)):
            return self._data[index]
        return NotImplemented

    def __invert__(self):
        return type(self)(int(not item) for item in self._data)

    def __or__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self_item | other_item for self_item, other_item in zip(self._data, other._data))
        return NotImplemented

    def __and__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self_item & other_item for self_item, other_item in zip(self._data, other._data))
        return NotImplemented
```


