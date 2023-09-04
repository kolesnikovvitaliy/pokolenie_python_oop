<h2 style="text-align:center">Классы ArithmeticProgression и GeometricProgression</h2>

### Реализуйте класс ArithmeticProgression для генерации членов арифметической прогрессии. При создании экземпляра класса ArithmeticProgression должны указываться первый член последовательности и разность прогрессии:
```python
progression = ArithmeticProgression(0, 1)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 0 1 2 3 4 5 6 7 8 9 10
```
#### Обратите внимание, что арифметическая прогрессия должна быть итерируемой, а также бесконечной.

#### Аналогичным образом реализуйте класс GeometricProgression для генерации членов геометрической прогрессии. При создании экземпляра класса GeometricProgression должны указываться первый член последовательности и знаменатель прогрессии:
```python
progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 1 2 4 8
```
#### Геометрическая прогрессия, как и арифметическая, должна быть итерируемой, а также бесконечной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">progression = ArithmeticProgression(0, 1)<br>
                          for elem in progression:<br>
                              if elem > 10:<br>
                                  break<br>
                              print(elem, end=' ')<br></td>
      <td align="center">progression = GeometricProgression(1, 2)<br>
                          for elem in progression:<br>
                              if elem > 10:<br>
                                  break<br>
                              print(elem, end=' ')<br></td>
      <td align="center">progression = ArithmeticProgression(0, -1)<br>
                          for _ in range(20):<br>
                              print(next(progression), end=' ')<br></td>
      <td align="center">progression = GeometricProgression(4, -2)<br>
                          count = 0<br>
                          for item in progression:<br>
                              if count == 20:<br>
                                  break<br>
                              count += 1<br>
                              print(item, end=' ')<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        0 1 2 3 4 5 6 7 8 9 10<br>
      </td>
      <td align="center">
                        1 2 4 8<br>
      </td>
      <td align="center">
                        0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19<br>
      </td>
      <td align="center">
                        4 -8 16 -32 64 -128 256 -512 1024 -2048 4096 -8192 16384 -32768 65536 -131072 262144 -524288 1048576 -2097152<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class ArithmeticProgression:
    def __init__(self, first, d):
        self.first = first
        self.d = d
        self.flag = True

    def __iter__(self):
        return self

    def __next__(self):
        res = self.first
        self.first += self.d
        return res


class GeometricProgression(ArithmeticProgression):
    def __next__(self):
        res = self.first
        self.first *= self.d
        return res
```
* Второй вариант решения

```python
from abc import ABC, abstractmethod


class Progression(ABC):
    def __init__(self, start, step):
        self._current = start
        self._step = step

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass


class ArithmeticProgression(Progression):
    def __next__(self):
        answer = self._current
        self._current += self._step
        return answer


class GeometricProgression(Progression):
    def __next__(self):
        answer = self._current
        self._current *= self._step
        return answer
```


