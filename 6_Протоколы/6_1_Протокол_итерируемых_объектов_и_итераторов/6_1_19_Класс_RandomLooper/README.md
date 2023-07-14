<h2 style="text-align:center">Класс RandomLooper</h2>


### Реализуйте класс RandomLooper. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является итерируемым объектом.

#### Экземпляр класса RandomLooper должен являться итератором, который генерирует в случайном порядке все элементы всех итерируемых объектов, переданных в конструктор, а затем возбуждает исключение StopIteration.

##### Примечание 1. Порядок элементов в возвращаемом итераторе необязательно должен совпадать с их порядком в тестовых данных.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Класс RandomLooper должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])<br>
                          print(list(randomlooper))<br>
                          print(list(randomlooper))<br></td>
      <td align="center">colors = ['red', 'blue', 'green', 'purple']<br>
                        shapes = ['square', 'circle', 'triangle', 'octagon']<br>
                        randomlooper = RandomLooper(colors, shapes)<br>
                        print(list(randomlooper))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        ['green', 'red', 'blue', 'purple']<br>
                        []<br>
      </td>
      <td align="center">
                        ['circle', 'red', 'purple', 'octagon', 'triangle', 'green', 'blue', 'square']<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class RandomLooper:
    def __init__(self, *args):
        self.__lst = iter([j for i in args for j in i])

    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.__lst)
```
* Второй вариант решения

```python
import itertools as it
import random


class RandomLooper:
    def __init__(self, *args):
        self.iterables = list(it.chain(*args))
        self.length = len(self.iterables)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.length:
            raise StopIteration
        self.length -= 1
        ind = random.randint(0, self.length)
        return self.iterables.pop(ind)
```


