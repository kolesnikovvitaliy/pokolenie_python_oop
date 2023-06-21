<h2 style="text-align:center">Класс User</h2>

### Вам доступен класс User, описывающий интернет-пользователя. При создании экземпляра класс принимает один аргумент:
* name — имя пользователя
#### Экземпляр класса User имеет два атрибута:
* name — имя пользователя
* friends — количество друзей пользователя, начальным значением является 0
#### Класс User имеет один метод экземпляра:
* add_friends() — метод, принимающий в качестве аргумента целое число n и увеличивающий количество друзей пользователя на n
#### Найдите и исправьте ошибки, допущенные при реализации метода add_friends().
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
```python
class User:
    def __init__(self, name):
        self.name = name
        self.friends = 0

    def add_friends(n):
        friends += n
```

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">user = User('Arthur')<br>
                         print(user.friends)<br></td>
      <td align="center">user = User('Timur')<br>
                         user.add_friends(2)<br>
                         user.add_friends(2)<br>
                         user.add_friends(3)<br>
                         print(user.friends)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
      0<br>
      </td>
      <td align="center">
                       7<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class User:
    def __init__(self, name):
        self.name = name
        self.friends = 0

    def add_friends(self, n):
        self.friends += n
```
* Второй вариант решения
```python
@__import__('dataclasses').dataclass
class User:
    name: str
    friends: int = 0

    def add_friends(self, n):
        self.friends += n
```


