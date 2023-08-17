<h2 style="text-align:center">Функции is_iterator() и is_iterable()</h2>

### 1. Реализуйте функцию is_iterable(), которая принимает один аргумент:
* obj — произвольный объект
#### Функция должна возвращать True, если объект obj является итерируемым объектом, или False в противном случае.
### 2. Также реализуйте функцию is_iterator(), которая принимает один аргумент:
* obj — произвольный объект
#### Функция должна возвращать True, если объект obj является итератором, или False в противном случае.

##### Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимые функции, но не код, вызывающий их.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">print(is_iterable(123))<br>
                        print(is_iterable([1, 2, 3]))<br>
                        print(is_iterable((1, 2, 3)))<br>
                        print(is_iterable('123'))<br>
                        print(is_iterable(iter('123')))<br>
                        print(is_iterable(map(int, '123')))<br></td>
      <td align="center">print(is_iterator(123))<br>
                          print(is_iterator([1, 2, 3]))<br>
                          print(is_iterator((1, 2, 3)))<br>
                          print(is_iterator('123'))<br>
                          print(is_iterator(iter('123')))<br>
                          print(is_iterator(map(int, '123')))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        False<br>
                        True<br>
                        True<br>
                        True<br>
                        True<br>
                        True<br>
      </td>
      <td align="center">
                        False<br>
                        False<br>
                        False<br>
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
from collections.abc import Iterable, Iterator


def is_iterable(obj):
    return isinstance(obj, Iterable)


def is_iterator(obj):
    return isinstance(obj, Iterator)
```
* Второй вариант решения

```python
from collections.abc import Iterable, Iterator

is_iterable = lambda obj: isinstance(obj, Iterable)
is_iterator = lambda obj: isinstance(obj, Iterator)
```


