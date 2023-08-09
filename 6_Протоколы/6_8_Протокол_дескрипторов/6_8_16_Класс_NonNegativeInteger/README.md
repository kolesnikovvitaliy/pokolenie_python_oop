<h2 style="text-align:center">Класс NonNegativeInteger</h2>


### Реализуйте класс NonNegativeInteger, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение атрибута является неотрицательным целым числом. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* name — имя атрибута, за которым будет закреплен дескриптор
* default — значение по умолчанию. Если не передан, имеет значение None

#### При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение не установлено, должно возвращаться значение по умолчанию, указанное при создании дескриптора. Если значение по умолчанию равняется None, должно быть возбуждено исключение AttributeError с текстом:
> Атрибут не найден
#### При установке или изменении значения атрибута дескриптор должен проверять, является ли это значение неотрицательным целым числом. Если значение не является неотрицательным целым числом, должно быть возбуждено исключение ValueError с текстом:
> Некорректное значение

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса NonNegativeInteger нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">class Student:<br>
                              score = NonNegativeInteger('score')<br>
                          student = Student()<br>
                          student.score = 90<br>
                          print(student.score)<br></td>
      <td align="center">class Student:<br>
                              score = NonNegativeInteger('score', 0)<br>
                          student = Student()<br>
                          print(student.score)<br>
                          student.score = 0<br>
                          print(student.score)<br></td>
      <td align="center">class Student:<br>
                              score = NonNegativeInteger('score')<br>
                          student = Student()<br>
                          try:<br>
                              print(student.score)<br>
                          except AttributeError as e:<br>
                              print(e)<br></td>
      <td align="center">class Student:<br>
                              score = NonNegativeInteger('score')<br>
                          student = Student()<br>
                          try:<br>
                              student.score = -90<br>
                          except ValueError as e:<br>
                              print(e)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        90<br>
      </td>
      <td align="center">
                        0<br>
                        0<br>
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
class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._attr = name
        self._default = default

    def __get__(self, obj, cls):
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            if self._default is not None:
                return self._default
        raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if isinstance(value, int) and value >= 0:
            obj.__dict__[self._attr] = value
        else:
            raise ValueError('Некорректное значение')
```
* Второй вариант решения

```python
class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._attr = name
        self._default = default

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr not in obj.__dict__ and self._default is None:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__.get(self._attr, self._default)

    def __set__(self, obj, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError('Некорректное значение')
        obj.__dict__[self._attr] = value
```


