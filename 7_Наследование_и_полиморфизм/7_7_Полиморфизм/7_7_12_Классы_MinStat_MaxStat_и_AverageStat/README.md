<h2 style="text-align:center">Классы MinStat, MaxStat и AverageStat</h2>

### 1. Реализуйте класс MinStat, описывающий объект, который находит минимальное значение среди определенного набора чисел. При создании экземпляра класс должен принимать один аргумент:

* iterable — итерируемый объект, определяющий начальный набор чисел. Если не передан, начальный набор считается пустым
#### Класс MinStat должен иметь три метода экземпляра:

* add() — метод, принимающий в качестве аргумента число и добавляющий его в набор
* result() — метод, возвращающий минимальное число из набора. Если набор пуст, метод должен вернуть значение None
* clear() — метод, удаляющий из набора все числа
### 2. Также реализуйте класс MaxStat, описывающий объект, который находит максимальное значение среди определенного набора чисел. При создании экземпляра класс должен принимать один аргумент:

* iterable — итерируемый объект, определяющий начальный набор чисел. Если не передан, начальный набор считается пустым
#### Класс MaxStat должен иметь три метода экземпляра:

* add() — метод, принимающий в качестве аргумента число и добавляющий его в набор
* result() — метод, возвращающий максимальное число из набора. Если набор пуст, метод должен вернуть значение None
* clear() — метод, удаляющий из набора все числа
### 3. Наконец, реализуйте класс AverageStat, описывающий объект, который находит среднее арифметическое определенного набора чисел. При создании экземпляра класс должен принимать один аргумент:

* iterable — итерируемый объект, определяющий начальный набор чисел. Если не передан, начальный набор считается пустым
#### Класс AverageStat должен иметь три метода экземпляра:

* add() — метод, принимающий в качестве аргумента число и добавляющий его в набор
* result() — метод, возвращающий среднее арифметическое набора чисел. Если набор пуст, метод должен вернуть значение None
* clear() — метод, удаляющий из набора все числа

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
      <td align="center">minstat = MinStat([1, 2, 4])<br>
                          maxstat = MaxStat([1, 2, 4])<br>
                          averagestat = AverageStat([1, 2, 4])<br>
                          minstat.add(5)<br>
                          maxstat.add(5)<br>
                          averagestat.add(5)<br>
                          print(minstat.result())<br>
                          print(maxstat.result())<br>
                          print(averagestat.result())<br></td>
      <td align="center">minstat = MinStat()<br>
                        maxstat = MaxStat()<br>
                        averagestat = AverageStat()<br>
                        for i in range(1, 6):<br>
                            minstat.add(i)<br>
                            maxstat.add(i)<br>
                            averagestat.add(i)<br>
                        print(minstat.result())<br>
                        print(maxstat.result())<br>
                        print(averagestat.result())<br></td>
      <td align="center">minstat = MinStat()<br>
                        maxstat = MaxStat()<br>
                        averagestat = AverageStat()<br>
                        print(minstat.result())<br>
                        print(maxstat.result())<br>
                        print(averagestat.result())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        1<br>
                        5<br>
                        3.0<br>
      </td>
      <td align="center">
                        1<br>
                        5<br>
                        3.0<br>
      </td>
      <td align="center">
                        None<br>
                        None<br>
                        None<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class MinStat:
    def __init__(self, iterable=[]):
        self.iterable = iterable

    def add(self, item):
        self.iterable.append(item)

    def result(self):
        if self.iterable:
            return min(self.iterable)
        return None

    def clear(self):
        self.iterable.clear()


class MaxStat(MinStat):
    def result(self):
        if self.iterable:
            return max(self.iterable)
        return None


class AverageStat(MinStat):
    def result(self):
        if self.iterable:
            return sum(self.iterable) / len(self.iterable)
        return None
```
* Второй вариант решения

```python
import statistics
from abc import ABC, abstractmethod


class Stat(ABC):
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def add(self, n):
        self.data.append(n)

    def clear(self):
        self.data.clear()

    @abstractmethod
    def result(self):
        pass


class MinStat(Stat):
    def result(self):
        return min(self.data, default=None)


class MaxStat(Stat):
    def result(self):
        return max(self.data, default=None)


class AverageStat(Stat):
    def result(self):
        return statistics.fmean(self.data) if self.data else None
```


