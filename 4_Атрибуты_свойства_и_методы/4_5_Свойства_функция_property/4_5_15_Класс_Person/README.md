<h2 style="text-align:center">Класс Person</h2>

### Реализуйте класс Person, описывающий человека. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* name — имя человека
* surname — фамилия человека
#### Экземпляр класса Person должен иметь два атрибута:
* name — имя человека
* surname — фамилия человека
#### Класс Person должен иметь одно свойство:
* fullname — свойство, доступное для чтения и записи, возвращающее полное имя человека в виде строки:
> <имя> <фамилия>

##### Примечание 1. При изменении имени и/или фамилии человека должно изменяться и его полное имя. Аналогично при изменении полного имени должны изменяться имя и фамилия.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">person = Person('Меган', 'Фокс')<br>
                        print(person.name)<br>
                        print(person.surname)<br>
                        print(person.fullname)<br></td>
      <td align="center">person = Person('Меган', 'Фокс')<br>
                        person.name = 'Стефани'<br>
                        print(person.fullname)<br></td>
      <td align="center">person = Person('Алан', 'Тьюринг')<br>
                          person.surname = 'Вирт'<br>
                          print(person.fullname)<br></td>
      <td align="center">person = Person('Джон', 'Маккарти')<br>
                        person.fullname = 'Алан Тьюринг'<br>
                        print(person.name)<br>
                        print(person.surname)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                       Меган<br>
                        Фокс<br>
                        Меган Фокс<br>
      </td>
      <td align="center">
                        Стефани Фокс<br>
      </td>
      <td align="center">
                        Алан Вирт<br>
      </td>
      <td align="center">
                        Алан<br>
                        Тьюринг<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return f'{self.name} {self.surname}'

    def set_fullname(self, fullname):
        self.name, self.surname = fullname.split()

    fullname = property(get_fullname, set_fullname)
```
* Второй вариант решения

```python
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return self.name, self.surname

    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()

    @fullname.getter
    def fullname(self):
        return f'{self.name} {self.surname}'
```


