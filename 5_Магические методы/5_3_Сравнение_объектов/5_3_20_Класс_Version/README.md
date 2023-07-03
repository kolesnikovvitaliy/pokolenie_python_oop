<h2 style="text-align:center">Класс Version</h2>

### Реализуйте класс Version, описывающий версию программного обеспечения. При создании экземпляра класс должен принимать один аргумент:
* version — строка из трех целых чисел, разделенных точками и описывающих версию ПО. Например, 2.8.1. Если одно из чисел не указано, оно считается равным нулю. Например, версия 2 равнозначна версии 2.0.0, а версия 2.8 равнозначна версии 2.8.0
#### Экземпляр класса Version должен иметь следующее формальное строковое представление:
> Version('<версия ПО в виде трех целых чисел, разделенных точками>')
#### И следующее неформальное строковое представление:
> <версия ПО в виде трех целых чисел, разделенных точками>

##### Также экземпляры класса Version должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=. Два Version объекта считаются равными, если все три числа в их версиях совпадают. Version объект считается больше другогоVersion объекта, если первое число в его версии больше. Или если второе число в его версии больше, если первые числа совпадают. Или если третье число в его версии больше, если первые и вторые числа совпадают.
##### Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса Version нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">print(Version('3.0.3') == Version('1.11.28'))<br>
                          print(Version('3.0.3') < Version('1.11.28'))<br>
                          print(Version('3.0.3') > Version('1.11.28'))<br>
                          print(Version('3.0.3') <= Version('1.11.28'))<br>
                          print(Version('3.0.3') >= Version('1.11.28'))<br></td>
      <td align="center">print(Version('3') == Version('3.0'))<br>
                          print(Version('3') == Version('3.0.0'))<br>
                          print(Version('3.0') == Version('3.0.0'))<br></td>
      <td align="center">versions = [Version('2'), Version('2.1'), Version('1.9.1')]<br>
                          print(sorted(versions))<br>
                          print(min(versions))<br>
                          print(max(versions))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        False<br>
                        False<br>
                        True<br>
                        False<br>
                        True<br>
      </td>
      <td align="center">
                        True<br>
                          True<br>
                          True<br>
      </td>
      <td align="center">
                        [Version('1.9.1'), Version('2.0.0'), Version('2.1.0')]<br>
                        1.9.1<br>
                        2.1.0<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version: str) -> str or bool:
        self.version = {0: '0', 1: '0', 2: '0'}
        for i in {enumerate(version.split('.'))}:
            self.version.update(i)
        self.version = '.'.join(map(lambda x: self.version[x], self.version))
        
    def __str__(self) -> str:
        return f'{self.version}'
    
    def __repr__(self) -> str:
        return f"{__class__.__name__}({repr(self.version)})"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Version):
            return self.version == __value.version
        return NotImplemented
        
    def __lt__(self, __value: object) -> bool:
        if isinstance(__value, Version):
            return list(map(int,self.version.split('.'))) < list(map(int, __value.version.split('.')))
        return NotImplemented
```
* Второй вариант решения

```python
from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version):
        self._parts = [int(i) for i in version.split('.')]
        self._parts += [0] * (3 - len(self._parts))

    def __str__(self):
        return '{}.{}.{}'.format(*self._parts)
    
    def __repr__(self):
        return "Version('{}.{}.{}')".format(*self._parts)
    
    def __eq__(self, other):
        if isinstance(other, Version):
            return self._parts == other._parts
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Version):
            return self._parts < other._parts
        return NotImplemented
```


