<h2 style="text-align:center">Класс DevelopmentTeam</h2>

### Реализуйте класс DevelopmentTeam, описывающий команду разработчиков двух уровней: junior (младший) и senior (старший). При создании экземпляра класс не должен принимать никаких аргументов.
#### Класс DevelopmentTeam должен иметь два метода экземпляра:
* add_junior() — метод, принимающий произвольное количество позиционных аргументов, каждый из которых является именем разработчика, и добавляющий их в число junior-разработчиков
* add_senior() — метод, принимающий произвольное количество позиционных аргументов, каждый из которых является именем разработчика, и добавляющий их в число senior-разработчиков
#### Экземпляр класса DevelopmentTeam должен быть итерируемым объектом, элементами которого сперва являются все его junior-разработчики, а затем — все senior-разработчики. Junior-разработчики должны быть представлены в виде кортежей:
> (<имя разработчика>, 'junior')

#### в то время как senior-разработчики — в виде кортежей:
> (<имя разработчика>, 'senior')

##### Примечание 1. Разработчики в группах должны располагаться в том порядке, в котором они были добавлены.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса DevelopmentTeam нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">beegeek = DevelopmentTeam()<br>
                        beegeek.add_junior('Timur')<br>
                        beegeek.add_junior('Arthur', 'Valery')<br>
                        beegeek.add_senior('Gvido')<br>
                        print(*beegeek, sep='\n')<br></td>
      <td align="center">beegeek = DevelopmentTeam()<br>
                          print(len(list(beegeek)))<br></td>
      <td align="center">beegeek = DevelopmentTeam()<br>
                        beegeek.add_junior('Timur')<br>
                        beegeek.add_junior('Arthur', 'Valery')<br>
                        print(*beegeek, sep='\n')<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        ('Timur', 'junior')<br>
                        ('Arthur', 'junior')<br>
                        ('Valery', 'junior')<br>
                        ('Gvido', 'senior')<br>
      </td>
      <td align="center">
                        0<br>
      </td>
      <td align="center">
                        ('Timur', 'junior')<br>
                        ('Arthur', 'junior')<br>
                        ('Valery', 'junior')<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class DevelopmentTeam:
    def __init__(self):
        self.__lst_junior = []
        self.__lst_senior = []

    def add_junior(self, *args):
        for i in args:
            self.__lst_junior.append((i, 'junior'))
        
    def add_senior(self, *args):
        for i in args:
            self.__lst_senior.append((i, 'senior'))

    def __iter__(self):
        yield from (self.__lst_junior + self.__lst_senior)
```
* Второй вариант решения

```python
class DevelopmentTeam:
    def __init__(self):
        self._seniors = []
        self._juniors = []
        
    def add_junior(self, *juniors):
        self._juniors.extend(juniors)
        
    def add_senior(self, *seniors):
        self._seniors.extend(seniors)
        
    def __iter__(self):
        for junior in self._juniors:
            yield (junior, 'junior')
        for senior in self._seniors:
            yield (senior, 'senior')
```


