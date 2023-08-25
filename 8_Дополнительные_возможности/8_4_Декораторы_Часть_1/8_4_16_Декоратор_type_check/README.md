<h2 style="text-align:center">Декоратор @type_check</h2>

### Реализуйте класс декоратор @type_check, который принимает один аргумент:

* types — список, элементами которого являются типы данных
#### Декоратор должен проверять, что типы всех позиционных аргументов, передаваемых в декорируемую функцию, полностью сопоставляются с типами из списка types, то есть типом первого аргумента является первый элемент списка types, типом второго аргумента — второй элемент списка types, и так далее. Если данное условие не выполняется, должно быть возбуждено исключение TypeError.

#### Если количество позиционных аргументов больше, чем количество элементов в списке types, то не сопоставляемые аргументы не должны учитываться при проверке. Если количество позиционных аргументов меньше чем количество элементов в списке types, то не сопоставляемые типы из списка types не должны учитываться при проверке.

##### Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

##### Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @type_check, но не код, вызывающий его.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">@type_check([int, int])<br>
                          def add(a, b):<br>
                              return a + b<br>
                          print(add(1, 2))<br></td>
      <td align="center">@type_check([int, int])<br>
                          def add(a, b):<br>
                              return a + b<br>
                          try:<br>
                              print(add(1, '2'))<br>
                          except Exception as error:<br>
                              print(type(error))<br></td>
      <td align="center">@type_check([int, int, str, list])<br>
                          def add(a, b):<br>
                              """sum a and b"""<br>
                              return a + b<br>
                          print(add.__name__)<br>
                          print(add.__doc__)<br>
                          print(add(1, 2))<br></td>
      <td align="center">@type_check([int, int])<br>
                          def add(a, b, c):<br>
                              return a + b + c<br>
                          print(add(1, 2, 3.0))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        3<br>
      </td>
      <td align="center">
                        class 'TypeError'<br>
      </td>
      <td align="center">
                        add<br>
                        sum a and b<br>
                        3<br>
      </td>
      <td align="center">
                        6.0<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
import functools


class type_check:
    def __init__(self, types):
        self.types = types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            all_arg = zip(self.types, args)
            arg = map(lambda x: True if type(x[1]) == x[0] else False, all_arg)
            if not all(arg):
                raise TypeError
            result = func(*args, **kwargs)
            return result
        return wrapper
```
* Второй вариант решения

```python
import functools


class type_check:
    def __init__(self, types):
        self.types = types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg, arg_type in zip(args, self.types):
                if not isinstance(arg, arg_type):
                    raise TypeError
            value = func(*args, **kwargs)
            return value

        return wrapper
```


