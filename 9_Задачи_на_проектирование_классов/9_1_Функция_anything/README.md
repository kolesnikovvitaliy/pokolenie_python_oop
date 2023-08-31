<h2 style="text-align:center">Функция anything()</h2>

### Реализуйте функцию anything(), которая возвращает такой объект, результат сравнения с которым c помощью операторов ==, !=, >, <, >= и <= всегда равен True.

##### Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию anything(), но не код, вызывающий ее.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">import math, re<br>
                          print(anything() != [])<br>
                          print(anything() < 'World')<br>
                          print(anything() > 81)<br>
                          print(anything() >= re)<br>
                          print(anything() <= math)<br>
                          print(anything() == ord)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
                        True<br>
                        True<br>
                        True<br>
                        True<br>
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class AllTrue:
    def __eq__(self, __value): return True
    def __ne__(self, __value): return True
    def __lt__(self, __value): return True
    def __gt__(self, __value): return True
    def __le__(self, __value): return True
    def __ge__(self, __value): return True


def anything():
    return AllTrue()
```
* Второй вариант решения

```python
class AlwaysTrue:
    def __eq__(self, other):
        return True

    __ne__ = __lt__ = __le__ = __gt__ = __ge__ = __eq__


def anything():
    return AlwaysTrue()
```


