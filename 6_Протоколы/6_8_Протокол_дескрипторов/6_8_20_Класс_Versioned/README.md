<h2 style="text-align:center">Класс Versioned</h2>

### Реализуйте класс Versioned, описывающий дескриптор, предоставляющий доступ как к текущему значению атрибута, так и ко всем предыдущим, если значение атрибута когда-либо изменялось. При создании экземпляра класс не должен принимать никаких аргументов.
#### Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.
#### При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:
> Атрибут не найден
#### При установке или изменении значения атрибута дескриптор должен устанавливать или изменять это значение без каких-либо дополнительных проверок.
#### Класс Versioned должен иметь два метода экземпляра:
* get_version() — метод, принимающий два аргумента: экземпляр класса, в котором определен дескриптор, и целое число n. Метод должен возвращать n-ое по счету значение атрибута этого экземпляра класса. Например, если значение атрибута было установлено, а затем изменено, то метод get_version() должен уметь вернуть как установленное значение (первое по счету), так и измененное (второе по счету)
* set_version() — метод, принимающий два аргумента: экземпляр класса, в котором определен дескриптор, и целое число n. Метод должен устанавливать n-ое по счету значение атрибута в качестве текущего

##### Примечание 1. Вызов метода set_version() не должен приравниваться к изменению значения атрибута. Будем считать, что атрибут изменяет свое значение только в том случае, если эта операция выполняется через точечную нотацию или функцию setattr().
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса Versioned нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">class Student:<br>
                              age = Versioned()<br>
                          student = Student()<br>
                          student.age = 18<br>
                          student.age = 19<br>
                          print(student.age)<br></td>
      <td align="center">class Student:<br>
                              age = Versioned()<br>
                          student = Student()<br>
                          student.age = 18<br>
                          student.age = 19<br>
                          student.age = 20<br>
                          print(student.age)<br>
                          print(Student.age.get_version(student, 1))<br>
                          print(Student.age.get_version(student, 2))<br>
                          print(Student.age.get_version(student, 3))<br></td>
      <td align="center">class Student:<br>
                              age = Versioned()<br>
                          student = Student()<br>
                          student.age = 18<br>
                          student.age = 19<br>
                          student.age = 20<br>
                          print(student.age)<br>
                          Student.age.set_version(student, 1)<br>
                          print(student.age)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        19<br>
      </td>
      <td align="center">
                        20<br>
                        18<br>
                        19<br>
                        20<br>
      </td>
      <td align="center">
                        20<br>
                        18<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Versioned:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr][-1]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        obj.__dict__.setdefault(self._attr, []).append(value)

    def get_version(self, obj, n: int):
        return obj.__dict__[self._attr][n-1]

    def set_version(self, obj, n: int):
        obj.__dict__[self._attr].append(obj.__dict__[self._attr][n-1])
```
* Второй вариант решения

```python
class Versioned:
    def __init__(self):
        self._index = -1

    def __set_name__(self, owner, name):
        self._attr = name

    def __get__(self, obj, owner):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr][self._index]
        raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if self._attr not in obj.__dict__:
            obj.__dict__[self._attr] = []
        obj.__dict__[self._attr].append(value)

    def get_version(self, obj, n):
        return obj.__dict__[self._attr][n - 1]

    def set_version(self, obj, n):
        self._index = n - 1
```


