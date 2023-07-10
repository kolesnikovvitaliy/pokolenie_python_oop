<h2 style="text-align:center">Класс DateFormatter</h2>

##### Нередко в разных странах используются разные форматы дат. Рассмотрим часть из них:
<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/5_Магические методы/5_6_Вызываемые_объекты/5_6_15_Класс_DateFormatter/img/task.png" title="Git" **alt="Git">
​</div>

### Реализуйте класс DateFormatter, экземпляры которого позволяют преобразовывать даты в формат определенной страны из таблицы выше. При создании экземпляра класс должен принимать один аргумент:
* country_code — код страны
#### Экземпляр класса DateFormatter должен являться вызываемым объектом и принимать один аргумент:
* d — дата (тип date)
#### Экземпляр класса DateFormatter должен возвращать строку с датой d в формате страны с кодом country_code.

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса DateFormatter нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">ru_format = DateFormatter('ru')<br>
                          print(ru_format(date(2022, 11, 7)))<br></td>
      <td align="center">us_format = DateFormatter('us')<br>
                          print(us_format(date(2022, 11, 7)))<br></td>
      <td align="center">ca_format = DateFormatter('ca')<br>
                          print(ca_format(date(2022, 11, 7)))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        07.11.2022<br>
      </td>
      <td align="center">
                        11-07-2022<br>
      </td>
      <td align="center">
                        2022-11-07<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from datetime import date


class DateFormatter:
    def __init__(self, country_code): 
        __code = {
        "ru": "%d.%m.%Y",
        "us": "%m-%d-%Y",
        "ca": "%Y-%m-%d",
        "br": "%d/%m/%Y",
        "fr": "%d.%m.%Y",
        "pt": "%d-%m-%Y"
    }
        self.country_code = __code[country_code]

    def __call__(self, date):
        return f"{date.strftime(self.country_code)}"
```
* Второй вариант решения

```python
class DateFormatter:
    def __init__(self, country_code  ):
        self.country_code   = country_code 
    
    def __call__(self, d):
        match self.country_code:
            case 'ru' | 'fr':
                return f'{d:%d.%m.%Y}'
            case 'us':
                return f'{d:%m-%d-%Y}'
            case 'ca': 
                return f'{d:%Y-%m-%d}'
            case 'br':
                return f'{d:%d/%m/%Y}'
            case 'pt':
                return f'{d:%d-%m-%Y}'
```


