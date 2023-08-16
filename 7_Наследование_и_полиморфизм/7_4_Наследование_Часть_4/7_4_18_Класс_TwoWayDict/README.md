<h2 style="text-align:center">Класс TwoWayDict</h2>


### Реализуйте класс TwoWayDict, наследника класса UserDict, описывающий двунаправленный словарь, в который при добавлении пары ключ: значение также добавляется и пара значение: ключ. Процесс создания экземпляра класса TwoWayDict должен совпадать с процессом создания экземпляра класса UserDict.


##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса TwoWayDict нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">twowaydict = TwoWayDict({'apple': 1})<br>
                          twowaydict['banana'] = 2<br>
                          print(twowaydict['apple'])<br>
                          print(twowaydict[1])<br>
                          print(twowaydict['banana'])<br>
                          print(twowaydict[2])<br></td>
      <td align="center">d = TwoWayDict()<br>
                        d[3] = 8<br>
                        d[7] = 6<br>
                        print(d[3], d[8])<br>
                        print(d[7], d[6])<br>
                        d.update({9: 7, 8: 2})<br>
                        print(d[9], d[7])<br>
                        print(d[8], d[2])<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        1<br>
                        apple<br>
                        2<br>
                        banana<br>
      </td>
      <td align="center">
                        8 3<br>
                        6 7<br>
                        7 9<br>
                        2 8<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from collections import UserDict


class TwoWayDict(UserDict):
    def __setitem__(self, key, item):
        self.data[key] = item
        self.data[item] = key
```
* Второй вариант решения

```python
from collections import UserDict

class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        self.data.__setitem__(key, value)
        self.data.__setitem__(value, key)
```


