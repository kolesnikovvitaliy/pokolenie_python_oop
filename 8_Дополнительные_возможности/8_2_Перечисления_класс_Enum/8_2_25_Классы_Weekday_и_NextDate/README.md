<h2 style="text-align:center">Классы Weekday и NextDate</h2>

### 1. Реализуйте класс Weekday, описывающий перечисление с днями недели. Перечисление должно иметь семь элементов:

* MONDAY — элемент со значением 0
* TUESDAY — элемент со значением 1
* WEDNESDAY — элемент со значением 2
* THURSDAY — элемент со значением 3
* FRIDAY — элемент со значением 4
* SATURDAY — элемент со значением 5
* SUNDAY — элемент со значением 6
### 2. Также реализуйте класс NextDate, позволяющий определять дату следующего дня недели, начиная с текущего дня. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

* today — дата текущего дня, представленная экземпляром класса date
weekday — день недели, представленный элементом перечисления Weekday
* after_today — булево значение, по умолчанию равняется False
#### Параметр after_today должен определять, учитывается ли текущая дата при определении даты следующего дня недели. Если он имеет значение False, текущая дата не должна учитываться, если True — должна учитываться.

#### Класс NextDate должен иметь два метода экземпляра:

* date() — метод, возвращающий дату следующего дня недели в виде экземпляра класса date
* days_until() — метод, возвращающий количество дней до даты следующего дня недели
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

##### Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">from datetime import date<br>
                        today = date(2023, 4, 17)                              # понедельник<br>
                        next_friday = NextDate(today, Weekday.FRIDAY)          # следующая пятница<br>
                        print(next_friday.date())<br>
                        print(next_friday.days_until())<br></td>
      <td align="center">from datetime import date<br>
                          today = date(2023, 4, 17)                              # понедельник<br>
                          next_monday = NextDate(today, Weekday.MONDAY)          # следующий понедельник без учета <br>текущего<br>
                          print(next_monday.date())<br>
                          print(next_monday.days_until())<br></td>
      <td align="center">from datetime import date<br>
                        today = date(2023, 4, 17)                              # понедельник<br>
                        next_monday = NextDate(today, Weekday.MONDAY, True)    # следующий понедельник с учетом <br>текущего<br>
                        print(next_monday.date())<br>
                        print(next_monday.days_until())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        2023-04-21<br>
                        4<br>
      </td>
      <td align="center">
                        2023-04-24<br>
                        7<br>
      </td>
      <td align="center">
                        2023-04-17<br>
                        0<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from enum import Enum
from datetime import timedelta


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class NextDate:
    def __init__(self, today, weekday, after_today=False):
        self.today = today
        self.weekday = weekday
        self.after_today = after_today

    def date(self):
        if self.today.weekday() < self.weekday.value:
            return self.today + timedelta(days=(self.weekday.value-self.today.weekday()))
        elif self.today.weekday() > self.weekday.value:
            return self.today + timedelta(days=(7 - self.today.weekday()+self.weekday.value))
        elif self.today.weekday() is self.weekday.value:
            if self.after_today:
                return self.today + timedelta(days=0)
            return self.today + timedelta(days=7)

    def days_until(self):
        return (self.date() - self.today).days
```
* Второй вариант решения

```python
from datetime import timedelta
from enum import IntEnum

Weekday = IntEnum('Weekday', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], start=0)


class NextDate:
    def __init__(self, today, weekday, after_today=False):
        self.today = today
        self.weekday = weekday
        self.after_today = after_today

    def date(self):
        next_date = self.today + timedelta((self.weekday - self.today.weekday()) % 7)
        if not self.after_today and next_date == self.today:
            next_date += timedelta(7)
        return next_date

    def days_until(self):
        return (self.date() - self.today).days
```


