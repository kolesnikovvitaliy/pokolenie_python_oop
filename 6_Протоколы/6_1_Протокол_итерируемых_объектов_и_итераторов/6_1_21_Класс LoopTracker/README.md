<h2 style="text-align:center">Класс LoopTracker</h2>


### Реализуйте класс LoopTracker. При создании экземпляра класс должен принимать один аргумент:
* iterable — итерируемый объект
  
### Экземпляр класса LoopTracker должен являться итератором, который генерирует элементы итерируемого объекта iterable в исходном порядке, а затем возбуждает исключение StopIteration.
#### Класс LoopTracker должен иметь четыре свойства:
* accesses — свойство, доступное только для чтения, возвращающее количество элементов, сгенерированных итератором на данный момент
empty_accesses — свойство, доступное только для чтения, возвращающее количество попыток получить следующий элемент опустевшего итератора
*first — свойство, доступное только для чтения, возвращающее первый элемент итератора и не сдвигающее его. Если итератор не имеет первого элемента, то есть создан на основе пустого итерируемого объекта, то должно быть возбуждено исключение AttributeError с текстом:
> Исходный итерируемый объект пуст

* last — свойство, доступное только для чтения, возвращающее последний элемент, сгенерированный итератором на данный момент. Если итератор еще не сгенерировал ни одного элемента, то должно быть возбуждено исключение AttributeError с текстом:
>  Последнего элемента нет

#### Класс LoopTracker должен иметь один метод экземпляра:
* is_empty() — метод, возвращающий True, если итератор опустошен, или False в противном случае

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

##### Примечание 2. Класс LoopTracker должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">loop_tracker = LoopTracker([1, 2, 3])<br>
                        print(next(loop_tracker))<br>
                        print(list(loop_tracker))<br></td>
      <td align="center">loop_tracker = LoopTracker([1, 2, 3])<br>
                          print(loop_tracker.accesses)<br>
                          next(loop_tracker)<br>
                          next(loop_tracker)<br>
                          print(loop_tracker.accesses)<br></td>
      <td align="center">loop_tracker = LoopTracker([1, 2, 3])<br>
                        print(loop_tracker.first)<br>
                        print(next(loop_tracker))<br>
                        print(loop_tracker.first)<br>
                        print(next(loop_tracker))<br>
                        print(loop_tracker.first)<br>
                        print(next(loop_tracker))<br>
                        print(loop_tracker.first)<br></td>
      <td align="center">loop_tracker = LoopTracker([1, 2, 3])<br>
                          print(next(loop_tracker))<br>
                          print(loop_tracker.last)<br>
                          print(next(loop_tracker))<br>
                          print(loop_tracker.last)<br>
                          print(next(loop_tracker))<br>
                          print(loop_tracker.last)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        1<br>
                        [2, 3]<br>
      </td>
      <td align="center">
                        0<br>
                        2<br>
      </td>
      <td align="center">
                        1<br>
                        1<br>
                        1<br>
                        2<br>
                        1<br>
                        3<br>
                        1<br>
      </td>
      <td align="center">
                        1<br>
                        1<br>
                        2<br>
                        2<br>
                        3<br>
                        3<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class LoopTracker:
    def __init__(self, iterables):
        self.iterable = list(iterables)
        self.__i = 0
        self.__j = 0

    @property
    def accesses(self):
        return self.__i - self.__j
    
    @property
    def empty_accesses(self):
        return self.__j
    
    @property
    def first(self):
        if len(self.iterable) == 0:
            raise AttributeError('Исходный итерируемый объект пуст')
        return self.iterable[0]
    
    @property
    def last(self):
        if self.__i == 0:
            raise AttributeError('Последнего элемента нет')
        else:
            return self.iterable[self.__i-1]
        
    
    def is_empty(self):
        if self.__i >= len(self.iterable):
            return True
        return False

    def __iter__(self):
        return self
    
    def __next__(self):
        self.__i += 1
        if self.__i >= len(self.iterable)+1:
            self.__j += 1
            raise StopIteration
        return self.iterable[self.__i-1]
```
* Второй вариант решения

```python
class LoopTracker:
    def __init__(self, iterable):
        self._iterable = iter(iterable)
        self._empty_accesses = self._accesses = 0
        self._is_empty = False
        try:
            self._nextvalue = self._first = next(self._iterable)
        except StopIteration:
            self._is_empty = True
        
    def __iter__(self):
        return self

    def __next__(self):
        if self._is_empty:
            self._empty_accesses += 1
            raise StopIteration
        self._curvalue = self._nextvalue
        self._accesses += 1
        try:
            self._nextvalue = next(self._iterable)
        except StopIteration:
            self._is_empty = True
        return self._curvalue

    @property
    def accesses(self):
        return self._accesses

    @property
    def empty_accesses(self):
        return self._empty_accesses

    @property
    def first(self):
        if hasattr(self, '_first'):
            return self._first
        raise AttributeError('Исходный итерируемый объект пуст')

    @property
    def last(self):
        if hasattr(self, '_curvalue'):
            return self._curvalue
        raise AttributeError('Последнего элемента нет')

    def is_empty(self):
        return self._is_empty
```


