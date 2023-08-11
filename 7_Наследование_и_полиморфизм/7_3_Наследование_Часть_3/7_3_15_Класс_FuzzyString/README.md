<h2 style="text-align:center">Класс FuzzyString</h2>

### Реализуйте класс FuzzyString, наследника класса str, описывающий строку, которая при любых сравнениях (==, !=, >, <, >=, <=) и проверках на принадлежность (in, not in) не учитывает регистр. Процесс создания экземпляра класса FuzzyString должен совпадать с процессом создания экземпляра класса str.

##### Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса FuzzyString нет, она может быть произвольной.
<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">s1 = FuzzyString('BeeGeek')<br>
                                s2 = FuzzyString('beegeek')<br>
                                print(s1 == s2)<br>
                                print(s1 in s2)<br>
                                print(s2 in s1)<br>
                                print(s2 not in s1)<br>
                                print(s2 not in s1)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                       True<br>
                        True<br>
                        True<br>
                        False<br>
                        False<br>
                              </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class FuzzyString(str):
    def __new__(cls, obj=''):
        obj = super().__new__(cls, str(obj).lower())
        return obj

    def __eq__(self, other):
        if isinstance(other, (str)):
            return len(self) == len(other)
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, (str)):
            return len(self) != len(other)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, (str)):
            return len(self) < len(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, (str)):
            return len(self) > len(other)
        return NotImplemented

    def __contains__(self, other):
        return self in other.lower()

    def __le__(self, other):
        if isinstance(other, str):
            return self.__lt__(other) or self.__eq__(other)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, str):
            return not self.__lt__(other)
        return NotImplemented
```
* Второй вариант решения

```python
from functools import total_ordering

@total_ordering
class FuzzyString(str):
    
    def __le__(self, other):
        if isinstance(other, str):
            return self.lower() <= other.lower()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, str):
            return self.lower() == other.lower()
        return NotImplemented

    def __contains__(self, substring):
        if isinstance(substring, str):
            return substring.lower() in self.lower()
        return NotImplemented
    
    __lt__ = getattr(object, '__lt__', None)
    __gt__ = getattr(object, '__gt__', None)
    __ge__ = getattr(object, '__ge__', None)
    __ne__ = getattr(object, '__ne__', None)
```


