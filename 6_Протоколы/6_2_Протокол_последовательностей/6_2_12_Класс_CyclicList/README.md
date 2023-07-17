<h2 style="text-align:center">Класс CyclicList</h2>

### Реализуйте класс CyclicList, описывающий циклический список. При создании экземпляра класс должен принимать один аргумент:
* iterable — итерируемый объект, определяющий начальный набор элементов циклического списка. Если не передан, начальный набор элементов считается пустым
#### Класс CyclicList должен иметь два метода экземпляра:
* append() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в конец циклического списка
* pop() — метод, который принимает в качестве аргумента индекс элемента циклического списка, возвращает его значение и удаляет из циклического списка элемент с данным индексом. Если аргумент не передан, возвращаемым и удаляемым элементом считается последний элемент циклического списка 
#### При передаче экземпляра класса CyclicList в функцию len() должно возвращаться количество элементов в нем.
#### Также экземпляр класса CyclicList должен быть зацикленным итерируемым объектом. Другими словами, итерация по нему должна происходить бесконечно, и при каждом достижении его последнего элемента она должна начинаться сначала.
#### Наконец, экземпляр класса CyclicList должен позволять получать значения своих элементов с помощью индексов, при этом индексы должны работать циклически. Например, в циклическом списке [1, 2, 3] элементом с индексом 4 должно являться число 2.

##### Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.
##### Примечание 2. Экземпляр класса CyclicList не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса CyclicList измениться  не должен.
##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 4. Никаких ограничений касательно реализации класса CyclicList нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">cyclic_list = CyclicList([1, 2, 3])<br>
                          for index, elem in enumerate(cyclic_list):<br>
                              if index > 6:<br>
                                  break<br>
                              print(elem, end=' ')<br></td>
      <td align="center">cyclic_list = CyclicList([1, 2, 3])<br>
                          cyclic_list.append(4)<br>
                          print(cyclic_list.pop())<br>
                          print(len(cyclic_list))<br>
                          print(cyclic_list.pop(0))<br>
                          print(len(cyclic_list))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        1 2 3 1 2 3 1<br>
      </td>
      <td align="center">
                        4<br>
3<br>
1<br>
2<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class CyclicList:
    def __init__(self, iterable):
        self.iterable = iterable.copy()
        
    def append(self, obj):
        self.iterable.append(obj)

    def pop(self, index=None):
        if index is None:
            return self.iterable.pop()
        return self.iterable.pop(index)

    def __len__(self):
        return len(self.iterable)

    def __iter__(self):
        for _ in self.iterable:
            yield from self.iterable
            
    def __getitem__(self, key):
        if len(self.iterable) < key:
            key = key % len(self.iterable)
            return self.iterable[key]
        return self.iterable[key]
```
* Второй вариант решения

```python
from itertools import cycle


class CyclicList:
    def __init__(self, iterable=()):
        self._data = list(iterable) or []

    def append(self, item):
        self._data.append(item)

    def pop(self, index=None):
        if index is None:
            return self._data.pop()
        return self._data.pop(index)

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        yield from cycle(self._data)

    def __getitem__(self, index):
        return self._data[index % len(self._data)]
```


