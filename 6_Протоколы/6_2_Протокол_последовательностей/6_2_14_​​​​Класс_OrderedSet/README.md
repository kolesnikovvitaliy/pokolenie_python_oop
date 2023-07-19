<h2 style="text-align:center">​​​​​Класс OrderedSet</h2>


### Реализуйте класс OrderedSet, описывающий упорядоченное множество. При создании экземпляра класс должен принимать один аргумент:
* iterable — итерируемый объект, определяющий начальный набор элементов упорядоченного множества. Если не передан, начальный набор элементов считается пустым
#### Класс OrderedSet должен иметь два метода экземпляра:
* add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в конец упорядоченного множества
* discard() — метод, принимающий в качестве аргумента произвольный объект и удаляющий его из упорядоченного множества, если он в нем присутствует
#### При передаче экземпляра класса OrderedSet в функцию len() должно возвращаться количество элементов в нем.
#### Помимо этого, экземпляр класса OrderedSet должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.
#### Также экземпляр класса OrderedSet должен поддерживать операцию проверки на принадлежность с помощью оператора in.
#### Наконец, экземпляры класса OrderedSet должны поддерживать операции сравнения с помощью операторов == и !=. Методы, реализующие операции сравнения, должны уметь сравнивать как два экземпляра класса OrderedSet между собой, так и экземпляр класса OrderedSet с экземпляром класса set. Если упорядоченное множество сравнивается с упорядоченным множеством, они считаются равными в том случае, если они имеют равную длину и содержат равные элементы на равных позициях. Если упорядоченное множество сравнивается с обычным множеством, они считаются равными в том случае, если имеют равную длину и содержат равные элементы без учета их расположения.
##### Примечание 1. Экземпляр класса OrderedSet не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса OrderedSet измениться  не должен.
##### Примечание 2. Если объект, с которыми происходит сравнение, некорректен, метод, реализующий операцию сравнения, должен вернуть константу NotImplemented.
##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 4. Никаких ограничений касательно реализации класса OrderedSet нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])<br>
                          print(*orderedset)<br>
                          print(len(orderedset))<br>
<br></td>
      <td align="center">orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])<br>
                          print('python' in orderedset)<br>
                          print('C++' in orderedset)<br></td>
      <td align="center">orderedset = OrderedSet()<br>
                          orderedset.add('green')<br>
                          orderedset.add('green')<br>
                          orderedset.add('blue')<br>
                          orderedset.add('red')<br>
                          print(*orderedset)<br>
                          orderedset.discard('blue')<br>
                          orderedset.discard('white')<br>
                          print(*orderedset)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        bee python stepik geek<br>
                        4<br>
      </td>
      <td align="center">
                        True<br>
                        False<br>
      </td>
      <td align="center">
                        green blue red<br>
                        green red<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class OrderedSet:
    def __init__(self, iterable=None):
        if iterable:
            self.iterable = {k: None for k in iterable.copy()} 
        else:
            self.iterable = dict() 

    def add(self, __value):
        self.iterable[__value] = None

    def discard(self, __value):
        if __value in self.iterable:
            del self.iterable[__value]
        return self.iterable
        
    
    def __len__(self):
        return len(self.iterable)

    def __iter__(self):
        yield from self.iterable

    def __contains__(self, item):
        return item in self.iterable

    def __eq__(self, __value: object):
        if isinstance(__value, __class__):
            if len(self.iterable) == len(__value.iterable):
                if False in (map(lambda x, y: x == y, self.iterable, __value.iterable)):
                    return False
                return True
        elif isinstance(__value, set):
            if len(self.iterable) == len(__value):
                if not set(self.iterable).isdisjoint(__value):
                    return True
            return False
        else:
            return NotImplemented
```
* Второй вариант решения

```python
class OrderedSet:
    def __init__(self, iterable=()):
        self._data = dict.fromkeys(iterable, None)

    def __len__(self):
        return len(self._data)

    def add(self, item):
        self._data.setdefault(item, None)

    def discard(self, item):
        self._data.pop(item, None)

    def __iter__(self):
        yield from self._data

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self._data) == len(other._data) and all(x == y for x, y in zip(self._data, other._data))
        if isinstance(other, set):
            return set(self._data) == other
        return NotImplemented
```


