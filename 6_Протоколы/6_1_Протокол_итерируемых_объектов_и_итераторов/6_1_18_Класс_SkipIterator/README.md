<h2 style="text-align:center">Класс SkipIterator</h2>

### Реализуйте класс SkipIterator. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* iterable — итерируемый объект
* n — целое неотрицательное число
#### Экземпляр класса SkipIterator должен являться итератором, который генерирует элементы итерируемого объекта iterable, пропуская по n элементов, а затем возбуждает исключение StopIteration.

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Класс SkipIterator должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)   # пропускаем по одному элементу<br>
print(*skipiterator)<br></td>
      <td align="center">skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)   # пропускаем по два элемента<br>
print(*skipiterator)<br></td>
      <td align="center">skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)   # не пропускаем элементы<br>
print(*skipiterator)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        1 3 5 7 9<br>
      </td>
      <td align="center">
                        1 4 7 10<br>
      </td>
      <td align="center">
                        1 2 3 4 5 6 7 8 9 10<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class SkipIterator:
    def __init__(self, iterable, n) -> None:
        self.iterable = list(iterable)
        self.n = n
        self.__i = 0

    def __iter__(self):
        return self

    def __next__(self):
        __lst = self.iterable[0::self.n+1]
        if self.__i >= len(__lst):
            raise StopIteration
        self.__i += 1
        return __lst[self.__i-1]
```
* Второй вариант решения

```python
class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = iter(iterable)
        self.n = n
        self.first = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.first:
            self.first = False
            return next(self.iterable)
        for _ in range(self.n):
            next(self.iterable)
        return next(self.iterable)
```


