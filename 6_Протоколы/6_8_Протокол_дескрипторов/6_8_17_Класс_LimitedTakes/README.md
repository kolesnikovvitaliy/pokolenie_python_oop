<h2 style="text-align:center">Класс LimitedTakes</h2>

### Реализуйте класс LimitedTakes, описывающий дескриптор, который позволяет получать значение атрибута лишь определенное количество раз. При создании экземпляра класс должен принимать один аргумент:
* times — количество доступных обращений к атрибуту
#### Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.

#### При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:
> Атрибут не найден
#### Если к атрибуту было выполнено times обращений, во время всех последующих обращений должно возбуждаться исключение MaxCallsException с текстом:
> Превышено количество доступных обращений
#### При установке или изменении значения атрибута дескриптор должен устанавливать или изменять это значение без каких-либо дополнительных проверок.
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса LimitedTakes нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">class Student:<br>
                              name = LimitedTakes(3)<br>
                          student = Student()<br>
                          student.name = 'Gwen'<br>
                          print(student.name)<br>
                          print(student.name)<br>
                          print(student.name)<br>
                          try:<br>
                              print(student.name)<br>
                          except MaxCallsException as e:<br>
                              print(e)<br></td>
      <td align="center">class Student:<br>
                              name = LimitedTakes(3)<br>
                          student = Student()<br>
                          for _ in range(100):<br>
                              student.name = 'Gwen'<br>
                          print(student.name)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Gwen<br>
                        Gwen<br>
                        Gwen<br>
                        Превышено количество доступных обращений<br>
      </td>
      <td align="center">
                        Gwen<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class MaxCallsException(Exception):...


class LimitedTakes:
    def __init__(self, times):
        self._times = times

    def __set_name__(self, cls, attr):
        self._name = attr

    def __get__(self, obj, cls):
        if self._times > 0:
            if self._name in obj.__dict__:
                self._times -= 1
                return obj.__dict__[self._name]
            raise AttributeError('Атрибут не найден')
        raise MaxCallsException('Превышено количество доступных обращений')

    def __set__(self, obj, value):
        obj.__dict__[self._name] = value
```
* Второй вариант решения

```python
class MaxCallsException(Exception):
    def __init__(self, message='Превышено количество доступных обращений'):
        super().__init__(message)


class LimitedTakes:
    def __init__(self, times):
        self.times = times
        self.calls = 0

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if self._name in instance.__dict__:
            if self.calls < self.times:
                self.calls += 1
                return instance.__dict__[self._name]
            raise MaxCallsException
        raise AttributeError('Атрибут не найден')

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value
```


