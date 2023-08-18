<h2 style="text-align:center">Семья</h2>

### С помощью множественного наследования постройте иерархию из приведенных ниже четырех классов. При решении старайтесь свести дублирование кода к минимуму.

### 1. Реализуйте класс Father, описывающий отца. При создании экземпляра класс должен принимать один аргумент:

* mood — настроение, по умолчанию равняется строкеneutral
#### Экземпляр класса Father должен иметь один атрибут:

* mood — настроение
#### Класс Father должен иметь два метода экземпляра:

* greet() — метод, возвращающий строку Hello!
* be_strict() — метод, изменяющий значение атрибута mood на строку strict
### 2. Также реализуйте класс Mother, описывающий мать. При создании экземпляра класс должен принимать один аргумент:

* mood — настроение, по умолчанию равняется строке neutral
#### Экземпляр класса Mother должен иметь один атрибут:

* mood — настроение
#### Класс Mother должен иметь два метода экземпляра:

* greet() — метод, возвращающий строку Hi, honey!
* be_kind() — метод, изменяющий значение атрибута mood на строку kind
### 3. Помимо этого, реализуйте класс Daughter, описывающий дочь. При создании экземпляра класс должен принимать один аргумент:

* mood — настроение, по умолчанию равняется строке neutral
#### Экземпляр класса Daughter должен иметь один атрибут:

* mood — настроение
#### Класс Daughter должен иметь три метода экземпляра:

* greet() — метод, возвращающий строку Hi, honey!
* be_kind() — метод, изменяющий значение атрибута mood на строку kind
* be_strict() — метод, изменяющий значение атрибута mood на строку strict
### 4. Наконец, реализуйте класс Son, описывающий сына. При создании экземпляра класс должен принимать один аргумент:

* mood — настроение, по умолчанию равняется строке neutral
#### Экземпляр класса Son должен иметь один атрибут:

* mood — настроение
#### Класс Son должен иметь три метода экземпляра:

* greet() — метод, возвращающий строку Hello!
* be_kind() — метод, изменяющий значение атрибута mood на строку kind
* be_strict() — метод, изменяющий значение атрибута mood на строку strict
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

##### Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">father = Father()<br>
                          mother = Mother()<br>
                          print(father.mood)<br>
                          print(mother.mood)<br>
                          print(father.greet())<br>
                          print(mother.greet())<br></td>
      <td align="center">father = Father('happy')<br>
                        mother = Mother('unhappy')<br>
                        print(father.mood)<br>
                        print(mother.mood)<br>
                        father.be_strict()<br>
                        mother.be_kind()<br>
                        print(father.mood)<br>
                        print(mother.mood)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        neutral<br>
                        neutral<br>
                        Hello!<br>
                        Hi, honey!<br>
      </td>
      <td align="center">
                        happy<br>
                        unhappy<br>
                        strict<br>
                        kind<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Father:
    def __init__(self, mood='neutral'):
        self.mood = mood

    def greet(self):
        return 'Hello!'

    def be_strict(self):
        self.mood = 'strict'


class Mother(Father):
    def greet(self):
        return 'Hi, honey!'

    def be_kind(self):
        self.mood = 'kind'


class Daughter(Mother):
    pass


class Son(Mother, Father):
    def greet(self):
        return Father.greet(self)
```
* Второй вариант решения

```python
from abc import ABC, abstractmethod


class Family(ABC):
    def __init__(self, mood='neutral'):
        self.mood = mood

    @abstractmethod
    def greet(self):
        pass


class Father(Family):
    def greet(self):
        return 'Hello!'

    def be_strict(self):
        self.mood = 'strict'


class Mother(Family):
    def greet(self):
        return 'Hi, honey!'

    def be_kind(self):
        self.mood = 'kind'


class Daughter(Mother, Father):
    pass


class Son(Father, Mother):
    pass
```


