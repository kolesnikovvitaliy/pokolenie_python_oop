<h2 style="text-align:center">Декоратор @takes_numbers</h2>

### Реализуйте класс декоратор @takes_numbers, который проверяет, что все аргументы, передаваемые в декорируемую функцию, принадлежат типам int или float. Если хотя бы один аргумент принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:

> Аргументы должны принадлежать типам int или float
##### Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

##### Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @takes_numbers, но не код, вызывающий его.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">@takes_numbers<br>
                          def mul(a, b):<br>
                              return a * b<br>
                          print(mul(1, 2))<br>
                          print(mul(1, 2.5))<br>
                          print(mul(1.5, 2))<br>
                          print(mul(1.5, 2.5))<br></td>
      <td align="center">@takes_numbers<br>
                          def mul(a, b):<br>
                              return a * b<br>
                          try:<br>
                              print(mul(1, '2'))<br>
                          except TypeError as error:<br>
                              print(error)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        2<br>
                        2.5<br>
                        3.0<br>
                        3.75<br>
      </td>
      <td align="center">
                        Аргументы должны принадлежать типам int или float<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
import functools


class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        arg = [isinstance(i, (int, float)) for i in args]
        kwarg = [isinstance(i, (int, float)) for i in kwargs.values()]
        if not all(arg + kwarg):
            raise TypeError('Аргументы должны принадлежать типам int или float')
        return self.func(*args, **kwargs)
```
* Второй вариант решения

```python
import functools


class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        if any((
                not all(isinstance(arg, (int, float)) for arg in args),
                not all(isinstance(arg, (int, float)) for arg in kwargs.values())
        )):
            raise TypeError('Аргументы должны принадлежать типам int или float')
        return self.func(*args, **kwargs)
```


