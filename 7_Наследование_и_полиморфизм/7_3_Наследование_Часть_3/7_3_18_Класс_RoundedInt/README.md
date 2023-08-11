<h2 style="text-align:center">Класс RoundedInt</h2>

### Ближайшим четным числом для целого нечетного числа n будем считать n + 1, ближайшим четным числом для целого четного числа будет оно само. Аналогично ближайшим нечетным числом для целого четного числа n будем считать n + 1. ближайшим нечетным числом для целого нечетного числа будет оно само.
### Реализуйте класс RoundedInt, наследника класса int, описывающий целое число, которое во время создания автоматически округляется до ближайшего четного или нечетного числа. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* num — объект, определяющий числовое значение экземпляра класса RoundedInt
* even — булево значение, определяющее четность при округлении. Если имеет значение True, округление происходит до ближайшего четного, если False — до ближайшего нечетного. По умолчанию имеет значение True

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса RoundedInt нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">print(RoundedInt(7))<br>
                        print(RoundedInt(8))<br>
                        print(RoundedInt(7, False))<br>
                        print(RoundedInt(8, False))<br></td>
      <td align="center">roundedint1 = RoundedInt(7)<br>
                          roundedint2 = RoundedInt(7, False)<br>
                          print(roundedint1 + roundedint2)<br>
                          print(roundedint1 + 1)<br>
                          print(roundedint2 + 1)<br>
                          print(type(roundedint1))<br>
                          print(type(roundedint2))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        8<br>
                        8<br>
                        7<br>
                        9<br>
      </td>
      <td align="center">
                        15<br>
                        9<br>
                        8<br>
                        class '__main__.RoundedInt'<br>
                        class '__main__.RoundedInt'<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class RoundedInt(int):
    def __new__(cls, num, even=True):
        if even:
            if num % 2:
                num += 1
            else:
                num = num
        else:
            if num % 2:
                num = num
            else:
                num += 1
        obj = super().__new__(cls, num)
        obj.even = even
        return obj
```
* Второй вариант решения

```python
class RoundedInt(int):
    def __new__(cls, value, even=True, *args, **kwargs):
        value += (value % 2 == 1) if even else (value % 2 == 0)
        instance = super().__new__(cls, value)
        return instance
```


