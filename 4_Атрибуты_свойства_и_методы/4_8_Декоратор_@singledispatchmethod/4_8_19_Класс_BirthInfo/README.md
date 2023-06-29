<h2 style="text-align:center">Класс BirthInfo</h2>

### Реализуйте класс BirthInfo, описывающий данные о дате рождения. При создании экземпляра класс должен принимать один аргумент:
* birth_date — дата рождения, представленная в одном из следующих вариантов:
  * экземпляр класса date
  * строка с датой в ISO формате
  * список или кортеж из трех целых чисел: года, месяца и дня

### Если дата рождения является некорректной или представлена в каком-либо другом формате, должно быть возбуждено исключение TypeError с текстом:
> Аргумент переданного типа не поддерживается
#### Экземпляр класса BirthInfo должен иметь один атрибут:
* birth_date — дата рождения в виде экземпляра класса date
#### Класс BirthInfo должен иметь одно свойство:
* age — свойство, доступное только для чтения, возвращающее текущий возраст в годах, то есть количество полных лет, прошедших с даты рождения на сегодняшний день

##### Примечание 1. Возраст в годах должен вычисляться так же, как и обычный возраст человека, то есть в день рождения его возраст увеличивается на один год.
##### Приведенный ниже код:
```python
birthinfo = BirthInfo(date(2023, 2, 26))

print(birthinfo.age)
в 2024-02-25 должен выводить:

0
в 2024-02-26 должен выводить:

1
в 2025-02-25 должен выводить:

1
 в 2025-02-26 должен выводить:

2
```



##### Примечание 2. Для проверки того, что свойство age возвращает верный возраст, мы используем собственную функцию current_age(), которая вычисляет возраст в годах на основе даты рождения и текущей даты.
##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 4. Никаких ограничений касательно реализации класса BirthInfo нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">birthinfo1 = BirthInfo('2020-09-18')<br>
                          birthinfo2 = BirthInfo(date(2010, 10, 10))<br>
                          birthinfo3 = BirthInfo([2016, 1, 1])<br>
                          print(birthinfo1.birth_date)<br>
                          print(birthinfo2.birth_date)<br>
                          print(birthinfo3.birth_date)<br></td>
      <td align="center">birthday = date(2020, 9, 18)<br>
                        today = date.today()<br>
                        birthinfo = BirthInfo(birthday)<br>
                        true_age = current_age(birthday, today)<br>
                        print(birthinfo.age == true_age)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        2020-09-18<br>
                        2010-10-10<br>
                        2016-01-01<br>
      </td>
      <td align="center">
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from functools import singledispatchmethod
from datetime import date, datetime, timedelta


class BirthInfo:
    @singledispatchmethod
    def __init__(self, arg):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def _(self, arg):
        self.birth_date = arg

    @__init__.register(str)
    def _(self, arg):
        arg = datetime.date(datetime.strptime(arg, "%Y-%m-%d"))
        self.birth_date = arg

    @__init__.register(tuple)
    @__init__.register(list)
    def _(self, arg):
        arg = datetime.date(datetime(*arg))
        self.birth_date = arg

    @property
    def age(self):
        age = datetime.date(datetime.today()) - self.birth_date
        a = int(age.days // 365.2)
        return a
```
* Второй вариант решения
from functools import singledispatchmethod
from datetime import date, datetime, timedelta


class BirthInfo:
    @singledispatchmethod
    def __init__(self, arg):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def _(self, arg):
        self.birth_date = arg

    @__init__.register(str)
    def _(self, arg):
        arg = datetime.date(datetime.strptime(arg, "%Y-%m-%d"))
        self.birth_date = arg

    @__init__.register(tuple)
    @__init__.register(list)
    def _(self, arg):
        arg = datetime.date(datetime(*arg))
        self.birth_date = arg

    @property
    def age(self):
        age = datetime.date(datetime.today()) - self.birth_date
        a = int(age.days // 365.2)
        return a
```python
from functools import singledispatchmethod
from datetime import date 


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @__init__.register(date)
    def _(self, birth_date):
        self.birth_date = birth_date
        
    @__init__.register(str)
    def _(self, birth_date):
        self.birth_date = date.fromisoformat(birth_date)
        
    @__init__.register(list)
    @__init__.register(tuple)
    def _(self, birth_date):
        self.birth_date = date(*birth_date)
    
    @property
    def age(self):
        return current_age(self.birth_date, date.today())
```


