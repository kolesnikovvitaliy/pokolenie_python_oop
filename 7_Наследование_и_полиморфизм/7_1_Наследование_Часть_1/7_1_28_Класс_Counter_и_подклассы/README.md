<h2 style="text-align:center">Класс Counter и подклассы</h2>


### 1. Реализуйте класс Counter, описывающий неотрицательный счетчик. При создании экземпляра класс должен принимать один аргумент:
* start — начальное значение счетчика, по умолчанию равняется 0
#### Экземпляр класса Counter должен иметь один атрибут:
* value — текущее значение счетчика
#### Класс Counter должен иметь два метода экземпляра:
* inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число. Если число не передано, метод должен увеличить значение счетчика на единицу
* dec() — метод, принимающий в качестве аргумента целое число и уменьшающий значение счетчика на это число. Если число не передано, метод должен уменьшить значение счетчика на единицу. Значение счетчика считается равным 0, если при уменьшении оно становится отрицательным

### 2. Также реализуйте класс NonDecCounter, наследника класса Counter, описывающий счетчик, значение которого можно увеличивать, но нельзя уменьшать. Процесс создания экземпляра класса NonDecCounter должен совпадать с процессом создания экземпляра класса Counter.

#### Экземпляр класса NonDecCounter должен иметь один атрибут:
* value — текущее значение счетчика
#### Класс NonDecCounter должен иметь один метод экземпляра:
* dec() — пустой метод. Сигнатура метода должна совпадать с сигнатурой метода dec() класса Counte
### 3. Наконец, реализуйте класс LimitedCounter, наследника класса Counter, описывающий счетчик, значение которого можно увеличивать лишь до определенного числа. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* start — начальное значение счетчика, по умолчанию равняется 0
* limit — максимально возможное значение счетчика, по умолчанию равняется 10
#### Экземпляр класса LimitedCounter должен иметь один атрибут:
* value — текущее значение счетчика
#### Класс LimitedCounter должен иметь один метод экземпляра:
* inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число. Если число не передано, метод должен увеличить значение счетчика на единицу. При увеличении значения счетчика метод не должен превышать установленный лимит


##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">rectangle = Rectangle(4, 5)<br>
                            print(rectangle.length)<br>
                            print(rectangle.width)<br>
                            print(rectangle.perimeter)<br>
                            print(rectangle.area)<br></td>
      <td align="center">rectangle = Rectangle(4, 5)<br>
                            rectangle.length = 2<br>
                            rectangle.width = 3<br>
                            print(rectangle.length)<br>
                            print(rectangle.width)<br>
                            print(rectangle.perimeter)<br>
                            print(rectangle.area)<br></td>
      <td align="center">rectangle = Rectangle(4, 5)<br>
                            print(rectangle.length)<br>
                            print(rectangle.width)<br>
                            print(rectangle.perimeter)<br>
                            print(rectangle.area)<br></td>
      <td align="center">rectangle = Rectangle(4, 5)<br>
                            rectangle.length = 2<br>
                            rectangle.width = 3<br>
                            print(rectangle.length)<br>
                            print(rectangle.width)<br>
                            print(rectangle.perimeter)<br>
                            print(rectangle.area)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        4<br>
                        5<br>
                        18<br>
                        20<br>
      </td>
      <td align="center">
                        2<br>
                        3<br>
                        10<br>
                        6<br>
      </td>
      <td align="center">
                        4<br>
                        5<br>
                        18<br>
                        20<br>
      </td>
      <td align="center">
                        2<br>
                        3<br>
                        10<br>
                        6<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Counter:
    def __init__(self, start: int = 0):
        self.value = start

    def inc(self, n=None):
        if n:
            self.value += n
        else:
            self.value += 1

    def dec(self, n=None):
        if n:
            self.value -= n
        else:
            self.value -= 1
        if self.value < 0:
            self.value = 0


class NonDecCounter(Counter):
    def dec(self, n=None):
        ...


class LimitedCounter(Counter):
    def __init__(self, start: int = 0, limit: int = 10):
        super().__init__(start)
        self.__limit = limit

    def inc(self, n=None):
        if self.value < self.__limit:
            if n:
                self.value += n
            else:
                self.value += 1
            if self.value > self.__limit:
                self.value = self.__limit
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


class NonDecCounter(Counter):
    def dec(self, n=1):
        return None


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        Counter.__init__(self, start)
        self.limit = limit

    def inc(self, n=1):
        self.value = min(self.value + n, self.limit)
```


