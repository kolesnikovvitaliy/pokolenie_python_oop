<h2 style="text-align:center">Класс Person</h2>

### Вам доступен класс Person, описывающий человека. При создании экземпляра класс принимает два аргумента в следующем порядке:
* name — имя человека
* surname — фамилия человека
#### Экземпляр класса Person имеет два атрибута:
* name — имя человека
* surname — фамилия человека
#### Класс Person имеет одно свойство:
* fullname — свойство, доступное для чтения и записи, возвращающее полное имя человека в виде строки:
> <имя> <фамилия>

### Реализуйте свойство fullname класса Person с помощью декоратора @property.
```python
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return self.name + ' ' + self.surname

    def set_fullname(self, fullname):
        self.name, self.surname = fullname.split()

    fullname = property(get_fullname, set_fullname)
```

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
      <td align="center">person = Person('Mike', 'Pondsmith')<br>
                          print(person.name)<br>
                          print(person.surname)<br>
                          print(person.fullname)<br></td>
      <td align="center">person = Person('Mike', 'Pondsmith')<br>
                        person.name = 'Troy'<br>
                        print(person.fullname)<br></td>
      <td align="center">person = Person('Mike', 'Pondsmith')<br>
                          person.surname = 'Baker'<br>
                          print(person.fullname)<br></td>
      <td align="center">person = Person('Mike', 'Pondsmith')<br>
                        person.fullname = 'Troy Baker'<br>
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
                        Mike<br>
                        Pondsmith<br>
                        Mike Pondsmith<br>
      </td>
      <td align="center">
                        Troy Pondsmith<br>
      </td>
      <td align="center">
                        Mike Baker<br>
      </td>
      <td align="center">
                        Troy<br>
                        Baker<br>
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

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'
    
    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()
```
* Второй вариант решения

```python
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    @property
    def fullname(self):
        return self.name + ' ' + self.surname

    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()
```


