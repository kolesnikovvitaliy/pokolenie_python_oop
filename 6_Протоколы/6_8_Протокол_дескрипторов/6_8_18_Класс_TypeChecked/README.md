<h2 style="text-align:center">Класс TypeChecked</h2>

### Реализуйте класс TypeChecked, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение атрибута принадлежит определенному типу данных. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является типом данных.
#### Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.


#### При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:
> Атрибут не найден
#### При установке или изменении значения атрибута дескриптор должен проверять, принадлежит ли это значение одному из типов, указанных при создании дескриптора. Если значение не принадлежит ни одному из типов, должно быть возбуждено исключение TypeError с текстом:
> Некорректное значение
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса TypeChecked нет, она может быть произвольной.



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
                              name = TypeChecked(str)<br>
                          student = Student()<br>
                          student.name = 'Mary'<br>
                          print(student.name)<br></td>
      <td align="center">class Student:<br>
                              name = TypeChecked(str)<br>
                          student = Student()<br>
                          try:<br>
                              print(student.name)<br>
                          except AttributeError as e:<br>
                              print(e)<br></td>
      <td align="center">class Student:<br>
                              name = TypeChecked(str)<br>
                          student = Student()<br>
                          student.name = 'Mary'<br>
                          try:<br>
                              student.name = 99<br>
                          except TypeError as e:<br>
                              print(e)<br>
                          print(student.name)<br></td>
      <td align="center">class Student:<br>
                              age = TypeChecked(int, float)<br>
                          student = Student()<br>
                          student.age = 18<br>
                          print(student.age)<br>
                          student.age = 18.5<br>
                          print(student.age)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        Mary<br>
      </td>
      <td align="center">
                        Атрибут не найден<br>
      </td>
      <td align="center">
                        Некорректное значение<br>
                        Mary<br>
      </td>
      <td align="center">
                        18<br>
                        18.5<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class TypeChecked:
    def __init__(self, *args):
        self._args = args

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if type(value) in self._args:
            obj.__dict__[self._attr] = value
        else:
            raise TypeError('Некорректное значение')
```
* Второй вариант решения

```python
class TypeChecked:
    def __init__(self, *types):
        self._types = types

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if not isinstance(value, self._types):
            raise TypeError('Некорректное значение')
        obj.__dict__[self._attr] = value
```


