<h2 style="text-align:center">Классы Lecture и Conference</h2>


### 1. Реализуйте класс Lecture, описывающий некоторое выступление. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

* topic — тема выступления
* start_time — время начала выступления в виде строки в формате HH:MM
* duration — длительность выступления в виде строки в формате HH:MM
### 2. Также реализуйте класс Conference, описывающий конференцию, протяженностью в один день. Конференция представляет собой набор последовательных выступлений. При создании экземпляра класс не должен принимать никаких аргументов.

#### Класс Conference должен иметь четыре метода экземпляра:

* add() — метод, принимающий в качестве аргумента выступление и добавляющий его в конференцию. Если выступление пересекается по времени с другими выступлениями, должно быть возбуждено исключение ValueError с текстом:
> Провести выступление в это время невозможно
* total() — метод, возвращающий суммарную длительность всех выступлений в конференции в виде строки в формате HH:MM
* longest_lecture() — метод, возвращающий длительность самого долгого выступления в конференции в виде строки в формате HH:MM
* longest_break() — метод, возвращающий длительность самого долгого перерыва между выступлениями в конференции в виде строке в формате HH:MM
##### Примечание 1. Перерыв между выступлениями может быть нулевым. Другими словами, одно выступление может заканчиваться, например, в 12:00, а другое начинаться в 12:00.

##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

##### Примечание 3. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">conference = Conference()<br>
                          conference.add(Lecture('Простые числа', '08:00', '01:30'))<br>
                          conference.add(Lecture('Жизнь после ChatGPT', '10:00', '02:00'))<br>
                          conference.add(Lecture('Муравьиный алгоритм', '13:30', '01:50'))<br>
                          print(conference.total())<br>
                          print(conference.longest_lecture())<br>
                          print(conference.longest_break())<br></td>
      <td align="center">conference = Conference()<br>
                          conference.add(Lecture('Простые числа', '08:00', '01:30'))<br>
                          try:<br>
                              conference.add(Lecture('Жизнь после ChatGPT', '09:00', '02:00'))<br>
                          except ValueError as error:<br>
                              print(error)<br></td>
      <td align="center">conference = Conference()<br>
                          conference.add(Lecture('Простые числа', '08:00', '01:00'))<br>
                          conference.add(Lecture('Жизнь после ChatGPT', '11:00', '02:00'))<br>
                          try:<br>
                              conference.add(Lecture('Муравьиный алгоритм', '10:00', '04:00'))<br>
                          except ValueError as error:<br>
                              print(error)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        05:20<br>
                        02:00<br>
                        01:30<br>
      </td>
      <td align="center">
                        Провести выступление в это время невозможно<br>
      </td>
      <td align="center">
                        Провести выступление в это время невозможно<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from datetime import timedelta


class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        h, m = map(int, start_time.split(':'))
        h_1, m_1 = map(int, duration.split(':'))
        self.start_time = timedelta(hours=h, minutes=m, seconds=00)
        self.duration = timedelta(hours=h_1, minutes=m_1, seconds=00)
        
        
class Conference:
    def __init__(self):
        self._lst = []

    def add(self, lecture):
        if self._lst:
            for i in self._lst:
                if i.start_time < lecture.start_time < i.start_time + i.duration:
                    raise ValueError('Провести выступление в это время невозможно')
                if lecture.start_time < i.start_time < lecture.start_time + lecture.duration:
                    raise ValueError('Провести выступление в это время невозможно')
                if lecture.start_time == i.start_time and lecture.duration == i.duration:
                    raise ValueError('Провести выступление в это время невозможно')
                if i.start_time == lecture.start_time < i.start_time + i.duration:
                    raise ValueError('Провести выступление в это время невозможно')
            self._lst.append(lecture)
        else:
            self._lst.append(lecture)

    def total(self):
        _tmp = list(map(lambda x: x.duration.seconds, self._lst))
        __lst = str(timedelta(seconds=sum(_tmp)))[:-3]
        if __lst[:2].isdigit():
            return __lst
        __lst = '0' + __lst
        return __lst

    def longest_lecture(self):
        _tmp = list(map(lambda x: x.duration.seconds, self._lst))
        __lst = str(timedelta(seconds=max(_tmp)))[:-3]
        if __lst[:2].isdigit():
            return __lst
        __lst = '0' + __lst
        return __lst

    def longest_break(self):
        __tmp = []
        sort_lst = sorted(self._lst, key=lambda x: x.start_time.seconds)
        _tmp = list(map(lambda x: (x.start_time, x.start_time + x.duration), sort_lst))
        for k, v in enumerate(_tmp, 1):
            if k < len(_tmp):
                __tmp.append(_tmp[k][0] - _tmp[k-1][1])
        _lst = list(map(lambda x: x.seconds, __tmp))
        result = str(timedelta(seconds=max(_lst)))[:-3]
        if result[:2].isdigit():
            return result
        result = '0' + result
        return result
```
* Второй вариант решения

```python
from bisect import insort
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta


class Lecture:
    _PATTERN = '%H:%M'

    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = datetime.strptime(start_time, self._PATTERN)
        self.duration = datetime.strptime(duration, self._PATTERN)
        self.end_time = self.start_time + timedelta(hours=self.duration.hour, minutes=self.duration.minute)


class Conference:
    def __init__(self):
        self.lectures = []

    def add(self, lecture):
        for cur_lecture in self.lectures:
            if any((
                    cur_lecture.start_time <= lecture.start_time < cur_lecture.end_time,
                    lecture.start_time <= cur_lecture.start_time < lecture.end_time,
            )):
                raise ValueError('Провести выступление в это время невозможно')
        insort(self.lectures, lecture, key=lambda item: item.start_time)

    def total(self):
        total = sum((lecture.end_time - lecture.start_time for lecture in self.lectures), start=relativedelta())
        return f'{total.hours:0>2}:{total.minutes:0>2}'

    def longest_lecture(self):
        longest = max(lecture.duration for lecture in self.lectures)
        return f'{longest.hour:0>2}:{longest.minute:0>2}'

    def longest_break(self):
        longest = max(self.lectures[i + 1].start_time - self.lectures[i].end_time for i in range(len(self.lectures) - 1))
        hours, minutes = int(longest.total_seconds()) // 3600, (int(longest.total_seconds()) // 60) % 60
        return f'{hours:0>2}:{minutes:0>2}'
```


