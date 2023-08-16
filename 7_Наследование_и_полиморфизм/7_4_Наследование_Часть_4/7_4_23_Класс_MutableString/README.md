<h2 style="text-align:center">Класс MutableString</h2>

### Реализуйте класс MutableString, наследника класса UserString, описывающий изменяемую строку. Процесс создания экземпляра класса MutableString должен совпадать с процессом создания экземпляра класса UserString.
#### Класс MutableString должен иметь три метода экземпляра:
* lower() — метод, переводящий все символы изменяемой строки в нижний регистр
* upper() — метод, переводящий все символы изменяемой строки в верхний регистр
* sort() — метод, сортирующий символы изменяемой строки. Может принимать два необязательных именованных аргумента key и reverse, выполняющих ту же задачу, что и в функции sorted()

#### Экземпляр класса MutableString должен позволять получать, изменять и удалять значения своих элементов с помощью индексов, причем как положительных, так и отрицательных.
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса MutableString нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">mutablestring = MutableString('Beegeek')<br>
                          mutablestring.lower()<br>
                          print(mutablestring)<br>
                          mutablestring.upper()<br>
                          print(mutablestring)<br>
                          mutablestring.sort()<br>
                          print(mutablestring)<br></td>
      <td align="center">mutablestring = MutableString('beegeek')<br>
                          print(mutablestring)<br>
                          mutablestring[0] = 'B'<br>
                          mutablestring[-4] = 'G'<br>
                          print(mutablestring)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        beegeek<br>
                        BEEGEEK<br>
                        BEEEEGK<br>
      </td>
      <td align="center">
                        beegeek<br>
                        BeeGeek<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from collections import UserString
from copy import copy


class MutableString(UserString):
    def __init__(self, string):
        super().__init__(string)

    def __setitem__(self, key, item):
        __lst = list(self.data)
        __lst[key] = item
        self.data = ''.join(copy(__lst))
        return self

    def __delitem__(self, key):
        __lst = list(self.data)
        del __lst[key]
        self.data = ''.join(copy(__lst))
        return self

    def lower(self):
        self.data = copy(self.data.lower())
        return self

    def upper(self):
        self.data = copy(self.data.upper())
        return self

    def sort(self, key=lambda x: x, reverse=False):
        self.data = ''.join(sorted(self.data, key=key, reverse=reverse))
        return self
```
* Второй вариант решения

```python
from collections import UserString


class MutableString(UserString):
    def __setitem__(self, index, value):
        data_as_list = list(self.data)
        data_as_list[index] = value
        self.data = "".join(data_as_list)

    def __delitem__(self, index):
        data_as_list = list(self.data)
        del data_as_list[index]
        self.data = "".join(data_as_list)

    def upper(self):
        self.data = self.data.upper()

    def lower(self):
        self.data = self.data.lower()

    def sort(self, key=None, reverse=False):
        self.data = "".join(sorted(self.data, key=key, reverse=reverse))
```


