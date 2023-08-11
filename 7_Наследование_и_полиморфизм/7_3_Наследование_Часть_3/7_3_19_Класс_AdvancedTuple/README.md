<h2 style="text-align:center">Класс AdvancedTuple</h2>

### Реализуйте класс AdvancedTuple, наследника класса tuple, который описывает кортеж, умеющий выполнять операцию сложения (+, +=) не только с экземплярами классов AdvancedTuple и tuple, но и с любыми итерируемыми объектами. Процесс создания экземпляра класса AdvancedTuple должен совпадать с процессом создания экземпляра класса tuple.

##### Примечание 1. Как бы ни выполнялось сложение, с помощью оператора + или +=, результатом операции должен являться новый экземпляр класса AdvancedTuple.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса AdvancedTuple нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">advancedtuple = AdvancedTuple([1, 2, 3])<br>
                        print(advancedtuple + (4, 5))<br>
                        print(advancedtuple + [4, 5])<br>
                        print({'a': 1, 'b': 2} + advancedtuple)<br></td>
      <td align="center">advancedtuple = AdvancedTuple([1, 2, 3])<br>
                        advancedtuple += [4, 5]<br>
                        advancedtuple += iter([6, 7, 8])<br>
                        print(advancedtuple)<br>
                        print(type(advancedtuple))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        (1, 2, 3, 4, 5)<br>
                        (1, 2, 3, 4, 5)<br>
                        ('a', 'b', 1, 2, 3)<br>
      </td>
      <td align="center">
                        (1, 2, 3, 4, 5, 6, 7, 8)<br>
                        class '__main__.AdvancedTuple'<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class AdvancedTuple(tuple):
    def __add__(self, other):
        return __class__((tuple(self) + tuple(other)))

    def __iadd__(self, other):
        return __class__((tuple(self) + tuple(other)))

    def __radd__(self, other):
        return __class__(tuple(other) + tuple(self))
```
* Второй вариант решения

```python
class AdvancedTuple(tuple):
    def __add__(self, other):
        if hasattr(other, '__iter__'):
            return AdvancedTuple(super().__add__(tuple(other)))

    def __radd__(self, other):
        return tuple(other).__add__(self)
```


