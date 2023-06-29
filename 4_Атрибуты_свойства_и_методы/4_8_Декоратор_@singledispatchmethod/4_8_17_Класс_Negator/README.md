<h2 style="text-align:center">Класс Negator</h2>


### Реализуйте класс Negator. При создании экземпляра класс не должен принимать никаких аргументов.

#### Класс Negator должен иметь один статический метод:
* neg() — метод, принимающий в качестве аргумента объект и возвращающий его противоположное значение. Если методу передается целое или вещественное число, он должен возвращать это число, взятое с противоположным знаком. Если методу в качестве аргумента передается булево значение, он должен возвращать булево значение, противоположное переданному. Если переданный объект принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:
> Аргумент переданного типа не поддерживается
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса Negator нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">print(Negator.neg(11.0))<br>
                          print(Negator.neg(-12))<br>
                          print(Negator.neg(True))<br>
                          print(Negator.neg(False))<br></td>
      <td align="center">try:<br>
                              Negator.neg('number')<br>
                          except TypeError as e:<br>
                              print(e)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        -11.0<br>
                          12<br>
                          False<br>
                          True<br>
      </td>
      <td align="center">
                        Аргумент переданного типа не поддерживается<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _int_neg(data):
        return -data
    
    @neg.register(bool)
    @staticmethod
    def _bool_neg(data):
        return not data
```
* Второй вариант решения

```python
from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _int_neg(data):
        return arg * (-1)
    
    @neg.register(bool)
    @staticmethod
    def _bool_neg(data):
        return bool([1, 0][data])
```


