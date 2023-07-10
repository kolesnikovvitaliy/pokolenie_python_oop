<h2 style="text-align:center">Класс RaiseTo</h2>

### Реализуйте класс RaiseTo, экземпляры которого позволяют возводить числа в фиксированную степень. При создании экземпляра класс должен принимать один аргумент:
* degree — показатель степени
#### Экземпляр класса RaiseTo должен являться вызываемым объектом и принимать один аргумент:
* x — число
#### Экземпляр класса RaiseTo должен возвращать значение x в степени degree.
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса RaiseTo нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">raise_to_two = RaiseTo(2)<br>
                        print(raise_to_two(2))<br>
                        print(raise_to_two(3))<br>
                        print(raise_to_two(4))<br></td>
      <td align="center">raise_to_three = RaiseTo(3)<br>
                        raise_to_four = RaiseTo(4)<br>
                        print(raise_to_three(3))<br>
                        print(raise_to_four(2))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        4<br>
                        9<br>
                        16<br>
      </td>
      <td align="center">
                        27<br>
                        16<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class  RaiseTo:
    def __init__(self, degree: int):
        self.degree = degree

    def __call__(self, x: int):
        return x**self.degree
```
* Второй вариант решения

```python
class RaiseTo:
    def __init__(self, degree):
        self.degree = degree
        
    def __call__(self, x):
        return x ** self.degree
```


