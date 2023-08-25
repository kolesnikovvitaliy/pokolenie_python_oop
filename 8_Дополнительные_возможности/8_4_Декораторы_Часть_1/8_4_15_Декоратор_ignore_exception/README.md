<h2 style="text-align:center">Декоратор @ignore_exception</h2>

### Реализуйте класс декоратор @ignore_exception, который принимает произвольное количество позиционных аргументов — типов исключений, и выводит текст:

> Исключение <тип исключения> обработано
#### если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов. Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.

##### Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

##### Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @ignore_exception, но не код, вызывающий его.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">@ignore_exception(ZeroDivisionError, TypeError, ValueError)<br>
                            def func(x):<br>
                                return 1 / x<br>
                            func(0)<br></td>
      <td align="center">min = ignore_exception(ZeroDivisionError)(min)<br>
                          try:<br>
                              print(min(1, '2', 3, [4, 5]))<br>
                          except Exception as error:<br>
                              print(type(error))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Исключение ZeroDivisionError обработано<br>
      </td>
      <td align="center">
                        class 'TypeError'<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
import functools


class ignore_exception:
    def __init__(self, *args):
        self.args = args

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as error:
                if type(error) in self.args:
                    print(f'Исключение {type(error).__name__} обработано')
                else:
                    raise type(error)
        return wrapper
```
* Второй вариант решения

```python
import functools


class ignore_exception:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
                return value
            except self.exceptions as e:
                print(f'Исключение {e.__class__.__name__} обработано')

        return wrapper
```


