<h2 style="text-align:center">Класс Rectangle</h2>

### Реализуйте класс Queue, описывающий очередь, элементами которой являются пары ключ: значение. При создании экземпляра класс должен принимать один аргумент:

* pairs — список или словарь, определяющий начальный набор элементов очереди. Порядок элементов в очереди должен совпадать с их порядком в переданном итерируемом объекте. Если не передан, очередь считается пустой
#### Класс Queue должен иметь два метода экземпляра:

* add() — метод, принимающий в качестве аргумента элемент и добавляющий его в конец очереди. Элементом в данном случае является двухэлементный кортеж, содержащий ключ и значение. Если в очереди уже содержится элемент с указанным ключом, он должен быть перенесен в конец очереди, а его значение должно быть обновлено
* pop() — метод, удаляющий из очереди первый элемент и возвращающий его. Элементом в данном случае является двухэлементный кортеж, содержащий ключ и значение. Если очередь пуста, должно быть возбуждено исключение KeyError с текстом:
> Очередь пуста
#### Экземпляр класса Queue должен иметь следующее формальное строковое представление:

> Queue([(<ключ 1-го элемента>, <значение 1-го элемента>), (<ключ 2-го элемента>, <значение 2-го элемента>), ...])
#### При передаче экземпляра класса Queue в функцию len() должно возвращаться количество элементов в нем.

##### Примечание 1. Вероятно, при решении задачи будет удобно воспользоваться одним из классов из модуля collections.

##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

##### Примечание 3. Никаких ограничений касательно реализации класса Queue нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
      <th>Sample Input 5: </th>
    </tr>
    <tr>
      <td align="center">queue = Queue()<br>
                          queue.add(('one', 1))<br>
                          queue.add(('two', 2))<br>
                          print(queue)<br></td>
      <td align="center">queue = Queue([('one', 1)])<br>
                          queue.add(('two', 2))<br>
                          print(queue.pop())<br>
                          print(queue.pop())<br>
                          print(queue)<br></td>
      <td align="center">queue = Queue({'one': 1, 'two': 2})<br>
                        print(len(queue))<br>
                        queue.add(('three', 1))<br>
                        print(len(queue))<br></td>
      <td align="center">queue = Queue()<br>
                          queue.add(('one', 1))<br>
                          queue.add(('two', 2))<br>
                          print(queue)<br>
                          queue.add(('one', 10))<br>
                          print(queue)<br></td>
      <td align="center">queue = Queue()<br>
                          try:<br>
                              queue.pop()<br>
                          except KeyError as error:<br>
                              print(error)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      <td>Sample Output 5:</td>
      </tr>
    <tr>
      <td align="center">
                        Queue([('one', 1), ('two', 2)])<br>
      </td>
      <td align="center">
                        ('one', 1)<br>
                        ('two', 2)<br>
                        Queue([])<br>
      </td>
      <td align="center">
                        2<br>
                        3<br>
      </td>
      <td align="center">
                        Queue([('one', 1), ('two', 2)])<br>
                        Queue([('two', 2), ('one', 10)])<br>
      </td>
      <td align="center">
                        'Очередь пуста'<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Queue:
    def __init__(self, pairs=[]):
        if isinstance(pairs, dict):
            self.pairs = [(k, v) for k, v in pairs.items()]
        else:
            self.pairs = pairs[:]

    def add(self, item):
        for i, k in enumerate(self.pairs):
            if item[0] == k[0]:
                del self.pairs[i]
        self.pairs.append(item)

    def pop(self):
        if self.pairs:
            return self.pairs.pop(0)
        raise KeyError('Очередь пуста')

    def __repr__(self):
        return f'{__class__.__name__}({self.pairs})'

    def __len__(self):
        return len(self.pairs)
```
* Второй вариант решения

```python
class Queue(dict):
    def add(self, elem):
        key, value = elem 
        if key in self:
            del self[key]
        self[key] = value
        
    def pop(self):
        if not self:
            raise KeyError('Очередь пуста')
        key, value = tuple(self.items())[0]
        del self[key]
        return key, value
        
    def __repr__(self):
        return f'{type(self).__name__}({list(self.items())})'
```


