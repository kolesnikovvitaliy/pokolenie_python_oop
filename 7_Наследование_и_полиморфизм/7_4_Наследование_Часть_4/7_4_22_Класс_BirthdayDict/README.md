<h2 style="text-align:center">Класс BirthdayDict</h2>


### Реализуйте класс BirthdayDict, наследника класса UserDict, описывающий словарь с информацией о днях рождения, ключами в котором являются имена, а значениями — даты дней рождения. Процесс создания экземпляра класса BirthdayDict должен совпадать с процессом создания экземпляра класса UserDict.
#### При добавлении новой пары ключ: значение в экземпляр класса BirthdayDict должна производиться проверка на наличие в этом экземпляре пары, которая имеет такое же значение, что и добавляемая пара. И если такая пара есть, должен выводиться текст:
> Хей, <ключ добавляемой пары>, не только ты празднуешь день рождения в этот день!
### Аналогичное поведение должно быть и при изменении значения по ключу.
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса BirthdayDict нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">from datetime import date<br>
                          birthdaydict = BirthdayDict()<br>
                          birthdaydict['Боб'] = date(1987, 6, 15)<br>
                          birthdaydict['Том'] = date(1984, 7, 15)<br>
                          birthdaydict['Мария'] = date(1987, 6, 15)<br>
<br></td>
      <td align="center">from datetime import date<br>
                          birthdaydict = BirthdayDict()<br>
                          birthdaydict['Боб'] = date(1987, 6, 15)<br>
                          birthdaydict['Том'] = date(1984, 7, 15)<br>
                          birthdaydict['Мария'] = date(1989, 10, 1)<br>
                          birthdaydict['Боб'] = date(1989, 10, 1)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                       Хей, Мария, не только ты празднуешь день рождения в этот день!<br>
      </td>
      <td align="center">
                        Хей, Боб, не только ты празднуешь день рождения в этот день!<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from collections import UserDict


class BirthdayDict(UserDict):
    def __setitem__(self, key, item):
        if item in self.values():
            print(f'Хей, {key}, не только ты празднуешь день рождения в ' +
                  'этот день!')
        return super().__setitem__(key, item)
```
* Второй вариант решения

```python
from collections import UserDict

class BirthdayDict(UserDict):

    def __setitem__(self, key, value):
        if value in self.data.values():
            print(f'Хей, {key}, не только ты празднуешь день рождения в этот день!')
        self.data[key] = value
```


