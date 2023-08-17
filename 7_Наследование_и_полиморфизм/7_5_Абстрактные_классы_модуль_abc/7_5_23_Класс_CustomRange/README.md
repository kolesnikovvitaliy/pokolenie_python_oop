<h2 style="text-align:center">Класс CustomRange</h2>

### Назовем диапазоном запись двух целых неотрицательных чисел через дефис a-b, где a — левая граница диапазона, b — правая граница диапазона, причем a <= b. Диапазон содержит в себе все числа от a до b включительно. Например, диапазон 1-4 содержит числа 1, 2, 3 и 4.
### Реализуйте класс CustomRange, описывающий последовательность, элементами которой являются одиночные целые числа и числа из определенных диапазонов. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является одиночным целым числом либо диапазоном.
#### При передаче экземпляра класса CustomRange в функцию len() должно возвращаться количество элементов в нем. При передаче экземпляра класса CustomRange в функцию reversed() должен возвращаться итератор, элементами которого являются элементы переданного экземпляра класса CustomRange, расположенные в обратном порядке.
#### Экземпляр класса CustomRange должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.
#### Помимо этого, экземпляр класса CustomRange должен поддерживать операцию проверки на принадлежность с помощью оператора in.
#### Наконец, экземпляр класса CustomRange должен позволять получать значения своих элементов с помощью индексов, причем как как положительных, так и отрицательных

##### Примечание 1. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве родительского.
##### Примечание 2. Реализация класса CustomRange может быть произвольной, то есть требований к наличию определенных атрибутов нет.
##### Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">customrange = CustomRange(1, '2-5', 5, '6-8')<br>
                          print(customrange[0])<br>
                          print(customrange[1])<br>
                          print(customrange[2])<br>
                          print(customrange[-1])<br>
                          print(customrange[-2])<br>
                          print(customrange[-3])<br></td>
      <td align="center">customrange = CustomRange(1, '2-5', 3, '1-4')<br>
                          print(*customrange)<br>
                          print(*reversed(customrange))<br>
                          print(len(customrange))<br>
                          print(1 in customrange)<br>
                          print(10 in customrange)<br></td>
      <td align="center">customrange = CustomRange()<br>
                          print(len(customrange))<br>
                          print(*customrange)<br>
                          print(*reversed(customrange))<br></td>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        1<br>
                        2<br>
                        3<br>
                        8<br>
                        7<br>
                        6<br>
      </td>
      <td align="center">
                        1 2 3 4 5 3 1 2 3 4<br>
                        4 3 2 1 3 5 4 3 2 1<br>
                        10<br>
                        True<br>
                        False<br>
      </td>
      <td align="center">
                        0<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self.args = self.set_items(args)

    def set_items(self, args):
        __result = []
        for i in args:
            if isinstance(i, str):
                __tmp = [int(j) for j in i.split('-')]
                __tmp[1] += 1
                __tmp = range(*__tmp)
                __result.extend([j for j in __tmp])
            else:
                __result.append(i)
        return __result

    def __getitem__(self, index):
        return self.args[index]

    def __len__(self):
        return len(self.args)
```
* Второй вариант решения

```python
from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self._data = []
        for arg in args:
            start, stop = (arg, arg) if isinstance(arg, int) else map(int, arg.split('-'))
            self._data.extend(range(start, stop + 1))

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._data[item]
        return NotImplemented

    def __len__(self):
        return len(self._data)
```


