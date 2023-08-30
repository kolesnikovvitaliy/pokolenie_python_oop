<h2 style="text-align:center">Декоратор @auto_repr</h2>

### Реализуйте декоратор @auto_repr для декорирования класса. Декоратор должен принимать два аргумента в следующем порядке:

* args — список имен атрибутов
* kwargs — список имен атрибутов
#### Декоратор должен реализовывать формальное строковое представление для экземпляров декорируемого класса. Строковое представление должно содержать имя класса и значения атрибутов экземпляра класса и иметь вид:

> <имя класса>(<атрибут>, <атрибут>, ...)
#### Если атрибут указан в списке args, в строковом представлении должно быть только его значение, если же атрибут указан в списке kwargs, в строковом представлении должно быть его значение вместе с именем.

##### Примечание 1. Атрибуты в форматированной строке должны располагаться в том порядке, в котором они были присвоены экземпляру.

##### Примечание 2. Гарантируется, что при декорировании указываются все необходимые имена атрибутов. Также гарантируется, что имя атрибута указывается либо только в списке args, либо только в списке kwargs. Причем порядок расположения имен атрибутов в списках args и kwargs повторяет их расположение в сигнатуре инициализатора декорируемого класса.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">@auto_repr(args=['x', 'y'], kwargs=['color'])<br>
                          class Point:<br>
                              def __init__(self, x, y, color):<br>
                                  self.x = x<br>
                                  self.y = y<br>
                                  self.color = color<br>
                          point = Point(1, 2, color='green')<br>
                          print(point)<br>
                          point.x = 10<br>
                          point.y = 20<br>
                          print(point)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        Point(1, 2, color='green')<br>
                        Point(10, 20, color='green')<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
import functools


def auto_repr(args, kwargs):
    lst_args = [*args]
    lst_kwargs = [*kwargs]

    def wrapper(cls):
        old_repr = cls.__repr__

        @functools.wraps(old_repr)
        def decorator(self):
            tmp = []
            for i in lst_args:
                tmp.append(repr(self.__dict__[i]))
            for i in lst_kwargs:
                tmp.append(f'{i}={repr(self.__dict__[i])}')
            return f'{cls.__name__}({", ".join(map(str,tmp))})'
        cls.__repr__ = decorator
        return cls
    return wrapper
```
* Второй вариант решения

```python
def auto_repr(args, kwargs):
    def wrapper(cls):
        def __repr__(self):
            cls_args = [repr(self.__dict__[k]) for k in args]
            cls_kwargs = [f'{k}={self.__dict__[k]!r}' for k in kwargs]
            return f'{type(self).__name__}({", ".join(cls_args + cls_kwargs)})'

        cls.__repr__ = __repr__
        return cls

    return wrapper
```


