<h2 style="text-align:center">Декоратор @returns</h2>

### Реализуйте класс декоратор @returns, который принимает один аргумент:

* datatype — тип данных
#### Декоратор должен проверять, что возвращаемое значение декорируемой функции принадлежит типу datatype. Если возвращаемое значение принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError.

##### Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

##### Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @returns, но не код, вызывающий его.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">@returns(int)<br>
                          def add(a, b):<br>
                              return a + b<br>
                          print(add(1, 2))<br></td>
      <td align="center">@returns(int)<br>
                        def add(a, b):<br>
                            return a + b<br>
                        try:<br>
                            print(add('1', '2'))<br>
                        except Exception as error:<br>
                            print(type(error))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        3<br>
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


class returns:
    def __init__(self, datatype):
        self.datatype = datatype

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, self.datatype):
                return result
            raise TypeError
        return wrapper
```
* Второй вариант решения

```python
import functools


class returns:
    def __init__(self, datatype):
        self.datatype = datatype

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if not isinstance(value, self.datatype):
                raise TypeError
            return value

        return wrapper
```


