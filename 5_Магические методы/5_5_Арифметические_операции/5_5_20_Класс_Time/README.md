<h2 style="text-align:center">Класс Time</h2>

### Реализуйте класс Time, описывающий время на цифровых часах. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* hours — количество часов; каждые 24 часа должны преобразовываться в 0 часов
* minutes — количество минут; каждые 60 минут должны преобразовываться в 1 час
#### Экземпляр класса Time должен иметь следующее неформальное строковое представление:
> <количество часов в формате HH>:<количество минут в формате MM>
#### Также экземпляры класса Time должны поддерживать между собой операцию сложения с помощью операторов + и +=:
* результатом сложения с помощью оператора + должен являться новый экземпляр класса Time, количество часов которого равно сумме часов исходных экземпляров класса Time, количество минут — сумме минут исходных экземпляров класса Time
* результатом сложения с помощью оператора += должен являться левый экземпляр класса Time, количество часов которого увеличено на количество часов правого экземпляра класса Time, количество минут — на количество минут правого экземпляра класса Time

##### Примечание 1. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса Time нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">time1 = Time(2, 30)
                        time2 = Time(3, 10)
                        print(time1 + time2)
                        print(time2 + time1)<br></td>
      <td align="center">time1 = Time(2, 30)
                          time2 = Time(3, 10)
                          time1 += time2
                          print(time1)
                          print(time2)<br></td>
      <td align="center">time1 = Time(25, 20)
                        time2 = Time(10, 130)
                        print(time1)
                        print(time2)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        05:40
                        05:40<br>
      </td>
      <td align="center">
                        05:40
                        03:10<br>
      </td>
      <td align="center">
                        01:20
                        12:10<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from datetime import time


class Time:
    def __init__(self, hours, minutes):
        __time = (hours%24,*divmod(minutes,60))
        self.hours, self.minutes = (__time[0]+__time[1],__time[2])
    
    def __add__(self, other):
        if isinstance(other, __class__):
            h, m = map(sum, zip((self.hours, self.minutes), (other.hours, other.minutes)))
            return __class__(h, m)
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, __class__):
            self.hours += other.hours 
            self.minutes += other.minutes
            return self
        return NotImplemented
    
    def __str__(self) -> str:
        __time = (self.hours%24,*divmod(self.minutes,60))
        hours, minutes = (__time[0]+__time[1],__time[2])
        return f"{time(hours, minutes).strftime('%H:%M')}"
```
* Второй вариант решения

```python
class Time:
    def __init__(self, hours, minutes):
        self.hours, self.minutes = Time._normalize(hours, minutes)

    @staticmethod
    def _normalize(hours, minutes):
        return (hours + minutes // 60) % 24, minutes % 60

    def __str__(self):
        return f'{self.hours:>02}:{self.minutes:>02}'

    def __add__(self, other):
        if isinstance(other, Time):
            hours, minutes = self._normalize(self.hours + other.hours, self.minutes + other.minutes)
            return Time(hours, minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours, self.minutes = self._normalize(self.hours + other.hours, self.minutes + other.minutes)
            return self
        return NotImplemented
```


