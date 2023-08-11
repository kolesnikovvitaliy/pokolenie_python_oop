<h2 style="text-align:center">Класс LowerString</h2>

### Реализуйте класс LowerString, наследника класса str, описывающий строку, которая во время создания автоматически переводится в нижний регистр. При создании экземпляра класс должен принимать один аргумент:
* obj — объект, определяющий начальное значение строки. Может быть не передан, в таком случае начальное значение считается пустой строкой
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса LowerString нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">s1 = LowerString('BEEGEEK')<br>
                          s2 = LowerString('BeeGeek')<br>
                          print(s1)<br>
                          print(s2)<br>
                          print(s1 == s2)<br>
                          print(issubclass(LowerString, str))<br></td>
      <td align="center">print(LowerString(['Bee', 'Geek']))<br>
                          print(LowerString({'A': 1, 'B': 2, 'C': 3}))<br></td>
      <td align="center">s = LowerString('BeeGeek')<br>
                          print(s[0], s[3])<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        beegeek<br>
                        beegeek<br>
                        True<br>
                        True<br>
      </td>
      <td align="center">
                        ['bee', 'geek']<br>
                        {'a': 1, 'b': 2, 'c': 3}<br>
      </td>
      <td align="center">
                        b g<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class LowerString(str):
    def __new__(cls, obj=''):
        obj = super().__new__(cls, str(obj).lower())
        return obj
```
* Второй вариант решения

```python
class LowerString(str):
    def __new__(cls, obj=''):
        return super().__new__(cls, str(obj).lower())
```


