<h2 style="text-align:center">Класс SequenceZip</h2>


### Реализуйте класс SequenceZip. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является итерируемым объектом. Класс SequenceZip должен описывать последовательность, элементами которой являются элементы переданных в конструктор итерируемых объектов, объединенные в кортежи. Объединение должно происходить аналогично тому, как это делает функция zip().
#### При передаче экземпляра класса SequenceZip в функцию len() должно возвращаться количество элементов в нем.
#### Также экземпляр класса SequenceZip должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.
#### Наконец, экземпляр класса SequenceZip должен позволять получать значения своих элементов с помощью индексов.
##### Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.
##### Примечание 2. Экземпляр класса SequenceZip не должен зависеть от итерируемых объектов, на основе которых он был создан. Другими словами, если исходные итерируемые объекты изменятся, то экземпляр класса SequenceZip измениться  не должен.
##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 4. Никаких ограничений касательно реализации класса SequenceZip нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])<br>
                        print(list(sequencezip))<br>
                        print(tuple(sequencezip))<br></td>
      <td align="center">sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])<br>
                        print(len(sequencezip))<br>
                        print(sequencezip[1])<br>
                        print(sequencezip[2])<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        [('A', 'bee', 1), ('B', 'geek', 2), ('C', 'python', 3)]<br>
                          (('A', 'bee', 1), ('B', 'geek', 2), ('C', 'python', 3))<br>
      </td>
      <td align="center">
                        3
                        ('B', 'geek', 2)<br>
                        ('C', 'python', 3)<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from copy import deepcopy



class SequenceZip:
    def __init__(self, *args):
        self.args = deepcopy(args)
        
    def __len__(self):
        return len(list((zip(*self.args))))
    
    def __iter__(self):
        yield from zip(*self.args)

    def __next__(self):
        yield zip(*self.args)

    def __getitem__(self, key):
        self.__lst = zip(*self.args)
        for i in range(key+1):
            if i == key:
                return next(self.__lst)
            next(self.__lst)
```
* Второй вариант решения

```python
import copy


class SequenceZip:
    def __init__(self, *sequences):
        self.sequences = copy.deepcopy(sequences)

    def __len__(self):
        return min((len(s) for s in self.sequences), default=0)

    def __getitem__(self, index):
        count = -1
        for item in self:
            count += 1
            if count == index:
                return item

    def __iter__(self):
        yield from zip(*self.sequences)
```


