<h2 style="text-align:center">Класс RandomNumber</h2>

### Реализуйте класс RandomNumber, описывающий дескриптор, который при обращении к атрибуту возвращает случайное целое число в заданном диапазоне. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
* start — целое число
* end — целое число
* cache — булево значение, по умолчанию равняется False
#### Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.
#### При обращении к атрибуту дескриптор должен возвращать случайное целое число от start до end включительно. Если в качестве значения параметра cache при создании дескриптора было указано значение True, при каждом обращении к атрибуту дескриптор должен возвращать то число, которое было сгенерировано при первом обращении.
#### При установке или изменении значения атрибута дескриптор должен возбуждать исключение AttributeError с текстом:
> Изменение невозможно

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса RandomNumber нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">class MagicPoint:<br>
                              x = RandomNumber(1, 5)<br>
                              y = RandomNumber(1, 5)<br>
                              z = RandomNumber(1, 5)<br>
                          magicpoint = MagicPoint()<br>
                          print(magicpoint.x in [1, 2, 3, 4, 5])<br>
                          print(magicpoint.y in [1, 2, 3, 4, 5])<br>
                          print(magicpoint.z in [1, 2, 3, 4, 5])<br></td>
      <td align="center">class MagicPoint:<br>
                              x = RandomNumber(1, 5)<br>
                              y = RandomNumber(1, 5)<br>
                              z = RandomNumber(1, 5)<br>
                          magicpoint = MagicPoint()<br>
                          print(magicpoint.x in [6, 7, 8, 9, 10])<br>
                          print(magicpoint.y in [6, 7, 8, 9, 10])<br>
                          print(magicpoint.z in [6, 7, 8, 9, 10])<br></td>
      <td align="center">class MagicPoint:<br>
                              x = RandomNumber(0, 5, True)<br>
                              y = RandomNumber(0, 5)<br>
                              z = RandomNumber(0, 5)<br>
                          magicpoint = MagicPoint()<br>
                          value = magicpoint.x<br>
                          print(magicpoint.x == value)<br>
                          print(magicpoint.x == value)<br>
                          print(magicpoint.x == value)<br></td>
      <td align="center">class MagicPoint:<br>
                              x = RandomNumber(0, 5)<br>
                              y = RandomNumber(0, 5)<br>
                              z = RandomNumber(0, 5)<br>
                          magicpoint = MagicPoint()<br>
                          try:<br>
                              magicpoint.x = 10<br>
                          except AttributeError as e:<br>
                              print(e)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
                        True<br>
                        True<br>
      </td>
      <td align="center">
                        False<br>
                        False<br>
                        False<br>
      </td>
      <td align="center">
                        True<br>
                        True<br>
                        True<br>
      </td>
      <td align="center">
                        Изменение невозможно<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from random import randint


class RandomNumber:
    _lst: dict = {}

    def __init__(self, start: int, end: int, cache=False):
        self._start = start
        self._end = end
        self._cache = cache
        self._random_int = randint(self._start, self._end)

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if self._cache:
            obj.__dict__.setdefault(self._attr, set()).add(self._random_int)
            return obj.__dict__[self._attr]
        else:
            return self._random_int

    def __set__(self, obj, value):
        raise AttributeError('Изменение невозможно')
```
* Второй вариант решения

```python
from random import randint

class RandomNumber:
    def __init__(self, start, end, cache=False):
        self.start = start
        self.end = end
        self.cache = cache
        self.permanent = randint(self.start, self.end)

    def __set_name__(self, owner, attr):
        self._attr = attr

    def __set__(self, obj, value):
        raise AttributeError('Изменение невозможно')

    def __get__(self, obj, owner):
        if obj is None:
            return self
        if not self.cache:
            return randint(self.start, self.end)
        return self.permanent
```


