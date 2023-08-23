<h2 style="text-align:center">Класс Seasons</h2>


### Реализуйте класс Seasons, описывающий перечисление с временами года. Перечисление должно иметь четыре элемента:

* WINTER — элемент со значением 1
* SPRING — элемент со значением 2
* SUMMER — элемент со значением 3
* FALL — элемент со значением 4
#### Элемент перечисления должен иметь один метод:
* text_value() — метод, принимающий в качестве аргумента код страны en или ru и возвращающий строковое значение элемента в зависимости от переданного аргумента. Для WINTER en и ru значениями являются winter и зима соответственно, для SPRING — spring и весна, для SUMMER — summer и лето, для FALL — fall и осень

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса Seasons нет, она может быть произвольной.



<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">print(Seasons.FALL.text_value('ru'))<br>
                          print(Seasons.FALL.text_value('en'))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        осень<br>
                        fall<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from enum import Enum


class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, item):
        match item:
            case 'ru':
                ru_seasons = ('зима', 'весна', 'лето', 'осень')
                codes = dict(zip(Seasons, ru_seasons))
                return codes[self]
            case 'en':
                en_seasons = ('winter', 'spring', 'summer', 'fall')
                codes = dict(zip(Seasons, en_seasons))
                return codes[self]
```
* Второй вариант решения

```python
from enum import Enum, auto


class Seasons(Enum):
    WINTER = auto()
    SPRING = auto()
    SUMMER = auto()
    FALL = auto()

    def text_value(self, country_code):
        seasons_translate = {
            'en': {
                self.WINTER: 'winter',
                self.SPRING: 'spring',
                self.SUMMER: 'summer',
                self.FALL: 'fall'
            },
            'ru': {
                self.WINTER: 'зима',
                self.SPRING: 'весна',
                self.SUMMER: 'лето',
                self.FALL: 'осень'
            },
        }
        return seasons_translate[country_code][self]
```


