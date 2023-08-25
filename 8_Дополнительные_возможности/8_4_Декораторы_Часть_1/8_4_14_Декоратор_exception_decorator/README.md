<h2 style="text-align:center">Декоратор @exception_decorator</h2>

### Реализуйте класс декоратор @exception_decorator, который возвращает

* кортеж (value, None), если декорируемая функция завершила свою работу без возбуждения исключения, где value — возвращаемое значение декорируемой функции
* кортеж (None, errortype), если во время выполнения декорируемой функции было возбуждено исключение, где errortype — тип возбужденного исключения
##### Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

##### Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @exception_decorator, но не код, вызывающий его. 

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">@exception_decorator<br>
                          def func(x):<br>
                              return 2*x + 1<br>
                          print(func(1))<br>
                          print(func('bee'))<br></td>
      <td align="center">@exception_decorator<br>
                        def f(x, y):<br>
                            return x * y<br>
                        print(f('stepik', 10))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        (3, None)<br>
                        (None, class 'TypeError')<br>
      </td>
      <td align="center">
                        ('stepikstepikstepikstepikstepikstepikstepikstepikstepikstepik', None)<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
import functools


class exception_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            result = self.func(*args, **kwargs)
            return result, None
        except TypeError:
            return None, TypeError
```
* Второй вариант решения

```python
import functools


class exception_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            value = self.func(*args, **kwargs)
            return value, None
        except Exception as e:
            return None, type(e)
```


