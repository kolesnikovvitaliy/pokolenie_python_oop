<h2 style="text-align:center">Декоратор @limited_calls</h2>

### Реализуйте класс декоратор @limited_calls, который принимает один аргумент:

* n — целое число
#### Декоратор должен разрешать вызывать декорируемую функцию n раз. Если декорируемая функция вызывается более n раз, должно быть возбуждено исключение MaxCallsException с текстом:

> Превышено допустимое количество вызовов
##### Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

##### Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @limited_calls, но не код, вызывающий его.



<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">@limited_calls(3)<br>
                          def add(a, b):<br>
                              return a + b<br>
                          print(add(1, 2))<br>
                          print(add(3, 4))<br>
                          print(add(5, 6))<br>
                          try:<br>
                              print(add())<br>
                          except MaxCallsException as e:<br>
                              print(e)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
    <tr>
      <td align="center">
                        3<br>
                        7<br>
                        11<br>
                        Превышено допустимое количество вызовов<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from functools import wraps


class MaxCallsException(Exception):
    pass


class limited_calls:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args):
            if self.n:
                result = func(*args)
                self.n -= 1
                return result
            raise MaxCallsException('Превышено допустимое количество вызовов')
        return wrapper
```
* Второй вариант решения

```python
import functools


class MaxCallsException(Exception):
    pass


class limited_calls:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.n == 0:
                raise MaxCallsException('Превышено допустимое количество вызовов')
            self.n -= 1
            return func(*args, **kwargs)

        return wrapper
```


