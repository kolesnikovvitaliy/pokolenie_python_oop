<h2 style="text-align:center">Декоратор @snake_case</h2>

### Реализуйте декоратор @snake_case для декорирования класса. Декоратор должен принимать один аргумент:

* attrs — булево значение, по умолчанию равняется False
#### Декоратор должен переименовать все не магические методы в декорируемом классе, меняя их стиль написания c Camel Case и Lower Camel Case на Snake case. Параметр attrs должен определять, будут ли аналогичным образом переименованы атрибуты класса. Если он имеет значение True, стиль написания имен атрибутов класса должен поменяться с Camel Case и Lower Camel Case на Snake case, если False — остаться прежним.

##### Примечание 1. Гарантируется, что имена всех не магических методов и атрибутов в классе написаны в стилях Camel Case, LowerCamelCase или Snake Case.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">@snake_case()<br>
                          class MyClass:<br>
                              def FirstMethod(self):<br>
                                  return 1<br>
                              def superSecondMethod(self):<br>
                                  return 2<br>
                          obj = MyClass()<br>
                          print(obj.first_method())<br>
                          print(obj.super_second_method())<br></td>
      <td align="center">@snake_case(attrs=True)<br>
                          class MyClass:<br>
                              FirstAttr = 1<br>
                              superSecondAttr = 2<br>
                          print(MyClass.first_attr)<br>
                          print(MyClass.super_second_attr)<br></td>
      <td align="center">@snake_case()<br>
                          class MyClass:<br>
                              FirstAttr = 1<br>
                              def FirstMethod(self):<br>
                                  return 1<br>
                          obj = MyClass()<br>
                          print(MyClass.FirstAttr)<br>
                          print(obj.first_method())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        1<br>
                        2<br>
      </td>
      <td align="center">
                        1<br>
                        2<br>
      </td>
      <td align="center">
                        1<br>
                        1<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
def snake_case(attrs=False):
    def wrapper(cls, *args, **kwargs):
        def replase_name(cls, items, key):
            setattr(cls, items, cls.__dict__[key])
            delattr(cls, key)

        def str_snake_case(item):
            def redact_str(item):
                return ''.join(map(lambda item: item[1].lower() if
                               item[0] == 0 or
                               (item[0] > 0 and item[1].lower() == item[1])
                               else f'_{item[1].lower()}', enumerate(item)))
            if item.startswith('_'):
                item = item[1:]
                _str = '_' + redact_str(item)
                return _str
            return redact_str(item)

        not_dunder_method = [method for method in cls.__dict__.keys()
                             if not method.startswith('__')]
        if attrs:
            for i in not_dunder_method:
                str_snake = str_snake_case(i)
                replase_name(cls, str_snake, i)
            return cls
        else:
            for i in not_dunder_method:
                if 'function' in str(type(cls.__dict__[i])):
                    str_snake = str_snake_case(i)
                    replase_name(cls, str_snake, i)
            return cls
    return wrapper
```
* Второй вариант решения

```python
import re
from typing import Callable


def snake_case(attrs=False):
    regex_object = re.compile(r'_?\B([A-Z])')

    def wrapper(cls, *args, **kwargs):
        class_attributes = list(cls.__dict__.keys())
        for attribute in class_attributes:
            if any((
                    attribute.startswith('__') and attribute.endswith('__'),
                    not isinstance(cls.__dict__[attribute], Callable) and not attrs
            )):
                continue
            setattr(cls, regex_object.sub(r'_\1', attribute).lower(), cls.__dict__[attribute])
            delattr(cls, attribute)
        return cls

    return wrapper
```


