<h2 style="text-align:center">Класс Queue</h2>

### Очередь — абстрактный тип данных с дисциплиной доступа к элементам "первый пришёл — первый вышел". Добавление элемента возможно лишь в конец очереди, выборка — только из начала очереди, при этом выбранный элемент из очереди удаляется.
### Реализуйте класс Queue, описывающий очередь. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является элементом очереди. Порядок следования аргументов образует порядок элементов в очереди, то есть первый аргумент — первый элемент очереди, второй аргумент — второй элемент очереди, и так далее.
#### Класс Queue должен иметь два метода экземпляра:
* add() — метод, принимающий произвольное количество позиционных аргументов и добавляющий их в конец очереди в том порядке, в котором они были переданы
* pop() — метод, удаляющий из очереди первый элемент и возвращающий его. Если очередь пуста, метод должен вернуть значение None
#### Экземпляр класса Queue должен иметь следующее неформальное строковое представление:
> <первый элемент очереди> -> <второй элемент очереди> -> <третий элемент очереди> -> ...
#### Помимо этого, экземпляры класса Queue должны поддерживать между собой операции сравнения с помощью операторов == и!=. Две очереди считаются равными, если они имеют равную длину и содержат равные элементы на равных позициях.
#### Также экземпляры класса Queue должны поддерживать между собой операцию сложения с помощью операторов + и +=:
* результатом сложения с помощью оператора + должен являться новый экземпляр класса Queue, представляющий очередь со всеми элементами исходных очередей: сначала все элементы левой очереди, затем все элементы правой очереди
* результатом сложения с помощью оператора += должен являться левый экземпляр класса Queue, представляющий очередь, к которой добавлены все элементы правой очереди

#### Наконец, экземпляр класса Queue должен поддерживать операцию побитового сдвига вправо на целое число n с помощью оператора >>, результатом которой должен являться новый экземпляр класса Queue, представляющий исходную очередь без первых n элементов. Если n больше или равно длине исходной очереди, результатом должен являться экземпляр класса Queue, представляющий пустую очередь.
##### Примечание 1. Если объект, с которым выполняется операция сравнения или арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
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
      <td align="center">queue = Queue(1, 2)<br>
                          queue.add(3)<br>
                          queue.add(4, 5)<br>
                          print(queue)<br>
                          print(queue.pop())<br>
                          print(queue)<br></td>
      <td align="center">queue1 = Queue(1, 2, 3)<br>
                          queue2 = Queue(1, 2)<br>
                          print(queue1 == queue2)<br>
                          queue2.add(3)<br>
                          print(queue1 == queue2)<br></td>
      <td align="center">queue1 = Queue(1, 2, 3)<br>
                          queue2 = Queue(4, 5)<br>
                          print(queue1 + queue2)<br></td>
      <td align="center">queue1 = Queue(1, 2, 3)<br>
                          queue2 = Queue(4, 5)<br>
                          queue1 += queue2<br>
                          print(queue1)<br></td>
      <td align="center">queue = Queue(1, 2, 3, 4, 5)<br>
                          print(queue >> 3)<br></td>
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
                        1 -> 2 -> 3 -> 4 -> 5<br>
                        1<br>
                        2 -> 3 -> 4 -> 5<br>
      </td>
      <td align="center">
                        False<br>
                        True<br>
      </td>
      <td align="center">
                        1 -> 2 -> 3 -> 4 -> 5<br>
      </td>
      <td align="center">
                        1 -> 2 -> 3 -> 4 -> 5<br>
      </td>
      <td align="center">
                        4 -> 5<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Queue:
    def __init__(self, *args):
        self.arg = [*args]

    def add(self, *args):
        self.arg.extend(args)

    def pop(self):
        if self.arg:
            return self.arg.pop(0)
        return None

    def __add__(self, other):
        if isinstance(other, __class__):
            return __class__(*(self.arg + other.arg))
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, __class__):
            self.arg += other.arg
            return self
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, __class__):
            return len(self.arg) == len(other.arg) and self.arg == other.arg
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, __class__):
            return len(self.arg) != len(other.arg) and self.arg != other.arg
        return NotImplemented

    def __rshift__(self, n):
        if isinstance(n, int):
            return __class__(*self.arg[n:])
        return NotImplemented

    def __str__(self) -> str:
        return f"{' -> '.join(map(str, self.arg))}"
```
* Второй вариант решения

```python
class Queue:
    def __init__(self, *args):
        self.queue = [*args]

    def add(self, *args):
        self.queue.extend(args)

    def pop(self):
        return self.queue.pop(0) if self.queue else None

    def __str__(self):
        return ' -> '.join(map(str, self.queue))

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.queue == other.queue
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Queue):
            return Queue(*(self.queue + other.queue))
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.add(*other.queue)
            return self
        return NotImplemented

    def __rshift__(self, n):
        if isinstance(n, int):
            return Queue(*self.queue[n:])
        return NotImplemented
```


