<h2 style="text-align:center">Класс SortedList</h2>

### Реализуйте класс SortedList, описывающий список, который автоматически сортируется при создании и любом изменении. При создании экземпляра класс должен принимать один аргумент:
* iterable — итерируемый объект, определяющий начальный набор элементов отсортированного списка. Если не передан, начальный набор элементов считается пустым
#### Класс SortedList должен иметь три метода экземпляра:
* add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в экземпляр класса SortedList
* discard() — метод, принимающий в качестве аргумента произвольный объект и удаляющий все его включения из экземпляра класса SortedList, если он в нем присутствует
* update() — метод, принимающий в качестве аргумента итерируемый объект и добавляющий все его элементы в экземпляр класса SortedList
#### Также класс SortedList должен иметь такие методы экземпляра, как append(), insert(), extend() и reverse(), при попытке воспользоваться которыми должно быть возбуждено исключение NotImplementedError.
#### Экземпляр класса SortedList должен иметь следующее формальное строковое представление:
> SortedList([<первый элемент списка>, <второй элемент списка>, ...])

#### При передаче экземпляра класса SortedList в функцию len() должно возвращаться количество элементов в нем. При попытке передачи экземпляра класса SortedList в функцию reversed() должно быть возбуждено исключение NotImplementedError.
#### Помимо этого, экземпляр класса SortedList должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.
#### Также экземпляр класса SortedList должен поддерживать операцию проверки на принадлежность с помощью оператора in.
#### Вдобавок ко всему, экземпляр класса SortedList должен позволять получать и удалять значения своих элементов с помощью индексов, причем как положительных, так и отрицательных. При попытке изменить значение элемента по его индексу должно быть возбуждено исключение NotImplementedError.
#### Экземпляры класса SortedList должны поддерживать между собой арифметические операции с помощью операторов + и +=:
* оператор + должен выполнять операцию сложения двух отсортированных списков путем их конкатенации и последующей сортировки. Результатом работы оператора должен являться новый экземпляр класса SortedList
* оператор += должен выполнять операцию сложения двух отсортированных списков путем их конкатенации и последующей сортировки. Результатом работы оператора должен являться левый экземпляр класса SortedList
####  Наконец, экземпляр класса SortedList должен поддерживать операцию умножения на целое число n с помощью операторов * и *=:
* оператор * должен выполнять операцию умножения отсортированного списка на число с последующей его сортировкой. Результатом работы оператора должен являться новый экземпляр класса SortedList
* оператор *= должен выполнять операцию умножения отсортированного списка на число с последующей его сортировкой. Результатом работы оператора должен являться левый экземпляр класса SortedList
##### Примечание 1. Гарантируется, что элементами одного экземпляра класса SortedList являются объекты, сравнимые между собой.
##### Примечание 2. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве родительского.
##### Примечание3. Экземпляр класса SortedList не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса SortedList измениться  не должен.
##### Примечание 4.  Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий операцию сравнения, должен вернуть константу NotImplemented.
##### Примечание 5. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 6. Никаких ограничений касательно реализации класса SortedList нет, она может быть произвольной. Однако попробуйте решить задачу так, чтобы операция добавления элементов в список выполнялась как можно быстрее.


<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">numbers = SortedList([5, 3, 4, 2, 1])<br>
                          print(numbers)<br>
                          print(numbers[1])<br>
                          print(numbers[-2])<br>
                          numbers.add(0)<br>
                          print(numbers)<br>
                          numbers.discard(4)<br>
                          print(numbers)<br>
                          numbers.update([4, 6])<br>
                          print(numbers)<br></td>
      <td align="center">numbers = SortedList([5, 3, 4, 2, 1])<br>
                          print(len(numbers))<br>
                          print(*numbers)<br>
                          print(1 in numbers)<br>
                          print(6 in numbers)<br></td>
      <td align="center">numbers1 = SortedList([1, 3, 5])<br>
                          numbers2 = SortedList([2, 4])<br>
                          print(numbers1 + numbers2)<br>
                          print(numbers1 * 2)<br>
                          print(numbers2 * 2)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        SortedList([1, 2, 3, 4, 5])<br>
                        2<br>
                        4<br>
                        SortedList([0, 1, 2, 3, 4, 5])<br>
                        SortedList([0, 1, 2, 3, 5])<br>
                        SortedList([0, 1, 2, 3, 4, 5, 6])<br>
      </td>
      <td align="center">
                        5<br>
                        1 2 3 4 5<br>
                        True<br>
                        False<br>
      </td>
      <td align="center">
                        SortedList([1, 2, 3, 4, 5])<br>
                        SortedList([1, 1, 3, 3, 5, 5])<br>
                        SortedList([2, 2, 4, 4])<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from collections.abc import Sequence


