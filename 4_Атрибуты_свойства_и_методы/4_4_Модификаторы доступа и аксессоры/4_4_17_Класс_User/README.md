<h2 style="text-align:center">Класс User</h2>

### Реализуйте класс User, описывающий интернет-пользователя. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* name — имя пользователя. Если name не является непустой строкой, состоящей только из букв, должно быть возбуждено исключение ValueError с текстом:
> Некорректное имя
* age — возраст пользователя. Если age не является целым числом, принадлежащим отрезку [0; 110], должно быть возбуждено исключение ValueError с текстом:
> Некорректный возраст
#### Экземпляр класса User должен иметь два атрибута:
* _name — имя пользователя
* _age — возраст пользователя
#### Класс User должен иметь четыре метода экземпляра:
* get_name() — метод, возвращающий имя пользователя
* set_name() — метод, принимающий в качестве аргумента значение new_name и изменяющий имя пользователя на new_name. Если new_name не является непустой строкой, состоящей только из букв, должно быть возбуждено исключение ValueError с текстом:
> Некорректное имя

* get_age() — метод, возвращающий возраст пользователя
* set_age() — метод, принимающий в качестве аргумента значение new_age и изменяющий возраст пользователя на new_age. Если new_age не является целым числом, принадлежащим отрезку [0; 110], должно быть возбуждено исключение ValueError с текстом:
> Некорректный возраст



##### Примечание 1. Если при создании экземпляра класса User имя и возраст одновременно являются некорректными, должно быть возбуждено исключение, связанное с именем.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">user = User('Гвидо', 67)<br>
                            print(user.get_name())<br>
                            print(user.get_age())<br></td>
      <td align="center">user = User('Гвидо', 67)<br>
                            user.set_name('Тимур')<br>
                            user.set_age(30)<br>
                            print(user.get_name())<br>
                            print(user.get_age())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Гвидо<br>
                            67<br>
      </td>
      <td align="center">
                        Тимур<br>
                            30<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class User:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        self._name = self.get_name()
        self._age = self.get_age()

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if (not isinstance(new_name, str) or not new_name.isalpha()):
            raise ValueError('Некорректное имя')
        self._name = new_name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age not in range(0,111):
            raise ValueError('Некорректный возраст')
        self._age = new_age
```
* Второй вариант решения

```python
class User:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def set_name(self, name):
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')
    
    def set_age(self, age):
        if isinstance(age, int) and 0 <= age <= 100:
            self._age = age
        else:
            raise ValueError('Некорректный возраст')
   
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

```


