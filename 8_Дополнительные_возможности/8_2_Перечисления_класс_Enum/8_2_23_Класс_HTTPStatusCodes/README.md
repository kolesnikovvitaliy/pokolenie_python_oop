<h2 style="text-align:center">Класс HTTPStatusCodes</h2>

### Коды состояния HTTP представляют собой трехзначные целые числа и используются для указания успешности конкретного HTTP запроса. Выделяют пять групп кодов состояния:

* информация (100-199)
* успех (200-299)
* перенаправление (300-399)
* ошибка клиента (400-499)
* ошибка сервера (500-599)
### Реализуйте класс HTTPStatusCodes, описывающий перечисление с  кодами состояния HTTP. Перечисление должно иметь пять элементов:

* CONTINUE — элемент со значением 100
* OK — элемент со значением 200
* USE_PROXY — элемент со значением 305
* NOT_FOUND — элемент со значением 404
* BAD_GATEWAY — элемент со значением 502
#### Элемент перечисления должен иметь два метода:

* info() — метод, возвращающий двухэлементный кортеж, содержащий имя элемента и его значение
code_class() — метод, возвращающий название группы на русском, к которой относится элемент
##### Примечание 1. Подробнее про коды состояния HTTP можно почитать по ссылке.

##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

##### Примечание 3. Никаких ограничений касательно реализации класса HTTPStatusCodes нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">print(HTTPStatusCodes.OK.info())<br>
                          print(HTTPStatusCodes.OK.code_class())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        ('OK', 200)<br>
                        успех<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from enum import Enum


class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value

    def code_class(self):
        RU_CODES = {
            'CONTINUE': 'информация',
            'OK': 'успех',
            'USE_PROXY': 'перенаправление',
            'NOT_FOUND': 'ошибка клиента',
            'BAD_GATEWAY': 'ошибка сервера'
            }
        return RU_CODES[self.name]
```
* Второй вариант решения

```python
from enum import Enum


class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value

    def code_class(self):
        groups = ('информация', 'успех', 'перенаправление', 'ошибка клиента', 'ошибка сервера')
        codes = dict(zip(HTTPStatusCodes, groups))
        return codes[self]
```


