<h2 style="text-align:center">Класс IPAddress</h2>

### IP-адрес — это уникальный адрес, идентифицирующий устройство в интернете или локальной сети. IP-адреса представляют собой набор из четырех целых чисел, разделенных точками. Например, 192.158.1.38. Каждое число в наборе принадлежит интервалу от 0 до 255. Таким образом, полный диапазон IP-адресации — это адреса от 0.0.0.0 до 255.255.255.255.

### Реализуйте класс IPAddress, описывающий IP-адрес. При создании экземпляра класс должен принимать один аргумент:
* ipaddress — IP-адрес, представленный в одном из следующих вариантов:
   1. строка из четырех целых чисел, разделенных точками
   2. список или кортеж из четырех целых чисел

#### Экземпляр класса IPAddress должен иметь следующее формальное строковое представление:
> IPAddress('<IP-адрес в виде четырех целых чисел, разделенных точками>')
#### И следующее неформальное строковое представление:
> <IP-адрес в виде четырех целых чисел, разделенных точками>
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса IPAddress нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">ip = IPAddress('8.8.1.1')<br>
                          print(str(ip))<br>
                          print(repr(ip))<br></td>
      <td align="center">ip = IPAddress([1, 1, 10, 10])<br>
                          print(str(ip))<br>
                          print(repr(ip))<br></td>
      <td align="center">ip = IPAddress((1, 1, 11, 11))<br>
                          print(str(ip))<br>
                          print(repr(ip))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        8.8.1.1<br>
                        IPAddress('8.8.1.1')<br>
      </td>
      <td align="center">
                        1.1.10.10<br>
                        IPAddress('1.1.10.10')<br>
      </td>
      <td align="center">
                        1.1.11.11<br>
                        IPAddress('1.1.11.11')<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, arg):
        self.ipaddress = arg

    @__init__.register(list)
    @__init__.register(tuple)
    def _(self, arg):
        self.ipaddress = '.'.join(map(str,arg))

    def __str__(self):
        return f'{self.ipaddress}'
    
    def __repr__(self) -> str:
        return f"{__class__.__name__}('{self.ipaddress}')"
```
* Второй вариант решения

```python
class IPAddress:
    def __init__(self, ipadress):
        if isinstance(ipadress, str):
            self.ipadress = ipadress
        elif isinstance(ipadress, (list, tuple)):
            self.ipadress = '.'.join(map(str, ipadress))
            
    def __str__(self):
        return self.ipadress
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.ipadress}')"
```


