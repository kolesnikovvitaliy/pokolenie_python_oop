<h2 style="text-align:center">Функция decimal()</h2>

### Будем считать вещественным числом последовательность из одной или более цифр, которая может начинаться с необязательного символа дефиса -, а также содержать на любой позиции одну десятичную точку ., кроме случая, когда точка стоит перед символом дефиса.
#### Реализуйте функцию is_decimal(), которая принимает один аргумент:
* string — строка, содержащая произвольный набор символов


#### Функция должна возвращать True, если строка string представляет собой целое или вещественное число, или False в противном случае.




<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3:</th>
    </tr>
    <tr>
      <td align="center">print(is_decimal('100'))</td>
      <td align="center">print(is_decimal('199.1'))</td>
      <td align="center">print(is_decimal('.-95'))</td>
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
import re


def is_decimal(string: str) -> bool:
    regex_obj = re.compile(r'-?\.?\d+\.\d+')
    try:
        return bool(float(string))
    except:
        return bool(regex_obj.fullmatch(string))
```
* Второй вариант решения
```python
# import re

# def is_decimal(n):
#     return bool(re.search(r'^-?(?:\d+\.?\d*|\d*\.?\d+)$', n))
```


