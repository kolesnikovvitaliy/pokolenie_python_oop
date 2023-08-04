<h2 style="text-align:center">Класс AdvancedTimer</h2>

### Реализуйте класс AdvancedTimer. При создании экземпляра класс не должен принимать никаких аргументов.
#### Экземпляр класса AdvancedTimer должен являться многоразовым контекстным менеджером, который замеряет время выполнение кода внутри каждого блока with.

#### Также экземпляр класса AdvancedTimer должен иметь четыре атрибута:
* last_run — число, представляющее время выполнения кода внутри последнего блока with
* runs — список чисел, каждое из которых представляет время выполнения какого-либо кода внутри блока with. Первый элемент списка должен представлять собой время выполнения кода внутри первого блока with, второй элемент — внутри второго блока with, и так далее
* min — число, представляющее минимальное время выполнения кода внутри блока with среди всех замеров
* max — число, представляющее максимальное время выполнения кода внутри блока with среди всех замеров
#### Если экземпляр класса AdvancedTimer ни разу не использовался для замера скорости выполнения какого-либо блока кода, значения атрибутов last_run, min и max должны равняться None.
##### Примечание 1. Наглядные примеры использования класса AdvancedTimer продемонстрированы в тестовых данных.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Класс AdvancedTimer должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">timer = AdvancedTimer()<br>
                        print(timer.runs)<br>
                        print(timer.last_run)<br>
                        print(timer.min)<br>
                        print(timer.max)<br></td>
      <td align="center">from time import sleep<br>
                          timer = AdvancedTimer()<br>
                          with timer:<br>
                              sleep(1.5)<br>
                          print(round(timer.last_run, 1))<br>
                          with timer:<br>
                              sleep(0.7)<br>
                          print(round(timer.last_run, 1))<br>
                          with timer:<br>
                              sleep(1)<br>
                          print(round(timer.last_run, 1))<br></td>
      <td align="center">from time import sleep<br>
                          timer = AdvancedTimer()<br>
                          with timer:<br>
                              sleep(1.5)<br>
                          with timer:<br>
                              sleep(0.7)<br>
                          with timer:<br>
                              sleep(1)<br>
                          print([round(runtime, 1) for runtime in timer.runs])<br>
                          print(round(timer.min, 1))<br>
                          print(round(timer.max, 1))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        []<br>
                        None<br>
                        None<br>
                        None<br>
      </td>
      <td align="center">
                        1.5<br>
                        0.7<br>
                        1.0<br>
      </td>
      <td align="center">
                        [1.5, 0.7, 1.0]<br>
                        0.7<br>
                        1.5<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from time import perf_counter


class AdvancedTimer:
    def __init__(self):
        self.hisory_run = []
        self.runs = self.hisory_run
        self.last_run = None
        self.max = None
        self.min = None

    def __enter__(self):
        self._start = perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.result = perf_counter() - self._start
        self.hisory_run.append(self.result)
        self.last_run = self.hisory_run[-1]
        self.runs = self.hisory_run
        self.max = max(self.hisory_run)
        self.min = min(self.hisory_run)
        return True
```
* Второй вариант решения

```python
import time

class AdvancedTimer:
    def __init__(self):
        self.runs = []
        self.last_run = self.min = self.max = None

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args, **kwargs):
        self.last_run = time.perf_counter() - self.start
        self.runs.append(self.last_run)
        self.min = min(self.runs)
        self.max = max(self.runs)
```


