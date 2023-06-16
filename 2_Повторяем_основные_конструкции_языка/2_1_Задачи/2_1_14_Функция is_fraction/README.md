<h2 style="text-align:center">Функция is_fraction()</h2>

### Будем считать обыкновенной дробью последовательность из одной или более цифр, за которой следует прямая косая черта /, а затем — последовательность из одной или более цифр, хотя бы одна из которых отлична от нуля (знаменатель не может равняться нулю). Последовательность, представляющая собой обыкновенную дробь, может начинаться с необязательного символа дефиса -.


#### Реализуйте функцию is_fraction(), которая принимает один аргумент:
* string — строка, содержащая произвольный набор символов


#### ФФункция должна возвращать True, если строка string представляет собой обыкновенную дробь, или False в противном случае.




<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3:</th>
    </tr>
    <tr>
      <td align="center">print(is_fraction('-54/9'))</td>
      <td align="center">print(is_fraction('71'))</td>
      <td align="center">print(is_fraction('1 / 82'))</td>
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
      False<br>
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
def is_fraction(string: str) -> bool:
    regex_obj = re.compile(r'-?[0-9]+/0*[1-9]\d*')
    return bool(regex_obj.fullmatch(string))
```
* Второй вариант решения
```python
def is_fraction(string):
    regex = r'^-?\d+/[1-9]\d*$'
    rez = bool(__import__('re').fullmatch(regex, string))
    return rez
```


