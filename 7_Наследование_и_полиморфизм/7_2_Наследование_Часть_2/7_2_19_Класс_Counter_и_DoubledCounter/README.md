<h2 style="text-align:center">Класс Counter и DoubledCounter</h2>

### Вам доступен класс Counter, описывающий неотрицательный счетчик:
```python 
class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)
```
#### При создании экземпляра класс принимает один аргумент:
* start — начальное значение счетчика, по умолчанию равняется 0

#### Экземпляр класса Counter имеет один атрибут:
* value — текущее значение счетчика
#### Класс Counter имеет два метода экземпляра:
* inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число. Если число не передано, метод увеличивает значение счетчика на единицу
* dec() — метод, принимающий в качестве аргумента целое число и уменьшающий значение счетчика на это число. Если число не передано, метод уменьшает значение счетчика на единицу. Значение счетчика считается равным 0, если при уменьшении оно становится отрицательным
### Реализуйте класс DoubledCounter, наследника класса Counter, описывающий неотрицательный счетчик, значение которого увеличивается и уменьшается дважды при вызове соответствующих методов. Процесс создания экземпляра класса DoubledCounter должен совпадать с процессом создания экземпляра класса Counter.
#### Экземпляр класса DoubledCounter должен иметь один атрибут:
* value — текущее значение счетчика
#### Класс DoubledCounter должен иметь два метода экземпляра:
* inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число дважды. Если число не передано, метод должен увеличить значение счетчика на два
* dec() — метод, принимающий в качестве аргумента целое число и уменьшающий значение счетчика на это число дважды. Если число не передано, метод должен уменьшить значение счетчика на два. Значение счетчика считается равным 0, если при уменьшении оно становится отрицательным

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">print(issubclass(DoubledCounter, Counter))<br></td>
      <td align="center">counter = Counter(10)<br>
                        print(counter.value)<br>
                        counter.inc()<br>
                        counter.inc(5)<br>
                        print(counter.value)<br>
                        counter.dec()<br>
                        counter.dec(10)<br>
                        print(counter.value)<br>
                        counter.dec(10)<br>
                        print(counter.value)<br></td>
      <td align="center">counter = DoubledCounter(20)<br>
                          print(counter.value)<br>
                          counter.inc()<br>
                          counter.inc(5)<br>
                          print(counter.value)<br>
                          counter.dec()<br>
                          counter.dec(10)<br>
                          print(counter.value)<br>
                          counter.dec(10)<br>
                          print(counter.value)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
      </td>
      <td align="center">
                        10<br>
                        16<br>
                        5<br>
                        0<br>
      </td>
      <td align="center">
                        20<br>
                        32<br>
                        10<br>
                        0<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)


class DoubledCounter(Counter):
    def inc(self, n=None):
        if n:
            super().inc(n*2)
        else:
            super().inc(2)

    def dec(self, n=None):
        if n:
            super().dec(n*2)
        else:
            super().dec(2)
```
* Второй вариант решения

```python
class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)


class DoubledCounter(Counter):
    def inc(self, n=1):
        super().inc(n * 2)

    def dec(self, n=1):
        super().dec(n * 2)
```