class SortedList(Sequence):
    def __init__(self, iterable=[]):
        self.iterable = sorted(iterable)

    def add(self, other):
        if isinstance(other, int):
            tmp_list = [self.iterable, [other]]
            self.iterable = sorted([i for lst in tmp_list for i in lst])
        else:
            self.__add_list(self, other)
        return self.iterable

    @staticmethod
    def __add_list(self, other):
        tmp_list = [self.iterable, other]
        self.iterable = sorted([i for lst in tmp_list for i in lst])
        return self

    def discard(self, obj):
        self.iterable = [i for i in self.iterable if i != obj]
        return __class__(self.iterable)

    def update(self, obj):
        return __class__.add(self, obj)

    def append(self, item):
        raise NotImplementedError

    def insert(self, index, item):
        raise NotImplementedError

    def extend(self, item):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def __repr__(self):
        return f'{__class__.__name__}({self.iterable})'

    def __len__(self):
        return len(self.iterable)

    def __reversed__(self):
        raise NotImplementedError

    def __iter__(self):
        yield from self.iterable

    def __getitem__(self, index):
        return self.iterable[index]

    def __setitem__(self, index, item):
        raise NotImplementedError

    def __delitem__(self, index):
        del self.iterable[index]

    def __add__(self, other):
        if isinstance(other, __class__):
            tmp_list = [self.iterable, other]
            self = sorted([i for lst in tmp_list for i in lst])
            return __class__(self)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, __class__):
            self.__add_list(self, other)
            return self
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, int):
            self.iterable = sorted(self.iterable * n)
            return self
        return NotImplemented

    def __imul__(self, n):
        if isinstance(n, int):
            self.iterable = sorted(self.iterable * n)
            return self
        return NotImplemented
```
* Второй вариант решения

```python
from collections.abc import Sequence
class SortedList(Sequence):
    def __init__(self, iterable=()):
        self.iterable = sorted(iterable)

    def __getitem__(self, index):
        return self.iterable[index]

    def __setitem__(self, index, value):
        raise NotImplementedError

    def __reversed__(self):
        raise NotImplementedError

    def append(self, other):
        raise NotImplementedError

    def insert(self, index, other):
        raise NotImplementedError

    def extend(self, other):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def __delitem__(self, key):
        del self.iterable[key]

    def __len__(self):
        return len(self.iterable)

    def add(self, other):
        self.iterable.append(other)

    def discard(self, other):
        self.iterable = list(filter(lambda x: x != other, self.iterable))

    def update(self, other):
        self.iterable.extend(other)
        self.iterable = sorted(self.iterable)

    def __add__(self, other):
        if isinstance(other, type(self)):
            return SortedList(self.iterable + other.iterable)
        return NotImplemented

    def __iadd__(self, other):
        if not isinstance(other, SortedList):
            return NotImplemented
        self.iterable += other.iterable
        self.iterable.sort()
        return self

    def __mul__(self, n):
        if isinstance(n, int):
            return SortedList(sorted(self.iterable * n))
        return NotImplemented

    def __imul__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        self.iterable = self.iterable * n
        self.iterable.sort()
        return self

    def __str__(self):
        return f"SortedList({sorted(self.iterable)})"
```


