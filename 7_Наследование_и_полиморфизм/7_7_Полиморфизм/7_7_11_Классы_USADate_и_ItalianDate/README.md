<h2 style="text-align:center">Классы USADate и ItalianDate</h2>

### 1. Реализуйте класс USADate, описывающий дату в американском формате. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
* year — год
* month — месяц
* day — день
#### Класс USADate должен иметь два метода экземпляра:
* format() — метод, который возвращает строку, представляющую собой дату в формате MM-DD-YYYY
* iso_format() — метод, который возвращает строку, представляющую собой дату в формате YYYY-MM-DD
### 2. Также реализуйте класс ItalianDate, описывающий дату в итальянском формате, конструктор которого принимает три аргумента:
* year — год
* month — месяц
* day — день
#### Класс ItalianDate должен иметь два метода экземпляра:
* format() — который возвращает строку, представляющую собой дату в формате DD/MM/YYYY
* iso_format() — который возвращает строку, представляющую собой дату в формате YYYY-MM-DD

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.


<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">usadate = USADate(2023, 4, 6)<br>
                        print(usadate.format())<br>
                        print(usadate.iso_format())<br></td>
      <td align="center">italiandate = ItalianDate(2023, 4, 6)<br>
                          print(italiandate.format())<br>
                          print(italiandate.iso_format())<br></td>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        04-06-2023<br>
                        2023-04-06<br>
      </td>
      <td align="center">
                        06/04/2023<br>
                        2023-04-06<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class USADate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return f'{self.month:02}-{self.day:02}-{self.year}'

    def iso_format(self):
        return f'{self.year}-{self.month:02}-{self.day:02}'


class ItalianDate(USADate):
    def format(self):
        return f'{self.day:02}/{self.month:02}/{self.year}'
```
* Второй вариант решения

```python
from abc import ABC, abstractmethod
from datetime import date


class DateFormat(ABC):
    def __init__(self, year, month, day):
        self._date = date(year, month, day)

    def iso_format(self):
        return self._date.isoformat()

    @abstractmethod
    def format(self):
        pass


class USADate(DateFormat):
    def format(self):
        return self._date.strftime('%m-%d-%Y')


class ItalianDate(DateFormat):
    def format(self):
        return self._date.strftime('%d/%m/%Y')
```


