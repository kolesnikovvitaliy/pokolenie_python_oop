<h2 style="text-align:center">Класс PhoneNumber</h2>


### Реализуйте класс PhoneNumber, описывающий телефонный номер. При создании экземпляра класс должен принимать один аргумент:
* phone_number — телефонный номер, представляющий строку из десяти цифр в одном из следующих форматов:
    1. >dddddddddd
    2. > ddd ddd dddd
#### Экземпляр класса PhoneNumber должен иметь следующее формальное строковое представление:
> PhoneNumber('<телефонный номер в формате dddddddddd>')
#### И следующее неформальное строковое представление:
> <телефонный номер в формате (ddd) ddd-dddd>
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса PhoneNumber нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">phone = PhoneNumber('9173963385')<br>
                          print(str(phone))<br>
                          print(repr(phone))<br></td>
      <td align="center">phone = PhoneNumber('918 396 3389')<br>
                          print(str(phone))<br>
                          print(repr(phone))<br></td>
      <td align="center">phone1 = PhoneNumber('9173963385')<br>
                          phone2 = PhoneNumber('918 396 3389')<br>
                          phone3 = PhoneNumber('919 333 3344')<br>
                          print(phone1, phone2, phone3, sep=', ')<br>
                          print([phone1, phone2, phone3])<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        (917) 396-3385<br>
                        PhoneNumber('9173963385')<br>
      </td>
      <td align="center">
                        (918) 396-3389<br>
                        PhoneNumber('9183963389')<br>
      </td>
      <td align="center">
                        (917) 396-3385, (918) 396-3389, (919) 333-3344<br>
                        [PhoneNumber('9173963385'), PhoneNumber('9183963389'), PhoneNumber('9193333344')]<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class PhoneNumber:
    def __init__(self, arg):
        if ' ' in arg:
            self.phone_number = ''.join(map(lambda x: x if x != ' ' else '',arg))
        else:
            self.phone_number = arg


    def __str__(self) -> str:
        return f'({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}'
    
    def __repr__(self):
        return f"{__class__.__name__}('{self.phone_number}')"
```
* Второй вариант решения

```python
class PhoneNumber:
    def __init__(self, phone_number):
        self.phone_number = phone_number.replace(' ', '')

    def __str__(self):
        return f'({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}'

    def __repr__(self):
        return f"PhoneNumber('{self.phone_number}')"
```


