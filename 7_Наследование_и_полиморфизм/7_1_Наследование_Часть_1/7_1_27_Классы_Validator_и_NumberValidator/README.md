<h2 style="text-align:center">Классы Validator и NumberValidator</h2>


### Реализуйте класс Validator, описывающий объект, проверяющий значение на корректность. При создании экземпляра класс должен принимать один аргумент:
* obj — произвольный объект
#### Класс Validator должен иметь один метод экземпляра:
* is_valid() — пустой метод, всегда возвращающий значение None
  
### Также реализуйте класс NumberValidator, наследника класса Validator, описывающий объект, проверяющий значение на принадлежность типу int или float. Процесс создания экземпляра класса NumberValidator должен совпадать с процессом создания экземпляра класса Validator.
#### Класс NumberValidator должен иметь один метод экземпляра:
* is_valid() — метод, возвращающий True, если значение переданное в инициализатор принадлежит типу int или float, или False в противном случае

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">print(issubclass(NumberValidator, Validator))<br></td>
      <td align="center">validator1 = Validator('beegeek')<br>
                          validator2 = Validator(1)<br>
                          validator3 = Validator(1.1)<br>
                          print(validator1.is_valid())<br>
                          print(validator2.is_valid())<br>
                          print(validator3.is_valid())<br></td>
      <td align="center">validator1 = NumberValidator('beegeek')<br>
                          validator2 = NumberValidator(1)<br>
                          validator3 = NumberValidator(1.1)<br>
                          print(validator1.is_valid())<br>
                          print(validator2.is_valid())<br>
                          print(validator3.is_valid())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
      </td>
      <td align="center">
                        None<br>
                        None<br>
                        None<br>
      </td>
      <td align="center">
                        False<br>
                        True<br>
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Validator:
    def __init__(self, obj: object):
        self._obj = obj

    def is_valid(self):
        return None


class NumberValidator(Validator):
    def __init__(self, obj):
        super().__init__(obj)

    def is_valid(self):
        return isinstance(self._obj, (int, float))
```
* Второй вариант решения

```python
class Validator:
    def __init__(self, obj):
        self._obj = obj

    def is_valid(self):
        pass


class NumberValidator(Validator):
    def is_valid(self):
        return isinstance(self._obj, (int, float))
```


