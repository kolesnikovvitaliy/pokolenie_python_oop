<h2 style="text-align:center">Класс NonKeyword</h2>


### Реализуйте класс NonKeyword, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение атрибута не является строковым ключевым словом в Python. При создании экземпляра класс должен принимать один аргумент:
* name — имя атрибута, за которым будет закреплен дескриптор
#### При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:
> Атрибут не найден
#### При установке или изменении значения атрибута дескриптор должен проверять, не является ли это значение строковым ключевым словом в Python. Если значение является строковым ключевым словом, должно быть возбуждено исключение ValueError с текстом:
* Некорректное значение

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса NonKeyword нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">class Student:<br>
                            name = NonKeyword('name')<br>
                        student = Student()<br>
                        student.name = 'Peter'<br>
                        print(student.name)<br></td>
      <td align="center">class Student:<br>
                            name = NonKeyword('name')<br>
                        student = Student()<br>
                        try:<br>
                            print(student.name)<br>
                        except AttributeError as e:<br>
                            print(e)<br></td>
      <td align="center">class Student:<br>
                              name = NonKeyword('name')<br>
                          student = Student()<br>
                          student.name = 'Peter'<br>
                          try:<br>
                              student.name = 'class'<br>
                          except ValueError as e:<br>
                              print(e)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        Peter<br>
      </td>
      <td align="center">
                        Атрибут не найден<br>
      </td>
      <td align="center">
                        Некорректное значение<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from keyword import iskeyword


class NonKeyword:
    def __init__(self, name):
        self._attr = name

    def __get__(self, obj, cls):
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if type(value) is not str or not iskeyword(value):
            obj.__dict__[self._attr] = value
        else:
            raise ValueError('Некорректное значение')
```
* Второй вариант решения

```python
from keyword import kwlist


class NonKeyword:
    def __init__(self, name):
        self._attr = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr not in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        if value in kwlist:
            raise ValueError('Некорректное значение')
        obj.__dict__[self._attr] = value
```


