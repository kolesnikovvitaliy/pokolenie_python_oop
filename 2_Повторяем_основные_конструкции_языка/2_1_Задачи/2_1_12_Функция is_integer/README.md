<h2 style="text-align:center">Функция is_integer()</h2>

### Целым числом будем считать последовательность из одной или более цифр, которая может начинаться с необязательного символа дефиса -.
#### Реализуйте функцию is_integer(), которая принимает один аргумент:
* string — строка, содержащая произвольный набор символов


#### Функция должна возвращать True, если строка string представляет собой целое число, или False в противном случае.


<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3:</th>
    </tr>
    <tr>
      <td align="center">print(is_integer('5.0'))</td>
      <td align="center">print(is_integer('-43'))</td>
      <td align="center">print(is_integer('5f'))</td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
    </tr>
    <tr>
      <td align="center">
      False<br>
      </td>
      <td align="center">
      True<br>
      </td>
      <td align="center">
      False<br>
      </td>
    </tr>
  </tbody>
</table>

## Примеры решений:
* Первый вариант решения
```python
def is_integer(string):
    try:
        return bool(int(string))
    except:
        return False

# print(is_integer('-0001'))
# print(is_integer('0001'))
```
* Второй вариант решения
```python
import re


def is_integer(string: str) -> bool:
    regex_obj = re.compile(r'-?\d+')
    return bool(regex_obj.fullmatch(string))
```


